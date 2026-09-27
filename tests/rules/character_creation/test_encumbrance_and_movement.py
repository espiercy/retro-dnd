"""CHAR-005 approved contract cases M1-M48 and M60-M76 (CLUSTER-003 Slice D).

Slice D of docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md §10 owns the
single authoritative numerical movement system.

    this module   M1-M48, M60-M76
    NOT V1-WIRED  M49-M59 — card §7 condition modifiers (plan §8)

**M49-M59 appear nowhere below, deliberately.** Every causation owner for
blindness, stunning, prone and starvation is Unresearched, so no landed or
approved card can produce any of those conditions; the plan dispositions
them NOT V1-WIRED. SR-10 remains approved and recorded on the card. Guard
tests at the end assert that no condition parameter, enum or pipeline was
built in anticipation.

A clearly separated implementation/coverage section follows at the end.
Those tests are NOT approved contract cases and must not be counted among
CHAR-005's 76.
"""

import ast
import inspect
from fractions import Fraction
from types import MappingProxyType

import pytest

from rules.character_creation import encumbrance_and_movement
from rules.character_creation.character_class import CharacterClass
from rules.character_creation.encumbrance_and_movement import (
    MAXIMUM_LEVEL,
    MAXIMUM_RUNNING_ROUNDS,
    MYSTIC_MAXIMUM_LEVEL,
    MYSTIC_MV,
    MYSTIC_UNENCUMBERED_MAXIMUM_CN,
    REQUIRED_REST_TURNS,
    SUIT_ARMOR_ENCUMBRANCE_CN,
    ExhaustionPenalty,
    MovementMode,
    MovementRate,
    Setting,
    combat_movement,
    is_rested,
    may_attack_in_the_same_round,
    movement_rate,
    party_movement_rate,
    run_for,
)
from rules.character_creation.errors import (
    MovementLevelError,
    MovementNotPermittedError,
)

CC = CharacterClass

# Movement is level-independent for every class but the Mystic, so the
# ordinary-character cases below use a fighter at 1st level.
ORDINARY = CC.FIGHTER


def rate_of(encumbrance_cn: int, cls: CharacterClass = ORDINARY, level: int = 1) -> MovementRate:
    return movement_rate(cls, level, encumbrance_cn)


# --- The encumbrance table: M1-M14 -----------------------------------------


@pytest.mark.parametrize(
    ("case", "encumbrance_cn", "normal", "encounter"),
    [
        ("M1", 0, 120, 40),
        ("M2", 400, 120, 40),
        ("M3", 401, 90, 30),
        ("M4", 800, 90, 30),
        ("M5", 801, 60, 20),
        ("M6", 1200, 60, 20),
        ("M7", 1201, 30, 10),
        ("M8", 1600, 30, 10),
        ("M9", 1601, 15, 5),
        ("M10", 2400, 15, 5),
        ("M11", 2401, 0, 0),
        ("M12", 10000, 0, 0),
        ("M13", 600, 90, 30),
    ],
    ids=lambda v: str(v),
)
def test_every_band_and_both_sides_of_every_boundary(
    case: str, encumbrance_cn: int, normal: int, encounter: int
) -> None:
    """M1-M13 — the six bands, both sides of all five boundaries, and RC's example.

    M13 is RC's own worked example: 600 cn moves 90' (30').
    """
    rate = rate_of(encumbrance_cn)
    assert rate.normal == normal
    assert rate.encounter == encounter
    assert rate.running == normal


def test_m11_the_top_band_is_immobile() -> None:
    """M11 — 2,401 cn: 0' (0'), immobile."""
    rate = rate_of(2401)
    assert rate.is_immobile
    assert not rate_of(2400).is_immobile


@pytest.mark.parametrize("bad", [-1, -400])
def test_m14_a_negative_encumbrance_is_refused(bad: int) -> None:
    """M14 — negative cn: ERROR."""
    with pytest.raises(ValueError, match="must not be negative"):
        rate_of(bad)


@pytest.mark.parametrize("bad", [400.5, "400", None, Fraction(1, 2)])
def test_m14_a_non_integer_encumbrance_is_refused(bad: object) -> None:
    """M14 — non-integer cn: ERROR. RC states cn in whole coins."""
    with pytest.raises(ValueError, match="must be an int"):
        rate_of(bad)  # type: ignore[arg-type]


@pytest.mark.parametrize("bad", [True, False])
def test_m14_a_bool_encumbrance_is_refused(bad: bool) -> None:
    """M14 — bool is a subtype of int, so True would read as 1 cn."""
    with pytest.raises(ValueError, match="must be an int"):
        rate_of(bad)


