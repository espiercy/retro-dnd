"""Tests for the shared currency primitive
(docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md §5.1/§6.1, Slice A).

Slice A owns the representation only. Starting-gold generation, catalogs,
purchasing, class legality and the Druid pricing *policy* are CHAR-004's
and arrive in Slices B and C; nothing here anticipates them. The exactness
these tests pin down is what those slices will depend on.
"""

import dataclasses
from typing import Any

import pytest

from rules.currency import IN_COPPER, Coin, Denomination

# --- Denomination representation -----------------------------------------


def test_denominations_are_the_five_rc_names() -> None:
    # RC Ch. 4 p. 62 names exactly these; no speculative denomination is
    # added (Slice A authorization §4).
    assert set(Denomination) == {
        Denomination.PLATINUM,
        Denomination.GOLD,
        Denomination.ELECTRUM,
        Denomination.SILVER,
        Denomination.COPPER,
    }
    assert len(Denomination) == 5


def test_conversion_table_matches_rc_exactly() -> None:
    # RC: 1 pp = 5 gp = 10 ep = 50 sp = 500 cp (Ch. 4 p. 62; CHAR-004 §4).
    assert IN_COPPER[Denomination.PLATINUM] == 500
    assert IN_COPPER[Denomination.GOLD] == 100
    assert IN_COPPER[Denomination.ELECTRUM] == 50
    assert IN_COPPER[Denomination.SILVER] == 10
    assert IN_COPPER[Denomination.COPPER] == 1


@pytest.mark.parametrize(
    ("denomination", "per_platinum"),
    [
        (Denomination.GOLD, 5),
        (Denomination.ELECTRUM, 10),
        (Denomination.SILVER, 50),
        (Denomination.COPPER, 500),
    ],
)
def test_every_denomination_reconciles_against_the_platinum_anchor(
    denomination: Denomination, per_platinum: int
) -> None:
    # The whole table derives from one RC statement, so each row must
    # reproduce it rather than merely look plausible.
    assert IN_COPPER[denomination] * per_platinum == IN_COPPER[Denomination.PLATINUM]


def test_conversion_table_is_not_mutable() -> None:
    with pytest.raises(TypeError):
        IN_COPPER[Denomination.GOLD] = 1  # type: ignore[index]


# --- Exact representation ------------------------------------------------


def test_whole_gp_is_exact() -> None:
    assert Coin.of(1, Denomination.GOLD).copper == 100
    assert Coin.of(30, Denomination.GOLD).copper == 3_000
    assert Coin.of(180, Denomination.GOLD).copper == 18_000


def test_four_and_a_half_gp_equals_forty_five_sp_equals_four_hundred_fifty_cp() -> None:
    # The exactness the Slice-A authorization names explicitly:
    #     4.5 gp = 45 sp = 450 cp
    # 4.5 gp is not constructible as a whole number of gold, which is the
    # point -- it is reached exactly through the smaller denominations and
    # through scaled().
    four_and_a_half_gp = Coin(450)
    assert Coin.of(45, Denomination.SILVER) == four_and_a_half_gp
    assert Coin.of(450, Denomination.COPPER) == four_and_a_half_gp
    assert four_and_a_half_gp.copper * 2 == Coin.of(9, Denomination.GOLD).copper


@pytest.mark.parametrize(
    ("amount", "denomination", "expected_copper"),
    [
        (1, Denomination.PLATINUM, 500),
        (1, Denomination.GOLD, 100),
        (1, Denomination.ELECTRUM, 50),
        (1, Denomination.SILVER, 10),
        (1, Denomination.COPPER, 1),
        (0, Denomination.GOLD, 0),
        (5, Denomination.SILVER, 50),
        (2, Denomination.SILVER, 20),
    ],
)
def test_of_converts_exactly(
    amount: int, denomination: Denomination, expected_copper: int
) -> None:
    assert Coin.of(amount, denomination).copper == expected_copper


def test_equal_values_built_from_different_denominations_are_equal() -> None:
    assert Coin.of(1, Denomination.GOLD) == Coin.of(10, Denomination.SILVER)
    assert Coin.of(1, Denomination.GOLD) == Coin.of(100, Denomination.COPPER)
    assert Coin.of(1, Denomination.PLATINUM) == Coin.of(5, Denomination.GOLD)
    assert Coin.of(1, Denomination.PLATINUM) == Coin.of(10, Denomination.ELECTRUM)


# --- No floating point enters the authoritative value --------------------


