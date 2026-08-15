# Cluster 1: Dungeon Exploration Time

## 1. Cluster ID

`CLUSTER-001`

## 2. Working Title

Dungeon Exploration Time

*(Deliberately narrower than "Dungeon Exploration" generally — see §5–6. This is a proposed boundary for human review, not an accepted title.)*

## 3. Status

`PROPOSED` — awaiting human review. Not accepted, not a decision record, not an authorization to research or implement.

## 4. Purpose

Make `EXP-001` (Dungeon Wandering-Monster Check, already `APPROVED`) integrable by resolving the smallest additional set of historical rules needed to supply it with a real "a qualifying dungeon-turn interval has elapsed" signal — its one stated dependency — and to demonstrate that signal being produced by genuine, historically-sourced turn-consuming activities rather than a synthetic test stub.

This cluster is deliberately **not** "all of dungeon exploration." It is the turn-accounting core that everything else in the `exploration` domain ultimately depends on, scoped as narrowly as the dependency analysis in §6 supports.

## 5. Included Inventory Items

| ID | Title | Why it belongs |
|---|---|---|
| `EXP-001` | Dungeon Wandering-Monster Check | Already `APPROVED`. The cluster's reason for existing — this is what the cluster makes integrable. Not reopened; see §10. |
| `EXP-002` | Dungeon Turn / Time Accounting | `EXP-001`'s one stated hard dependency. The cluster's core research target. Per its own inventory entry, already-sourced material covers *what counts as a turn* and *the turn-cost of movement, resting, searching, and combat as historical facts* — this cluster's scope is that turn-definition-and-accounting layer, not the full procedural content of those activities (see §6). |
| `EXP-004` | Resting Procedure | A second, independently well-sourced, historically *mandatory* turn-consuming activity ("one turn every hour must be spent motionless," Vol. 3 p. 8). Included so the cluster demonstrates the turn counter being driven by more than one activity type, and by a real historical rule rather than only a generic "movement happened" stub. |

Three items. This is a small cluster deliberately — see §7 for why it isn't larger.

## 6. Explicitly Excluded Neighboring Items

