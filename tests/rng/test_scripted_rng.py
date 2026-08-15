"""Tests for ScriptedRNG, the deterministic test double (RNG_CONTRACT.md §9)."""

import pytest

from rng import (
    InvalidDiceExpressionError,
    InvalidDieSizeError,
    RollSequenceExhaustedError,
    ScriptedRNG,
)


def test_returns_queued_values_in_order() -> None:
    rng = ScriptedRNG([6, 2, 4, 1])
    assert rng.roll_die(6).dice == (6,)
    assert rng.roll_die(6).dice == (2,)
    assert rng.roll_die(6).dice == (4,)
    assert rng.roll_die(6).dice == (1,)


def test_exercises_real_aggregation_for_expression_not_a_canned_total() -> None:
    # A scripted [4, 2, 5] used for "3d6" must construct total=11 via real
    # summation, never simply return a pre-baked total.
    rng = ScriptedRNG([4, 2, 5])
    result = rng.roll("3d6")

    assert result.dice == (4, 2, 5)
    assert result.total == 11


def test_applies_modifier_on_top_of_scripted_values() -> None:
    # Matches RNG_CONTRACT.md's own worked example: 2d6+1 → [2,6] + 1 = 9.
    rng = ScriptedRNG([2, 6])
    result = rng.roll("2d6+1")

    assert result.total == 9


def test_raises_when_exhausted() -> None:
    rng = ScriptedRNG([1])
    rng.roll_die(6)
    with pytest.raises(RollSequenceExhaustedError):
        rng.roll_die(6)


def test_raises_on_partial_exhaustion_mid_expression() -> None:
    rng = ScriptedRNG([1, 2])  # 3d6 needs three values, only two are queued
    with pytest.raises(RollSequenceExhaustedError):
        rng.roll("3d6")


def test_never_falls_back_to_real_randomness_when_exhausted() -> None:
    rng = ScriptedRNG([])
    with pytest.raises(RollSequenceExhaustedError):
        rng.roll_die(6)
    # Still exhausted on a second attempt — no silent repeat/wrap of the queue.
    with pytest.raises(RollSequenceExhaustedError):
        rng.roll_die(6)


def test_sequence_numbers_follow_the_same_semantics_as_seeded_rng() -> None:
    rng = ScriptedRNG([4, 2, 5, 9])
    first = rng.roll("3d6")
    second = rng.roll_die(6)

    assert first.sequence_number == 1
    assert second.sequence_number == 2  # not 4 — one number per operation, not per die


def test_rejects_invalid_die_size() -> None:
    rng = ScriptedRNG([1])
    with pytest.raises(InvalidDieSizeError):
        rng.roll_die(0)


def test_rejects_invalid_expression() -> None:
    rng = ScriptedRNG([1])
    with pytest.raises(InvalidDiceExpressionError):
        rng.roll("bad")


def test_rejected_call_does_not_consume_queue_or_sequence_number() -> None:
    rng = ScriptedRNG([9])
    with pytest.raises(InvalidDieSizeError):
        rng.roll_die(0)

    result = rng.roll_die(6)
    assert result.dice == (9,)  # the queued value wasn't consumed by the failed call
    assert result.sequence_number == 1
