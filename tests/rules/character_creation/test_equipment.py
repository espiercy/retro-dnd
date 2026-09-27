"""CHAR-004 approved contract cases E1-E25 and E53-E60 (Slice B).

Slice B of docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md §10 owns the
catalogs, starting money and the derived-encumbrance cases. The per-class
legality and Druid-pricing cases **E26-E52 belong to Slice C** and appear
nowhere below; guard tests at the end assert that no legality or surcharge
behaviour has leaked into Slice B ahead of its authorization.

    this module   E1-E25, E53-E60
    Slice C       E26-E52

A clearly separated implementation/coverage section follows at the end.
Those tests are NOT approved contract cases and must not be counted among
CHAR-004's 60.
"""

import ast
import inspect
from types import MappingProxyType

import pytest

from rng import RollResult, ScriptedRNG
from rules.character_creation import equipment
from rules.character_creation.equipment import (
    ADVENTURING_GEAR,
    AMMUNITION,
    ARMOR,
    FILLED_QUIVER_ENCUMBRANCE_CN,
    IRON_SPIKE,
    STANDARD_LOAD_SHOTS,
    TORCH,
    WATERSKIN_FILLED_ENCUMBRANCE_CN,
    WEAPONS,
    Ammunition,
    FixedPrice,
    Item,
    ItemCategory,
    KitEntry,
    OpenEndedPrice,
    PurchaseOffer,
    QuantityPrice,
    WeaponSize,
    WeaponTrait,
    ammunition_encumbrance,
    catalog_item,
    clothing_encumbrance,
    filled_container_encumbrance,
    free_starting_kit,
    missile_weapon_encumbrance,
    net,
    resolve_price,
    selection_cost,
    starting_gold,
    starting_kit_encumbrance,
    unlisted_item,
    whip,
)
from rules.character_creation.errors import (
    EncumbranceError,
    UnlistedItemError,
    UnresolvedPriceError,
)
from rules.currency import Coin, Denomination

GP = Denomination.GOLD
SP = Denomination.SILVER
CP = Denomination.COPPER


# --- Starting money: E1-E4 -------------------------------------------------


@pytest.mark.parametrize(
    ("case", "script", "expected_gp"),
    [
        ("E1", [1, 1, 1], 30),
        ("E2", [6, 6, 6], 180),
        ("E3", [4, 3, 5], 120),
    ],
    ids=["E1-minimum", "E2-maximum", "E3-mid"],
)
def test_starting_gold_is_3d6_x_10(case: str, script: list[int], expected_gp: int) -> None:
    """E1, E2, E3 — starting money is 3d6 x 10 gp, spanning 30-180."""
    assert starting_gold(ScriptedRNG(script)) == Coin.of(expected_gp, GP)


class _RecordingRNG:
    """Wraps a real RNG and records the rules-facing calls made through it.

    Only the call log is added; every value still comes from the real
    ScriptedRNG, so nothing here manufactures a result (RNG_CONTRACT.md §9).
    """

    def __init__(self, inner: ScriptedRNG) -> None:
        self._inner = inner
        self.calls: list[tuple[str, object]] = []

    def roll_die(self, sides: int) -> RollResult:
        self.calls.append(("roll_die", sides))
        return self._inner.roll_die(sides)

    def roll(self, expression: str) -> RollResult:
        self.calls.append(("roll", expression))
        return self._inner.roll(expression)


def test_e4_starting_gold_consumes_exactly_three_d6_in_roll_order() -> None:
    """E4 — exactly three d6 per character, in roll order.

    One ``3d6`` expression: three d6 consumed from the head of the queue in
    order, one sequence number, and nothing else rolled. That the queue is
    consumed in order is ScriptedRNG's own guaranteed behaviour, covered by
    tests/rng.
    """
    scripted = ScriptedRNG([4, 3, 5, 6])
    rng = _RecordingRNG(scripted)
    assert starting_gold(rng) == Coin.of(120, GP)
    assert rng.calls == [("roll", "3d6")]
    # The fourth scripted value is untouched: exactly three were consumed.
    assert scripted.roll_die(6).total == 6


# --- Container encumbrance: E5-E13 -----------------------------------------


def test_e5_belt_pouch_empty_is_2_cn() -> None:
    """E5 — belt pouch, empty: 2 cn."""
    assert ADVENTURING_GEAR["Pouch, belt"].encumbrance_cn == 2


def test_e6_belt_pouch_fully_loaded_is_52_cn_and_never_55() -> None:
    """E6 — belt pouch, fully loaded: 52 cn (SR-6). Must not be 55."""
    pouch = ADVENTURING_GEAR["Pouch, belt"]
    assert pouch.capacity_cn == 50
    filled = filled_container_encumbrance(pouch, 50)
    assert filled == 52
    assert filled != 55


def test_e7_belt_pouch_carrying_20_cn_is_22_cn() -> None:
    """E7 — belt pouch carrying 20 cn of goods: 22 cn."""
    assert filled_container_encumbrance(ADVENTURING_GEAR["Pouch, belt"], 20) == 22


def test_e8_backpack_empty_is_20_cn() -> None:
    """E8 — backpack, empty: 20 cn."""
    assert ADVENTURING_GEAR["Backpack"].encumbrance_cn == 20


def test_e9_backpack_full_to_capacity_is_420_cn() -> None:
    """E9 — backpack full to its 400 cn capacity: 420 cn."""
    backpack = ADVENTURING_GEAR["Backpack"]
    assert backpack.capacity_cn == 400
    assert filled_container_encumbrance(backpack, 400) == 420


def test_e10_small_sack_is_1_cn_empty_and_201_cn_full() -> None:
    """E10 — sack, small: 1 cn empty, 201 cn full."""
    sack = ADVENTURING_GEAR["Sack, small"]
    assert sack.encumbrance_cn == 1
    assert sack.capacity_cn == 200
    assert filled_container_encumbrance(sack, 200) == 201