| ID | Title | Disposition | Why |
|---|---|---|---|
| `CHAR-005` | Encumbrance & Movement Rate | Excluded — stable external contract | Cluster 1 needs only the *fixed* historical time-conversion "two moves constitute a turn" (already part of `EXP-002`'s sourced material) — not the *encumbrance-derived* feet-per-turn rate, which only matters for knowing how far the party moved in space. See §11. |
| `EXP-003` | Dungeon Movement, Mapping & Special Terrain | Excluded — likely splits; see §9 | The movement *time-cost* fact this cluster needs is already covered under `EXP-002`. The rest of `EXP-003` — spatial mapping, and the special-terrain/aquatic-movement concern flagged in the last inventory revision — is not needed for turn accounting and is deferred to a later movement/mapping cluster. |
| `EXP-005` | Searching, Listening, Doors & Secret Features | Excluded in full; see §9 | Its *time-cost* fact ("a full turn" for a 10' wall section, shorter activities referee-adjudged) is already reflected in `EXP-002`'s sourced material. The actual detection procedures (secret-door odds, listening odds, door-forcing odds) are unrelated to turn accounting and belong to a later "Dungeon Search & Perception" cluster. |
| `EXP-006` | Light & Exploration Resources | Excluded — downstream consumer | Light consumption is naturally a *subscriber* to "a turn has elapsed," not a rule the turn-accounting system itself needs resolved. It also carries its own unresolved research gap (consumption rate not yet located) — pulling it in now risks exactly the "force the implementation agent to invent behavior" failure mode this cluster is meant to avoid. |
| `EXP-007` | Traps (trigger mechanic only) | Excluded — dependency direction questioned, not assumed | The inventory lists `EXP-002` as `EXP-007`'s dependency, but the already-sourced trigger text ("sprung by a roll of a 1 or a 2 ... when any character passes over or by them") describes a movement/spatial trigger, not a turn-elapsed trigger like `EXP-001`'s. This cluster does not need traps resolved, and traps do not appear to need turn accounting resolved either. Flagged in §21 for human review rather than silently corrected. |
| `EXP-008` | Dungeon Stocking | Excluded | Depends on `MON-001`, `MON-002`, `TREAS-001`, and (for a real dungeon) `SIM-001` — none related to turn accounting. Sharing the `EXP` prefix is not a reason to include it; explicitly called out per the assigning instructions. |
| `EXP-010` | Party Formation & Marching Order | Excluded | Matters for encounter positioning, surprise, and hazard exposure — all downstream of an encounter or hazard actually being resolved, which `EXP-001` itself explicitly does not do. Belongs with a future encounter-resolution cluster, not exploration-time. |
| `SIM-001` | Procedural Dungeon Generation | Excluded — testable against a fixture | Cluster 1's integration target does not require a real generated dungeon; a small hand-constructed fixture (a handful of rooms/passages) is sufficient to exercise turn accounting and movement/rest activities. See §12. |
| `SIM-002` | Survivability Policy Specification | Excluded — not a dependency at all | Cluster 1's procedures are canonical historical rules that structurally never accept a survivability parameter (`ARCHITECTURE.md` §10, restated in `EXP-001`'s own "Survivability out of scope" clause). `SIM-002` would govern a policy layer sitting atop already-implemented canonical clusters later; it has no bearing on whether Cluster 1 itself is implementable. See §12. |

## 7. Hard Mechanical Dependencies

Dependencies the cluster cannot execute its promised behavior without:

- `EXP-002` requires `EXP-001`'s consumer relationship to be honored (one sequence-numbered check per elapsed turn boundary — already specified in `EXP-001`'s approved card, not renegotiable by this cluster).
- `EXP-004` requires `EXP-002`'s turn definition to know what "one turn every hour" means precisely.
- Both `EXP-002` and `EXP-004` require the already-approved RNG abstraction (`RNG_CONTRACT.md`) for `EXP-001`'s own die roll — not a new dependency, already satisfied.

No other item in the inventory is a hard mechanical dependency of this cluster.

## 8. External Stable-Contract Dependencies

Described mechanically, not as an implementation architecture:

- **A recognized "movement action occurred" input.** The cluster needs to know that a movement action took place and how much turn-time it cost (a fact `EXP-002` already has: two moves constitute one turn) — it does not need to know how far the party moved in feet, or where, which depends on `CHAR-005` (movement rate) and `EXP-003` (mapping). Whatever future system tracks party position may supply this signal; Cluster 1 does not implement or require resolving that system's internals.
- **A minimal test-dungeon fixture.** A small, hand-constructed stand-in for "a dungeon" (enough rooms/passages to exercise movement and rest over several turns), used only for this cluster's own integration test — not a real generated or stocked dungeon. Not `SIM-001`, not `EXP-008`.

If no such stable contract could be described without resolving the excluded rule first, that would be evidence the rule belongs *inside* the cluster instead (per the assigning instructions) — that test was applied to each exclusion in §6 and did not trigger for any of them.

## 9. Expected Rule Card Splits

- **`EXP-003`** is likely to split during research into (a) the narrow movement time-cost fact, which this analysis suggests is already adequately covered by `EXP-002`'s own scope and may not need a separate card at all, and (b) a broader spatial-mapping-and-special-terrain card (including the previously-flagged aquatic-movement question) for a later cluster. Not resolved here — a research-time determination, per "A note on grouping" in the inventory.
- **`EXP-005`** is likely to split into its distinct historical procedures (secret-door detection, listening, door-forcing, trap/pit triggering) once research begins, none of which are needed by Cluster 1.
- **`EXP-002`** is not expected to split for Cluster 1's purposes, though it may end up with internally distinct subsections for each activity type's turn-cost (movement, rest, search, combat) without those becoming separate Rule IDs.

## 10. Already-Approved Rule Cards in the Cluster

