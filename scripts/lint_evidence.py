"""Structural linter for Stage-A evidence packets (DEC-0012).

This tool verifies that a Stage-A evidence packet **carries the research
instruments the protocol requires**, and that the packet's own
machine-readable ledgers are internally consistent. It is deliberately a
*structural* checker:

    It does NOT decide whether the rules research is factually correct.
    It does NOT read the Rules Cyclopedia.
    It does NOT judge interpretation, ownership or mechanical synthesis.

Those remain the job of the adversarial self-review
(`RULE_CARD_RESEARCH_PROTOCOL.md` §10.1.1), the independent completeness
review (§10.1.2) and human evidence review (§11). What this linter
replaces is the part of the five `CLUSTER-004` review cycles that was
spent finding *bookkeeping* defects a machine can find in milliseconds:
a page carrying an evidence row that appears on no visual-inspection
list, an absence claim with no Negative Claim Record behind it, a
`BLOCKED` closure item sitting in a packet that recommends
`EVIDENCE READY FOR HUMAN REVIEW`, a §17 hard-stop string used as an
inline label.

Every check below is traceable to a concrete, recorded `CLUSTER-004`
review finding (see `docs/decisions/DEC-0012-*.md` §"Check-to-failure
map"). Checks were not added speculatively.

Scope: `docs/rules/evidence/<RULE-ID>-evidence*.md` — Stage-A packets, as
named by §12. Reviewer artifacts (completeness reviews, audits,
gap-research records) are not packets and are not linted. Packets that
predate DEC-0012 are grandfathered by explicit name (§"Grandfathering").

Usage:

    uv run python scripts/lint_evidence.py [<evidence-directory>]

With no argument it lints the repository's own `docs/rules/evidence/`. A
directory argument is used by the tests to exercise this gate end to end.

Exits 0 if every linted packet passes, 1 otherwise, printing the exact
packet, check ID and reason for each failure.
"""

from __future__ import annotations

import re
import sys
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = REPO_ROOT / "docs" / "rules" / "evidence"

# A Stage-A packet, per RULE_CARD_RESEARCH_PROTOCOL.md §12's naming
# convention. Reviewer artifacts do not match this shape by design.
PACKET_GLOB = "*-evidence*.md"

# The canonical Stage-A packet template (§11.2) is linted as a **reference
# packet** on every run. Two reasons, both load-bearing:
#
#   1. It keeps this gate LIVE. Every real packet in the repository today is
#      grandfathered, so without the reference packet the gate would lint
#      zero files and pass vacuously -- a green check proving nothing. A
#      structurally inert gate is worse than no gate, because it is
#      mistaken for enforcement.
#   2. The template is the artifact every future packet is copied from. If
#      an edit makes it non-conformant, every packet started from it
#      inherits that defect, so the template is exactly what a continuous
#      check should protect.
#
# Its absence is itself a failure: §11.2 requires it to exist.
REFERENCE_PACKET = "_TEMPLATE.md"

# Grandfathering (DEC-0012 consequence 7). Every Stage-A packet that
# existed when DEC-0012 was adopted is exempt: those packets were
# researched, reviewed and (for CLUSTER-004) independently certified
# under the protocol as it then stood, and retro-fitting the new ledgers
# to them would rewrite accepted evidence rather than improve it.
#
# This list is CLOSED. A packet written after DEC-0012 is never added to
# it -- tests/tooling/test_lint_evidence.py pins the exact membership, so
# extending it requires changing a test and is therefore visible in
# review rather than silent.
GRANDFATHERED: frozenset[str] = frozenset(
    {
        "CHAR-001-evidence.md",
        "CHAR-002-evidence.md",
        "CHAR-003-evidence.md",
        "CHAR-004-evidence.md",
        "CHAR-005-evidence.md",
        "CHAR-007-evidence.md",
        "ENC-005-evidence.md",
        "ENC-005-evidence-remediated.md",
        "EXP-001-evidence.md",
        "EXP-003-evidence.md",
        "EXP-006-evidence.md",
        "EXP-006-evidence-remediated.md",
    }
)

