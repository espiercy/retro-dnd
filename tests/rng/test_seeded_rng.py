"""Tests for SeededRNG (RNG_CONTRACT.md §9).

Each test builds its own reference `random.Random(seed)` and draws from it
directly to compute the expected result, then asserts SeededRNG produces
exactly the same values. This verifies both the mapping from seed to result
and, precisely, how many raw draws each call consumes from the shared
stream — without hard-coding magic numbers that would obscure what's being
tested (TESTING_STRATEGY.md §3).
"""

import random

import pytest

from rng import InvalidDiceExpressionError, InvalidDieSizeError, SeededRNG


def test_same_seed_and_sequence_reproduce_results() -> None:
    seed = 12345
    reference = random.Random(seed)
    expected_die = reference.randint(1, 6)

    rng = SeededRNG(seed)
    result = rng.roll_die(6)

    assert result.dice == (expected_die,)
    assert result.total == expected_die
    assert result.die_size == 6
    assert result.modifier == 0
    assert result.expression == "1d6"
    assert result.sequence_number == 1


def test_repeated_construction_with_same_seed_reproduces_full_sequence() -> None:
    seed = 777
    first = SeededRNG(seed)
    second = SeededRNG(seed)

    for _ in range(5):
        assert first.roll_die(20) == second.roll_die(20)


def test_expression_roll_consumes_one_draw_per_die() -> None:
    seed = 999
    reference = random.Random(seed)
    expected_dice = tuple(reference.randint(1, 6) for _ in range(3))

    rng = SeededRNG(seed)
    result = rng.roll("3d6")

    assert result.dice == expected_dice
    assert result.total == sum(expected_dice)


def test_multi_die_expression_receives_one_sequence_number_not_one_per_die() -> None:
    # This is the DEC-0002 refinement: a 3d6 call consumes three raw draws
    # from the stream (verified below) but is one rules-visible operation.
    seed = 999
    reference = random.Random(seed)
    expected_three_d_six = tuple(reference.randint(1, 6) for _ in range(3))
    expected_next_die = reference.randint(1, 8)

    rng = SeededRNG(seed)
    three_d_six = rng.roll("3d6")
    next_die = rng.roll_die(8)

    assert three_d_six.dice == expected_three_d_six
    assert three_d_six.sequence_number == 1
    # If 3d6 had minted one sequence number per die, this would be 4, not 2.
    assert next_die.sequence_number == 2
    assert next_die.dice == (expected_next_die,)


def test_sequence_numbers_increment_across_mixed_calls() -> None:
    rng = SeededRNG(seed=1)
    assert rng.roll_die(6).sequence_number == 1
    assert rng.roll("2d6+1").sequence_number == 2
    assert rng.roll_die(20).sequence_number == 3
    assert rng.roll("1d6-1").sequence_number == 4


def test_expression_with_positive_modifier_matches_worked_example() -> None:
    seed = 7
    reference = random.Random(seed)
    expected_dice = tuple(reference.randint(1, 20) for _ in range(2))

    rng = SeededRNG(seed)
    result = rng.roll("2d20+3")

    assert result.dice == expected_dice
    assert result.modifier == 3
    assert result.total == sum(expected_dice) + 3


def test_d_shorthand_matches_1d_form_for_same_stream_position() -> None:
    seed = 55
    reference = random.Random(seed)
    expected = reference.randint(1, 6)

    rng = SeededRNG(seed)
    result = rng.roll("d6")

    assert result.dice == (expected,)
    assert result.expression == "d6"  # preserves the exact requested notation
    assert result.die_size == 6


@pytest.mark.parametrize("sides", [0, -1, -6])
def test_roll_die_rejects_non_positive_size(sides: int) -> None:
    rng = SeededRNG(seed=1)
    with pytest.raises(InvalidDieSizeError):
        rng.roll_die(sides)


def test_roll_die_rejects_bool_size() -> None:
    # bool is a subtype of int, so this is statically well-typed — the
    # rejection is a deliberate runtime distinction (RNG_CONTRACT.md §12:
    # explicit failure over silent coercion), not a type error.
    rng = SeededRNG(seed=1)
    with pytest.raises(InvalidDieSizeError):
        rng.roll_die(True)


def test_roll_die_rejects_non_int_size() -> None:
    rng = SeededRNG(seed=1)
    with pytest.raises(InvalidDieSizeError):
        rng.roll_die("6")  # type: ignore[arg-type]


def test_roll_rejects_malformed_expression() -> None:
    rng = SeededRNG(seed=1)
    with pytest.raises(InvalidDiceExpressionError):
        rng.roll("not-a-dice-expression")


def test_rejected_roll_die_call_does_not_consume_stream_or_sequence_number() -> None:
    seed = 3
    rng = SeededRNG(seed)
    with pytest.raises(InvalidDieSizeError):
        rng.roll_die(0)

    reference = random.Random(seed)
    expected = reference.randint(1, 6)
    result = rng.roll_die(6)

    assert result.dice == (expected,)  # stream wasn't advanced by the failed call
    assert result.sequence_number == 1  # the failed call didn't consume a sequence number


def test_rejected_roll_expression_does_not_consume_stream_or_sequence_number() -> None:
    seed = 3
    rng = SeededRNG(seed)
    with pytest.raises(InvalidDiceExpressionError):
        rng.roll("bad")

    reference = random.Random(seed)
    expected = reference.randint(1, 6)
    result = rng.roll_die(6)

    assert result.dice == (expected,)
    assert result.sequence_number == 1
