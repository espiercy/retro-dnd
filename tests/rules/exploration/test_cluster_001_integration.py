"""CLUSTER-001 Step 4 — direct cross-card integration tests.

Proves that EXP-002 (`DungeonTimeAccounting`) and EXP-001
(`WanderingMonsterCadence`) compose correctly under the approved
Game-Turn procedural sequencing
(docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md §7, §13), using the
real, already-`VERIFIED` production components -- never a stand-in or a
duplicated re-implementation of either card's algorithm.

This module is a deterministic procedural *test harness*, not a
production exploration driver. Every "Game Turn begins" moment is
represented by an explicit `resolve_arrival()` call, written out inline
in each scenario, so the required sequencing contract stays visible
rather than hidden behind an abstraction:

    BEGIN GAME TURN
        -> WanderingMonsterCadence.resolve_arrival()
        -> if arrival occurred: this Game Turn is preempted -- no
           ordinary credit is produced for it, and advance() is not
           called for it.
        -> otherwise: the externally-governed Game Turn occurs, then
           DungeonTimeAccounting.complete_ordinary_turn() produces one
           ORDINARY TurnCredit, which is passed to
           WanderingMonsterCadence.advance().

Encounter resolution is represented once the encounter has already
resolved, per the same approved contract:

    DungeonTimeAccounting.resolve_encounter(rounds)
        -> ordered ENCOUNTER_DERIVED TurnCredits
        -> each passed to WanderingMonsterCadence.advance() in order
        -> cadence advances; zero wandering checks execute from them

No `Player`/`Command`/`Dungeon`/`Party`/`ExplorationEngine`/`TurnManager`/
`DungeonTurnCycle`/`GameState`-shaped abstraction is introduced -- the
future human-playable exploration driver remains deliberately deferred
(implementation plan §11).

Every `ScriptedRNG` queue below is sized to *exactly* the number of
rolls the scenario's approved mechanics require. This is itself the RNG
audit this file performs: if either component consumed an unexpected
extra draw, a later intended draw would receive the wrong value, or the
queue would exhaust early (`RollSequenceExhaustedError`) -- either way
the scenario fails, without needing to introspect private RNG state.
"""

from __future__ import annotations

from rng import ScriptedRNG
from rules.exploration.dungeon_turn_time_accounting import DungeonTimeAccounting
from rules.exploration.dungeon_wandering_monster_check import (
    ArrivalResult,
    CheckOutcome,
    WanderingMonsterCadence,
)
from rules.exploration.turn_credit import TurnCredit, TurnCreditOrigin


def _fresh_pair() -> tuple[DungeonTimeAccounting, WanderingMonsterCadence]:
    """A freshly constructed, real producer/consumer pair -- no algorithm
    or sequencing logic lives here, only object construction."""
    return DungeonTimeAccounting(), WanderingMonsterCadence()


# --- Scenario 1: ordinary wandering trigger --------------------------------


def test_scenario_1_ordinary_wandering_trigger() -> None:
    accounting, cadence = _fresh_pair()
    rng = ScriptedRNG([1])  # exactly one due check this scenario ever performs

    # Game Turn 1 begins.
    arrival_1 = cadence.resolve_arrival()
    assert arrival_1 == ArrivalResult(occurred=False)
    credit_1 = accounting.complete_ordinary_turn()
    assert credit_1 == TurnCredit(turn_number=1, origin=TurnCreditOrigin.ORDINARY)
    result_1 = cadence.advance(credit_1, rng=rng)
    assert result_1.outcome is CheckOutcome.NOT_DUE

    # Game Turn 2 begins.
    arrival_2 = cadence.resolve_arrival()
    assert arrival_2 == ArrivalResult(occurred=False)
    credit_2 = accounting.complete_ordinary_turn()
    assert credit_2 == TurnCredit(turn_number=2, origin=TurnCreditOrigin.ORDINARY)
    result_2 = cadence.advance(credit_2, rng=rng)
    assert result_2.outcome is CheckOutcome.TRIGGERED
    assert result_2.roll is not None and result_2.roll.total == 1
    assert cadence.pending_arrival is True

    # Game Turn 3 begins: the pending arrival is resolved and preempts
    # this turn entirely.
    arrival_3 = cadence.resolve_arrival()
    assert arrival_3 == ArrivalResult(occurred=True)
    assert cadence.pending_arrival is False
    # Game Turn 3 is preempted: EXP-002 does NOT produce ordinary credit
    # #3 for it, and EXP-001.advance() is NOT called for it. Once
    # resolve_arrival() reports occurred=True, the Game Turn Checklist
    # has been left for encounter handling -- CLUSTER-001 does not own,
    # and this scenario does not assume, that downstream encounter's
    # resolution procedure. This scenario's approved responsibility ends
    # here: a wandering arrival itself produces no ordinary Game-Turn
    # credit, and the preempted Game Turn never reaches ordinary
    # completion. Any future ordinary-credit numbering depends on
    # whatever authoritative encounter accounting occurs before ordinary
    # exploration resumes, which is outside this scenario's scope.