def test_e11_large_sack_is_5_cn_empty_and_605_cn_full() -> None:
    """E11 — sack, large: 5 cn empty, 605 cn full."""
    sack = ADVENTURING_GEAR["Sack, large"]
    assert sack.encumbrance_cn == 5
    assert sack.capacity_cn == 600
    assert filled_container_encumbrance(sack, 600) == 605


def test_e12_filled_quiver_is_10_cn_in_total_and_never_15() -> None:
    """E12 — quiver filled with 20 arrows: 10 cn total, not 5 + 10."""
    quiver = ADVENTURING_GEAR["Quiver"]
    assert quiver.encumbrance_cn == 5
    assert FILLED_QUIVER_ENCUMBRANCE_CN == 10
    naive_sum = quiver.encumbrance_cn + ammunition_encumbrance(AMMUNITION["Arrow"], 20)
    assert naive_sum == 15
    assert naive_sum != FILLED_QUIVER_ENCUMBRANCE_CN
    # The footnote * arithmetic is refused for the quiver rather than
    # silently producing that 15.
    with pytest.raises(EncumbranceError, match="footnote"):
        filled_container_encumbrance(quiver, 10)


@pytest.mark.parametrize(
    ("container", "over_capacity"),
    [("Pouch, belt", 51), ("Backpack", 401), ("Sack, small", 201), ("Sack, large", 601)],
)
def test_e13_goods_exceeding_capacity_are_refused(container: str, over_capacity: int) -> None:
    """E13 — goods exceeding a container's capacity: rejected; capacity is a hard limit."""
    with pytest.raises(EncumbranceError, match="hard limit"):
        filled_container_encumbrance(ADVENTURING_GEAR[container], over_capacity)


# --- Worn versus packed: E14-E16 -------------------------------------------


def test_e14_plain_clothes_worn_are_0_cn() -> None:
    """E14 — plain clothes, worn: 0 cn."""
    assert clothing_encumbrance(ADVENTURING_GEAR["Clothes, plain"], worn=True) == 0


def test_e15_plain_clothes_packed_are_20_cn() -> None:
    """E15 — plain clothes, packed: 20 cn."""
    assert clothing_encumbrance(ADVENTURING_GEAR["Clothes, plain"], worn=False) == 20


@pytest.mark.parametrize("sets", [2, 3])
def test_e16_free_starting_kit_as_issued_is_2_cn(sets: int) -> None:
    """E16 — free starting kit as issued: 2 cn total, whichever clothes count."""
    kit = free_starting_kit(sets)
    assert starting_kit_encumbrance(kit) == 2
    assert [entry.item.name for entry in kit] == [
        "Clothes, plain",
        "Shoes",
        "Belt",
        "Pouch, belt",
    ]


# --- Derived encumbrance: E17-E25 ------------------------------------------


@pytest.mark.parametrize(
    ("case", "side", "expected"),
    [("E17", 6, 36), ("E18", 4, 16)],
    ids=["E17-medium-net", "E18-small-net"],
)
def test_net_cost_and_encumbrance_follow_its_area(case: str, side: int, expected: int) -> None:
    """E17, E18 — a net costs 1 sp and weighs 1 cn per square foot."""
    made = net(side)
    assert made.encumbrance_cn == expected
    assert made.price == FixedPrice(Coin.of(expected, SP))


def test_e19_a_ten_foot_whip_is_100_cn_and_10_gp() -> None:
    """E19 — whip, 10 ft: 100 cn, cost 10 gp."""
    made = whip(10)
    assert made.encumbrance_cn == 100
    assert made.price == FixedPrice(Coin.of(10, GP))


def test_e20_long_bow_with_its_standard_load_is_30_cn() -> None:
    """E20 — long bow with standard load: 30 cn printed, which includes 20 arrows."""
    bow = WEAPONS["Bow, Long"]
    assert bow.encumbrance_cn == 30
    assert WeaponTrait.AMMUNITION_INCLUDED in bow.traits
    assert missile_weapon_encumbrance(bow, AMMUNITION["Arrow"], 20) == 30


def test_e21_long_bow_without_arrows_is_20_cn() -> None:
    """E21 — long bow without arrows: 20 cn."""
    assert missile_weapon_encumbrance(WEAPONS["Bow, Long"], AMMUNITION["Arrow"], 0) == 20


def test_e22_light_crossbow_without_quarrels_is_40_cn() -> None:
    """E22 — light crossbow without quarrels: 40 cn."""
    crossbow = WEAPONS["Crossbow, Lt"]
    assert crossbow.encumbrance_cn == 50
    assert missile_weapon_encumbrance(crossbow, AMMUNITION["Quarrel"], 0) == 40


def test_e23_ten_loose_arrows_are_5_cn() -> None:
    """E23 — 10 loose arrows: 5 cn, at RC's rate of 2 arrows per cn."""
    assert AMMUNITION["Arrow"].shots_per_cn == 2
    assert ammunition_encumbrance(AMMUNITION["Arrow"], 10) == 5


def test_e24_thirty_loose_sling_stones_are_6_cn() -> None:
    """E24 — 30 loose sling stones: 6 cn, at RC's rate of 5 stones per cn."""
    stones = AMMUNITION["Stone or lead pellet"]
    assert stones.shots_per_cn == 5
    assert ammunition_encumbrance(stones, 30) == 6


def test_e25_waterskin_is_5_cn_empty_and_30_cn_filled() -> None:
    """E25 — waterskin empty / filled: 5 cn / 30 cn."""
    assert ADVENTURING_GEAR["Waterskin/wineskin"].encumbrance_cn == 5
    assert WATERSKIN_FILLED_ENCUMBRANCE_CN == 30


# --- Purchase procedure: E53-E55 -------------------------------------------


def test_e53_a_selection_costing_more_than_money_held_is_invalid() -> None:
    """E53 — selection costing more than money held: INVALID; no partial purchase."""
    money = Coin.of(30, GP)
    selection = [WEAPONS["Sword, Normal"], ARMOR["Plate Mail"]]
    total = selection_cost(selection)
    assert total == Coin.of(70, GP)
    assert not total <= money
    # Deducting anyway is refused rather than producing a debt or a
    # part-filled selection.
    with pytest.raises(ValueError, match="must not be negative"):
        money - total


