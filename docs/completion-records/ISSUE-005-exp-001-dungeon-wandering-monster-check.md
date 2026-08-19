# ISSUE-005: EXP-001 — Dungeon Wandering-Monster Check

## 1. Issue/Task Identifier and Objective

ISSUE-005 (completion-record ledger). Implement Step 3 of
`docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` (`IMPLEMENTATION PLAN
APPROVED`, human-approved 2026-08-18): the wandering-monster cadence and
pending-arrival procedure for `EXP-001` — the cadence tally, due-ness,
execution eligibility, the 1d6 roll, and pending-arrival state and
resolution — preserving approved Simulator Rulings A, B, and C exactly
as approved. `EXP-001`'s consumers (`MON-001` onward) and cross-card
integration with `EXP-002` are explicitly **not** part of this issue.

## 2. Approved Inputs/Specifications

- `docs/rules/exploration/dungeon_wandering_monster_check.md` (`EXP-001`,
  Status: `VERIFIED` as of this issue; human-approved 2026-08-18,
  including Simulator Rulings A, B, and C).
- `docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` §4.2, §8, §12.2–§12.5
  (`Status: IMPLEMENTATION PLAN APPROVED`, human-approved 2026-08-18) —
  the approved mechanical-contract extraction, module design, and
  EXP001-01..34 test-traceability obligations this issue implements.
- `ISSUE-003` (`src/rules/exploration/turn_credit.py`) — the shared
  `TurnCredit`/`TurnCreditOrigin` contract this issue's module depends
  on and does not modify.
