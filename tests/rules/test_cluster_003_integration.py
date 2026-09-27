"""CLUSTER-003 cross-card integration — Slice F.

Canonical owner of the cluster's cross-card composition evidence, per
docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md §9.2 and §10.1.

    executable cross-card composition   E60, M25, M29, D28, D29, D30
    the worked fixture (plan §10.1)     the whole chain, both gate states

Every case ID above already has a canonical owning test in its own slice's
module; this file **re-owns none of them**. It exists to prove that the
independent components agree at runtime, and the ISSUE-020 ledger records
where each of the 176 approved cases is owned.

**This slice adds no production code.** These tests compose the real public
APIs of Slices A-E directly, in the approved order. No engine, creator,
builder, session, state object or test-only coordinator is introduced — the
tests demonstrate that independent rules components agree, they do not
create an application layer (plan §4.1).

**Every component is real.** The RNG is a ScriptedRNG, which exercises the
same parsing and aggregation logic as SeededRNG; everything else is the
production object, including landed EXP-002's DungeonTimeAccounting. No
stub, fake or test double of a rules procedure appears anywhere below.
"""

from fractions import Fraction

import pytest

from rng import ScriptedRNG
from rules.character_creation.ability import AbilityScores
from rules.character_creation.character_class import CharacterClass
from rules.character_creation.encumbrance_and_movement import (
    MYSTIC_UNENCUMBERED_MAXIMUM_CN,
    SUIT_ARMOR_ENCUMBRANCE_CN,
    MovementMode,
    combat_movement,
    movement_rate,
    party_movement_rate,
)
from rules.character_creation.equipment import (
    ADVENTURING_GEAR,
    ARMOR,
    TORCH,
    WEAPONS,
    Material,
    ammunition_encumbrance,
    clothing_encumbrance,
    commissioned,
    filled_container_encumbrance,
    free_starting_kit,
    is_legal,
    purchase_cost,
    selection_cost,
    starting_gold,
    starting_kit_encumbrance,
)
from rules.character_creation.errors import EquipmentLegalityError
from rules.character_creation.hit_points_and_hit_dice import hit_point_gain
from rules.character_creation.race_and_class_eligibility import (
    Eligibility,
    eligibility,
)
from rules.currency import Coin, Denomination
from rules.exploration.dungeon_movement import turn_movement_allowance
from rules.exploration.dungeon_turn_time_accounting import DungeonTimeAccounting
from rules.exploration.turn_credit import TurnCreditOrigin

CC = CharacterClass
GP = Denomination.GOLD

WATERSKIN_FILLED_CN = 30
BACKPACK_WITH_RATIONS_CN = 220
FILLED_POUCH_CN = 52


def _scores(
    strength: int = 12,
    intelligence: int = 12,
    wisdom: int = 12,
    dexterity: int = 12,
    constitution: int = 12,
    charisma: int = 12,
) -> AbilityScores:
    return AbilityScores(
        strength=strength,
        intelligence=intelligence,
        wisdom=wisdom,
        dexterity=dexterity,
        constitution=constitution,
        charisma=charisma,
    )


# --- The worked fixture from implementation plan §10.1 ---------------------
#
# A 10th-level Mystic, legally equipped, driven through every card in the
# cluster with real components. It exercises SR-9 in BOTH directions, the
# worn-clothing rule, SR-6, the exact-fraction path and the EXP-002
# boundary — which is why the plan named it before any code existed.


def _mystic_load() -> dict[str, int]:
    """The plan's §10.1 pack, each line derived by the card that owns it."""
    return {
        "dagger": WEAPONS["Dagger, Normal"].encumbrance_cn,
        "backpack_with_rations": filled_container_encumbrance(
            ADVENTURING_GEAR["Backpack"],
            ADVENTURING_GEAR["Rations, standard"].encumbrance_cn,
        ),
        "waterskin_filled": WATERSKIN_FILLED_CN,
        "belt_pouch_filled": filled_container_encumbrance(
            ADVENTURING_GEAR["Pouch, belt"], ADVENTURING_GEAR["Pouch, belt"].capacity_cn or 0
        ),
        "torches_six": 6 * TORCH.encumbrance_cn,
        "rope": ADVENTURING_GEAR["Rope"].encumbrance_cn,
    }


