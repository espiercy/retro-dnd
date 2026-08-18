"""EXP-002 — Dungeon Turn / Time Accounting.

See docs/rules/exploration/dungeon_turn_time_accounting.md (Status:
APPROVED) for the governing Rule Card, and
docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md §4.1/§8 for the
approved implementation contract this module implements (Step 2 of that
plan).

This module owns only authoritative whole-turn accounting: it maintains
one cumulative dungeon-turn count and produces a :class:`TurnCredit`
(src/rules/exploration/turn_credit.py) for each ordinary Game-Turn-
Checklist iteration or resolved encounter it is told has completed.

It does not, and must not:

- execute a Game Turn (that belongs to whatever future exploration-turn
  driver decides Actions/Results content — this module is only told
  "an ordinary iteration completed");
- execute or track combat rounds progressively (it is consulted only
  once round-mode resolution has *finished* and the final round count
  is known — Rule Card "Approved Mechanical Specification," "Turn-credit
  accounting");
- determine when an encounter starts or ends;
- know what activities occurred during a turn;
- know wandering-monster cadence (EXP-001's own concern — see the Rule
  Card's "Integration with EXP-001": "how EXP-001 interprets a given
  credit is entirely its own concern");
- perform RNG (Rule Card: "No RNG owned by this card");
- select encounters or monsters, or implement rest/movement/search/
  combat rules;
- maintain fractional time (Rule Card: "No fractional/rational ledger is
  maintained. Turn-credits are whole numbers only.").
"""

from __future__ import annotations

from rules.exploration.turn_credit import TurnCredit, TurnCreditOrigin

_ROUNDS_PER_TURN = 60
"""RC's structurally-confirmed 60-rounds-per-turn ratio (Rule Card
"Rules Cyclopedia Explicitly Establishes" item 2, Timetrack Table,
Ch. 13 p. 148)."""


def encounter_turn_cost(encounter_rounds: int) -> int:
    """The human-approved long-encounter Simulator Ruling, exactly:

        encounter_turn_cost = max(1, ceiling(encounter_rounds / 60))

    (Rule Card "Simulator Ruling," human-approved 2026-08-16.) For
    ``encounter_rounds`` in ``1..60`` this is always exactly ``1``,
    identical to RC's own explicit one-turn minimum (Rule Card
    "Rules Cyclopedia Explicitly Establishes" item 4); it only exceeds
    ``1`` for the RC-unspecified case of an encounter exceeding 60
    rounds. The result is deliberately a whole number of discrete
    procedural turn-blocks, never a fractional or continuous elapsed-time
    value — RC treats encounter time as an abstraction, not stopwatch
    arithmetic (Rule Card "Simulator Ruling," "Rationale").

    Computed with exact integer arithmetic (``ceiling(a / b) ==
    (a + b - 1) // b`` for positive integers) — no floating-point value
    is ever constructed, consistent with this card's "no fractional
    ledger" requirement applying to every intermediate value, not only
    the final result.

    This card's own contract does not define behavior for a
    non-positive, non-int, or otherwise malformed ``encounter_rounds``
    (its deterministic test obligations exercise only positive round
    counts); no such behavior is invented here.
    """
    return max(1, (encounter_rounds + _ROUNDS_PER_TURN - 1) // _ROUNDS_PER_TURN)


class DungeonTimeAccounting:
    """The authoritative, cumulative dungeon-turn counter (EXP-002).

    Owns exactly one non-negative integer count of whole dungeon turns
    credited so far this session. It never decreases and never resets
    for the lifetime of an instance (Rule Card: "Turn-credits are
    strictly ordered and cumulative across a session... with no reset
    and no gap"). A freshly constructed instance has credited zero turns
    — the first credit either method produces has ``turn_number == 1``.

    No credit history is stored beyond the running count: the Rule
    Card's individually-distinguishable/correctly-ordered requirement is
    satisfied by each returned :class:`TurnCredit`'s own ``turn_number``,
    not by this object retaining a log of every credit it has ever
    produced.
    """

    def __init__(self) -> None:
        self._turn_count = 0

    def complete_ordinary_turn(self) -> TurnCredit:
        """Record that one ordinary Game-Turn-Checklist iteration has
        already completed, and return the resulting whole-turn credit.

        Takes no activity, movement, search, rest, or RNG data — RC's own
        Game Turn Checklist treats an ordinary turn as a single atomic
        unit regardless of what filled it (Rule Card "Approved Mechanical
        Specification," "Preserve responsibility boundaries"). The fact
        that the turn completed is the only input this card needs.
        """
        self._turn_count += 1
        return TurnCredit(turn_number=self._turn_count, origin=TurnCreditOrigin.ORDINARY)

    def resolve_encounter(self, encounter_rounds: int) -> tuple[TurnCredit, ...]:
        """Record that an encounter has already resolved, having taken
        ``encounter_rounds`` actual rounds, and return the resulting
        whole-turn credit(s).

        This call means round-mode resolution has *finished* — this card
        produces no credit at all while an encounter is still in
        progress (Rule Card: "No dungeon-turn credit is produced during
        round-mode encounter resolution"). Exactly ``encounter_turn_cost
        (encounter_rounds)`` credits are produced, each with
        ``origin=TurnCreditOrigin.ENCOUNTER_DERIVED``, with strictly
        sequential and gapless ``turn_number`` values continuing this
        instance's own cumulative count — individually recoverable and
        ordered, never collapsed into one opaque multi-turn value (Rule
        Card: "those credits remain individually distinguishable and
        correctly ordered").
        """
        cost = encounter_turn_cost(encounter_rounds)
        credits = []
        for _ in range(cost):
            self._turn_count += 1
            credits.append(
                TurnCredit(turn_number=self._turn_count, origin=TurnCreditOrigin.ENCOUNTER_DERIVED)
            )
        return tuple(credits)
