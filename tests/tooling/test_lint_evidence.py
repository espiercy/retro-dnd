"""Tests for the Stage-A evidence-packet structural linter (DEC-0012).

These tests protect the linter's *decisions*, not its formatting: for each
check, one packet that must pass and one that must fail, with the failing
case built from the corresponding recorded `CLUSTER-004` defect wherever
that defect can be reproduced in miniature. If a check stops firing on the
defect it was created for, one of these tests fails.

Two tests deliberately pin project state rather than behaviour:

    test_template_is_a_conforming_packet   -- the canonical template must
        itself satisfy every structural check, so a researcher who fills it
        in honestly starts from a green baseline.

    test_grandfather_list_is_exactly_the_pre_dec_0012_packets -- the
        grandfather list is CLOSED (DEC-0012 consequence 7). Adding a packet
        to it requires changing this test, which makes the exemption visible
        in review instead of silent.
"""

from __future__ import annotations

from pathlib import Path

import lint_evidence as linter
import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_DIR = REPO_ROOT / "docs" / "rules" / "evidence"
TEMPLATE = EVIDENCE_DIR / "_TEMPLATE.md"


# --- A minimal conforming packet, used as the baseline for every mutation -

def _conforming_packet(
    *,
    recommendation: str = linter.EVIDENCE_READY,
    evidence_pages: str = "69, 70",
    image_verified: str = "69, 70",
    locator_only: str = "72",
    access_blocked: str = "none",
    extra: str = "",
    confidence: str = "DIRECT PRIMARY TEXT",
    closure_disposition: str = "RESOLVED BY SOURCE INSPECTION",
    include_negative_record: bool = True,
    self_falsification: str = "COMPLETE",
) -> str:
    """Build a packet that passes every check, then let callers break one.

    Every required section, ledger and vocabulary item is present, so a
    finding in a mutated copy is attributable to the mutation alone.
    """
    negative_record = (
        """```text
NEGATIVE-CLAIM-RECORD
CLAIM:                           no second illumination table governs this card
SCOPE SEARCHED:                  Ch. 4, Ch. 7, Ch. 13
STRUCTURAL INSTRUMENTS CHECKED:  TOC, Tables Index
INDEXES CHECKED:                 General Index, Index to Spells
SEARCH TERMS USED:               torch, lantern, light, illumination
CROSS-REFERENCES FOLLOWED:       p. 93, p. 150
VISUAL PAGES INSPECTED:          69, 70
FALSIFICATION ATTEMPT:           re-swept the Tables Index for every table naming light
CONFIDENCE:                      DIRECT PRIMARY TEXT
```"""
        if include_negative_record
        else linter.NO_NEGATIVE_CLAIMS
    )

    return f"""# `TEST-001` — Test Card — Stage-A Evidence

```text
PACKET-STATUS
RULE-ID:              TEST-001
PASS:                 1
SELF-FALSIFICATION:   {self_falsification}
REPOSITORY-FACT-PASS: COMPLETE
INDEPENDENT-REVIEW:   {linter.PREPARED}
RECOMMENDATION:       {recommendation}
```

## 1. Research-Start Gate
Scope established from the inventory this pass.

## 2. Primary Source Accessed
Page images; OCR as locator only. No access limitation encountered.

## 3. Source Structure
Ch. 4 Equipment, pp. 62-74.

## 4. Coverage Manifest
| # | Object | Class | Page | Disposition |
|---|---|---|---|---|
| 1 | Adventuring Gear Table | B | 69 | VISUALLY INSPECTED |

## 5. Index Enumeration
| Entry | Pages | Followed? | Disposition |
|---|---|---|---|
| Torch | 69 | yes | DISPOSITIONED |

## 6. Governing Objects
The p. 69 item descriptions are the principal governing object.

## 7. Visual Inspection Record
```text
COVERAGE-LEDGER
EVIDENCE-PAGES:  {evidence_pages}
IMAGE-VERIFIED:  {image_verified}
LOCATOR-ONLY:    {locator_only}
ACCESS-BLOCKED:  {access_blocked}
```

## 8. Cross-Reference Ledger
| From | Explicit reference | Followed to | Result |
|---|---|---|---|
| 69 | see p. 93 | 93 | encounter-distance table located |

## 9. Repository-Fact Verification
| Project claim | Artifact inspected | Identifier / section | Verdict |
|---|---|---|---|
| CHAR-004 owns item cost | docs/rules/INVENTORY.md | row CHAR-004 | VERIFIED |

## 10. Evidence Map
| # | Fact | Object | Provenance | Confidence |
|---|---|---|---|---|
| E-1 | A torch burns for six turns | p. 69 | Rules Cyclopedia Explicit | {confidence} |

## 11. Negative Claim Ledger
{negative_record}

## 12. Ownership and Dependency Routing
| Mechanic | Owner | Status | Evidence for the routing |
|---|---|---|---|
| encounter distance | ENC-001 | UNRESEARCHED | §9 row 1 |

## 13. Falsification Pass
```text
FALSIFICATION-RECORD
CONCLUSION:     a torch burns for six turns
WOULD FALSIFY:  a second duration printed elsewhere in the source
SOUGHT:         Tables Index, General Index Torch entry, Ch. 13
RESULT:         none located; no competing duration printed
DISPOSITION:    CONFIRMED
```

## 14. Open-Question Closure
| # | Open question | Object implicated | Disposition |
|---|---|---|---|
| 1 | does light gate surprise? | p. 92 | {closure_disposition} |

## 15. Primary-Source Coverage Checklist
- Relevant structural units inspected: Ch. 4
- Visual verification completed for: pp. 69, 70

## 16. Independent Review Status
```text
ORIGINAL RESEARCHER OUTPUT:  {linter.PREPARED}
INDEPENDENT REVIEW:          NOT YET PERFORMED
HUMAN EVIDENCE REVIEW:       NOT GIVEN
```
{extra}
"""


