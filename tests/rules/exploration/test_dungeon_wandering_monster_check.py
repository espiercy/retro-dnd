"""Tests for EXP-001 (docs/rules/exploration/dungeon_wandering_monster_check.md),
per its own "Deterministic Test Cases" (34 cases) and
docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md §12.2-12.5 (EXP001-01..34).
"""

from __future__ import annotations

import pytest

from rng import ScriptedRNG, SeededRNG
from rules.exploration.dungeon_wandering_monster_check import (
    ArrivalResult,
    CheckOutcome,
    WanderingMonsterCadence,
)
from rules.exploration.turn_credit import TurnCredit, TurnCreditOrigin


def _ordinary(turn_number: int) -> TurnCredit:
    return TurnCredit(turn_number=turn_number, origin=TurnCreditOrigin.ORDINARY)


def _encounter_derived(turn_number: int) -> TurnCredit:
    return TurnCredit(turn_number=turn_number, origin=TurnCreditOrigin.ENCOUNTER_DERIVED)


# --- EXP001-01..06: baseline 1d6 outcomes (ordinary chance, check due) -----


@pytest.mark.parametrize(
    ("scripted_roll", "expected_outcome"),
    [
        (1, CheckOutcome.TRIGGERED),
        (2, CheckOutcome.NO_TRIGGER),
        (3, CheckOutcome.NO_TRIGGER),
        (4, CheckOutcome.NO_TRIGGER),
        (5, CheckOutcome.NO_TRIGGER),
        (6, CheckOutcome.NO_TRIGGER),
    ],
)
def test_exp001_01_06_baseline_die_outcomes(
    scripted_roll: int, expected_outcome: CheckOutcome
) -> None:
    rng = ScriptedRNG([scripted_roll])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)  # first credit: not yet due
    result = cadence.advance(_ordinary(2), rng=rng)  # second credit: due
    assert result.outcome is expected_outcome
    assert result.roll is not None
    assert result.roll.total == scripted_roll
    assert cadence.turns_since_last_check == 0
    assert cadence.pending_arrival is (expected_outcome is CheckOutcome.TRIGGERED)


# --- EXP001-07..09: baseline cadence ---------------------------------------


def test_exp001_07_first_ordinary_credit_is_not_due() -> None:
    rng = ScriptedRNG([])
    cadence = WanderingMonsterCadence()
    result = cadence.advance(_ordinary(1), rng=rng)
    assert result.outcome is CheckOutcome.NOT_DUE
    assert result.roll is None
    assert cadence.turns_since_last_check == 1


def test_exp001_08_second_ordinary_credit_is_due() -> None:
    rng = ScriptedRNG([3])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)
    result = cadence.advance(_ordinary(2), rng=rng)
    assert result.outcome is CheckOutcome.NO_TRIGGER
    assert cadence.turns_since_last_check == 0


def test_exp001_09_repeated_two_turn_cycle_has_no_drift() -> None:
    rng = ScriptedRNG([2] * 10)
    cadence = WanderingMonsterCadence()
    outcomes = [cadence.advance(_ordinary(n), rng=rng).outcome for n in range(1, 21)]
    assert outcomes == [
        CheckOutcome.NOT_DUE if i % 2 == 0 else CheckOutcome.NO_TRIGGER for i in range(20)
    ]


# --- EXP001-10..11: pre-decided skip, cadence bookkeeping -------------------


def test_exp001_10_due_check_with_skip_signal_is_skipped() -> None:
    rng = ScriptedRNG([])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)
    result = cadence.advance(_ordinary(2), rng=rng, skip_signal=True)
    assert result.outcome is CheckOutcome.SKIPPED
    assert result.roll is None
    assert cadence.turns_since_last_check == 0


def test_exp001_11_skip_does_not_cause_early_or_extra_roll() -> None:
    rng = ScriptedRNG([4])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)
    cadence.advance(_ordinary(2), rng=rng, skip_signal=True)
    third = cadence.advance(_ordinary(3), rng=rng)
    assert third.outcome is CheckOutcome.NOT_DUE
    assert cadence.turns_since_last_check == 1
    fourth = cadence.advance(_ordinary(4), rng=rng)
    assert fourth.outcome is CheckOutcome.NO_TRIGGER
    assert cadence.turns_since_last_check == 0


# --- EXP001-12..17: trigger scheduling, arrival, pending-arrival invariant -


def test_exp001_12_triggering_check_does_not_itself_signal_arrival() -> None:
    rng = ScriptedRNG([1])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)
    result = cadence.advance(_ordinary(2), rng=rng)
    assert result.outcome is CheckOutcome.TRIGGERED
    assert cadence.pending_arrival is True