def test_stored_value_is_an_int_not_a_float() -> None:
    value = Coin.of(45, Denomination.SILVER).copper
    assert isinstance(value, int)
    assert not isinstance(value, float)


def test_a_float_amount_is_refused() -> None:
    # 4.5 gp must be reached exactly, never by handing a float to the
    # constructor (Slice A authorization §4: no float, no lossy decimal
    # conversion, no implicit rounding).
    with pytest.raises(ValueError, match="amount must be an int"):
        Coin.of(4.5, Denomination.GOLD)  # type: ignore[arg-type]


def test_a_float_copper_value_is_refused() -> None:
    with pytest.raises(ValueError, match="copper must be an int"):
        Coin(450.0)  # type: ignore[arg-type]


def test_scaling_never_produces_a_float() -> None:
    result = Coin.of(3, Denomination.GOLD).scaled(3, 2)
    assert isinstance(result.copper, int)
    assert not isinstance(result.copper, float)


# --- Exact arithmetic for the later +50% surcharge -----------------------


def test_three_gp_surcharged_by_fifty_percent_is_exactly_four_and_a_half_gp() -> None:
    # The arithmetic CHAR-004 §7's Druid rule will need in Slice C.
    # Slice A proves the representation supports it; it does NOT decide
    # which classes or items the surcharge applies to.
    club = Coin.of(3, Denomination.GOLD)
    assert club.scaled(3, 2) == Coin(450)


@pytest.mark.parametrize(
    ("amount", "denomination", "expected_copper"),
    [
        (3, Denomination.GOLD, 450),
        (5, Denomination.GOLD, 750),
        (1, Denomination.GOLD, 150),
        (5, Denomination.SILVER, 75),
        (1, Denomination.SILVER, 15),
        (2, Denomination.SILVER, 30),
    ],
)
def test_fifty_percent_surcharge_is_exact_for_catalog_shaped_prices(
    amount: int, denomination: Denomination, expected_copper: int
) -> None:
    # Every approved catalog price is a whole number of silver or gold,
    # hence an even number of copper, so scaled(3, 2) lands exactly.
    assert Coin.of(amount, denomination).scaled(3, 2).copper == expected_copper


def test_scaling_refuses_a_ratio_that_would_not_land_on_a_whole_copper() -> None:
    # RC names no unit below the copper piece. Rounding here would
    # substitute a value the source does not have.
    with pytest.raises(ValueError, match="will not round"):
        Coin(5).scaled(3, 2)


def test_scaling_by_one_is_identity() -> None:
    assert Coin(450).scaled(1, 1) == Coin(450)


def test_scaling_can_reduce_exactly() -> None:
    assert Coin.of(1, Denomination.GOLD).scaled(1, 2) == Coin(50)


def test_scaling_by_a_zero_denominator_is_refused() -> None:
    with pytest.raises(ValueError, match="denominator must not be zero"):
        Coin(100).scaled(1, 0)


def test_scaling_by_a_negative_ratio_is_refused() -> None:
    # Rejected by the non-negative invariant, not by a special case.
    with pytest.raises(ValueError, match="must not be negative"):
        Coin(100).scaled(-1, 2)


@pytest.mark.parametrize("bad", [True, False])
def test_scaling_refuses_bool_operands(bad: bool) -> None:
    with pytest.raises(ValueError, match="numerator must be an int"):
        Coin(100).scaled(bad, 2)
    with pytest.raises(ValueError, match="denominator must be an int"):
        Coin(100).scaled(3, bad)


# --- Arithmetic --------------------------------------------------------


def test_addition_is_exact() -> None:
    assert Coin.of(1, Denomination.GOLD) + Coin.of(5, Denomination.SILVER) == Coin(150)


def test_subtraction_is_exact() -> None:
    assert Coin.of(1, Denomination.GOLD) - Coin.of(5, Denomination.SILVER) == Coin(50)


def test_subtracting_to_exactly_zero_is_permitted() -> None:
    # CHAR-004 §5: a selection costing exactly the money held is valid,
    # and the remainder is zero.
    assert Coin(100) - Coin(100) == Coin(0)


def test_subtracting_past_zero_is_refused() -> None:
    # CHAR-004 §5 requires the affordability check before the deduction;
    # going negative means it was skipped. No debt is invented.
    with pytest.raises(ValueError, match="must not be negative"):
        Coin(100) - Coin(101)


def test_multiplication_by_a_count_is_exact() -> None:
    assert Coin.of(2, Denomination.SILVER) * 6 == Coin(120)


