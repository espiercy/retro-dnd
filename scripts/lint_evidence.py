"""Stage-A evidence-packet linter (``DEC-0013``).

This replaces the ``DEC-0012`` structural linter. The check *count* is
comparable -- what changed is what the researcher has to maintain by hand, and
where the obligations come from:

* **page-seed obligations are derived here**, from ``INVENTORY.md`` and from
  accepted neighbour packets, so the candidate page set is not the researcher's
  to narrow. Deleting a page from the packet does not delete its obligation.
* **citations** are matched against the packet's own page transcriptions, so a
  page number cannot drift away from the text it names;
* **counts** are derived here and printed, so there is no hand-maintained
  tally that can go stale.

One limit, stated plainly rather than implied away: **index-derived seeds are
not external yet.** The repository holds no structured transcription of the
Rules Cyclopedia's Tables/Checklists or General Index outside Stage-A packets,
and reading the index ledger inside the packet under review would be circular.
Index enumeration therefore remains research work the semantic reviewer judges,
not a machine-checked obligation.

``DEC-0012``'s pilot failed because its instruments checked each other. A
Coverage Manifest is the researcher's account of what the researcher looked at;
if a page was never opened it simply does not appear, and every cross-check
agrees. **Internal consistency is not external completeness.**

What this tool still cannot do is judge whether the research is right. A green
run is a floor, never a certification, and the original researcher may never
certify its own packet (``RULE_CARD_RESEARCH_PROTOCOL.md`` §10.1.2).

Usage:

    uv run python scripts/lint_evidence.py [<evidence-directory>]

With no argument it lints the repository's own ``docs/rules/evidence/``. A
directory argument is used by the tests to exercise this gate end to end.

Exits 0 if every linted packet passes, 1 otherwise, printing the exact packet,
check ID and reason for each failure.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = REPO_ROOT / "docs" / "rules" / "evidence"
PACKET_GLOB = "*-evidence*.md"

# The template is linted as a reference packet for the same reason DEC-0012
# gave: every pre-existing packet is grandfathered, so without it the gate
# would lint zero files and pass vacuously. A structurally inert gate is worse
# than no gate, because it is mistaken for enforcement.
REFERENCE_PACKET = "_TEMPLATE.md"

# Grandfathering (DEC-0012 consequence 7, carried forward unchanged by
# DEC-0013). Every Stage-A packet that existed when DEC-0012 was adopted is
# exempt. DEC-0013 does not retrofit history: these packets were researched and
# reviewed under the protocol as it then stood, and converting them would
# rewrite accepted evidence rather than improve it.
#
# This list is CLOSED. A packet written after DEC-0012 is never added to it --
# tests/tooling/test_lint_evidence.py pins the exact membership, so extending
# it requires changing a test and is therefore visible in review.
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

# --- Required sections (DEC-0013; the template's own shape) ---------------
#
# Fourteen, against DEC-0012's sixteen -- and four of those that remain are
# materially smaller (see the template). Matched as a case-insensitive
# substring of a heading line, so numbering stays free-form.
REQUIRED_SECTIONS: tuple[str, ...] = (
    "Scope and Seams",
    "Primary Source",
    "Seeds",
    "Page Dispositions",
    "Governing Objects",
    "Index Enumeration",
    "Transcriptions",
    "Evidence Map",
    "Cross-References",
    "Ownership and Dependency Routing",
    "Consequential Negative Claims",
    "Targeted Falsification",
    "Open Questions",
    "Independent Review",
)

# --- Controlled vocabularies ---------------------------------------------

CONFIDENCE_LABELS: frozenset[str] = frozenset(
    {
        "DIRECT PRIMARY TEXT",
        "PRIMARY TEXT + CROSS-REFERENCE CONFIRMED",
        "NECESSARY CONSEQUENCE",
        "SECONDARY SOURCE LOCATOR ONLY",
        "NOT YET VERIFIED",
        "NOT YET ESTABLISHED",
        "REPOSITORY FACT — NOT A SOURCE CLAIM",
    }
)

CLOSURE_DISPOSITIONS: frozenset[str] = frozenset(
    {
        "RESOLVED BY SOURCE INSPECTION",
        "CONFIRMED OUT OF SCOPE",
        "RETAINED AS GENUINE SOURCE AMBIGUITY",
        "BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED",
    }
)
BLOCKED_DISPOSITION = "BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED"

# Page-disposition vocabulary (DEC-0013). Deliberately five values. Two of
# them carry an obligation: a routed or out-of-scope page must say where it
# went, because "not mine" without an owner is how a mechanic becomes unowned.
PAGE_DISPOSITIONS: frozenset[str] = frozenset(
    {
        "INSPECTED",
        "ROUTED_EXTERNAL",
        "IRRELEVANT_AFTER_INSPECTION",
        "OUTSIDE_CARD_SCOPE",
        "ACCESS_BLOCKED",
    }
)
DISPOSITIONS_NEEDING_REASON: frozenset[str] = frozenset(
    {"ROUTED_EXTERNAL", "OUTSIDE_CARD_SCOPE"}
)

EVIDENCE_READY = "EVIDENCE READY FOR HUMAN REVIEW"
MORE_RESEARCH_REQUIRED = "MORE PRIMARY RESEARCH REQUIRED"
RECOMMENDATIONS: frozenset[str] = frozenset({EVIDENCE_READY, MORE_RESEARCH_REQUIRED})

PREPARED = "PREPARED FOR INDEPENDENT COMPLETENESS REVIEW"
INDEPENDENT_REVIEW_STATES: frozenset[str] = frozenset(
    {
        PREPARED,
        "NOT YET PERFORMED",
        "INDEPENDENT COMPLETENESS REVIEW PASSED",
        "INDEPENDENT COMPLETENESS REVIEW FAILED",
    }
)
PROHIBITED_SELF_CERTIFICATIONS: tuple[str, ...] = (
    "SOURCE COMPLETENESS PASSED",
    "SOURCE COMPLETENESS CERTIFIED",
    "HUMAN EVIDENCE GATE CLEARED",
)
REVIEW_STATUS_KEYS: frozenset[str] = frozenset(
    {
        "INDEPENDENT-REVIEW",
        "INDEPENDENT REVIEW",
        "HUMAN EVIDENCE REVIEW",
        "SOURCE COMPLETENESS",
        "STATUS",
    }
)

HARD_STOP_BODIES: tuple[str, ...] = (
    "PRIMARY SOURCE ACCESS REQUIRED",
    "PRIMARY-SOURCE VISUAL ACCESS REQUIRED",
    "PRIMARY PROCEDURE NOT YET ESTABLISHED",
    "INTERNAL SOURCE CONFLICT REQUIRES REVIEW",
    "MORE PRIMARY RESEARCH REQUIRED",
    "COMPLETION COMPATIBILITY NOT ESTABLISHED",
    "HUMAN RULING REQUIRED",
)
# "MORE PRIMARY RESEARCH REQUIRED" is excluded: it is a legitimate
# RECOMMENDATION value, so its bare appearance cannot be diagnosed structurally.
E015_BODIES: tuple[str, ...] = tuple(
    body for body in HARD_STOP_BODIES if body != MORE_RESEARCH_REQUIRED
)
VISUAL_ACCESS_STOP = "STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED"

# --- Hand-maintained counts are now a defect ------------------------------
#
# The pilot's BLOCKING-3 was three stale tallies inside a gate that said "each
# line confirmed, not assumed" -- committed, in one case, inside the
# remediation of that very finding. The fix is not to check the counts. It is
# to make the fields not exist, and to fail a packet that reintroduces one.
MANUAL_COUNT_PATTERNS: tuple[str, ...] = (
    r"\b\d+\s+(?:rows?|entries|records?|blocks?)\s+dispositioned\b",
    r"\b(?:Coverage Manifest|manifest)\s+rows?\s*[:=]\s*\d+",
    r"\b(?:entries|records?|rows?|questions?|pages?)\s+dispositioned\s*[:=]\s*\d+",
    r"\bCross-references followed\s*[:=]?\s*\d+",
    r"\b\d+\s+(?:negative[- ]claim|falsification)\s+records?\b",
    r"\bTotal\s+(?:rows?|pages?|entries)\s*[:=]\s*\d+",
)

PACKET_STATUS_KEYS: tuple[str, ...] = ("RULE-ID", "INDEPENDENT-REVIEW", "RECOMMENDATION")

# What the researcher declares, and what the tool derives.
#
# The researcher declares SUBJECT-TERMS and SEAMS -- judgment the reviewer
# checks -- and LEADS, which are discovered during inspection. The researcher
# does **not** declare the resulting page set: that is derived here from
# INVENTORY.md and from accepted neighbour packets, so deleting a page from
# this packet cannot delete the obligation. That inversion is the whole point
# of DEC-0013, and the first implementation got it wrong.
SEED_KEYS: tuple[str, ...] = ("SUBJECT-TERMS", "SEAMS", "LEADS")

INVENTORY_PATH = REPO_ROOT / "docs" / "rules" / "INVENTORY.md"
_RULE_ID = re.compile(r"\b([A-Z]{3,6}-\d{3})\b")
_PAGE_CITATION = re.compile(r"\bpp?\.\s*(\d+)")
NEGATIVE_CLAIM_FIELDS: tuple[str, ...] = (
    "CLAIM",
    "SCOPE SEARCHED",
    "INSTRUMENTS CHECKED",
    "FALSIFICATION ATTEMPT",
)
FALSIFICATION_FIELDS: tuple[str, ...] = ("CONCLUSION", "SOUGHT", "RESULT", "DISPOSITION")
NO_NEGATIVE_CLAIMS = "NEGATIVE CLAIMS: NONE"

_HEADING = re.compile(r"^#{1,6}\s+(?P<title>.+?)\s*$", re.MULTILINE)
_FENCE = re.compile(r"^```[^\n]*\n(?P<body>.*?)^```", re.MULTILINE | re.DOTALL)
_TABLE_SEPARATOR = re.compile(r"^\s*\|?[\s:|-]+\|[\s:|-]*$")
_PAGE_RANGE = re.compile(r"^\s*(\d+)\s*-\s*(\d+)\s*$")


@dataclass(frozen=True)
class Finding:
    """One defect in one packet."""

    packet: str
    check: str
    detail: str

    def __str__(self) -> str:
        return f"{self.packet}: [{self.check}] {self.detail}"


@dataclass(frozen=True)
class Derived:
    """Counts the packet no longer states and the linter computes instead."""

    seeded_pages: int
    dispositioned_pages: int
    inspected_pages: int
    evidence_rows: int
    quoted_rows: int
    transcriptions: int
    governing_objects: int
    open_questions: int
    negative_claims: int


def _headings(text: str) -> list[str]:
    return [match.group("title") for match in _HEADING.finditer(text)]


def _fenced_blocks(text: str) -> list[str]:
    return [match.group("body") for match in _FENCE.finditer(text)]


def _prose_outside_fences(text: str) -> str:
    """The packet with fenced blocks removed.

    Verbatim source transcriptions live in fenced blocks, and RC's own wording
    must never be linted as though the researcher had written it.
    """
    return _FENCE.sub("\n", text)


def _strip_markup(cell: str) -> str:
    return cell.replace("**", "").replace("`", "").replace("*", "").strip()


def _is_placeholder(value: str) -> bool:
    """Is this an unfilled ``<...>`` slot rather than a real value?

    The template is linted as a reference packet, so its own slots must not be
    read as vocabulary violations. This is the only accommodation the linter
    makes, it applies to every vocabulary check uniformly, and a real packet
    that leaves a slot unfilled still fails the section and field checks.
    """
    stripped = value.strip()
    return stripped.startswith("<") and stripped.endswith(">")


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


def _blocks_headed(text: str, header: str) -> list[str]:
    """Every fenced block whose first line is ``header``."""
    found: list[str] = []
    for body in _fenced_blocks(text):
        lines = body.splitlines()
        if lines and lines[0].strip() == header:
            found.append(body)
    return found


def _pages_in(raw: str) -> set[int]:
    """Parse ``91, 93, 96-98`` into a page set. Ignores non-numeric tokens."""
    pages: set[int] = set()
    for token in re.split(r"[,;]", raw):
        candidate = token.strip()
        if not candidate:
            continue
        span = _PAGE_RANGE.match(candidate)
        if span:
            first, last = int(span.group(1)), int(span.group(2))
            if first <= last and last - first < 500:
                pages.update(range(first, last + 1))
            continue
        bare = re.match(r"^p?p?\.?\s*(\d+)$", candidate)
        if bare:
            pages.add(int(bare.group(1)))
    return pages


class SeedInputError(ValueError):
    """A seed or seam declaration that cannot be parsed.

    Malformed input must fail loudly. The first implementation let a dropped
    colon parse to the empty set, which silently turned an instrument into a
    no-op -- the same shape of defect as a coverage claim with nothing behind it.
    """


@dataclass(frozen=True)
class RepoContext:
    """Where the externally-derived facts live.

    Held as data so the tests can point the derivation at a temporary
    repository, and so it is obvious that these two paths are the only things
    outside the packet that the linter trusts.
    """

    evidence_dir: Path
    inventory: Path

    @classmethod
    def default(cls) -> RepoContext:
        return cls(evidence_dir=EVIDENCE_DIR, inventory=INVENTORY_PATH)

    def inventory_text(self) -> str:
        return self.inventory.read_text(encoding="utf-8") if self.inventory.is_file() else ""


def inventory_neighbours(rule_id: str, inventory_text: str) -> set[str]:
    """Rule IDs related to ``rule_id`` by an INVENTORY row, in both directions.

    Forward: every Rule ID named in this card's own row. Reverse: every row
    that names this card. Deliberately over-inclusive -- a seed is an
    obligation to look, and an unnecessary one costs a single line to
    disposition, while a missing one costs an independent review.

    INVENTORY is **not** treated as complete. ENC-001's own row carries an em
    dash in both dependency columns, so this function alone would have returned
    nothing for the pilot card; declared seams supplement it, and the reviewer
    judges whether they were adequate.
    """
    related: set[str] = set()
    for line in inventory_text.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        ids = set(_RULE_ID.findall(line))
        if not ids:
            continue
        row_id = _RULE_ID.search(line)
        own = row_id.group(1) if row_id else ""
        if own == rule_id:
            related |= ids
        elif rule_id in ids and own:
            related.add(own)
    related.discard(rule_id)
    return related


def accepted_packets(rule_ids: Iterable[str], evidence_dir: Path) -> dict[str, list[Path]]:
    """The accepted evidence packets belonging to each Rule ID.

    Accepted means landed in ``docs/rules/evidence/``. A card may have more
    than one (``-evidence.md`` and ``-evidence-remediated.md``); both are read,
    because a page cited by either is a page someone thought mattered.
    """
    found: dict[str, list[Path]] = {}
    if not evidence_dir.is_dir():
        return found
    for rule_id in sorted(set(rule_ids)):
        paths = sorted(evidence_dir.glob(f"{rule_id}-evidence*.md"))
        if paths:
            found[rule_id] = paths
    return found


def cited_pages(packet_text: str) -> set[int]:
    """Every page a packet cites, by its printed ``p. N`` / ``pp. N`` form.

    Only the page number travels. No quotation, disposition, confidence or
    conclusion is read, so a wrong interpretation in an accepted packet cannot
    become inherited truth -- it can only oblige the new researcher to look at
    the same page and reach their own finding.
    """
    return {int(match) for match in _PAGE_CITATION.findall(packet_text)}


def derive_external_seeds(
    rule_id: str, seams: Iterable[str], context: RepoContext
) -> dict[int, list[str]]:
    """``{page: [origins]}`` derived from outside the packet under review.

    Sources are INVENTORY edges (both directions) union the declared seams,
    resolved to their accepted packets and then to the pages those packets
    cite. The packet under review is excluded from its own derivation.

    **Index-derived seeds are not produced here.** The repository holds no
    structured representation of the Rules Cyclopedia's Tables/Checklists or
    General Index outside Stage-A packets themselves, and deriving them from a
    ledger written inside the packet under review would be circular. That gap
    is reported rather than papered over; see ``_report``.
    """
    neighbours = inventory_neighbours(rule_id, context.inventory_text()) | set(seams)
    neighbours.discard(rule_id)
    seeds: dict[int, list[str]] = {}
    for neighbour, paths in accepted_packets(neighbours, context.evidence_dir).items():
        for path in paths:
            if path.name.startswith(f"{rule_id}-evidence"):
                continue
            for page in sorted(cited_pages(path.read_text(encoding="utf-8"))):
                seeds.setdefault(page, []).append(f"{neighbour} ({path.name})")
    return seeds


def _declared(block: dict[str, str] | None, key: str) -> list[str]:
    """Parse a declared comma-separated list, failing loudly if malformed."""
    if block is None:
        return []
    raw = block.get(key, "")
    if raw.strip().lower() in {"none", "", "-"}:
        return []
    if not any(character.isalnum() for character in raw):
        raise SeedInputError(f"{key} is not parseable: {raw!r}")
    items = [item.strip() for item in raw.split(",") if item.strip()]
    if not items or any(not any(c.isalnum() for c in item) for item in items):
        raise SeedInputError(f"{key} is not parseable: {raw!r}")
    return items


def _seed_pages(text: str) -> tuple[set[int], dict[str, str] | None]:
    """Every page the external instruments put on the researcher's desk."""
    block = _keyed_block(text, "SEEDS")
    if block is None:
        return set(), None
    # Only LEADS contributes pages from inside the packet, and only because a
    # lead is discovered during inspection and has nowhere else to come from.
    # Every other page obligation is derived externally.
    pages: set[int] = set()
    for clause in block.get("LEADS", "").split(";"):
        _, arrow, tail = clause.partition("->")
        if arrow:
            pages |= _pages_in(tail)
    return pages, block