# --- Rate relationships (Q4): M15-M20 --------------------------------------


def test_m15_normal_120_gives_encounter_40() -> None:
    """M15 — normal 120' -> encounter 40' per round."""
    assert rate_of(0).encounter == 40


def test_m16_normal_120_runs_at_120_not_360() -> None:
    """M16 — normal 120' -> running 120' per round. NOT 360'."""
    rate = rate_of(0)
    assert rate.running == 120
    assert rate.running != 360


@pytest.mark.parametrize("encumbrance_cn", [0, 401, 801, 1201, 1601, 2401])
def test_m17_encounter_times_three_equals_running_at_every_band(encumbrance_cn: int) -> None:
    """M17 — encounter x 3 == running, at every band."""
    rate = rate_of(encumbrance_cn)
    assert rate.encounter * 3 == rate.running


def test_m18_and_m19_the_remaining_printed_rows() -> None:
    """M18, M19 — normal 90' -> 30'/90'; normal 15' -> 5'/15'."""
    ninety = rate_of(401)
    assert ninety.encounter == 30
    assert ninety.running == 90
    fifteen = rate_of(1601)
    assert fifteen.encounter == 5
    assert fifteen.running == 15


def test_m20_chapter_8s_three_times_normal_resolves_to_three_times_encounter() -> None:
    """M20 — Ch. 8's "3 x normal movement" is 3 x encounter, never 3 x per-turn.

    Read literally against the per-turn number it would give 360'; the Q4
    interpretation preserves the Ch. 6 table, and is RC-explicit
    interpretation reinforced by necessary consequence — not a ruling.
    """
    rate = rate_of(0)
    assert rate.encounter * 3 == rate.running == 120
    assert rate.normal * 3 != rate.running


# --- Scale boundary (Ch. 8 p. 103): M21-M24 --------------------------------


def test_m21_normal_speed_is_refused_inside_the_combat_sequence() -> None:
    """M21 — normal speed requested during the combat sequence: refused."""
    rate = rate_of(0)
    with pytest.raises(MovementNotPermittedError, match="never used during the combat sequence"):
        combat_movement(rate, MovementMode.NORMAL)
    with pytest.raises(MovementNotPermittedError, match="never used during the combat sequence"):
        may_attack_in_the_same_round(MovementMode.NORMAL)


def test_m22_encounter_speed_may_be_moved_in_full_and_still_attack() -> None:
    """M22 — move full encounter speed, then attack: both permitted."""
    rate = rate_of(0)
    assert combat_movement(rate, MovementMode.ENCOUNTER) == 40
    assert may_attack_in_the_same_round(MovementMode.ENCOUNTER)


def test_m23_running_forbids_an_attack_in_the_same_round() -> None:
    """M23 — move full running speed, then attack: attack refused."""
    rate = rate_of(0)
    assert combat_movement(rate, MovementMode.RUNNING) == 120
    assert not may_attack_in_the_same_round(MovementMode.RUNNING)


def test_m24_a_character_already_engaged_may_not_run() -> None:
    """M24 — run while already engaged in combat: refused."""
    rate = rate_of(0)
    with pytest.raises(MovementNotPermittedError, match="already engaged"):
        combat_movement(rate, MovementMode.RUNNING, already_engaged=True)
    # Encounter movement is unaffected by engagement.
    assert combat_movement(rate, MovementMode.ENCOUNTER, already_engaged=True) == 40


# --- Suit Armor (SR-8): M25-M30 --------------------------------------------


def test_m25_suit_armor_alone_moves_at_ninety_not_thirty() -> None:
    """M25 — Suit Armor alone, total 750 cn: 90' (30'). Must NOT be 30' (10')."""
    rate = rate_of(SUIT_ARMOR_ENCUMBRANCE_CN)
    assert SUIT_ARMOR_ENCUMBRANCE_CN == 750
    assert rate.normal == 90
    assert rate.encounter == 30
    assert rate.normal != 30


def test_m26_suit_armor_plus_gear_keeps_banding_ordinarily() -> None:
    """M26 — Suit Armor + 100 cn = 850 cn: 60' (20')."""
    rate = rate_of(SUIT_ARMOR_ENCUMBRANCE_CN + 100)
    assert rate.normal == 60
    assert rate.encounter == 20