`EXP-001` only. Its historical conclusions are not reopened by this cluster proposal. What Cluster 1 must supply to it, what it supplies in return, and when it becomes integrable are addressed in §16 below (report) and restated here for the document's own completeness:

- **Cluster 1 must supply `EXP-001`:** a real "a qualifying dungeon-turn interval has elapsed" signal, produced by `EXP-002`'s accounting once it is approved and implemented.
- **`EXP-001` supplies Cluster 1:** a trigger/no-trigger outcome and its `RollResult` audit data, each time that signal fires — the cluster's demonstrable integration output.
- **Becomes integrable:** once `EXP-002` (and, for a fuller demonstration, `EXP-004`) are `APPROVED` and implemented, and the turn-elapsed signal is wired to `EXP-001`'s existing, unmodified procedure.

## 11. Proposed Rule Card Research Order Inside the Cluster

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

## 12. Cluster Implementation-Readiness Criteria

Applying `ARCHITECTURE.md` §15.1's five general criteria to this specific cluster:

1. **Scope clearly defined:** advance authoritative dungeon exploration time through movement and mandatory rest, and invoke `EXP-001` at each elapsed-turn boundary. Nothing else.
2. **All historical rules directly required identified:** `EXP-001` (done), `EXP-002`, `EXP-004` — see §5.
3. **All Rule Cards required are human-approved:** `EXP-002` and `EXP-004` must each reach `APPROVED`; `EXP-001` already is.
4. **External dependencies have a stable, sufficient contract:** the RNG abstraction (already approved); the "movement action occurred" signal and the minimal test-dungeon fixture (§8) — neither requires a historical Rule Card, but a short implementation-time design note for each is expected before Cluster 1's implementation issue begins, not before this proposal is reviewed.
5. **No unresolved rules ambiguity left for the implementation agent:** requires `EXP-002`'s approval to explicitly close the turn-accounting-algorithm gap named in §11 — this is the one item in the whole cluster proposal most likely to determine whether readiness is actually reached on the first attempt.

## 13. Eventual Integration-Test Target

Given a party engaged in dungeon exploration — its composition, movement rate, and spatial position all supplied externally and out of this cluster's scope (§8) — and given a sequence of recognized turn-consuming activities (a generic "a movement action was taken" event, and the historically mandatory periodic rest), Cluster 1 authoritatively advances the campaign's dungeon-turn counter according to the approved `EXP-002` accounting rule, itself enforcing the `EXP-004` mandatory-rest requirement, and — at the boundary of every elapsed turn — invokes the already-approved `EXP-001` procedure exactly once, producing its trigger/no-trigger outcome and audit data.

No monster is generated, no encounter is resolved, no map is produced, no light is consumed, no search/listen/door procedure runs, and no other historical procedure outside `EXP-001`/`EXP-002`/`EXP-004` is invoked by this cluster. Those are exactly the boundaries in §6.

## 14. Open Questions Requiring Human Review

1. Is the proposed three-item boundary (`EXP-001` + `EXP-002` + `EXP-004`) the intended scope, or should a narrow slice of `EXP-003` and/or `EXP-005` be pulled in explicitly rather than treated as already-covered by `EXP-002`?
2. Do the `EXP-003` and `EXP-005` splitting expectations in §9 look right, or should either be expected to stay a single card?
3. Is the "externally supplied movement capability" framing (deferring `CHAR-005` and spatial mapping entirely) acceptable for Cluster 1, or does the human reviewer want basic spatial movement included even at the cost of a larger cluster?
4. `EXP-007`'s dependency-direction question (§6, §21 of the accompanying report) — should the inventory's stated `EXP-002` dependency be corrected, left as-is pending `EXP-007`'s own future research, or is there a historical nuance (e.g., traps checked *during* a movement turn) that would restore a genuine turn-accounting relationship?
5. Should the minimal test-dungeon fixture (§8) be described in more detail now, or left entirely to implementation-time design once this cluster is accepted?

---

*This document proposes a cluster boundary for human review. It does not authorize Rule Card research, implementation, or production code for any item listed above.*
