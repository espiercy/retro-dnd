"""Shared value types for the EXP-002 -> EXP-001 turn-credit interface.

This contract is owned by neither Rule Card individually — it is the
interface between docs/rules/exploration/dungeon_turn_time_accounting.md
(EXP-002, the producer) and
docs/rules/exploration/dungeon_wandering_monster_check.md (EXP-001, the
consumer). See docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md §6
("EXP-002 → EXP-001 Interface (Turn-Credit Contract)") for the approved
representation this module implements.

Deliberately not a generalized event type: no round-count, timestamp, or
activity data is attached (that remains EXP-002's internal concern, or
another card's concern entirely). No production module beyond EXP-002 and
EXP-001 needs to import this module.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class TurnCreditOrigin(Enum):
    """Whether a whole-turn credit arose from an ordinary Game-Turn-Checklist
    iteration or from a resolved encounter's round-mode resolution.

    A closed, two-value distinction (implementation plan §6). EXP-001's own
    mechanical contract requires distinguishing these two origins — only an
    ``ORDINARY`` credit can represent a step-4 wandering-monster-check
    opportunity (implementation plan §4.2, "Necessary Mechanical
    Consequence"); an ``ENCOUNTER_DERIVED`` credit can only ever advance
    cadence. No other origin exists.
    """

    ORDINARY = auto()
    ENCOUNTER_DERIVED = auto()


@dataclass(frozen=True, slots=True)
class TurnCredit:
    """One authoritative, ordered, whole-turn credit.

    Represents exactly one whole dungeon turn EXP-002 has produced — never
    a fraction of a turn, never more than one turn, and never any
    encounter, wandering-monster, RNG, or presentation data (implementation
    plan §5, §6).

    ``turn_number`` provides ordering/identity within one session's
    authoritative dungeon-turn accounting. A valid credit's ``turn_number``
    is a positive int (implementation plan §5/§6); a valid *sequence* of
    credits is additionally strictly increasing and gapless, but that
    sequence-level property is a producer invariant — EXP-002's own future
    counter (not yet implemented) — that a single, isolated ``TurnCredit``
    instance has no way to observe or enforce on its own (implementation
    plan §5: "an orchestration-level guarantee this type cannot
    self-enforce"). Only the per-instance positivity constraint is
    validated here.

    ``origin`` records whether the credit is ordinary or encounter-derived.
    """

    turn_number: int
    origin: TurnCreditOrigin

    def __post_init__(self) -> None:
        if (
            not isinstance(self.turn_number, int)
            or isinstance(self.turn_number, bool)
            or self.turn_number < 1
        ):
            raise ValueError(f"turn_number must be a positive int, got {self.turn_number!r}")