# --- Scenario 2: ordinary no-trigger ----------------------------------------


def test_scenario_2_ordinary_no_trigger() -> None:
    accounting, cadence = _fresh_pair()
    rng = ScriptedRNG([4])  # exactly one due check this scenario ever performs

    arrival_1 = cadence.resolve_arrival()
    assert arrival_1.occurred is False
    credit_1 = accounting.complete_ordinary_turn()
    result_1 = cadence.advance(credit_1, rng=rng)
    assert result_1.outcome is CheckOutcome.NOT_DUE

    arrival_2 = cadence.resolve_arrival()
    assert arrival_2.occurred is False
    credit_2 = accounting.complete_ordinary_turn()
    result_2 = cadence.advance(credit_2, rng=rng)
    assert result_2.outcome is CheckOutcome.NO_TRIGGER
    assert result_2.roll is not None and result_2.roll.total == 4
    assert cadence.pending_arrival is False

    # The next Game Turn is not preempted (no pending arrival exists),
    # and ordinary progression continues normally.
    arrival_3 = cadence.resolve_arrival()
    assert arrival_3.occurred is False
    credit_3 = accounting.complete_ordinary_turn()
    result_3 = cadence.advance(credit_3, rng=rng)
    assert result_3.outcome is CheckOutcome.NOT_DUE

    # Exactly two credits (#1, #2) were relevant to the one due check
    # that occurred; credit #3 begins a fresh period.
    assert (credit_1.turn_number, credit_2.turn_number, credit_3.turn_number) == (1, 2, 3)


# --- Scenario 3: long encounter crosses cadence -----------------------------


def test_scenario_3_long_encounter_crosses_cadence() -> None:
    accounting, cadence = _fresh_pair()
    rng = ScriptedRNG([5])  # exactly one due check this scenario ever performs

    # Ordinary Game Turn: tally -> 1, not due.
    arrival_1 = cadence.resolve_arrival()
    assert arrival_1.occurred is False
    credit_1 = accounting.complete_ordinary_turn()
    result_1 = cadence.advance(credit_1, rng=rng)
    assert result_1.outcome is CheckOutcome.NOT_DUE
    assert cadence.turns_since_last_check == 1

    # The encounter has already resolved after 121 rounds --
    # encounter_turn_cost(121) == 3 (max(1, ceiling(121/60))).
    encounter_credits = accounting.resolve_encounter(121)
    assert encounter_credits == (
        TurnCredit(turn_number=2, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),
        TurnCredit(turn_number=3, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),
        TurnCredit(turn_number=4, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),
    )
    encounter_results = [cadence.advance(credit, rng=rng) for credit in encounter_credits]
    assert all(result.outcome is CheckOutcome.CADENCE_ADVANCED_ONLY for result in encounter_results)
    assert all(result.roll is None for result in encounter_results)
    # The tally has advanced past the normal due threshold while the
    # checklist was suspended, but nothing has executed yet.
    assert cadence.turns_since_last_check == 4

    # The next Game Turn begins: no arrival was ever pending (nothing
    # has triggered), so this ordinary turn is not preempted.
    arrival_2 = cadence.resolve_arrival()
    assert arrival_2.occurred is False
    credit_5 = accounting.complete_ordinary_turn()
    assert credit_5 == TurnCredit(turn_number=5, origin=TurnCreditOrigin.ORDINARY)
    result_5 = cadence.advance(credit_5, rng=rng)
    # The tally first advances to 5, then exactly one deferred due check
    # executes, resolving all accumulated due-ness in a single roll.
    assert result_5.outcome is CheckOutcome.NO_TRIGGER
    assert result_5.roll is not None and result_5.roll.total == 5
    assert cadence.turns_since_last_check == 0  # excess accumulated due-ness discarded

    # Exact long-encounter credit sequence: ordinary #1, encounter-derived
    # #2-#4, ordinary #5 -- origin and turn_number both preserved and
    # globally ordered across the EXP-002 -> EXP-001 boundary.
    all_credits = (credit_1, *encounter_credits, credit_5)
    assert [c.turn_number for c in all_credits] == [1, 2, 3, 4, 5]
    assert [c.origin for c in all_credits] == [
        TurnCreditOrigin.ORDINARY,
        TurnCreditOrigin.ENCOUNTER_DERIVED,
        TurnCreditOrigin.ENCOUNTER_DERIVED,
        TurnCreditOrigin.ENCOUNTER_DERIVED,
        TurnCreditOrigin.ORDINARY,
    ]

    # Total authoritative credits = 5; wandering checks executed = 1 --
    # not one check per two total credits (Simulator Ruling B's approved,
    # intentional collapse).
    all_results = (result_1, *encounter_results, result_5)
    assert len(all_credits) == 5
    checks_executed = sum(1 for result in all_results if result.roll is not None)
    assert checks_executed == 1