def test_the_plan_fixture_pack_totals_482_cn_with_worn_clothing_free() -> None:
    """CHAR-004 half of §10.1: 10 + 220 + 30 + 52 + 120 + 50 = 482 cn."""
    load = _mystic_load()
    assert load == {
        "dagger": 10,
        "backpack_with_rations": BACKPACK_WITH_RATIONS_CN,
        "waterskin_filled": WATERSKIN_FILLED_CN,
        "belt_pouch_filled": FILLED_POUCH_CN,
        "torches_six": 120,
        "rope": 50,
    }
    assert sum(load.values()) == 482

    # Clothes and shoes are WORN, so they contribute nothing (E14).
    assert clothing_encumbrance(ADVENTURING_GEAR["Clothes, plain"], worn=True) == 0
    assert clothing_encumbrance(ADVENTURING_GEAR["Shoes"], worn=True) == 0

    # And a Mystic may wear no armour at all (E48), which is why the pack
    # has none to weigh.
    for armour in ARMOR.values():
        assert not is_legal(CC.MYSTIC, armour)


def test_the_plan_fixture_chain_with_the_gate_closed() -> None:
    """§10.1, first half — 482 cn closes the SR-9 gate.

    CHAR-004 -> CHAR-005 -> EXP-003 -> EXP-002, real components throughout.
    The Mystic moves 90' (30'), NOT 210': it is not immune (M34, M38).
    """
    total_cn = sum(_mystic_load().values())
    assert total_cn == 482
    assert total_cn > MYSTIC_UNENCUMBERED_MAXIMUM_CN

    rate = movement_rate(CC.MYSTIC, 10, total_cn)
    assert rate.normal == 90
    assert rate.encounter == 30
    assert rate.running == 90
    assert rate.normal != 210
    # Identical to an ordinary character's at the same load: no scaling.
    assert rate == movement_rate(CC.FIGHTER, 1, total_cn)

    allowance = turn_movement_allowance(rate)
    assert allowance.feet == 90
    assert allowance.squares() == 9

    accounting = DungeonTimeAccounting()
    credit = accounting.complete_ordinary_turn()
    assert credit.turn_number == 1
    assert credit.origin is TurnCreditOrigin.ORDINARY


def test_the_plan_fixture_chain_with_the_gate_open() -> None:
    """§10.1, second half — dropping the torches and rope opens the gate.

    482 - 170 = 312 cn -> MV 210' -> encounter 70' EXACTLY -> 21 squares.
    """
    load = _mystic_load()
    dropped = load.pop("torches_six") + load.pop("rope")
    assert dropped == 170

    total_cn = sum(load.values())
    assert total_cn == 312
    assert total_cn <= MYSTIC_UNENCUMBERED_MAXIMUM_CN

    rate = movement_rate(CC.MYSTIC, 10, total_cn)
    assert rate.normal == 210
    assert rate.encounter == 70
    assert rate.running == 210

    allowance = turn_movement_allowance(rate)
    assert allowance.feet == 210
    assert allowance.squares() == 21


def test_the_fixture_gate_flips_on_exactly_one_coin_weight() -> None:
    """SR-9 is a threshold, so the whole chain turns on 400 vs 401 cn."""
    open_rate = movement_rate(CC.MYSTIC, 10, 400)
    shut_rate = movement_rate(CC.MYSTIC, 10, 401)
    assert turn_movement_allowance(open_rate).feet == 210
    assert turn_movement_allowance(shut_rate).feet == 90


# --- The full creation-to-exploration chain --------------------------------


