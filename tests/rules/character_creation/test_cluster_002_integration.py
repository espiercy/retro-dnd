"""CLUSTER-002 cross-card integration — Slice F.

Canonical owner of the last nine approved CLUSTER-002 cases, per
docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §12:

    executable cross-card composition   5   E29, E30, O1, O2, O4
    documented calling-contract         4   E23, S2, W7, O3
                                       ---
                                        9

The four calling-contract cases receive **no pytest function**. Each states
a fact about caller sequencing that a stateless pure operation cannot
observe, and the approved architecture keeps it that way: no phase,
creation state, completion flag or class-selected flag exists in
production. Their canonical evidence is the conformance table in
ISSUE-013, the production module contracts, and the positive-order
composition tests below. They are marked in place, in card order, with the
reason.

**This slice adds no production code.** These tests compose the real public
APIs of Slices A-E directly, in the approved order. No engine, creator,
builder, session, state object or test-only coordinator is introduced — the
tests demonstrate that independent rules components agree, they do not
create an application layer.

One non-contract composition regression follows the approved cases: the
producer/consumer proof from implementation plan §10.1. It is an
implementation test and is **not** one of the 189 approved cases.
"""

import pytest

from rng import ScriptedRNG
from rules.character_creation.ability import Ability, AbilityScores
from rules.character_creation.ability_score_effects import adjustment
from rules.character_creation.ability_score_generation import (
    apply_highest_score_switch,
    apply_trade,
    discard_may_be_offered,
    generate_ability_scores,
)
from rules.character_creation.character_class import CharacterClass
from rules.character_creation.errors import (
    AbilityScoreDomainError,
    ClassMinimumViolationError,
    IllegalTradeError,
    PrimeRequisiteCeilingError,
)
from rules.character_creation.race_and_class_eligibility import (
    Eligibility,
    eligibility,
)


def _scores(
    strength: int = 12,
    intelligence: int = 12,
    wisdom: int = 12,
    dexterity: int = 12,
    constitution: int = 12,
    charisma: int = 12,
) -> AbilityScores:
    """Scores in RC's order: Str, Int, Wis, Dex, Con, Cha."""
    return AbilityScores(
        strength, intelligence, wisdom, dexterity, constitution, charisma
    )


def _three_d6_for(total: int) -> list[int]:
    """Three d6 faces summing to ``total`` (3-18)."""
    first = min(6, total - 2)
    second = min(6, total - first - 1)
    return [first, second, total - first - second]


def _stream(totals: list[int]) -> list[int]:
    """A d6 stream producing each 3d6 total in turn."""
    return [face for total in totals for face in _three_d6_for(total)]


# Classes selectable at creation, each with an array that satisfies its
# creation minimums. The Druid is excluded because CHAR-002 makes it
# unselectable at creation, so "any selected class" cannot include it.
_SELECTABLE = {
    CharacterClass.CLERIC: _scores(),
    CharacterClass.FIGHTER: _scores(),
    CharacterClass.MAGIC_USER: _scores(),
    CharacterClass.THIEF: _scores(),
    CharacterClass.DWARF: _scores(),
    CharacterClass.ELF: _scores(),
    CharacterClass.HALFLING: _scores(),
    CharacterClass.MYSTIC: _scores(wisdom=15, dexterity=13),
}


# --- CHAR-002 E29 / E30 — the class-eligibility invariant ----------------


def test_e29_the_trade_may_not_lower_a_mystic_below_its_wisdom_minimum() -> None:
    # The Mystic qualifies on Wis 13 / Dex 13 ...
    qualified = _scores(strength=12, wisdom=13, dexterity=13)
    assert eligibility(qualified, CharacterClass.MYSTIC) is Eligibility.ELIGIBLE
    # ... and CHAR-001's trade refuses to take Wisdom to 12. CHAR-002's
    # result is an invariant the trade must preserve; the enforcement lives
    # in CHAR-001, and this case makes the requirement visible from the
    # card that owns the minimum.
    with pytest.raises(ClassMinimumViolationError, match="R10"):
        apply_trade(
            qualified, CharacterClass.MYSTIC, Ability.WISDOM, Ability.STRENGTH
        )


def test_e30_every_creation_minimum_survives_every_legal_trade() -> None:
    # Exhaustive over every selectable class and every donor/target pair:
    # whatever CHAR-001 permits, CHAR-002 still finds eligible afterwards.
    attempted = 0
    permitted = 0
    for cls, scores in _SELECTABLE.items():
        assert eligibility(scores, cls) is Eligibility.ELIGIBLE
        for donor in Ability:
            for target in Ability:
                attempted += 1
                try:
                    adjusted = apply_trade(scores, cls, donor, target)
                except (
                    IllegalTradeError,
                    ClassMinimumViolationError,
                    PrimeRequisiteCeilingError,
                ):
                    continue
                permitted += 1
                assert eligibility(adjusted, cls) is Eligibility.ELIGIBLE
    assert attempted == len(_SELECTABLE) * len(Ability) ** 2
    assert permitted > 0


# --- CHAR-001 O1 / O2 / O4 — ordering and composition --------------------


def test_o1_the_trade_cannot_establish_eligibility_for_any_class() -> None:
    # Constitution 8 keeps the Dwarf out, and no trade can change that.
    scores = _scores(strength=12, wisdom=15, constitution=8)
    assert (
        eligibility(scores, CharacterClass.DWARF)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )
    # A Fighter is chosen, and its trade raises Strength 12 -> 13 ...
    adjusted = apply_trade(
        scores, CharacterClass.FIGHTER, Ability.WISDOM, Ability.STRENGTH
    )
    assert adjusted.strength == 13
    # ... which establishes nothing. Contrast W1, where the *switch* can.
    assert (
        eligibility(adjusted, CharacterClass.DWARF)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )


