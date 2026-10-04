"""The externally-derived seed obligation, and the probe that broke the first try.

The first DEC-0013 implementation let the packet declare its own seed pages.
The independent review's probe was decisive: delete p. 98 from the packet and
the pilot's original `B-1` defect lints clean again. These tests exist so that
probe can never pass.

The requirement is specific, and a fixture that preloads p. 98 does **not**
satisfy it: the obligation has to be regenerated from `INVENTORY.md` and from an
accepted neighbour packet, neither of which the packet under review controls.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))

import lint_evidence  # noqa: E402
from lint_evidence import (  # noqa: E402
    RepoContext,
    RuleIdError,
    SeedInputError,
    accepted_packets,
    cited_pages,
    derive_external_seeds,
    inventory_neighbours,
    inventory_rule_ids,
    lint_packet,
    rule_id_from_filename,
    validate_rule_id,
)

# An accepted neighbour packet, in the shape the real ones take: prose with
# printed page citations. Note the deliberately WRONG interpretation -- it is
# here to prove that only the page number travels.
NEIGHBOUR_PACKET = """# `ENC-005` — Evasion — Stage-A Evidence

| N-4 | `Contact` (p. 98): the DM determines the encounter distance | p. 98 |
| N-4a | The Encounter Distances Table is light-keyed | p. 92 |

Further material at p. 100 (Evasion at Sea) and p. 93 (the table itself).
"""

INVENTORY = """# Inventory

| ID | Title | Deps | Downstream | Status |
|---|---|---|---|---|
| `ENC-001` | Encounter Distance | — | — | Unresearched |
| `ENC-005` | Retreat, Pursuit & Evasion | `EXP-002` | — | Stage A accepted. Needs `ENC-001`. |
"""


def _packet(page_lines: str, seams: str = "ENC-005") -> str:
    return f"""# `ENC-001` — Encounter Distance — Stage-A Evidence

```text
PACKET-STATUS
RULE-ID:              ENC-001
INDEPENDENT-REVIEW:   PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
RECOMMENDATION:       EVIDENCE READY FOR HUMAN REVIEW
```

## 1. Scope and Seams
Owns encounter-distance determination.

## 2. Primary Source

| Source | Access method | Role |
|---|---|---|
| Rules Cyclopedia | page images | authoritative |

## 3. Seeds

```text
SEEDS
SUBJECT-TERMS:  encounter distance
SEAMS:          {seams}
LEADS:          none
```

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

**Enumerated absences:** None recorded.

## 7. Transcriptions

```text
TRANSCRIPTION p. 93
Setting and visibility selects the distance.
```

## 8. Evidence Map

| # | Page | Quote | Paraphrase | Object | Provenance | Confidence |
|---|---|---|---|---|---|---|
| E-1 | 93 | visibility selects the distance | | table | RC Explicit | DIRECT PRIMARY TEXT |

## 9. Cross-References

| From | Printed reference | To | Result |
|---|---|---|---|
| 93 | see page 98 | 98 | Contact |

## 10. Ownership and Dependency Routing

| Mechanic | Owner | Status | Basis |
|---|---|---|---|
| Surprise | `ENC-002` | UNRESEARCHED | routed |

## 11. Consequential Negative Claims

NEGATIVE CLAIMS: NONE

## 12. Targeted Falsification