- `ISSUE-004` (`EXP-002`) — the credit producer this card is designed to
  consume; not composed with in this issue (Step 4's scope).
- `ARCHITECTURE.md` §15.2 — `CLUSTER-001` historical-rules implementation
  authorized 2026-08-18.
- Human implementation review: implementation commit
  `a341a77de06098135fc9b57531b038bd9ebf3478`; correction commit
  `2d9f7f90695b088cd2920df9c0bacad725138fa0`. `HUMAN IMPLEMENTATION
  REVIEW: APPROVED`, 2026-08-18.

## 3. Files Created, Modified, or Deleted

**Created:**
- `src/rules/exploration/dungeon_wandering_monster_check.py`
- `tests/rules/exploration/test_dungeon_wandering_monster_check.py`
- This completion record.

**Modified:** none. (`src/rules/exploration/turn_credit.py`,
`src/rules/exploration/dungeon_turn_time_accounting.py`, and their tests
from `ISSUE-003`/`ISSUE-004` are unchanged.)

**Deleted:** none.

Cumulative accepted branch state: `cluster-001-step-3-exp-001` through
commit `2d9f7f9` (implementation `a341a77` plus human-review correction
`2d9f7f9`).

## 4. Behavior Actually Implemented

- `CheckOutcome` — a closed five-member `enum.Enum`: `CADENCE_ADVANCED_ONLY`,
  `NOT_DUE`, `SKIPPED`, `NO_TRIGGER`, `TRIGGERED`. No monster identity,
  direction, distance, surprise, reaction, combat state, or
  narrative/presentation string is represented anywhere.
- `WanderingCheckResult(outcome: CheckOutcome, roll: RollResult | None)`
  and `ArrivalResult(occurred: bool)` — immutable, slotted, frozen
  dataclasses. `roll` carries the exact `RollResult` the RNG operation
  produced for `NO_TRIGGER`/`TRIGGERED`; `None` for every outcome that
  performs no roll.
- `WanderingMonsterCadence` — owns exactly `turns_since_last_check`
  (int, starts `0`) and `pending_arrival` (bool, starts `False`),
  exposed via read-only properties; no separate "check due" flag is
  persisted.
  - **Cadence advancement (Simulator Ruling A).** Every `TurnCredit`
    `advance()` receives — ordinary or encounter-derived — advances
    `turns_since_last_check` by exactly 1, unconditionally, before any
    other logic runs.
  - **Encounter-derived credits (Simulator Ruling B).** An
    encounter-derived credit returns `CADENCE_ADVANCED_ONLY` immediately
    after the tally advances — no due-ness evaluation, no skip-signal
    evaluation, no heightened-checking evaluation, and no RNG
    consumption occur; the tally may grow arbitrarily past any threshold
    while unresolved.
  - **Due-ness.** For an ordinary credit, due-ness is recomputed fresh
    each call: `heightened_checking OR turns_since_last_check >= 2` —
    every-two-credits at baseline, every credit when heightened checking
    is active.
  - **Due-period collapse (Simulator Ruling B).** Once due, the tally
    resets to `0` unconditionally, before the skip signal is even
    checked — a performed check and a pre-decided skip both consume the
    due period identically, and any accumulated excess from prior
    encounter-derived credits is discarded with no remainder arithmetic.
  - **Pre-decided skip.** Consumes zero RNG operations and does not
    affect any other credit.
  - **Executed check.** Exactly one rules-visible `rng.roll_die(6)` call.
    Trigger threshold is `1` at baseline, or the supplied
    `heightened_chance_level` (validated to an `int` in `1..4`,
    excluding `bool`) when heightened checking is active and the check
    will actually execute — validated before any RNG consumption or
    due-period reset, and never for an inactive or skipped check.
  - **Trigger scheduling.** A trigger sets `pending_arrival := True`
    only; it does not itself signal arrival.
  - **`resolve_arrival()` (Procedure B).** A distinct operation — no
    `TurnCredit`, no RNG, zero RNG consumption, no modification of
    `turns_since_last_check` — that resolves and clears a pending
    arrival if one exists. The Rule Card's documented pending-arrival
    invariant (sufficient as a single boolean under valid execution
    sequences) is implemented as specified: no defensive guard against
    malformed caller ordering was added.
  - **Shared normal/heightened cadence tally (Simulator Ruling C).**
    `turns_since_last_check` is the single counter for both normal and
    heightened checking; activating or deactivating heightened checking
    never resets or otherwise adjusts it on its own.
- **Dependency boundary.** The module imports only
  `rules.exploration.turn_credit` (`TurnCredit`, `TurnCreditOrigin`) and
  the `RNG`/`RollResult` types from `rng` (the `RNG` Protocol only, never
  a concrete implementation). It does not import
  `dungeon_turn_time_accounting`, does not know `encounter_rounds` or
  `encounter_turn_cost`, and does not own an RNG stream, `DungeonTimeAccounting`
  state, or any orchestration layer.
- **Explicitly not implemented by this card** (unchanged from the Rule
  Card's own scope, confirmed by this implementation): wandering-monster
  selection, encounter distance, surprise, reaction, and combat — all
  remain `MON-001`/`ENC-001`/`ENC-002`/`ENC-003`/combat-domain
  responsibilities this card does not perform.

## 5. Rules Provenance

`docs/rules/exploration/dungeon_wandering_monster_check.md` (`EXP-001`),
Status `APPROVED` (now additionally `VERIFIED` as of this issue). Per the
Rule Card's own "Provenance Classification": ordinary/heightened cadence,
the 1d6 trigger, trigger-vs-arrival timing, and the responsibility
boundary are Rules Cyclopedia Explicit; the execution-eligibility split
(only an ordinary credit can execute a check) is a Necessary Mechanical
Consequence; encounter-credited-turn cadence participation (**Simulator
Ruling A**), deferred execution / collapse for threshold crossings during
a suspended checklist (**Simulator Ruling B**), and the heightened-checking
shared-counter transition (**Simulator Ruling C**) are each implemented
here exactly as their respective human-approved rulings (2026-08-18)
specify, not reinterpreted.

## 6. Tests Added or Modified

40 tests in `tests/rules/exploration/test_dungeon_wandering_monster_check.py`,
implementing the Rule Card's own EXP001-01 through EXP001-34 deterministic
test cases plus 6 supplemental structural-validation cases:

- **EXP001-01–06** — all six 1d6 baseline outcomes on a due ordinary
  check (parametrized), confirming trigger only on `1`, one roll each,
  the retained `RollResult`, and the tally reset.
- **EXP001-07–09** — baseline cadence: first credit not due, second due,
  repeated two-credit cycles with no drift.
- **EXP001-10–11** — pre-decided skip: due-and-skipped consumes the
  period with zero RNG; the following cycle is not primed early.
- **EXP001-12–17** — trigger scheduling versus arrival, the beginning-
  of-next-Game-Turn resolution, zero rolls on the arrival turn, no
  signal absent a trigger, and the pending-arrival invariant under valid
  sequencing, including clean state after a resolved arrival.
- **EXP001-18–22** — heightened checking: every-credit due-ness, the
  three chance-level boundaries (2/3/4), and the ordinary-cadence/1-in-6
  default absent an explicit heightened input.
- **EXP001-23–25** — the shared-counter transition: entry mid-cadence,
  exit mid-cadence, and repeated transitions with no drift, double-check,
  or missed check.
- **EXP001-26–30** — encounter-derived credits: single-credit and
  three-credit (121-round-equivalent) cadence-advancement-without-
  execution, deferred execution resolving all accumulated due-ness with
  exactly one roll, a mixed ordinary/encounter-derived sequence rolling
  only at ordinary credits, and the explicit non-rate-preserving
  collapse (four total credits, one check, not two).
- **EXP001-31** — the round-mode negative boundary: no credit supplied
  means `advance()` is simply never invoked; no in-progress-encounter
  state exists to test.
- **EXP001-32** — exactly one RNG operation per performed check,
  corrected during human review to use non-triggering scripted results
  (`2, 3`) so the test's later `advance()` calls remain within the Rule
  Card's valid-sequencing contract — this is an RNG-audit test, not a
  trigger/arrival test, and no longer leaves an unresolved
  `pending_arrival` across subsequent calls.
- **EXP001-33** — arrival and encounter-derived credits each consume
  zero RNG operations, proven via an empty `ScriptedRNG` queue.
- **EXP001-34** — determinism, strengthened during human review: two
  independent `SeededRNG(seed=12345)` runs record the actual immutable
  `WanderingCheckResult`/`ArrivalResult` objects (not a reduced
  `(outcome, roll total)` summary), with `resolve_arrival()` invoked at
  each beginning-of-Game-Turn moment before an ordinary credit (never
  before an encounter-derived one) and that turn's own `advance()`
  correctly skipped if arrival occurs. Because both result types are
  frozen dataclasses with field-based equality, and `WanderingCheckResult.roll`
  embeds the complete `RollResult`, the repeated-run comparison proves
  equality of `CheckOutcome`, the full `RollResult` (`expression`,
  `dice`, `die_size`, `modifier`, `sequence_number`, `total`), and
  `ArrivalResult` — not merely roll totals.
- **Supplemental structural validation** (does not renumber the 34
  approved cases): malformed active `heightened_chance_level` values
  `5`, `0`, `True` (a `bool`), and a genuine non-`int` (`"2"`) are each
  rejected with `ValueError` before any RNG consumption or due-period
  reset, with the credit's own already-applied cadence advance
  preserved; an otherwise-malformed value is correctly *not* rejected
  when heightened checking is inactive, and *not* rejected when the due
  check is skipped (the value is never actually needed in either case).

## 7. Exact Verification Commands Executed

- `uv run python scripts/verify.py` (re-run in this task at commit
  `2d9f7f9` to confirm current evidence, not relied on from an earlier
  report alone).

## 8. Verification Results

- **Tests:** all project tests passed (155 total: 115 pre-existing +
  40 new).
- **Coverage:** PASS — differentiated gate: `src/rules/` 5 files, 100%
  required per file, met; core aggregate 100.00% (≥95% required).
- **Ruff:** clean.
- **mypy --strict:** clean.
- **Overall: PASS.**
- **Feature-branch CI:** PASS (GitHub Actions, `cluster-001-step-3-exp-001`
  at commit `2d9f7f9`).

## 9. Coverage Results

`src/rules/exploration/dungeon_wandering_monster_check.py`: 67/67
statements (100%), 14/14 branches (100%) — every meaningful semantic
branch is exercised: the encounter-derived early return, ordinary
not-due, ordinary due with and without skip, baseline trigger and
non-trigger, heightened trigger/non-trigger at each boundary, both
pending-arrival states in `resolve_arrival()`, and both outcomes of
active-heightened-level validation.

## 10. Deviations

None from the approved Rule Card or implementation plan. The human-review
correction round (commit `2d9f7f9`) changed two test bodies and one
inline comment only — no production mechanic, validation rule, or public
API changed as a result.

## 11. Known Limitations/Unresolved Issues

- `EXP-001` is not yet consumed by anything — no cross-card composition
  with `EXP-002`'s `DungeonTimeAccounting` exists yet (`CLUSTER-001`
  Step 4, `tests/rules/exploration/test_cluster_001_integration.py`, not
  begun by this issue).
- No production orchestration/application/presentation layer exists that
  actually drives `advance()`/`resolve_arrival()` from real player/DM
  input — deliberately deferred per
  `docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` §11 (human
  architecture decision).
- `CLUSTER-001` as a whole is not yet implementation-complete or
  verified — both constituent Rule Cards (`EXP-001`, `EXP-002`) are now
  individually implemented and verified, but the cross-card integration
  gate remains outstanding.

## 12. Architectural Consequences

None to `ARCHITECTURE.md`'s approved module boundaries — this issue
populates `src/rules/exploration/` with its third module, exactly as
already anticipated by `ARCHITECTURE.md` §13 and the approved
implementation plan's own §8 module-structure table. No boundary or
invariant changed.