# --- Scenario 4: pre-decided skip -------------------------------------------


def test_scenario_4_pre_decided_skip() -> None:
    accounting, cadence = _fresh_pair()
    rng = ScriptedRNG([2])  # exactly one due check this scenario ever performs (skip consumes none)

    # Ordinary Game Turn 1: not due.
    arrival_1 = cadence.resolve_arrival()
    assert arrival_1.occurred is False
    credit_1 = accounting.complete_ordinary_turn()
    result_1 = cadence.advance(credit_1, rng=rng)
    assert result_1.outcome is CheckOutcome.NOT_DUE

    # Ordinary Game Turn 2: due, pre-decided skip.
    arrival_2 = cadence.resolve_arrival()
    assert arrival_2.occurred is False
    credit_2 = accounting.complete_ordinary_turn()
    result_2 = cadence.advance(credit_2, rng=rng, skip_signal=True)
    assert result_2.outcome is CheckOutcome.SKIPPED
    assert result_2.roll is None
    assert cadence.turns_since_last_check == 0  # the skip still consumes the due period

    # The skip did not prevent EXP-002 from producing the ordinary
    # credit (credit_2 exists, turn_number 2) and consumed the due
    # cadence period (proven next: Game Turn 3 is not due).
    arrival_3 = cadence.resolve_arrival()
    assert arrival_3.occurred is False
    credit_3 = accounting.complete_ordinary_turn()
    assert credit_3 == TurnCredit(turn_number=3, origin=TurnCreditOrigin.ORDINARY)
    result_3 = cadence.advance(credit_3, rng=rng)
    assert result_3.outcome is CheckOutcome.NOT_DUE

    # Ordinary Game Turn 4: due normally -- the skip did not cause the
    # next wandering check to occur one turn early.
    arrival_4 = cadence.resolve_arrival()
    assert arrival_4.occurred is False
    credit_4 = accounting.complete_ordinary_turn()
    result_4 = cadence.advance(credit_4, rng=rng)
    assert result_4.outcome is CheckOutcome.NO_TRIGGER
    assert result_4.roll is not None and result_4.roll.total == 2


# --- Scenario 5: heightened transition --------------------------------------


def test_scenario_5_heightened_transition() -> None:
    accounting, cadence = _fresh_pair()
    rng = ScriptedRNG([3, 4])  # exactly two due checks this scenario ever performs

    # Normal ordinary credit: tally -> 1, not due.
    arrival_1 = cadence.resolve_arrival()
    assert arrival_1.occurred is False
    credit_1 = accounting.complete_ordinary_turn()
    result_1 = cadence.advance(credit_1, rng=rng)
    assert result_1.outcome is CheckOutcome.NOT_DUE
    assert cadence.turns_since_last_check == 1

    # Next Game Turn under heightened mode: due because
    # heightened_checking=True (an explicit, valid chance level of 1).
    arrival_2 = cadence.resolve_arrival()
    assert arrival_2.occurred is False
    credit_2 = accounting.complete_ordinary_turn()
    result_2 = cadence.advance(
        credit_2, rng=rng, heightened_checking=True, heightened_chance_level=1
    )
    assert result_2.outcome is CheckOutcome.NO_TRIGGER
    assert result_2.roll is not None and result_2.roll.total == 3
    # The tally resets because this due check actually executes, not
    # because heightened mode was entered -- the normal/heightened
    # transition behavior itself is approved Simulator Ruling C; this is
    # not the suspended/deferred-check collapse governed by Ruling B
    # (no encounter-derived credits are involved in this scenario).
    assert cadence.turns_since_last_check == 0

    # Heightened mode ends. Next ordinary Game Turn: tally -> 1, not due
    # -- no reset merely because heightened mode ended, and no hidden
    # saved normal-cadence phase is consulted or restored.
    arrival_3 = cadence.resolve_arrival()
    assert arrival_3.occurred is False
    credit_3 = accounting.complete_ordinary_turn()
    result_3 = cadence.advance(credit_3, rng=rng)
    assert result_3.outcome is CheckOutcome.NOT_DUE
    assert cadence.turns_since_last_check == 1

    # Following ordinary Game Turn: baseline check due via the ordinary
    # every-two-credit cadence, unaffected by the earlier heightened
    # episode.
    arrival_4 = cadence.resolve_arrival()
    assert arrival_4.occurred is False
    credit_4 = accounting.complete_ordinary_turn()
    result_4 = cadence.advance(credit_4, rng=rng)
    assert result_4.outcome is CheckOutcome.NO_TRIGGER
    assert result_4.roll is not None and result_4.roll.total == 4
    assert cadence.turns_since_last_check == 0