def _checks(text: str, name: str = "TEST-001-evidence.md") -> set[str]:
    return {finding.check for finding in linter.lint_packet(text, name)}


# --- The baseline itself --------------------------------------------------


def test_conforming_packet_has_no_findings() -> None:
    findings = linter.lint_packet(_conforming_packet(), "TEST-001-evidence.md")
    assert findings == [], f"baseline packet should be clean, got: {findings}"


def test_template_is_a_conforming_packet() -> None:
    # The canonical template must pass its own linter, or a researcher who
    # follows it starts from a red baseline and learns to ignore the gate.
    findings = linter.lint_packet(TEMPLATE.read_text(encoding="utf-8"), TEMPLATE.name)
    assert findings == [], f"the Stage-A template must lint clean, got: {findings}"


# --- E001 required sections ---------------------------------------------


@pytest.mark.parametrize(
    "section",
    [
        "Coverage Manifest",
        "Negative Claim Ledger",
        "Repository-Fact Verification",
        "Falsification Pass",
        "Index Enumeration",
        "Primary-Source Coverage Checklist",
    ],
)
def test_missing_required_section_is_reported(section: str) -> None:
    text = _conforming_packet().replace(f"## 4. {section}", "## 4. Something Else")
    text = text.replace(f"## 11. {section}", "## 11. Something Else")
    text = text.replace(f"## 9. {section}", "## 9. Something Else")
    text = text.replace(f"## 13. {section}", "## 13. Something Else")
    text = text.replace(f"## 5. {section}", "## 5. Something Else")
    text = text.replace(f"## 15. {section}", "## 15. Something Else")
    assert "E001" in _checks(text)


def test_all_required_sections_are_named_by_the_protocol_template() -> None:
    # The linter matches on section names; the template must supply each one,
    # so the two cannot drift apart silently.
    template = TEMPLATE.read_text(encoding="utf-8").lower()
    for section in linter.REQUIRED_SECTIONS:
        assert section.lower() in template, f"template lacks the {section!r} section"


# --- E002 / E003 / E004 status block ------------------------------------


def test_missing_packet_status_block_is_reported() -> None:
    text = _conforming_packet().replace("PACKET-STATUS", "PACKET-NOTES")
    assert "E002" in _checks(text)


def test_recommendation_outside_the_two_permitted_values_is_reported() -> None:
    text = _conforming_packet(recommendation="LOOKS GOOD TO ME")
    assert "E003" in _checks(text)


