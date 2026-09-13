"""CHAR-007 approved contract cases A1-A48.

Canonical owner of all 48 approved deterministic cases from
docs/rules/character_creation/ability_score_effects.md (Status: APPROVED),
per docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §12's ownership
ledger. Each approved case appears exactly once, under its own case ID, in
the card's own order.

A clearly separated implementation/coverage section follows at the end.
Those tests are NOT approved contract cases and must not be counted among
the 189.
"""

import inspect

import pytest

from rules.character_creation import ability_score_effects
from rules.character_creation.ability import Ability
from rules.character_creation.ability_score_effects import (
    CONDITIONAL_EFFECTS,
    AbilityEffect,
    CharismaEffects,
    LanguageCapability,
    Literacy,
    adjusted_effects,
    adjustment,
    charisma_effects,
    language_capability,
)
from rules.character_creation.errors import AbilityScoreDomainError

_PUBLIC_FUNCTIONS = frozenset(
    name
    for name in ability_score_effects.__all__
    if inspect.isfunction(getattr(ability_score_effects, name))
)
"""Every function CHAR-007 exposes. All four are value lookups; the card
owns no procedure, and this set is what several boundary cases assert."""

_VALUE_LOOKUPS = frozenset(
    {"adjustment", "language_capability", "charisma_effects", "adjusted_effects"}
)


# --- Shared adjustment table: every band and every boundary --------------


def test_a1_score_2_gives_minus_3() -> None:
    assert adjustment(2) == -3


def test_a2_score_3_gives_minus_3() -> None:
    assert adjustment(3) == -3


def test_a3_score_4_gives_minus_2() -> None:
    assert adjustment(4) == -2


def test_a4_score_5_gives_minus_2() -> None:
    assert adjustment(5) == -2


def test_a5_score_6_gives_minus_1() -> None:
    assert adjustment(6) == -1


def test_a6_score_8_gives_minus_1() -> None:
    assert adjustment(8) == -1


def test_a7_score_9_gives_no_adjustment() -> None:
    assert adjustment(9) == 0


def test_a8_score_12_gives_no_adjustment() -> None:
    assert adjustment(12) == 0


def test_a9_score_13_gives_plus_1() -> None:
    assert adjustment(13) == 1


def test_a10_score_15_gives_plus_1() -> None:
    assert adjustment(15) == 1


def test_a11_score_16_gives_plus_2() -> None:
    assert adjustment(16) == 2


def test_a12_score_17_gives_plus_2() -> None:
    assert adjustment(17) == 2


def test_a13_score_18_gives_plus_3() -> None:
    assert adjustment(18) == 3


def test_a14_one_shared_table_for_all_six_abilities() -> None:
    # The lookup takes no ability parameter at all, so a per-ability,
    # per-class or per-race variation is not expressible (card §1).
    assert list(inspect.signature(adjustment).parameters) == ["score"]
    assert len({adjustment(13) for _ in Ability}) == 1


def test_a15_score_1_or_19_is_a_rejected_input() -> None:
    # Outside the declared 2-18 domain. No value may be extrapolated, and
    # this is not a ruling about what the game does to such a score.
    for score in (1, 19):
        with pytest.raises(AbilityScoreDomainError, match="2-18"):
            adjustment(score)


# --- Intelligence and Languages ------------------------------------------


def test_a16_intelligence_3_has_trouble_speaking_and_cannot_read_or_write() -> None:
    assert language_capability(3) == LanguageCapability(
        Literacy.TROUBLE_SPEAKING_CANNOT_READ_OR_WRITE, 0
    )


def test_a17_intelligence_5_cannot_read_or_write_common() -> None:
    assert language_capability(5) == LanguageCapability(
        Literacy.CANNOT_READ_OR_WRITE_COMMON, 0
    )


def test_a18_intelligence_8_writes_simple_common_words() -> None:
    assert language_capability(8) == LanguageCapability(
        Literacy.WRITES_SIMPLE_COMMON_WORDS, 0
    )


def test_a19_intelligence_9_reads_native_languages_and_no_additional() -> None:
    assert language_capability(9) == LanguageCapability(
        Literacy.READS_AND_WRITES_NATIVE_LANGUAGES, 0
    )


def test_a20_intelligence_12_matches_intelligence_9() -> None:
    # Band boundary: 9-12 is one band.
    assert language_capability(12) == language_capability(9)


def test_a21_intelligence_13_gives_one_additional_language() -> None:
    assert language_capability(13).additional_languages == 1


def test_a22_intelligence_16_gives_two_additional_languages() -> None:
    assert language_capability(16).additional_languages == 2


