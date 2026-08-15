"""Tests for the dice-expression parser (RNG_CONTRACT.md §7).

Verifies the deterministic mapping from notation to (count, sides,
modifier) directly, per TESTING_STRATEGY.md §3 — not by sampling.
"""

import pytest

from rng import InvalidDiceExpressionError
from rng.expressions import parse_dice_expression


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("d6", (1, 6, 0)),
        ("1d6", (1, 6, 0)),
        ("1d20", (1, 20, 0)),
        ("2d6", (2, 6, 0)),
        ("3d6", (3, 6, 0)),
        ("3d6+1", (3, 6, 1)),
        ("1d6-1", (1, 6, -1)),
        ("2d20+3", (2, 20, 3)),
        ("d1", (1, 1, 0)),  # minimum valid die size
        ("100d6", (100, 6, 0)),  # no artificial upper bound on dice count
    ],
)
def test_parses_supported_notation(
    expression: str, expected: tuple[int, int, int]
) -> None:
    assert parse_dice_expression(expression) == expected


def test_d6_and_1d6_are_equivalent_counts() -> None:
    assert parse_dice_expression("d6")[0] == parse_dice_expression("1d6")[0] == 1


@pytest.mark.parametrize(
    "expression",
    [
        "",
        "abc",
        "6",
        "d",
        "0d6",  # zero dice
        "d0",  # zero-sided die
        "-1d6",  # negative dice count (not even grammar-matching)
        "3d-6",  # negative die size
        "3d6+1+2",  # multiple modifiers
        "2d6+1d4",  # mixed dice pool
        "D6",  # case-sensitive: uppercase D rejected
        "3d6 ",  # trailing whitespace rejected
        " 3d6",  # leading whitespace rejected
        "1d%",  # percentile shorthand not supported
        "2d6*2",  # unsupported operator
        "3d6++1",  # malformed modifier
    ],
)
def test_rejects_unsupported_notation(expression: str) -> None:
    with pytest.raises(InvalidDiceExpressionError):
        parse_dice_expression(expression)


def test_rejects_non_string_input() -> None:
    with pytest.raises(InvalidDiceExpressionError):
        parse_dice_expression(123)  # type: ignore[arg-type]


def test_rejects_none_input() -> None:
    with pytest.raises(InvalidDiceExpressionError):
        parse_dice_expression(None)  # type: ignore[arg-type]