def _page_dispositions(text: str) -> dict[int, tuple[str, str]]:
    """``{page: (disposition, remainder)}`` from the PAGE-DISPOSITIONS block."""
    parsed: dict[int, tuple[str, str]] = {}
    for body in _blocks_headed(text, "PAGE-DISPOSITIONS"):
        for line in body.splitlines()[1:]:
            stripped = line.split("#", 1)[0].strip()
            if not stripped:
                continue
            key, separator, value = stripped.partition(":")
            if not separator or not key.strip().isdigit():
                continue
            words = value.split()
            if not words:
                continue
            parsed[int(key.strip())] = (words[0], " ".join(words[1:]).strip())
    return parsed


def _table_rows(text: str, column: str) -> list[list[str]]:
    """Data rows of every Markdown table whose header names ``column``."""
    rows: list[list[str]] = []
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if "|" not in line:
            index += 1
            continue
        header_cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if index + 1 >= len(lines) or not _TABLE_SEPARATOR.match(lines[index + 1]):
            index += 1
            continue
        if not any(column.lower() == _strip_markup(cell).lower() for cell in header_cells):
            index += 1
            continue
        index += 2
        while index < len(lines) and "|" in lines[index]:
            cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
            if len(cells) == len(header_cells):
                rows.append(cells)
            index += 1
    return rows


