"""CHAR-001 approved contract cases owned by Slice D.

Canonical owner of 57 of the card's 69 approved cases, per
docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §12 (revision 4):

    runtime / executable   52   G1-G5, T1-T10, T12-T14, S3, M1-M5,
                                V1-V12, W1, W3-W5, D1-D6, D8, C1-C5
    static / API-shape      1   S1
    calling-contract        4   T11, W2, W6, D7  -- no pytest functions
                           ---
                            57

T11, W2, W6 and D7 each state a fact about **caller discretion** a
stateless pure operation cannot observe (plan §12.2.1): that the trade may
simply not be invoked; that a switch's *authorization* is the DM's or
policy's; that *at most one* switch is a caller obligation; and that the
player may retain a character the discard predicate says may be offered.
They receive no ceremonial pytest function. Their evidence is this module's
production contract and the ISSUE-011 checklist. W6's *swap* clause does
have executable evidence, in the W-series and switch tests below — that
coverage is evidence for W6, not an additional approved case.

NOT owned here, and deliberately absent: S2, W7 (Slice F calling contract),
O1-O4 (Slice F), and H1-H6 (Chapter 10, Slice E).

A clearly separated implementation/coverage section follows at the end.
Those tests are NOT approved contract cases.
"""

import ast
import inspect

import pytest