def test_exp001_13_arrival_is_resolved_at_beginning_of_next_game_turn() -> None:
    rng = ScriptedRNG([1])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)
    cadence.advance(_ordinary(2), rng=rng)  # triggers at end of turn N
    arrival = cadence.resolve_arrival()  # beginning of turn N+1
    assert arrival == ArrivalResult(occurred=True)
    assert cadence.pending_arrival is False


def test_exp001_14_no_extra_roll_on_the_arrival_turn() -> None:
    rng = ScriptedRNG([1])  # exactly one value: the triggering roll only
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)
    cadence.advance(_ordinary(2), rng=rng)  # consumes the single queued value
    # resolve_arrival() takes no rng parameter at all -- structurally
    # cannot consume one -- and succeeding here, with the scripted queue
    # already exhausted, confirms no further roll was needed.
    arrival = cadence.resolve_arrival()
    assert arrival == ArrivalResult(occurred=True)


def test_exp001_15_absent_a_trigger_resolve_arrival_never_signals() -> None:
    rng = ScriptedRNG([2, 2, 2])
    cadence = WanderingMonsterCadence()
    for turn_number in range(1, 4):
        cadence.advance(_ordinary(turn_number), rng=rng)
        assert cadence.resolve_arrival() == ArrivalResult(occurred=False)


def test_exp001_16_valid_sequence_pending_arrival_invariant() -> None:
    rng = ScriptedRNG([1])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)
    cadence.advance(_ordinary(2), rng=rng)  # triggers; pending_arrival=True
    assert cadence.pending_arrival is True
    # Valid sequencing: Procedure B is invoked before that same turn's
    # own Procedure A, so the preempted turn's own advance() call is
    # never made -- no second TRIGGERED transition can occur.
    arrival = cadence.resolve_arrival()
    assert arrival.occurred is True
    assert cadence.pending_arrival is False


def test_exp001_17_state_is_clean_after_a_resolved_arrival() -> None:
    rng = ScriptedRNG([1, 3])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)
    cadence.advance(_ordinary(2), rng=rng)
    cadence.resolve_arrival()
    result = cadence.advance(_ordinary(3), rng=rng)  # fresh tally, not due yet
    assert result.outcome is CheckOutcome.NOT_DUE
    assert cadence.pending_arrival is False
    result2 = cadence.advance(_ordinary(4), rng=rng)
    assert result2.outcome is CheckOutcome.NO_TRIGGER


# --- EXP001-18..22: heightened checking ------------------------------------


def test_exp001_18_heightened_makes_every_ordinary_credit_due() -> None:
    rng = ScriptedRNG([2, 2, 2])
    cadence = WanderingMonsterCadence()
    for turn_number in range(1, 4):
        result = cadence.advance(
            _ordinary(turn_number), rng=rng, heightened_checking=True, heightened_chance_level=1
        )
        assert result.outcome is CheckOutcome.NO_TRIGGER
        assert cadence.turns_since_last_check == 0


def test_exp001_19_chance_level_two_triggers_on_two_not_three() -> None:
    triggering = WanderingMonsterCadence().advance(
        _ordinary(1), rng=ScriptedRNG([2]), heightened_checking=True, heightened_chance_level=2
    )
    non_triggering = WanderingMonsterCadence().advance(
        _ordinary(1), rng=ScriptedRNG([3]), heightened_checking=True, heightened_chance_level=2
    )
    assert triggering.outcome is CheckOutcome.TRIGGERED
    assert non_triggering.outcome is CheckOutcome.NO_TRIGGER


def test_exp001_20_chance_level_three_triggers_on_three_not_four() -> None:
    triggering = WanderingMonsterCadence().advance(
        _ordinary(1), rng=ScriptedRNG([3]), heightened_checking=True, heightened_chance_level=3
    )
    non_triggering = WanderingMonsterCadence().advance(
        _ordinary(1), rng=ScriptedRNG([4]), heightened_checking=True, heightened_chance_level=3
    )
    assert triggering.outcome is CheckOutcome.TRIGGERED
    assert non_triggering.outcome is CheckOutcome.NO_TRIGGER


def test_exp001_21_chance_level_four_triggers_on_four_not_five() -> None:
    triggering = WanderingMonsterCadence().advance(
        _ordinary(1), rng=ScriptedRNG([4]), heightened_checking=True, heightened_chance_level=4
    )
    non_triggering = WanderingMonsterCadence().advance(
        _ordinary(1), rng=ScriptedRNG([5]), heightened_checking=True, heightened_chance_level=4
    )
    assert triggering.outcome is CheckOutcome.TRIGGERED
    assert non_triggering.outcome is CheckOutcome.NO_TRIGGER


def test_exp001_22_absent_explicit_heightened_input_defaults_to_baseline() -> None:
    rng = ScriptedRNG([1])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)  # no heightened_checking supplied
    result = cadence.advance(_ordinary(2), rng=rng)  # due only via normal 2-credit cadence
    assert result.outcome is CheckOutcome.TRIGGERED  # baseline 1-in-6


