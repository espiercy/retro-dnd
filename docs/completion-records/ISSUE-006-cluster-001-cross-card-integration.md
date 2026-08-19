# ISSUE-006: CLUSTER-001 — Cross-Card Integration Gate

## 1. Issue/Task Identifier and Objective

ISSUE-006 (completion-record ledger). Implement Step 4 of
`docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` (`IMPLEMENTATION PLAN
APPROVED`, human-approved 2026-08-18): verify that the independently
`VERIFIED` `EXP-001` and `EXP-002` production components compose
correctly across the approved `CLUSTER-001` procedural boundary, without
adding a production orchestration layer. This is the cluster's cross-card
integration gate — the last of the four implementation steps the plan
defines (§14).

This issue does **not** implement, modify, or reinterpret either Rule
Card's mechanics; it proves the two already-verified production modules
(`ISSUE-004`, `ISSUE-005`) compose correctly when sequenced per the
approved contract (implementation plan §7, §13).

## 2. Approved Inputs/Specifications

- `docs/rules/exploration/dungeon_wandering_monster_check.md` (`EXP-001`),
  Status `VERIFIED` — human-approved 2026-08-18, including Simulator
  Rulings A, B, and C.
- `docs/rules/exploration/dungeon_turn_time_accounting.md` (`EXP-002`),
  Status `VERIFIED` — human-approved 2026-08-16, including its
  long-encounter Simulator Ruling.
- `docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` §7, §9, §11–§13
  (`Status: IMPLEMENTATION PLAN APPROVED`, human-approved 2026-08-18) —
  the approved procedural sequencing contract, the resolved decision that
  no production orchestration module is implemented for this cluster, and
  the five required cross-card integration scenarios this issue
  implements.
- `ARCHITECTURE.md` §15.2 — `CLUSTER-001` historical-rules implementation
  authorized 2026-08-18.
- `ISSUE-003` (`src/rules/exploration/turn_credit.py`) — the shared
  `TurnCredit`/`TurnCreditOrigin` contract composed here, unmodified.
- `ISSUE-004` (`EXP-002`, `src/rules/exploration/dungeon_turn_time_accounting.py`)
  — the real, verified credit producer composed here, unmodified.
- `ISSUE-005` (`EXP-001`, `src/rules/exploration/dungeon_wandering_monster_check.py`)
  — the real, verified cadence/arrival consumer composed here, unmodified.
- Human integration review: integration-test commit
  `c5ab7778650f1db8ea3a80636636bd9353df10bd`; human-review correction
  commit `0a680817a1d7cee4c9d1a0d4f2be9a5aa4f83c1e`. `HUMAN INTEGRATION
  REVIEW: APPROVED`, 2026-08-18.

## 3. Files Created, Modified, or Deleted

**Created:**
- `tests/rules/exploration/test_cluster_001_integration.py` (commit
  `c5ab777`; corrected commit `0a68081`).
- `docs/completion-records/ISSUE-006-cluster-001-cross-card-integration.md`
  (this record).

**Modified:**
- `docs/completion-records/INDEX.md` (adds the `ISSUE-006` row).
- `docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` (§14 Step 4
  completion-record mapping: `Step 4 → ISSUE-006 — Complete`).

These two documentation changes record this already-human-approved
issue's completion/lifecycle state; they do not alter the reviewed test
file or any production mechanic. (`src/rules/exploration/turn_credit.py`,
`dungeon_turn_time_accounting.py`, `dungeon_wandering_monster_check.py`,
and their own tests from `ISSUE-003`/`ISSUE-004`/`ISSUE-005` are
unchanged — `src/` is untouched by this issue in its entirety.)

The broader cluster-level lifecycle closeout (`docs/rules/clusters/CLUSTER-001-dungeon-exploration-time.md`,
`docs/rules/INVENTORY.md`, `ARCHITECTURE.md` §15.2, and the final cluster
completion record itself) is `ISSUE-007`'s own file accounting, not
duplicated here — see `ISSUE-007` for those changes.

**Deleted:** none.

Cumulative accepted branch state: `cluster-001-step-4-integration`
through commit `0a68081` (integration tests `c5ab777` plus human-review
correction `0a68081`).

## 4. Behavior Verified

This issue verifies, rather than implements, mechanical behavior — it
proves the two independently `VERIFIED` production components compose
correctly under the approved Game-Turn procedural sequencing, using the
real production classes directly (no algorithm duplication, no faked
`TurnCredit`, no stand-in for either card):

- **`EXP-002` ordinary credits feed `EXP-001` cadence correctly.**
  `DungeonTimeAccounting.complete_ordinary_turn()`'s returned `TurnCredit`
  passed directly to `WanderingMonsterCadence.advance()` advances the
  tally and, once due, executes a real check.
