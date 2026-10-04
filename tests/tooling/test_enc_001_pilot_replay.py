"""Replay of the ENC-001 DEC-0012 pilot against the DEC-0013 mechanism.

These are **simulations**. They do not read, import or modify the real ENC-001
packet, which is frozen on its own branch; they reconstruct the pilot's seed
inputs from relationships the pilot itself established, and assert that the new
mechanism surfaces the omissions before independent review.

What the pilot actually found, and what each case here replays:

* Review #1 `B-1`  -- RC p. 98 `Contact` was never enumerated. ENC-005's
  accepted packet cites p. 98 and bolds "encounter distance"; the researcher
  read line 147 of that file and not line 146.
* Review #1 `B-2`  -- the City sentence was cited to p. 91; it is printed on
  p. 93.
* Review #2 `BLOCKING-1` -- "every row is now visually inspected" while six
  cited pages were uninspected.
* Review #2 `BLOCKING-2` -- RC p. 100 `Evasion at Sea` states a
  visibility-conditioned distance and was never enumerated.
* Review #2 `BLOCKING-3` -- three hand-maintained counts had gone stale.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))

import lint_evidence  # noqa: E402
from lint_evidence import derive, lint_packet  # noqa: E402

# Seeds as the instruments would have produced them for ENC-001.
#
# TABLES-INDEX: "Encounter Distances Table ... 93", "Chance of Encounter Table
#   ... 92", "Game Turn Checklist ... 91", "Evasion Checklist ... 99",
#   "Ship Evasion Table ... 100".
# GENERAL-INDEX: "Encounters ... 91-96", "Distance ... 87",
#   "Infravision ... 24, 25".
# NEIGHBOUR: ENC-005's accepted packet cites pp. 88, 92, 93, 98, 99, 100, 102,
#   103, 104; EXP-006's cites pp. 69, 70, 93.
SEEDS = """```text
SEEDS
TABLES-INDEX:   91, 92, 93, 99, 100
GENERAL-INDEX:  87, 91-96, 24, 25
NEIGHBOUR:      ENC-005: 88, 92, 93, 98, 99, 100, 102, 103, 104; EXP-006: 69, 70, 93
LEADS:          infravision -> 24, 25
```"""

# What the pilot's pass-1 packet actually inspected: 24, 25, 26, 27, 87, 91,
# 92, 93, 95, 108, 115, 150, 153, 215 and the index pages.
PILOT_PASS_1_PAGES = [24, 25, 26, 27, 87, 91, 92, 93, 95]


def _packet(page_lines: str, evidence: str = "", transcriptions: str = "") -> str:
    return f"""# `ENC-001` — Encounter Distance — Stage-A Evidence

```text
PACKET-STATUS
RULE-ID:              ENC-001
INDEPENDENT-REVIEW:   PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
RECOMMENDATION:       EVIDENCE READY FOR HUMAN REVIEW
```

## 1. Scope and Seams
Owns encounter-distance determination. Routes surprise to `ENC-002`.

## 2. Primary Source

| Source | Access method | Role |
|---|---|---|
| Rules Cyclopedia | page images | authoritative |

## 3. Seeds

{SEEDS}

## 4. Page Dispositions

```text
PAGE-DISPOSITIONS
{page_lines}
```

## 5. Governing Objects

| Object | Page | Kind | Disposition | Owner |
|---|---|---|---|---|
| Encounter Distances Table | 93 | table | GOVERNING | |

## 6. Index Enumeration

| Instrument | Entry | Pages | Disposition |
|---|---|---|---|
| Tables | Encounter Distances Table | 93 | GOVERNING |

**Enumerated absences:** No `Encounter distance` entry in the General Index.

## 7. Transcriptions

{transcriptions}

## 8. Evidence Map

| # | Page | Quote | Paraphrase | Object | Provenance | Confidence |
|---|---|---|---|---|---|---|
{evidence}

## 9. Cross-References

| From | Printed reference | To | Result |
|---|---|---|---|
| 91 | see the Encounter Distance section | 92 | the three surprise branches |

## 10. Ownership and Dependency Routing

| Mechanic | Owner | Status | Basis |
|---|---|---|---|
| Surprise determination | `ENC-002` | UNRESEARCHED | consumed, not absorbed |

## 11. Consequential Negative Claims

NEGATIVE CLAIMS: NONE

## 12. Targeted Falsification

```text
FALSIFICATION
CONCLUSION:   The table governs.
SOUGHT:       Ch. 7
RESULT:       No competing procedure.
DISPOSITION:  CONFIRMED
```

## 13. Open Questions

| # | Question | Object | Disposition |
|---|---|---|---|
| 1 | Does "normal dungeon" mean Dim light? | p. 91 | RETAINED AS GENUINE SOURCE AMBIGUITY |

## 14. Independent Review

