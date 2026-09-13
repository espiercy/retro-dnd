"""CHAR-002 approved contract cases E1-E22 and E24-E28.

Canonical owner of 27 of the card's 30 approved deterministic cases, per
docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §12's ownership ledger.
Each appears exactly once, under its own case ID, in the card's order.

E23, E29 and E30 are deliberately NOT here. Their canonical owners are the
Slice F cross-card work: E29 and E30 are executable composition tests, and
E23 is a documented calling-contract conformance case (plan §12.2-§12.3).

A clearly separated implementation/coverage section follows at the end.
Those tests are NOT approved contract cases and must not be counted among
the 189.
"""

import ast
import inspect
from collections.abc import Mapping

import pytest

from rules.character_creation import race_and_class_eligibility
from rules.character_creation.ability import Ability, AbilityScores
from rules.character_creation.character_class import CharacterClass
from rules.character_creation.race_and_class_eligibility import (
    Eligibility,
    creation_minimums,
    eligibility,
    eligible_classes,
    prime_requisites,
)

_HUMAN_CLASSES = frozenset(
    {
        CharacterClass.CLERIC,
        CharacterClass.FIGHTER,
        CharacterClass.MAGIC_USER,
        CharacterClass.THIEF,
    }
)

_EXPECTED_PUBLIC_SURFACE = frozenset(
    {
        "Eligibility",
        "eligibility",
        "eligible_classes",
        "prime_requisites",
        "creation_minimums",
    }
)


def _scores(
    strength: int = 3,
    intelligence: int = 3,
    wisdom: int = 3,
    dexterity: int = 3,
    constitution: int = 3,
    charisma: int = 3,
) -> AbilityScores:
    """Scores in RC's order: Str, Int, Wis, Dex, Con, Cha."""
    return AbilityScores(
        strength, intelligence, wisdom, dexterity, constitution, charisma
    )


def _imported_modules() -> set[str]:
    """Every module name this card's source imports, from its own AST."""
    tree = ast.parse(inspect.getsource(race_and_class_eligibility))
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            names.add(node.module)
    return names


# --- Human classes are unconditional -------------------------------------


def test_e1_all_scores_3() -> None:
    scores = _scores()
    assert eligible_classes(scores) == _HUMAN_CLASSES
    for cls in (
        CharacterClass.DWARF,
        CharacterClass.ELF,
        CharacterClass.HALFLING,
        CharacterClass.MYSTIC,
    ):
        assert eligibility(scores, cls) is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    assert (
        eligibility(scores, CharacterClass.DRUID)
        is Eligibility.NOT_ELIGIBLE_AT_CREATION
    )


def test_e2_all_scores_18() -> None:
    scores = _scores(18, 18, 18, 18, 18, 18)
    assert eligible_classes(scores) == set(CharacterClass) - {CharacterClass.DRUID}
    assert (
        eligibility(scores, CharacterClass.DRUID)
        is Eligibility.NOT_ELIGIBLE_AT_CREATION
    )


def test_e3_the_four_human_classes_are_always_present_and_the_set_is_never_empty() -> (
    None
):
    for scores in (
        _scores(),
        _scores(18, 18, 18, 18, 18, 18),
        _scores(3, 9, 13, 8, 12, 5),
        _scores(11, 4, 7, 16, 8, 14),
    ):
        available = eligible_classes(scores)
        assert available >= _HUMAN_CLASSES
        assert available


# --- Demihuman boundaries ------------------------------------------------


def test_e4_dwarf_constitution_9_is_eligible() -> None:
    assert (
        eligibility(_scores(constitution=9), CharacterClass.DWARF)
        is Eligibility.ELIGIBLE
    )


def test_e5_dwarf_constitution_8_is_not_eligible_whatever_else_is_rolled() -> None:
    scores = _scores(18, 18, 18, 18, 8, 18)
    assert (
        eligibility(scores, CharacterClass.DWARF)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )
    assert CharacterClass.DWARF not in eligible_classes(scores)


def test_e6_elf_intelligence_9_is_eligible() -> None:
    assert (
        eligibility(_scores(intelligence=9), CharacterClass.ELF) is Eligibility.ELIGIBLE
    )


