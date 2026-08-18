"""Tests for EXP-002 (docs/rules/exploration/dungeon_turn_time_accounting.md),
per its own "Deterministic Test Cases" and
docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md §12.1 (EXP002-01..16).
"""

import inspect

from rules.exploration.dungeon_turn_time_accounting import (
    DungeonTimeAccounting,
    encounter_turn_cost,
)
from rules.exploration.turn_credit import TurnCredit, TurnCreditOrigin

# --- EXP002-01/02: ordinary turns -----------------------------------------


def test_exp002_01_one_ordinary_turn_produces_one_ordinary_credit() -> None:
    accounting = DungeonTimeAccounting()
    credit = accounting.complete_ordinary_turn()
    assert credit == TurnCredit(turn_number=1, origin=TurnCreditOrigin.ORDINARY)


def test_exp002_02_five_ordinary_turns_are_strictly_increasing_and_gapless() -> None:
    accounting = DungeonTimeAccounting()
    credits = [accounting.complete_ordinary_turn() for _ in range(5)]
    assert credits == [
        TurnCredit(turn_number=n, origin=TurnCreditOrigin.ORDINARY) for n in range(1, 6)
    ]


# --- EXP002-03..09: encounter round-count boundaries -----------------------


def test_exp002_03_one_round_encounter_produces_one_credit() -> None:
    accounting = DungeonTimeAccounting()
    credits = accounting.resolve_encounter(1)
    assert credits == (TurnCredit(turn_number=1, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),)


def test_exp002_04_four_round_encounter_produces_one_credit() -> None:
    accounting = DungeonTimeAccounting()
    credits = accounting.resolve_encounter(4)
    assert credits == (TurnCredit(turn_number=1, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),)


def test_exp002_05_fifty_nine_round_encounter_produces_one_credit() -> None:
    accounting = DungeonTimeAccounting()
    credits = accounting.resolve_encounter(59)
    assert credits == (TurnCredit(turn_number=1, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),)


def test_exp002_06_sixty_round_encounter_produces_one_credit() -> None:
    accounting = DungeonTimeAccounting()
    credits = accounting.resolve_encounter(60)
    assert credits == (TurnCredit(turn_number=1, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),)


def test_exp002_07_sixty_one_round_encounter_produces_two_credits() -> None:
    accounting = DungeonTimeAccounting()
    credits = accounting.resolve_encounter(61)
    assert credits == (
        TurnCredit(turn_number=1, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),
        TurnCredit(turn_number=2, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),
    )


def test_exp002_08_one_hundred_twenty_round_encounter_produces_two_credits() -> None:
    accounting = DungeonTimeAccounting()
    credits = accounting.resolve_encounter(120)
    assert credits == (
        TurnCredit(turn_number=1, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),
        TurnCredit(turn_number=2, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),
    )


def test_exp002_09_one_hundred_twenty_one_round_encounter_produces_three_credits() -> None:
    accounting = DungeonTimeAccounting()
    credits = accounting.resolve_encounter(121)
    assert credits == (
        TurnCredit(turn_number=1, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),
        TurnCredit(turn_number=2, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),
        TurnCredit(turn_number=3, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),
    )


# --- EXP002-10: no mid-encounter credit ------------------------------------


def test_exp002_10_no_credit_is_produced_until_an_encounter_is_reported_resolved() -> None:
    # EXP-002 has no progressive round-mode credit production: there is no
    # "encounter in progress" API to call at all, only the two approved
    # operations below. Doing nothing (standing in for an encounter still
    # being resolved in round-mode) leaves the cumulative count untouched
    # -- proven by the *next* produced credit still starting at 1, not by
    # inspecting any private state.
    accounting = DungeonTimeAccounting()
    public_api = {
        name
        for name, member in inspect.getmembers(accounting, predicate=inspect.ismethod)
        if not name.startswith("_")
    }
    assert public_api == {"complete_ordinary_turn", "resolve_encounter"}

    # No credit exists yet merely because an encounter might be "in
    # progress" -- only an explicit resolve_encounter() call produces one.
    first_credit_after_waiting = accounting.resolve_encounter(30)
    assert first_credit_after_waiting == (
        TurnCredit(turn_number=1, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),
    )