def test_original_researcher_self_certification_is_reported() -> None:
    # §10.1.2: the researcher may prepare a packet for review; it may not
    # certify its own completeness.
    text = _conforming_packet().replace(
        "INDEPENDENT REVIEW:          NOT YET PERFORMED",
        "INDEPENDENT REVIEW:          SOURCE COMPLETENESS PASSED",
    )
    assert "E004" in _checks(text)


def test_naming_a_prohibited_certification_to_warn_against_it_is_allowed() -> None:
    # The template and real packets quote these strings in order to forbid
    # them. Only their use AS this packet's own status is a defect.
    text = _conforming_packet(
        extra="\n> Never write `SOURCE COMPLETENESS PASSED` in your own packet.\n"
    )
    assert "E004" not in _checks(text)


# --- E005 / E006 / E007 the coverage ledger -----------------------------


def test_missing_coverage_ledger_is_reported() -> None:
    text = _conforming_packet().replace("COVERAGE-LEDGER", "COVERAGE-NOTES")
    assert "E005" in _checks(text)


def test_unparseable_page_list_is_reported() -> None:
    text = _conforming_packet(image_verified="sixty-nine")
    assert "E005" in _checks(text)


def test_evidence_page_missing_from_every_inspection_list_is_reported() -> None:
    # The CLUSTER-004 defect: RC p. 84 carried evidence row E-43 and
    # appeared on neither coverage list. It survived three research passes
    # and two independent reviews (review 4 F1/F7, review 5 F1).
    text = _conforming_packet(evidence_pages="69, 70, 84", image_verified="69, 70")
    findings = linter.lint_packet(text, "TEST-001-evidence.md")
    assert "E006" in {finding.check for finding in findings}
    assert "84" in " ".join(finding.detail for finding in findings)


def test_page_recorded_as_both_image_verified_and_locator_only_is_reported() -> None:
    text = _conforming_packet(image_verified="69, 70", locator_only="70")
    assert "E007" in _checks(text)


# --- E008 the visual-access gate ----------------------------------------


def test_access_blocked_page_with_a_ready_recommendation_is_reported() -> None:
    # Review 4 Finding 1 (HIGH): an unrenderable page presented as
    # inspected, in a packet recommending EVIDENCE READY.
    text = _conforming_packet(
        evidence_pages="69, 70, 84",
        access_blocked="84",
        recommendation=linter.EVIDENCE_READY,
    )
    assert "E008" in _checks(text)


def test_access_blocked_page_without_the_hard_stop_is_reported() -> None:
    text = _conforming_packet(
        evidence_pages="69, 70, 84",
        access_blocked="84",
        recommendation=linter.MORE_RESEARCH_REQUIRED,
    )
    assert "E008" in _checks(text)


def test_access_blocked_page_declared_correctly_is_accepted() -> None:
    text = _conforming_packet(
        evidence_pages="69, 70, 84",
        access_blocked="84",
        recommendation=linter.MORE_RESEARCH_REQUIRED,
        extra=f"\n{linter.VISUAL_ACCESS_STOP} for p. 84, columns 2-3.\n",
    )
    assert "E008" not in _checks(text)


# --- E009 a BLOCKED closure item ----------------------------------------


def test_blocked_closure_item_with_a_ready_recommendation_is_reported() -> None:
    # Review 2 Finding 12 (HIGH): §17 forbids exactly this combination.
    text = _conforming_packet(
        closure_disposition=linter.BLOCKED_DISPOSITION,
        recommendation=linter.EVIDENCE_READY,
    )
    assert "E009" in _checks(text)


def test_blocked_closure_item_with_more_research_required_is_accepted() -> None:
    text = _conforming_packet(
        closure_disposition=linter.BLOCKED_DISPOSITION,
        recommendation=linter.MORE_RESEARCH_REQUIRED,
    )
    assert "E009" not in _checks(text)


# --- E010 / E011 the Negative Claim Gate --------------------------------


def test_negative_claim_record_missing_a_required_field_is_reported() -> None:
    text = _conforming_packet().replace("INDEXES CHECKED:                 ", "SKIPPED: ")
    assert "E010" in _checks(text)