def test_e54_a_selection_costing_exactly_the_money_held_leaves_zero() -> None:
    """E54 — selection costing exactly the money held: VALID; remainder 0."""
    money = Coin.of(30, GP)
    total = selection_cost([WEAPONS["Sword, Normal"], ARMOR["Leather Armor"]])
    assert total == money
    assert money - total == Coin(0)


def test_e55_money_remaining_after_a_purchase_is_retained() -> None:
    """E55 — money remaining after purchase: retained, not discarded."""
    money = Coin.of(120, GP)
    total = selection_cost([WEAPONS["Dagger, Normal"], ADVENTURING_GEAR["Backpack"]])
    assert total == Coin.of(8, GP)
    assert money - total == Coin.of(112, GP)


# --- Unlisted items: E56-E57 -----------------------------------------------


def test_e56_an_item_absent_from_the_catalogs_is_refused() -> None:
    """E56 — item absent from the Ch. 4 catalogs, no DM allowance: REFUSED."""
    with pytest.raises(UnlistedItemError, match="not in the Chapter 4 catalogs"):
        catalog_item("Spyglass")


@pytest.mark.parametrize(
    ("cost", "encumbrance_cn"),
    [(None, 10), (Coin.of(5, GP), None), (None, None)],
    ids=["no-cost", "no-encumbrance", "neither"],
)
def test_e57_a_dm_allowance_without_cost_and_encumbrance_is_an_error(
    cost: Coin | None, encumbrance_cn: int | None
) -> None:
    """E57 — DM-allowed item without a cost and encumbrance: ERROR, must not default."""
    with pytest.raises(UnlistedItemError, match="permits no default"):
        unlisted_item("Spyglass", ItemCategory.GEAR, cost=cost, encumbrance_cn=encumbrance_cn)


def test_a_dm_allowed_item_with_both_values_is_built_as_given() -> None:
    """The other side of E57: supplied with both, the item is built and nothing invented."""
    item = unlisted_item(
        "Spyglass", ItemCategory.GEAR, cost=Coin.of(5, GP), encumbrance_cn=10
    )
    assert item == Item(
        name="Spyglass",
        category=ItemCategory.GEAR,
        price=FixedPrice(Coin.of(5, GP)),
        encumbrance_cn=10,
    )


# --- Guard cases: E58-E60 --------------------------------------------------


@pytest.mark.parametrize(
    "out_of_scope",
    [
        "Horse, Riding",
        "Horse, War",
        "Mule",
        "Cart",
        "Wagon",
        "Barding",
        "Saddle",
        "Small boat",
        "Sailing ship",
        "Galley, small",
        "Catapult",
        "Battering ram",
        "Siege tower",
    ],
)
def test_e58_mounts_vehicles_ships_and_siege_equipment_are_refused(out_of_scope: str) -> None:
    """E58 — mounts, vehicles, ships or siege equipment: REFUSED, out of V1 scope.

    They are printed in RC Chapter 4 but excluded by human decision, so they
    are simply not catalogued: nothing here silently prices or encumbers them.
    """
    with pytest.raises(UnlistedItemError):
        catalog_item(out_of_scope)


def test_e59_no_chapter_10_high_level_money_or_equipment_pathway_exists() -> None:
    """E59 — Chapter 10 high-level money or equipment: REFUSED, NOT V1-WIRED.

    Its cash rule is 1% of XP and its equipment is granted rather than
    bought. No entry point for either exists: starting_gold takes an RNG and
    nothing else, and no symbol mentions experience or a grant.
    """
    assert list(inspect.signature(starting_gold).parameters) == ["rng"]
    public = {name for name in vars(equipment) if not name.startswith("_")}
    forbidden = {
        "experience_points",
        "high_level_starting_money",
        "granted_equipment",
        "chapter_10_equipment",
        "equipment_grant",
        "xp_cash",
    }
    assert public & forbidden == set()


def test_e60_this_card_cannot_be_asked_for_a_movement_rate() -> None:
    """E60 — any caller asking this card for a movement rate: not its responsibility.

    The module returns cn only. It exposes no movement symbol, no encumbrance
    band and no total carried load — summing a character's load and reading a
    band from it are CHAR-005's.
    """
    public = {name for name in vars(equipment) if not name.startswith("_")}
    forbidden = {
        "movement_rate",
        "MovementRate",
        "encumbrance_band",
        "ENCUMBRANCE_BANDS",
        "total_encumbrance",
        "carried_encumbrance",
        "party_movement_rate",
        "running_rate",
        "encounter_rate",
    }
    assert public & forbidden == set()
    source = inspect.getsource(equipment)
    assert "encumbrance_and_movement" not in source
    assert "dungeon_movement" not in source


# --- Price-specification forms and the blowgun load: E61-E66 ---------------
# Added by the human-approved CHAR-004 amendment of 2026-09-26 (§4.1).


def test_e61_one_torch_costs_two_silver_pieces_exactly() -> None:
    """E61 — one torch purchased: 2 sp = 20 cp exactly, no fractional copper."""
    assert TORCH.price.cost_of(1) == Coin.of(2, SP)
    assert TORCH.price.cost_of(1) == Coin(20)


def test_e62_six_torches_cost_one_gold_piece_exactly() -> None:
    """E62 — six torches: 1 gp = 100 cp, the printed bundle offer.

    Not derived as six times one sixth of a gold piece: that fraction is
    16 2/3 cp, which RC cannot express and Coin cannot hold.
    """
    assert TORCH.price.cost_of(6) == Coin.of(1, GP)
    assert TORCH.price.cost_of(6) == Coin(100)
    # The printed source notation is preserved, not replaced.
    assert isinstance(TORCH.price, QuantityPrice)
    assert TORCH.price.printed_unit_notation == "1/6 gp"