# --- The required packet sections (DEC-0012 item 3; protocol §11.2) -------
#
# Matched as a case-insensitive substring of a Markdown heading line, so
# section numbering and trailing qualifiers stay free-form.
REQUIRED_SECTIONS: tuple[str, ...] = (
    "Research-Start Gate",
    "Primary Source Accessed",
    "Source Structure",
    "Coverage Manifest",
    "Index Enumeration",
    "Governing Objects",
    "Visual Inspection Record",
    "Cross-Reference Ledger",
    "Repository-Fact Verification",
    "Evidence Map",
    "Negative Claim Ledger",
    "Ownership and Dependency Routing",
    "Falsification Pass",
    "Open-Question Closure",
    "Primary-Source Coverage Checklist",
    "Independent Review Status",
)

# --- Controlled vocabularies ---------------------------------------------

# §6 confidence vocabulary, plus the repository-fact label DEC-0012 adds
# (review 5 Finding 8: a project fact is not a source claim, and none of
# §6's five labels fits one).
CONFIDENCE_LABELS: frozenset[str] = frozenset(
    {
        "DIRECT PRIMARY TEXT",
        "PRIMARY TEXT + CROSS-REFERENCE CONFIRMED",
        "NECESSARY CONSEQUENCE",
        "SECONDARY SOURCE LOCATOR ONLY",
        "NOT YET VERIFIED",
        # Added by DEC-0012. A negative claim whose enumeration is not yet
        # complete is classified NOT YET ESTABLISHED rather than reported
        # as source silence (§10.4); a project fact is not a source claim
        # at all, and none of §6's five labels fits one (review 5
        # Finding 8).
        "NOT YET ESTABLISHED",
        "REPOSITORY FACT — NOT A SOURCE CLAIM",
    }
)

# §10.2 open-question closure dispositions.
CLOSURE_DISPOSITIONS: frozenset[str] = frozenset(
    {
        "RESOLVED BY SOURCE INSPECTION",
        "CONFIRMED OUT OF SCOPE",
        "RETAINED AS GENUINE SOURCE AMBIGUITY",
        "BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED",
    }
)

BLOCKED_DISPOSITION = "BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED"

EVIDENCE_READY = "EVIDENCE READY FOR HUMAN REVIEW"
MORE_RESEARCH_REQUIRED = "MORE PRIMARY RESEARCH REQUIRED"
RECOMMENDATIONS: frozenset[str] = frozenset({EVIDENCE_READY, MORE_RESEARCH_REQUIRED})

# §10.1.2: what an original researcher may and may not write as its own
# packet's review status.
PREPARED = "PREPARED FOR INDEPENDENT COMPLETENESS REVIEW"
INDEPENDENT_REVIEW_STATES: frozenset[str] = frozenset(
    {
        PREPARED,
        "INDEPENDENT COMPLETENESS REVIEW PASSED",
        "INDEPENDENT COMPLETENESS REVIEW FAILED",
    }
)
PROHIBITED_SELF_CERTIFICATIONS: tuple[str, ...] = (
    "SOURCE COMPLETENESS PASSED",
    "SOURCE COMPLETENESS CERTIFIED",
    "HUMAN EVIDENCE GATE CLEARED",
)

# The keys whose *value* carries a review verdict. A prohibited string is a
# self-certification when assigned to one of these, and ordinary prose when
# it appears anywhere else -- a packet may name these strings to warn
# against them.
REVIEW_STATUS_KEYS: frozenset[str] = frozenset(
    {
        "INDEPENDENT-REVIEW",
        "INDEPENDENT REVIEW",
        "ORIGINAL RESEARCHER OUTPUT",
        "HUMAN EVIDENCE REVIEW",
        "SOURCE COMPLETENESS",
        "STATUS",
    }
)

# §17 hard-stop bodies. Each must always carry its "STOP — " prefix; used
# bare, the string reads as a live hard stop (review 4 Finding 6).
HARD_STOP_BODIES: tuple[str, ...] = (
    "PRIMARY SOURCE ACCESS REQUIRED",
    "PRIMARY-SOURCE VISUAL ACCESS REQUIRED",
    "PRIMARY PROCEDURE NOT YET ESTABLISHED",
    "INTERNAL SOURCE CONFLICT REQUIRES REVIEW",
    "MORE PRIMARY RESEARCH REQUIRED",
    "COMPLETION COMPATIBILITY NOT ESTABLISHED",
    "HUMAN RULING REQUIRED",
)