- **`EXP-002` encounter-derived credits advance `EXP-001` cadence without
  executing wandering checks.** Every credit `resolve_encounter()`
  returns, passed to `advance()` in order, returns
  `CheckOutcome.CADENCE_ADVANCED_ONLY` and consumes zero RNG operations,
  regardless of how far the tally advances past any threshold.
- **Pending wandering arrival is resolved at Game-Turn beginning, before
  ordinary completion.** Every scenario calls `resolve_arrival()` first,
  before any `complete_ordinary_turn()`/`advance()` call for that same
  turn, per the approved sequencing contract (implementation plan §7).
- **An arriving wandering encounter preempts that Game Turn.** When
  `resolve_arrival()` reports `occurred=True`, no ordinary credit is
  produced and `advance()` is not called for that turn (Scenario 1).
- **Long encounters may cross multiple cadence thresholds but produce
  exactly one deferred check at the next valid ordinary step-4
  opportunity.** A 121-round encounter's three encounter-derived credits
  advance the tally to 4 with zero rolls; the next ordinary credit
  executes exactly one roll, resolving all accumulated due-ness at once
  (Scenario 3).
- **Pre-decided skips consume the due period without RNG.** A due
  ordinary credit's `skip_signal=True` call returns `SKIPPED`, consumes
  zero RNG operations, and still resets the tally exactly as a performed
  check would — proven by the following period not becoming due one turn
  early (Scenario 4).
- **Normal/heightened transitions share one cadence state.** The same
  `turns_since_last_check` tally is used across a normal → heightened →
  normal sequence, with no reset merely from entering or leaving
  heightened mode, and no hidden phase restored on return to normal
  (Scenario 5).