def test_e62_a_count_rc_prints_no_offer_for_is_refused_not_prorated() -> None:
    """E62, other side — RC states no price for four torches, so none is invented."""
    with pytest.raises(UnresolvedPriceError, match="will not prorate"):
        TORCH.price.cost_of(4)


def test_e63_a_torch_used_as_a_weapon_is_the_same_commodity() -> None:
    """E63 — a torch used as a weapon: the same item, not a second priced commodity."""
    assert WEAPONS["Torch"] is ADVENTURING_GEAR["Torch"]
    assert WEAPONS["Torch"] is TORCH
    # It carries its Weapons Table size and note codes, and one price.
    assert TORCH.size is WeaponSize.SMALL
    assert WeaponTrait.CLERIC_PERMITTED in TORCH.traits
    assert TORCH.encumbrance_cn == 20


def test_e64_extravagant_clothes_refuse_to_answer_a_concrete_cost() -> None:
    """E64 — asked for a concrete cost: ERROR. Must not silently answer 50 gp."""
    clothes = ADVENTURING_GEAR["Clothes, extravagant"]
    assert isinstance(clothes.price, OpenEndedPrice)
    assert clothes.price.minimum == Coin.of(50, GP)
    with pytest.raises(UnresolvedPriceError, match="open-ended"):
        clothes.price.cost_of(1)
    # A consumer needing a total cannot get the floor by the back door either.
    with pytest.raises(UnresolvedPriceError, match="open-ended"):
        selection_cost([clothes])


@pytest.mark.parametrize("gp", [50, 51, 200, 5000])
def test_e65_a_resolved_price_at_or_above_the_floor_is_accepted(gp: int) -> None:
    """E65 — an explicitly resolved amount >= 50 gp is accepted; RC bounds it above by nothing."""
    resolved = resolve_price(ADVENTURING_GEAR["Clothes, extravagant"], Coin.of(gp, GP))
    assert resolved.price == FixedPrice(Coin.of(gp, GP))
    assert selection_cost([resolved]) == Coin.of(gp, GP)
    # Resolution does not disturb anything else about the row.
    assert resolved.encumbrance_cn == 30
    assert resolved.category is ItemCategory.CLOTHING


@pytest.mark.parametrize("gp", [49, 1, 0])
def test_e65_a_resolved_price_below_the_floor_is_refused(gp: int) -> None:
    """E65, other side — below the printed 50 gp minimum is refused."""
    with pytest.raises(UnresolvedPriceError, match="below the 5000 cp minimum"):
        resolve_price(ADVENTURING_GEAR["Clothes, extravagant"], Coin.of(gp, GP))


def test_e65_the_catalog_row_is_not_mutated_by_resolving_it() -> None:
    """E65 — resolution produces a new item; the printed open-ended row stands."""
    resolve_price(ADVENTURING_GEAR["Clothes, extravagant"], Coin.of(80, GP))
    assert isinstance(ADVENTURING_GEAR["Clothes, extravagant"].price, OpenEndedPrice)


def test_e67_a_sling_with_its_normal_load_is_its_printed_twenty_cn() -> None:
    """E67 — sling with its normal load: 20 cn as printed; it includes 30 stones."""
    stones = AMMUNITION["Stone or lead pellet"]
    assert WEAPONS["Sling"].encumbrance_cn == 20
    assert stones.shots_per_cn == 5
    assert ammunition_encumbrance(stones, 30) == 6
    assert missile_weapon_encumbrance(WEAPONS["Sling"], stones, 30) == 20


def test_e68_a_sling_without_stones_is_fourteen_cn() -> None:
    """E68 — sling without stones: 14 cn = 20 - (30 / 5).

    RC's own arithmetic on RC's own two values. Not the unofficial
    companion's house-corrected 3 cn, which corrects RC rather than
    interpreting it (card §6.3).
    """
    empty = missile_weapon_encumbrance(WEAPONS["Sling"], AMMUNITION["Stone or lead pellet"], 0)
    assert empty == 14
    assert empty != 3


def test_e68_a_sling_carrying_more_than_its_normal_load(
) -> None:
    """E68, extended — varying the load varies the encumbrance at RC's rate."""
    stones = AMMUNITION["Stone or lead pellet"]
    assert missile_weapon_encumbrance(WEAPONS["Sling"], stones, 60) == 26
    assert missile_weapon_encumbrance(WEAPONS["Sling"], stones, 15) == 17


def test_e66_a_blowgun_normal_load_is_five_darts() -> None:
    """E66 — blowgun normal load: 5 darts (Weapons note a; Ammunition Table)."""
    assert STANDARD_LOAD_SHOTS["Blowgun, up to 2'"] == 5
    assert STANDARD_LOAD_SHOTS["Blowgun, 2' +"] == 5
    assert AMMUNITION["Dart"].standard_load_shots == 5


def test_e66_the_blowgun_normal_load_is_exactly_one_cn() -> None:
    """E66 — at RC's rate of 5 darts per cn, the normal load is exactly 1 cn."""
    dart = AMMUNITION["Dart"]
    assert dart.shots_per_cn == 5
    assert ammunition_encumbrance(dart, 5) == 1


@pytest.mark.parametrize(
    ("weapon", "printed_cn", "empty_cn"),
    [("Blowgun, up to 2'", 6, 5), ("Blowgun, 2' +", 15, 14)],
)
def test_e66_blowgun_load_arithmetic_is_coherent(
    weapon: str, printed_cn: int, empty_cn: int
) -> None:
    """E66 — the former deliberate refusal is gone and the arithmetic works out.

    The printed Enc includes 5 darts, which weigh exactly 1 cn, so a blowgun
    without darts is one cn lighter than printed.
    """
    dart = AMMUNITION["Dart"]
    assert WEAPONS[weapon].encumbrance_cn == printed_cn
    assert missile_weapon_encumbrance(WEAPONS[weapon], dart, 5) == printed_cn
    assert missile_weapon_encumbrance(WEAPONS[weapon], dart, 0) == empty_cn
    assert missile_weapon_encumbrance(WEAPONS[weapon], dart, 10) == printed_cn + 1


