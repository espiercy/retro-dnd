"""CHAR-001 §5 approved contract cases H1-H6 (Chapter 10).

Canonical owner of the six Chapter 10 cases, per
docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §12:

    runtime / executable        5   H1-H5
    static / import-graph       1   H6
                               ---
                                6

**These are CHAR-001's H-series, not CHAR-003's H1-H42**, which live in
test_hit_points_and_hit_dice.py. Every test name here is qualified
``char001`` so the two runs can never be confused in a failure report.

A clearly separated implementation/coverage section follows at the end.
Those tests are NOT approved contract cases.
"""

import ast
import inspect

import pytest

from rng import RollSequenceExhaustedError, ScriptedRNG
from rules.character_creation import (
    ability_score_generation,
    high_level_ability_score_generation,
)
from rules.character_creation.ability import Ability
from rules.character_creation.errors import (
    AbilityScoreDomainError,
    CharacterCreationError,
    PointAllocationError,
)
from rules.character_creation.high_level_ability_score_generation import (
    allocate_points,
    assign_scores,
    roll_and_keep_six,
    roll_point_allocation_total,
)

_ALL_ABILITIES = (
    Ability.STRENGTH,
    Ability.INTELLIGENCE,
    Ability.WISDOM,
    Ability.DEXTERITY,
    Ability.CONSTITUTION,
    Ability.CHARISMA,
)


def _three_d6_for(total: int) -> list[int]:
    """Three d6 faces summing to ``total`` (3-18)."""
    first = min(6, total - 2)
    second = min(6, total - first - 1)
    return [first, second, total - first - second]


def _stream(totals: list[int]) -> list[int]:
    """A d6 stream producing each 3d6 total in turn."""
    return [face for total in totals for face in _three_d6_for(total)]


def _imports_of(module: object) -> set[str]:
    """Every module name ``module``'s source imports, from its own AST."""
    tree = ast.parse(inspect.getsource(module))  # type: ignore[arg-type]
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            names.add(node.module)
    return names


# --- First Method --------------------------------------------------------


def test_char001_h1_eight_rolls_keep_the_six_best() -> None:
    rolled = [18, 17, 16, 15, 14, 13, 12, 11]
    kept = roll_and_keep_six(ScriptedRNG(_stream(rolled)))
    # The six best are retained and the two lowest discarded.
    assert sorted(kept, reverse=True) == [18, 17, 16, 15, 14, 13]
    assert 12 not in kept
    assert 11 not in kept
    # The tuple's order is a representation only: assignment is the
    # player's, and the same retained values support different characters.
    fighterish = assign_scores(kept, _ALL_ABILITIES)
    magic_userish = assign_scores(
        kept,
        (
            Ability.INTELLIGENCE,
            Ability.STRENGTH,
            Ability.WISDOM,
            Ability.DEXTERITY,
            Ability.CONSTITUTION,
            Ability.CHARISMA,
        ),
    )
    assert fighterish.strength == 18
    assert magic_userish.intelligence == 18
    assert fighterish != magic_userish


def test_char001_h2_exactly_twenty_four_d6_draws_are_consumed() -> None:
    # Eight 3d6 expressions, not the six of ordinary generation.
    rng = ScriptedRNG(_stream([12] * 8))
    roll_and_keep_six(rng)
    with pytest.raises(RollSequenceExhaustedError):
        rng.roll_die(6)


# --- Second Method -------------------------------------------------------


def test_char001_h3_point_total_is_sixty_plus_five_d6() -> None:
    rng = ScriptedRNG([3, 3, 3, 3, 3])
    assert roll_point_allocation_total(rng) == 75
    with pytest.raises(RollSequenceExhaustedError):
        rng.roll_die(6)


def test_char001_h4_an_allocated_score_above_18_is_rejected() -> None:
    # 19 + 18 + 14 + 8 + 8 + 8 = 75, so the sum is correct and the
    # rejection is unambiguously about the ability score.
    allocation = {
        Ability.STRENGTH: 19,
        Ability.INTELLIGENCE: 18,
        Ability.WISDOM: 14,
        Ability.DEXTERITY: 8,
        Ability.CONSTITUTION: 8,
        Ability.CHARISMA: 8,
    }
    assert sum(allocation.values()) == 75
    with pytest.raises(AbilityScoreDomainError, match="3 to 18"):
        allocate_points(75, allocation)


def test_char001_h5_an_allotment_outside_60_to_90_is_rejected() -> None:
    for total in (59, 91):
        with pytest.raises(PointAllocationError, match="60-90"):
            allocate_points(total, dict.fromkeys(_ALL_ABILITIES, 10))


# --- Separation from ordinary 1st-level generation -----------------------


def test_char001_h6_chapter_10_is_unreachable_from_ordinary_generation() -> None:
    # STATIC / IMPORT-GRAPH CONFORMANCE. CHAR-001 §1 remains the only
    # 1st-level generation path because the module that owns it does not
    # import this one. Asserted from the AST, not by source-text matching.
    assert not [
        module
        for module in _imports_of(ability_score_generation)
        if "high_level_ability_score_generation" in module
    ]


# =========================================================================
# Implementation / coverage tests — NOT approved contract cases.
# =========================================================================