```text
INDEPENDENT REVIEW:    NOT YET PERFORMED
HUMAN EVIDENCE REVIEW: NOT GIVEN
```
"""


def _checks(text: str) -> set[str]:
    return {finding.check for finding in lint_packet(text, "ENC-001-evidence.md")}


def test_the_instruments_seed_the_three_pages_the_pilot_needed() -> None:
    """p. 93, p. 98 and p. 100 all arrive from external instruments."""
    seeds, block = lint_evidence._seed_pages(SEEDS)
    assert block is not None
    assert 93 in seeds, "Encounter Distances Table -- Tables Index"
    assert 98 in seeds, "Contact -- ENC-005's accepted packet"
    assert 100 in seeds, "Evasion at Sea -- ENC-005 and the Tables Index"


def test_p98_is_seeded_by_two_mutually_independent_instruments() -> None:
    """The General Index has no `Encounter distance` entry at all, so index
    seeding alone could miss this card's own subject. ENC-005's packet does not
    depend on the index. Redundancy is the point of using both.
    """
    index_only, _ = lint_evidence._seed_pages(
        "```text\nSEEDS\nTABLES-INDEX: 91, 92, 93, 99, 100\n"
        "GENERAL-INDEX: 87, 91-96, 24, 25\nNEIGHBOUR: none\nLEADS: none\n```"
    )
    neighbour_only, _ = lint_evidence._seed_pages(
        "```text\nSEEDS\nTABLES-INDEX: none\nGENERAL-INDEX: none\n"
        "NEIGHBOUR: ENC-005: 88, 92, 93, 98, 99, 100, 102, 103, 104\nLEADS: none\n```"
    )
    assert 98 not in index_only
    assert 98 in neighbour_only


def test_the_pilots_pass_1_coverage_fails_before_review() -> None:
    """B-1 and BLOCKING-1/2 replay.

    The pilot's pass-1 page set reached an independent reviewer. Here it does
    not reach one: the seeded pages it never accounted for are a gate failure.
    """
    lines = "\n".join(f"{page}: INSPECTED" for page in PILOT_PASS_1_PAGES)
    findings = lint_packet(_packet(lines), "ENC-001-evidence.md")
    assert any(f.check == "S005" for f in findings)
    detail = next(f.detail for f in findings if f.check == "S005")
    for missed in (88, 94, 96, 98, 99, 100, 102, 103, 104):
        assert str(missed) in detail, f"p. {missed} should be an unmet obligation"


def test_dispositioning_every_seed_passes_including_cheap_dismissals() -> None:
    """E replay: p. 104 is ENC-005's Retreat/Fighting Withdrawal, genuinely not
    this card's. It costs one line. So do pp. 102, 103, 69, 70.
    """
    lines = "\n".join(
        [
            *(f"{page}: INSPECTED" for page in [24, 25, 87, 91, 92, 93, 94, 95, 96, 98]),
            "88: IRRELEVANT_AFTER_INSPECTION",
            "99: ROUTED_EXTERNAL ENC-005",
            "100: ROUTED_EXTERNAL ENC-005",
            "102: ROUTED_EXTERNAL COMBAT-006",
            "103: ROUTED_EXTERNAL ENC-004",
            "104: OUTSIDE_CARD_SCOPE COMBAT-*",
            "69: ROUTED_EXTERNAL EXP-006",
            "70: ROUTED_EXTERNAL EXP-006",
        ]
    )
    assert lint_packet(_packet(lines), "ENC-001-evidence.md") == []


def test_the_city_sentence_cited_to_p91_fails_mechanically() -> None:
    """B-2 replay: the sentence is printed on p. 93, not p. 91."""
    lines = "\n".join(
        [
            *(f"{page}: INSPECTED" for page in [24, 25, 87, 91, 92, 93, 94, 95, 96, 98]),
            "88: IRRELEVANT_AFTER_INSPECTION",
            "99: ROUTED_EXTERNAL ENC-005",
            "100: ROUTED_EXTERNAL ENC-005",
            "102: ROUTED_EXTERNAL COMBAT-006",
            "103: ROUTED_EXTERNAL ENC-004",
            "104: OUTSIDE_CARD_SCOPE COMBAT-*",
            "69: ROUTED_EXTERNAL EXP-006",
            "70: ROUTED_EXTERNAL EXP-006",
        ]
    )
    transcriptions = (
        "```text\nTRANSCRIPTION p. 91\n"
        "An encounter occurs when two or more groups come within visual range.\n```\n\n"
        "```text\nTRANSCRIPTION p. 93\n"
        "'City' is treated just like any other wilderness terrain.\n```"
    )
    wrong = (
        "| E-19 | 91 | 'City' is treated just like any other wilderness terrain | "
        "| p. 91 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |"
    )
    right = wrong.replace("| E-19 | 91 |", "| E-19 | 93 |").replace("| p. 91 |", "| p. 93 |")
    assert "S010" in _checks(_packet(lines, wrong, transcriptions))
    assert lint_packet(_packet(lines, right, transcriptions), "ENC-001-evidence.md") == []


def test_counts_are_derived_so_none_can_go_stale() -> None:
    """BLOCKING-3 replay: the packet states no count, so none can drift."""
    lines = "\n".join(f"{page}: INSPECTED" for page in PILOT_PASS_1_PAGES)
    counts = derive(_packet(lines))
    assert counts.dispositioned_pages == len(PILOT_PASS_1_PAGES)
    assert counts.governing_objects == 1
    assert counts.open_questions == 1


def test_a_categorical_coverage_claim_cannot_be_written() -> None:
    """BLOCKING-1 replay: the claim form itself is rejected."""
    lines = "\n".join(f"{page}: INSPECTED" for page in PILOT_PASS_1_PAGES)
    boast = _packet(lines).replace(
        "**Enumerated absences:**",
        "Every row is now visually inspected. 38 rows dispositioned.\n\n**Enumerated absences:**",
    )
    assert "S018" in _checks(boast)