def test_e7_elf_intelligence_8_is_not_eligible() -> None:
    scores = _scores(18, 8, 18, 18, 18, 18)
    assert (
        eligibility(scores, CharacterClass.ELF)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )


def test_e8_halfling_both_gates_at_the_boundary_is_eligible() -> None:
    scores = _scores(dexterity=9, constitution=9)
    assert eligibility(scores, CharacterClass.HALFLING) is Eligibility.ELIGIBLE


def test_e9_halfling_requirements_are_conjunctive_constitution_fails() -> None:
    scores = _scores(dexterity=9, constitution=8)
    assert (
        eligibility(scores, CharacterClass.HALFLING)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )


def test_e10_halfling_requirements_are_conjunctive_dexterity_fails() -> None:
    scores = _scores(dexterity=8, constitution=9)
    assert (
        eligibility(scores, CharacterClass.HALFLING)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )


# --- Mystic boundaries ---------------------------------------------------


def test_e11_mystic_both_gates_at_the_boundary_is_eligible() -> None:
    scores = _scores(wisdom=13, dexterity=13)
    assert eligibility(scores, CharacterClass.MYSTIC) is Eligibility.ELIGIBLE


def test_e12_mystic_dexterity_12_is_not_eligible() -> None:
    scores = _scores(wisdom=13, dexterity=12)
    assert (
        eligibility(scores, CharacterClass.MYSTIC)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )


def test_e13_mystic_wisdom_12_is_not_eligible() -> None:
    scores = _scores(wisdom=12, dexterity=13)
    assert (
        eligibility(scores, CharacterClass.MYSTIC)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )


def test_e14_mystic_strength_is_a_prime_requisite_not_a_gate() -> None:
    scores = _scores(strength=3, wisdom=18, dexterity=18)
    assert eligibility(scores, CharacterClass.MYSTIC) is Eligibility.ELIGIBLE
    assert Ability.STRENGTH in prime_requisites(CharacterClass.MYSTIC)
    assert Ability.STRENGTH not in creation_minimums(CharacterClass.MYSTIC)


# --- Prime requisites are inert ------------------------------------------


def test_e15_cleric_with_wisdom_3_is_eligible() -> None:
    scores = _scores(18, 18, 3, 18, 18, 18)
    assert eligibility(scores, CharacterClass.CLERIC) is Eligibility.ELIGIBLE
    assert Ability.WISDOM in prime_requisites(CharacterClass.CLERIC)
    assert not creation_minimums(CharacterClass.CLERIC)


def test_e16_elf_with_strength_3_is_eligible_only_intelligence_is_tested() -> None:
    scores = _scores(3, 9, 12, 12, 12, 12)
    assert eligibility(scores, CharacterClass.ELF) is Eligibility.ELIGIBLE
    assert Ability.STRENGTH in prime_requisites(CharacterClass.ELF)
    assert dict(creation_minimums(CharacterClass.ELF)) == {Ability.INTELLIGENCE: 9}


def test_e17_no_eligibility_decision_reads_the_experience_bonuses_table() -> None:
    # The p. 12 Experience Bonuses and Penalties table establishes what
    # prime requisites *do* — it belongs to ADV-001 and plays no part here.
    assert frozenset(race_and_class_eligibility.__all__) == _EXPECTED_PUBLIC_SURFACE
    assert not [
        name
        for name in _EXPECTED_PUBLIC_SURFACE
        if "EXPERIENCE" in name.upper() or "BONUS" in name.upper()
    ]
    assert not [
        module
        for module in _imported_modules()
        if "experience" in module or "adv" in module.split(".")
    ]


# --- Druid ---------------------------------------------------------------


def test_e18_druid_reason_differs_from_a_failed_ability_requirement() -> None:
    # Even with Wisdom 18 — the Druid's prime requisite — and every other
    # score maxed, the Druid reports the at-creation reason.
    assert (
        eligibility(_scores(18, 18, 18, 18, 18, 18), CharacterClass.DRUID)
        is Eligibility.NOT_ELIGIBLE_AT_CREATION
    )
    # The other ineligible reason is real and distinct: a genuinely
    # ability-gated class reports *that* one instead.
    assert (
        eligibility(_scores(18, 18, 18, 18, 8, 18), CharacterClass.DWARF)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )
    # No score array can satisfy the Druid: its requirement is 9th level
    # as a cleric, not an ability threshold.
    assert not creation_minimums(CharacterClass.DRUID)