# --- EXP001-23..25: heightened-checking transition (Simulator Ruling C) ---


def test_exp001_23_entry_mid_cadence() -> None:
    rng = ScriptedRNG([1])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)  # tally=1, normal cadence
    assert cadence.turns_since_last_check == 1
    result = cadence.advance(
        _ordinary(2), rng=rng, heightened_checking=True, heightened_chance_level=1
    )
    assert result.outcome is CheckOutcome.TRIGGERED
    assert cadence.turns_since_last_check == 0


def test_exp001_24_exit_mid_cadence() -> None:
    rng = ScriptedRNG([2, 3])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng, heightened_checking=True, heightened_chance_level=1)
    assert cadence.turns_since_last_check == 0
    result = cadence.advance(_ordinary(2), rng=rng)  # heightened now inactive
    assert result.outcome is CheckOutcome.NOT_DUE
    assert cadence.turns_since_last_check == 1
    result2 = cadence.advance(_ordinary(3), rng=rng)
    assert result2.outcome is CheckOutcome.NO_TRIGGER


def test_exp001_25_repeated_transitions_produce_no_drift() -> None:
    rng = ScriptedRNG([2] * 20)
    cadence = WanderingMonsterCadence()
    turn_number = 1
    for _cycle in range(5):
        cadence.advance(
            _ordinary(turn_number), rng=rng, heightened_checking=True, heightened_chance_level=1
        )
        turn_number += 1
        cadence.advance(
            _ordinary(turn_number), rng=rng, heightened_checking=True, heightened_chance_level=1
        )
        turn_number += 1
        assert cadence.turns_since_last_check == 0

        cadence.advance(_ordinary(turn_number), rng=rng)
        turn_number += 1
        assert cadence.turns_since_last_check == 1
        cadence.advance(_ordinary(turn_number), rng=rng)
        turn_number += 1
        assert cadence.turns_since_last_check == 0


# --- EXP001-26..30: encounter-derived credits, cadence-only, collapse ------


def test_exp001_26_single_encounter_derived_credit_does_not_execute() -> None:
    rng = ScriptedRNG([])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)
    result = cadence.advance(_encounter_derived(2), rng=rng)
    assert result.outcome is CheckOutcome.CADENCE_ADVANCED_ONLY
    assert result.roll is None
    assert cadence.turns_since_last_check == 2  # not reset; no execution occurred
    assert cadence.pending_arrival is False


def test_exp001_27_long_encounter_produces_zero_rolls_during_it() -> None:
    rng = ScriptedRNG([])
    cadence = WanderingMonsterCadence()
    for turn_number in range(1, 4):  # three encounter-derived credits (121-round encounter)
        result = cadence.advance(_encounter_derived(turn_number), rng=rng)
        assert result.outcome is CheckOutcome.CADENCE_ADVANCED_ONLY
        assert result.roll is None
    assert cadence.turns_since_last_check == 3  # past the normal threshold, still unresolved


def test_exp001_28_deferred_execution_resolves_all_of_it_with_one_roll() -> None:
    rng = ScriptedRNG([4])
    cadence = WanderingMonsterCadence()
    for turn_number in range(1, 4):
        cadence.advance(_encounter_derived(turn_number), rng=rng)
    result = cadence.advance(_ordinary(4), rng=rng)
    assert result.outcome is CheckOutcome.NO_TRIGGER
    assert result.roll is not None
    assert cadence.turns_since_last_check == 0  # excess discarded


def test_exp001_29_mixed_sequence_rolls_only_at_ordinary_credits() -> None:
    rng = ScriptedRNG([5])
    cadence = WanderingMonsterCadence()
    r1 = cadence.advance(_ordinary(1), rng=rng)
    r2 = cadence.advance(_encounter_derived(2), rng=rng)
    r3 = cadence.advance(_encounter_derived(3), rng=rng)
    r4 = cadence.advance(_ordinary(4), rng=rng)
    assert r1.outcome is CheckOutcome.NOT_DUE
    assert r2.outcome is CheckOutcome.CADENCE_ADVANCED_ONLY
    assert r3.outcome is CheckOutcome.CADENCE_ADVANCED_ONLY
    assert r4.outcome is CheckOutcome.NO_TRIGGER
    assert r4.roll is not None


def test_exp001_30_collapse_is_not_rate_preserving() -> None:
    rng = ScriptedRNG([6])
    cadence = WanderingMonsterCadence()
    for turn_number in range(1, 4):
        cadence.advance(_encounter_derived(turn_number), rng=rng)
    result = cadence.advance(_ordinary(4), rng=rng)
    # Four total credits produced exactly one wandering check, not two --
    # the approved, intentional consequence of Simulator Ruling B.
    assert result.outcome is CheckOutcome.NO_TRIGGER
    assert cadence.turns_since_last_check == 0