def test_multiplication_by_zero_yields_zero() -> None:
    assert Coin.of(5, Denomination.GOLD) * 0 == Coin(0)


def test_multiplication_by_a_negative_count_is_refused() -> None:
    with pytest.raises(ValueError, match="must not be negative"):
        Coin(100) * -1


@pytest.mark.parametrize("bad", [True, False])
def test_multiplication_refuses_a_bool_count(bad: bool) -> None:
    with pytest.raises(ValueError, match="count must be an int"):
        Coin(100) * bad


# --- Equality and ordering ------------------------------------------------


def test_ordering_is_exact_integer_ordering() -> None:
    assert Coin(99) < Coin(100)
    assert Coin(100) <= Coin(100)
    assert Coin(101) > Coin(100)
    assert Coin(100) >= Coin(100)


def test_ordering_supports_the_affordability_comparison() -> None:
    # The shape CHAR-004 §5 step 5 will use in Slice B: reject when the
    # cost exceeds the money held.
    money_held = Coin.of(30, Denomination.GOLD)
    affordable = Coin.of(29, Denomination.GOLD) + Coin.of(9, Denomination.SILVER)
    too_dear = Coin.of(30, Denomination.GOLD) + Coin.of(1, Denomination.COPPER)
    assert affordable <= money_held
    assert too_dear > money_held


def test_equality_ignores_how_the_value_was_built() -> None:
    assert Coin.of(1, Denomination.PLATINUM) == Coin(500)
    assert Coin.of(50, Denomination.SILVER) == Coin(500)


def test_values_are_hashable_and_deduplicate_by_worth() -> None:
    assert len({Coin(100), Coin.of(1, Denomination.GOLD), Coin.of(10, Denomination.SILVER)}) == 1


def test_sorting_is_deterministic() -> None:
    unsorted = [Coin(300), Coin(0), Coin(100), Coin(450)]
    assert sorted(unsorted) == [Coin(0), Coin(100), Coin(300), Coin(450)]


# --- Validation and immutability ------------------------------------------


def test_zero_is_representable() -> None:
    assert Coin(0).copper == 0


def test_a_negative_amount_is_refused() -> None:
    # RC states no negative price and no debt in any approved V1 rule.
    with pytest.raises(ValueError, match="must not be negative"):
        Coin(-1)


def test_a_negative_amount_via_of_is_refused() -> None:
    with pytest.raises(ValueError, match="must not be negative"):
        Coin.of(-1, Denomination.GOLD)


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_copper_value_is_refused(bad: bool) -> None:
    # bool is a subtype of int, so static typing alone permits Coin(True)
    # and it would read as one copper piece.
    with pytest.raises(ValueError, match="copper must be an int"):
        Coin(bad)


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_amount_is_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="amount must be an int"):
        Coin.of(bad, Denomination.GOLD)


@pytest.mark.parametrize("bad", ["100", None, [1]])
def test_a_non_int_copper_value_is_refused(bad: Any) -> None:
    with pytest.raises(ValueError, match="copper must be an int"):
        Coin(bad)


def test_values_are_immutable() -> None:
    coin = Coin(100)
    with pytest.raises(dataclasses.FrozenInstanceError):
        coin.copper = 200  # type: ignore[misc]


def test_values_carry_no_extra_state() -> None:
    # slots=True: no instance dict, so no caller can attach ownership,
    # provenance or campaign state to a bare monetary value. Asserted on the
    # instance rather than by attempting an assignment, because a frozen
    # slots dataclass refuses an unknown attribute name from inside its
    # generated __setattr__ with TypeError rather than AttributeError, which
    # would make the test assert a CPython detail instead of the invariant.
    assert not hasattr(Coin(100), "__dict__")
    assert Coin.__slots__ == ("copper",)


# --- Ownership boundary (Slice A owns representation only) ----------------


def test_module_exposes_no_price_catalog_or_purchasing_behaviour() -> None:
    # Guard: Slice A must not pre-build Slice B/C behaviour
    # (authorization §5, §7; implementation plan §4.3).
    import rules.currency as currency

    public = {name for name in vars(currency) if not name.startswith("_")}
    forbidden = {
        "starting_gold",
        "WEAPONS",
        "ARMOR",
        "ADVENTURING_GEAR",
        "AMMUNITION",
        "Item",
        "purchase_cost",
        "is_legal",
        "DRUID_SURCHARGE",
        "encumbrance",
        "movement_rate",
    }
    assert public & forbidden == set()
