"""Tests for RollResult (RNG_CONTRACT.md §5)."""

import dataclasses

import pytest

from rng import RollResult


def test_total_is_sum_of_dice_plus_zero_modifier() -> None:
    result = RollResult(
        expression="3d6", dice=(4, 2, 5), die_size=6, modifier=0, sequence_number=1
    )
    assert result.total == 11


def test_total_applies_positive_modifier() -> None:
    # Matches RNG_CONTRACT.md's own worked example: 2d6+1 → [2,6] + 1 = 9.
    result = RollResult(
        expression="2d6+1", dice=(2, 6), die_size=6, modifier=1, sequence_number=1
    )
    assert result.total == 9


def test_total_applies_negative_modifier() -> None:
    result = RollResult(
        expression="1d6-1", dice=(3,), die_size=6, modifier=-1, sequence_number=1
    )
    assert result.total == 2


def test_dice_field_preserves_roll_order() -> None:
    result = RollResult(
        expression="3d6", dice=(6, 1, 3), die_size=6, modifier=0, sequence_number=1
    )
    assert result.dice == (6, 1, 3)


def test_result_is_immutable() -> None:
    result = RollResult(
        expression="1d6", dice=(4,), die_size=6, modifier=0, sequence_number=1
    )
    with pytest.raises(dataclasses.FrozenInstanceError):
        result.total = 99  # type: ignore[misc]
