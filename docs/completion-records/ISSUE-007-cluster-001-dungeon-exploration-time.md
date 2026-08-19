# ISSUE-007: CLUSTER-001 — Dungeon Exploration Time (Cluster Completion)

## 1. Issue/Task Identifier and Objective

ISSUE-007 (completion-record ledger). Records `CLUSTER-001`'s completion
as a whole, now that all four implementation/integration steps in
`docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` are complete.

**Objective:** implement and verify the approved `CLUSTER-001` boundary,
`EXP-001` + `EXP-002`, establishing authoritative dungeon whole-turn
accounting and wandering-monster cadence/arrival integration.

This record summarizes the completed cluster; it does not duplicate the
four per-step completion records, each of which remains the authoritative
account of its own step's implementation detail:

- [`ISSUE-003`](ISSUE-003-cluster-001-turn-credit-contract.md) — the
  shared `TurnCredit`/`TurnCreditOrigin` contract.
- [`ISSUE-004`](ISSUE-004-exp-002-dungeon-turn-time-accounting.md) —
  `EXP-002`, Dungeon Turn / Time Accounting.
- [`ISSUE-005`](ISSUE-005-exp-001-dungeon-wandering-monster-check.md) —
  `EXP-001`, Dungeon Wandering-Monster Check.
- [`ISSUE-006`](ISSUE-006-cluster-001-cross-card-integration.md) —
  cross-card integration gate.

Per the approved implementation plan §14: "A further, final `CLUSTER-001`
completion/integration record, summarizing the cluster's own integration
gate once all four steps are done, remains a legitimate and useful
addition after step 4 — but it supplements the four per-step records
above; it does not substitute for any of them." This record is that
supplement.

## 2. Approved Inputs/Specifications

- `docs/rules/exploration/dungeon_wandering_monster_check.md` (`EXP-001`),
  Status `VERIFIED` — human-approved 2026-08-18, including Simulator
  Rulings A, B, and C.
- `docs/rules/exploration/dungeon_turn_time_accounting.md` (`EXP-002`),
  Status `VERIFIED` — human-approved 2026-08-16, including its
  long-encounter Simulator Ruling.
- `docs/rules/clusters/CLUSTER-001-dungeon-exploration-time.md`, Current
  section — the human-revalidated two-card cluster boundary
  (`APPROVED`, 2026-08-16).
- `docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` (`IMPLEMENTATION
  PLAN APPROVED`, human-approved 2026-08-18) — the full implementation
  plan this cluster's four steps executed.
- `ARCHITECTURE.md` §15.2 — `CLUSTER-001` historical-rules implementation
  `AUTHORIZED — 2026-08-18` (Rules Baseline Migration Gate, steps 1–4
  satisfied specifically for this boundary).
- `ISSUE-003`, `ISSUE-004`, `ISSUE-005`, `ISSUE-006` — the four completion
  records this record supplements.
- Human cluster-completion review: `HUMAN INTEGRATION REVIEW: APPROVED`
  (Step 4, 2026-08-18).
- **`HUMAN CLUSTER-COMPLETION REVIEW: APPROVED`. Date: 2026-08-18.**
  Human review confirmed that all four `CLUSTER-001`
  implementation/integration steps, their completion records, the final
  cross-card integration gate, and the cluster-level closeout metadata
  satisfy the approved Rule Cards, implementation plan, testing
  requirements, and governance process.

## 3. Files Created, Modified, or Deleted

**Created:**
- `docs/completion-records/ISSUE-007-cluster-001-dungeon-exploration-time.md`
  (this record).

