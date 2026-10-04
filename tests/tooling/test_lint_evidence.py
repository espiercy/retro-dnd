"""Tests for the DEC-0013 Stage-A evidence linter.

Cases A-G replay the defects actually observed in the ENC-001 DEC-0012 pilot
and the EXP-006 review series. Each one is a defect that reached, or would have
reached, a human reviewer under DEC-0012; each must now be caught mechanically
or cost nothing to dismiss.

The suite also pins the grandfathered set, which is closed: extending it has to
change a test, and is therefore visible in review.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))

import lint_evidence  # noqa: E402
from lint_evidence import (  # noqa: E402
    GRANDFATHERED,
    REFERENCE_PACKET,
    derive,
    lint_packet,
    main,
    normalize,
)

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "lint_evidence.py"


# --- A minimal packet that passes, which every case below perturbs ---------

VALID = """# `TEST-900` — Example — Stage-A Evidence

```text
PACKET-STATUS
RULE-ID:              TEST-900
INDEPENDENT-REVIEW:   PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
RECOMMENDATION:       EVIDENCE READY FOR HUMAN REVIEW
```

## 1. Scope and Seams
Owns the example mechanic. Routes surprise to `ENC-002`.

## 2. Primary Source

| Source | Access method | Role |
|---|---|---|
| Example edition | page images | authoritative |

## 3. Seeds

```text
SEEDS
SUBJECT-TERMS:  encounter distance
SEAMS:          none
LEADS:          infravision -> 24
```

## 4. Page Dispositions

```text
PAGE-DISPOSITIONS
91: INSPECTED
92: INSPECTED
93: INSPECTED
98: INSPECTED
104: OUTSIDE_CARD_SCOPE COMBAT-*
24: INSPECTED
```

## 5. Governing Objects

| Object | Page | Kind | Disposition | Owner |
|---|---|---|---|---|
| Example Table | 93 | table | GOVERNING | |

## 6. Index Enumeration

| Instrument | Entry | Pages | Disposition |
|---|---|---|---|
| Tables | Example Table | 93 | GOVERNING |

**Enumerated absences:** None recorded.

## 7. Transcriptions

```text
TRANSCRIPTION p. 93
The encounter distance is determined by setting and visibility.
```

```text
TRANSCRIPTION p. 98
Contact occurs when the two parties encounter one another.
```

## 8. Evidence Map

| # | Page | Quote | Paraphrase | Object | Provenance | Confidence |
|---|---|---|---|---|---|---|
| E-1 | 93 | distance is determined by setting | | table | RC Explicit | DIRECT PRIMARY TEXT |
| E-2 | 98 | | Contact is defined here | prose | RC Explicit | DIRECT PRIMARY TEXT |

## 9. Cross-References

| From | Printed reference | To | Result |
|---|---|---|---|
| 93 | see page 98 | 98 | Contact definition |

## 10. Ownership and Dependency Routing

| Mechanic | Owner | Status | Basis |
|---|---|---|---|
| Surprise | `ENC-002` | UNRESEARCHED | routed, not absorbed |

## 11. Consequential Negative Claims

```text
NEGATIVE-CLAIM
CLAIM:                  No other rule modifies the example distance.
SCOPE SEARCHED:         pp. 91-104
INSTRUMENTS CHECKED:    Tables Index, General Index
FALSIFICATION ATTEMPT:  Sought a second distance statement; none found.
```

## 12. Targeted Falsification

```text
FALSIFICATION
CONCLUSION:   The table governs.
SOUGHT:       pp. 91-104
RESULT:       No competing procedure.
DISPOSITION:  CONFIRMED
```

## 13. Open Questions

| # | Question | Object | Disposition |
|---|---|---|---|
| 1 | Does visibility bind? | p. 93 | RETAINED AS GENUINE SOURCE AMBIGUITY |

## 14. Independent Review

