"""Parsing for the approved dice-expression grammar.

See docs/technical/RNG_CONTRACT.md §7. Supported notation:

    dS
    NdS
    NdS+M
    NdS-M

This module contains pure parsing logic only — no randomness. It is used
identically by every RNG implementation (RNG_CONTRACT.md §4), so the
expression grammar cannot drift between implementations.

Deliberately not supported (RNG_CONTRACT.md §7) — all raise
InvalidDiceExpressionError rather than silently degrading: mixed-size dice
pools, exploding dice, keep/drop syntax, multiple modifiers, and percentile
shorthand beyond explicit ``1d100``.
"""

from __future__ import annotations

import re

from rng.errors import InvalidDiceExpressionError

_DICE_EXPRESSION_PATTERN = re.compile(r"^(\d*)d(\d+)([+-]\d+)?$")


def parse_dice_expression(expression: str) -> tuple[int, int, int]:
    """Parse a dice expression into ``(count, sides, modifier)``.

    Raises ``InvalidDiceExpressionError`` for anything outside the approved
    grammar: a non-string argument, a string that doesn't match the
    grammar at all, or a syntactically valid string with a non-positive
    dice count or die size.

    No whitespace tolerance and no case-insensitivity are provided —
    notation must match exactly (e.g. ``"3d6"``, not ``"3d6 "`` or
    ``"3D6"``), per the contract's preference for explicit behavior over
    lenient/clever parsing.
    """
    if not isinstance(expression, str):
        raise InvalidDiceExpressionError(
            f"dice expression must be a string, got {type(expression).__name__!r}"
        )

    match = _DICE_EXPRESSION_PATTERN.fullmatch(expression)
    if match is None:
        raise InvalidDiceExpressionError(f"not a valid dice expression: {expression!r}")

    count_text, sides_text, modifier_text = match.groups()
    count = int(count_text) if count_text else 1
    sides = int(sides_text)
    modifier = int(modifier_text) if modifier_text else 0

    if count < 1:
        raise InvalidDiceExpressionError(
            f"dice expression must specify at least one die, got {expression!r}"
        )
    if sides < 1:
        raise InvalidDiceExpressionError(f"die size must be a positive integer, got {expression!r}")

    return count, sides, modifier
