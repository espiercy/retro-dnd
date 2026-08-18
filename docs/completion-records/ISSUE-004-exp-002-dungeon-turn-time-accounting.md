# ISSUE-004: EXP-002 — Dungeon Turn / Time Accounting

## 1. Issue/Task Identifier and Objective

ISSUE-004 (completion-record ledger). Implement Step 2 of
`docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` (`IMPLEMENTATION PLAN
APPROVED`, human-approved 2026-08-18): the authoritative whole-turn
accounting procedure for `EXP-002` — one cumulative dungeon-turn counter,
one credit per completed ordinary Game-Turn-Checklist iteration, and the
human-approved long-encounter formula for resolved-encounter credits.
`EXP-001`'s own mechanical implementation is explicitly **not** part of
this issue.

## 2. Approved Inputs/Specifications

- `docs/rules/exploration/dungeon_turn_time_accounting.md` (`EXP-002`,
  Status: `APPROVED`, human-approved 2026-08-16, including its
  human-approved long-encounter Simulator Ruling,
  `encounter_turn_cost = max(1, ceiling(encounter_rounds / 60))`).
- `docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` §4.1, §8, §12.1
  (`Status: IMPLEMENTATION PLAN APPROVED`, human-approved 2026-08-18) —
  the approved mechanical-contract extraction, module design, and
  EXP002-01..16 test-traceability obligations this issue implements.
- `ISSUE-003` (`src/rules/exploration/turn_credit.py`) — the shared
  `TurnCredit`/`TurnCreditOrigin` contract this issue's module depends on
  and does not modify.
- `ARCHITECTURE.md` §15.2 — `CLUSTER-001` historical-rules implementation
  authorized 2026-08-18.
- Human implementation review: reviewed implementation commit
  `2dd0135d1db2207f4fa710e53823bf1c5b3586ee`, `HUMAN-APPROVED — 2026-08-18`.

## 3. Files Created, Modified, or Deleted

**Created:**
- `src/rules/exploration/dungeon_turn_time_accounting.py`
- `tests/rules/exploration/test_dungeon_turn_time_accounting.py`
- This completion record.

**Modified:** none. (`src/rules/exploration/turn_credit.py` and its tests
from `ISSUE-003` are unchanged.)

**Deleted:** none.

Merged to `main` at `7197fe06b0a1cb1fdc8af7034c000343d0db7ab2`.

## 4. Behavior Actually Implemented

- `encounter_turn_cost(encounter_rounds: int) -> int` — the human-approved
  formula `max(1, ceiling(encounter_rounds / 60))`, computed with exact
  integer arithmetic (`ceiling(a / b) == (a + b - 1) // b` for positive
  integers) — no floating-point value is ever constructed. Preserves the
  approved formula's deliberately discrete, whole-turn-block behavior
  exactly as specified, including its worked examples: 1 round, 59
  rounds, and 60 rounds each cost exactly 1 turn; 61 rounds costs 2; 120
  rounds costs 2; 121 rounds costs 3. No behavior was invented for
  zero, negative, non-`int`, or `bool` `encounter_rounds` — the approved
  Rule Card and implementation plan do not define behavior for those
  inputs, and this issue does not silently create a rule for them.
