"""Tests for the EXP-002 -> EXP-001 turn-credit contract
(docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md §5/§6).
"""

import dataclasses

import pytest

from rules.exploration.turn_credit import TurnCredit, TurnCreditOrigin

# --- Origin representation ---------------------------------------------


def test_ordinary_origin_exists() -> None:
    assert TurnCreditOrigin.ORDINARY is TurnCreditOrigin.ORDINARY


def test_encounter_derived_origin_exists() -> None:
    assert TurnCreditOrigin.ENCOUNTER_DERIVED is TurnCreditOrigin.ENCOUNTER_DERIVED


def test_origin_is_a_closed_two_value_set() -> None:
    # No unintended additional origin values (implementation plan §4:
    # "a closed two-value enumeration").
    assert set(TurnCreditOrigin) == {TurnCreditOrigin.ORDINARY, TurnCreditOrigin.ENCOUNTER_DERIVED}
    assert len(TurnCreditOrigin) == 2


# --- Construction --------------------------------------------------------


def test_ordinary_credit_is_representable() -> None:
    credit = TurnCredit(turn_number=1, origin=TurnCreditOrigin.ORDINARY)
    assert credit.turn_number == 1
    assert credit.origin is TurnCreditOrigin.ORDINARY


def test_encounter_derived_credit_is_representable() -> None:
    credit = TurnCredit(turn_number=42, origin=TurnCreditOrigin.ENCOUNTER_DERIVED)
    assert credit.turn_number == 42
    assert credit.origin is TurnCreditOrigin.ENCOUNTER_DERIVED


# --- Immutability ----------------------------------------------------------


def test_turn_number_cannot_be_mutated() -> None:
    credit = TurnCredit(turn_number=1, origin=TurnCreditOrigin.ORDINARY)
    with pytest.raises(dataclasses.FrozenInstanceError):
        credit.turn_number = 2  # type: ignore[misc]


def test_origin_cannot_be_mutated() -> None:
    credit = TurnCredit(turn_number=1, origin=TurnCreditOrigin.ORDINARY)
    with pytest.raises(dataclasses.FrozenInstanceError):
        credit.origin = TurnCreditOrigin.ENCOUNTER_DERIVED  # type: ignore[misc]


# --- Value semantics (natural to a frozen dataclass; not invented) --------


def test_credits_with_identical_fields_compare_equal() -> None:
    a = TurnCredit(turn_number=5, origin=TurnCreditOrigin.ORDINARY)
    b = TurnCredit(turn_number=5, origin=TurnCreditOrigin.ORDINARY)
    assert a == b


def test_credits_with_different_turn_numbers_are_distinguishable() -> None:
    a = TurnCredit(turn_number=5, origin=TurnCreditOrigin.ORDINARY)
    b = TurnCredit(turn_number=6, origin=TurnCreditOrigin.ORDINARY)
    assert a != b


def test_credits_with_different_origins_are_distinguishable() -> None:
    a = TurnCredit(turn_number=5, origin=TurnCreditOrigin.ORDINARY)
    b = TurnCredit(turn_number=5, origin=TurnCreditOrigin.ENCOUNTER_DERIVED)
    assert a != b


# --- Validation (turn_number must be a positive int; plan §5/§6) ---------


def test_turn_number_one_is_the_smallest_valid_value() -> None:
    # Boundary: the smallest positive int must be accepted, not rejected.
    credit = TurnCredit(turn_number=1, origin=TurnCreditOrigin.ORDINARY)
    assert credit.turn_number == 1


def test_turn_number_zero_is_rejected() -> None:
    with pytest.raises(ValueError, match="positive int"):
        TurnCredit(turn_number=0, origin=TurnCreditOrigin.ORDINARY)


def test_turn_number_negative_is_rejected() -> None:
    with pytest.raises(ValueError, match="positive int"):
        TurnCredit(turn_number=-1, origin=TurnCreditOrigin.ORDINARY)


def test_turn_number_non_int_is_rejected() -> None:
    with pytest.raises(ValueError, match="positive int"):
        TurnCredit(turn_number="1", origin=TurnCreditOrigin.ORDINARY)  # type: ignore[arg-type]


def test_turn_number_bool_is_rejected() -> None:
    # bool is a subtype of int in Python but is not a valid turn number —
    # the same exclusion this codebase already applies to RNG die-size and
    # scripted-value validation (src/rng/rng.py).
    with pytest.raises(ValueError, match="positive int"):
        # No type: ignore needed here: bool is statically a subtype of int
        # (mypy accepts `True` where `int` is expected), which is exactly
        # why this runtime check exists — mypy strict cannot catch this
        # case, so TurnCredit.__post_init__ must.
        TurnCredit(turn_number=True, origin=TurnCreditOrigin.ORDINARY)
