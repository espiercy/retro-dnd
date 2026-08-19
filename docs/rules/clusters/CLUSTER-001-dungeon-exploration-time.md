# Cluster 1: Dungeon Exploration Time

> **Revalidation note (2026-08-16).** This cluster's boundary has completed Rules Cyclopedia revalidation and been human-selected as the first RC-native implementation cluster, following review of `docs/rules/clusters/RC_V1_FIRST_CLUSTER_ANALYSIS.md`. The current, authoritative boundary is `EXP-001` + `EXP-002` — see "Current Rules Cyclopedia-Revalidated Boundary" immediately below. The original 2026-08-16 migration note (recording this cluster's suspension pending revalidation) and the full three-item `EXP-001` + `EXP-002` + `EXP-004` boundary approved 2026-08-15 under the since-superseded 1974-primary source policy are preserved unchanged, for provenance only, under "Historical 1974-Primary Boundary and Analysis" further below. **That historical section does not describe the current cluster.**

## Current Rules Cyclopedia-Revalidated Boundary (2026-08-16)

**Status: `APPROVED`** — the cluster *boundary* only. See "Status of the boundary vs. status of its Rule Cards" below for what remains outstanding before implementation.

**Current authority:** Rules Cyclopedia (`docs/decisions/DEC-0007-rules-cyclopedia-primary-rules-authority.md`), as scoped for V1 by `docs/decisions/DEC-0008-rules-cyclopedia-v1-rules-profile.md`.

**Human revalidation date:** 2026-08-16

**Approved boundary:** `EXP-001` (Dungeon Wandering-Monster Check) + `EXP-002` (Dungeon Turn / Time Accounting). Two Rule Cards.

### Why this boundary

- This boundary was **re-derived from the approved `docs/rules/INVENTORY.md` RC V1 Rules Inventory** (`APPROVED` 2026-08-16) — it is not inherited from the old three-item 1974-primary cluster preserved below. It happens to overlap with two of that cluster's three original members, but that overlap is a consequence of independent re-analysis, not an assumption carried forward. See `docs/rules/clusters/RC_V1_FIRST_CLUSTER_ANALYSIS.md` for the full comparative candidate analysis that produced this recommendation.
- **`EXP-002` is the time-accounting foundation.** It has no dependency on any other inventory item and supplies the "a qualifying dungeon-turn interval has elapsed" signal that the rest of this boundary — and much of the wider exploration/encounter domain — depends on.
- **`EXP-001` depends on `EXP-002`** for that elapsed-turn signal, and on the **already-approved RNG abstraction** (`docs/technical/RNG_CONTRACT.md`) for its own die roll.
- **No other historical-rule dependency is required for this boundary.** `EXP-001` and `EXP-002` are dependency-complete on their own — no character, monster, combat, or map content is needed to exercise them.
- **`EXP-004` (Resting Procedure) is deliberately removed from this boundary.** Its old mandatory-hourly-rest mechanic does not survive as Rules Cyclopedia canon, and its replacement responsibility is currently classified `REFRAME` with an open `SPLIT CANDIDATE` flag (possible short-term running/exhaustion content, a distinct wilderness-travel-rest responsibility, or both) in `docs/rules/INVENTORY_MIGRATION_MAP.md`. Its scope is not settled enough to belong in a stable cluster boundary. See "`EXP-004` — excluded from the current boundary" below.
- **The cluster's boundary was stable independent of either Rule Card's own revalidation outcome, and that has now been borne out: both `EXP-001` and `EXP-002` are human-approved, and both are now individually implemented and `VERIFIED`.** `EXP-002` was human-approved 2026-08-16; `EXP-001` was human-approved 2026-08-18, including Simulator Rulings A–C. Boundary stability and Rule Card readiness were always different questions — the boundary never depended on the outcome of either card's revalidation, since neither `EXP-001` nor `EXP-002` gained or lost the other as a dependency once revalidated.

### Status of the boundary vs. status of its Rule Cards — do not conflate these