def test_m27_thirty_feet_is_reached_by_encumbrance_not_by_an_item_rule() -> None:
    """M27 — Suit Armor + 500 cn = 1,250 cn: 30' (10'), by the table."""
    rate = rate_of(SUIT_ARMOR_ENCUMBRANCE_CN + 500)
    assert rate.normal == 30
    assert rate.encounter == 10


def test_m28_no_suit_armor_specific_movement_rate_exists() -> None:
    """M28 — any request for a Suit Armor-specific rate: no such rate exists."""
    public = {name for name in vars(encumbrance_and_movement) if not name.startswith("_")}
    forbidden = {
        "suit_armor_movement_rate",
        "SUIT_ARMOR_MOVEMENT_RATE",
        "SUIT_ARMOR_NORMAL_SPEED",
        "suit_armor_rate",
    }
    assert public & forbidden == set()


def test_m29_no_generic_equipment_overrides_encumbrance_pathway_exists() -> None:
    """M29 — any generic "equipment overrides encumbrance" pathway: MUST NOT EXIST.

    movement_rate takes a class, a level and a cn total. It cannot be handed
    an item, so no item can override the band it produces.
    """
    parameters = list(inspect.signature(movement_rate).parameters)
    assert parameters == ["cls", "level", "total_encumbrance_cn"]
    public = {name for name in vars(encumbrance_and_movement) if not name.startswith("_")}
    forbidden = {
        "equipment_override",
        "EQUIPMENT_OVERRIDES",
        "item_movement_rate",
        "override_rate",
        "Item",
        "ItemCategory",
        "WEAPONS",
        "ARMOR",
    }
    assert public & forbidden == set()


def test_m30_suit_armor_is_exactly_750_cn_unscaled() -> None:
    """M30 — Suit Armor encumbrance: exactly 750 cn, no scaling, no adjustment.

    Re-exported from CHAR-004's catalog, so there is one value.
    """
    from rules.character_creation.equipment import ARMOR

    assert SUIT_ARMOR_ENCUMBRANCE_CN == ARMOR["Suit Armor"].encumbrance_cn == 750


# --- The Mystic MV gate (SR-9): M31-M40 ------------------------------------


def test_m31_a_first_level_mystic_moves_at_120() -> None:
    """M31 — Mystic L1, 0 cn: 120' normal."""
    assert rate_of(0, CC.MYSTIC, 1).normal == 120


def test_m32_a_tenth_level_mystic_moves_at_210() -> None:
    """M32 — Mystic L10, 0 cn: 210' normal."""
    assert rate_of(0, CC.MYSTIC, 10).normal == 210


def test_m33_the_gate_is_open_at_exactly_400_cn() -> None:
    """M33 — Mystic L16, 400 cn (boundary): 320' normal, MV still active."""
    assert MYSTIC_UNENCUMBERED_MAXIMUM_CN == 400
    assert rate_of(400, CC.MYSTIC, 16).normal == 320


def test_m34_the_gate_is_shut_at_401_cn() -> None:
    """M34 — Mystic L16, 401 cn: 90' (30'). MV off; the standard table.

    Must not be 320', and must not be a scaled MV.
    """
    rate = rate_of(401, CC.MYSTIC, 16)
    assert rate.normal == 90
    assert rate.encounter == 30
    assert rate.normal != 320
    # A scaled MV would land somewhere between; it lands exactly on the band.
    assert rate.normal == rate_of(401, ORDINARY).normal


def test_m35_an_encumbered_mystic_uses_the_ordinary_band() -> None:
    """M35 — Mystic L10, 900 cn: 60' (20')."""
    rate = rate_of(900, CC.MYSTIC, 10)
    assert rate.normal == 60
    assert rate.encounter == 20


def test_m36_a_mystic_is_not_immune_to_encumbrance() -> None:
    """M36 — Mystic L16, 2,401 cn: 0' (0'). No immunity."""
    rate = rate_of(2401, CC.MYSTIC, 16)
    assert rate.is_immobile
    assert rate.normal == 0


@pytest.mark.parametrize("encumbrance_cn", [401, 500, 800, 1201, 2401])
def test_m37_mv_is_never_proportionally_scaled_by_encumbrance(encumbrance_cn: int) -> None:
    """M37 — any proportional scaling of MV by encumbrance: MUST NOT EXIST.

    Past the gate a Mystic's rate is exactly an ordinary character's — never
    a fraction of the MV, which is what scaling would produce.
    """
    mystic = rate_of(encumbrance_cn, CC.MYSTIC, 16)
    ordinary = rate_of(encumbrance_cn, ORDINARY)
    assert mystic == ordinary
    assert mystic.normal in (90, 60, 30, 15, 0)


