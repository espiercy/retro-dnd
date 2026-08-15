"""Errors raised by the RNG/dice abstraction.

See docs/technical/RNG_CONTRACT.md §12 for the approved error-behavior
contract: invalid requests fail explicitly and are never silently coerced,
clamped, or defaulted.
"""

from __future__ import annotations


class DiceError(Exception):
    """Base class for all errors raised by the RNG/dice abstraction."""


class InvalidDiceExpressionError(DiceError):
    """A dice-expression string is malformed or uses unsupported notation.

    Covers, per RNG_CONTRACT.md §7 and §12: a non-string argument, a string
    that doesn't match the approved grammar (``dS`` / ``NdS`` / ``NdS+M`` /
    ``NdS-M``), a syntactically valid string with a non-positive dice count
    or die size (e.g. ``"0d6"``, ``"3d0"``), and any notation outside that
    grammar (mixed dice pools, multiple modifiers, exploding/keep-drop
    syntax, percentile shorthand, etc.).
    """


class InvalidDieSizeError(DiceError):
    """A single-die roll was requested with a non-positive or non-integer size."""


class RollSequenceExhaustedError(DiceError):
    """The scripted/deterministic RNG's queued values are exhausted.

    Per RNG_CONTRACT.md §9: the scripted RNG must fail explicitly rather
    than fall back to real randomness or silently repeat/wrap its queue.
    """