def test_a23_intelligence_18_gives_three_additional_languages() -> None:
    assert language_capability(18).additional_languages == 3


def test_a24_language_count_is_not_derived_from_the_adjustment() -> None:
    # At 18 the two values coincide; they are still two distinct tables.
    assert adjustment(18) == 3
    assert language_capability(18).additional_languages == 3
    # And they diverge, which is what proves the independence: at 3 the
    # adjustment is -3 while the additional-language count is 0.
    assert adjustment(3) == -3
    assert language_capability(3).additional_languages == 0


# --- Charisma: three outputs ---------------------------------------------


def test_a25_charisma_3() -> None:
    assert charisma_effects(3) == CharismaEffects(-3, 1, 4)


def test_a26_charisma_8() -> None:
    assert charisma_effects(8) == CharismaEffects(-1, 3, 6)


def test_a27_charisma_9() -> None:
    assert charisma_effects(9) == CharismaEffects(0, 4, 7)


def test_a28_charisma_12() -> None:
    assert charisma_effects(12) == CharismaEffects(0, 4, 7)


def test_a29_charisma_13() -> None:
    assert charisma_effects(13) == CharismaEffects(1, 5, 8)


def test_a30_charisma_18() -> None:
    assert charisma_effects(18) == CharismaEffects(3, 7, 10)


def test_a31_reaction_adjustment_cannot_be_applied_to_a_players_roll() -> None:
    # RC: the adjustment "never adjust[s] any rolls you make; they only
    # affect rolls made by the Dungeon Master." CHAR-007 supplies the
    # value and exposes no way to apply it to any roll, so a player-side
    # application cannot originate here.
    effects = charisma_effects(13)
    assert effects.reaction_adjustment == 1
    assert not [
        name
        for name in dir(effects)
        if not name.startswith("_") and callable(getattr(effects, name))
    ]
    assert _PUBLIC_FUNCTIONS == _VALUE_LOOKUPS


def test_a32_reaction_adjustment_applicability_is_not_decided_here() -> None:
    # The adjustment applies only while the character is talking to the
    # creature. This lookup takes no situational context, so CHAR-007
    # neither knows nor decides when that is true — ENC-003 does.
    assert list(inspect.signature(charisma_effects).parameters) == ["charisma"]


# --- Per-ability assignment ----------------------------------------------


def test_a33_strength_adjusts_melee_attack_rolls() -> None:
    assert AbilityEffect.MELEE_ATTACK_ROLLS in adjusted_effects(Ability.STRENGTH)


def test_a34_strength_does_not_adjust_missile_attack_rolls() -> None:
    assert AbilityEffect.MISSILE_AND_THROWN_ATTACK_ROLLS not in adjusted_effects(
        Ability.STRENGTH
    )


def test_a35_dexterity_adjusts_thrown_weapon_attack_rolls() -> None:
    assert AbilityEffect.MISSILE_AND_THROWN_ATTACK_ROLLS in adjusted_effects(
        Ability.DEXTERITY
    )


def test_a36_strength_adjusts_thrown_weapon_damage_rolls() -> None:
    # Strength covers melee *and thrown* damage, though only melee attack rolls.
    assert AbilityEffect.MELEE_AND_THROWN_DAMAGE_ROLLS in adjusted_effects(
        Ability.STRENGTH
    )


def test_a37_wisdom_adjusts_saving_throws_versus_spells() -> None:
    assert AbilityEffect.SAVING_THROWS_VS_SPELLS in adjusted_effects(Ability.WISDOM)


def test_a38_wisdom_does_not_adjust_saves_versus_dragon_breath() -> None:
    # Under core rules Wisdom's only save effect is versus spells; the
    # Chapter 19 variant that maps other abilities to other categories is
    # COMBAT-004's. No such effect exists in this closed set.
    assert adjusted_effects(Ability.WISDOM) == {AbilityEffect.SAVING_THROWS_VS_SPELLS}
    assert not [
        effect for effect in AbilityEffect if "DRAGON" in effect.name
    ]


def test_a39_constitution_adjusts_hit_points_per_experience_level() -> None:
    assert AbilityEffect.HIT_POINTS_PER_EXPERIENCE_LEVEL in adjusted_effects(
        Ability.CONSTITUTION
    )


def test_a40_constitution_does_not_adjust_fixed_gains_above_name_level() -> None:
    # CHAR-003 §5: Constitution never applies to fixed gains. There is no
    # effect in this set for them.
    assert adjusted_effects(Ability.CONSTITUTION) == {
        AbilityEffect.HIT_POINTS_PER_EXPERIENCE_LEVEL
    }
    assert not [effect for effect in AbilityEffect if "FIXED" in effect.name]


