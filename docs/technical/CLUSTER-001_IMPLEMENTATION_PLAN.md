# CLUSTER-001 — Implementation / Integration Preparation Plan

## 1. Status / Purpose

**This document is a technical implementation plan. It is not a Rule Card, not a new rules authority, and not itself an authorization to implement.** It translates the two `APPROVED` Rule Cards that make up `CLUSTER-001`'s boundary into a precise, human-reviewable plan another agent can execute without making rules decisions, per `ARCHITECTURE.md` §15.1's cluster workflow and `docs/decisions/DEC-0005-v1-rules-inventory-and-clustered-implementation.md`.

**No production code is written by this document or this task.** `src/` and `tests/` are untouched. This document does not begin implementation, does not add placeholder classes, and does not add test skeletons — it specifies what those would need to contain.

**Mechanics cited below are extracted, not reinterpreted.** Every mechanical statement in §4–§9 is sourced to a specific clause of `docs/rules/exploration/dungeon_wandering_monster_check.md` (`EXP-001`) or `docs/rules/exploration/dungeon_turn_time_accounting.md` (`EXP-002`), both `Status: APPROVED`. Where this plan proposes a *representation* (a class, a field, a module path) rather than a *mechanic*, that is called out explicitly as an implementation-shape choice, distinguishable from rules content. Historical (1974-primary) sections of either card are provenance only and are not used as a source of current mechanics anywhere below.

**Human Implementation-Plan Review: APPROVED.**