from rng import RollSequenceExhaustedError, ScriptedRNG
from rules.character_creation import ability_score_generation
from rules.character_creation.ability import Ability, AbilityScores
from rules.character_creation.ability_score_generation import (
    apply_highest_score_switch,
    apply_trade,
    discard_may_be_offered,
    generate_ability_scores,
)
from rules.character_creation.character_class import CharacterClass
from rules.character_creation.errors import (
    CharacterCreationError,
    ClassMinimumViolationError,
    IllegalSwitchError,
    IllegalTradeError,
    PrimeRequisiteCeilingError,
)
from rules.character_creation.race_and_class_eligibility import (
    Eligibility,
    eligibility,
    prime_requisites,
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


def _imported_modules() -> set[str]:
    tree = ast.parse(inspect.getsource(ability_score_generation))
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            names.add(node.module)
    return names


# --- Generation ----------------------------------------------------------


def test_g1_three_threes_per_ability_gives_nine_across_the_board() -> None:
    scores = generate_ability_scores(ScriptedRNG([3] * 18))
    assert [scores[ability] for ability in Ability] == [9] * 6
    assert list(Ability) == [
        Ability.STRENGTH,
        Ability.INTELLIGENCE,
        Ability.WISDOM,
        Ability.DEXTERITY,
        Ability.CONSTITUTION,
        Ability.CHARISMA,
    ]


def test_g2_all_ones_gives_the_minimum_of_three() -> None:
    scores = generate_ability_scores(ScriptedRNG([1] * 18))
    assert [scores[ability] for ability in Ability] == [3] * 6


def test_g3_all_sixes_gives_the_maximum_of_eighteen() -> None:
    scores = generate_ability_scores(ScriptedRNG([6] * 18))
    assert [scores[ability] for ability in Ability] == [18] * 6


def test_g4_assignment_follows_roll_order_not_sorted_order() -> None:
    stream = [1, 1, 1, 6, 6, 6, 3, 4, 5, 2, 2, 2, 5, 5, 5, 4, 4, 4]
    scores = generate_ability_scores(ScriptedRNG(stream))
    assert [scores[ability] for ability in Ability] == [3, 18, 12, 6, 15, 12]
    # Sorted order would have put the 18 first; it does not.
    assert scores.strength == 3


def test_g5_exactly_eighteen_d6_draws_are_consumed() -> None:
    rng = ScriptedRNG([4] * 18)
    generate_ability_scores(rng)
    with pytest.raises(RollSequenceExhaustedError):
        rng.roll_die(6)


# --- Trade — legality boundaries -----------------------------------------


def test_t1_donor_landing_exactly_on_the_floor_is_legal() -> None:
    result = apply_trade(
        _scores(strength=12, wisdom=11),
        CharacterClass.FIGHTER,
        Ability.WISDOM,
        Ability.STRENGTH,
    )
    assert (result.strength, result.wisdom) == (13, 9)


def test_t2_donor_already_at_10_cannot_be_lowered() -> None:
    with pytest.raises(IllegalTradeError, match="R6/R7"):
        apply_trade(
            _scores(strength=12, wisdom=10),
            CharacterClass.FIGHTER,
            Ability.WISDOM,
            Ability.STRENGTH,
        )


def test_t3_donor_already_at_9_cannot_be_lowered() -> None:
    with pytest.raises(IllegalTradeError, match="R6/R7"):
        apply_trade(
            _scores(strength=12, wisdom=9),
            CharacterClass.FIGHTER,
            Ability.WISDOM,
            Ability.STRENGTH,
        )


def test_t4_constitution_cannot_be_exchanged() -> None:
    with pytest.raises(IllegalTradeError, match="R3"):
        apply_trade(
            _scores(strength=12, constitution=16),
            CharacterClass.FIGHTER,
            Ability.CONSTITUTION,
            Ability.STRENGTH,
        )


def test_t5_charisma_cannot_be_exchanged() -> None:
    with pytest.raises(IllegalTradeError, match="R3"):
        apply_trade(
            _scores(strength=12, charisma=16),
            CharacterClass.FIGHTER,
            Ability.CHARISMA,
            Ability.STRENGTH,
        )


def test_t6_dexterity_cannot_be_lowered() -> None:
    with pytest.raises(IllegalTradeError, match="R4"):
        apply_trade(
            _scores(strength=12, dexterity=16),
            CharacterClass.FIGHTER,
            Ability.DEXTERITY,
            Ability.STRENGTH,
        )


def test_t7_target_must_be_a_prime_requisite_of_the_chosen_class() -> None:
    with pytest.raises(IllegalTradeError, match="R1"):
        apply_trade(
            _scores(wisdom=12, strength=11),
            CharacterClass.CLERIC,
            Ability.STRENGTH,
            Ability.INTELLIGENCE,
        )


def test_t8_dexterity_may_be_raised_where_it_is_a_prime_requisite() -> None:
    result = apply_trade(
        _scores(dexterity=12, wisdom=15),
        CharacterClass.THIEF,
        Ability.WISDOM,
        Ability.DEXTERITY,
    )
    assert (result.dexterity, result.wisdom) == (13, 13)


def test_t9_a_two_prime_requisite_class_may_raise_either() -> None:
    scores = _scores(strength=12, dexterity=12, wisdom=15)
    first = apply_trade(
        scores, CharacterClass.HALFLING, Ability.WISDOM, Ability.DEXTERITY
    )
    second = apply_trade(
        first, CharacterClass.HALFLING, Ability.WISDOM, Ability.STRENGTH
    )
    assert (second.dexterity, second.strength, second.wisdom) == (13, 13, 11)


def test_t10_the_elf_may_raise_both_prime_requisites() -> None:
    scores = _scores(strength=12, intelligence=12, wisdom=15)
    first = apply_trade(
        scores, CharacterClass.ELF, Ability.WISDOM, Ability.STRENGTH
    )
    second = apply_trade(
        first, CharacterClass.ELF, Ability.WISDOM, Ability.INTELLIGENCE
    )
    assert (second.strength, second.intelligence, second.wisdom) == (13, 13, 11)


# T11 -- DOCUMENTED CALLING-CONTRACT CONFORMANCE, no pytest function.
# "Perform no trades -> adjusted scores = as-rolled scores (R8)."
# apply_trade cannot enforce a caller's decision not to invoke it, and
# AbilityScores is immutable, so an uninvoked trade changes nothing. See the
# module contract and ISSUE-011.


# --- Trade — RC's own worked examples (regression) -----------------------


def test_t12_rc_page_7_example_1_elf() -> None:
    scores = _scores(intelligence=12, strength=12, wisdom=13)
    first = apply_trade(
        scores, CharacterClass.ELF, Ability.WISDOM, Ability.STRENGTH
    )
    second = apply_trade(
        first, CharacterClass.ELF, Ability.WISDOM, Ability.INTELLIGENCE
    )
    assert (second.intelligence, second.strength, second.wisdom) == (13, 13, 9)


def test_t13_rc_page_7_example_2_cleric() -> None:
    scores = _scores(strength=15, wisdom=15)
    for _ in range(3):
        scores = apply_trade(
            scores, CharacterClass.CLERIC, Ability.STRENGTH, Ability.WISDOM
        )
    assert (scores.strength, scores.wisdom) == (9, 18)


def test_t14_a_further_trade_from_strength_9_is_rejected_on_the_donor_floor() -> None:
    scores = _scores(strength=9, wisdom=18)
    # The target would also breach R11 (18 -> 19); the donor floor is
    # checked first, so R6/R7 is what this case observes.
    with pytest.raises(IllegalTradeError, match="R6/R7"):
        apply_trade(
            scores, CharacterClass.CLERIC, Ability.STRENGTH, Ability.WISDOM
        )


# --- Prime-requisite ceiling (R11) ---------------------------------------


def test_c1_a_target_landing_exactly_on_18_is_legal() -> None:
    result = apply_trade(
        _scores(strength=17, wisdom=11),
        CharacterClass.FIGHTER,
        Ability.WISDOM,
        Ability.STRENGTH,
    )
    # Both boundaries exercised at once: target on the ceiling, donor on
    # the floor.
    assert (result.strength, result.wisdom) == (18, 9)


def test_c2_a_target_that_would_reach_19_is_rejected_by_r11_alone() -> None:
    # R1, R6 and R7 all permit this trade.
    with pytest.raises(PrimeRequisiteCeilingError, match="R11"):
        apply_trade(
            _scores(strength=18, wisdom=11),
            CharacterClass.FIGHTER,
            Ability.WISDOM,
            Ability.STRENGTH,
        )


def test_c3_one_prime_requisite_at_18_does_not_block_the_other() -> None:
    result = apply_trade(
        _scores(strength=18, intelligence=12, wisdom=15),
        CharacterClass.ELF,
        Ability.WISDOM,
        Ability.INTELLIGENCE,
    )
    assert (result.intelligence, result.wisdom) == (13, 13)


def test_c4_both_prime_requisites_at_18_leaves_no_legal_target() -> None:
    scores = _scores(strength=18, intelligence=18, wisdom=15)
    for target in (Ability.STRENGTH, Ability.INTELLIGENCE):
        with pytest.raises(PrimeRequisiteCeilingError, match="R11"):
            apply_trade(scores, CharacterClass.ELF, Ability.WISDOM, target)


def test_c5_r11_does_not_break_rc_own_worked_example() -> None:
    scores = _scores(strength=15, wisdom=15)
    for _ in range(3):
        scores = apply_trade(
            scores, CharacterClass.CLERIC, Ability.STRENGTH, Ability.WISDOM
        )
    assert (scores.strength, scores.wisdom) == (9, 18)


# --- Sequencing ----------------------------------------------------------


def test_s1_a_chosen_class_is_structurally_required() -> None:
    # STATIC / API-SHAPE CONFORMANCE. The prime requisite is undetermined
    # without a class, so chosen_class is a required parameter with no
    # default -- a trade without one is unconstructible, not a runtime
    # rejection. No NoClassSelectedError exists.
    parameters = inspect.signature(apply_trade).parameters
    assert list(parameters) == ["scores", "chosen_class", "donor", "target"]
    assert parameters["chosen_class"].default is inspect.Parameter.empty
    assert not [
        name for name in dir(ability_score_generation) if "NoClass" in name
    ]


def test_s3_no_trade_sequence_can_raise_a_dwarfs_constitution() -> None:
    scores = _scores(strength=18, constitution=8)
    assert Ability.CONSTITUTION not in prime_requisites(CharacterClass.DWARF)
    # Constitution cannot be a target (R1) ...
    with pytest.raises(IllegalTradeError, match="R1"):
        apply_trade(
            scores, CharacterClass.DWARF, Ability.WISDOM, Ability.CONSTITUTION
        )
    # ... and cannot be a donor (R3). No trade touches it at all.
    with pytest.raises(IllegalTradeError, match="R3"):
        apply_trade(
            scores, CharacterClass.DWARF, Ability.CONSTITUTION, Ability.STRENGTH
        )


# --- Mystic Dexterity trade (SR-2) ---------------------------------------


def test_m1_a_mystic_may_raise_dexterity() -> None:
    result = apply_trade(
        _scores(dexterity=13, strength=12, wisdom=15),
        CharacterClass.MYSTIC,
        Ability.WISDOM,
        Ability.DEXTERITY,
    )
    assert (result.dexterity, result.wisdom) == (14, 13)


def test_m2_a_mystic_may_raise_strength() -> None:
    result = apply_trade(
        _scores(strength=12, wisdom=15, dexterity=13),
        CharacterClass.MYSTIC,
        Ability.WISDOM,
        Ability.STRENGTH,
    )
    assert (result.strength, result.wisdom) == (13, 13)


def test_m3_a_mystic_may_never_lower_dexterity() -> None:
    with pytest.raises(IllegalTradeError, match="R4"):
        apply_trade(
            _scores(dexterity=16, strength=12, wisdom=15),
            CharacterClass.MYSTIC,
            Ability.DEXTERITY,
            Ability.STRENGTH,
        )


def test_m4_wisdom_is_a_mystic_requirement_not_a_prime_requisite() -> None:
    with pytest.raises(IllegalTradeError, match="R1"):
        apply_trade(
            _scores(wisdom=15, dexterity=13),
            CharacterClass.MYSTIC,
            Ability.WISDOM,
            Ability.WISDOM,
        )


def test_m5_the_exchange_rate_is_2_to_1_for_every_class() -> None:
    mystic_before = _scores(strength=12, wisdom=15, dexterity=13)
    mystic_after = apply_trade(
        mystic_before, CharacterClass.MYSTIC, Ability.WISDOM, Ability.STRENGTH
    )
    fighter_before = _scores(strength=12, wisdom=15)
    fighter_after = apply_trade(
        fighter_before, CharacterClass.FIGHTER, Ability.WISDOM, Ability.STRENGTH
    )
    for before, after in ((mystic_before, mystic_after), (fighter_before, fighter_after)):
        assert before.wisdom - after.wisdom == 2
        assert after.strength - before.strength == 1


# --- Class eligibility invariant (SR-5, rule R10) ------------------------


def test_v1_a_trade_landing_exactly_on_the_minimum_is_legal() -> None:
    result = apply_trade(
        _scores(wisdom=15, strength=12, dexterity=13),
        CharacterClass.MYSTIC,
        Ability.WISDOM,
        Ability.STRENGTH,
    )
    assert result.wisdom == 13


def test_v2_r10_forbids_what_the_donor_floor_would_have_permitted() -> None:
    # Wis 14 -> 12 clears R6's floor of 9; R10 is what forbids it.
    with pytest.raises(ClassMinimumViolationError, match="R10"):
        apply_trade(
            _scores(wisdom=14, strength=12, dexterity=13),
            CharacterClass.MYSTIC,
            Ability.WISDOM,
            Ability.STRENGTH,
        )


def test_v3_a_score_already_at_the_minimum_cannot_be_lowered() -> None:
    with pytest.raises(ClassMinimumViolationError, match="R10"):
        apply_trade(
            _scores(wisdom=13, strength=12, dexterity=13),
            CharacterClass.MYSTIC,
            Ability.WISDOM,
            Ability.STRENGTH,
        )


def test_v4_two_trades_landing_on_the_minimum_are_legal() -> None:
    scores = _scores(wisdom=17, strength=12, dexterity=13)
    for _ in range(2):
        scores = apply_trade(
            scores, CharacterClass.MYSTIC, Ability.WISDOM, Ability.STRENGTH
        )
    assert (scores.wisdom, scores.strength) == (13, 14)


def test_v5_a_third_trade_breaching_the_minimum_is_rejected() -> None:
    scores = _scores(wisdom=17, strength=12, dexterity=13)
    for _ in range(2):
        scores = apply_trade(
            scores, CharacterClass.MYSTIC, Ability.WISDOM, Ability.STRENGTH
        )
    with pytest.raises(ClassMinimumViolationError, match="R10"):
        apply_trade(
            scores, CharacterClass.MYSTIC, Ability.WISDOM, Ability.STRENGTH
        )


def test_v6_a_legal_dexterity_raise_then_an_illegal_second_trade() -> None:
    scores = _scores(wisdom=15, dexterity=14, strength=12)
    first = apply_trade(
        scores, CharacterClass.MYSTIC, Ability.WISDOM, Ability.DEXTERITY
    )
    assert (first.wisdom, first.dexterity) == (13, 15)
    with pytest.raises(ClassMinimumViolationError, match="R10"):
        apply_trade(
            first, CharacterClass.MYSTIC, Ability.WISDOM, Ability.STRENGTH
        )


def test_v7_r10_is_stated_generally_not_as_a_mystic_special_case() -> None:
    # The rule reads CHAR-002's minimum table for whatever class it is
    # given. The Mystic rejects because its table has a Wisdom entry; the
    # Fighter permits the identical trade because its table is empty --
    # not because of any class check.
    with pytest.raises(ClassMinimumViolationError, match="R10"):
        apply_trade(
            _scores(wisdom=14, strength=12, dexterity=13),
            CharacterClass.MYSTIC,
            Ability.WISDOM,
            Ability.STRENGTH,
        )
    permitted = apply_trade(
        _scores(wisdom=14, strength=12, dexterity=13),
        CharacterClass.FIGHTER,
        Ability.WISDOM,
        Ability.STRENGTH,
    )
    assert permitted.wisdom == 12
    # And no class name appears anywhere in the module's own source.
    tree = ast.parse(inspect.getsource(ability_score_generation))
    assert not [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == "CharacterClass"
    ]


def test_v8_raising_an_ability_that_sits_at_its_minimum_is_legal() -> None:
    result = apply_trade(
        _scores(intelligence=9, wisdom=15),
        CharacterClass.ELF,
        Ability.WISDOM,
        Ability.INTELLIGENCE,
    )
    assert (result.intelligence, result.wisdom) == (10, 13)


def test_v9_the_dwarf_constitution_gate_is_already_barred_by_r3() -> None:
    with pytest.raises(IllegalTradeError, match="R3"):
        apply_trade(
            _scores(constitution=9),
            CharacterClass.DWARF,
            Ability.CONSTITUTION,
            Ability.STRENGTH,
        )


def test_v10_the_halfling_dexterity_gate_is_already_barred_by_r4() -> None:
    with pytest.raises(IllegalTradeError, match="R4"):
        apply_trade(
            _scores(dexterity=9),
            CharacterClass.HALFLING,
            Ability.DEXTERITY,
            Ability.STRENGTH,
        )


def test_v11_the_invariant_holds_after_the_trade() -> None:
    before = _scores(wisdom=15, strength=12, dexterity=13)
    assert eligibility(before, CharacterClass.MYSTIC) is Eligibility.ELIGIBLE
    after = apply_trade(
        before, CharacterClass.MYSTIC, Ability.WISDOM, Ability.STRENGTH
    )
    assert after.wisdom == 13
    assert eligibility(after, CharacterClass.MYSTIC) is Eligibility.ELIGIBLE


def test_v12_a_class_without_a_creation_minimum_is_unconstrained_by_r10() -> None:
    scores = _scores(wisdom=18, strength=12)
    for _ in range(4):
        scores = apply_trade(
            scores, CharacterClass.FIGHTER, Ability.WISDOM, Ability.STRENGTH
        )
    assert (scores.wisdom, scores.strength) == (10, 16)


# --- Chapter 13 switch (SR-3) --------------------------------------------


def test_w1_an_authorized_switch_can_establish_the_elf_intelligence_gate() -> None:
    scores = _scores(strength=16, intelligence=8, wisdom=12, dexterity=12)
    switched = apply_highest_score_switch(
        scores, CharacterClass.ELF, Ability.STRENGTH, Ability.INTELLIGENCE
    )
    assert (switched.intelligence, switched.strength) == (16, 8)
    assert eligibility(switched, CharacterClass.ELF) is Eligibility.ELIGIBLE


# W2 -- DOCUMENTED CALLING-CONTRACT CONFORMANCE, no pytest function.
# "Switch not authorized -> no switch occurs; eligibility scores equal the
# as-rolled scores." Authorization is the DM's or the simulation policy's;
# an unauthorized switch means this function is simply not called. No
# `authorized` parameter exists. See the module contract and ISSUE-011.


def test_w3_no_switch_can_reach_the_dwarf_constitution_gate() -> None:
    scores = _scores(strength=18, constitution=8)
    assert prime_requisites(CharacterClass.DWARF) == {Ability.STRENGTH}
    # The only legal destination is Strength, which already holds the
    # maximum -- so the request is degenerate, and Constitution is
    # unreachable either way.
    with pytest.raises(IllegalSwitchError, match="swap of two scores"):
        apply_highest_score_switch(
            scores, CharacterClass.DWARF, Ability.STRENGTH, Ability.STRENGTH
        )
    with pytest.raises(IllegalSwitchError, match="prime requisite"):
        apply_highest_score_switch(
            scores, CharacterClass.DWARF, Ability.STRENGTH, Ability.CONSTITUTION
        )
    assert (
        eligibility(scores, CharacterClass.DWARF)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )


def test_w4_a_switch_reaches_halfling_dexterity_but_never_constitution() -> None:
    scores = _scores(strength=17, intelligence=12, wisdom=12, dexterity=8, constitution=8)
    switched = apply_highest_score_switch(
        scores, CharacterClass.HALFLING, Ability.STRENGTH, Ability.DEXTERITY
    )
    assert (switched.dexterity, switched.strength) == (17, 8)
    assert switched.constitution == 8
    assert (
        eligibility(switched, CharacterClass.HALFLING)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )


def test_w5_a_switch_reaches_mystic_dexterity_but_never_wisdom() -> None:
    scores = _scores(strength=12, intelligence=12, wisdom=12, dexterity=11, charisma=17)
    switched = apply_highest_score_switch(
        scores, CharacterClass.MYSTIC, Ability.CHARISMA, Ability.DEXTERITY
    )
    assert (switched.dexterity, switched.charisma) == (17, 11)
    assert switched.wisdom == 12
    assert (
        eligibility(switched, CharacterClass.MYSTIC)
        is Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT
    )


# W6 -- DOCUMENTED CALLING-CONTRACT CONFORMANCE, no pytest function.
# "At most one switch, and it is a swap of two scores." The swap clause has
# executable evidence in W1/W4/W5 above and in the implementation tests
# below -- exactly two abilities exchange values and nothing else changes.
# The at-most-one clause is a caller obligation this stateless function
# cannot observe: nothing stops a caller invoking it twice, and no
# already_switched flag, switch count or creation state is added to detect
# that. See the module contract and ISSUE-011.


# --- Discard determination (SR-4) ----------------------------------------


def test_d1_no_score_above_9_offers_a_discard() -> None:
    assert discard_may_be_offered(_scores(9, 9, 8, 7, 6, 5)) is True


def test_d2_two_scores_below_6_offer_a_discard_despite_a_10() -> None:
    assert discard_may_be_offered(_scores(10, 5, 5, 9, 9, 9)) is True


def test_d3_a_score_above_9_and_no_low_pair_offers_nothing() -> None:
    assert discard_may_be_offered(_scores(10, 9, 9, 9, 9, 9)) is False


def test_d4_the_second_predicate_is_independent_of_the_first() -> None:
    assert discard_may_be_offered(_scores(18, 5, 5, 12, 12, 12)) is True


def test_d5_six_is_not_below_six() -> None:
    assert discard_may_be_offered(_scores(18, 6, 6, 12, 12, 12)) is False


def test_d6_nine_is_not_above_nine() -> None:
    assert discard_may_be_offered(_scores(9, 9, 9, 9, 9, 9)) is True


# D7 -- DOCUMENTED CALLING-CONTRACT CONFORMANCE, no pytest function.
# "Any qualifying array; the player elects to keep -> character retained
# and creation continues." The predicate returns permission to OFFER; it
# never forces a discard and has no parameter through which a player's
# decision could be expressed. No discard_choice or player_choice is added.
# See the module contract and ISSUE-011.


def test_d8_all_eights_satisfies_both_rc_formulations() -> None:
    assert discard_may_be_offered(_scores(8, 8, 8, 8, 8, 8)) is True


# =========================================================================
# Implementation / coverage tests — NOT approved contract cases.
# =========================================================================


def test_switch_rejects_a_source_that_is_not_the_maximum() -> None:
    with pytest.raises(IllegalSwitchError, match="highest rolled score"):
        apply_highest_score_switch(
            _scores(strength=16, intelligence=8),
            CharacterClass.ELF,
            Ability.INTELLIGENCE,
            Ability.STRENGTH,
        )


def test_switch_rejects_a_destination_that_is_not_a_prime_requisite() -> None:
    with pytest.raises(IllegalSwitchError, match="prime requisite"):
        apply_highest_score_switch(
            _scores(strength=16, wisdom=8),
            CharacterClass.ELF,
            Ability.STRENGTH,
            Ability.WISDOM,
        )


def test_switch_rejects_a_degenerate_source_equal_to_the_destination() -> None:
    with pytest.raises(IllegalSwitchError, match="swap of two scores"):
        apply_highest_score_switch(
            _scores(strength=16),
            CharacterClass.FIGHTER,
            Ability.STRENGTH,
            Ability.STRENGTH,
        )


def test_switch_accepts_any_tied_maximum_as_the_authorized_source() -> None:
    # No ability-order, alphabetical or random tie-break exists: the caller
    # names the source, and either tied ability is acceptable.
    scores = _scores(strength=16, charisma=16, intelligence=8)
    from_strength = apply_highest_score_switch(
        scores, CharacterClass.ELF, Ability.STRENGTH, Ability.INTELLIGENCE
    )
    from_charisma = apply_highest_score_switch(
        scores, CharacterClass.ELF, Ability.CHARISMA, Ability.INTELLIGENCE
    )
    assert (from_strength.intelligence, from_strength.strength) == (16, 8)
    assert (from_charisma.intelligence, from_charisma.charisma) == (16, 8)
    assert from_strength != from_charisma


def test_switch_changes_exactly_two_scores() -> None:
    scores = _scores(strength=16, intelligence=8)
    switched = apply_highest_score_switch(
        scores, CharacterClass.ELF, Ability.STRENGTH, Ability.INTELLIGENCE
    )
    changed = [
        ability for ability in Ability if scores[ability] != switched[ability]
    ]
    assert changed == [Ability.STRENGTH, Ability.INTELLIGENCE]


def test_trade_rejects_a_donor_that_is_also_the_target() -> None:
    with pytest.raises(IllegalTradeError, match="R5"):
        apply_trade(
            _scores(strength=15),
            CharacterClass.FIGHTER,
            Ability.STRENGTH,
            Ability.STRENGTH,
        )


def test_switch_trade_and_discard_consume_no_rng() -> None:
    # An empty queue raises on any draw, so reaching a result proves none.
    empty = ScriptedRNG([])
    assert discard_may_be_offered(_scores()) is False
    apply_highest_score_switch(
        _scores(strength=16, intelligence=8),
        CharacterClass.ELF,
        Ability.STRENGTH,
        Ability.INTELLIGENCE,
    )
    apply_trade(
        _scores(strength=12, wisdom=15),
        CharacterClass.FIGHTER,
        Ability.WISDOM,
        Ability.STRENGTH,
    )
    with pytest.raises(RollSequenceExhaustedError):
        empty.roll_die(6)


def test_all_slice_d_errors_are_character_creation_errors() -> None:
    for error in (
        IllegalTradeError,
        ClassMinimumViolationError,
        PrimeRequisiteCeilingError,
        IllegalSwitchError,
    ):
        assert issubclass(error, CharacterCreationError)


def test_public_surface_is_the_four_approved_operations() -> None:
    assert sorted(ability_score_generation.__all__) == [
        "apply_highest_score_switch",
        "apply_trade",
        "discard_may_be_offered",
        "generate_ability_scores",
    ]


def test_chapter_10_generation_is_not_reachable_from_this_module() -> None:
    assert not [
        module
        for module in _imported_modules()
        if "high_level_ability_score_generation" in module
    ]


def test_dependency_boundaries_are_held() -> None:
    modules = _imported_modules()
    assert "rng" in modules
    assert any("race_and_class_eligibility" in module for module in modules)
    assert not [
        module
        for module in modules
        if module == "random"
        or "ability_score_effects" in module
        or "hit_points_and_hit_dice" in module
        or "rules.exploration" in module
    ]


def test_no_concrete_rng_implementation_is_imported() -> None:
    tree = ast.parse(inspect.getsource(ability_score_generation))
    imported = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
        for alias in node.names
    }
    assert "RNG" in imported
    assert not {"SeededRNG", "ScriptedRNG"} & imported


def test_no_orchestration_object_exists() -> None:
    forbidden = {
        "Character",
        "Player",
        "CharacterCreator",
        "CharacterBuilder",
        "CharacterCreationEngine",
        "CreationSession",
        "CreationState",
        "CreationPhase",
        "GameState",
    }
    assert forbidden.isdisjoint(dir(ability_score_generation))
