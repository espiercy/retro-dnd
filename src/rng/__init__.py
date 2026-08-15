"""Simulation-owned RNG / dice abstraction.

Public contract per docs/technical/RNG_CONTRACT.md and
docs/decisions/DEC-0002-rng-contract.md. All simulation randomness must
flow through this module (ARCHITECTURE.md §5); rules procedures must never
call an uncontrolled random facility directly.
"""

from rng.errors import (
    DiceError,
    InvalidDiceExpressionError,
    InvalidDieSizeError,
    RollSequenceExhaustedError,
)
from rng.expressions import parse_dice_expression
from rng.results import RollResult
from rng.rng import RNG, ScriptedRNG, SeededRNG

__all__ = [
    "RNG",
    "DiceError",
    "InvalidDiceExpressionError",
    "InvalidDieSizeError",
    "RollSequenceExhaustedError",
    "RollResult",
    "ScriptedRNG",
    "SeededRNG",
    "parse_dice_expression",
]
