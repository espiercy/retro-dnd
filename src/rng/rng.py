"""The RNG abstraction: two public rules-facing operations built on one
private raw-draw primitive.

See docs/technical/RNG_CONTRACT.md, particularly §4 (Public Contract),
§6 (Sequence-Number Semantics), §8 (Consumption Semantics), and §9
(Deterministic Testing).
"""

from __future__ import annotations

import random
from collections import deque
from collections.abc import Sequence
from typing import Protocol

from rng.errors import (
    InvalidDieSizeError,
    InvalidScriptedValueError,
    RollSequenceExhaustedError,
)
from rng.expressions import parse_dice_expression
from rng.results import RollResult


class RNG(Protocol):  # pragma: no cover — structural typing only; stub bodies never execute
    """The rules-facing RNG contract. Both SeededRNG and ScriptedRNG satisfy this.

    Rules procedures should depend on this contract, not on a concrete
    implementation, so either implementation can be substituted in tests
    (RNG_CONTRACT.md §4).
    """

    def roll_die(self, sides: int) -> RollResult:
        """Roll one die of the given size."""
        ...

    def roll(self, expression: str) -> RollResult:
        """Roll the dice described by a dice expression (RNG_CONTRACT.md §7)."""
        ...


class _BaseRNG:
    """Shared parsing/sequencing logic for every RNG implementation.

    Subclasses supply randomness only via ``_raw_draw`` — the single point
    of contact with actual randomness (RNG_CONTRACT.md §4). Dice-expression
    aggregation and sequence-number assignment are implemented once here so
    they cannot drift between implementations, and so a multi-die
    expression receives exactly one sequence number rather than one per
    die (RNG_CONTRACT.md §6).

    Validation (invalid die size / invalid expression) always happens
    before any raw draw or sequence-number assignment, so a rejected call
    never perturbs the RNG stream or the rules-visible roll history.
    """

    def __init__(self) -> None:
        self._sequence_number = 0

    def _raw_draw(self, sides: int) -> int:
        raise NotImplementedError

    def _next_sequence_number(self) -> int:
        self._sequence_number += 1
        return self._sequence_number

    def roll_die(self, sides: int) -> RollResult:
        if not isinstance(sides, int) or isinstance(sides, bool) or sides < 1:
            raise InvalidDieSizeError(f"die size must be a positive integer, got {sides!r}")
        value = self._raw_draw(sides)
        return RollResult(
            expression=f"1d{sides}",
            dice=(value,),
            die_size=sides,
            modifier=0,
            sequence_number=self._next_sequence_number(),
        )

    def roll(self, expression: str) -> RollResult:
        count, sides, modifier = parse_dice_expression(expression)
        # Every raw draw for this call goes through _raw_draw directly,
        # never through roll_die — a multi-die operation receives exactly
        # one sequence number, not one per die (RNG_CONTRACT.md §6).
        dice = tuple(self._raw_draw(sides) for _ in range(count))
        return RollResult(
            expression=expression,
            dice=dice,
            die_size=sides,
            modifier=modifier,
            sequence_number=self._next_sequence_number(),
        )


class SeededRNG(_BaseRNG):
    """The production RNG: deterministic given a seed and call sequence.

    Wraps a single ``random.Random`` instance. That generator is chosen
    specifically because its internal state is introspectable/serializable
    (``getstate``/``setstate``), keeping a future persistence
    implementation achievable (RNG_CONTRACT.md §13) without redesigning
    this boundary.

    Reproducibility is guaranteed for the same supported Python/toolchain
    version, seed, and call sequence (RNG_CONTRACT.md §9) — not promised
    indefinitely across arbitrary future Python versions.
    """

    def __init__(self, seed: int) -> None:
        super().__init__()
        self._random = random.Random(seed)

    def _raw_draw(self, sides: int) -> int:
        return self._random.randint(1, sides)


class ScriptedRNG(_BaseRNG):
    """The deterministic test double: returns a pre-supplied queue of raw values.

    Exercises the same real parsing/aggregation logic as SeededRNG
    (RNG_CONTRACT.md §9) — only the source of individual die values
    differs. A scripted sequence of ``[4, 2, 5]`` used for ``"3d6"`` still
    constructs its total via real summation, never a pre-baked total.

    Raises ``RollSequenceExhaustedError`` when the queue runs out, rather
    than falling back to real randomness or silently repeating/wrapping
    the queue.

    Each queued value is validated against the specific die it is drawn
    for — a value is only accepted if it is an ``int`` (excluding
    ``bool``, which is a subtype of ``int`` but not a valid die result)
    and lies within ``[1, sides]``. This can only be checked at draw time,
    not at construction time, since the same instance may be asked for
    different die sizes across its lifetime. A scripted RNG may force any
    result the corresponding production die could produce; it must not be
    able to manufacture one the production die never could
    (``InvalidScriptedValueError``).

    An invalid value is treated as a malformed test fixture, not a
    completed roll: it is left in the queue rather than consumed (the
    same "check before consume" shape already used for exhaustion above),
    and the failure occurs before any sequence number is assigned, so a
    rejected call never advances the rules-visible roll history any more
    than a rejected ``roll_die``/``roll`` call does (see ``_BaseRNG``).
    Raw values already drawn earlier in the *same* multi-die operation are
    not rolled back — only the operation-level result fails to
    materialize, consistent with the project's general rule that raw
    stream consumption, once it has happened, is not undone.
    """

    def __init__(self, values: Sequence[int]) -> None:
        super().__init__()
        self._queue: deque[int] = deque(values)

    def _raw_draw(self, sides: int) -> int:
        if not self._queue:
            raise RollSequenceExhaustedError(
                "scripted RNG's controlled sequence is exhausted; "
                "supply more values or shorten the test scenario"
            )
        value = self._queue[0]
        if not isinstance(value, int) or isinstance(value, bool) or not (1 <= value <= sides):
            raise InvalidScriptedValueError(
                f"scripted value {value!r} is not a possible result for a "
                f"{sides}-sided die; scripted values must be an int in [1, {sides}]"
            )
        self._queue.popleft()
        return value