# ===========================================================================
# Implementation and coverage tests below. NOT approved contract cases.
# ===========================================================================

# --- Slice C boundary: legality and Druid pricing must not exist yet -------


def test_slice_b_exposes_no_class_legality_or_druid_pricing() -> None:
    public = {name for name in vars(equipment) if not name.startswith("_")}
    forbidden = {
        "is_legal",
        "purchase_cost",
        "legality",
        "CLASS_LEGALITY",
        "DRUID_SURCHARGE",
        "druid_price",
        "wooden_weapon_cost",
        "EquipmentLegalityError",
        "magic_user_expanded_list",
    }
    assert public & forbidden == set()


def test_slice_b_imports_no_character_class() -> None:
    # Legality is the only reason this module would need class identity, and
    # legality is Slice C.
    assert "CharacterClass" not in inspect.getsource(equipment)


def test_no_floating_point_literal_or_conversion_appears_in_the_module() -> None:
    source = inspect.getsource(equipment)
    assert "float(" not in source
    assert "Decimal" not in source
    assert "round(" not in source


def test_the_currency_primitive_was_not_weakened_by_the_price_forms() -> None:
    # The 1/6 gp discovery must not have leaked a fraction into Coin. It is
    # still integral copper, non-negative, and refuses a non-whole result.
    assert Coin(450) == Coin.of(45, SP)
    with pytest.raises(ValueError, match="must be an int"):
        Coin(16.67)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="must not be negative"):
        Coin(-1)
    with pytest.raises(ValueError, match="will not round"):
        # One sixth of a gold piece is exactly what Coin still refuses.
        Coin.of(1, GP).scaled(1, 6)


def test_every_price_form_yields_only_whole_copper_amounts() -> None:
    amounts = []
    for catalog in (WEAPONS, ARMOR, ADVENTURING_GEAR):
        for row in catalog.values():
            if isinstance(row.price, FixedPrice):
                amounts.append(row.price.unit)
            elif isinstance(row.price, QuantityPrice):
                amounts.extend(offer.price for offer in row.price.offers)
            else:
                amounts.append(row.price.minimum)
    assert amounts
    for amount in amounts:
        assert isinstance(amount.copper, int)
        assert not isinstance(amount.copper, bool)
        assert amount.copper >= 0


# --- Catalog integrity -----------------------------------------------------


@pytest.mark.parametrize(
    "catalog", [WEAPONS, AMMUNITION, ARMOR, ADVENTURING_GEAR], ids=lambda c: str(len(c))
)
def test_catalogs_are_immutable(catalog: object) -> None:
    assert isinstance(catalog, MappingProxyType)
    with pytest.raises(TypeError):
        catalog["Anything"] = None  # type: ignore[index]


def test_catalog_rows_are_keyed_by_their_own_name() -> None:
    for catalog in (WEAPONS, ARMOR, ADVENTURING_GEAR, AMMUNITION):
        for key, row in catalog.items():
            assert key == row.name


def test_every_catalog_price_is_one_of_the_three_approved_forms() -> None:
    forms = (FixedPrice, QuantityPrice, OpenEndedPrice)
    for catalog in (WEAPONS, ARMOR, ADVENTURING_GEAR):
        for row in catalog.values():
            assert isinstance(row.price, forms)
    for ammunition in AMMUNITION.values():
        assert isinstance(ammunition.cost, Coin)


def test_only_the_two_adjudicated_rows_carry_a_non_fixed_price() -> None:
    # Card §4.1 records exactly two printed rows that are not one fixed
    # amount. No speculative price form is attached to anything else.
    non_fixed = {
        name
        for catalog in (WEAPONS, ARMOR, ADVENTURING_GEAR)
        for name, row in catalog.items()
        if not isinstance(row.price, FixedPrice)
    }
    assert non_fixed == {"Torch", "Iron spike", "Clothes, extravagant"}


@pytest.mark.parametrize(
    ("name", "cost_cp", "encumbrance_cn"),
    [
        ("Club", 300, 50),
        ("Dagger, Normal", 300, 10),
        ("Mace", 500, 30),
        ("Staff", 500, 40),
        ("Sword, Normal", 1000, 60),
        ("Sword, Two-Handed", 1500, 100),
        ("Bow, Short", 2500, 20),
        ("Sling", 200, 20),
        ("Rock, Thrown", 10, 10),
    ],
)
def test_sampled_weapon_rows_match_the_printed_table(
    name: str, cost_cp: int, encumbrance_cn: int
) -> None:
    row = WEAPONS[name]
    assert row.price == FixedPrice(Coin(cost_cp))
    assert row.encumbrance_cn == encumbrance_cn


@pytest.mark.parametrize(
    ("name", "cost_gp", "encumbrance_cn"),
    [
        ("Shield", 10, 100),
        ("Leather Armor", 20, 200),
        ("Scale Mail", 30, 300),
        ("Chain Mail", 40, 400),
        ("Banded Mail", 50, 450),
        ("Plate Mail", 60, 500),
        ("Suit Armor", 250, 750),
    ],
)
def test_armor_rows_match_card_section_6_1(name: str, cost_gp: int, encumbrance_cn: int) -> None:
    row = ARMOR[name]
    assert row.price == FixedPrice(Coin.of(cost_gp, GP))
    assert row.encumbrance_cn == encumbrance_cn


def test_suit_armor_is_750_cn_and_carries_no_rate_of_its_own() -> None:
    # SR-8: Suit Armor appears in src/ only as an integer in a catalog row.
    suit = ARMOR["Suit Armor"]
    assert suit.encumbrance_cn == 750
    assert suit == Item(
        name="Suit Armor",
        category=ItemCategory.ARMOR,
        price=FixedPrice(Coin.of(250, GP)),
        encumbrance_cn=750,
    )
    # Named nowhere in executable logic: no function in the module mentions
    # it, so no branch, rate or special case can turn on it.
    module = ast.parse(inspect.getsource(equipment))
    for node in ast.walk(module):
        if isinstance(node, ast.FunctionDef):
            for inner in ast.walk(node):
                assert not (isinstance(inner, ast.Constant) and inner.value == "Suit Armor")


