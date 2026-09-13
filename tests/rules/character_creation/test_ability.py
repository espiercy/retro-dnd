"""Implementation/coverage tests for the CLUSTER-002 shared primitives
(docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §6.1-§6.4, §7.1-§7.3).

NONE of the tests in this module is an approved Rule Card contract case.
The 189 approved deterministic cases are owned elsewhere, per the plan's
§12 ledger; `test_ability.py` is listed there with a count of 0. These are
implementation tests written to exercise the primitives' own behaviour and
to reach the 100%-per-file branch coverage `src/rules/` requires, and they
must not be inflated into new Rule Card cases.
"""

import dataclasses
import inspect

import pytest

from rules.character_creation.ability import (
    MAXIMUM_CREATION_SCORE,
    MINIMUM_CREATION_SCORE,
    Ability,
    AbilityScores,
)
from rules.character_creation.character_class import CharacterClass
from rules.character_creation.errors import (
    AbilityScoreDomainError,
    CharacterCreationError,
)


def _scores(
    strength: int = 10,
    intelligence: int = 10,
    wisdom: int = 10,
    dexterity: int = 10,
    constitution: int = 10,
    charisma: int = 10,
) -> AbilityScores:
    """A valid score set, with any ability overridable."""
    return AbilityScores(
        strength, intelligence, wisdom, dexterity, constitution, charisma
    )


# --- Ability: RC declaration order ---------------------------------------


def test_ability_has_exactly_six_members() -> None:
    assert len(Ability) == 6


def test_ability_preserves_rc_declaration_order() -> None:
    # RC p. 6 lists the six abilities in this order, and CHAR-001 §1
    # generates scores "in the order listed" (approved case G4).
    assert list(Ability) == [
        Ability.STRENGTH,
        Ability.INTELLIGENCE,
        Ability.WISDOM,
        Ability.DEXTERITY,
        Ability.CONSTITUTION,
        Ability.CHARISMA,
    ]


def test_ability_order_is_not_alphabetical() -> None:
    # Guards the one way declaration order could silently become wrong.
    alphabetical = sorted(Ability, key=lambda ability: ability.name)
    assert list(Ability) != alphabetical


# --- CharacterClass: identity only ---------------------------------------


def test_character_class_has_exactly_nine_members() -> None:
    assert len(CharacterClass) == 9


def test_character_class_membership_matches_rc_page_7() -> None:
    assert set(CharacterClass) == {
        CharacterClass.CLERIC,
        CharacterClass.FIGHTER,
        CharacterClass.MAGIC_USER,
        CharacterClass.THIEF,
        CharacterClass.DWARF,
        CharacterClass.ELF,
        CharacterClass.HALFLING,
        CharacterClass.MYSTIC,
        CharacterClass.DRUID,
    }


def test_character_class_carries_no_class_mechanics() -> None:
    # Identity only: no prime requisites, minimums, Hit Dice, level caps,
    # fixed HP gains, XP or special abilities (implementation plan §6.2).
    forbidden = {
        "prime_requisite",
        "prime_requisites",
        "minimum",
        "minimums",
        "hit_die",
        "hit_dice",
        "maximum_level",
        "name_level",
        "fixed_gain",
        "experience",
    }
    assert forbidden.isdisjoint(dir(CharacterClass.FIGHTER))


# --- AbilityScores: construction and validation --------------------------


def test_constructor_requires_all_six_scores() -> None:
    parameters = inspect.signature(AbilityScores).parameters
    assert list(parameters) == [
        "strength",
        "intelligence",
        "wisdom",
        "dexterity",
        "constitution",
        "charisma",
    ]
    assert all(
        parameter.default is inspect.Parameter.empty
        for parameter in parameters.values()
    )


def test_valid_scores_are_accepted() -> None:
    scores = _scores(strength=12, charisma=7)
    assert scores.strength == 12
    assert scores.charisma == 7


def test_minimum_creation_score_is_accepted() -> None:
    assert _scores(strength=MINIMUM_CREATION_SCORE).strength == 3


def test_maximum_creation_score_is_accepted() -> None:
    assert _scores(strength=MAXIMUM_CREATION_SCORE).strength == 18


def test_score_below_the_creation_minimum_is_rejected() -> None:
    # 2 is inside CHAR-007's adjustment domain but outside the creation
    # range AbilityScores represents (implementation plan §6.4).
    with pytest.raises(AbilityScoreDomainError, match="STRENGTH"):
        _scores(strength=2)


def test_score_above_the_creation_maximum_is_rejected() -> None:
    with pytest.raises(AbilityScoreDomainError, match="CHARISMA"):
        _scores(charisma=19)


def test_domain_error_is_a_character_creation_error() -> None:
    assert issubclass(AbilityScoreDomainError, CharacterCreationError)


def test_bool_is_rejected_as_a_score() -> None:
    # bool is a subclass of int, so it needs an explicit guard.
    with pytest.raises(ValueError, match="must be an int"):
        _scores(wisdom=True)


def test_non_int_is_rejected_as_a_score() -> None:
    with pytest.raises(ValueError, match="must be an int"):
        _scores(dexterity="12")  # type: ignore[arg-type]


def test_scores_are_immutable() -> None:
    scores = _scores()
    with pytest.raises(dataclasses.FrozenInstanceError):
        scores.strength = 15  # type: ignore[misc]


# --- AbilityScores: lookup, maximum, replacement -------------------------


def test_lookup_returns_each_ability_score() -> None:
    scores = AbilityScores(3, 4, 5, 6, 7, 8)
    assert [scores[ability] for ability in Ability] == [3, 4, 5, 6, 7, 8]


def test_maximum_returns_the_highest_score() -> None:
    assert AbilityScores(3, 4, 17, 6, 7, 8).maximum() == 17


def test_maximum_reports_a_tie_without_resolving_it() -> None:
    # CHAR-001 §6.2.1: ties are the caller's to resolve; this primitive
    # reports the value only and selects no source ability.
    assert AbilityScores(17, 17, 5, 6, 7, 8).maximum() == 17


def test_replace_returns_a_new_score_set() -> None:
    original = _scores()
    replaced = original.replace({Ability.STRENGTH: 15})
    assert replaced.strength == 15
    assert original.strength == 10
    assert replaced is not original


def test_replace_applies_several_changes() -> None:
    replaced = _scores().replace({Ability.WISDOM: 13, Ability.CHARISMA: 4})
    assert replaced.wisdom == 13
    assert replaced.charisma == 4
    assert replaced.strength == 10


def test_replace_with_no_changes_returns_an_equal_score_set() -> None:
    original = _scores()
    assert original.replace({}) == original


def test_replace_validates_the_result() -> None:
    with pytest.raises(AbilityScoreDomainError, match="INTELLIGENCE"):
        _scores().replace({Ability.INTELLIGENCE: 19})