# E015 checks that a stop body never appears as a bare inline label.
# "MORE PRIMARY RESEARCH REQUIRED" is deliberately excluded: §11 uses that
# exact string as a legitimate *recommendation* value, so its bare
# appearance cannot be diagnosed structurally. The defect this check exists
# for -- review 4 Finding 6, a bare "INTERNAL SOURCE CONFLICT REQUIRES
# REVIEW" sitting beside an EVIDENCE READY recommendation -- is unaffected.
E015_BODIES: tuple[str, ...] = tuple(
    body for body in HARD_STOP_BODIES if body != "MORE PRIMARY RESEARCH REQUIRED"
)

VISUAL_ACCESS_STOP = "STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED"
UNVERIFIED_PROJECT_FACT = "UNVERIFIED PROJECT FACT"

# --- Absence / completeness wording (DEC-0012 items 4 and 8) -------------
#
# Deliberately narrow and literal. The linter does not attempt to
# understand prose; it asks only whether a packet that *states* absence
# carries the Negative Claim Records that state requires, and whether a
# packet that *claims* completeness carries the enumeration instruments
# that claim requires.
ABSENCE_PATTERNS: tuple[str, ...] = (
    r"\bRC (?:has|contains|states|prints|supplies|provides) no\b",
    r"\bthe Rules Cyclopedia (?:has|contains|states|prints|supplies|provides) no\b",
    r"\bno (?:such )?(?:table|procedure|mechanic|rule|entry|dependency|owner) exists\b",
    r"\bthe source is silent\b",
    r"\bRC is silent\b",
)
COMPLETENESS_PATTERNS: tuple[str, ...] = (
    r"\bread in full\b",
    r"\bfully inspected\b",
    r"\bexhaustive(?:ly)?\b",
    r"\ball relevant entries\b",
)

# --- Required ledger blocks ----------------------------------------------

PACKET_STATUS_KEYS: tuple[str, ...] = (
    "RULE-ID",
    "PASS",
    "SELF-FALSIFICATION",
    "REPOSITORY-FACT-PASS",
    "INDEPENDENT-REVIEW",
    "RECOMMENDATION",
)
COVERAGE_LEDGER_KEYS: tuple[str, ...] = (
    "EVIDENCE-PAGES",
    "IMAGE-VERIFIED",
    "LOCATOR-ONLY",
    "ACCESS-BLOCKED",
)

# Negative Claim Record fields (DEC-0012 item 4).
NCR_FIELDS: tuple[str, ...] = (
    "CLAIM",
    "SCOPE SEARCHED",
    "STRUCTURAL INSTRUMENTS CHECKED",
    "INDEXES CHECKED",
    "SEARCH TERMS USED",
    "CROSS-REFERENCES FOLLOWED",
    "VISUAL PAGES INSPECTED",
    "FALSIFICATION ATTEMPT",
    "CONFIDENCE",
)
NO_NEGATIVE_CLAIMS = "NEGATIVE CLAIMS: NONE"
NO_REPOSITORY_FACTS = "REPOSITORY FACTS: NONE"

# Falsification record fields (§10, restated as a required shape).
FALSIFICATION_FIELDS: tuple[str, ...] = (
    "CONCLUSION",
    "WOULD FALSIFY",
    "SOUGHT",
    "RESULT",
    "DISPOSITION",
)

_HEADING = re.compile(r"^#{1,6}\s+(?P<title>.+?)\s*$", re.MULTILINE)
_FENCE = re.compile(r"^```[^\n]*\n(?P<body>.*?)^```", re.MULTILINE | re.DOTALL)
_TABLE_SEPARATOR = re.compile(r"^\s*\|?[\s:|-]+\|[\s:|-]*$")


@dataclass(frozen=True)
class Finding:
    """One structural defect in one packet."""

    packet: str
    check: str
    detail: str

    def __str__(self) -> str:
        return f"{self.packet}: [{self.check}] {self.detail}"


def _headings(text: str) -> list[str]:
    return [match.group("title") for match in _HEADING.finditer(text)]


def _fenced_blocks(text: str) -> list[str]:
    return [match.group("body") for match in _FENCE.finditer(text)]