def test_explicit_none_satisfies_the_negative_claim_ledger() -> None:
    text = _conforming_packet(include_negative_record=False)
    assert "E010" not in _checks(text)


def test_absence_claim_without_a_negative_claim_record_is_reported() -> None:
    # The pass-1 failure in miniature: an absence asserted as a finding
    # with nothing behind it. Both of pass 1's headline claims of this
    # shape turned out to be false.
    text = _conforming_packet(
        include_negative_record=False,
        extra="\nRC has no light-conditioned table anywhere in the source.\n",
    )
    assert "E011" in _checks(text)


def test_absence_claim_backed_by_a_record_is_accepted() -> None:
    text = _conforming_packet(
        include_negative_record=True,
        extra="\nRC has no light-conditioned table; see the record above.\n",
    )
    assert "E011" not in _checks(text)


def test_absence_wording_inside_a_verbatim_quotation_is_not_a_finding() -> None:
    # Fenced blocks carry verbatim source text. RC's own wording must never
    # be linted as though the researcher had written it.
    text = _conforming_packet(
        include_negative_record=False,
        extra='\n```text\nRC has no such rule, the designers wrote.\n```\n',
    )
    assert "E011" not in _checks(text)


# --- E012 unsupported completeness language ------------------------------


def test_completeness_wording_without_the_enumeration_sections_is_reported() -> None:
    text = _conforming_packet(extra="\nThe General Index was read in full.\n")
    text = text.replace("## 5. Index Enumeration", "## 5. Some Notes")
    assert "E012" in _checks(text)


# --- E013 / E014 controlled vocabulary ----------------------------------


def test_confidence_cell_outside_the_protocol_vocabulary_is_reported() -> None:
    # Review 5 Finding 8: four cells carried prose instead of a §6 label.
    text = _conforming_packet(confidence="pretty sure")
    assert "E013" in _checks(text)


@pytest.mark.parametrize("label", sorted(linter.CONFIDENCE_LABELS))
def test_every_permitted_confidence_label_is_accepted(label: str) -> None:
    assert "E013" not in _checks(_conforming_packet(confidence=label))


def test_closure_disposition_outside_the_protocol_vocabulary_is_reported() -> None:
    text = _conforming_packet(closure_disposition="handled elsewhere")
    assert "E014" in _checks(text)


@pytest.mark.parametrize("label", sorted(linter.CLOSURE_DISPOSITIONS))
def test_every_permitted_closure_disposition_is_accepted(label: str) -> None:
    text = _conforming_packet(
        closure_disposition=label,
        recommendation=(
            linter.MORE_RESEARCH_REQUIRED
            if label == linter.BLOCKED_DISPOSITION
            else linter.EVIDENCE_READY
        ),
    )
    assert "E014" not in _checks(text)


# --- E015 hard-stop strings as inline labels ----------------------------


def test_hard_stop_string_used_as_a_bare_label_is_reported() -> None:
    # Review 4 Finding 6: review 3 raised this, one packet fixed it, the
    # sibling packet did not -- the signature of patching a handed list
    # rather than re-running the check.
    text = _conforming_packet(extra="\nN-14 remains unadjudicated. "
                              "`INTERNAL SOURCE CONFLICT REQUIRES REVIEW`.\n")
    assert "E015" in _checks(text)


def test_hard_stop_string_with_its_stop_prefix_is_accepted() -> None:
    text = _conforming_packet(
        extra="\nA packet choosing a number here would trip "
        "`STOP — INTERNAL SOURCE CONFLICT REQUIRES REVIEW`. This one does not choose.\n"
    )
    assert "E015" not in _checks(text)


def test_more_primary_research_required_is_not_treated_as_a_bare_label() -> None:
    # That exact string is also §11's legitimate recommendation value, so
    # E015 excludes it by design (DEC-0012 check-to-failure map).
    text = _conforming_packet(recommendation=linter.MORE_RESEARCH_REQUIRED)
    assert "E015" not in _checks(text)


# --- E016 the Repository Fact Gate --------------------------------------


