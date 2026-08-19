"""EXP-001 — Dungeon (Underworld) Wandering-Monster Check.

See docs/rules/exploration/dungeon_wandering_monster_check.md (Status:
APPROVED) for the governing Rule Card, and
docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md §4.2/§8 for the
approved implementation contract this module implements (Step 3 of that
plan). Approved Simulator Rulings A, B, and C (human-approved 2026-08-18)
are implemented here exactly as approved, not reinterpreted.

This module owns only the wandering-monster cadence tally and pending-
arrival state. It does not, and must not:

- own an RNG stream (it consumes the one shared stream supplied by a
  caller, only when a check actually executes — Rule Card "RNG usage");
- own `EXP-002`'s turn-counting mechanics (it consumes `TurnCredit`
  values only — Rule Card "Dependencies": "does not depend on `EXP-002`'s
  internal accounting mechanics — only on the credit sequence itself");
- retain any turn/credit history;
- select a monster, resolve encounter distance, surprise, or reaction,
  or begin combat (Rule Card "Scope": "does not determine which monster,
  Number Appearing, direction, distance, surprise, reaction, morale,
  pursuit/evasion, combat, or treasure");
- decide the upstream heightened-checking or pre-decided-skip policy —
  both are externally supplied inputs this card only honors when given
  (Rule Card "Heightened-checking input," "DM-discretion skip input");
- perform any orchestration: it does not decide *when* a Game Turn
  begins, *when* an ordinary iteration completes, or enforce the calling
  order between `advance()` and `resolve_arrival()` — that is a
  sequencing contract this card requires of its caller, not something
  it defends against (Rule Card "Approved Mechanical Specification,"
  the `pending_arrival` invariant's "Scope").
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto

from rng import RNG, RollResult
from rules.exploration.turn_credit import TurnCredit, TurnCreditOrigin

_BASELINE_TRIGGER_THRESHOLD = 1
"""Baseline trigger: a result of exactly 1 on 1d6 (Rules Cyclopedia Explicit
item 2)."""

_MIN_HEIGHTENED_CHANCE_LEVEL = 1
_MAX_HEIGHTENED_CHANCE_LEVEL = 4
"""The only active heightened-chance levels the approved plan and Rule Card
authorize: 1-in-6, 2-in-6 (1-2), 3-in-6 (1-3), 4-in-6 (1-4) (Rules
Cyclopedia Explicit item 7, corrected reading). 5 or 6 is not an RC-
authorized mechanic."""

_WANDERING_CHECK_DIE_SIZE = 6
"""1d6 (Rules Cyclopedia Explicit item 2)."""


class CheckOutcome(Enum):
    """The mechanically meaningful outcomes of one `advance()` call
    (Rule Card "Approved Mechanical Specification," Procedure A).

    A closed, five-value set — no monster identity, direction, distance,
    surprise, reaction, combat state, or narrative/presentation string is
    ever represented here (Rule Card "Output").
    """

    CADENCE_ADVANCED_ONLY = auto()
    """An encounter-derived credit: the tally advanced, but no step-4
    check could execute (Necessary Mechanical Consequence)."""

    NOT_DUE = auto()
    """An ordinary credit that did not reach the due threshold."""

    SKIPPED = auto()
    """A due ordinary credit whose roll was skipped via the pre-decided
    "already decided for this period" signal (Rules Cyclopedia Explicit
    item 6)."""

    NO_TRIGGER = auto()
    """A due ordinary credit's check was performed and did not trigger."""

    TRIGGERED = auto()
    """A due ordinary credit's check was performed and triggered —
    `pending_arrival` is now set. This does not itself mean an encounter
    has begun (Rule Card "Trigger scheduling vs. arrival")."""


@dataclass(frozen=True, slots=True)
class WanderingCheckResult:
    """The result of one `advance()` call.

    `roll` carries the exact `RollResult` the approved RNG operation
    produced when a check actually executed (`CheckOutcome.NO_TRIGGER` or
    `CheckOutcome.TRIGGERED`); it is `None` for every outcome that
    performs no roll (`CADENCE_ADVANCED_ONLY`, `NOT_DUE`, `SKIPPED`) —
    Rule Card "RNG usage": "none when a check is not due or is skipped."
    """

    outcome: CheckOutcome
    roll: RollResult | None


@dataclass(frozen=True, slots=True)
class ArrivalResult:
    """The result of one `resolve_arrival()` call.

    Carries only the authoritative fact of arrival — no monster identity,
    direction, distance, surprise, or reaction data (Rule Card "Output":
    "a future encounter-resolution consumer... receives only the fact
    that an encounter has begun").
    """

    occurred: bool