**Modified** (cluster-level lifecycle/closeout metadata sync — does not
alter any reviewed production mechanic, test, or Rule Card content):
- `docs/completion-records/INDEX.md` (adds the `ISSUE-007` row, alongside
  `ISSUE-006`'s own row added for that issue).
- `docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` (a concise later
  implementation-result note recording Steps 1–4 complete and this
  record as the final cluster completion record; historical `Human
  Implementation-Plan Review: APPROVED` text preserved unchanged).
- `docs/rules/clusters/CLUSTER-001-dungeon-exploration-time.md` (current
  section: `CLUSTER-001 Status: VERIFIED`, implementation-progress table
  updated to all four steps `Complete`/`VERIFIED`, pointer to this
  record; preserved Historical 1974-Primary section untouched except
  none — no contradiction requiring a banner update was found there).
- `docs/rules/INVENTORY.md` (`EXP-001`/`EXP-002` row prose updated only
  where it stated `CLUSTER-001` Step 4 or cluster-level completion was
  still outstanding; mechanics/source descriptions for both entries
  unchanged).
- `ARCHITECTURE.md` (§15.2: a concise later current-status update
  recording `CLUSTER-001` implementation/integration as `VERIFIED —
  2026-08-18`; the Rules Baseline Migration history and the original
  2026-08-18 implementation authorization preserved unchanged; general
  Pre-Code/cluster gates preserved, not lifted).

**Deleted:** none.

No `src/` or `tests/` file is touched by this issue — this is a
documentation-closeout record only.

## 4. Behavior Now Available

The verified `CLUSTER-001` boundary can now mechanically represent:

- completed ordinary dungeon turn → authoritative ordinary `TurnCredit`;
- completed encounter → authoritative ordered encounter-derived
  `TurnCredit` sequence;
- all credits (either origin) → wandering-cadence advancement;
- a valid ordinary step-4 opportunity → a due wandering check;
- a successful check → a pending wandering arrival;
- the beginning of a later Game Turn → arrival resolution / Game-Turn
  preemption.

**The project cannot yet:** choose which wandering monster appears; run
the resulting encounter; accept player movement/actions; execute a full
dungeon Game Turn automatically; or provide a playable UI. Those remain
outside `CLUSTER-001`'s approved boundary — see §6 and each per-step
record's own "Known Limitations" for detail.

## 5. Rules Provenance

Both constituent Rule Cards are independently `VERIFIED`:

- `EXP-001` — `docs/rules/exploration/dungeon_wandering_monster_check.md`.
- `EXP-002` — `docs/rules/exploration/dungeon_turn_time_accounting.md`.

Per each card's own Provenance Classification, this cluster's mechanics
are drawn from three distinct provenance tiers, preserved distinctly and
not conflated by this record:

- **Rules Cyclopedia Explicit** — the baseline/heightened cadence, the
  1d6 trigger and heightened chance-level range, trigger-vs-arrival
  timing, the pre-decided skip input, one credit per completed ordinary
  Game-Turn-Checklist iteration, and the two-mode (turn/round) structure.
- **Necessary Mechanical Consequence** — that only an ordinary credit can
  represent an executing step-4 check opportunity.
- **Simulator Rulings A, B, and C** (human-approved 2026-08-18) —
  encounter-credited-turn cadence participation (A); deferred execution
  and collapse of accumulated due-ness during a suspended checklist (B);
  the heightened-checking shared-counter transition behavior (C). Each
  implemented, and now cross-card-verified, exactly as approved — none
  reopened, reinterpreted, or extended by this record or by the Step 4
  integration gate.

No rule was re-researched, reinterpreted, or newly ruled upon in
completing this cluster.

## 6. Architectural Consequence

**Already-approved architectural result, not a new decision:**
`CLUSTER-001` proves direct rules-component composition without
requiring a production orchestration abstraction. The five Step-4
integration scenarios (`ISSUE-006`) compose `DungeonTimeAccounting` and
`WanderingMonsterCadence` directly, with no intervening `Player`,
`Command`, `Dungeon`, `Party`, `ExplorationEngine`, `TurnManager`,
`DungeonTurnCycle`, or `GameState`-shaped module. The eventual
human-playable exploration driver remains deferred until movement/actions
(`EXP-003`/`EXP-005`, a future cluster) and the surrounding exploration
responsibilities make that orchestration layer's responsibility concrete
(implementation plan §11, "Preserve the future human-playable
architecture"). `CLUSTER-001` supplies verified simulation-facing
mechanics; it does not yet provide the player-facing exploration loop or
a production Game-Turn orchestrator. No such code is created by this
record or by any step of this cluster.

## 7. Verification Summary

Each step's own exact verification commands and results are recorded in
its own completion record (`ISSUE-003` §7–§9, `ISSUE-004` §7–§9,
`ISSUE-005` §7–§9, `ISSUE-006` §8–§10). At cluster completion:

- **Tests:** 160/160 passing (the full project suite, including all 5
  Step-4 integration scenarios).
- **Coverage:** PASS — differentiated gate met for all 5 `src/rules/`
  files (100% required per file); core aggregate 100.00% (≥95%
  required).
- **Ruff:** clean.
- **mypy --strict:** clean.
- **Overall: PASS.**
- **Feature-branch CI:** PASS (`cluster-001-step-4-integration` at
  commit `0a68081`, and this closeout commit).

See `ISSUE-006` §8 for the one environment note recorded during Step 4
verification (canonical command intent vs. the `.venv`-direct invocation
actually used in that session).

## 8. Deviations

None from the approved implementation plan across any of the four steps.
Each step's own completion record documents that step's (absence of)
deviation individually; nothing is superseded or corrected by this
cluster-level record.

## 9. Known Limitations/Unresolved Issues (Cluster Level)

`CLUSTER-001`'s verified boundary still does not supply:

- the real exploration-turn driver (movement/action-driven Game-Turn
  orchestration);
- encounter/monster determination (`MON-001` onward) or any downstream
  wandering-encounter resolution;
- movement, searching, or other exploration-activity content
  (`EXP-003`, `EXP-005`, and neighboring cards);
- player commands;
- presentation/UI.

These are outside this cluster's approved two-card boundary (plan §3,
§16) — not incomplete `CLUSTER-001` behavior. `EXP-004` (Resting
Procedure) remains excluded from this cluster and remains
`REVALIDATION_REQUIRED`; it is not affected by, and does not affect,
this cluster's completion.

## 10. Architectural Consequences

See §6 above. No `ARCHITECTURE.md` module-boundary change results from
cluster completion — only a current-status recording in §15.2 that this
authorized boundary's implementation is now complete and verified. The
general Pre-Code Development Gate (§16) and the per-cluster Rules
Baseline Migration Gate requirement (§15.2) remain in force, unweakened,
for every other cluster and Rule Card; this record does not select,
authorize, or begin any other cluster.
