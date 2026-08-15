"""Both RNG implementations must satisfy the identical rules-facing
contract (RNG_CONTRACT.md §4, §9) — this file exercises that parity
directly, rather than assuming it from shared inheritance.
"""

from collections.abc import Callable

import pytest

from rng import (
    RNG,
    InvalidDiceExpressionError,
    InvalidDieSizeError,
    ScriptedRNG,
    SeededRNG,
)

_IMPLEMENTATIONS: list[Callable[[], RNG]] = [
    lambda: SeededRNG(seed=1),
    lambda: ScriptedRNG([1, 2, 3, 4, 5, 6, 7, 8]),
]


@pytest.mark.parametrize("make_rng", _IMPLEMENTATIONS)
def test_both_implementations_reject_invalid_die_size(make_rng: Callable[[], RNG]) -> None:
    rng = make_rng()
    with pytest.raises(InvalidDieSizeError):
        rng.roll_die(0)


@pytest.mark.parametrize("make_rng", _IMPLEMENTATIONS)
def test_both_implementations_reject_invalid_expression(make_rng: Callable[[], RNG]) -> None:
    rng = make_rng()
    with pytest.raises(InvalidDiceExpressionError):
        rng.roll("nonsense")


@pytest.mark.parametrize("make_rng", _IMPLEMENTATIONS)
def test_both_implementations_number_sequences_starting_at_one(
    make_rng: Callable[[], RNG],
) -> None:
    rng = make_rng()
    assert rng.roll_die(6).sequence_number == 1
    assert rng.roll_die(6).sequence_number == 2


@pytest.mark.parametrize("make_rng", _IMPLEMENTATIONS)
def test_both_implementations_produce_dS_and_1dS_with_equal_dice_count(
    make_rng: Callable[[], RNG],
) -> None:
    rng = make_rng()
    assert len(rng.roll("d6").dice) == 1