def _header_of(text: str, column: str) -> list[str]:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if "|" not in line or index + 1 >= len(lines):
            continue
        if not _TABLE_SEPARATOR.match(lines[index + 1]):
            continue
        cells = [_strip_markup(cell) for cell in line.strip().strip("|").split("|")]
        if any(column.lower() == cell.lower() for cell in cells):
            return cells
    return []


def normalize(text: str) -> str:
    """Fold a quotation to its comparable form.

    Whitespace, quotation glyphs and soft hyphenation differ between a page
    image, a transcription and an evidence row without any of them being wrong.
    Case is preserved: RC distinguishes "Dim light" from "dim light" in table
    cells, and flattening case would hide a real transcription error.
    """
    folded = unicodedata.normalize("NFKC", text)
    for dash in ("‐", "‑", "‒", "–", "—"):
        folded = folded.replace(dash, "-")
    for quote in ("‘", "’", "‛"):
        folded = folded.replace(quote, "'")
    for quote in ("“", "”", "‟"):
        folded = folded.replace(quote, '"')
    folded = folded.replace("­", "").replace("-\n", "")
    folded = _strip_markup(folded)
    return re.sub(r"\s+", " ", folded).strip()


def _transcriptions(text: str) -> dict[int, str]:
    """``{page: normalized transcription}`` from TRANSCRIPTION blocks."""
    found: dict[int, str] = {}
    for body in _fenced_blocks(text):
        lines = body.splitlines()
        if not lines:
            continue
        head = re.match(r"^TRANSCRIPTION\s+p\.?\s*(\d+)\s*$", lines[0].strip())
        if not head:
            continue
        page = int(head.group(1))
        found[page] = normalize("\n".join(lines[1:]))
    return found