```text
INDEPENDENT REVIEW:    NOT YET PERFORMED
HUMAN EVIDENCE REVIEW: NOT GIVEN
```
"""


def checks(text: str) -> set[str]:
    return {finding.check for finding in lint_packet(text, "TEST-900-evidence.md")}


def test_the_baseline_packet_passes() -> None:
    assert lint_packet(VALID, "TEST-900-evidence.md") == []


def test_the_shipped_template_passes() -> None:
    template = Path(lint_evidence.EVIDENCE_DIR) / REFERENCE_PACKET
    assert lint_packet(template.read_text(encoding="utf-8"), REFERENCE_PACKET) == []


# --- A / E / F: seed obligations -----------------------------------------
#
# These cases moved to test_external_seed_derivation.py when seed generation
# became external. Testing them here would mean asserting against a seed list
# the packet itself declares, which is the defect the move exists to remove.


# --- B: citation drift -----------------------------------------------------


def test_a_quote_attributed_to_the_wrong_page_fails() -> None:
    """ENC-001 B-2 replay: text cited to p. 91 that is printed on p. 93."""
    broken = VALID.replace(
        "| E-1 | 93 | distance is determined by setting",
        "| E-1 | 91 | distance is determined by setting",
    )
    assert "S010" in checks(broken)


def test_a_quote_matching_its_cited_page_passes_through_normalization() -> None:
    quoted = VALID.replace(
        "distance is determined by setting |",
        "distance  is   determined  by setting |",
    )
    assert "S010" not in checks(quoted)
    # A dash the transcription does not contain is a real mismatch, not a
    # normalization case: folding en-dash to hyphen must not invent one.
    invented = VALID.replace(
        "distance is determined by setting |",
        "distance – is determined by setting |",
    )
    assert "S010" in checks(invented)


def test_an_evidence_row_citing_an_undispositioned_page_fails() -> None:
    broken = VALID.replace("| E-1 | 93 |", "| E-1 | 77 |")
    assert "S009" in checks(broken)


def test_an_evidence_row_may_not_cite_a_routed_page() -> None:
    broken = VALID.replace("| E-2 | 98 | |", "| E-2 | 104 | |")
    assert "S009" in checks(broken)


# --- C: the stale-count class ---------------------------------------------


def test_no_count_field_exists_to_drift_and_counts_are_derived() -> None:
    """ENC-001 BLOCKING-3 replay.

    Three tallies went stale inside a gate asserting "each line confirmed, not
    assumed". The fix is not to check them: it is that the packet has no count
    field at all, and the linter derives them.
    """
    counts = derive(VALID)
    assert counts.seeded_pages == 1  # LEADS only; page obligations are external
    assert counts.dispositioned_pages == 6
    assert counts.inspected_pages == 5
    assert counts.evidence_rows == 2
    assert counts.quoted_rows == 1
    assert counts.transcriptions == 2
    assert counts.negative_claims == 1


def test_a_hand_maintained_count_is_rejected() -> None:
    broken = VALID.replace(
        "**Enumerated absences:** None recorded.",
        "**Enumerated absences:** None recorded. 38 rows dispositioned.",
    )
    assert "S018" in checks(broken)


# --- D: the false categorical-coverage class -------------------------------
#
# The missing-seed half of D is in test_external_seed_derivation.py. What
# remains here is the half that is purely local to the packet.


def test_a_routed_page_must_name_where_it_went() -> None:
    broken = VALID.replace("104: OUTSIDE_CARD_SCOPE COMBAT-*", "104: OUTSIDE_CARD_SCOPE")
    assert "S006" in checks(broken)


def test_access_blocked_is_a_hard_stop() -> None:
    broken = VALID.replace("92: INSPECTED", "92: ACCESS_BLOCKED")
    assert "S007" in checks(broken)


# --- E: the cheap false-positive dismissal --------------------------------


def test_an_unrelated_neighbour_seed_is_dismissed_in_one_line() -> None:
    """ENC-005 cites p. 104 (Retreat/Fighting Withdrawal), which is COMBAT-*'s.

    The whole cost of disposing of it is the single line already in VALID. If
    this test ever needs more ceremony than that line, the design has drifted.
    """
    assert lint_packet(VALID, "TEST-900-evidence.md") == []
    pages = lint_evidence._page_dispositions(VALID)
    assert pages[104] == ("OUTSIDE_CARD_SCOPE", "COMBAT-*")


# --- G: mechanical defects do not demand semantic re-review ----------------


def test_a_mechanical_defect_is_expressed_as_a_check_not_a_review_state() -> None:
    """The escalation rule is only honest if a mechanical defect is visible as
    a linter finding and leaves the review state untouched, so correcting it
    needs machine verification rather than a new semantic review.
    """
    broken = VALID.replace("| E-1 | 93 |", "| E-1 | 91 |")
    findings = lint_packet(broken, "TEST-900-evidence.md")
    assert findings and all(f.check.startswith("S") for f in findings)
    status = lint_evidence._keyed_block(broken, "PACKET-STATUS")
    assert status is not None
    assert status["INDEPENDENT-REVIEW"] == "PREPARED FOR INDEPENDENT COMPLETENESS REVIEW"


# --- Remaining structure --------------------------------------------------


def test_a_cross_reference_target_must_be_dispositioned() -> None:
    broken = VALID.replace("| 93 | see page 98 | 98 |", "| 93 | see page 77 | 77 |")
    assert "S012" in checks(broken)


def test_an_unresolved_lead_fails() -> None:
    broken = VALID.replace("LEADS:          infravision -> 24", "LEADS:          infravision")
    assert "S013" in checks(broken)


def test_a_missing_section_fails() -> None:
    broken = VALID.replace("## 3. Seeds", "## 3. Something Else")
    assert "S001" in checks(broken)


def test_self_certification_is_rejected() -> None:
    broken = VALID.replace(
        "INDEPENDENT REVIEW:    NOT YET PERFORMED",
        "INDEPENDENT REVIEW:    SOURCE COMPLETENESS CERTIFIED",
    )
    assert "S004" in checks(broken)


def test_a_blocked_open_question_forbids_evidence_ready() -> None:
    broken = VALID.replace(
        "RETAINED AS GENUINE SOURCE AMBIGUITY",
        "BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED",
    )
    assert "S008" in checks(broken)


def test_a_negative_claim_missing_its_evidence_fields_fails() -> None:
    broken = VALID.replace("INSTRUMENTS CHECKED:    Tables Index, General Index\n", "")
    assert "S014" in checks(broken)


def test_a_packet_with_no_consequential_negative_claim_must_say_so() -> None:
    without = VALID.replace(
        """```text
NEGATIVE-CLAIM
CLAIM:                  No other rule modifies the example distance.
SCOPE SEARCHED:         pp. 91-104
INSTRUMENTS CHECKED:    Tables Index, General Index
FALSIFICATION ATTEMPT:  Sought a second distance statement; none found.
```""",
        "NEGATIVE CLAIMS: NONE",
    )
    assert "S014" not in checks(without)


def test_an_unrecognised_confidence_label_fails() -> None:
    broken = VALID.replace("| DIRECT PRIMARY TEXT |", "| PRETTY SURE |", 1)
    assert "S011" in checks(broken)


def test_normalize_folds_whitespace_dashes_and_quotes_but_not_case() -> None:
    assert normalize("a — b") == normalize("a - b")
    assert normalize("“x”") == normalize('"x"')
    assert normalize("Dim light") != normalize("dim light")


# --- The gate itself -------------------------------------------------------


def test_the_grandfathered_set_is_closed_and_exact() -> None:
    assert set(GRANDFATHERED) == (
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


def test_grandfathered_packets_are_not_linted(tmp_path: Path) -> None:
    (tmp_path / REFERENCE_PACKET).write_text(VALID, encoding="utf-8")
    (tmp_path / "EXP-006-evidence.md").write_text("not a packet at all", encoding="utf-8")
    findings, linted = lint_evidence.lint_directory(tmp_path)
    assert findings == []
    assert [path.name for path in linted] == [REFERENCE_PACKET]


def test_a_missing_reference_packet_is_itself_a_failure(tmp_path: Path) -> None:
    findings, _ = lint_evidence.lint_directory(tmp_path)
    assert any(finding.check == "S000" for finding in findings)


@pytest.mark.parametrize("broken,expected", [(False, 0), (True, 1)])
def test_the_gate_returns_the_exit_code_it_promises(
    tmp_path: Path, broken: bool, expected: int
) -> None:
    packet = VALID.replace("| E-1 | 93 |", "| E-1 | 91 |") if broken else VALID
    (tmp_path / REFERENCE_PACKET).write_text(VALID, encoding="utf-8")
    (tmp_path / "TEST-900-evidence.md").write_text(packet, encoding="utf-8")
    assert main([str(tmp_path)]) == expected


def test_the_gate_runs_as_a_subprocess(tmp_path: Path) -> None:
    (tmp_path / REFERENCE_PACKET).write_text(VALID, encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(tmp_path)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "DEC-0013" in result.stdout