@pytest.mark.parametrize("level", sorted(MYSTIC_MV))
def test_m38_a_mystic_is_never_exempt_from_the_bands(level: int) -> None:
    """M38 — Mystic treated as immune to encumbrance: MUST NOT EXIST."""
    assert rate_of(2401, CC.MYSTIC, level).normal == 0
    assert rate_of(1601, CC.MYSTIC, level).normal == 15


@pytest.mark.parametrize("cls", [c for c in CharacterClass if c is not CharacterClass.MYSTIC])
def test_m39_mv_is_mystic_only(cls: CharacterClass) -> None:
    """M39 — non-Mystic of any level, 0 cn: 120'. MV is Mystic-only.

    "Any level" means any level the class can reach: the per-class maximum
    bounds the input for every class (§1.1).
    """
    maximum = MAXIMUM_LEVEL[cls]
    for level in (1, (1 + maximum) // 2, maximum):
        assert movement_rate(cls, level, 0).normal == 120


def test_m40_a_mystic_level_above_sixteen_is_refused() -> None:
    """M40 — Mystic level above 16: ERROR. 16 is the maximum."""
    assert MYSTIC_MAXIMUM_LEVEL == 16
    with pytest.raises(MovementLevelError, match="at most 16 for a mystic"):
        rate_of(0, CC.MYSTIC, 17)
    with pytest.raises(MovementLevelError, match="at most 16 for a mystic"):
        rate_of(0, CC.MYSTIC, 100)
    assert rate_of(0, CC.MYSTIC, 16).normal == 320


# --- Mystic encounter movement, exact fractions (Q6): M41-M48 --------------


@pytest.mark.parametrize(
    ("case", "level", "mv", "encounter"),
    [
        ("M41", 1, 120, Fraction(40)),
        ("M42", 2, 130, Fraction(130, 3)),
        ("M43", 3, 140, Fraction(140, 3)),
        ("M44", 10, 210, Fraction(70)),
        ("M45", 16, 320, Fraction(320, 3)),
    ],
    ids=lambda v: str(v),
)
def test_mystic_encounter_movement_is_an_exact_third(
    case: str, level: int, mv: int, encounter: Fraction
) -> None:
    """M41-M45 — encounter = MV / 3, exactly.

    M42 is 43 1/3', not 43 and not 44. M45 is 106 2/3', and must not be
    BECMI's defective 80'.
    """
    rate = rate_of(0, CC.MYSTIC, level)
    assert MYSTIC_MV[level] == mv
    assert rate.normal == mv
    assert rate.encounter == encounter


def test_m45_becmis_defective_eighty_feet_is_not_imported() -> None:
    """M45 — MV 320' gives 106 2/3', not BECMI's printed 80'."""
    encounter = rate_of(0, CC.MYSTIC, 16).encounter
    assert encounter == Fraction(320, 3)
    assert encounter != 80


@pytest.mark.parametrize("level", sorted(MYSTIC_MV))
def test_m46_no_mystic_encounter_rate_is_ever_rounded(level: int) -> None:
    """M46 — any rounding of a Mystic encounter rate: MUST NOT OCCUR.

    In either direction or to nearest. The exact third is retained for every
    level, including the eight whose MV is not divisible by 3.
    """
    rate = rate_of(0, CC.MYSTIC, level)
    assert rate.encounter * 3 == rate.normal
    assert rate.encounter == Fraction(MYSTIC_MV[level], 3)


def test_m47_a_fractional_rate_is_an_exact_rational_not_a_lossy_float() -> None:
    """M47 — representation of 43 1/3': exact rational, not a lossy float."""
    encounter = rate_of(0, CC.MYSTIC, 2).encounter
    assert isinstance(encounter, Fraction)
    assert encounter == Fraction(130, 3)
    assert encounter != float(Fraction(130, 3))
    # The float would lose the value; the Fraction reconstructs it exactly.
    assert encounter.numerator == 130
    assert encounter.denominator == 3


def test_m48_a_mystic_runs_at_its_mv_per_round() -> None:
    """M48 — Mystic running while MV active, MV 130': 130' per round (§6.1).

    The ordinary running derivation applies to the enhanced MV unchanged;
    there is no separate Mystic running formula.
    """
    rate = rate_of(0, CC.MYSTIC, 2)
    assert rate.running == 130
    assert rate.normal == 130
    assert rate.encounter == Fraction(130, 3)


def test_m48_the_worked_example_from_section_6_1() -> None:
    """§6.1's worked example: MV 210' -> 210' turn, 70' round, 210' round."""
    rate = rate_of(0, CC.MYSTIC, 10)
    assert rate.normal == 210
    assert rate.encounter == 70
    assert rate.running == 210


# --- Group movement: M60-M62 -----------------------------------------------


def test_m60_a_party_staying_together_moves_at_its_slowest_member() -> None:
    """M60 — party at 120', 90', 60' intending to stay together: 60'."""
    party = [rate_of(0), rate_of(401), rate_of(801)]
    assert party_movement_rate(party).normal == 60
    # Order does not matter: a faster member arriving after the slowest one
    # does not displace it.
    assert party_movement_rate(list(reversed(party))).normal == 60
    assert party_movement_rate([rate_of(801), rate_of(0)]).normal == 60


def test_m61_an_immobile_member_makes_the_party_immobile() -> None:
    """M61 — party including an immobile member (0'): 0'."""
    party = [rate_of(0), rate_of(2401)]
    assert party_movement_rate(party).is_immobile


def test_m62_a_party_not_staying_together_has_no_group_rate() -> None:
    """M62 — party not intending to stay together: each member uses their own.

    Calling party_movement_rate IS the intent to stay together; there is no
    flag that asks it for a rate ignoring the slowest member.
    """
    assert list(inspect.signature(party_movement_rate).parameters) == ["rates"]
    fast, slow = rate_of(0), rate_of(801)
    assert fast.normal == 120
    assert slow.normal == 60


def test_the_slowest_member_is_slowest_on_all_three_rates() -> None:
    """M60 — the group rate is a whole rate, not just a normal speed."""
    group = party_movement_rate([rate_of(0), rate_of(801)])
    assert group.normal == 60
    assert group.encounter == 20
    assert group.running == 60


# --- Exhaustion: M63-M69 ---------------------------------------------------


def test_m63_running_thirty_rounds_is_permitted_and_exhausts() -> None:
    """M63 — running for 30 rounds: permitted; exhausted at the end."""
    assert MAXIMUM_RUNNING_ROUNDS == 30
    assert run_for(30) is True
    assert run_for(29) is False


def test_m64_running_thirty_one_rounds_is_refused() -> None:
    """M64 — running for 31 rounds: refused. The limit is 30."""
    with pytest.raises(MovementNotPermittedError, match="at most 30 rounds"):
        run_for(31)


def test_m65_three_turns_of_rest_clear_exhaustion() -> None:
    """M65 — exhausted, rest 3 turns: may run or fight again."""
    assert REQUIRED_REST_TURNS == 3
    assert is_rested(3)
    assert is_rested(10)


def test_m66_two_turns_of_rest_do_not() -> None:
    """M66 — exhausted, rest 2 turns: still exhausted."""
    assert not is_rested(2)
    assert not is_rested(0)


def test_m67_exhausted_combat_penalties_are_recorded() -> None:
    """M67 — exhausted, forced to fight: monsters +2 to hit; character -2 damage.

    Recorded, not applied: resolving an attack or a damage roll is
    COMBAT-002/003's (card §A).
    """
    penalty = ExhaustionPenalty()
    assert penalty.monster_attack_bonus == 2
    assert penalty.damage_penalty == 2


def test_m68_a_successful_hit_still_inflicts_at_least_one_point() -> None:
    """M68 — exhausted, -2 reduces damage below 1: minimum 1.

    The floor is recorded on the value object. Applying it to a damage roll
    is COMBAT-003's, and this module deliberately has no such operation.
    """
    assert ExhaustionPenalty().minimum_damage == 1
    public = {name for name in vars(encumbrance_and_movement) if not name.startswith("_")}
    assert "damage_after_exhaustion" not in public
    assert "apply_exhaustion" not in public


def test_m69_an_exhausted_runner_drops_to_encounter_speed() -> None:
    """M69 — exhausted, forced to keep running: drops to encounter speed."""
    rate = rate_of(0)
    assert combat_movement(rate, MovementMode.ENCOUNTER) == rate.encounter == 40
    assert rate.encounter < rate.running


# --- Units: M70-M71 --------------------------------------------------------


def test_m70_and_m71_the_numbers_do_not_change_only_the_unit_does() -> None:
    """M70, M71 — 90' indoors is 90 feet per turn; outdoors, 90 yards per turn."""
    assert Setting.INDOORS.unit == "feet"
    assert Setting.OUTDOORS.unit == "yards"
    rate = rate_of(401)
    assert rate.normal == 90
    # movement_rate takes no setting, because the number is the same either way.
    assert "setting" not in inspect.signature(movement_rate).parameters


# --- Guard cases: M72-M76 --------------------------------------------------


def test_m72_no_racial_armour_penalty_is_quantified() -> None:
    """M72 — racial-armour penalty requested as a number: not specified.

    RC delegates it by design — "The DM CAN impose penalties" — so this card
    quantifies nothing.
    """
    public = {name for name in vars(encumbrance_and_movement) if not name.startswith("_")}
    forbidden = {
        "racial_armour_penalty",
        "racial_armor_penalty",
        "RACIAL_ARMOR_PENALTY",
        "wrong_race_armour_modifier",
    }
    assert public & forbidden == set()


def test_m73_no_monster_or_mount_encumbrance_system_exists() -> None:
    """M73 — monster or mount encumbrance: not this card's two-band system."""
    public = {name for name in vars(encumbrance_and_movement) if not name.startswith("_")}
    forbidden = {
        "monster_movement_rate",
        "MONSTER_BANDS",
        "mount_encumbrance",
        "barding_multiplier",
        "vehicle_movement_rate",
    }
    assert public & forbidden == set()
    # The character system has six bands, not two.
    normals = {rate_of(cn).normal for cn in (0, 401, 801, 1201, 1601, 2401)}
    assert len(normals) == 6


def test_m74_no_quantisation_to_map_squares_is_provided() -> None:
    """M74 — quantisation to 10' map squares: not provided, separate concern."""
    public = {name for name in vars(encumbrance_and_movement) if not name.startswith("_")}
    forbidden = {"squares", "to_squares", "MAP_SCALE_FEET", "quantise", "quantize", "snap"}
    assert public & forbidden == set()
    # A fractional rate stays fractional; nothing snaps it.
    assert rate_of(0, CC.MYSTIC, 2).encounter == Fraction(130, 3)


def test_m75_the_mystic_personal_possessions_flavour_is_not_an_ownership_limit() -> None:
    """M75 — "personal possessions" treated as an ownership limit: MUST NOT EXIST.

    The SR-9 gate is about carried encumbrance and nothing else. A Mystic
    may own anything; what matters is the cn total being carried.
    """
    public = {name for name in vars(encumbrance_and_movement) if not name.startswith("_")}
    forbidden = {
        "personal_possessions",
        "PERSONAL_POSSESSION_LIMIT",
        "owned_items",
        "possession_limit",
    }
    assert public & forbidden == set()
    # The gate reads a cn total, not an inventory.
    assert rate_of(400, CC.MYSTIC, 16).normal == 320
    assert rate_of(401, CC.MYSTIC, 16).normal == 90


def test_m76_no_terrain_modifier_is_reachable_from_this_card() -> None:
    """M76 — terrain modifier requested: no terrain mechanic exists here."""
    public = {name for name in vars(encumbrance_and_movement) if not name.startswith("_")}
    forbidden = {
        "terrain",
        "Terrain",
        "TERRAIN_MODIFIERS",
        "rough_terrain",
        "broken_terrain",
        "terrain_modifier",
    }
    assert public & forbidden == set()
    assert "terrain" not in inspect.signature(movement_rate).parameters


# ===========================================================================
# Implementation and coverage tests below. NOT approved contract cases.
# ===========================================================================


# --- §7 conditions are NOT V1-WIRED ----------------------------------------


def test_no_condition_infrastructure_was_built_in_anticipation() -> None:
    """Plan §8 — nothing in §7 is implemented, and no hook for it exists.

    Every causation owner is Unresearched, so no landed or approved card can
    produce blindness, stunning, prone or starvation. SR-10 stays approved
    and recorded on the card.
    """
    assert "condition" not in inspect.signature(movement_rate).parameters
    public = {name for name in vars(encumbrance_and_movement) if not name.startswith("_")}
    forbidden = {
        "Condition",
        "CONDITIONS",
        "condition_modifier",
        "apply_conditions",
        "blindness",
        "BLINDNESS_UNGUIDED",
        "stunned",
        "STARVATION_MULTIPLIERS",
        "starvation",
        "prone",
    }
    assert public & forbidden == set()


def test_no_starvation_multiplier_is_implemented() -> None:
    """SR-10 is recorded on the card and implemented nowhere (plan §8)."""
    source = inspect.getsource(encumbrance_and_movement)
    for forbidden in ("Fraction(3, 4)", "Fraction(1, 2)", "Fraction(1, 4)"):
        assert forbidden not in source


# --- No float anywhere -----------------------------------------------------


def test_no_floating_point_appears_in_the_module() -> None:
    # Asserted over the parsed module rather than its text, so a docstring
    # or an identifier such as "may_attack_in_the_same_round" cannot trip it.
    module = ast.parse(inspect.getsource(encumbrance_and_movement))
    for node in ast.walk(module):
        if isinstance(node, ast.Constant):
            assert not isinstance(node.value, float)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            assert node.func.id not in ("float", "round")
        if isinstance(node, ast.Name):
            assert node.id != "Decimal"


@pytest.mark.parametrize("level", sorted(MYSTIC_MV))
def test_every_rate_this_module_produces_is_an_exact_rational(level: int) -> None:
    for encumbrance_cn in (0, 400, 401, 801, 1201, 1601, 2401):
        rate = movement_rate(CC.MYSTIC, level, encumbrance_cn)
        for value in (rate.normal, rate.encounter, rate.running):
            assert isinstance(value, Fraction)
            assert not isinstance(value, float)


# --- Ownership boundary ----------------------------------------------------


def test_this_module_owns_no_item_or_dungeon_behaviour() -> None:
    # CHAR-004 supplies cn; EXP-003 spends the rate; EXP-002 owns time.
    # Asserted over the import graph, not the prose, which names those cards.
    module = ast.parse(inspect.getsource(encumbrance_and_movement))
    imported_from = {
        node.module
        for node in ast.walk(module)
        if isinstance(node, ast.ImportFrom) and node.module is not None
    }
    assert not any("exploration" in name for name in imported_from)
    assert imported_from == {
        "collections.abc",
        "dataclasses",
        "enum",
        "fractions",
        "types",
        "typing",
        "__future__",
        "rules.character_creation.character_class",
        "rules.character_creation.equipment",
        "rules.character_creation.errors",
    }
    public = {name for name in vars(encumbrance_and_movement) if not name.startswith("_")}
    forbidden = {
        "turn_movement_allowance",
        "DungeonMovementAllowance",
        "TurnCredit",
        "complete_ordinary_turn",
        "catalog_item",
        "is_legal",
        "purchase_cost",
    }
    assert public & forbidden == set()


def test_only_the_suit_armor_integer_crosses_from_char_004() -> None:
    # The import exists for one value, and that value is an int.
    assert isinstance(SUIT_ARMOR_ENCUMBRANCE_CN, int)
    assert not isinstance(SUIT_ARMOR_ENCUMBRANCE_CN, bool)


def test_the_mystic_table_is_immutable() -> None:
    assert isinstance(MYSTIC_MV, MappingProxyType)
    with pytest.raises(TypeError):
        MYSTIC_MV[1] = 999  # type: ignore[index]


def test_the_mystic_table_covers_exactly_levels_one_to_sixteen() -> None:
    assert sorted(MYSTIC_MV) == list(range(1, MYSTIC_MAXIMUM_LEVEL + 1))
    assert MYSTIC_MV[1] == 120
    assert MYSTIC_MV[MYSTIC_MAXIMUM_LEVEL] == 320


def test_the_mystic_progression_is_a_table_not_a_formula() -> None:
    # 10-foot steps to 11th level, 20-foot steps thereafter: no arithmetic
    # rule reproduces it, which is why it is transcribed.
    steps = [MYSTIC_MV[level + 1] - MYSTIC_MV[level] for level in range(1, 16)]
    assert steps == [10] * 10 + [20] * 5


# --- Validation ------------------------------------------------------------


@pytest.mark.parametrize("bad", [0, -1])
def test_a_level_below_one_is_refused(bad: int) -> None:
    with pytest.raises(MovementLevelError, match="at least 1"):
        rate_of(0, CC.MYSTIC, bad)


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_level_is_refused(bad: bool) -> None:
    with pytest.raises(MovementLevelError, match="must be an int"):
        rate_of(0, CC.MYSTIC, bad)


@pytest.mark.parametrize("bad", ["1", None, 1.0])
def test_a_non_int_level_is_refused(bad: object) -> None:
    with pytest.raises(MovementLevelError, match="must be an int"):
        rate_of(0, CC.MYSTIC, bad)  # type: ignore[arg-type]


@pytest.mark.parametrize("cls", list(CharacterClass))
def test_every_class_maximum_level_is_accepted_and_one_past_it_is_not(
    cls: CharacterClass,
) -> None:
    """§1.1 — the per-class maximum bounds the input for EVERY class."""
    maximum = MAXIMUM_LEVEL[cls]
    assert movement_rate(cls, maximum, 0).normal > 0
    with pytest.raises(MovementLevelError, match=f"at most {maximum}"):
        movement_rate(cls, maximum + 1, 0)


def test_the_maximum_level_projection_matches_char_003s() -> None:
    """Two card-local projections of one ADV-002 property must not drift.

    CHAR-003 projects the same maxima to bound hit-point accrual. Reaching
    into its private table is deliberate: this test exists so that changing
    one projection without the other fails loudly here rather than leaving
    the two cards quietly disagreeing about who can reach what level.
    """
    from rules.character_creation.hit_points_and_hit_dice import _MAXIMUM_LEVEL

    assert dict(MAXIMUM_LEVEL) == dict(_MAXIMUM_LEVEL)


def test_the_maximum_level_table_covers_every_class() -> None:
    assert set(MAXIMUM_LEVEL) == set(CharacterClass)
    assert MAXIMUM_LEVEL[CC.MYSTIC] == MYSTIC_MAXIMUM_LEVEL == 16
    # The demihuman limits and the human 36 are ADV-002's property,
    # projected here only to bound what this card accepts.
    assert MAXIMUM_LEVEL[CC.DWARF] == 12
    assert MAXIMUM_LEVEL[CC.ELF] == 10
    assert MAXIMUM_LEVEL[CC.HALFLING] == 8
    assert MAXIMUM_LEVEL[CC.FIGHTER] == 36


def test_the_maximum_level_table_is_immutable() -> None:
    assert isinstance(MAXIMUM_LEVEL, MappingProxyType)
    with pytest.raises(TypeError):
        MAXIMUM_LEVEL[CC.FIGHTER] = 99  # type: ignore[index]


def test_a_non_character_class_is_refused() -> None:
    with pytest.raises(ValueError, match="cls must be a CharacterClass"):
        movement_rate("fighter", 1, 0)  # type: ignore[arg-type]


@pytest.mark.parametrize("bad", ["0", None, 1.5])
def test_a_movement_rate_cannot_be_built_from_a_non_fraction(bad: object) -> None:
    with pytest.raises(ValueError, match="must be a Fraction"):
        MovementRate(bad)  # type: ignore[arg-type]


def test_a_negative_movement_rate_is_refused() -> None:
    with pytest.raises(ValueError, match="must not be negative"):
        MovementRate(Fraction(-1))


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_normal_speed_is_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="must not be a bool"):
        MovementRate(bad)  # type: ignore[arg-type]