def _find_patterns(text: str, patterns: Iterable[str]) -> list[str]:
    hits: list[str] = []
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            hits.append(match.group(0))
    return hits


def _status_assignments(text: str) -> list[tuple[str, str]]:
    assignments: list[tuple[str, str]] = []
    for line in text.splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            continue
        assignments.append((_strip_markup(key).upper(), _strip_markup(value)))
    return assignments


def _section_body(text: str, section: str) -> str:
    for match in _HEADING.finditer(text):
        if section.lower() not in match.group("title").lower():
            continue
        start = match.end()
        following = _HEADING.search(text, start)
        return text[start : following.start() if following else len(text)]
    return ""


def derive(text: str) -> Derived:
    """Compute every count the packet is forbidden to state."""
    seeds, _ = _seed_pages(text)
    pages = _page_dispositions(text)
    evidence = _table_rows(_prose_outside_fences(text), "Quote")
    header = _header_of(_prose_outside_fences(text), "Quote")
    quoted = 0
    if header:
        quote_at = next(i for i, c in enumerate(header) if c.lower() == "quote")
        quoted = sum(1 for row in evidence if row[quote_at].strip(" `*"))
    return Derived(
        seeded_pages=len(seeds),
        dispositioned_pages=len(pages),
        inspected_pages=sum(1 for value in pages.values() if value[0] == "INSPECTED"),
        evidence_rows=len(evidence),
        quoted_rows=quoted,
        transcriptions=len(_transcriptions(text)),
        governing_objects=len(_table_rows(_prose_outside_fences(text), "Kind")),
        open_questions=len(_table_rows(_prose_outside_fences(text), "Question")),
        negative_claims=len(_blocks_headed(text, "NEGATIVE-CLAIM")),
    )