def test_rcs_six_torch_bundle_row_is_the_six_count_offer_not_a_second_row() -> None:
    # RC prints "Torches / Six torches / 1 gp / 120". Both of its printed
    # values are represented: the price is the 6-count offer, and the 120 cn
    # is exactly six of the single torch's 20 cn.
    assert "Torches" not in ADVENTURING_GEAR
    assert TORCH.price.cost_of(6) == Coin.of(1, GP)
    assert 6 * TORCH.encumbrance_cn == 120


def test_rcs_twelve_spike_bundle_row_is_the_twelve_count_offer() -> None:
    # Found by the independent transcription review: RC prints "Iron spike /
    # One spike / 1 sp / 5" and "Iron spikes / Twelve spikes / 1 gp / 60".
    # Both printed prices are represented, and the bundle's 60 cn is exactly
    # twelve of the single spike's 5 cn.
    assert "Iron spikes" not in ADVENTURING_GEAR
    assert IRON_SPIKE.price.cost_of(1) == Coin.of(1, SP)
    assert IRON_SPIKE.price.cost_of(12) == Coin.of(1, GP)
    assert 12 * IRON_SPIKE.encumbrance_cn == 60
    assert ADVENTURING_GEAR["Iron spike"] is IRON_SPIKE


def test_only_the_net_carries_note_n_and_the_whip_prints_its_own_rates() -> None:
    # Found by the independent transcription review: the Whip row's Notes are
    # s,w,M with no `n`. Note n names the net alone.
    assert "n" not in {trait.value for trait in WeaponTrait}
    assert "Whip" not in WEAPONS
    made = whip(3)
    assert made.price == FixedPrice(Coin.of(3, GP))
    assert made.encumbrance_cn == 30


def test_a_net_carries_no_size_because_rc_prints_a_disjunction() -> None:
    # The net's Notes read "M or L" — a disjunction RC resolves through the
    # Nets Table, which is not this slice's. Nothing is guessed from the
    # dimensions.
    assert net(6).size is None
    assert net(9).size is None


def test_clothing_is_exactly_the_rows_carrying_footnote_two_stars() -> None:
    clothing = {
        name
        for name, row in ADVENTURING_GEAR.items()
        if row.category is ItemCategory.CLOTHING
    }
    assert clothing == {
        "Belt",
        "Boots, plain",
        "Boots, riding or swash-topped",
        "Cloak, short",
        "Cloak, long",
        "Clothes, plain",
        "Clothes, middle-class",
        "Clothes, fine",
        "Clothes, extravagant",
        "Shoes",
    }
    # "Hat or cap" prints no footnote marker, so it is not clothing.
    assert ADVENTURING_GEAR["Hat or cap"].category is ItemCategory.GEAR


def test_containers_are_exactly_the_rows_carrying_a_capacity_or_the_quiver() -> None:
    containers = {
        name
        for name, row in ADVENTURING_GEAR.items()
        if row.category is ItemCategory.CONTAINER
    }
    assert containers == {"Backpack", "Pouch, belt", "Sack, small", "Sack, large", "Quiver"}
    assert ADVENTURING_GEAR["Quiver"].capacity_cn is None


def test_ammunition_rows_match_the_printed_table() -> None:
    assert {name: row.shots_per_cn for name, row in AMMUNITION.items()} == {
        "Dart": 5,
        "Arrow": 2,
        "Silver-tipped arrow": 2,
        "Quarrel": 3,
        "Silver-tipped quarrel": 3,
        "Stone or lead pellet": 5,
        "Silver pellet": 5,
    }
    assert AMMUNITION["Arrow"].standard_load_shots == 20
    assert AMMUNITION["Quarrel"].standard_load_shots == 30
    assert AMMUNITION["Arrow"].cost == Coin.of(5, GP)


def test_weapon_sizes_are_read_from_the_notes_column() -> None:
    assert WEAPONS["Dagger, Normal"].size is WeaponSize.SMALL
    assert WEAPONS["Mace"].size is WeaponSize.MEDIUM
    assert WEAPONS["Sword, Two-Handed"].size is WeaponSize.LARGE
    assert WeaponTrait.TWO_HANDED in WEAPONS["Sword, Two-Handed"].traits
    assert WeaponTrait.HAND_OR_TWO_HANDED in WEAPONS["Sword, Bastard, One-Handed"].traits


# --- Derivation edges ------------------------------------------------------


def test_an_ammunition_count_rc_does_not_state_is_refused_rather_than_rounded() -> None:
    with pytest.raises(EncumbranceError, match="will not round"):
        ammunition_encumbrance(AMMUNITION["Arrow"], 3)


def test_standard_loads_are_exactly_the_weapons_rc_note_a_names() -> None:
    # Note a names four families: bow, crossbow, sling, blowgun.
    assert set(STANDARD_LOAD_SHOTS) == {
        "Bow, Short",
        "Bow, Long",
        "Crossbow, Lt",
        "Crossbow, Hvy",
        "Sling",
        "Blowgun, up to 2'",
        "Blowgun, 2' +",
    }


def test_the_transcribed_sling_row_still_prints_no_note_a_marker() -> None:
    """§6.3 — the marker defect is recorded on the card, not papered over here.

    RC prints the Sling row's notes as c,m,w,S. The approved resolution does
    not licence adding an `a` to the transcribed data to make it tidy, which
    is why the derivation reads STANDARD_LOAD_SHOTS instead.
    """
    assert WeaponTrait.AMMUNITION_INCLUDED not in WEAPONS["Sling"].traits
    assert WEAPONS["Sling"].traits == frozenset(
        {
            WeaponTrait.CLERIC_PERMITTED,
            WeaponTrait.MISSILE_ONLY,
            WeaponTrait.MAGIC_USER_DISCRETIONARY,
        }
    )
    assert STANDARD_LOAD_SHOTS["Sling"] == 30