def _validate_heightened_chance_level(level: int) -> None:
    """Rules Cyclopedia Explicit item 7's active heightened-chance range is
    exactly {1, 2, 3, 4} — never 5 or 6, which RC does not authorize.

    Called only when `heightened_checking` is active and the current
    credit's check will actually execute a roll (not skipped) — an
    inactive or unused level is never validated (implementation plan §6:
    "Do not reject an otherwise irrelevant supplied value merely to
    create defensive behavior").
    """
    if (
        not isinstance(level, int)
        or isinstance(level, bool)
        or not (_MIN_HEIGHTENED_CHANCE_LEVEL <= level <= _MAX_HEIGHTENED_CHANCE_LEVEL)
    ):
        raise ValueError(
            "heightened_chance_level must be an int in "
            f"{_MIN_HEIGHTENED_CHANCE_LEVEL}..{_MAX_HEIGHTENED_CHANCE_LEVEL} "
            f"when heightened_checking is active, got {level!r}"
        )


class WanderingMonsterCadence:
    """The authoritative wandering-monster-check cadence and pending-
    arrival state (EXP-001).

    Owns exactly two facts: the cadence tally (`turns_since_last_check`)
    and whether an arrival is pending (`pending_arrival`), both starting
    at their zero/false values (Rule Card "State this card maintains").
    No "check due" flag is separately persisted — due-ness is recomputed
    from the current tally and the current caller-supplied
    `heightened_checking` input each time it matters, per the Rule Card's
    own statement that this is "the smallest state adequate to Simulator
    Ruling B."
    """

    def __init__(self) -> None:
        self._turns_since_last_check = 0
        self._pending_arrival = False

    @property
    def turns_since_last_check(self) -> int:
        """Read-only view of the authoritative cadence tally."""
        return self._turns_since_last_check

    @property
    def pending_arrival(self) -> bool:
        """Read-only view of whether an arrival is pending resolution."""
        return self._pending_arrival

    def advance(
        self,
        credit: TurnCredit,
        *,
        rng: RNG,
        skip_signal: bool = False,
        heightened_checking: bool = False,
        heightened_chance_level: int = 1,
    ) -> WanderingCheckResult:
        """Procedure A — invoked once per completed whole-turn credit
        `EXP-002` produces, in the order produced.

        Every credit advances the tally uniformly, regardless of origin
        (Simulator Ruling A). Only an ordinary credit can represent an
        actually-executing step-4 checklist opportunity (Necessary
        Mechanical Consequence) — an encounter-derived credit returns
        `CADENCE_ADVANCED_ONLY` immediately, never evaluating due-ness,
        the skip signal, heightened checking, or RNG (Simulator Ruling B).
        """
        self._turns_since_last_check += 1

        if credit.origin is TurnCreditOrigin.ENCOUNTER_DERIVED:
            return WanderingCheckResult(outcome=CheckOutcome.CADENCE_ADVANCED_ONLY, roll=None)

        due = heightened_checking or self._turns_since_last_check >= 2
        if not due:
            return WanderingCheckResult(outcome=CheckOutcome.NOT_DUE, roll=None)

        # A due ordinary period has been identified. Validate an active,
        # actually-used heightened chance before consuming RNG or
        # consuming/resetting the due period. The authoritative credit's
        # unconditional cadence advance (above) has already occurred and
        # is preserved regardless of this validation's outcome — only
        # the due-period reset and any RNG consumption are guarded by it.
        will_execute = not skip_signal
        if heightened_checking and will_execute:
            _validate_heightened_chance_level(heightened_chance_level)

        # The due period is consumed whether the roll is performed or
        # skipped, and regardless of how many encounter-derived credits
        # contributed to crossing the threshold while the checklist was
        # suspended (Simulator Ruling B: exactly one roll resolves all of
        # it; no remainder is preserved).
        self._turns_since_last_check = 0

        if skip_signal:
            return WanderingCheckResult(outcome=CheckOutcome.SKIPPED, roll=None)

        roll = rng.roll_die(_WANDERING_CHECK_DIE_SIZE)
        trigger_threshold = (
            heightened_chance_level if heightened_checking else _BASELINE_TRIGGER_THRESHOLD
        )
        if roll.total <= trigger_threshold:
            self._pending_arrival = True
            return WanderingCheckResult(outcome=CheckOutcome.TRIGGERED, roll=roll)
        return WanderingCheckResult(outcome=CheckOutcome.NO_TRIGGER, roll=roll)

    def resolve_arrival(self) -> ArrivalResult:
        """Procedure B — invoked once at the beginning of each new Game
        Turn, before that turn's own Actions/Results/step-4 check occur.

        Represents "a new Game Turn is beginning," a distinct procedural
        fact from "a credit was completed" — it accepts no `TurnCredit`
        and no RNG, and consumes no RNG operation. The caller is
        responsible for treating `occurred=True` as preempting that Game
        Turn's own Actions/Results/step-4 procedure (Rules Cyclopedia
        Explicit item 4) — this card does not itself begin an encounter
        or any orchestration.
        """
        if self._pending_arrival:
            self._pending_arrival = False
            return ArrivalResult(occurred=True)
        return ArrivalResult(occurred=False)