def lint_packet(text: str, name: str, context: RepoContext | None = None) -> list[Finding]:
    """Run every DEC-0013 check against one packet's Markdown source.

    ``context`` supplies the two external sources -- the evidence directory and
    ``INVENTORY.md`` -- that the seed obligations are derived from. It defaults
    to this repository's own.
    """
    context = context or RepoContext.default()
    findings: list[Finding] = []

    def fail(check: str, detail: str) -> None:
        findings.append(Finding(packet=name, check=check, detail=detail))

    prose = _prose_outside_fences(text)
    headings = " || ".join(_headings(text))

    # S001 -- required sections.
    missing_sections = [
        section for section in REQUIRED_SECTIONS if section.lower() not in headings.lower()
    ]
    for section in missing_sections:
        fail("S001", f"required section missing: {section!r}")

    # S002 -- PACKET-STATUS and its three keys.
    status = _keyed_block(text, "PACKET-STATUS")
    if status is None:
        fail("S002", "no PACKET-STATUS ledger block found")
        status = {}
    for key in PACKET_STATUS_KEYS:
        if key not in status:
            fail("S002", f"PACKET-STATUS is missing the {key} field")
    recommendation = status.get("RECOMMENDATION", "")
    review_state = status.get("INDEPENDENT-REVIEW", "")

    # S003 / S004 -- recommendation and review vocabulary; no self-certification.
    if recommendation and recommendation not in RECOMMENDATIONS:
        fail("S003", f"RECOMMENDATION {recommendation!r} is not one of the two values")
    if review_state and review_state not in INDEPENDENT_REVIEW_STATES:
        fail("S004", f"INDEPENDENT-REVIEW {review_state!r} is not a recognised state")
    for key, value in _status_assignments(text):
        if key not in REVIEW_STATUS_KEYS:
            continue
        for prohibited in PROHIBITED_SELF_CERTIFICATIONS:
            if prohibited in value:
                fail("S004", f"{key} asserts {prohibited!r}; a researcher may not self-certify")

    # S005 -- the SEEDS block exists, and every seeded page is dispositioned.
    # This is the check DEC-0012 had no equivalent of: the candidate set comes
    # from the indexes and from accepted neighbour packets, so a page the
    # researcher never opened still has to be accounted for.
    seeds, seed_block = _seed_pages(text)
    pages = _page_dispositions(text)
    if seed_block is None:
        fail("S005", "no SEEDS ledger block found")
    else:
        for key in SEED_KEYS:
            if key not in seed_block:
                fail("S005", f"SEEDS is missing the {key} field")

    # S019 -- the externally-derived obligation set. Generated from
    # INVENTORY.md and from accepted neighbour packets, never from this
    # packet, so removing a page here cannot remove the obligation.
    rule_id = status.get("RULE-ID", "")
    try:
        seams = _declared(seed_block, "SEAMS")
        _declared(seed_block, "SUBJECT-TERMS")
    except SeedInputError as error:
        fail("S019", str(error))
        seams = []
    if rule_id and not _is_placeholder(rule_id):
        external = derive_external_seeds(rule_id, seams, context)
        missing = sorted(set(external) - set(pages))
        if missing:
            origins = "; ".join(
                f"p. {page} <- {', '.join(sorted(set(external[page])))}" for page in missing[:8]
            )
            fail(
                "S019",
                f"{len(missing)} externally-derived page seed(s) carry no disposition: "
                f"{origins}{' ...' if len(missing) > 8 else ''}",
            )

    undispositioned = sorted(seeds - set(pages))
    if undispositioned:
        fail(
            "S005",
            f"lead pages carry no disposition: {undispositioned} "
            "(a seed is an obligation to inspect or route, not inherited truth)",
        )

    # S006 -- page-disposition vocabulary, and the two values owing a reason.
    if not pages:
        fail("S006", "no PAGE-DISPOSITIONS ledger block found")
    for page, (disposition, remainder) in sorted(pages.items()):
        if disposition not in PAGE_DISPOSITIONS:
            fail("S006", f"p. {page}: {disposition!r} is not a page-disposition value")
            continue
        if disposition in DISPOSITIONS_NEEDING_REASON and not remainder:
            fail("S006", f"p. {page}: {disposition} requires a Rule ID or bounded reason")

    # S007 -- ACCESS_BLOCKED is a hard stop.
    blocked = sorted(page for page, value in pages.items() if value[0] == "ACCESS_BLOCKED")
    if blocked:
        if recommendation == EVIDENCE_READY:
            fail(
                "S007",
                f"pages {blocked} are ACCESS_BLOCKED; may not recommend {EVIDENCE_READY!r}",
            )
        if VISUAL_ACCESS_STOP not in text:
            fail("S007", f"pages {blocked} are ACCESS_BLOCKED but {VISUAL_ACCESS_STOP!r} is absent")

    # S008 -- an open question BLOCKED forbids an EVIDENCE READY recommendation.
    if BLOCKED_DISPOSITION in text and recommendation == EVIDENCE_READY:
        fail("S008", f"a BLOCKED open question forbids {EVIDENCE_READY!r}")

    # S009 -- every page an evidence row cites must be dispositioned INSPECTED.
    header = _header_of(prose, "Quote")
    evidence_rows = _table_rows(prose, "Quote")
    if header and evidence_rows:
        at = {name.lower(): i for i, name in enumerate(header)}
        page_at = at.get("page")
        quote_at = at.get("quote")
        para_at = at.get("paraphrase")
        confidence_at = at.get("confidence")
        transcriptions = _transcriptions(text)
        for row in evidence_rows:
            label = _strip_markup(row[0]) or "?"
            if page_at is None:
                break
            cited = _pages_in(_strip_markup(row[page_at]))
            for page in sorted(cited):
                if page not in pages:
                    fail("S009", f"{label}: cites p. {page}, which has no disposition")
                elif pages[page][0] != "INSPECTED":
                    fail(
                        "S009",
                        f"{label}: cites p. {page}, dispositioned {pages[page][0]} "
                        "-- only an INSPECTED page may support an evidence row",
                    )
            # S010 -- citation verification. A quote must occur in the
            # transcription recorded for the page it is attributed to. This is
            # the check that makes a page number mechanically falsifiable.
            quote = _strip_markup(row[quote_at]) if quote_at is not None else ""
            para = _strip_markup(row[para_at]) if para_at is not None else ""
            # M-5: exactly one. Both was already rejected; neither was not,
            # though the template required one -- an evidence row supporting
            # nothing is the emptiest form of the claim-without-mechanism
            # defect this whole record exists to stop.
            if quote_at is not None and para_at is not None:
                filled = [value for value in (quote, para) if value and not _is_placeholder(value)]
                if len(filled) > 1:
                    fail("S010", f"{label}: carries both a quote and a paraphrase; use exactly one")
                elif not filled and not (_is_placeholder(quote) or _is_placeholder(para)):
                    fail("S010", f"{label}: carries neither a quote nor a paraphrase")
            if quote:
                needle = normalize(quote)
                for page in sorted(cited):
                    haystack = transcriptions.get(page)
                    if haystack is None:
                        fail("S010", f"{label}: p. {page} has no TRANSCRIPTION block to match")
                    elif needle not in haystack:
                        fail(
                            "S010",
                            f"{label}: quoted text does not occur in p. {page}'s "
                            "transcription (wrong page, or the transcription is incomplete)",
                        )
            # S011 -- confidence vocabulary.
            if confidence_at is not None:
                label_text = _strip_markup(row[confidence_at])
                known = label_text in CONFIDENCE_LABELS or _is_placeholder(label_text)
                if label_text and not known:
                    fail("S011", f"{label}: confidence {label_text!r} is not the vocabulary")

    # S012 -- every printed cross-reference target must be dispositioned. A
    # followed reference that leads somewhere unaccounted for is exactly how
    # p. 98 went missing in the pilot.
    for row in _table_rows(prose, "To"):
        target = _pages_in(_strip_markup(row[2]) if len(row) > 2 else "")
        for page in sorted(target - set(pages)):
            fail("S012", f"cross-reference target p. {page} carries no disposition")

    # S013 -- every LEAD resolves to at least one page.
    if seed_block is not None:
        raw_leads = seed_block.get("LEADS", "")
        if raw_leads.strip().lower() not in {"none", "", "-"}:
            for clause in raw_leads.split(";"):
                if not clause.strip():
                    continue
                term, arrow, tail = clause.partition("->")
                if _is_placeholder(clause.strip()):
                    continue
                if not arrow or not _pages_in(tail):
                    fail("S013", f"LEAD {term.strip()!r} never resolves to a page")

    # S014 -- consequential negative claims carry their three evidence fields.
    claim_blocks = _blocks_headed(text, "NEGATIVE-CLAIM")
    if not claim_blocks and NO_NEGATIVE_CLAIMS not in text:
        fail("S014", f"no NEGATIVE-CLAIM block and no explicit {NO_NEGATIVE_CLAIMS!r}")
    for position, body in enumerate(claim_blocks, start=1):
        upper = body.upper()
        for field in NEGATIVE_CLAIM_FIELDS:
            if field not in upper:
                fail("S014", f"NEGATIVE-CLAIM {position} is missing the {field!r} field")

    # S015 -- targeted falsification records keep their shape where present.
    for position, body in enumerate(_blocks_headed(text, "FALSIFICATION"), start=1):
        upper = body.upper()
        for field in FALSIFICATION_FIELDS:
            if field not in upper:
                fail("S015", f"FALSIFICATION {position} is missing the {field!r} field")

    # S016 -- each table's Disposition column is validated against its OWN
    # vocabulary. The first implementation accepted the union of three, so an
    # Open Question dispositioned INSPECTED passed while the template said the
    # permitted labels were exactly four, "verbatim". A permissive union is a
    # check that agrees with everything.
    for section, allowed, what in (
        ("Open Questions", CLOSURE_DISPOSITIONS, "open-question"),
        ("Governing Objects", frozenset({"GOVERNING", "ROUTED"}), "governing-object"),
    ):
        for row in _table_rows(_prose_outside_fences(_section_body(text, section)), "Disposition"):
            label_text = _strip_markup(row[-1] if section == "Open Questions" else row[3])
            if not label_text or _is_placeholder(label_text):
                continue
            if label_text not in allowed:
                fail("S016", f"{what} disposition {label_text!r} is not that field's vocabulary")

    # S017 -- hard-stop bodies must carry their STOP prefix.
    for body_text in E015_BODIES:
        for match in re.finditer(re.escape(body_text), text):
            preceding = text[max(0, match.start() - 8) : match.start()]
            if "STOP — " not in preceding and "STOP - " not in preceding:
                fail("S017", f"{body_text!r} appears without its 'STOP — ' prefix")

    # S018 -- a backstop, not a general rule.
    #
    # The real protection against stale counts is structural: the template has
    # no count field, so there is nothing to maintain and nothing to drift.
    # This check only catches the phrasings actually observed going stale in
    # the pilot. Establishing "no count anywhere" mechanically would need
    # general language parsing, which this project does not want and which
    # would be a worse cure than the disease -- so the claim is narrowed to
    # what the patterns below genuinely prove, rather than the patterns being
    # described as something they are not.
    for hit in _find_patterns(prose, MANUAL_COUNT_PATTERNS):
        fail(
            "S018",
            f"hand-maintained count {hit.strip()!r}: counts are derived by this "
            "linter and must not be written into the packet",
        )

    return findings