def test_a_weapon_without_note_a_has_no_load_to_vary() -> None:
    with pytest.raises(EncumbranceError, match="nothing to vary"):
        missile_weapon_encumbrance(WEAPONS["Mace"], AMMUNITION["Arrow"], 10)


def test_a_non_container_is_refused_the_container_arithmetic() -> None:
    with pytest.raises(EncumbranceError, match="not a container"):
        filled_container_encumbrance(WEAPONS["Mace"], 10)


def test_a_non_garment_is_refused_the_worn_rule() -> None:
    with pytest.raises(EncumbranceError, match="footnote"):
        clothing_encumbrance(ADVENTURING_GEAR["Hat or cap"], worn=True)


def test_an_empty_container_carrying_nothing_is_its_printed_value() -> None:
    assert filled_container_encumbrance(ADVENTURING_GEAR["Backpack"], 0) == 20


def test_zero_shots_weigh_nothing() -> None:
    assert ammunition_encumbrance(AMMUNITION["Arrow"], 0) == 0


def test_selection_cost_of_nothing_is_zero() -> None:
    assert selection_cost([]) == Coin(0)


def test_packed_kit_clothing_carries_its_printed_value() -> None:
    # The kit is issued worn; the same entry packed is the printed value,
    # times the number of sets.
    entry = KitEntry(ADVENTURING_GEAR["Clothes, plain"], 3, worn=False)
    assert entry.encumbrance_cn == 60


def test_a_non_clothing_kit_entry_uses_the_printed_value_directly() -> None:
    assert KitEntry(ADVENTURING_GEAR["Rope"], 2, worn=False).encumbrance_cn == 100


# --- Validation ------------------------------------------------------------


@pytest.mark.parametrize("sets", [1, 4, 0, -1])
def test_a_clothes_count_outside_rcs_two_or_three_is_refused(sets: int) -> None:
    with pytest.raises(ValueError, match="two or three"):
        free_starting_kit(sets)


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_clothes_count_is_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="must be an int"):
        free_starting_kit(bad)


@pytest.mark.parametrize("bad", ["2", None])
def test_a_non_int_clothes_count_is_refused(bad: object) -> None:
    with pytest.raises(ValueError, match="must be an int"):
        free_starting_kit(bad)  # type: ignore[arg-type]


@pytest.mark.parametrize("bad", [0, -1])
def test_a_net_side_that_is_not_positive_is_refused(bad: int) -> None:
    with pytest.raises(ValueError, match="side_feet must be positive"):
        net(bad)


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_net_side_is_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="side_feet must be an int"):
        net(bad)


@pytest.mark.parametrize("bad", [0, -1])
def test_a_whip_length_that_is_not_positive_is_refused(bad: int) -> None:
    with pytest.raises(ValueError, match="length_feet must be positive"):
        whip(bad)


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_whip_length_is_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="length_feet must be an int"):
        whip(bad)


def test_negative_container_contents_are_refused() -> None:
    with pytest.raises(ValueError, match="contents_cn must not be negative"):
        filled_container_encumbrance(ADVENTURING_GEAR["Backpack"], -1)


@pytest.mark.parametrize("bad", [True, False])
def test_bool_container_contents_are_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="contents_cn must be an int"):
        filled_container_encumbrance(ADVENTURING_GEAR["Backpack"], bad)


def test_negative_shot_counts_are_refused() -> None:
    with pytest.raises(ValueError, match="shots must not be negative"):
        ammunition_encumbrance(AMMUNITION["Arrow"], -1)


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_shot_count_is_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="shots must be an int"):
        ammunition_encumbrance(AMMUNITION["Arrow"], bad)


def test_a_non_item_container_is_refused() -> None:
    with pytest.raises(ValueError, match="container must be an Item"):
        filled_container_encumbrance("Backpack", 10)  # type: ignore[arg-type]


def test_a_non_item_garment_is_refused() -> None:
    with pytest.raises(ValueError, match="item must be an Item"):
        clothing_encumbrance("Belt", worn=True)  # type: ignore[arg-type]


def test_a_non_bool_worn_flag_is_refused() -> None:
    with pytest.raises(ValueError, match="worn must be a bool"):
        clothing_encumbrance(ADVENTURING_GEAR["Belt"], worn=1)  # type: ignore[arg-type]


def test_a_non_ammunition_row_is_refused() -> None:
    with pytest.raises(ValueError, match="row must be an Ammunition"):
        ammunition_encumbrance(WEAPONS["Sling"], 10)  # type: ignore[arg-type]


def test_a_non_item_weapon_is_refused() -> None:
    with pytest.raises(ValueError, match="weapon must be an Item"):
        missile_weapon_encumbrance("Bow, Long", AMMUNITION["Arrow"], 10)  # type: ignore[arg-type]


def test_a_non_item_in_a_selection_is_refused() -> None:
    with pytest.raises(ValueError, match="must be an Item"):
        selection_cost([WEAPONS["Mace"], "Plate Mail"])  # type: ignore[list-item]


def test_a_non_item_kit_entry_is_refused() -> None:
    with pytest.raises(ValueError, match="item must be an Item"):
        KitEntry("Rope", 1, worn=False)  # type: ignore[arg-type]


@pytest.mark.parametrize("bad", [0, -1])
def test_a_kit_entry_count_that_is_not_positive_is_refused(bad: int) -> None:
    with pytest.raises(ValueError, match="count must be positive"):
        KitEntry(ADVENTURING_GEAR["Rope"], bad, worn=False)


def test_a_non_bool_kit_entry_worn_flag_is_refused() -> None:
    with pytest.raises(ValueError, match="worn must be a bool"):
        KitEntry(ADVENTURING_GEAR["Belt"], 1, worn=1)  # type: ignore[arg-type]