# --- EXP002-11: turn-mode -> round-mode -> turn-mode -----------------------


def test_exp002_11_mode_transition_continues_cumulative_numbering() -> None:
    accounting = DungeonTimeAccounting()
    ordinary_1 = accounting.complete_ordinary_turn()
    encounter_credits = accounting.resolve_encounter(61)
    ordinary_2 = accounting.complete_ordinary_turn()

    assert ordinary_1 == TurnCredit(turn_number=1, origin=TurnCreditOrigin.ORDINARY)
    assert encounter_credits == (
        TurnCredit(turn_number=2, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),
        TurnCredit(turn_number=3, origin=TurnCreditOrigin.ENCOUNTER_DERIVED),
    )
    assert ordinary_2 == TurnCredit(turn_number=4, origin=TurnCreditOrigin.ORDINARY)


# --- EXP002-12: multi-credit recovery ---------------------------------------


def test_exp002_12_long_encounter_credits_are_individually_recoverable_and_ordered() -> None:
    accounting = DungeonTimeAccounting()
    credits = accounting.resolve_encounter(121)
    assert len(credits) == 3
    assert credits[0].turn_number == 1
    assert credits[1].turn_number == 2
    assert credits[2].turn_number == 3
    assert all(credit.origin is TurnCreditOrigin.ENCOUNTER_DERIVED for credit in credits)


# --- EXP002-13: arbitrary mixed accounting ---------------------------------


def test_exp002_13_mixed_sequence_is_one_strictly_increasing_gapless_sequence() -> None:
    accounting = DungeonTimeAccounting()
    produced: list[TurnCredit] = []
    produced.append(accounting.complete_ordinary_turn())
    produced.extend(accounting.resolve_encounter(1))  # short: 1 credit
    produced.append(accounting.complete_ordinary_turn())
    produced.extend(accounting.resolve_encounter(121))  # long: 3 credits
    produced.append(accounting.complete_ordinary_turn())
    produced.extend(accounting.resolve_encounter(60))  # boundary: 1 credit
    produced.append(accounting.complete_ordinary_turn())

    turn_numbers = [credit.turn_number for credit in produced]
    assert turn_numbers == list(range(1, len(produced) + 1))


# --- EXP002-14: no RNG dependency -------------------------------------------


def test_exp002_14_neither_public_operation_accepts_or_needs_an_rng() -> None:
    # Demonstrated through the actual public API/behavior, not a
    # manufactured no-op RNG hook: neither operation declares an RNG (or
    # any) parameter beyond what its own mechanics require, and every
    # test in this module already exercises both operations repeatedly
    # without ever constructing or importing anything from src/rng.
    ordinary_params = list(
        inspect.signature(DungeonTimeAccounting.complete_ordinary_turn).parameters
    )
    encounter_params = list(
        inspect.signature(DungeonTimeAccounting.resolve_encounter).parameters
    )
    assert ordinary_params == ["self"]
    assert encounter_params == ["self", "encounter_rounds"]


# --- EXP002-15: no cadence filtering ----------------------------------------


def test_exp002_15_every_completed_turn_is_credited_none_discarded() -> None:
    accounting = DungeonTimeAccounting()
    ordinary_credits = [accounting.complete_ordinary_turn() for _ in range(4)]
    # If EXP-002 filtered by any every-other-turn cadence, only 2 of these
    # 4 calls would yield a distinct credit. EXP-002 has no cadence
    # concept at all -- every call produces its own credit.
    assert [credit.turn_number for credit in ordinary_credits] == [1, 2, 3, 4]

    encounter_credits = accounting.resolve_encounter(121)
    # None of a long encounter's several credits are discarded either.
    assert len(encounter_credits) == 3
    assert [credit.turn_number for credit in encounter_credits] == [5, 6, 7]


# --- EXP002-16: isolated encounter_turn_cost() formula ----------------------


def test_exp002_16_encounter_turn_cost_matches_the_approved_formula() -> None:
    assert encounter_turn_cost(1) == 1
    assert encounter_turn_cost(59) == 1
    assert encounter_turn_cost(60) == 1
    assert encounter_turn_cost(61) == 2
    assert encounter_turn_cost(120) == 2
    assert encounter_turn_cost(121) == 3
    assert encounter_turn_cost(481) == 9