| Item | Status |
|---|---|
| `CLUSTER-001` boundary (this document's current scope) | **`APPROVED`** |
| `EXP-001` (Dungeon Wandering-Monster Check) | **`VERIFIED`** (human-approved 2026-08-18, including Simulator Rulings A–C; implemented and verified 2026-08-18 — `src/rules/exploration/dungeon_wandering_monster_check.py`, `docs/completion-records/ISSUE-005-exp-001-dungeon-wandering-monster-check.md`) |
| `EXP-002` (Dungeon Turn / Time Accounting) | **`VERIFIED`** (human-approved 2026-08-16, including its long-encounter Simulator Ruling; implemented and verified 2026-08-18 — `src/rules/exploration/dungeon_turn_time_accounting.py`, `docs/completion-records/ISSUE-004-exp-002-dungeon-turn-time-accounting.md`) |
| `EXP-004` (Resting Procedure) | `REVALIDATION_REQUIRED` — excluded from this cluster; see below |

**The cluster's required Rule Cards are now human-approved and individually implemented/verified.** The historical-rules research gate for the selected `EXP-001` + `EXP-002` boundary is complete: both `EXP-001` and `EXP-002` have completed Rules Cyclopedia revalidation and human approval. Per `DEC-0005-v1-rules-inventory-and-clustered-implementation.md`'s workflow, implementation/integration preparation has since occurred (`docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md`, `IMPLEMENTATION PLAN APPROVED`), and implementation of this boundary was authorized 2026-08-18 (`ARCHITECTURE.md` §15.2). See "Implementation Progress" immediately below for the cluster's current, in-progress implementation state — **both constituent Rule Cards are now individually implemented and verified, but `CLUSTER-001` itself is not yet implementation-complete or verified, because the approved cross-card integration gate remains outstanding.**

### Implementation Progress (2026-08-18)

`CLUSTER-001` implementation is in progress, tracked as four steps in the approved implementation plan:

| Step | Scope | Status |
|---|---|---|
| 1 | `TurnCredit` / `TurnCreditOrigin` (shared contract) | **Complete** — `docs/completion-records/ISSUE-003-cluster-001-turn-credit-contract.md` |
| 2 | `EXP-002` mechanical implementation | **Complete / `VERIFIED`** — `docs/completion-records/ISSUE-004-exp-002-dungeon-turn-time-accounting.md` |
| 3 | `EXP-001` mechanical implementation | **Complete / `VERIFIED`** — `docs/completion-records/ISSUE-005-exp-001-dungeon-wandering-monster-check.md` |
| 4 | Cross-card integration tests | **Not begun** |

**Both constituent Rule Cards are now individually implemented and verified, but `CLUSTER-001` itself is not yet implementation-complete or verified** — the approved cross-card integration gate (Step 4) remains outstanding. Do not read Steps 1–3's completion as `CLUSTER-001` itself being implemented or verified.

### `EXP-004` — excluded from the current boundary

`EXP-004` is excluded from `CLUSTER-001` as currently revalidated. Its lifecycle remains `REVALIDATION_REQUIRED`. Its future cluster placement is unresolved: its eventual scope may involve short-term running/exhaustion content, a distinct wilderness-travel-rest responsibility, or both, and remains subject to dedicated future revalidation before it is assigned to any cluster. This document does not resolve or split it.

### Stable external dependency

The cluster's one currently established external stable dependency is the **already-approved RNG abstraction** (`src/rng/`, `docs/technical/RNG_CONTRACT.md`) — `EXP-001`'s own dependency for its die roll. `EXP-002`'s revalidation is complete and now `VERIFIED` (implemented 2026-08-18): it establishes the boundary's authoritative executable time-accounting contract directly — a discrete whole-turn credit model (one credit per completed Game-Turn-Checklist iteration, plus `max(1, ceiling(encounter_rounds / 60))` whole-turn credit(s) for a resolved encounter, produced only once round-mode resolution finishes), not a fractional ledger or a synthetic activity-cost input. See `docs/rules/exploration/dungeon_turn_time_accounting.md` for the full specification and `src/rules/exploration/dungeon_turn_time_accounting.py` for the implementation. `EXP-001`'s own revalidation is likewise complete and now `VERIFIED` (human-approved and implemented 2026-08-18) — see `docs/rules/exploration/dungeon_wandering_monster_check.md` for the full specification and `src/rules/exploration/dungeon_wandering_monster_check.py` for the implementation (`CLUSTER-001` Step 3, "Implementation Progress" above). The historical-rules research gate for this cluster's boundary is closed; both constituent Rule Cards are individually implemented and verified, but the cluster's own cross-card integration (Step 4) is not yet begun, so the cluster's implementation is in progress but not complete.

### Provenance

Selected following human review of `docs/rules/clusters/RC_V1_FIRST_CLUSTER_ANALYSIS.md` (comparative candidate analysis; not rewritten by this revalidation). No decision record was created for this selection — `DEC-0005-v1-rules-inventory-and-clustered-implementation.md` already governs dependency-complete cluster selection and sequencing; this document is the record of the human selection itself.

---

## Historical 1974-Primary Boundary and Analysis (preserved for provenance)

> **This section is historical and does not describe the current cluster.** Everything from here to the end of this document is the original 1974-primary-sourced cluster proposal, approved 2026-08-15 under the since-superseded 1974-primary source policy (`DEC-0006-v1-playable-content-scope.md`, superseded by `DEC-0007`), together with the 2026-08-16 migration note that recorded its suspension pending Rules Cyclopedia revalidation. It is preserved verbatim below for provenance — to show the reasoning and research that led to today's re-derived boundary above — not as a statement of `CLUSTER-001`'s current scope, membership, or status. In particular: **do not read anything below as saying `EXP-004` is part of the current cluster, or that a mandatory-hourly-rest mechanic is current Rules Cyclopedia canon.** Historical statements below that `EXP-001` was "already `APPROVED`" refer to its old 1974-primary approval and must not be treated as the authority for its present status. `EXP-001` is now independently `APPROVED` again following Rules Cyclopedia revalidation and human approval on 2026-08-18; see the Current section above.

> **Migration note (2026-08-16), preserved as originally written.** This cluster was approved based on three Rule Cards (`EXP-001`, `EXP-002`, `EXP-004`) researched under the superseded 1974-primary source policy. Its implementation authority is suspended: status changed to `REVALIDATION_REQUIRED` below. Requires Rules Cyclopedia revalidation of its boundary and included rules before implementation authority is restored (`DEC-0007-rules-cyclopedia-primary-rules-authority.md`, `DEVELOPMENT_WORKFLOW.md` §9.7, `ARCHITECTURE.md` §15.2). Do not assume the existing three-item boundary below will remain unchanged once revalidated — it is preserved here as the historical record of what was previously approved, not as a pre-committed outcome of revalidation. See `docs/rules/RULESET_BASELINE_MIGRATION.md`.

### 1. Cluster ID

`CLUSTER-001`

### 2. Working Title

Dungeon Exploration Time

*(Deliberately narrower than "Dungeon Exploration" generally — see §5–6.)*

### 3. Status

`REVALIDATION_REQUIRED` — previously `APPROVED` (human-approved 2026-08-15, subject to the consistency corrections recorded in §14); that approval was granted under the since-superseded 1974-primary source policy and no longer authorizes implementation as-is (see migration note above). The historical approval record, boundary analysis, rationale, and research ordering below (§4–§14) are preserved unchanged; none of it is rewritten by this migration.

This document previously approved the cluster *boundary* itself (§5–§13) and did not, by itself, begin Rule Card research or authorize implementation — both remained separate, explicitly authorized tasks under the established workflow (`ARCHITECTURE.md` §15.1, `DEVELOPMENT_WORKFLOW.md`). That remains true; implementation of this cluster additionally now requires the revalidation described above before the established workflow can resume.

### 4. Purpose

Make `EXP-001` (Dungeon Wandering-Monster Check, already `APPROVED`) integrable by resolving the smallest additional set of historical rules needed to supply it with a real "a qualifying dungeon-turn interval has elapsed" signal — its one stated dependency — and to demonstrate that signal being produced by genuine, historically-sourced turn-consuming activities rather than a synthetic test stub.

This cluster is deliberately **not** "all of dungeon exploration." It is the turn-accounting core that everything else in the `exploration` domain ultimately depends on, scoped as narrowly as the dependency analysis in §6 supports.

### 5. Included Inventory Items

| ID | Title | Why it belongs |
|---|---|---|
| `EXP-001` | Dungeon Wandering-Monster Check | Already `APPROVED`. The cluster's reason for existing — this is what the cluster makes integrable. Not reopened; see §10. |
| `EXP-002` | Dungeon Turn / Time Accounting | `EXP-001`'s one stated hard dependency. The cluster's core research target. Per its own inventory entry, already-sourced material covers *what counts as a turn* and *the turn-cost of movement, resting, searching, and combat as historical facts* — this cluster's scope is that turn-definition-and-accounting layer, not the full procedural content of those activities (see §6). |
| `EXP-004` | Resting Procedure | A second, independently well-sourced, historically *mandatory* turn-consuming activity ("one turn every hour must be spent motionless," Vol. 3 p. 8). Included so the cluster demonstrates the turn counter being driven by more than one activity type, and by a real historical rule rather than only a generic "movement happened" stub. |

Three items. This is a small cluster deliberately — see §7 for why it isn't larger.

### 6. Explicitly Excluded Neighboring Items

| ID | Title | Disposition | Why |
|---|---|---|---|
| `CHAR-005` | Encumbrance & Movement Rate | Excluded — stable external contract | Cluster 1 needs only the *fixed* historical time-conversion "two moves constitute a turn" (already part of `EXP-002`'s sourced material) — not the *encumbrance-derived* feet-per-turn rate, which only matters for knowing how far the party moved in space. See §11. |
| `EXP-003` | Dungeon Movement, Mapping & Special Terrain | Excluded — a candidate for splitting when researched; see §9 | The movement *time-cost* fact this cluster needs is already covered under `EXP-002`. The rest of `EXP-003` — spatial mapping, and the special-terrain/aquatic-movement concern flagged in the last inventory revision — is not needed for turn accounting and is deferred to a later movement/mapping cluster. |
| `EXP-005` | Searching, Listening, Doors & Secret Features | Excluded in full; see §9 | Its *time-cost* fact ("a full turn" for a 10' wall section, shorter activities referee-adjudged) is already reflected in `EXP-002`'s sourced material. The actual detection procedures (secret-door odds, listening odds, door-forcing odds) are unrelated to turn accounting and belong to a later "Dungeon Search & Perception" cluster. |
| `EXP-006` | Light & Exploration Resources | Excluded — downstream consumer | Light consumption is naturally a *subscriber* to "a turn has elapsed," not a rule the turn-accounting system itself needs resolved. It also carries its own unresolved research gap (consumption rate not yet located) — pulling it in now risks exactly the "force the implementation agent to invent behavior" failure mode this cluster is meant to avoid. |
| `EXP-007` | Traps (trigger mechanic only) | Excluded — historical dependency question left unresolved, pending `EXP-007`'s own future research | The inventory currently records overlapping content between two entries: `EXP-005`'s "already sourced" list includes a "trap/pit trigger 1–2 on d6" fact, while `EXP-007` separately owns "Traps — trigger mechanic only" as its own title and scope. Separately, `EXP-007`'s listed `EXP-002` dependency is questionable — the already-sourced trigger text ("sprung by a roll of a 1 or a 2 ... when any character passes over or by them") reads as movement/spatial-triggered, not turn-elapsed-triggered like `EXP-001`'s. Neither the overlap nor the dependency question is resolved or corrected here; both are recorded for `EXP-007`'s own future research. Cluster 1 does not need traps resolved either way. |
| `EXP-008` | Dungeon Stocking | Excluded | Depends on `MON-001`, `MON-002`, `TREAS-001`, and (for a real dungeon) `SIM-001` — none related to turn accounting. Sharing the `EXP` prefix is not a reason to include it; explicitly called out per the assigning instructions. |
| `EXP-010` | Party Formation & Marching Order | Excluded | Matters for encounter positioning, surprise, and hazard exposure — all downstream of an encounter or hazard actually being resolved, which `EXP-001` itself explicitly does not do. Belongs with a future encounter-resolution cluster, not exploration-time. |
| `SIM-001` | Procedural Dungeon Generation | Excluded — no spatial fixture required at all | Cluster 1's integration target does not require a real generated dungeon, or even a spatially modeled one (rooms, passages, a map). Sufficient controlled underworld-exploration inputs (§8) are enough to exercise turn accounting and movement/rest activities. See §12. |
| `SIM-002` | Survivability Policy Specification | Excluded — not a dependency at all | Cluster 1's procedures are canonical historical rules that structurally never accept a survivability parameter (`ARCHITECTURE.md` §10, restated in `EXP-001`'s own "Survivability out of scope" clause). `SIM-002` would govern a policy layer sitting atop already-implemented canonical clusters later; it has no bearing on whether Cluster 1 itself is implementable. See §12. |

### 7. Hard Mechanical Dependencies

Dependencies the cluster cannot execute its promised behavior without:

- `EXP-001` requires a real "a qualifying dungeon-turn interval has elapsed" signal, which only `EXP-002` supplies. The integration relationship runs one direction — `EXP-002` → elapsed-turn signal → `EXP-001` — not the reverse: `EXP-002`'s own mechanical content (what a turn is, how turn-count advances) does not depend on `EXP-001` in any way; it simply produces a signal that `EXP-001` happens to consume, and could in principle produce that signal even if `EXP-001` didn't exist.
- `EXP-004` requires `EXP-002`'s turn definition to know what "one turn every hour" means precisely.
- `EXP-001` requires the already-approved RNG abstraction (`RNG_CONTRACT.md`) for its own die roll — an existing, already-satisfied dependency of `EXP-001` specifically. `EXP-002` and `EXP-004` do not independently require RNG merely because they integrate with `EXP-001`; neither rolls dice itself.

No other item in the inventory is a hard mechanical dependency of this cluster.

### 8. External Stable-Contract Dependencies

Described mechanically, not as an implementation architecture:

- **A recognized "movement action occurred" input.** The cluster needs to know that a movement action took place and how much turn-time it cost (a fact `EXP-002` already has: two moves constitute one turn) — it does not need to know how far the party moved in feet, or where, which depends on `CHAR-005` (movement rate) and `EXP-003` (mapping). Whatever future system tracks party position may supply this signal; Cluster 1 does not implement or require resolving that system's internals.
- **Sufficient controlled underworld-exploration inputs — not a spatial rooms/passages test-dungeon fixture.** Cluster 1's own integration test needs only enough controlled inputs (e.g., a scripted sequence of recognized activities — movement actions, a mandatory rest — occurring "in the underworld") to exercise the approved time procedures. It does not require a spatially modeled dungeon (rooms, passages, or a map) at all. The exact form of that integration fixture is left to implementation-time preparation, not fixed by this document. Not `SIM-001`, not `EXP-008`.

If no such stable contract could be described without resolving the excluded rule first, that would be evidence the rule belongs *inside* the cluster instead (per the assigning instructions) — that test was applied to each exclusion in §6 and did not trigger for any of them.

### 9. Expected Rule Card Splits

- **`EXP-003`** is a *candidate* for splitting when researched — for instance, a narrow movement time-cost fact (this analysis suggests already adequately covered by `EXP-002`'s own scope) versus a broader spatial-mapping-and-special-terrain concern. This document does not commit to that or any other specific split shape; the actual boundary is a research-time determination, per "A note on grouping" in the inventory.
- **`EXP-005`** is likewise a *candidate* for splitting into its distinct historical procedures (secret-door detection, listening, door-forcing, trap/pit triggering) once research begins — again, not a committed shape. Whether or how it splits, none of its content is needed by Cluster 1.
- **`EXP-002`** is not expected to split for Cluster 1's purposes, though it may end up with internally distinct subsections for each activity type's turn-cost (movement, rest, search, combat) without those becoming separate Rule IDs.

### 10. Already-Approved Rule Cards in the Cluster

`EXP-001` only. Its historical conclusions are not reopened by this cluster proposal. What Cluster 1 must supply to it, what it supplies in return, and when it becomes integrable:

- **Cluster 1 must supply `EXP-001`:** a real "a qualifying dungeon-turn interval has elapsed" signal, produced by `EXP-002`'s accounting once it is approved and implemented.
- **`EXP-001` supplies Cluster 1:** a trigger/no-trigger outcome and its `RollResult` audit data, each time that signal fires — the cluster's demonstrable integration output.
- **Becomes integrable:** once `EXP-002` (and, for a fuller demonstration, `EXP-004`) are `APPROVED` and implemented, and the turn-elapsed signal is wired to `EXP-001`'s existing, unmodified procedure.

### 11. Proposed Rule Card Research Order Inside the Cluster

1. **`EXP-002` — Dungeon Turn / Time Accounting.**
   - *Why it belongs:* `EXP-001`'s sole hard dependency; the cluster's entire reason for existing.
   - *Depends on:* nothing within the cluster; it is the foundation.
   - *Already approved:* no.
   - *Likely to split:* no (see §9) — but may absorb small turn-cost facts for movement/search/combat as historical data points without those becoming separate cards.
   - *What must be researched before approval:* the precise turn-accounting *algorithm* — how partial-turn activities accumulate toward a whole elapsed turn, and exactly when the elapsed-turn signal fires relative to that accounting. This is the same gap already named in `EXP-001`'s own "Open Questions" and must be closed here, not left open into implementation.

2. **`EXP-004` — Resting Procedure.**
   - *Why it belongs:* a second, real, well-sourced turn-consuming activity, demonstrating the turn counter driven by more than a synthetic stub.
   - *Depends on:* `EXP-002`'s completed turn definition.
   - *Already approved:* no.
   - *Likely to split:* no — small and largely already sourced.
   - *What must be researched before approval:* whether skipping the mandatory rest turn has a stated historical consequence, and the exact enforcement mechanic, beyond the already-extracted "one turn every hour must be spent motionless."

3. **`EXP-001` — Dungeon Wandering-Monster Check.**
   - Already `APPROVED`. No further research. Included in this order only to note that it is the *last* item to become newly integrable — implementation-ready only once `EXP-002` and `EXP-004` are both approved — not because it needs revisiting.

This order minimizes revisiting `EXP-001`: it is touched zero times for research purposes.

### 12. Cluster Implementation-Readiness Criteria

Applying `ARCHITECTURE.md` §15.1's five general criteria to this specific cluster:

1. **Scope clearly defined:** advance authoritative dungeon exploration time through movement and mandatory rest, and invoke `EXP-001` at each elapsed-turn boundary. Nothing else.
2. **All historical rules directly required identified:** `EXP-001` (done), `EXP-002`, `EXP-004` — see §5.
3. **All Rule Cards required are human-approved:** `EXP-002` and `EXP-004` must each reach `APPROVED`; `EXP-001` already is.
4. **External dependencies have a stable, sufficient contract:** the RNG abstraction (already approved, and specifically `EXP-001`'s dependency — see §7); the "movement action occurred" signal and sufficient controlled underworld-exploration inputs (§8, not a spatial fixture) — none of these requires a historical Rule Card, but a short implementation-time design note for each is expected before Cluster 1's implementation issue begins, not before this proposal is reviewed.
5. **No unresolved rules ambiguity left for the implementation agent:** requires `EXP-002`'s approval to explicitly close the turn-accounting-algorithm gap named in §11 — this is the one item in the whole cluster proposal most likely to determine whether readiness is actually reached on the first attempt.

### 13. Eventual Integration-Test Target

Given a party engaged in dungeon exploration — its composition, movement rate, and spatial position all supplied externally and out of this cluster's scope (§8) — and given a sequence of recognized turn-consuming activities (a generic "a movement action was taken" event, and the historically mandatory periodic rest), Cluster 1 authoritatively advances the campaign's dungeon-turn counter according to the approved `EXP-002` accounting rule, itself enforcing the `EXP-004` mandatory-rest requirement, and — at the boundary of every elapsed turn — invokes the already-approved `EXP-001` procedure exactly once, producing its trigger/no-trigger outcome and audit data.

No monster is generated, no encounter is resolved, no map is produced, no light is consumed, no search/listen/door procedure runs, and no other historical procedure outside `EXP-001`/`EXP-002`/`EXP-004` is invoked by this cluster. Those are exactly the boundaries in §6.

### 14. Human-Review Decisions Recorded (2026-08-15)

All five items originally raised in this section were resolved by human review on 2026-08-15, alongside cluster approval (§3):

1. **Cluster boundary.** The three-item boundary (`EXP-001` + `EXP-002` + `EXP-004`) is approved as proposed, in substance.
2. **`EXP-003`/`EXP-005` split expectations.** Not committed to a specific shape — both remain candidates that may split when researched (§9); no further decision needed at this stage.
3. **Externally supplied movement-capability framing.** Approved. `CHAR-005` and spatial movement/mapping remain outside Cluster 1 (§6, §8).
4. **`EXP-007` dependency-direction question, and the `EXP-005`/`EXP-007` trap-trigger overlap.** Left unresolved by decision, deferred to `EXP-007`'s own future research — not resolved and not silently corrected in the approved inventory (§6).
5. **Test-dungeon fixture.** Not required as a cluster-level dependency, and not required to be spatial at all. Cluster 1 needs only sufficient controlled underworld-exploration inputs (§8) to exercise the approved time procedures; the exact integration fixture/design is left to implementation preparation, not fixed here.

No open questions remain blocking Cluster 1's approval.

---

*This historical document recorded an approved cluster boundary as of 2026-08-15. Approval of the boundary was not, by itself, authorization to begin Rule Card research, implementation, or production code for any item listed above — each remained a separate, explicitly authorized task. That principle still holds for the current, re-derived boundary at the top of this document: `CLUSTER-001`'s boundary is `APPROVED`, but `EXP-001` and `EXP-002` remain `REVALIDATION_REQUIRED`, and neither Rule Card research nor implementation is authorized by this document.*