def _prose_outside_fences(text: str) -> str:
    """The packet with fenced blocks removed.

    Verbatim source transcriptions live in fenced blocks, and RC's own
    wording must never be linted as though the researcher had written it.
    """
    return _FENCE.sub("\n", text)


def _keyed_block(text: str, header: str) -> dict[str, str] | None:
    """Parse a fenced ``HEADER`` / ``KEY: value`` ledger block."""
    for body in _fenced_blocks(text):
        lines = [line for line in body.splitlines() if line.strip()]
        if not lines or lines[0].strip() != header:
            continue
        parsed: dict[str, str] = {}
        for line in lines[1:]:
            key, separator, value = line.partition(":")
            if separator:
                parsed[key.strip().upper()] = value.strip()
        return parsed
    return None


def _page_list(raw: str) -> tuple[frozenset[int], str | None]:
    """Parse ``68, 69, 70`` or ``none`` into a page set."""
    if raw.strip().lower() in {"none", "-", "n/a"}:
        return frozenset(), None
    pages: set[int] = set()
    for token in raw.replace(";", ",").split(","):
        candidate = token.strip()
        if not candidate:
            continue
        if not candidate.isdigit():
            return frozenset(), f"{candidate!r} is not a page number"
        pages.add(int(candidate))
    return frozenset(pages), None


def _table_rows(text: str, column: str) -> list[list[str]]:
    """Data rows of every Markdown table carrying ``column`` in its header.

    Returns each row as its list of stripped cells, restricted to tables
    whose header row names the column. Tables inside fenced blocks are
    excluded by the caller passing de-fenced text.
    """
    rows: list[list[str]] = []
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if "|" not in line:
            index += 1
            continue
        header_cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if (
            index + 1 >= len(lines)
            or not _TABLE_SEPARATOR.match(lines[index + 1])
            or not any(column.lower() in cell.lower() for cell in header_cells)
        ):
            index += 1
            continue
        position = next(
            i for i, cell in enumerate(header_cells) if column.lower() in cell.lower()
        )
        index += 2
        while index < len(lines) and "|" in lines[index]:
            cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
            if position < len(cells):
                rows.append([cells[position], lines[index]])
            index += 1
    return rows


def _strip_markup(cell: str) -> str:
    """Reduce a table cell to its bare label text."""
    return cell.replace("**", "").replace("`", "").replace("*", "").strip()


def _find_patterns(text: str, patterns: Iterable[str]) -> list[str]:
    hits: list[str] = []
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            hits.append(match.group(0))
    return hits


def _status_assignments(text: str) -> list[tuple[str, str]]:
    """Every ``KEY: value`` line in the packet, as (upper-cased key, value)."""
    assignments: list[tuple[str, str]] = []
    for line in text.splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            continue
        assignments.append((_strip_markup(key).upper(), _strip_markup(value)))
    return assignments


def _section_body(text: str, section: str) -> str:
    """The text of the first heading containing ``section``, to the next heading."""
    for match in _HEADING.finditer(text):
        if section.lower() not in match.group("title").lower():
            continue
        start = match.end()
        following = _HEADING.search(text, start)
        return text[start : following.start() if following else len(text)]
    return ""