def test_repository_fact_section_with_no_rows_and_no_none_is_reported() -> None:
    text = _conforming_packet().replace(
        "| CHAR-004 owns item cost | docs/rules/INVENTORY.md | row CHAR-004 | VERIFIED |",
        "",
    )
    assert "E016" in _checks(text)


def test_explicit_none_satisfies_the_repository_fact_section() -> None:
    text = _conforming_packet().replace(
        "| Project claim | Artifact inspected | Identifier / section | Verdict |\n"
        "|---|---|---|---|\n"
        "| CHAR-004 owns item cost | docs/rules/INVENTORY.md | row CHAR-004 | VERIFIED |",
        linter.NO_REPOSITORY_FACTS,
    )
    assert "E016" not in _checks(text)


def test_unverified_project_fact_with_a_ready_recommendation_is_reported() -> None:
    # Review 4 Finding 5: CHAR-011 named as the owner of p. 150's
    # conditions without opening INVENTORY.md, which says Weapon Mastery.
    text = _conforming_packet(
        extra=f"\nOwnership of the p. 150 conditions: {linter.UNVERIFIED_PROJECT_FACT}.\n"
    )
    assert "E016" in _checks(text)


# --- E017 / E018 the falsification and completion gates -----------------


def test_missing_falsification_record_is_reported() -> None:
    text = _conforming_packet().replace("FALSIFICATION-RECORD", "SOME-NOTES")
    assert "E017" in _checks(text)


def test_falsification_record_missing_a_required_field_is_reported() -> None:
    text = _conforming_packet().replace("WOULD FALSIFY:", "NOTES:")
    assert "E017" in _checks(text)


def test_incomplete_self_falsification_with_a_ready_recommendation_is_reported() -> None:
    text = _conforming_packet(self_falsification="NOT STARTED")
    assert "E018" in _checks(text)


def test_incomplete_self_falsification_without_a_ready_recommendation_is_accepted() -> None:
    text = _conforming_packet(
        self_falsification="NOT STARTED", recommendation=linter.MORE_RESEARCH_REQUIRED
    )
    assert "E018" not in _checks(text)


# --- Scope, grandfathering and the directory walk ------------------------


def test_grandfather_list_is_exactly_the_pre_dec_0012_packets() -> None:
    # DEC-0012 consequence 7: the list is CLOSED. A packet written after
    # DEC-0012 is never added, so changing this set must change this test.
    expected = frozenset(
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
    assert expected == linter.GRANDFATHERED


def test_every_grandfathered_packet_still_exists() -> None:
    # If an exempt packet is renamed or removed, the exemption is stale and
    # should be corrected rather than left to mask a new file.
    for name in linter.GRANDFATHERED:
        assert (EVIDENCE_DIR / name).is_file(), f"grandfathered packet {name} not found"


def test_grandfathered_and_template_files_are_not_linted() -> None:
    linted = {path.name for path in linter.packet_paths(EVIDENCE_DIR)}
    assert not (linted & linter.GRANDFATHERED)
    assert TEMPLATE.name not in linted


def test_reviewer_artifacts_are_not_treated_as_packets() -> None:
    # Completeness reviews, audits and gap-research records are reviewer
    # artifacts, not Stage-A packets (§12's naming convention).
    linted = {path.name for path in linter.packet_paths(EVIDENCE_DIR)}
    for name in linted:
        assert "review" not in name and "audit" not in name


def test_repository_evidence_directory_currently_passes() -> None:
    # The gate that runs in canonical verification. It must be green on a
    # clean tree, or the gate is noise.
    findings, _ = linter.lint_directory(EVIDENCE_DIR)
    assert findings == [], f"repository evidence packets have findings: {findings}"


def test_directory_walk_reports_findings_for_a_non_conforming_packet(
    tmp_path: Path,
) -> None:
    (tmp_path / "TEST-002-evidence.md").write_text("# nothing here", encoding="utf-8")
    findings, linted = linter.lint_directory(tmp_path)
    assert [path.name for path in linted] == ["TEST-002-evidence.md"]
    assert "E001" in {finding.check for finding in findings}


def test_finding_renders_packet_check_and_detail() -> None:
    rendered = str(linter.Finding(packet="p.md", check="E006", detail="pages [84]"))
    assert rendered == "p.md: [E006] pages [84]"
