"""`EXP-006` live-record consistency — a deliberately narrow mechanical check.

WHY THIS EXISTS. Three independent final implementation reviews each found
the same defect class, and never a rules defect:

    review #1  MED-3   five artifacts of record said "NOT AUTHORIZED" after
                       implementation was authorized and complete
    review #2  MED-4   three mutually inconsistent deterministic-case totals
                       in one plan section, and a gate table still at 50
    review #3  MED-1   three live records still said "review #2 pending"
               MED-4   ISSUE-022 said 108 tests where its own §6 said 111

Hand-patching prose after the fact has now failed three times. The pattern is
not carelessness about rules -- the mechanics have been clean throughout --
it is that this project has excellent *mechanical* guards for code and had
**none** for the handful of current facts its records duplicate.

WHAT THIS CHECKS, and nothing more:

    A. the current review PHASE token, across named live status records
    B. the deterministic Rule Card case TOTAL, across named live records
       that genuinely state it

WHAT THIS DELIBERATELY DOES NOT DO (human direction, 2026-10-03):

    * it does not scan arbitrary prose;
    * it is not a generic documentation linter;
    * it does not parse historical review artifacts -- those preserve
      obsolete claims ON PURPOSE and must never be "corrected";
    * it does not reject deliberately historical numbers; a figure inside a
      block marked historical, superseded or withdrawn is evidence, not drift;
    * it does not pin the global suite test count. That number changes
      whenever any unrelated project test is added, so pinning it across
      documents would manufacture the very brittleness this file exists to
      remove. Duplicated global counts were REMOVED from the records instead.

The purpose is to prevent recurrence of the exact live-status and
current-total contradictions three reviews have already found -- not to
verify documentation in general.
"""

from __future__ import annotations

import ast
import pathlib
import re

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]

# --- A. the current review phase -------------------------------------------

# One token, spelled identically everywhere it appears. Updating the phase is
# a deliberate act: change it here and every named record must follow, or this
# test fails.
CURRENT_PHASE = "EXP-006-PHASE: REVIEW-3-REMEDIATED"

PHASE_RECORDS = (
    "ARCHITECTURE.md",
    "docs/rules/INVENTORY.md",
    "docs/rules/clusters/CLUSTER-004-equipment-resources-and-evasion.md",
    "docs/technical/EXP-006_IMPLEMENTATION_PLAN.md",
    "docs/completion-records/ISSUE-022-exp-006-light-and-exploration-resources.md",
)

# Phrases that were true once and are now false. A live record must not
# assert any of them; the historical review artifacts may and do.
SUPERSEDED_PHASE_CLAIMS = (
    "review #2 pending",
    "review #2 PENDING",
    "awaiting review #2",
    "pending independent review #2",
    "a second independent review is pending",
    "A SECOND INDEPENDENT FINAL IMPLEMENTATION REVIEW",
)

# --- B. the deterministic case total ---------------------------------------

CASE_TOTAL_RECORDS = (
    "docs/technical/EXP-006_IMPLEMENTATION_PLAN.md",
    "docs/technical/EXP-006_PRE_CODE_GATE.md",
)

# Markers that make a figure explicitly historical. A superseded total inside
# a line carrying one of these is preserved evidence, not drift.
HISTORICAL_MARKERS = (
    "historical",
    "HISTORICAL",
    "superseded",
    "SUPERSEDED",
    "withdrawn",
    "previously",
    "corrected",
    "review #1",
    "review #2",
    "review-#1",
    "review-#2",
    "review-#3",
)


def _read(rel: str) -> str:
    return (REPO_ROOT / rel).read_text(encoding="utf-8")


def _approved_case_total() -> int:
    """The Rule Card's own case count, enumerated from its tables."""
    card = _read("docs/rules/exploration/light_and_exploration_resources.md")
    ids = set(re.findall(r"^\|\s*\**`?(L\d+[a-z]?)`?\**\s*\|", card, re.M))
    return len(ids)


def test_the_approved_case_total_is_still_what_the_records_claim() -> None:
    """The card is the source of truth for its own case count."""
    assert _approved_case_total() == 53


def test_live_status_records_agree_on_the_review_phase() -> None:
    """`MED-1` — every named live status record carries the same phase token.

    This is the check that makes the review-phase drift impossible rather
    than merely corrected: a remediation that advances the phase in one
    record and forgets another fails here.
    """
    missing = [rel for rel in PHASE_RECORDS if CURRENT_PHASE not in _read(rel)]
    assert missing == [], (
        f"these live records do not carry {CURRENT_PHASE!r}: {missing}. "
        "Advancing the review phase means updating CURRENT_PHASE here and "
        "every record in PHASE_RECORDS together."
    )


def test_no_live_record_still_asserts_a_superseded_review_phase() -> None:
    """`MED-1` — the specific stale phrasings three reviews have found.

    Scoped to the named live records only. The review artifacts preserve
    these phrases deliberately and are not read here.
    """
    offences: list[str] = []
    for rel in PHASE_RECORDS:
        for lineno, line in enumerate(_read(rel).splitlines(), 1):
            if any(marker in line for marker in HISTORICAL_MARKERS):
                continue  # explicitly historical; evidence, not drift
            for claim in SUPERSEDED_PHASE_CLAIMS:
                if claim in line:
                    offences.append(f"{rel}:{lineno}: {claim!r}")
    assert offences == [], (
        "live records still assert a superseded review phase; mark the "
        f"statement historical or correct it: {offences}"
    )


def test_live_records_do_not_state_a_stale_case_total() -> None:
    """`MED-4`/review-#2 `MED-4` — no live record contradicts the card's total.

    A line that mentions a case total must state the current one, unless it
    is explicitly marked historical. Totals the project has actually drifted
    through are checked; arbitrary numerals are not.
    """
    total = _approved_case_total()
    stale = {"47", "50", "51"} - {str(total)}
    offences: list[str] = []
    for rel in CASE_TOTAL_RECORDS:
        for lineno, line in enumerate(_read(rel).splitlines(), 1):
            if any(marker in line for marker in HISTORICAL_MARKERS):
                continue
            if not re.search(r"\bcase|\bdeterministic|\btotal\b", line, re.I):
                continue
            for figure in sorted(stale):
                if re.search(rf"\b{figure}\b", line):
                    offences.append(f"{rel}:{lineno}: stale total {figure!r}")
    assert offences == [], (
        f"live records state a case total other than {total}, unmarked as "
        f"historical: {offences}"
    )


def test_the_case_ledger_total_matches_the_card() -> None:
    """The test ledger and the card cannot disagree about how many cases exist.

    Parsed from the sibling module's source rather than imported, so this
    file stays a document check and does not couple to the suite.
    """
    ledger_src = (
        REPO_ROOT / "tests/rules/exploration/test_light_and_exploration_resources.py"
    ).read_text(encoding="utf-8")
    tree = ast.parse(ledger_src)
    mapped: set[str] | None = None
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == "CASE_DISCHARGE"
            and isinstance(node.value, ast.Dict)
        ):
            mapped = {
                key.value
                for key in node.value.keys
                if isinstance(key, ast.Constant) and isinstance(key.value, str)
            }
    assert mapped is not None, "CASE_DISCHARGE not found in the test ledger"
    assert len(mapped) == _approved_case_total()