def test_a_character_is_created_equipped_and_moved_with_real_components() -> None:
    """The authoritative chain, end to end, using production objects only.

    CHAR-001 scores -> CHAR-002 eligibility -> CHAR-003 hit points ->
    CHAR-004 money, legality and encumbrance -> CHAR-005 rate ->
    EXP-003 allowance -> EXP-002 turn credit.
    """
    # CHAR-001 / CHAR-002 — a fighter with ordinary scores is eligible.
    scores = _scores(strength=13, constitution=13)
    assert eligibility(scores, CC.FIGHTER) is Eligibility.ELIGIBLE

    # CHAR-003 — one rolled level, one real die.
    gained = hit_point_gain(ScriptedRNG([6]), CC.FIGHTER, 1, scores.constitution)
    assert gained == 7  # 6 rolled, +1 for Constitution 13

    # CHAR-004 — starting money, a legal selection, and its cost.
    money = starting_gold(ScriptedRNG([6, 6, 6]))
    assert money == Coin.of(180, GP)

    selection = [
        WEAPONS["Sword, Normal"],
        ARMOR["Chain Mail"],
        ARMOR["Shield"],
        ADVENTURING_GEAR["Backpack"],
        ADVENTURING_GEAR["Rope"],
    ]
    for item in selection:
        assert is_legal(CC.FIGHTER, item)
        assert purchase_cost(CC.FIGHTER, item) == item.price.cost_of(1)

    cost = selection_cost(selection)
    assert cost == Coin.of(66, GP)  # 10 + 40 + 10 + 5 + 1
    assert cost <= money
    assert money - cost == Coin.of(114, GP)

    # CHAR-004 — total carried encumbrance, including the free kit.
    kit = free_starting_kit(2)
    carried_cn = starting_kit_encumbrance(kit) + sum(
        item.encumbrance_cn for item in selection
    )
    assert starting_kit_encumbrance(kit) == 2  # the belt-pouch, empty
    assert carried_cn == 2 + 60 + 400 + 100 + 20 + 50
    assert carried_cn == 632

    # CHAR-005 — the rate, from that total.
    rate = movement_rate(CC.FIGHTER, 1, carried_cn)
    assert rate.normal == 90
    assert rate.encounter == 30

    # EXP-003 — the exploration allowance.
    allowance = turn_movement_allowance(rate)
    assert allowance.feet == 90
    assert allowance.squares() == 9

    # EXP-002 — the turn credit, from the landed implementation.
    accounting = DungeonTimeAccounting()
    assert accounting.complete_ordinary_turn().turn_number == 1


def test_the_chain_refuses_an_illegal_selection_before_it_reaches_movement() -> None:
    """Card §5 step 3 rejects before cost is summed, so nothing downstream runs."""
    with pytest.raises(EquipmentLegalityError):
        purchase_cost(CC.MAGIC_USER, ARMOR["Plate Mail"])


# --- Cross-card composition evidence ---------------------------------------


def test_e60_char_004_cannot_be_asked_for_a_movement_rate() -> None:
    """E60 — composed: the rate comes from CHAR-005, never from an item.

    equipment supplies cn; movement_rate consumes a total. There is no path
    from an Item to a rate that does not pass through a cn integer.
    """
    item = ARMOR["Plate Mail"]
    assert not hasattr(item, "movement_rate")
    assert isinstance(item.encumbrance_cn, int)
    assert movement_rate(CC.FIGHTER, 1, item.encumbrance_cn).normal == 90


def test_m25_and_m29_suit_armor_composes_through_encumbrance_only() -> None:
    """M25, M29 — composed: Suit Armor reaches movement as 750 cn and nothing else.

    The value crosses the card boundary as an integer from CHAR-004's
    catalog, and CHAR-005 bands it ordinarily. There is no item-shaped path
    into movement for an override to travel along.
    """
    suit = ARMOR["Suit Armor"]
    assert suit.encumbrance_cn == SUIT_ARMOR_ENCUMBRANCE_CN == 750

    alone = movement_rate(CC.FIGHTER, 1, suit.encumbrance_cn)
    assert alone.normal == 90  # NOT 30
    assert turn_movement_allowance(alone).feet == 90

    # Additional gear keeps banding ordinarily (M26, M27).
    with_gear = movement_rate(
        CC.FIGHTER, 1, suit.encumbrance_cn + ARMOR["Shield"].encumbrance_cn
    )
    assert with_gear.normal == 60