- `DungeonTimeAccounting` — a plain class (no `@dataclass`, no
  `__slots__`, matching the existing stateful-class convention already
  used by `src/rng/rng.py`'s `_BaseRNG`/`SeededRNG`/`ScriptedRNG`) owning
  one private cumulative integer dungeon-turn counter, starting at zero
  credited turns:
  - `complete_ordinary_turn()` takes no arguments, advances the counter
    by exactly 1, and returns one `TurnCredit(origin=ORDINARY)`.
  - `resolve_encounter(encounter_rounds)` computes
    `encounter_turn_cost(encounter_rounds)` and returns that many
    sequential `TurnCredit(origin=ENCOUNTER_DERIVED)` values as an
    ordered tuple — individually recoverable, never collapsed into one
    opaque multi-turn value.
  - Both operations draw from the same single counter, producing one
    strictly increasing, gapless credit sequence across any mixture of
    ordinary turns and resolved encounters, with no reset for the
    lifetime of an instance.
  - No credit history beyond the running counter is retained; each
    returned credit's own `turn_number` establishes the ordering
    invariant.
- No mid-encounter accounting API exists (no `advance_round()`,
  `begin_encounter()`, `encounter_in_progress`, or similar) — `EXP-002`
  is consulted only once an encounter has already resolved and its final
  round count is known; zero credits are produced while round-mode
  resolution is in progress, by construction (there is no call that could
  produce one).
- Neither operation accepts, constructs, or interacts with an RNG,
  activity cost, movement, search, or rest data. No fractional-time value
  (float, `Fraction`, minutes/seconds field, partial-turn remainder)
  appears anywhere in the module.
- The module depends only on `rules.exploration.turn_credit` and the
  Python standard library — no import of `dungeon_wandering_monster_check`,
  `src/rng`, `src/survivability`, or any orchestration/application/
  presentation/events code. `EXP-002` has no knowledge of `EXP-001`'s
  every-two-turn cadence or any other consumer-side interpretation of the
  credits it produces.

## 5. Rules Provenance

`docs/rules/exploration/dungeon_turn_time_accounting.md` (`EXP-002`),
Status `APPROVED` (now additionally `VERIFIED` as of this issue — see
the Rule Card's own current-facing lifecycle update). Provenance per the
Rule Card's own "Provenance Classification": ordinary-turn crediting and
the two-mode (turn/round) structure are Rules Cyclopedia Explicit; the
long-encounter `encounter_turn_cost` formula is the card's own
human-approved Simulator Ruling (2026-08-16), implemented here exactly as
approved, not reinterpreted.

## 6. Tests Added or Modified

16 tests in `tests/rules/exploration/test_dungeon_turn_time_accounting.py`,
implementing `docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` §12.1's
EXP002-01 through EXP002-16 traceability obligations:

- **EXP002-01/02** — one ordinary turn produces one `ORDINARY` credit;
  five consecutive ordinary turns produce credits `1..5`, strictly
  increasing and gapless.
- **EXP002-03..09** — the full round-count boundary set (1, 4, 59, 60,
  61, 120, 121 rounds), asserting the exact expected credit count and
  that every returned credit is `ENCOUNTER_DERIVED`.
- **EXP002-10** — no credit is produced until an encounter is reported
  resolved: asserted via the approved two-method public API surface
  (`inspect.getmembers`, confirming no third, progressive-accounting
  method exists) and via the next produced credit still starting its
  numbering at `1` — not via an invented in-progress-encounter state
  machine.
- **EXP002-11** — the exact ordinary → resolved-encounter → ordinary
  worked example from the implementation plan, confirming cumulative
  numbering continues with no reset, gap, or duplicate.
- **EXP002-12** — a 121-round encounter's three credits are individually
  recoverable and correctly ordered.
- **EXP002-13** — an arbitrary mixed sequence of ordinary turns and both
  short and >60-round encounters produces one strictly increasing,
  gapless global sequence.
- **EXP002-14** — neither public operation accepts an RNG parameter,
  confirmed via `inspect.signature` against the actual declared API
  (not a manufactured no-op RNG hook).
- **EXP002-15** — every completed turn is credited; none are discarded
  or filtered by any cadence concept, for both ordinary and
  encounter-derived credits.
- **EXP002-16** — the isolated `encounter_turn_cost()` formula at 1, 59,
  60, 61, 120, 121, and 481 rounds, confirming the general case beyond
  the Rule Card's own small worked examples.

## 7. Exact Verification Commands Executed

- `uv run python scripts/verify.py`

## 8. Verification Results

- **Tests:** all project tests passed on the reviewed branch (115 total
  at the time of this issue: 99 pre-existing + 16 new).
- **Coverage:** PASS — differentiated gate: `src/rules/` 4 files, 100%
  required per file, met; core aggregate 100.00% (≥95% required).
- **Ruff:** clean. One finding surfaced and was fixed during
  development: an `E501` line-too-long in the test module, resolved by
  wrapping the offending `inspect.signature(...)` call across lines —
  no behavioral change.
- **mypy --strict:** clean.
- **Overall: PASS.**

## 9. Coverage Results

`src/rules/exploration/dungeon_turn_time_accounting.py`: 19/19 statements
(100%), 2/2 branches (100%) — the module's only branch point (the `for`
loop in `resolve_encounter`) has both its "continue iterating" arc
(exercised by every ≥2-credit encounter test) and its "exit after the
final iteration" arc (exercised by every 1-credit encounter test)
covered by the existing EXP002-03..09/11/12/13 tests, with no need for a
contrived zero-iteration case (the approved formula's own `max(1, ...)`
guarantees `resolve_encounter` always produces at least one credit).

## 10. Deviations

None from the approved Rule Card or implementation plan. As directed, no
validation was added for `encounter_rounds` values the approved contract
does not define (zero, negative, non-`int`, `bool`) — this is a
deliberate scope boundary, not an oversight, and is recorded here rather
than silently omitted.

## 11. Known Limitations/Unresolved Issues

- `EXP-001`'s own mechanical implementation (wandering-monster cadence,
  pending arrival, heightened checking, RNG integration) does not exist
  yet — this issue implements `EXP-002` only. `EXP-002`'s credits are not
  yet consumed by anything; that is `CLUSTER-001` Step 3's scope.
- No cross-card integration test exists yet (`CLUSTER-001` Step 4,
  `tests/rules/exploration/test_cluster_001_integration.py`) — not begun
  by this issue.
- No production orchestration/application/presentation layer exists that
  actually drives `complete_ordinary_turn()`/`resolve_encounter()` from
  real player/DM input — deliberately deferred per
  `docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` §11 (human
  architecture decision, "Preserve the future human-playable
  architecture").

## 12. Architectural Consequences

None to `ARCHITECTURE.md`'s approved module boundaries — this issue
populates `src/rules/exploration/` with its second module, exactly as
already anticipated by `ARCHITECTURE.md` §13 and the approved
implementation plan's own §8 module-structure table. No boundary or
invariant changed.