def lint_packet(text: str, name: str) -> list[Finding]:
    """Run every structural check against one packet's Markdown source."""
    findings: list[Finding] = []

    def fail(check: str, detail: str) -> None:
        findings.append(Finding(packet=name, check=check, detail=detail))

    prose = _prose_outside_fences(text)
    headings = " || ".join(_headings(text))

    # E001 -- required instrument sections (DEC-0012 item 3 / item 13).
    missing_sections = [
        section for section in REQUIRED_SECTIONS if section.lower() not in headings.lower()
    ]
    for section in missing_sections:
        fail("E001", f"required section missing: {section!r}")

    # E002 -- the PACKET-STATUS block and its keys.
    status = _keyed_block(text, "PACKET-STATUS")
    if status is None:
        fail("E002", "no PACKET-STATUS ledger block found")
        status = {}
    for key in PACKET_STATUS_KEYS:
        if key not in status:
            fail("E002", f"PACKET-STATUS is missing the {key} field")

    recommendation = status.get("RECOMMENDATION", "")
    review_state = status.get("INDEPENDENT-REVIEW", "")

    # E003 -- recommendation must be exactly one of §11's two strings.
    if recommendation and recommendation not in RECOMMENDATIONS:
        fail("E003", f"RECOMMENDATION {recommendation!r} is not one of §11's two values")

    # E004 -- independent-review status vocabulary (§10.1.2).
    if review_state and review_state not in INDEPENDENT_REVIEW_STATES:
        fail("E004", f"INDEPENDENT-REVIEW {review_state!r} is not a recognised state")
    # Scoped to where such a string would actually *function* as a
    # certification: the value side of a review-status assignment. A packet
    # (or the template) may name these strings in prose in order to warn
    # against them, which is not a certification.
    for key, value in _status_assignments(text):
        if key not in REVIEW_STATUS_KEYS:
            continue
        for prohibited in PROHIBITED_SELF_CERTIFICATIONS:
            if prohibited in value:
                fail(
                    "E004",
                    f"prohibited self-certification {prohibited!r} assigned to {key!r} — "
                    "an original researcher may not certify its own packet (§10.1.2)",
                )

    # E005 -- the coverage ledger and its page lists.
    ledger = _keyed_block(text, "COVERAGE-LEDGER")
    pages: dict[str, frozenset[int]] = {}
    if ledger is None:
        fail("E005", "no COVERAGE-LEDGER ledger block found")
    else:
        for key in COVERAGE_LEDGER_KEYS:
            if key not in ledger:
                fail("E005", f"COVERAGE-LEDGER is missing the {key} field")
                continue
            parsed, error = _page_list(ledger[key])
            if error:
                fail("E005", f"COVERAGE-LEDGER {key}: {error}")
            pages[key] = parsed

    evidence_pages = pages.get("EVIDENCE-PAGES", frozenset())
    image_verified = pages.get("IMAGE-VERIFIED", frozenset())
    locator_only = pages.get("LOCATOR-ONLY", frozenset())
    access_blocked = pages.get("ACCESS-BLOCKED", frozenset())

    # E006 -- a page carrying an evidence row must be visually inspected,
    # or declared access-blocked. (Review 4 Findings 1 and 7; review 5
    # Finding 1: pp. 84-86 carried evidence rows and appeared on no
    # visual-inspection list.)
    unaccounted = sorted(evidence_pages - image_verified - access_blocked)
    if unaccounted:
        fail(
            "E006",
            "pages carry evidence rows but are neither IMAGE-VERIFIED nor "
            f"ACCESS-BLOCKED: {unaccounted}",
        )

    # E007 -- a page cannot be both visually inspected and locator-only.
    both = sorted(image_verified & locator_only)
    if both:
        fail("E007", f"pages listed as both IMAGE-VERIFIED and LOCATOR-ONLY: {both}")

    # E008 -- an unresolved visual-access blocker is a hard stop (§9.2).
    if access_blocked:
        if recommendation == EVIDENCE_READY:
            fail(
                "E008",
                f"ACCESS-BLOCKED pages {sorted(access_blocked)} remain, so the packet "
                f"may not recommend {EVIDENCE_READY!r} (§9.2)",
            )
        if VISUAL_ACCESS_STOP not in text:
            fail(
                "E008",
                f"ACCESS-BLOCKED pages {sorted(access_blocked)} are recorded but "
                f"{VISUAL_ACCESS_STOP!r} is never issued (§9.2, §17)",
            )

    # E009 -- a BLOCKED closure item forbids an EVIDENCE READY
    # recommendation. (Review 2 Finding 12, HIGH: ENC-005 pass 2 did
    # exactly this.)
    if BLOCKED_DISPOSITION in text and recommendation == EVIDENCE_READY:
        fail(
            "E009",
            f"a {BLOCKED_DISPOSITION!r} closure item is present, so the packet may not "
            f"recommend {EVIDENCE_READY!r} (§10.2, §17)",
        )

    # E010 -- Negative Claim Ledger: records, or an explicit NONE.
    ncr_blocks = [
        body
        for body in _fenced_blocks(text)
        if body.splitlines() and body.splitlines()[0].strip() == "NEGATIVE-CLAIM-RECORD"
    ]
    declares_no_negatives = NO_NEGATIVE_CLAIMS in text
    if not ncr_blocks and not declares_no_negatives:
        fail(
            "E010",
            "Negative Claim Ledger carries no NEGATIVE-CLAIM-RECORD block and does not "
            f"state {NO_NEGATIVE_CLAIMS!r}",
        )
    for position, body in enumerate(ncr_blocks, start=1):
        upper = body.upper()
        for field in NCR_FIELDS:
            if field not in upper:
                fail("E010", f"NEGATIVE-CLAIM-RECORD {position} is missing the {field!r} field")

    # E011 -- absence stated in prose requires a Negative Claim Record.
    # (The pass-1 failure: "RC states no consequence for having no light"
    # and "RC has no light-conditioned table", both false, both asserted
    # with nothing behind them.)
    absence_hits = _find_patterns(prose, ABSENCE_PATTERNS)
    if absence_hits and not ncr_blocks:
        fail(
            "E011",
            "absence is stated in prose with no NEGATIVE-CLAIM-RECORD behind it "
            f"(first: {absence_hits[0]!r}) — use NOT YET ESTABLISHED instead (§10.4)",
        )

    # E012 -- completeness wording requires the enumeration instruments
    # that make it auditable (DEC-0012 item 8).
    completeness_hits = _find_patterns(prose, COMPLETENESS_PATTERNS)
    if completeness_hits:
        for required in ("Coverage Manifest", "Index Enumeration"):
            if required in missing_sections:
                fail(
                    "E012",
                    f"completeness wording {completeness_hits[0]!r} is used while the "
                    f"{required!r} section is absent (§9.10)",
                )

    # E013 -- §6 confidence vocabulary in every evidence-map row.
    for cell, line in _table_rows(prose, "Confidence"):
        label = _strip_markup(cell)
        if not label or label.lower() in {"confidence", "---"}:
            continue
        if label not in CONFIDENCE_LABELS:
            fail("E013", f"confidence cell {label!r} is not §6 vocabulary — row: {line.strip()!r}")

    # E014 -- §10.2 disposition vocabulary in the closure section.
    closure = _prose_outside_fences(_section_body(text, "Open-Question Closure"))
    for cell, line in _table_rows(closure, "Disposition"):
        label = _strip_markup(cell)
        if not label or label.lower() in {"disposition", "---"}:
            continue
        if label not in CLOSURE_DISPOSITIONS:
            fail(
                "E014",
                f"closure disposition {label!r} is not §10.2 vocabulary — row: {line.strip()!r}",
            )

    # E015 -- a §17 hard-stop body must always carry its STOP prefix.
    # (Review 4 Finding 6: the bare string asserts a live hard stop.)
    for body_text in E015_BODIES:
        for match in re.finditer(re.escape(body_text), text):
            preceding = text[max(0, match.start() - 8) : match.start()]
            if "STOP — " not in preceding and "STOP - " not in preceding:
                fail(
                    "E015",
                    f"hard-stop string {body_text!r} used without its 'STOP — ' prefix "
                    "(§17 vocabulary is not an inline label)",
                )
                break

    # E016 -- Repository-Fact Verification: rows, or an explicit NONE;
    # and an unverified project fact blocks the gate (DEC-0012 item 5).
    # (Review 4 Finding 5: CHAR-011 named as the owner of p. 150's
    # conditions without opening INVENTORY.md, which says Weapon Mastery.)
    repo_section = _section_body(text, "Repository-Fact Verification")
    repo_rows = _table_rows(_prose_outside_fences(repo_section), "Artifact inspected")
    if not repo_rows and NO_REPOSITORY_FACTS not in text:
        fail(
            "E016",
            "Repository-Fact Verification carries no verified-fact row and does not state "
            f"{NO_REPOSITORY_FACTS!r}",
        )
    if UNVERIFIED_PROJECT_FACT in text and recommendation == EVIDENCE_READY:
        fail(
            "E016",
            f"an {UNVERIFIED_PROJECT_FACT!r} marker remains, so the packet may not "
            f"recommend {EVIDENCE_READY!r} (§10.5)",
        )

    # E017 -- the pre-review self-falsification pass is mandatory and has
    # a required shape (§10.6). There is no "none" option.
    falsification_blocks = [
        body
        for body in _fenced_blocks(text)
        if body.splitlines() and body.splitlines()[0].strip() == "FALSIFICATION-RECORD"
    ]
    if not falsification_blocks:
        fail("E017", "no FALSIFICATION-RECORD block found (§10, §10.6)")
    for position, body in enumerate(falsification_blocks, start=1):
        upper = body.upper()
        for field in FALSIFICATION_FIELDS:
            if field not in upper:
                fail("E017", f"FALSIFICATION-RECORD {position} is missing the {field!r} field")

    # E018 -- the research-completion gate's own declarations (§11.1).
    for key, expected in (
        ("SELF-FALSIFICATION", "COMPLETE"),
        ("REPOSITORY-FACT-PASS", "COMPLETE"),
    ):
        value = status.get(key, "")
        if value and value != expected and recommendation == EVIDENCE_READY:
            fail(
                "E018",
                f"PACKET-STATUS {key} is {value!r}, not {expected!r}, so the packet may "
                f"not recommend {EVIDENCE_READY!r} (§11.1)",
            )

    return findings