def test_a41_language_effect_is_unconditional_general_skills_is_not() -> None:
    effects = adjusted_effects(Ability.INTELLIGENCE)
    assert AbilityEffect.LANGUAGES in effects
    assert AbilityEffect.LANGUAGES not in CONDITIONAL_EFFECTS
    assert AbilityEffect.GENERAL_SKILLS in effects
    assert AbilityEffect.GENERAL_SKILLS in CONDITIONAL_EFFECTS


# --- Boundary guards -----------------------------------------------------


def test_a42_open_doors_value_is_owned_here_the_procedure_is_not() -> None:
    # CHAR-007 owns the Strength adjustment value; the 1d6 roll, the 5-6
    # target and the natural-6 override belong to EXP-005.
    assert AbilityEffect.OPENING_DOORS in adjusted_effects(Ability.STRENGTH)
    assert _PUBLIC_FUNCTIONS == _VALUE_LOOKUPS


def test_a43_once_per_round_and_surprise_forfeiture_are_absent_by_design() -> None:
    # Chapter 13 p. 147's two extra door rules belong to EXP-005, which
    # thereby acquires an ENC-002 (surprise) dependency.
    assert _PUBLIC_FUNCTIONS == _VALUE_LOOKUPS
    assert not [
        name
        for name in ability_score_effects.__all__
        if "DOOR" in name.upper() or "SURPRISE" in name.upper()
    ]


def test_a44_dexterity_is_not_applied_to_initiative_in_v1() -> None:
    # RC p. 102's Dexterity initiative modifier is the optional
    # individual-initiative rule, declined for V1 by DEC-0008.
    assert not [effect for effect in AbilityEffect if "INITIATIVE" in effect.name]
    assert adjusted_effects(Ability.DEXTERITY) == {
        AbilityEffect.MISSILE_AND_THROWN_ATTACK_ROLLS,
        AbilityEffect.ARMOR_CLASS,
    }


def test_a45_only_wisdom_affects_a_saving_throw_under_core_rules() -> None:
    saving = {
        ability
        for ability in Ability
        if AbilityEffect.SAVING_THROWS_VS_SPELLS in adjusted_effects(ability)
    }
    assert saving == {Ability.WISDOM}


def test_a46_the_chapter_13_ability_check_is_out_of_scope() -> None:
    # A different mechanic, a different responsibility. No Rule ID is
    # assigned or invented here; P3 remains deferred for human governance.
    assert _PUBLIC_FUNCTIONS == _VALUE_LOOKUPS
    assert not [
        name for name in ability_score_effects.__all__ if "CHECK" in name.upper()
    ]


def test_a47_the_ability_check_does_not_use_the_adjustment_table() -> None:
    # The check rolls 1d20 against the *raw* score; this table plays no
    # part, and no effect in the closed set represents it.
    assert not [effect for effect in AbilityEffect if "CHECK" in effect.name]


def test_a48_retainer_count_and_morale_values_are_supplied() -> None:
    # Values here; their use belongs to CHAR-006.
    effects = charisma_effects(18)
    assert effects.maximum_retainers == 7
    assert effects.retainer_morale == 10
    assert AbilityEffect.RETAINERS in adjusted_effects(Ability.CHARISMA)


# =========================================================================
# Implementation / coverage tests — NOT approved contract cases.
# These exercise declared input domains and module structure. They must
# not be counted among the 189 approved deterministic cases.
# =========================================================================


def test_supplementary_tables_begin_at_3_not_2() -> None:
    # RC's own difference from the shared adjustment table, faithfully
    # reproduced (card §1). 2 is a valid adjustment input but not a valid
    # Intelligence or Charisma input.
    assert adjustment(2) == -3
    with pytest.raises(AbilityScoreDomainError, match="3-18"):
        language_capability(2)
    with pytest.raises(AbilityScoreDomainError, match="3-18"):
        charisma_effects(2)


def test_supplementary_tables_reject_scores_above_18() -> None:
    with pytest.raises(AbilityScoreDomainError, match="Intelligence"):
        language_capability(19)
    with pytest.raises(AbilityScoreDomainError, match="Charisma"):
        charisma_effects(19)


def test_every_ability_has_an_effect_assignment() -> None:
    assert {ability: adjusted_effects(ability) for ability in Ability}.keys() == set(
        Ability
    )


def test_ability_effect_is_a_closed_set_of_eleven() -> None:
    assert len(AbilityEffect) == 11


def test_results_are_immutable_value_objects() -> None:
    assert language_capability(9) == language_capability(12)
    assert charisma_effects(9) is charisma_effects(12)