def lint_directory(
    directory: Path, context: RepoContext | None = None
) -> tuple[list[Finding], list[Path]]:
    context = context or RepoContext(evidence_dir=directory, inventory=INVENTORY_PATH)
    findings: list[Finding] = []
    linted: list[Path] = []
    reference = directory / REFERENCE_PACKET
    if reference.is_file():
        linted.append(reference)
        findings.extend(
            lint_packet(reference.read_text(encoding="utf-8"), reference.name, context)
        )
    else:
        findings.append(
            Finding(packet=REFERENCE_PACKET, check="S000", detail="reference packet is missing")
        )
    for path in sorted(directory.glob(PACKET_GLOB)):
        if path.name in GRANDFATHERED or path.name == REFERENCE_PACKET:
            continue
        linted.append(path)
        findings.extend(lint_packet(path.read_text(encoding="utf-8"), path.name, context))
    return findings, linted


def _report(
    findings: Sequence[Finding],
    linted: Sequence[Path],
    skipped: int,
    context: RepoContext | None = None,
) -> None:
    context = context or RepoContext.default()
    reference_count = sum(1 for path in linted if path.name == REFERENCE_PACKET)
    print("Stage-A evidence-packet linter (DEC-0013)")
    print("-" * 60)
    print(f"reference packet linted:  {reference_count}  ({REFERENCE_PACKET})")
    print(f"Stage-A packets linted:   {len(linted) - reference_count}")
    print(f"Stage-A grandfathered:    {skipped}  (closed set; not migrated)")
    for path in linted:
        packet_findings = [finding for finding in findings if finding.packet == path.name]
        verdict = "PASS" if not packet_findings else f"FAIL ({len(packet_findings)})"
        label = " (reference)" if path.name == REFERENCE_PACKET else ""
        print(f"  {path.name + label:<44} {verdict}")
        if path.name == REFERENCE_PACKET:
            continue
        packet_text = path.read_text(encoding="utf-8")
        status = _keyed_block(packet_text, "PACKET-STATUS") or {}
        rule_id = status.get("RULE-ID", "")
        if rule_id and not _is_placeholder(rule_id):
            seed_block = _keyed_block(packet_text, "SEEDS")
            try:
                seams = _declared(seed_block, "SEAMS")
            except SeedInputError:
                seams = []
            external = derive_external_seeds(rule_id, seams, context)
            if external:
                print(f"      REQUIRED EXTERNAL PAGE SEEDS ({len(external)}):")
                for page in sorted(external):
                    origins = ", ".join(sorted(set(external[page])))
                    print(f"        p. {page} <- {origins}")
            else:
                print("      REQUIRED EXTERNAL PAGE SEEDS: none derived")
            print(
                "      (index-derived seeds are NOT external: no structured RC index\n"
                "       transcription exists outside Stage-A packets -- see module docstring)"
            )
        counts = derive(packet_text)
        print(
            f"      derived: seeded {counts.seeded_pages}, dispositioned "
            f"{counts.dispositioned_pages} ({counts.inspected_pages} inspected), "
            f"objects {counts.governing_objects}, evidence {counts.evidence_rows} "
            f"({counts.quoted_rows} quoted / {counts.transcriptions} transcriptions), "
            f"questions {counts.open_questions}, negative claims {counts.negative_claims}"
        )
    if findings:
        print("\nFAILED:")
        for finding in findings:
            print(f"  - {finding}")
    else:
        print("\nEvery linted Stage-A packet carries its required instruments,")
        print("every seeded page is dispositioned, and every quotation matches")
        print("the transcription of the page it cites.")
        if len(linted) == reference_count:
            print(
                "\nNo post-DEC-0013 Stage-A packet exists yet, so only the reference\n"
                "packet was checked. This gate is live but has not yet governed a\n"
                "real packet."
            )


def main(argv: Sequence[str] | None = None) -> int:
    """Lint an evidence directory. Defaults to the repository's own."""
    arguments = list(sys.argv[1:] if argv is None else argv)
    directory = Path(arguments[0]).resolve() if arguments else EVIDENCE_DIR
    if not directory.is_dir():
        print(f"error: {directory} not found", file=sys.stderr)
        return 1
    context = RepoContext(evidence_dir=directory, inventory=INVENTORY_PATH)
    findings, linted = lint_directory(directory, context)
    grandfathered_present = sum(
        1 for path in directory.glob(PACKET_GLOB) if path.name in GRANDFATHERED
    )
    _report(findings, linted, grandfathered_present, context)
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