def packet_paths(directory: Path) -> list[Path]:
    """Every Stage-A packet in ``directory`` that this linter governs."""
    return sorted(
        path
        for path in directory.glob(PACKET_GLOB)
        if not path.name.startswith("_") and path.name not in GRANDFATHERED
    )


def lint_directory(directory: Path) -> tuple[list[Finding], list[Path]]:
    """Lint the reference packet and every governed Stage-A packet.

    The reference packet comes first so that a template defect is reported
    before any packet derived from it.
    """
    findings: list[Finding] = []
    linted: list[Path] = []

    reference = directory / REFERENCE_PACKET
    if reference.is_file():
        linted.append(reference)
        findings.extend(lint_packet(reference.read_text(encoding="utf-8"), reference.name))
    else:
        findings.append(
            Finding(
                packet=REFERENCE_PACKET,
                check="E000",
                detail=(
                    f"the canonical Stage-A packet template is missing from {directory} — "
                    "§11.2 requires it, and without it this gate has nothing to verify"
                ),
            )
        )

    for path in packet_paths(directory):
        linted.append(path)
        findings.extend(lint_packet(path.read_text(encoding="utf-8"), path.name))
    return findings, linted


def _report(findings: Sequence[Finding], linted: Sequence[Path], skipped: int) -> None:
    reference_count = sum(1 for path in linted if path.name == REFERENCE_PACKET)
    print("Stage-A evidence-packet structural linter (DEC-0012)")
    print("-" * 60)
    print(f"reference packet linted:  {reference_count}  ({REFERENCE_PACKET})")
    print(f"Stage-A packets linted:   {len(linted) - reference_count}")
    print(f"Stage-A grandfathered:    {skipped}")
    for path in linted:
        packet_findings = [finding for finding in findings if finding.packet == path.name]
        verdict = "PASS" if not packet_findings else f"FAIL ({len(packet_findings)})"
        label = " (reference)" if path.name == REFERENCE_PACKET else ""
        print(f"  {path.name + label:<44} {verdict}")
    if findings:
        print("\nFAILED:")
        for finding in findings:
            print(f"  - {finding}")
    else:
        print("\nEvery linted Stage-A packet carries its required instruments.")
        if len(linted) == reference_count:
            print(
                "No post-DEC-0012 Stage-A packet exists yet, so only the reference\n"
                "packet was checked. This gate is live but has not yet governed a\n"
                "real packet -- see DEC-0012 consequence 7 on grandfathering."
            )


def main(argv: Sequence[str] | None = None) -> int:
    """Lint an evidence directory. Defaults to the repository's own.

    The optional directory argument exists so the enforcement path itself can
    be exercised end to end -- running this script as a subprocess against a
    prepared directory and asserting the exit code, rather than only calling
    lint_packet() in-process. A gate is only proven by the exit code it
    actually returns.
    """
    arguments = list(sys.argv[1:] if argv is None else argv)
    directory = Path(arguments[0]).resolve() if arguments else EVIDENCE_DIR
    if not directory.is_dir():
        print(f"error: {directory} not found", file=sys.stderr)
        return 1
    findings, linted = lint_directory(directory)
    grandfathered_present = sum(
        1 for path in directory.glob(PACKET_GLOB) if path.name in GRANDFATHERED
    )
    _report(findings, linted, grandfathered_present)
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