def test_retained_scores_keep_their_roll_order() -> None:
    # Roll order, not a descending sort -- so the tuple cannot be mistaken
    # for an assignment rule.
    kept = roll_and_keep_six(ScriptedRNG(_stream([10, 4, 17, 3, 12, 9, 15, 6])))
    assert kept == (10, 17, 12, 9, 15, 6)


def test_equal_values_straddling_the_cutoff_retain_the_same_multiset() -> None:
    # Two 7s straddle the six/two cut. Which is dropped is mechanically
    # irrelevant; no gameplay tie-break is invented.
    kept = roll_and_keep_six(ScriptedRNG(_stream([7, 7, 12, 13, 14, 15, 16, 5])))
    assert sorted(kept) == [7, 12, 13, 14, 15, 16]


def test_assignment_rejects_the_wrong_number_of_retained_scores() -> None:
    with pytest.raises(ValueError, match="retained scores"):
        assign_scores((10, 10, 10, 10, 10), _ALL_ABILITIES)


def test_assignment_rejects_a_duplicated_ability() -> None:
    with pytest.raises(ValueError, match="exactly once"):
        assign_scores(
            (10,) * 6,
            (
                Ability.STRENGTH,
                Ability.STRENGTH,
                Ability.WISDOM,
                Ability.DEXTERITY,
                Ability.CONSTITUTION,
                Ability.CHARISMA,
            ),
        )


def test_assignment_rejects_the_wrong_number_of_destinations() -> None:
    with pytest.raises(ValueError, match="exactly once"):
        assign_scores((10,) * 6, _ALL_ABILITIES[:5])


def test_assignment_uses_every_retained_score_exactly_once() -> None:
    kept = (3, 18, 12, 6, 15, 9)
    assigned = assign_scores(kept, _ALL_ABILITIES)
    assert sorted(assigned[ability] for ability in Ability) == sorted(kept)


def test_allocation_rejects_a_bool_total() -> None:
    # bool is a subtype of int, so static typing alone permits these.
    for total in (True, False):
        with pytest.raises(PointAllocationError, match="must not be a bool"):
            allocate_points(total, dict.fromkeys(_ALL_ABILITIES, 10))


def test_allocation_rejects_a_non_integer_total() -> None:
    for total in (59.5, "75", None):
        with pytest.raises(PointAllocationError, match="must be an int"):
            allocate_points(
                total,  # type: ignore[arg-type]
                dict.fromkeys(_ALL_ABILITIES, 10),
            )


def test_allocation_accepts_the_legal_total_boundaries() -> None:
    lowest = allocate_points(
        60, dict.fromkeys(_ALL_ABILITIES, 10)
    )
    assert sum(lowest[ability] for ability in Ability) == 60
    highest = allocate_points(
        90, dict.fromkeys(_ALL_ABILITIES, 15)
    )
    assert sum(highest[ability] for ability in Ability) == 90


def test_allocation_rejects_a_malformed_allocation_shape() -> None:
    missing = {ability: 12 for ability in _ALL_ABILITIES[:5]}
    with pytest.raises(PointAllocationError, match="exactly once"):
        allocate_points(60, missing)


def test_allocation_rejects_a_sum_that_does_not_match_the_total() -> None:
    with pytest.raises(PointAllocationError, match="exactly 75 points"):
        allocate_points(75, dict.fromkeys(_ALL_ABILITIES, 10))


def test_allocation_rejects_a_score_below_the_range() -> None:
    allocation = dict.fromkeys(_ALL_ABILITIES, 12)
    allocation[Ability.STRENGTH] = 2
    allocation[Ability.CHARISMA] = 22
    with pytest.raises(AbilityScoreDomainError, match="3 to 18"):
        allocate_points(84, allocation)


def test_assignment_and_allocation_consume_no_rng() -> None:
    empty = ScriptedRNG([])  # any draw attempt raises immediately
    assign_scores((10,) * 6, _ALL_ABILITIES)
    allocate_points(60, dict.fromkeys(_ALL_ABILITIES, 10))
    with pytest.raises(RollSequenceExhaustedError):
        empty.roll_die(6)


def test_chapter_10_does_not_import_ordinary_generation_either() -> None:
    # The separation is bidirectional: two sibling pure rule modules with
    # no coupling in either direction, and no circular dependency.
    assert not [
        module
        for module in _imports_of(high_level_ability_score_generation)
        if module.endswith("ability_score_generation")
    ]


def test_dependency_boundaries_are_held() -> None:
    modules = _imports_of(high_level_ability_score_generation)
    assert "rng" in modules
    assert not [
        module
        for module in modules
        if module == "random"
        or "race_and_class_eligibility" in module
        or "ability_score_effects" in module
        or "hit_points_and_hit_dice" in module
        or "rules.exploration" in module
    ]


def test_no_concrete_rng_implementation_is_imported() -> None:
    tree = ast.parse(inspect.getsource(high_level_ability_score_generation))
    imported = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
        for alias in node.names
    }
    assert "RNG" in imported
    assert not {"SeededRNG", "ScriptedRNG"} & imported


def test_no_generation_mode_or_orchestration_exists() -> None:
    forbidden = {
        "HighLevelCharacterCreator",
        "GenerationMethod",
        "GenerationMode",
        "CharacterBuilder",
        "CreationSession",
        "Player",
    }
    assert forbidden.isdisjoint(dir(high_level_ability_score_generation))


def test_point_allocation_error_is_a_character_creation_error() -> None:
    assert issubclass(PointAllocationError, CharacterCreationError)