```text
FALSIFICATION
CONCLUSION:   The table governs.
SOUGHT:       Ch. 7
RESULT:       Nothing competing.
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


ALL_PAGES = "\n".join(
    [
        "92: ROUTED_EXTERNAL ENC-002",
        "93: INSPECTED",
        "98: INSPECTED",
        "100: ROUTED_EXTERNAL ENC-005",
    ]
)


@pytest.fixture
def context(tmp_path: Path) -> RepoContext:
    evidence = tmp_path / "evidence"
    evidence.mkdir()
    (evidence / "ENC-005-evidence.md").write_text(NEIGHBOUR_PACKET, encoding="utf-8")
    inventory = tmp_path / "INVENTORY.md"
    inventory.write_text(INVENTORY, encoding="utf-8")
    return RepoContext(evidence_dir=evidence, inventory=inventory)


# --- The principal regression ---------------------------------------------


def test_p98_obligation_is_regenerated_after_being_deleted_from_the_packet(
    context: RepoContext,
) -> None:
    """THE probe from the independent review.

    p. 98 appears nowhere in the packet's own seed or disposition content. It
    must still be required, because the tool reads ENC-005's accepted packet.
    """
    without_98 = "\n".join(
        line for line in ALL_PAGES.splitlines() if not line.startswith("98:")
    )
    assert "98" not in without_98
    findings = lint_packet(_packet(without_98), "ENC-001-evidence.md", context)
    s019 = [f for f in findings if f.check == "S019"]
    assert s019, "the externally-derived p. 98 obligation did not survive its deletion"
    assert "p. 98" in s019[0].detail
    assert "ENC-005" in s019[0].detail, "the obligation must name the packet it came from"


def test_the_obligation_originates_outside_the_packet_entirely(context: RepoContext) -> None:
    """Derivation reads only INVENTORY and neighbour packets, never the packet."""
    seeds = derive_external_seeds("ENC-001", ["ENC-005"], context)
    assert {93, 98, 100, 92} <= set(seeds)
    assert all("ENC-005" in origin for page in seeds for origin in seeds[page])


def test_dispositioning_every_derived_page_passes(context: RepoContext) -> None:
    assert lint_packet(_packet(ALL_PAGES), "ENC-001-evidence.md", context) == []


# --- Neighbour resolution --------------------------------------------------


def test_inventory_edges_are_read_in_both_directions() -> None:
    """ENC-001's own row carries em dashes, so only the reverse edge exists.

    This is why INVENTORY is not treated as complete, and why declared seams
    supplement it rather than duplicating it.
    """
    # ENC-001's own row names nothing, so only the reverse edge from ENC-005's
    # row -- which names ENC-001 in its notes -- reaches it.
    assert inventory_neighbours("ENC-001", INVENTORY) == {"ENC-005"}
    # ENC-005's row names both, so the forward edge carries them.
    forward = inventory_neighbours("ENC-005", INVENTORY)
    assert {"EXP-002", "ENC-001"} <= forward


def test_a_declared_seam_supplements_inventory(context: RepoContext) -> None:
    from_inventory = derive_external_seeds("ENC-001", [], context)
    assert 98 in from_inventory, "the reverse INVENTORY edge alone should reach ENC-005"


def test_accepted_packets_are_resolved_by_rule_id(context: RepoContext) -> None:
    found = accepted_packets(["ENC-005", "NOPE-999"], context.evidence_dir)
    assert list(found) == ["ENC-005"]


# --- Conclusions are not inherited ----------------------------------------


def test_only_the_page_obligation_is_inherited_not_the_interpretation(
    context: RepoContext,
) -> None:
    """ENC-005's packet contains a wrong claim -- that the table is
    "light-keyed". ENC-001 refuted that against primary text. The seed must
    carry the page and nothing else, so the refutation stays possible.
    """
    assert "light-keyed" in NEIGHBOUR_PACKET
    seeds = derive_external_seeds("ENC-001", ["ENC-005"], context)
    blob = repr(seeds)
    assert "light-keyed" not in blob
    assert "Contact" not in blob
    assert all(isinstance(page, int) for page in seeds)
    for origins in seeds.values():
        assert all(origin.startswith("ENC-005 (") for origin in origins)


def test_cited_pages_extracts_only_integers() -> None:
    assert cited_pages(NEIGHBOUR_PACKET) == {92, 93, 98, 100}


# --- Malformed input fails loudly -----------------------------------------


def test_a_malformed_seam_declaration_fails_rather_than_parsing_to_nothing(
    context: RepoContext,
) -> None:
    """A dropped value used to yield an empty set and a clean run."""
    with pytest.raises(SeedInputError):
        lint_evidence._declared({"SEAMS": ","}, "SEAMS")


def test_a_malformed_seam_in_a_packet_is_reported(context: RepoContext) -> None:
    findings = lint_packet(_packet(ALL_PAGES, seams=","), "ENC-001-evidence.md", context)
    assert any(f.check == "S019" for f in findings)


def test_an_explicit_none_is_distinguishable_from_a_typo() -> None:
    assert lint_evidence._declared({"SEAMS": "none"}, "SEAMS") == []
    with pytest.raises(SeedInputError):
        lint_evidence._declared({"SEAMS": ";;"}, "SEAMS")


# --- Field-specific vocabulary (M-3) ---------------------------------------


def test_an_open_question_may_not_borrow_the_page_vocabulary(context: RepoContext) -> None:
    broken = _packet(ALL_PAGES).replace(
        "RETAINED AS GENUINE SOURCE AMBIGUITY", "INSPECTED"
    )
    findings = lint_packet(broken, "ENC-001-evidence.md", context)
    assert any(f.check == "S016" for f in findings)


def test_a_governing_object_may_not_borrow_the_closure_vocabulary(
    context: RepoContext,
) -> None:
    broken = _packet(ALL_PAGES).replace(
        "| Encounter Distances Table | 93 | table | GOVERNING | |",
        "| Encounter Distances Table | 93 | table | CONFIRMED OUT OF SCOPE | |",
    )
    findings = lint_packet(broken, "ENC-001-evidence.md", context)
    assert any(f.check == "S016" for f in findings)


# --- Quote/paraphrase cardinality (M-5) ------------------------------------


def test_exactly_one_of_quote_or_paraphrase(context: RepoContext) -> None:
    row = "| E-1 | 93 | visibility selects the distance | | table | RC Explicit | DIRECT PRIMARY TEXT |"  # noqa: E501
    quote_only = _packet(ALL_PAGES)
    assert lint_packet(quote_only, "ENC-001-evidence.md", context) == []

    para_only = quote_only.replace(
        row, row.replace("| visibility selects the distance | |", "| | paraphrased |")
    )
    para_findings = lint_packet(para_only, "ENC-001-evidence.md", context)
    assert not [f for f in para_findings if f.check == "S010"]

    both = quote_only.replace(
        row, row.replace("selects the distance | |", "selects the distance | also summarised |")
    )
    assert any(f.check == "S010" for f in lint_packet(both, "ENC-001-evidence.md", context))

    neither = quote_only.replace(
        row, row.replace("| visibility selects the distance | |", "| | |")
    )
    assert any(f.check == "S010" for f in lint_packet(neither, "ENC-001-evidence.md", context))


# --- RULE-ID may not be the packet's own authority over its obligations -----
#
# The closure review's blocking finding: RULE-ID came from PACKET-STATUS, was
# never corroborated, and a one-character typo derived zero pages and linted
# clean. Validation now takes two confirmations the packet does not control --
# the filename it was saved under, and INVENTORY.md.


def test_a_matching_registered_rule_id_is_valid() -> None:
    assert validate_rule_id("ENC-001", "ENC-001-evidence.md", INVENTORY) == "ENC-001"


def test_a_rule_id_absent_from_inventory_fails() -> None:
    with pytest.raises(RuleIdError, match="no INVENTORY"):
        validate_rule_id("ENC-999", "ENC-999-evidence.md", INVENTORY)


def test_a_rule_id_disagreeing_with_the_filename_fails() -> None:
    with pytest.raises(RuleIdError, match="does not match"):
        validate_rule_id("ENC-999", "ENC-001-evidence.md", INVENTORY)


def test_a_one_character_typo_fails_and_is_not_repaired() -> None:
    """ENC-00I is not ENC-001. Nothing is inferred or corrected."""
    with pytest.raises(RuleIdError):
        validate_rule_id("ENC-00I", "ENC-001-evidence.md", INVENTORY)


def test_a_valid_looking_but_unregistered_rule_id_fails() -> None:
    with pytest.raises(RuleIdError, match="no INVENTORY"):
        validate_rule_id("ENC-007", "ENC-007-evidence.md", INVENTORY)


def test_rule_id_is_read_from_the_filename_not_the_packet() -> None:
    assert rule_id_from_filename("ENC-001-evidence.md") == "ENC-001"
    assert rule_id_from_filename("ENC-001-evidence-remediated.md") == "ENC-001"
    assert rule_id_from_filename("notes.md") is None


def test_inventory_rows_define_registered_ids_but_mentions_do_not() -> None:
    """ENC-005's row mentions ENC-001; that makes ENC-001 a neighbour, not an
    entry. Only a row's own first ID registers it.
    """
    assert inventory_rule_ids(INVENTORY) == {"ENC-001", "ENC-005"}


@pytest.mark.parametrize("bad", ["ENC-999", "ENC-00I", "EXP-404"])
def test_changing_only_rule_id_cannot_empty_the_obligation_set(
    context: RepoContext, bad: str
) -> None:
    """THE invariant. A packet-authored edit must not silently buy an empty
    obligation set. Before this fix each of these linted clean with zero
    external seeds; now each fails loudly and derivation never runs.
    """
    good = lint_packet(_packet(ALL_PAGES), "ENC-001-evidence.md", context)
    assert good == [], "the honest packet should pass"

    tampered = _packet(ALL_PAGES).replace(
        "RULE-ID:              ENC-001", f"RULE-ID:              {bad}"
    )
    findings = lint_packet(tampered, "ENC-001-evidence.md", context)
    assert any(f.check == "S020" for f in findings), f"{bad} must not pass unchallenged"


def test_a_tampered_rule_id_fails_even_with_every_page_removed(
    context: RepoContext,
) -> None:
    """The two failure modes cannot be combined into a clean run: deleting the
    dispositions AND redirecting the Rule ID still fails.
    """
    tampered = _packet("91: INSPECTED").replace(
        "RULE-ID:              ENC-001", "RULE-ID:              ENC-999"
    )
    findings = lint_packet(tampered, "ENC-001-evidence.md", context)
    assert any(f.check == "S020" for f in findings)


def test_a_valid_packet_still_derives_the_real_pilot_pages() -> None:
    """Validation gates derivation; it must not weaken it. Against the real
    repository, the honest ENC-001 packet still derives pp. 93, 98 and 100.
    """
    repo = RepoContext.default()
    assert validate_rule_id("ENC-001", "ENC-001-evidence.md", repo.inventory_text())
    seeds = derive_external_seeds("ENC-001", [], repo)
    assert {93, 98, 100} <= set(seeds)