def test_an_int_normal_speed_is_refused() -> None:
    # Rates stay exact rationals; accepting a bare int would invite a float
    # to arrive by the same door.
    with pytest.raises(ValueError, match="must be a Fraction"):
        MovementRate(120)  # type: ignore[arg-type]


def test_movement_rates_are_immutable() -> None:
    import dataclasses

    with pytest.raises(dataclasses.FrozenInstanceError):
        rate_of(0).normal = Fraction(999)  # type: ignore[misc]


def test_a_party_needs_at_least_one_member() -> None:
    with pytest.raises(ValueError, match="at least one member"):
        party_movement_rate([])


def test_a_party_member_must_be_a_movement_rate() -> None:
    with pytest.raises(ValueError, match="must be a MovementRate"):
        party_movement_rate([rate_of(0), 90])  # type: ignore[list-item]


def test_combat_movement_validates_its_arguments() -> None:
    with pytest.raises(ValueError, match="rate must be a MovementRate"):
        combat_movement(90, MovementMode.ENCOUNTER)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="mode must be a MovementMode"):
        combat_movement(rate_of(0), "encounter")  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="already_engaged must be a bool"):
        combat_movement(rate_of(0), MovementMode.RUNNING, already_engaged=1)  # type: ignore[arg-type]


def test_may_attack_validates_its_argument() -> None:
    with pytest.raises(ValueError, match="mode must be a MovementMode"):
        may_attack_in_the_same_round("running")  # type: ignore[arg-type]


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_round_or_turn_count_is_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="must be an int"):
        run_for(bad)
    with pytest.raises(ValueError, match="must be an int"):
        is_rested(bad)


def test_negative_round_and_turn_counts_are_refused() -> None:
    with pytest.raises(ValueError, match="must not be negative"):
        run_for(-1)
    with pytest.raises(ValueError, match="must not be negative"):
        is_rested(-1)