@pytest.mark.parametrize("bad", ["", None, 7])
def test_an_item_without_a_usable_name_is_refused(bad: object) -> None:
    with pytest.raises(ValueError, match="name must be a non-empty str"):
        Item(
            name=bad,  # type: ignore[arg-type]
            category=ItemCategory.GEAR,
            price=FixedPrice(Coin(1)),
            encumbrance_cn=1,
        )


def test_an_item_price_that_is_not_a_price_form_is_refused() -> None:
    with pytest.raises(ValueError, match="price must be a Price"):
        # A bare Coin is an amount, not a price specification.
        Item(name="x", category=ItemCategory.GEAR, price=Coin(1), encumbrance_cn=1)  # type: ignore[arg-type]


def test_a_negative_item_encumbrance_is_refused() -> None:
    with pytest.raises(ValueError, match="encumbrance_cn must not be negative"):
        Item(
            name="x",
            category=ItemCategory.GEAR,
            price=FixedPrice(Coin(1)),
            encumbrance_cn=-1,
        )


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_item_encumbrance_is_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="encumbrance_cn must be an int"):
        Item(
            name="x",
            category=ItemCategory.GEAR,
            price=FixedPrice(Coin(1)),
            encumbrance_cn=bad,
        )


@pytest.mark.parametrize("bad", [0, -1])
def test_an_item_capacity_that_is_not_positive_is_refused(bad: int) -> None:
    with pytest.raises(ValueError, match="capacity_cn must be positive"):
        Item(
            name="x",
            category=ItemCategory.CONTAINER,
            price=FixedPrice(Coin(1)),
            encumbrance_cn=1,
            capacity_cn=bad,
        )


@pytest.mark.parametrize("bad", [0, -1])
def test_an_ammunition_standard_load_that_is_not_positive_is_refused(bad: int) -> None:
    with pytest.raises(ValueError, match="standard_load_shots must be positive"):
        Ammunition("x", "Bow", bad, Coin(1), 2)


@pytest.mark.parametrize("bad", [0, -1])
def test_an_ammunition_rate_that_is_not_positive_is_refused(bad: int) -> None:
    with pytest.raises(ValueError, match="shots_per_cn must be positive"):
        Ammunition("x", "Bow", 20, Coin(1), bad)


def test_items_are_immutable() -> None:
    import dataclasses

    with pytest.raises(dataclasses.FrozenInstanceError):
        ADVENTURING_GEAR["Backpack"].encumbrance_cn = 1  # type: ignore[misc]


# --- Price-form validation and coverage ------------------------------------


def test_a_fixed_price_multiplies_by_the_count() -> None:
    assert FixedPrice(Coin.of(3, GP)).cost_of(4) == Coin.of(12, GP)
    assert FixedPrice(Coin.of(3, GP)).cost_of() == Coin.of(3, GP)


@pytest.mark.parametrize("bad", [0, -1])
def test_a_fixed_price_count_that_is_not_positive_is_refused(bad: int) -> None:
    with pytest.raises(ValueError, match="count must be positive"):
        FixedPrice(Coin(1)).cost_of(bad)


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_fixed_price_count_is_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="count must be an int"):
        FixedPrice(Coin(1)).cost_of(bad)


def test_a_fixed_price_unit_that_is_not_a_coin_is_refused() -> None:
    with pytest.raises(ValueError, match="unit must be a Coin"):
        FixedPrice(5)  # type: ignore[arg-type]


@pytest.mark.parametrize("bad", [0, -1])
def test_a_quantity_price_count_that_is_not_positive_is_refused(bad: int) -> None:
    with pytest.raises(ValueError, match="count must be positive"):
        TORCH.price.cost_of(bad)


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_quantity_price_count_is_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="count must be an int"):
        TORCH.price.cost_of(bad)


def test_a_quantity_price_needs_at_least_one_offer() -> None:
    with pytest.raises(ValueError, match="offers must not be empty"):
        QuantityPrice(offers=())


def test_a_quantity_price_may_not_repeat_a_count() -> None:
    with pytest.raises(ValueError, match="must not repeat a count"):
        QuantityPrice(
            offers=(PurchaseOffer(1, Coin(10)), PurchaseOffer(1, Coin(20))),
        )


@pytest.mark.parametrize("bad", [0, -1])
def test_a_purchase_offer_count_that_is_not_positive_is_refused(bad: int) -> None:
    with pytest.raises(ValueError, match="count must be positive"):
        PurchaseOffer(bad, Coin(10))


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_purchase_offer_count_is_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="count must be an int"):
        PurchaseOffer(bad, Coin(10))


def test_a_purchase_offer_price_that_is_not_a_coin_is_refused() -> None:
    with pytest.raises(ValueError, match="price must be a Coin"):
        PurchaseOffer(1, 10)  # type: ignore[arg-type]


def test_an_open_ended_minimum_that_is_not_a_coin_is_refused() -> None:
    with pytest.raises(ValueError, match="minimum must be a Coin"):
        OpenEndedPrice(50)  # type: ignore[arg-type]


def test_an_open_ended_price_resolved_with_a_non_coin_is_refused() -> None:
    with pytest.raises(ValueError, match="amount must be a Coin"):
        OpenEndedPrice(Coin(10)).resolve(20)  # type: ignore[arg-type]


def test_resolving_a_row_whose_price_rc_prints_is_refused() -> None:
    with pytest.raises(UnresolvedPriceError, match="no open-ended price to resolve"):
        resolve_price(ADVENTURING_GEAR["Rope"], Coin.of(5, GP))


def test_resolving_a_non_item_is_refused() -> None:
    with pytest.raises(ValueError, match="item must be an Item"):
        resolve_price("Clothes, extravagant", Coin.of(50, GP))  # type: ignore[arg-type]


def test_catalog_lookup_finds_rows_in_every_catalog() -> None:
    assert catalog_item("Mace") is WEAPONS["Mace"]
    assert catalog_item("Plate Mail") is ARMOR["Plate Mail"]
    assert catalog_item("Rope") is ADVENTURING_GEAR["Rope"]