def test_o2_a_switch_establishes_eligibility_then_the_trade_adjusts() -> None:
    # As-rolled, Intelligence 8 leaves the Elf out. ("Int 9" in the card
    # denotes the Elf's Intelligence-9 minimum: the switch must move the
    # *highest* score, so it establishes the minimum rather than landing
    # exactly on it.)
    as_rolled = _scores(strength=12, intelligence=8, wisdom=15)
    assert (
        eligibility(as_rolled, CharacterClass.ELF)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )
    # The authorized switch establishes the minimum ...
    switched = apply_highest_score_switch(
        as_rolled, CharacterClass.ELF, Ability.WISDOM, Ability.INTELLIGENCE
    )
    assert switched.intelligence == 15
    assert eligibility(switched, CharacterClass.ELF) is Eligibility.ELIGIBLE
    # ... the class is chosen, and the trade then operates as an ordinary
    # post-eligibility adjustment, raising Intelligence further.
    adjusted = apply_trade(
        switched, CharacterClass.ELF, Ability.STRENGTH, Ability.INTELLIGENCE
    )
    assert (adjusted.intelligence, adjusted.strength) == (16, 10)
    assert eligibility(adjusted, CharacterClass.ELF) is Eligibility.ELIGIBLE


def test_o4_a_discarded_character_restarts_before_any_later_step() -> None:
    # Generation produces an array that qualifies for discard ...
    discarded = generate_ability_scores(ScriptedRNG(_stream([8] * 6)))
    assert discard_may_be_offered(discarded) is True
    # ... the character is discarded, and generation restarts at §1. No
    # switch, eligibility evaluation or trade is performed for it: the
    # next steps below are reached only by the replacement array.
    replacement = generate_ability_scores(ScriptedRNG(_stream([12] * 6)))
    assert discard_may_be_offered(replacement) is False
    assert replacement != discarded
    assert eligibility(replacement, CharacterClass.FIGHTER) is Eligibility.ELIGIBLE
    adjusted = apply_trade(
        replacement, CharacterClass.FIGHTER, Ability.WISDOM, Ability.STRENGTH
    )
    assert adjusted.strength == 13


# =========================================================================
# DOCUMENTED CALLING-CONTRACT CONFORMANCE — no pytest functions.
#
# E23  A Chapter 13 switch applied AFTER a class is chosen is rejected.
#      apply_highest_score_switch receives scores and a destination; it has
#      no class-selected flag and cannot observe when it was called. The
#      approved caller sequence places the switch before eligibility and
#      class selection, and O2 above demonstrates that order working.
#
# S2   A trade attempted AFTER creation completes is rejected (R9).
#      "Completed" is not observable from six integers and a class.
#      R9 is documented in ability_score_generation.py's module contract,
#      and no completion or phase state was added.
#
# W7   A switch attempted AFTER a class is chosen is rejected.
#      The same unobservability as E23, seen from CHAR-001's side.
#
# O3   A trade attempted BEFORE eligibility is evaluated is rejected.
#      apply_trade cannot observe whether CHAR-002 has run. O1, O2 and O4
#      above are the positive evidence that the canonical order works; no
#      Slice-F production wrapper was introduced to enforce it.
#
# Canonical evidence: the conformance table in ISSUE-013.
# =========================================================================


# =========================================================================
# Non-contract composition regression — NOT an approved case.
# =========================================================================


def test_char_001_never_emits_a_score_char_007_would_reject() -> None:
    """Implementation plan §10.1: the producer/consumer proof.

    CHAR-001 produces ability scores in 3-18; CHAR-007's adjustment lookup
    accepts 2-18. This regression exists because, before rule R11, the
    approved cluster admitted a trade result of 19 that CHAR-007 rejects —
    the Pre-Code blocker.
    """
    outputs: list[AbilityScores] = [
        generate_ability_scores(ScriptedRNG(_stream([3] * 6))),
        generate_ability_scores(ScriptedRNG(_stream([18] * 6))),
        generate_ability_scores(ScriptedRNG(_stream([10, 3, 18, 7, 12, 15]))),
    ]
    # A switch is a permutation, and a legal trade lands the target at most
    # on 18 -- the boundary the blocker turned on.
    outputs.append(
        apply_highest_score_switch(
            _scores(strength=16, intelligence=8),
            CharacterClass.ELF,
            Ability.STRENGTH,
            Ability.INTELLIGENCE,
        )
    )
    outputs.append(
        apply_trade(
            _scores(strength=17, wisdom=11),
            CharacterClass.FIGHTER,
            Ability.WISDOM,
            Ability.STRENGTH,
        )
    )
    for scores in outputs:
        for ability in Ability:
            # Every produced score is inside CHAR-007's accepted domain, so
            # the lookup answers rather than rejecting.
            adjustment(scores[ability])

    # R11 is what keeps 19 out of CHAR-001's output range ...
    with pytest.raises(PrimeRequisiteCeilingError, match="R11"):
        apply_trade(
            _scores(strength=18, wisdom=11),
            CharacterClass.FIGHTER,
            Ability.WISDOM,
            Ability.STRENGTH,
        )
    # ... and CHAR-007 would indeed have rejected it.
    with pytest.raises(AbilityScoreDomainError):
        adjustment(19)