def test_d29_the_party_rate_reaches_exploration_through_char_005() -> None:
    """D29 — composed: EXP-003 consumes the party rate CHAR-005 §8 derives."""
    party = [
        movement_rate(CC.FIGHTER, 1, 0),
        movement_rate(CC.DWARF, 1, 401),
        movement_rate(CC.HALFLING, 1, 801),
    ]
    group = party_movement_rate(party)
    assert group.normal == 60
    assert turn_movement_allowance(group).feet == 60


def test_d30_a_fractional_mystic_rate_survives_every_card_boundary() -> None:
    """D30 — composed: nothing between CHAR-005 and EXP-003 rounds a rate.

    The Mystic's encounter rate is an exact third at eight of sixteen
    levels; the normal speed EXP-003 consumes is whole, and the exactness of
    the encounter rate survives alongside it.
    """
    rate = movement_rate(CC.MYSTIC, 2, 0)
    assert rate.normal == 130
    assert rate.encounter == Fraction(130, 3)
    assert isinstance(rate.encounter, Fraction)

    allowance = turn_movement_allowance(rate)
    assert allowance.feet == 130
    assert allowance.squares() == 13
    assert allowance.squares(3) == Fraction(130, 3)


def test_d28_movement_and_time_compose_without_either_owning_the_other() -> None:
    """D28 — composed: EXP-003 returns an allowance, EXP-002 returns credits.

    Three turns of exploration at the same rate. The allowance does not
    advance time and the credit does not carry a distance; the caller holds
    both, which is exactly the separation the two cards describe.
    """
    accounting = DungeonTimeAccounting()
    rate = movement_rate(CC.FIGHTER, 1, 0)

    covered = Fraction(0)
    for expected_turn in (1, 2, 3):
        allowance = turn_movement_allowance(rate)
        covered += allowance.feet
        credit = accounting.complete_ordinary_turn()
        assert credit.turn_number == expected_turn
        assert credit.origin is TurnCreditOrigin.ORDINARY

    assert covered == 360
    assert not hasattr(credit, "feet")


def test_the_combat_boundary_holds_from_both_sides() -> None:
    """M21 and D6 composed — normal speed never enters the combat sequence.

    EXP-003 uses normal speed for the exploration turn; CHAR-005 refuses it
    for a combat round. The same rate object serves both, and the boundary
    is enforced where the scale changes.
    """
    rate = movement_rate(CC.FIGHTER, 1, 0)
    assert turn_movement_allowance(rate).feet == rate.normal == 120
    assert combat_movement(rate, MovementMode.ENCOUNTER) == 40
    with pytest.raises(Exception, match="never used during the combat sequence"):
        combat_movement(rate, MovementMode.NORMAL)


# --- The Druid surcharge, composed through the currency primitive ----------


def test_the_druid_surcharge_stays_exact_through_the_whole_money_path() -> None:
    """E51/E52 composed with Slice A — 4.5 gp exists only as 450 copper pieces.

    The surcharge is applied by the shared primitive's exact scaling, and
    the result is a Coin like any other: it can be summed, compared against
    starting money and deducted, with no float anywhere.
    """
    club = commissioned(WEAPONS["Club"], Material.ALL_WOODEN)
    druid_price = purchase_cost(CC.DRUID, club)
    assert druid_price == Coin(450)
    assert druid_price == Coin.of(45, Denomination.SILVER)

    # Class-specific: the same object costs a non-druid the printed price.
    assert purchase_cost(CC.FIGHTER, club) == Coin.of(3, GP)

    money = starting_gold(ScriptedRNG([1, 1, 1]))
    assert money == Coin.of(30, GP)
    assert druid_price <= money
    assert money - druid_price == Coin(2550)


def test_a_cleric_may_not_buy_the_arrows_for_a_bow_it_may_not_use() -> None:
    """E38/E39 composed — the prohibition reaches weapon and ammunition alike."""
    from rules.character_creation.equipment import AMMUNITION

    assert not is_legal(CC.CLERIC, WEAPONS["Bow, Long"])
    assert not is_legal(CC.CLERIC, AMMUNITION["Arrow"])
    # And the encumbrance arithmetic is unaffected by legality: the two are
    # different questions, answered by different operations.
    assert ammunition_encumbrance(AMMUNITION["Arrow"], 10) == 5