**No production orchestration module was required to prove any of the
above.** All five scenarios compose `DungeonTimeAccounting` and
`WanderingMonsterCadence` directly, calling `resolve_arrival()`,
`complete_ordinary_turn()`, `resolve_encounter()`, and `advance()`
themselves in the sequence the approved contract requires — confirming
the implementation plan's own resolved architecture decision (§11, §18)
that a thin orchestration seam (`dungeon_turn_cycle.py`) is not needed at
this stage. The future human-playable exploration driver remains
deliberately deferred (plan §11, "Preserve the future human-playable
architecture") — see §11 below.

## 5. Scenario Evidence

Five scenarios in `tests/rules/exploration/test_cluster_001_integration.py`,
implementing the implementation plan's §13 cross-card integration
scenarios exactly:

- **Scenario 1 — ordinary wandering trigger / arrival preemption.** Two
  ordinary credits (`turn_number` 1, 2); the second is due and a scripted
  roll of `1` triggers, setting `pending_arrival`. The following Game
  Turn's `resolve_arrival()` returns `occurred=True` and clears
  `pending_arrival`. Per the human-review correction (commit `0a68081`),
  the scenario stops at that preemption boundary — it does not continue
  into a fabricated encounter-resolution duration or claim what the next
  ordinary credit's number would be; `CLUSTER-001` does not own that
  downstream procedure.
- **Scenario 2 — ordinary no-trigger.** Two ordinary credits reach a due
  check that does not trigger (`NO_TRIGGER`, scripted roll `4`);
  `pending_arrival` stays `False`; the following Game Turn is not
  preempted and ordinary progression continues normally.
- **Scenario 3 — long encounter crosses cadence.** The decisive
  cross-card collapse proof:
  - credit #1 = `ORDINARY`
  - credit #2 = `ENCOUNTER_DERIVED`
  - credit #3 = `ENCOUNTER_DERIVED`
  - credit #4 = `ENCOUNTER_DERIVED`
  - credit #5 = `ORDINARY`
  - authoritative credits = 5
  - wandering checks executed = 1

  The three encounter-derived credits (from a 121-round encounter,
  `encounter_turn_cost(121) == 3`) advance the tally from 1 to 4 with
  zero RNG operations each. The following ordinary credit executes
  exactly one due check (`NO_TRIGGER`, scripted roll `5`), resetting the
  tally to 0. The full ordered `turn_number`/`origin` sequence across the
  `EXP-002` → `EXP-001` boundary is asserted explicitly, and the total
  authoritative-credits-vs-checks-executed count is asserted explicitly
  as 5 credits to 1 check — not one check per two total credits.
- **Scenario 4 — pre-decided skip.** A due ordinary credit's
  `skip_signal=True` call returns `SKIPPED` with zero RNG operations and
  resets the tally; the following period is not primed one turn early
  (`NOT_DUE`); the period after that is due normally with exactly one
  roll.
- **Scenario 5 — normal → heightened → normal transition.** A normal
  ordinary credit (`NOT_DUE`, tally 1); a heightened credit (due via
  `heightened_checking=True`, `NO_TRIGGER`, one roll, tally resets to 0
  — the normal consequence of the check actually executing, not of
  entering heightened mode); heightened mode ends, and the next ordinary
  credit is `NOT_DUE` with the tally at 1, not reset and not restoring
  any hidden saved phase; the following credit is due under the ordinary
  baseline cadence and executes normally.

RNG-consumption audit: every scenario's `ScriptedRNG` queue is sized to
exactly the number of rolls that scenario's approved mechanics require
(1, 1, 1, 1, and 2 respectively) — an unexpected extra or missing draw
would desynchronize a later expected roll value or exhaust the queue,
either of which fails the test naturally. This is the audit mechanism;
no private RNG-call-count introspection was added or needed.

## 6. Rules Provenance

No rules research, reinterpretation, or new Simulator Ruling occurred in
this issue. Every mechanical fact these scenarios exercise is already
established and approved at the unit level in `EXP-001`
(`docs/rules/exploration/dungeon_wandering_monster_check.md`, Simulator
Rulings A/B/C) and `EXP-002`
(`docs/rules/exploration/dungeon_turn_time_accounting.md`, the
long-encounter Simulator Ruling) — this issue composes those
already-approved mechanics, it does not extend or reconsider them.

## 7. Tests Added or Modified

5 tests in `tests/rules/exploration/test_cluster_001_integration.py`
(`test_scenario_1_ordinary_wandering_trigger`,
`test_scenario_2_ordinary_no_trigger`,
`test_scenario_3_long_encounter_crosses_cadence`,
`test_scenario_4_pre_decided_skip`,
`test_scenario_5_heightened_transition`), implementing the implementation
plan's §13 scenario table exactly. Scenario 1 was corrected during human
review (commit `0a68081`) to stop at the arrival-preemption boundary
instead of continuing into an unowned downstream procedure; Scenario 5's
inline comment was corrected in the same commit to attribute the
post-check tally reset to the executed check itself rather than to
Simulator Ruling B (which governs the unrelated suspended/deferred-check
collapse). No test mechanics changed in Scenarios 2–4.

## 8. Exact Verification Commands Executed

- `uv run python scripts/verify.py` was the intended canonical command.
  `uv` was not available on this session's `PATH` in this environment
  (confirmed absent via `Get-Command`/`where.exe` and a search of common
  install locations); verification was instead executed directly against
  the repository's existing `.venv` (`.venv\Scripts\python.exe
  scripts\verify.py`), which invokes the identical `scripts/verify.py`
  entry point `uv run` would dispatch to, using the same locked
  dependency environment. This substitution is recorded here rather than
  silently presented as the literal `uv` invocation.

## 9. Verification Results

- **Tests:** all project tests passed (160 total: 155 pre-existing + 5
  new).
- **Coverage:** PASS — differentiated gate: `src/rules/` 5 files, 100%
  required per file, met; core aggregate 100.00% (≥95% required). No
  `src/` file's coverage changed from `ISSUE-005`'s figures, since this
  issue adds no production code.
- **Ruff:** clean.
- **mypy --strict:** clean.
- **Overall: PASS.**
- **Feature-branch CI:** PASS (GitHub Actions,
  `cluster-001-step-4-integration` at commit `0a68081`).

## 10. Coverage Results

Unchanged from `ISSUE-005`: `turn_credit.py` 13/13 statements (100%),
2/2 branches (100%); `dungeon_turn_time_accounting.py` 19/19 statements
(100%), 2/2 branches (100%); `dungeon_wandering_monster_check.py` 67/67
statements (100%), 14/14 branches (100%). This issue adds no production
code and changes no `src/` file's coverage.

## 11. Deviations

None from the approved implementation plan. The human-review correction
round (commit `0a68081`) changed one scenario's stopping point and one
inline comment's ruling attribution only — no scenario's mechanics,
assertions substance, or RNG-audit sizing changed as a result, and no
production code was ever touched.

## 12. Known Limitations/Unresolved Issues

`CLUSTER-001`'s verified simulation-facing mechanics still do not supply:

- the real exploration-turn driver that decides *when* a Game Turn
  begins, when player actions complete one, or when an encounter
  resolves, from actual player/DM input;
- encounter/monster determination (`MON-001` onward) or any downstream
  wandering-encounter resolution once `pending_arrival` resolves to
  `occurred=True`;
- movement, searching, or any other exploration activity content
  (`EXP-003`, `EXP-005`, and neighboring cards);
- player commands or any presentation/UI layer.

These are outside `CLUSTER-001`'s approved boundary entirely (plan §3,
§16) — not incomplete `CLUSTER-001` behavior. See `ISSUE-007` for the
cluster-level statement of what is now mechanically available versus
what remains deliberately out of scope.

## 13. Architectural Consequences

None to `ARCHITECTURE.md`'s approved module boundaries. This issue adds
no production module — it confirms, rather than changes, the
implementation plan's resolved architecture decision (§11, §18) that
cross-card sequencing is demonstrated directly through tests composing
the two already-verified rule modules, with no production orchestration
seam required at this stage. `ARCHITECTURE.md` §15.2 receives a
current-status update recording the cluster's overall completion —
`ISSUE-007`'s own accounting, not this issue's.