# --- EXP001-31: round-mode boundary ----------------------------------------


def test_exp001_31_no_credit_supplied_means_advance_is_simply_not_invoked() -> None:
    # EXP-001 owns no round-mode state or API of its own -- while
    # EXP-002 produces no credit (round-mode in progress), advance() is
    # simply never called, and there is nothing for this card itself to
    # track. A freshly constructed instance's state proves this: no
    # in-progress-encounter machinery exists to have advanced it.
    cadence = WanderingMonsterCadence()
    assert cadence.turns_since_last_check == 0
    assert cadence.pending_arrival is False


# --- EXP001-32..33: RNG audit ------------------------------------------------


def test_exp001_32_exactly_one_roll_per_performed_check() -> None:
    rng = ScriptedRNG([1, 2])  # exact length: two due checks need exactly two values
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)
    result1 = cadence.advance(_ordinary(2), rng=rng)
    cadence.advance(_ordinary(3), rng=rng)
    result2 = cadence.advance(_ordinary(4), rng=rng)
    assert result1.roll is not None and result1.roll.total == 1
    assert result2.roll is not None and result2.roll.total == 2


def test_exp001_33_arrival_and_encounter_derived_credits_consume_zero_rolls() -> None:
    rng = ScriptedRNG([])  # any draw attempt raises immediately
    cadence = WanderingMonsterCadence()
    cadence.advance(_encounter_derived(1), rng=rng)
    cadence.advance(_encounter_derived(2), rng=rng)
    cadence.resolve_arrival()
    # No RollSequenceExhaustedError was raised despite the empty queue.


# --- EXP001-34: determinism --------------------------------------------------


def test_exp001_34_determinism_with_seeded_rng() -> None:
    def run() -> list[tuple[CheckOutcome, int | None]]:
        rng = SeededRNG(seed=12345)
        cadence = WanderingMonsterCadence()
        credits = [_ordinary(1), _ordinary(2), _encounter_derived(3), _ordinary(4), _ordinary(5)]
        results = []
        for credit in credits:
            result = cadence.advance(credit, rng=rng)
            roll_total = result.roll.total if result.roll is not None else None
            results.append((result.outcome, roll_total))
        return results

    assert run() == run()


# --- Supplemental: active heightened-chance-level validation ---------------
# (structural input validation of the approved plan's explicit valid-value
# contract, {1,2,3,4} -- not a new game mechanic; does not renumber the
# approved EXP001-01..34 cases above)


def test_supplemental_malformed_heightened_chance_level_five_rejected() -> None:
    rng = ScriptedRNG([])
    cadence = WanderingMonsterCadence()
    with pytest.raises(ValueError, match="heightened_chance_level"):
        cadence.advance(_ordinary(1), rng=rng, heightened_checking=True, heightened_chance_level=5)
    # No reset occurred beyond the unconditional +1 every credit applies.
    assert cadence.turns_since_last_check == 1


def test_supplemental_malformed_heightened_chance_level_zero_rejected() -> None:
    rng = ScriptedRNG([])
    cadence = WanderingMonsterCadence()
    with pytest.raises(ValueError, match="heightened_chance_level"):
        cadence.advance(_ordinary(1), rng=rng, heightened_checking=True, heightened_chance_level=0)


def test_supplemental_malformed_heightened_chance_level_bool_rejected() -> None:
    rng = ScriptedRNG([])
    cadence = WanderingMonsterCadence()
    with pytest.raises(ValueError, match="heightened_chance_level"):
        cadence.advance(
            _ordinary(1), rng=rng, heightened_checking=True, heightened_chance_level=True
        )


def test_supplemental_irrelevant_heightened_chance_level_ignored_when_inactive() -> None:
    rng = ScriptedRNG([1])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)
    # heightened_checking is False (default); an otherwise-malformed
    # heightened_chance_level must not be rejected merely because it is
    # irrelevant and unused.
    result = cadence.advance(_ordinary(2), rng=rng, heightened_chance_level=99)
    assert result.outcome is CheckOutcome.TRIGGERED


def test_supplemental_irrelevant_heightened_chance_level_ignored_when_skipped() -> None:
    rng = ScriptedRNG([])
    cadence = WanderingMonsterCadence()
    cadence.advance(_ordinary(1), rng=rng)  # tally=1, not due, no roll
    # Due via heightened on the 2nd credit, but skipped -- heightened_chance_level
    # is never actually needed for this call, so a malformed value must
    # not be rejected.
    result = cadence.advance(
        _ordinary(2),
        rng=rng,
        skip_signal=True,
        heightened_checking=True,
        heightened_chance_level=99,
    )
    assert result.outcome is CheckOutcome.SKIPPED
