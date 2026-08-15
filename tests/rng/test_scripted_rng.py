"""Tests for ScriptedRNG, the deterministic test double (RNG_CONTRACT.md §9)."""

import pytest

from rng import (
    InvalidDiceExpressionError,
    InvalidDieSizeError,
    InvalidScriptedValueError,
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
    # The 4th value (3) only needs to be *some* valid d6 result -- its
    # specific value is incidental to what this test checks.
    rng = ScriptedRNG([4, 2, 5, 3])
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
    rng = ScriptedRNG([4])
    with pytest.raises(InvalidDieSizeError):
        rng.roll_die(0)

    result = rng.roll_die(6)
    assert result.dice == (4,)  # the queued value wasn't consumed by the failed call
    assert result.sequence_number == 1


# --- Scripted die-value validation (post-merge defect fix, see ISSUE-002) ---
#
# The production RNG can never return a value outside [1, sides] for a
# given die. A scripted RNG must not be able to either -- it may force
# *which* valid result occurs, but not manufacture a result the
# corresponding production die could never produce (RNG_CONTRACT.md §9).


@pytest.mark.parametrize("value", [1, 6])
def test_accepts_values_at_the_valid_boundary(value: int) -> None:
    rng = ScriptedRNG([value])
    result = rng.roll_die(6)
    assert result.dice == (value,)


@pytest.mark.parametrize("value", [0, -1, 7, 9])
def test_rejects_out_of_range_values_for_the_requested_die(value: int) -> None:
    rng = ScriptedRNG([value])
    with pytest.raises(InvalidScriptedValueError):
        rng.roll_die(6)


def test_rejects_bool_true_even_though_bool_is_an_int_subtype() -> None:
    # bool is a subtype of int, so `ScriptedRNG([True])` is statically
    # well-typed -- no `type: ignore` needed here, unlike the cases below.
    # True == 1 numerically, but a scripted "True" is not a meaningful
    # die result; the rejection is a deliberate runtime-only distinction,
    # mirroring roll_die's own bool rejection.
    rng = ScriptedRNG([True])
    with pytest.raises(InvalidScriptedValueError):
        rng.roll_die(6)


def test_rejects_bool_false() -> None:
    rng = ScriptedRNG([False])
    with pytest.raises(InvalidScriptedValueError):
        rng.roll_die(6)


def test_rejects_non_integer_numeric_value() -> None:
    rng = ScriptedRNG([1.5])  # type: ignore[list-item]
    with pytest.raises(InvalidScriptedValueError):
        rng.roll_die(6)


def test_rejects_string_value() -> None:
    rng = ScriptedRNG(["4"])  # type: ignore[list-item]
    with pytest.raises(InvalidScriptedValueError):
        rng.roll_die(6)


def test_rejects_none_value() -> None:
    rng = ScriptedRNG([None])  # type: ignore[list-item]
    with pytest.raises(InvalidScriptedValueError):
        rng.roll_die(6)


def test_invalid_constituent_value_fails_multi_die_operation() -> None:
    # 3d6 with a scripted [4, 9, 5] -- the middle value is impossible for
    # a d6. The operation must fail rather than produce a RollResult
    # containing an impossible die value.
    rng = ScriptedRNG([4, 9, 5])
    with pytest.raises(InvalidScriptedValueError):
        rng.roll("3d6")


def test_invalid_value_is_left_queued_not_consumed() -> None:
    # Chosen behavior (documented in the ISSUE-002 completion record): an
    # invalid value is a malformed test fixture, not a completed roll, so
    # it is left at the front of the queue rather than discarded -- the
    # same call raises the identical error again rather than silently
    # advancing to whatever's queued after it or reporting exhaustion.
    rng = ScriptedRNG([9])
    with pytest.raises(InvalidScriptedValueError):
        rng.roll_die(6)
    with pytest.raises(InvalidScriptedValueError):
        rng.roll_die(6)


def test_failed_single_die_call_does_not_advance_sequence_number() -> None:
    rng = ScriptedRNG([9])
    with pytest.raises(InvalidScriptedValueError):
        rng.roll_die(6)
    # No RollResult was produced, so no sequence number was ever assigned.
    assert rng._sequence_number == 0  # verifying an internal invariant, see comment above


def test_failed_multi_die_call_does_not_advance_sequence_number() -> None:
    rng = ScriptedRNG([4, 9, 5])
    with pytest.raises(InvalidScriptedValueError):
        rng.roll("3d6")
    assert rng._sequence_number == 0  # verifying an internal invariant, see comment above


def test_multi_die_failure_consumes_valid_values_before_the_invalid_one() -> None:
    # The first die (4) was validly drawn -- and so genuinely consumed
    # from the stream -- before hitting the impossible "9" as the second
    # die. Per the documented design, already-consumed raw draws are not
    # rolled back; only the operation-level result fails to materialize.
    # The invalid "9" itself remains queued (see the test above).
    rng = ScriptedRNG([4, 9, 5])
    with pytest.raises(InvalidScriptedValueError):
        rng.roll("3d6")

    assert list(rng._queue) == [9, 5]  # "4" was consumed; "9" was not