- **Date:** 2026-08-18
- **This plan is approved as the authoritative implementation plan for `CLUSTER-001`.**
- **Approval authorizes production implementation only after the `ARCHITECTURE.md` §15.2 Rules Baseline Migration Gate is synchronized to record `CLUSTER-001` implementation readiness as re-approved.** (Synchronized the same day this approval was recorded — see `ARCHITECTURE.md` §15.2's "Status update (2026-08-18)" for the resulting authorization record.)
- **Resolved orchestration decision, confirmed unchanged by this approval:** Production Game-Turn orchestration is deliberately deferred until movement/actions and related exploration responsibilities create a real exploration-turn driver. `CLUSTER-001` will implement only its approved simulation-facing rules components and will verify their integration through direct deterministic composition tests (§11, §13).
- This approval does not alter this plan's mechanics, module design, test plan, or implementation sequence (§4–§16 unchanged in substance).

**Ending recommendation:** `IMPLEMENTATION PLAN APPROVED` — see §19.

---

## 2. Authoritative Inputs

Read in full for this plan:

- `GAME_CONSTITUTION.md`
- `ARCHITECTURE.md`
- `AGENTS.md`
- `DEVELOPMENT_WORKFLOW.md`
- `TESTING_STRATEGY.md`
- `CLAUDE.md`
- `docs/decisions/DEC-0005-v1-rules-inventory-and-clustered-implementation.md`
- `docs/rules/clusters/CLUSTER-001-dungeon-exploration-time.md` (Current section only — the preserved Historical 1974-primary section, including its own embedded forward-looking "Cluster 2"-shaped material referencing `EXP-004`, is not authoritative for this plan's scope; see §3)
- `docs/rules/exploration/dungeon_wandering_monster_check.md` (`EXP-001`, `APPROVED`, human-approved 2026-08-18)
- `docs/rules/exploration/dungeon_turn_time_accounting.md` (`EXP-002`, `APPROVED`, human-approved 2026-08-16)
- `docs/technical/RNG_CONTRACT.md`
- `docs/technical/TOOLCHAIN_AND_CI.md`

Repository state inspected: `src/rng/` (the only existing production code — `RNG` Protocol, `SeededRNG`, `ScriptedRNG`, `RollResult`, dice-expression parsing, error types) and `tests/rng/`. No `src/rules/`, `src/state/`, `src/survivability/`, or `src/events/` exists yet — this cluster is the first work to populate `src/rules/`.

---

## 3. Cluster Responsibility Boundary

`CLUSTER-001`'s current, authoritative boundary (per `docs/rules/clusters/CLUSTER-001-dungeon-exploration-time.md`, Current section) is exactly **two** Rule Cards: `EXP-001` + `EXP-002`. `EXP-004` is explicitly excluded (still `REVALIDATION_REQUIRED`). This plan targets that two-card boundary only.

**Note on an inconsistency in `CLUSTER-001-dungeon-exploration-time.md`.** That document's preserved Historical 1974-Primary section contains later material (its own §§4, 9–15 area) written as though a three-item `EXP-001`+`EXP-002`+`EXP-004` boundary and a broader "advance authoritative dungeon exploration time through movement and mandatory rest" scope were current. That material predates, and is inconsistent with, the Current section's own two-item boundary and this task's explicit instruction (`EXP-001` + `EXP-002` only). This plan treats the Current section as authoritative and does not use that historical material to shape scope. This inconsistency is not resolved by this task (out of scope; flagged for a future documentation-consistency pass, not an architecture or rules decision).

This cluster does **not** implement, and this plan does not design:

- `MON-001` (wandering monster determination), `MON-002` (Number Appearing), `ENC-001` (encounter distance), `ENC-002` (surprise), `ENC-003` (reaction) — all explicitly out of `EXP-001`'s own scope (`EXP-001` "Responsibility Boundary").
- `EXP-008` (dungeon stocking) or the `MON-001` ↔ `EXP-008` circularity — not investigated or resolved by either card or this plan.
- `EXP-004` (rest-related exploration responsibility) — excluded from this cluster's boundary.
- `EXP-003`/`EXP-005` (movement, search) or any other activity that might cause an ordinary Game Turn to complete — `EXP-002`'s own card is explicit that it does not need or accept per-activity turn costs; this cluster treats "an ordinary Game-Turn-Checklist iteration completed" and "an encounter resolved, having taken *N* rounds" as opaque external signals, not something it generates.

`EXP-001` produces only a trigger/arrival fact for downstream encounter handling. It does not select a monster, roll reaction, or begin combat.

---

## 4. Mechanical Contract Extraction

### 4.1 `EXP-002` — Time Accounting

| Behavior | Extracted rule | Card citation |
|---|---|---|
| Ordinary completed Game-Turn-Checklist iterations | Each produces exactly **one** whole-turn credit. | "Approved Mechanical Specification," "Turn-credit accounting" |
| Encounter/round-mode | No dungeon-turn credit is produced while round-mode resolution is in progress. `EXP-002` is not consulted mid-encounter. | Same section, bullet 3 |
| When encounter-derived credit becomes authoritative | Only once the encounter's round-mode resolution has **finished** — computed as a single event, not progressively during combat. | Same section, bullet 2 |
| Long-encounter calculation | `encounter_turn_cost = max(1, ceiling(encounter_rounds / 60))`. For `encounter_rounds ≤ 60` this is always exactly `1`, identical to RC's explicit minimum. | "Simulator Ruling" (human-approved 2026-08-16) |
| Ordering of multiple credits | When an encounter produces more than one credit, those credits remain **individually distinguishable and correctly ordered** — never collapsed into one opaque multi-turn event. | "Approved Mechanical Specification," bullet 4 |
| Distinguishability of origin | Whether a credit arose from an ordinary iteration or an encounter's resolution remains distinguishable information; `EXP-002` does not discard it. `EXP-002` itself does not decide how a consumer uses that distinction. | Same section, bullet 6; "Integration with `EXP-001`" |
| Absence of mid-encounter credit production | Explicit — see round/encounter row above. Also: turn-credits are strictly ordered and cumulative across a session, with no reset and no gap when turn-mode resumes after an encounter. | Same section, bullets 3, 5 |
| No fractional ledger | Turn-credits are whole numbers only; `EXP-002` performs no fractional-turn accumulation. (The Historical section's fractional-ledger accumulator model is 1974-primary provenance only and is **not** current mechanics — explicitly disclaimed by the card's own migration banner.) | "Approved Mechanical Specification," "No fractional/rational ledger is maintained" |
| No RNG | `EXP-002` performs no die rolls and must not be given its own RNG stream. | Same section, "No RNG owned by this card" |
| Survivability | Out of scope; must not accept a survivability policy. | Same section, "Survivability out of scope" |

### 4.2 `EXP-001` — Wandering-Monster Cadence

| Behavior | Extracted rule | Card citation |
|---|---|---|
| Ordinary baseline cadence | Every **two** credited turns, a check may become due. | "Rules Cyclopedia Explicit" item 1 |
| Heightened cadence | When active, due after **every** credited turn instead of every two. | "Heightened-checking input" (as corrected in the 2026-08-18 approval round) |
| Baseline probability | 1d6; result of exactly `1` triggers. | "Rules Cyclopedia Explicit" item 2 |
| Heightened probability | One of {1-in-6, 2-in-6 (1-2), 3-in-6 (1-3), 4-in-6 (1-4)} on 1d6, externally supplied. | "Rules Cyclopedia Explicit" item 7, corrected reading |
| Cadence advancement by all credits | **Every** completed whole-turn credit — ordinary or encounter-derived — advances the cadence tally by one. | **Simulator Ruling A**, human-approved 2026-08-18 |
| Cadence advancement vs. check execution | Only an **ordinary** credit, produced by an actually-executing Game-Turn-Checklist iteration, can represent step 4 and therefore execute a roll. An encounter-derived credit can never itself execute a check. | Necessary Mechanical Consequence, "Approved Mechanical Specification" |
| Deferred due checks / collapse | When the threshold is crossed by encounter-derived credits during a suspended checklist, execution defers to the next ordinary credit's step-4 opportunity; that single execution resolves **all** accumulated due-ness. Additional crossings during the same suspension do not create additional checks — the resulting actual check rate can be **lower** than one check per two total credits; this is intentional, not a defect. | **Simulator Ruling B**, human-approved 2026-08-18 (precise interpretation) |
| Pre-decided skip | An externally supplied "already decided for this period" signal, honored only at an ordinary credit's due-moment: skips the roll, consumes zero RNG operations, and still resets the tally as a performed roll would. | "Rules Cyclopedia Explicit" item 6; "DM-discretion skip input" |
| RNG consumption | Exactly one rules-visible 1d6 roll per **executed** check; zero for not-due, skipped, encounter-derived-credit-only, or arrival resolution. | "RNG usage" |
| Positive trigger scheduling | A triggering check does **not** itself resolve arrival — it sets `pending_arrival := true` only. | "Rules Cyclopedia Explicit" item 3; "Approved Mechanical Specification," Procedure A |
| Beginning-of-next-Game-Turn arrival | Arrival is resolved at the **beginning** of the immediately following Game Turn, before that turn's own Actions/Results/step-4 check — a distinct procedural moment from "a credit was completed." | "Rules Cyclopedia Explicit" item 3; Procedure B |
| Pending-arrival sequencing | `pending_arrival` is a sufficient single boolean under valid execution sequences (Procedure B before that same turn's own Procedure A) — proven, not assumed, in the card's own invariant proof; the proof is explicitly scoped to that valid ordering and does not claim to defend against malformed sequencing. | "Invariant" subsection, "Approved Mechanical Specification" |
| Arrival preempts the remainder of that Game Turn Checklist | On arrival, that turn's own Actions/Results/step-4 check do not occur at all. | "Rules Cyclopedia Explicit" item 4 |
| Shared normal/heightened cadence tally | One shared counter (`turns_since_last_check`) for both; it resets when an ordinary due period is resolved — either a performed wandering-monster check, or the approved pre-decided-period skip — but never merely because heightened checking activates or deactivates. | **Simulator Ruling C**, human-approved 2026-08-18 (transition behavior); "Rules Cyclopedia Explicit" item 6 (skip-resolution reset) |

**Simulator Rulings A, B, and C are preserved as mechanics by this plan, exactly as approved. They are not reopened, reinterpreted, or reconsidered here.**

---

## 5. Required Authoritative State

State concepts, identified mechanically before any class design:

| Concept | Owning Rule Card | Why mechanically necessary | Mutable | Lifetime | Valid values | Invariants | Explicitly NOT responsible for |
|---|---|---|---|---|---|---|---|
| Turn-credit origin | `EXP-002` (produces the distinction); consumed by `EXP-001` | `EXP-001`'s execution-eligibility rule (§4.2) requires distinguishing ordinary from encounter-derived credits. | N/A (value) | Value type, no lifetime | Exactly two values: ordinary, encounter-derived | Closed set of two | Encoding round count, cadence state, or check outcome |
| Turn credit | `EXP-002` | `EXP-001`'s own "Dependencies" section requires "an absolute turn number per credit... strictly ordered." | No (immutable value) | Ephemeral — produced per elapsed turn, consumed by the next stage | `turn_number` a positive int, strictly increasing and gapless across a session; origin one of the two values above | Never produced during round-mode (an orchestration-level guarantee this type cannot self-enforce — see §11) | Which activity produced it; encounter details; cadence/check state |
| Dungeon-turn counter | `EXP-002` | "Maintains an authoritative, discrete... dungeon-turn counter" (Scope) | Yes | Per campaign/exploration session | Non-negative int, monotonically increasing | Advances by exactly 1 per ordinary credit, or by `encounter_turn_cost` per resolved encounter; never decreases, never skips | Wandering-check cadence, RNG, arrival |
| Wandering cadence tally (`turns_since_last_check`) | `EXP-001` | Baseline/heightened due-ness both depend on it (§4.2) | Yes | Per campaign/exploration session | Non-negative int, unbounded | Advances by exactly 1 per credit received (any origin — Simulator Ruling A). Resets to 0 when an ordinary due period is resolved: either a performed wandering-monster check, or the approved pre-decided-period skip ("Rules Cyclopedia Explicit" item 6 / "DM-discretion skip input") — both consume the due period identically. Unaffected by heightened checking's own activation or deactivation alone (Simulator Ruling C). | Die results, RNG, arrival |
| Pending arrival (`pending_arrival`) | `EXP-001` | Trigger-vs-arrival is a distinct procedural moment (§4.2) | Yes | Per campaign/exploration session | `{True, False}` | Proven sufficient as a single boolean under valid execution sequencing (§4.2) | Monster identity, distance, arrival details beyond the fact |
| Heightened-checking frequency flag | Externally supplied; `EXP-001` only consumes it | `EXP-001` explicitly does not decide which upstream condition sets it | See §6 | Per call (recommended) or per session (if a future policy layer needs push semantics) | `{True, False}` | None owned by `EXP-001` | Deciding when it is true |
| Heightened chance level | Externally supplied; `EXP-001` only consumes it | Same as above — magnitude of the heightened trigger range | See §6 | Same as above | One of `{1, 2, 3, 4}` (representing 1-in-6 … 4-in-6); meaningful only when the frequency flag is true; ignored/defaulted otherwise | Defaults to baseline (`1`) when heightened checking is inactive | Deciding which level a given condition warrants |
| Pre-decided skip signal | Externally supplied; `EXP-001` only consumes it | "Rules Cyclopedia Explicit" item 6 | Per call | Per due-check evaluation only | `{True, False}` | Evaluated only when a roll would otherwise occur (ordinary credit, due, not encounter-derived) | Deciding *when* to assert it |

No state item is added merely because it might be useful later — the table above is the complete set the two approved cards require.

---

## 6. `EXP-002` → `EXP-001` Interface (Turn-Credit Contract)

**Contract, restated as an interface requirement:** a whole-turn credit is authoritative, ordered, and distinguishable by origin, and `EXP-001` must be able to tell, for each credit it receives, whether that credit is eligible to represent a step-4 check opportunity.

**Proposed smallest representation** (implementation-shape, not a rules decision):

```text
TurnCreditOrigin — a closed two-value enumeration: ORDINARY, ENCOUNTER_DERIVED

TurnCredit — an immutable value object:
    turn_number : positive int, strictly increasing and gapless across a session
    origin      : TurnCreditOrigin
```

This is deliberately not a generalized event type. It carries only the two facts both cards require the interface to carry (§4.1 "Distinguishability of origin"; `EXP-001` "Dependencies": "an absolute turn number per credit, ordinary-vs-encounter-derived origin distinguishable, strictly ordered"). No round-count, timestamp, or activity data is attached — those remain `EXP-002`'s internal concern (round count is consumed as an *input* to compute `encounter_turn_cost`, never re-exposed on the credit itself) or another card's concern entirely.

**Where this type lives (recommendation, not a rules or architecture decision):** a small shared module (§8) rather than embedding it in either card's own module, because it is a contract *between* the two cards, owned by neither individually. `EXP-002`'s module depends on it to produce credits; `EXP-001`'s module depends on it to consume them; `EXP-002`'s module is never imported by `EXP-001`'s module (see §9 dependency direction) — sharing the type through its own tiny module avoids forcing that unwanted import. A reviewer who prefers fewer files may instead define this type inside `EXP-002`'s own module with no mechanical difference; this plan's recommendation is a file-count/import-direction convenience, not something requiring escalation.

**No generalized event system.** Nothing here proposes a turn-credit *stream* type, a publish/subscribe mechanism, or a generic event bus — `TurnCredit` is a plain returned/passed value, matching both cards' own explicit "this card does not prescribe a software event/API architecture" language.

---

## 7. Procedural Sequencing

Per §4.2 and the task's own instruction, these three procedural moments are kept distinct and are not collapsed into one operation.

### 7.1 Moment A — Beginning of a new Game Turn

`EXP-001` must resolve any pending arrival **before** that turn's own Actions/Results/step-4 proceed. This is Procedure B in the Rule Card. Proposed shape: a method with no credit input (it is not triggered by a completed credit at all):

```text
WanderingMonsterCadence.resolve_arrival() -> ArrivalResult

    IF pending_arrival is true:
        pending_arrival := false
        return ArrivalResult(occurred=True)
        # caller must not proceed with this turn's own Actions/Results/step-4;
        # the Game Turn Checklist is left for the Encounter Checklist instead
    ELSE:
        return ArrivalResult(occurred=False)
        # caller proceeds with this turn's own Actions/Results, and — once
        # that iteration completes — reports the resulting ordinary credit
        # through Moment B
```

### 7.2 Moment B — Completion of an ordinary Game Turn

Produces one ordinary `TurnCredit` (`EXP-002`) and, because that credit is ordinary, may permit a due wandering check (`EXP-001`). Proposed shape:

```text
credit = DungeonTimeAccounting.complete_ordinary_turn() -> TurnCredit   # origin=ORDINARY

result = WanderingMonsterCadence.advance(
    credit, skip_signal=..., heightened_checking=..., heightened_chance_level=..., rng=...
) -> WanderingCheckResult
```

`advance()` is Procedure A, split internally by `credit.origin` exactly as the card requires (§4.2, "Cadence advancement vs. check execution").

### 7.3 Moment C — End of an encounter

`EXP-002` computes `encounter_turn_cost = max(1, ceiling(encounter_rounds / 60))` ordered encounter-derived credits, only once round-mode resolution has finished:

```text
credits = DungeonTimeAccounting.resolve_encounter(encounter_rounds) -> tuple[TurnCredit, ...]  # all origin=ENCOUNTER_DERIVED

FOR each credit IN credits, IN ORDER:
    result = WanderingMonsterCadence.advance(credit, ...)
    # each call advances the tally only; none executes a roll or sets
    # pending_arrival (Simulator Ruling B) — due-ness, if any, is left
    # for the next ordinary credit's own Moment B call
```

**These three moments must not be accidentally called in the wrong order or collapsed.** In particular: Moment A must run, and be allowed to preempt, before Moment B's own credit is even produced for that turn — a caller must not call `complete_ordinary_turn()` for a turn whose own `resolve_arrival()` has not yet been checked. This ordering requirement is stated as an explicit orchestration contract (§11), not defended against inside `WanderingMonsterCadence` itself (§8 below).

**No software event bus is introduced merely because these are three distinct moments.** They are three plain method calls made in a specific required order by whatever orchestrates a Game Turn (§11) — not three subscribers to a published event.

---

## 8. Proposed Module/File Structure

| Path | Responsibility | Authoritative Rule Card(s) | Public mechanical contract | Dependencies | Forbidden dependencies | State owned | State not owned |
|---|---|---|---|---|---|---|---|
| `src/rules/exploration/turn_credit.py` | Shared value types for the `EXP-002` → `EXP-001` interface (§6) | `EXP-001`, `EXP-002` (contract between them; owned by neither's mechanics alone) | `TurnCreditOrigin`, `TurnCredit` | None (stdlib `enum`, `dataclasses` only) | Neither Rule Card module; no RNG | None (pure value types) | Everything mechanical |
| `src/rules/exploration/dungeon_turn_time_accounting.py` | `EXP-002`'s full contract: the dungeon-turn counter, ordinary-turn credit production, encounter-turn-cost calculation, encounter-derived credit production | `EXP-002` | `DungeonTimeAccounting` class; `encounter_turn_cost(encounter_rounds: int) -> int` helper, tested independently of the class per §4.1's formula | `turn_credit` | `dungeon_wandering_monster_check`; `src/rng` (this card owns no RNG); `src/survivability` | The dungeon-turn counter | Wandering-check cadence, RNG, arrival |
| `src/rules/exploration/dungeon_wandering_monster_check.py` | `EXP-001`'s full contract: cadence tally, due-ness, execution eligibility, the 1d6 roll, pending-arrival state and resolution | `EXP-001` | `WanderingMonsterCadence` class (`advance()` = Procedure A, `resolve_arrival()` = Procedure B); `WanderingCheckResult`, `CheckOutcome`, `ArrivalResult` | `turn_credit`; `src/rng` (`RNG` Protocol only — never a concrete implementation) | `dungeon_turn_time_accounting` (per `EXP-001`'s own "Dependencies": depends on the credit sequence only, not `EXP-002`'s internal mechanics); `src/survivability` | The cadence tally, `pending_arrival` | Turn-counting, encounter-cost calculation |

**No production orchestration module is proposed for `CLUSTER-001`.** Per human architecture decision (§11), `src/rules/exploration/dungeon_turn_cycle.py` — a proposed thin orchestration seam sequencing the three moments in §7 — is **not** implemented in this cluster. Neither Rule Card's own mechanics require it: cross-card sequencing (§7) is instead demonstrated directly by tests composing `DungeonTimeAccounting`, `WanderingMonsterCadence`, and `TurnCredit` according to the approved sequencing contract (§12/§13), with no intervening production wrapper. A production driver that determines *when* the three moments actually occur is a distinct, larger responsibility deferred to a future exploration-turn driver (§11).

```text
src/
    rules/
        __init__.py
        exploration/
            __init__.py
            turn_credit.py
            dungeon_turn_time_accounting.py
            dungeon_wandering_monster_check.py
tests/
    rules/
        exploration/
            test_turn_credit.py
            test_dungeon_turn_time_accounting.py
            test_dungeon_wandering_monster_check.py
            test_cluster_001_integration.py    # cross-card integration scenarios, §13 —
                                                #  composes the two production modules above
                                                #  directly; no production orchestration module
```

This mirrors the existing `docs/rules/exploration/` naming (one module per Rule Card slug) and `ARCHITECTURE.md` §13's `src/rules/` bucket. No `engine`, `generation`, `world`, `application/`, or `presentation/` layer is created — consistent with §13's explicit deferral of those boundaries "until the codebase demonstrates a real need for them," and with the human decision in §11 that this cluster does not yet supply that need. No `src/events/` module is created; `advance()`/`resolve_arrival()`/`complete_ordinary_turn()`/`resolve_encounter()` return values are the authoritative outcome for now, consumed directly by callers and tests. Structured-event emission (`ARCHITECTURE.md` §8's illustrative `DungeonTurnElapsed`/`WanderingEncounterTriggered`) is deferred until a real consumer (presentation, logging, persistence) exists to need it — introducing it now would be exactly the "generic event system... unless the current architecture already requires one" this task instructs against.

---

## 9. Dependency Direction

```text
turn_credit.py
      ↑                  ↑
      │                  │
dungeon_turn_time_    dungeon_wandering_
accounting.py          monster_check.py  ──→  src/rng (RNG Protocol only)
      ↑                  ↑
      └──────┬───────────┘
             │
  tests/rules/exploration/test_cluster_001_integration.py
  (the only place both Rule Card modules are composed together —
   a test module, not a production module; see §11)
```

- `EXP-002`'s module has **no** dependency on `EXP-001`'s module, matching `CLUSTER-001-dungeon-exploration-time.md`'s explicit one-way integration relationship ("`EXP-002` → elapsed-turn signal → `EXP-001`... not the reverse").
- `EXP-001`'s module has **no** dependency on `EXP-002`'s module — only on the shared `turn_credit` type, matching `EXP-001`'s own "Dependencies" section ("does not depend on `EXP-002`'s internal accounting mechanics — only on the credit sequence itself").
- Neither Rule Card module depends on `src/state`, `src/survivability`, `src/events`, or any presentation/narrative code — all either do not exist yet or are structurally forbidden (`ARCHITECTURE.md` §10/§11; both cards' own "Survivability out of scope" clauses).
- **No production module imports both Rule Card modules** — per the human decision in §11, that composition exists only in the integration test module for this cluster; a future production orchestrator, when one is actually needed, is a distinct, later responsibility (§11, §16).
- `src/rng` remains a leaf dependency, consistent with its existing role — no rules module is imported by it.

---

## 10. RNG Integration

Uses the already-approved abstraction (`src/rng`) exactly as it exists today; nothing about it is redesigned.

- `WanderingMonsterCadence.advance()` accepts an `RNG` (the existing Protocol — `roll_die`/`roll`, satisfied by both `SeededRNG` and `ScriptedRNG`) as a call parameter, not a constructor-injected/owned instance — the campaign/simulation owns the one shared RNG stream (`ARCHITECTURE.md` §5); `EXP-001`'s tracker does not own or construct an RNG of its own.
- **Exactly one** `rng.roll_die(6)` call occurs, and only when a check actually executes: an ordinary credit, due, and no pre-decided skip signal present.
- **Zero** RNG operations occur for: a not-yet-due ordinary credit; a skipped check; any encounter-derived credit (cadence-advance-only branch); `resolve_arrival()` (Procedure B never rolls).
- The resulting `RollResult` (with its existing `sequence_number`, `dice`, `total`, etc.) is embedded directly in the returned `WanderingCheckResult`, mirroring `RNG_CONTRACT.md` §10's pattern of embedding roll results in the structured outcome a rules procedure produces — adapted here to a returned value rather than an emitted event, since no event layer exists yet (§8). This is the sole audit path; no second randomness path or duplicate roll is introduced.
- `EXP-002`'s module never touches `RNG` at all — it is purely arithmetic/counting (§4.1), consistent with its own "No RNG owned by this card" clause.
- No retry/reroll logic anywhere in either module — neither card specifies one, and `RNG_CONTRACT.md` §8 forbids implementation-convenience rerolls.

---

## 11. Orchestration — Where Moments A/B/C Are Sequenced (Resolved Human Decision)

Neither Rule Card designs, and `ARCHITECTURE.md` does not yet define, the code that:

1. knows when a Game Turn is beginning (Moment A trigger);
2. decides when an ordinary Game-Turn-Checklist iteration has "completed" (Moment B trigger — driven, ultimately, by real movement/search/rest content this cluster does not implement, per §3);
3. decides when an encounter has "resolved" with a known round count (Moment C trigger);
4. enforces that Moment A's `resolve_arrival()` call happens before that same turn's own Moment B `advance()` call.

`EXP-001`'s own card names this explicitly as "a future implementation-time design question, not a rules-content question" (Open Questions item 7) and states the required *ordering contract* without designing the mechanism.

**`RESOLVED` — production Game-Turn orchestration deferred until a real exploration-turn driver exists; `CLUSTER-001` integration is verified directly through the approved rule-module contracts.**

The immediately prior draft of this plan proposed a thin production orchestration module (`dungeon_turn_cycle.py`) to sequence Moments A/B/C. Human review determined that module is unnecessary at this stage: the four responsibilities listed at the top of this section (knowing when a Game Turn begins; deciding when player actions complete one; deciding when an encounter resolves; enforcing call order) show it would not itself determine any of that timing from player/DM intent — its only realistic caller at this stage is the deterministic integration-test harness. A production wrapper with no independent simulation responsibility of its own is not warranted merely to give the two Rule Card modules a shared caller.

**Consequence for this plan:**

- **No production orchestration module is implemented in `CLUSTER-001`.** §8/§9/§13/§14 are corrected accordingly.
- **Cross-card sequencing is instead demonstrated by tests** (`tests/rules/exploration/test_cluster_001_integration.py`, §12/§13) that compose `DungeonTimeAccounting`, `WanderingMonsterCadence`, and `TurnCredit` directly, calling `resolve_arrival()` (Moment A), `complete_ordinary_turn()` + `advance()` (Moment B), and `resolve_encounter()` + `advance()` (Moment C) themselves, in the order the approved sequencing contract requires (§7). No production orchestrator is needed to test the contract — the test *is* the composition.
- This is **not** a rejection of an eventual Simulation Engine or Game-Turn orchestration layer. It is a deliberate deferral: that responsibility becomes concrete once a real exploration-turn driver exists (§16, "Preserve the future human-playable architecture," below) — not before.

### Preserve the future human-playable architecture

`CLUSTER-001`'s rules modules are simulation-facing mechanical components, not the final player interface. A future exploration-turn driver will consume player/DM intent, determine when the Game Turn Checklist's procedural moments occur, invoke these approved rules components in the required order, mutate authoritative simulation state, and expose outcomes downstream to presentation. Its exact package/API is deliberately deferred until movement/actions and related exploration responsibilities (`EXP-003`/`EXP-005`, a future cluster) make that orchestration concrete. This plan does not create that driver now, and does not create `engine/`, `application/`, or `presentation/` merely to record this future responsibility — those remain correctly deferred per `ARCHITECTURE.md` §13 until a real need for them exists.

---

## 12. Deterministic Unit-Test Traceability Matrix

Derived directly from each Rule Card's own "Deterministic Test Cases" section — no test below is invented from an imagined implementation detail not already required by an approved clause.

### 12.1 `EXP-002` (source: `dungeon_turn_time_accounting.md`, "Deterministic Test Cases," 15 cases)

| Test ID | Approved behavior | Inputs/state | Expected mechanical result | RNG expectation | Proposed location |
|---|---|---|---|---|---|
| EXP002-01 | Single ordinary turn | One `complete_ordinary_turn()` call | Exactly one credit, `origin=ORDINARY` | None | `test_dungeon_turn_time_accounting.py` |
| EXP002-02 | Sequence of ordinary turns | Five `complete_ordinary_turn()` calls | Five credits, strictly increasing `turn_number`, no gaps | None | same |
| EXP002-03 | 1-round encounter | `resolve_encounter(1)` | 1 credit (`max(1, ceil(1/60))=1`) | None | same |
| EXP002-04 | 4-round encounter | `resolve_encounter(4)` | 1 credit | None | same |
| EXP002-05 | 59-round encounter | `resolve_encounter(59)` | 1 credit (boundary below 60) | None | same |
| EXP002-06 | 60-round encounter | `resolve_encounter(60)` | 1 credit (boundary at 60) | None | same |
| EXP002-07 | 61-round encounter | `resolve_encounter(61)` | 2 credits (boundary just above 60) | None | same |
| EXP002-08 | 120-round encounter | `resolve_encounter(120)` | 2 credits | None | same |
| EXP002-09 | 121-round encounter | `resolve_encounter(121)` | 3 credits | None | same |
| EXP002-10 | No credit mid-encounter | Simulated in-progress encounter state (no `resolve_encounter()` call yet) | Zero credits produced regardless of elapsed rounds | None | same |
| EXP002-11 | Turn-mode → round-mode → turn-mode | Ordinary, then `resolve_encounter(N)`, then ordinary | Cumulative count continues with no reset/gap/duplicate | None | same |
| EXP002-12 | Multi-credit distinguishability | `resolve_encounter(121)` (case 9) | Three credits individually recoverable and ordered, not one opaque total | None | same |
| EXP002-13 | Mixed-sequence cumulative accounting | Arbitrary interleaving of ordinary/encounter calls | Strictly increasing, gapless cumulative count | None | same |
| EXP002-14 | No RNG dependency | Any sequence, with no RNG double supplied (or one that raises on any call) | Correct results with zero RNG interaction | None (explicitly asserted absent) | same |
| EXP002-15 | Cadence remains `EXP-001`'s concern | Any credit sequence | Test asserts only count/order/distinguishability — never any every-two-turn filtering | None | same |
| EXP002-16 (new) | `encounter_turn_cost()` formula, isolated | Direct calls with rounds ∈ {1, 59, 60, 61, 120, 121, and a value ≫120, e.g. 481} | Matches `max(1, ceil(rounds/60))` exactly, including the general case beyond the card's own worked examples | None | same (formula-level test, supplementing EXP002-03–09's class-level tests) |

### 12.2 `EXP-001` baseline, trigger/arrival, skip (source: `dungeon_wandering_monster_check.md` cases 1–17)

| Test ID | Approved behavior | Inputs/state | Expected mechanical result | RNG expectation | Proposed location |
|---|---|---|---|---|---|
| EXP001-01..06 | All six 1d6 baseline outcomes | Ordinary credit, due, scripted roll 1..6 | Only `1` triggers | One `roll_die(6)` each | `test_dungeon_wandering_monster_check.py` |
| EXP001-07 | First ordinary credit does not make baseline due | One ordinary credit | `NOT_DUE`, tally=1, no roll | None | same |
| EXP001-08 | Second ordinary credit due | Two ordinary credits | Roll performed (per 01–06); tally resets to 0 | One roll | same |
| EXP001-09 | Two-turn cycle repeats cleanly | Many ordinary credits | Exactly one check per two credits, no drift | One roll per due check | same |
| EXP001-10 | Pre-decided skip | Due ordinary credit, skip signal present | `SKIPPED`; tally resets to 0 | Zero rolls | same |
| EXP001-11 | Skip does not cause early/extra roll | Following EXP001-10, two more ordinary credits | First not due (tally=1), second due (tally=2) | One roll only at the second | same |
| EXP001-12 | Triggering check does not itself signal arrival | Scripted roll=1 on a due ordinary credit | `TRIGGERED`; `pending_arrival=True`; no arrival yet | One roll | same |
| EXP001-13 | Arrival at beginning of next turn | `resolve_arrival()` called after EXP001-12 | `ArrivalResult(occurred=True)` | Zero rolls | same |
| EXP001-14 | No extra roll on arrival turn | `resolve_arrival()` returns `occurred=True`; caller does not call `advance()` for that same turn | Zero rolls on the arrival turn | Zero rolls | same |
| EXP001-15 | No trigger ⇒ no arrival | `resolve_arrival()` with `pending_arrival` never set | `ArrivalResult(occurred=False)`, regardless of call count | Zero rolls | same |
| EXP001-16 | Valid-sequence pending-arrival invariant | Trigger, then `resolve_arrival()` invoked correctly before the next `advance()` | No second `pending_arrival=True` occurs; single-slot boolean suffices | Zero extra rolls | same |
| EXP001-17 | Post-arrival state is clean | Next ordinary credit after EXP001-16 | Evaluates from `pending_arrival=False`; may execute normally | Per normal rules | same |

### 12.3 `EXP-001` heightened checking and transition (cases 18–25)

| Test ID | Approved behavior | Inputs/state | Expected mechanical result | RNG expectation | Proposed location |
|---|---|---|---|---|---|
| EXP001-18 | Heightened: due every credit | `heightened_checking=True`, ordinary credit | Roll every ordinary credit, not every two | One roll each | `test_dungeon_wandering_monster_check.py` |
| EXP001-19 | Chance level 2 (1-2) | `heightened_chance_level=2`, scripted 2 vs 3 | 2 triggers, 3 does not | One roll each | same |
| EXP001-20 | Chance level 3 (1-3) | level=3, scripted 3 vs 4 | 3 triggers, 4 does not | One roll each | same |
| EXP001-21 | Chance level 4 (1-4) | level=4, scripted 4 vs 5 | 4 triggers, 5 does not | One roll each | same |
| EXP001-22 | Default absent explicit input | No heightened input supplied | Ordinary cadence, 1-in-6 baseline | Per normal rules | same |
| EXP001-23 | Entry mid-cadence | tally=1 (normal), then heightened activates before next ordinary credit | That credit is due under the heightened threshold; executes; tally resets to 0 | One roll | same |
| EXP001-24 | Exit mid-cadence | Heightened active, tally just reset to 0, then deactivates before next ordinary credit | Normal two-turn threshold applies from current tally value with no carryover | Per normal rules | same |
| EXP001-25 | Many transitions, no drift | Repeated entry/exit at varying tally values | Shared-counter design self-consistent; no double-check, no missed check | Per normal rules | same |

### 12.4 `EXP-001` encounter-derived credits, cadence-only, collapse (cases 26–30)

| Test ID | Approved behavior | Inputs/state | Expected mechanical result | RNG expectation | Proposed location |
|---|---|---|---|---|---|
| EXP001-26 | Single encounter-derived credit | One encounter-derived credit (from a ≤60-round encounter) | `CADENCE_ADVANCED_ONLY`; tally advances; `pending_arrival` unchanged, even if now over threshold | Zero rolls | `test_dungeon_wandering_monster_check.py` |
| EXP001-27 | Long encounter — zero rolls during | Three encounter-derived credits (121-round encounter, EXP002-09) | Each `CADENCE_ADVANCED_ONLY`; zero rolls across all three, even past threshold | Zero rolls | same |
| EXP001-28 | Deferred execution resolves all of it | Next ordinary credit following EXP001-27 | Exactly one roll; tally resets to 0 regardless of accumulated excess | One roll | same |
| EXP001-29 | Mixed sequence, roll only at ordinary | Ordinary, encounter-derived, encounter-derived, ordinary | Roll only possible at the two ordinary credits, never the encounter-derived ones | Per which credits are due | same |
| EXP001-30 | Collapse is not rate-preserving | Repeated `EXP002-09`-shaped long-encounter sequences interleaved with ordinary credits | Actual check count can be **lower** than one check per two total credits (approved consequence of Simulator Ruling B) — must not be asserted as rate-preserving | Per due checks only | same |

### 12.5 `EXP-001` round-mode non-execution and RNG audit (cases 31–34)

| Test ID | Approved behavior | Inputs/state | Expected mechanical result | RNG expectation | Proposed location |
|---|---|---|---|---|---|
| EXP001-31 | No `advance()` calls during round-mode | Round-mode in progress, no credits produced | `advance()` simply not invoked (falls out of `EXP-002`'s own contract) | N/A | `test_dungeon_wandering_monster_check.py` |
| EXP001-32 | Exactly one roll per executed check | Various due/not-due/skipped/encounter-derived combinations | Never zero-when-due-and-executable, never more than one | Audited via a `ScriptedRNG` with an exact-length queue | same |
| EXP001-33 | Zero rolls for arrival and encounter-derived credits | `resolve_arrival()` and `advance()` on encounter-derived credits | Zero rolls in both cases | `ScriptedRNG` with an empty/zero-length-consumable queue proves no draw occurs | same |
| EXP001-34 | Determinism | Same seed/call sequence via `SeededRNG` | Identical outcome sequence reproduced | `SeededRNG` reproducibility | same |

---

## 13. Cross-Card Integration Scenarios

Exercised directly by `tests/rules/exploration/test_cluster_001_integration.py`, composing `DungeonTimeAccounting` and `WanderingMonsterCadence` itself — no production orchestrator exists or is needed (§11). Every scenario below makes the full valid ordinary-turn sequencing explicit, per the approved contract (§7):

```text
begin Game Turn
    → resolve_arrival()                              (EXP-001 Moment A / Procedure B)
    → IF arrival occurred: STOP — this turn's own Actions/Results/step-4
      do not occur; the test asserts this and does not call
      complete_ordinary_turn() for this same turn
    → ELSE: the externally-governed ordinary Game Turn executes
      (opaque to this cluster, per §3)
    → EXP-002.complete_ordinary_turn()  produces one ORDINARY credit
    → EXP-001.advance(credit, ...)                    (Moment B / Procedure A)
```

| Scenario | Steps (explicit) | Expected result | Proposed location |
|---|---|---|---|
| 1 — Ordinary wandering trigger | `resolve_arrival()`→no arrival; `complete_ordinary_turn()`+`advance()`→not due; `resolve_arrival()`→no arrival; `complete_ordinary_turn()`+`advance()`→due, scripted roll=1→`TRIGGERED`; then `resolve_arrival()` again | Final `resolve_arrival()` returns `occurred=True`; that turn's own Actions/Results/step-4 do not occur (test does not call `complete_ordinary_turn()` for it) | `test_cluster_001_integration.py` |
| 2 — Ordinary no-trigger | `resolve_arrival()`→no arrival; two `complete_ordinary_turn()`+`advance()` pairs → due check, scripted roll∈{2..6} | `NO_TRIGGER`; `pending_arrival` remains `False`; subsequent `resolve_arrival()` calls all return `occurred=False` | same |
| 3 — Long encounter crosses cadence | Cadence state pre-existing (e.g., tally=1) → `resolve_encounter(121)` (3 encounter-derived credits, each passed to `advance()`, zero rolls) → **`begin Game Turn`: `resolve_arrival()`→no arrival (no arrival was ever pending)** → `complete_ordinary_turn()`+`advance()` (the next *ordinary* credit) | Zero rolls across the three encounter-derived `advance()` calls; exactly one roll at the ordinary credit that follows, not three, not zero; the explicit `resolve_arrival()` call before that ordinary credit is part of the asserted sequence, not skipped | same |
| 4 — Pre-decided skip | `resolve_arrival()`→no arrival; `complete_ordinary_turn()`+`advance(..., skip_signal=True)` on a due ordinary credit | `SKIPPED`; zero RNG operations; tally resets for the next period | same |
| 5 — Heightened transition | `resolve_arrival()`/`complete_ordinary_turn()`/`advance()` cycles with `heightened_checking` toggled between calls, spanning several credits | Shared-counter behavior demonstrated across the transition, with no hidden phase restoration; `resolve_arrival()` is called at the start of every simulated turn throughout, not only when a trigger is expected | same |

Each scenario is a thin composition of already-unit-tested behavior (§12) — it proves the two Rule Cards' modules integrate correctly when sequenced per the approved contract, and does not re-prove any individual branch already covered at the unit level (`TESTING_STRATEGY.md` §4). No scenario advances past an unresolved `resolve_arrival()` call, and no scenario calls `complete_ordinary_turn()` for a turn whose own `resolve_arrival()` has not been checked first — both would be a sequencing-contract violation, not a case these tests exercise as valid (§7).

---

## 14. Implementation Sequence

Derived from the dependency graph in §9, not adopted from any illustrative template blindly:

1. **`turn_credit.py`** — the shared contract type. No dependencies; blocks everything else.
   *Verification gate: unit tests for the two value types (construction, immutability, equality) pass; `mypy --strict` and `ruff` clean.*
   *Completion record: [`ISSUE-003`](../completion-records/ISSUE-003-cluster-001-turn-credit-contract.md) — Complete.*
2. **`dungeon_turn_time_accounting.py`** (`EXP-002`) — depends only on step 1.
   *Gate: EXP002-01–16 pass; 100% branch coverage per `src/rules/` requirement (`TESTING_STRATEGY.md` §8).*
   *Completion record: [`ISSUE-004`](../completion-records/ISSUE-004-exp-002-dungeon-turn-time-accounting.md) — Complete.*
3. **`dungeon_wandering_monster_check.py`** (`EXP-001`) — depends only on step 1 and `src/rng`'s existing `RNG` Protocol; does **not** depend on step 2.
   *Gate: EXP001-01–34 pass; 100% branch coverage; RNG-audit cases (EXP001-32–34) specifically verified.*
   *Completion record: assigned the next unused issue number in `docs/completion-records/INDEX.md` when this step is implemented.*
4. **`tests/rules/exploration/test_cluster_001_integration.py`** — direct cross-card `CLUSTER-001` integration tests, composing steps 2–3's production modules with no intervening production module (§11: production orchestration is deliberately deferred; this step adds no production module).
   *Gate: cross-card integration scenarios 1–5 (§13) pass, using only already-verified EXP-001/EXP-002 behavior underneath.*
   *Completion record: assigned the next unused issue number when this step is implemented.*

Each step is independently reviewable; no step's tests depend on a later step's code existing (step 3 does not need step 2's implementation to exist to be tested, since `EXP-001`'s own tests construct `TurnCredit` values directly rather than obtaining them from a live `DungeonTimeAccounting` instance). Step 4 has no human-confirmation prerequisite of its own — the production-orchestration decision point (§11) is resolved, not merely deferred pending confirmation.

**Completion-record timing, corrected (2026-08-18).** `DEVELOPMENT_WORKFLOW.md` §3 requires a completion record for every completed implementation issue that changes behavior under `src/`, and treats that record as part of what makes the issue complete — not an optional summary written after some later milestone. **Each independently completed implementation step above that changes production behavior must receive its own required completion record before that step is considered complete**, per `DEVELOPMENT_WORKFLOW.md` §3–§5, exactly like any other implementation issue in this project. Steps 1 and 2 have each already been treated this way, retroactively: Step 1 → [`ISSUE-003`](../completion-records/ISSUE-003-cluster-001-turn-credit-contract.md); Step 2 → [`ISSUE-004`](../completion-records/ISSUE-004-exp-002-dungeon-turn-time-accounting.md). Future production steps (3 and 4 above) must follow the same workflow — each gets its own completion record at the point it is independently completed, not deferred to the end of the sequence.

This corrects the prior wording of this section, which described one completion record deferred until "steps 1–4 are implemented" — that framing conflicted with `DEVELOPMENT_WORKFLOW.md`'s own per-issue completion-record requirement once individual steps began being independently reviewed and merged as separate implementation issues, and is superseded by the per-step mapping above. A further, final `CLUSTER-001` completion/integration record, summarizing the cluster's own integration gate once all four steps are done, remains a legitimate and useful addition after step 4 — but it supplements the four per-step records above; it does not substitute for any of them.

This is a process-consistency correction only. It does not reopen, reinterpret, or alter this plan's mechanics, module design, sequencing, tests, architecture decisions, or human approval (§1, §4–§13, §18–§19 unchanged in substance).

---

## 15. Implementation Risks and Safeguards

| Risk | Concrete safeguard |
|---|---|
| Conflating elapsed credit with step-4 check opportunity | `advance()`'s internal branch on `credit.origin` (§7.2/§7.3) is the single structural gate; EXP001-26/27 directly assert zero rolls on encounter-derived credits regardless of tally value. |
| Firing arrival on the next completed credit rather than at Game-Turn start | `resolve_arrival()` is a distinct method with no credit parameter at all — it cannot be accidentally invoked "per credit"; EXP001-13/14 assert arrival is tied to the beginning-of-turn call, not credit completion. |
| Rolling retroactively for encounter-derived credits | Same structural gate as above — the encounter-derived branch returns before reaching the roll; EXP001-27 explicitly asserts zero rolls across a whole long encounter. |
| Generating multiple deferred checks after a long encounter | Due-ness is recomputed fresh at the next ordinary credit from the accumulated tally, never per encounter-derived credit; EXP001-28 asserts exactly one roll regardless of accumulated excess. |
| Incorrectly preserving a one-check-per-two-total-credits aggregate rate | EXP001-30 explicitly asserts the collapse is *not* rate-preserving — a regression here is a direct test failure, not merely an omission. |
| Resetting cadence merely because heightened mode changes | The tally reset happens only inside the branch that resolves a due ordinary period — a performed check or the pre-decided skip — never inside a heightened-flag setter (there is no such setter — the flag is a call parameter, §5/§6); EXP001-23/24/25 assert no reset on transition alone, and EXP001-10/11 assert the skip resets the tally exactly as a performed check does. |
| Consuming RNG on skipped/due-but-not-executable checks | `roll_die` is called from exactly one branch (due, ordinary, not skipped); EXP001-32/33 audit a `ScriptedRNG` with an exactly-sized queue, which fails loudly (`RollSequenceExhaustedError` or leftover unused values) if the call count is wrong. |
| Letting monster-selection responsibilities leak into `EXP-001` | `WanderingCheckResult`/`ArrivalResult` carry no monster/direction/distance fields at all — there is no field to populate even by mistake (§7.1, §4.2 "Responsibility boundary"). |
| Fractionalizing `EXP-002` time | `DungeonTimeAccounting`'s counter is typed as an integer turn count; `TurnCredit.turn_number` is an int; no floating-point or `Fraction` type appears anywhere in the proposed representation. |
| Changing approved 61-round/121-round behavior because it "feels" unintuitive | `encounter_turn_cost()` is a direct, isolated implementation of the card's own quoted formula (EXP002-16), tested independently of any narrative framing; EXP002-07/09 pin the exact approved outputs. |
| Coupling historical-rules modules to presentation/narrative code | No import of any presentation/narrative package appears in §8's dependency table (none exist yet, and the table forbids it going forward); `ARCHITECTURE.md` §2/§11 already establishes this boundary generally. |

---

## 16. Explicitly Deferred / Out-of-Scope Responsibilities

- `MON-001`, `MON-002`, `ENC-001`, `ENC-002`, `ENC-003` — not designed, not stubbed.
- `EXP-008` and the `MON-001` ↔ `EXP-008` circularity — not investigated.
- `EXP-004` — remains `REVALIDATION_REQUIRED`, excluded from this cluster.
- `EXP-003`/`EXP-005` (real movement/search content) and any future exploration-turn driver that decides *when* Moments A/B/C actually occur from player/DM input, mutates authoritative simulation state, and exposes outcomes downstream to presentation — deliberately deferred (§11, "Preserve the future human-playable architecture"). This cluster's integration tests sequence the three moments directly, once told they occurred; nothing in this cluster decides their timing from game content.
- Structured event emission (`ARCHITECTURE.md` §8) and any persistence of campaign/dungeon-turn state (`ARCHITECTURE.md` §7) — no consumer needs either yet.
- A code formatter, test-order randomization, or any other item `docs/technical/TOOLCHAIN_AND_CI.md` §11 already lists as deferred.
- Any survivability policy interaction — both cards are structurally excluded from accepting one (`ARCHITECTURE.md` §10).

---

## 17. Rule-Card Clarification Requirements

**None.** Both `EXP-001` and `EXP-002` are, after their respective 2026-08-16/2026-08-18 human-approval rounds, sufficiently precise for every mechanical question this plan needed to answer. No contradiction was found between the two cards — where `EXP-002` explicitly defers a question ("`DEFERRED TO EXP-001`," encounter-credited-turn cadence participation), `EXP-001` explicitly resolves it (Simulator Ruling A), and no other overlap was found to conflict.

---

## 18. Architecture-Decision Requirements

**None open.** One point was raised and is now resolved:

**`RESOLVED`** — production Game-Turn orchestration (the code deciding *when* Moments A/B/C occur and enforcing their required order) is deferred until a real exploration-turn driver exists; `CLUSTER-001` integration is verified directly through the approved rule-module contracts (§11). `ARCHITECTURE.md` still does not define an orchestration/engine layer, and this plan does not create one, does not fold its responsibility into a placeholder production module, and does not treat this as a rejection of an eventual Simulation Engine — only as a deliberate deferral until movement/actions content makes that layer's responsibility concrete (§11, "Preserve the future human-playable architecture"). This does not block any step of the implementation sequence (§14): step 4 now adds a test module, not a production module, and requires no further human confirmation before it begins.

No other architectural change is proposed. This plan does not add an event bus, ECS, plugin system, generic turn engine, or Application Layer — all remain correctly deferred per `ARCHITECTURE.md` §13.

---

## 19. Implementation-Readiness Assessment

- All five of `DEC-0005`'s cluster-readiness criteria are met for `CLUSTER-001`'s two-card boundary: (1) scope clearly defined (§3); (2) all historical rules directly required identified (§4); (3) both required Rule Cards `APPROVED` (`EXP-001` 2026-08-18, `EXP-002` 2026-08-16); (4) the one external dependency (the RNG abstraction) has a stable, already-approved contract (§10); (5) no unresolved rules ambiguity remains that an implementation agent would need to adjudicate (§17: none found).
- The one architecture-decision point raised in the prior draft (§18) is now resolved — production Game-Turn orchestration is deliberately deferred, and `CLUSTER-001` integrates through direct tests instead. No architecture decision point remains open.
- **This plan received Human Implementation-Plan Review: APPROVED, 2026-08-18** (see §1). Per `ARCHITECTURE.md` §15.2, that approval is the human authorization step (4), "(re-)approved implementation readiness," requires — distinct from, and in addition to, the two Rule Cards' own individual approvals.

**`GOVERNANCE SYNC — RESOLVED, 2026-08-18`:** `ARCHITECTURE.md` §15.2's current-status text has been updated in the same task that recorded this plan's approval, to record `CLUSTER-001` historical-rules implementation as `AUTHORIZED — 2026-08-18`, scoped specifically to the `EXP-001` + `EXP-002` boundary and this plan. See `ARCHITECTURE.md` §15.2's "Status update (2026-08-18)" for the authorization record itself. This does not authorize any other cluster or Rule Card, and does not weaken `ARCHITECTURE.md` §16's general Pre-Code Development Gate, which remains active project-wide.

- No production code, test skeletons, or placeholder classes have been created by this task.

**IMPLEMENTATION PLAN APPROVED**