def test_e19_druid_is_never_available_as_a_starting_class() -> None:
    for scores in (_scores(), _scores(18, 18, 18, 18, 18, 18)):
        assert CharacterClass.DRUID not in eligible_classes(scores)
        assert (
            eligibility(scores, CharacterClass.DRUID)
            is Eligibility.NOT_ELIGIBLE_AT_CREATION
        )


# --- Ordering ------------------------------------------------------------


def test_e20_no_trade_can_make_a_dwarf_candidate_with_constitution_8_eligible() -> None:
    # The Dwarf's only gate is Constitution, and Constitution is not one of
    # its prime requisites — so it can never be a trade target. (The trade's
    # own restrictions are CHAR-001's and are enforced in Slice D; the
    # eligibility-side fact is here.)
    scores = _scores(18, 18, 18, 18, 8, 18)
    assert dict(creation_minimums(CharacterClass.DWARF)) == {Ability.CONSTITUTION: 9}
    assert Ability.CONSTITUTION not in prime_requisites(CharacterClass.DWARF)
    assert (
        eligibility(scores, CharacterClass.DWARF)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )


def test_e21_this_card_can_never_consume_adjusted_post_trade_scores() -> None:
    # It takes an AbilityScores and nothing else — no stage, phase or
    # provenance parameter — and it cannot obtain adjusted scores itself,
    # because it does not import the card that produces them.
    assert list(inspect.signature(eligibility).parameters) == ["scores", "cls"]
    assert not [
        module
        for module in _imported_modules()
        if "ability_score_generation" in module
    ]


def test_e22_raising_a_fighters_strength_does_not_change_its_eligibility() -> None:
    before = _scores(strength=12, intelligence=12, wisdom=12, dexterity=12)
    after = before.replace({Ability.STRENGTH: 13})
    assert eligibility(before, CharacterClass.FIGHTER) is Eligibility.ELIGIBLE
    assert eligibility(after, CharacterClass.FIGHTER) is Eligibility.ELIGIBLE
    assert eligible_classes(before) == eligible_classes(after)


# --- Guard ---------------------------------------------------------------


def test_e24_druid_transition_requirements_are_not_answered_here() -> None:
    # Out of scope: the transition directs to CHAR-013/ADV-002 and remains
    # P1 — DEFER FOR HUMAN GOVERNANCE. No Rule ID is assigned, and nothing
    # about it is discoverable through this module.
    assert frozenset(race_and_class_eligibility.__all__) == _EXPECTED_PUBLIC_SURFACE
    assert not [
        name
        for name in dir(race_and_class_eligibility)
        if not name.startswith("_")
        and any(
            word in name.upper()
            for word in ("TRANSITION", "WOODLAND", "MEDITAT", "CHALLENGE", "DRUID")
        )
    ]
    # The Druid result is a bare enum member; it carries no transition data.
    result = eligibility(_scores(), CharacterClass.DRUID)
    assert isinstance(result, Eligibility)


# --- Chapter 13 switch (SR-3) --------------------------------------------


def test_e25_an_authorized_switch_can_establish_the_elf_intelligence_gate() -> None:
    # As-rolled Str 16, Int 8; the switch moves the highest score into
    # Intelligence, an Elf prime requisite. This card evaluates the result.
    after_switch = _scores(strength=8, intelligence=16)
    assert eligibility(after_switch, CharacterClass.ELF) is Eligibility.ELIGIBLE
    assert Ability.INTELLIGENCE in prime_requisites(CharacterClass.ELF)


def test_e26_without_a_switch_eligibility_scores_equal_the_as_rolled_scores() -> None:
    as_rolled = _scores(strength=16, intelligence=8)
    assert (
        eligibility(as_rolled, CharacterClass.ELF)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )


def test_e27_no_switch_can_reach_the_dwarf_constitution_gate() -> None:
    # The switch's destination must be a prime requisite; the Dwarf's is
    # Strength. Constitution is unreachable, so Con 8 stays Con 8.
    assert Ability.CONSTITUTION not in prime_requisites(CharacterClass.DWARF)
    after_switch = _scores(strength=18, constitution=8)
    assert (
        eligibility(after_switch, CharacterClass.DWARF)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )


def test_e28_no_switch_can_reach_the_mystic_wisdom_gate() -> None:
    # Wis 12, Dex 11, Cha 17: the switch reaches Dexterity, a Mystic prime
    # requisite, never Wisdom. Wisdom 12 remains, so the Mystic stays out.
    assert Ability.WISDOM not in prime_requisites(CharacterClass.MYSTIC)
    after_switch = _scores(wisdom=12, dexterity=17, charisma=11)
    assert (
        eligibility(after_switch, CharacterClass.MYSTIC)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )


# =========================================================================
# Implementation / coverage tests — NOT approved contract cases.
# These exercise table ownership, immutability and dependency boundaries.
# They must not be counted among the 189 approved deterministic cases.
# =========================================================================


def test_every_class_has_a_prime_requisite_and_a_minimum_table() -> None:
    for cls in CharacterClass:
        assert prime_requisites(cls)
        assert isinstance(creation_minimums(cls), Mapping)


def test_the_full_prime_requisite_table_matches_rc_page_7() -> None:
    assert {cls: prime_requisites(cls) for cls in CharacterClass} == {
        CharacterClass.CLERIC: frozenset({Ability.WISDOM}),
        CharacterClass.FIGHTER: frozenset({Ability.STRENGTH}),
        CharacterClass.MAGIC_USER: frozenset({Ability.INTELLIGENCE}),
        CharacterClass.THIEF: frozenset({Ability.DEXTERITY}),
        CharacterClass.DWARF: frozenset({Ability.STRENGTH}),
        CharacterClass.ELF: frozenset({Ability.STRENGTH, Ability.INTELLIGENCE}),
        CharacterClass.HALFLING: frozenset({Ability.STRENGTH, Ability.DEXTERITY}),
        CharacterClass.MYSTIC: frozenset({Ability.STRENGTH, Ability.DEXTERITY}),
        CharacterClass.DRUID: frozenset({Ability.WISDOM}),
    }


def test_the_full_creation_minimum_table_matches_rc_page_7() -> None:
    assert {cls: dict(creation_minimums(cls)) for cls in CharacterClass} == {
        CharacterClass.CLERIC: {},
        CharacterClass.FIGHTER: {},
        CharacterClass.MAGIC_USER: {},
        CharacterClass.THIEF: {},
        CharacterClass.DWARF: {Ability.CONSTITUTION: 9},
        CharacterClass.ELF: {Ability.INTELLIGENCE: 9},
        CharacterClass.HALFLING: {Ability.DEXTERITY: 9, Ability.CONSTITUTION: 9},
        CharacterClass.MYSTIC: {Ability.WISDOM: 13, Ability.DEXTERITY: 13},
        CharacterClass.DRUID: {},
    }


def test_creation_minimums_cannot_be_mutated_by_a_caller() -> None:
    minimums = creation_minimums(CharacterClass.DWARF)
    with pytest.raises(TypeError):
        minimums[Ability.STRENGTH] = 18  # type: ignore[index]
    assert dict(creation_minimums(CharacterClass.DWARF)) == {Ability.CONSTITUTION: 9}


def test_eligibility_result_is_a_closed_three_value_set() -> None:
    assert len(Eligibility) == 3
    assert set(Eligibility) == {
        Eligibility.ELIGIBLE,
        Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT,
        Eligibility.NOT_ELIGIBLE_AT_CREATION,
    }


def test_no_char_007_dependency_exists() -> None:
    # Every gate is a raw score; an ability score of 13 means 13, never
    # adjustment +1 (card §4.1, Open Questions).
    assert not [
        module for module in _imported_modules() if "ability_score_effects" in module
    ]


def test_no_rng_dependency_exists() -> None:
    assert not [
        module
        for module in _imported_modules()
        if module == "random" or module.split(".")[0] == "rng"
    ]
