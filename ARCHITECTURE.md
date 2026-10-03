# Retro D&D Simulator — Initial Architecture

## 1. Architectural Goal

The simulator should separate historical game rules from presentation so that rules behavior can be tested, reproduced, audited, and evolved without dependence on UI or narrative systems.

The initial architecture should favor correctness and testability over graphical sophistication.

## 2. Core Principle

> Simulation determines reality. Presentation describes reality.

The game engine must be capable of resolving an expedition without requiring graphical UI, narrative prose, or an LLM.

## 3. Proposed Layers

```text
Player / UI (deferred for the first vertical slice)
    ↓
Commands / Intent
    ↓
Simulation Engine
    ├── Rules (mechanical procedures, including generation procedures)
    ├── Random Number Source (single simulation-owned stream)
    ├── Campaign State
    ├── Dungeon State
    ├── Survivability Policy (structurally isolated — see §10)
    └── Event Generation
    ↓
Authoritative Simulation State / Events
    ├── Persistence Boundary → Storage Implementation (see §7)
    └── Presentation / Narrative Layer (deferred for the first vertical slice)
```

The previously proposed Application Layer between Commands/Intent and the Simulation Engine has been dropped from the initial architecture (see §13). Commands/Intent are consumed directly by the Simulation Engine for now. It may be reintroduced later, with a defined contract, if real command-handling complexity establishes a need for it.

## 4. Rules Layer

The rules layer contains implementations of approved mechanical procedures.

Examples:

- character generation;
- movement and dungeon turns;
- encounter checks;
- wandering-monster generation;
- surprise;
- reaction;
- morale;
- combat;
- spells;
- treasure generation;
- XP calculation;
- encumbrance;
- resource consumption.

Rules modules should be as pure and deterministic as practical.

They should not know how the result will be displayed.

For the initial architecture, procedures that generate content — including monster generation and treasure generation — are treated as ordinary rules procedures rather than as a separate `generation` layer. A dedicated generation boundary may be introduced later if implementation experience shows the distinction earns its keep (see §13).

Historically distinct procedures such as reaction, surprise, morale, pursuit/evasion, encounter generation, and combat must remain independently callable and independently testable rules procedures where the historical rules treat them as distinct systems. The architecture must not converge toward a single monolithic procedure (e.g., one fused `resolveEncounter()` function) that absorbs these distinctions internally. An encounter does not imply combat, and the boundaries between these systems are part of the rules fidelity the project exists to preserve.

## 5. Random Number Abstraction

All simulation randomness passes through a single, simulation-owned RNG abstraction.

```text
Campaign / Simulation
    └── RNG(seed)
```

For the initial implementation, the simulation uses one seeded RNG stream, owned by the campaign/simulation session. All historical random procedures — dice rolls, table lookups, checks — consume randomness through this shared, controlled source. Per-procedure or per-entity RNG streams are not used at this stage; that decision may be revisited later if implementation or debugging experience establishes a real need for it (see §13).

Requirements:

- seedable;
- injectable;
- deterministic in tests;
- suitable for replay/debugging;
- capable of supporting dice expressions and historical tables without coupling those tables to UI code;
- no hidden or uncontrolled random calls outside the abstraction anywhere in rules code.

The design should also make it practical to eventually diagnose or reproduce an individual random result, not only replay an entire campaign from its seed. The exact logging or replay representation needed for that does not need to be settled now.

## 6. Game State

Authoritative state should be explicit.

Likely state domains include:

### Campaign State

- calendar/time;
- party roster;
- living/dead/retired characters;
- town resources;
- discovered locations;
- rumors or known information;
- expedition history.

### Dungeon State

- dungeon identity;
- levels;
- rooms/areas;
- doors and passages;
- explored status;
- inhabitants;
- removed treasure;
- triggered/disarmed traps;
- persistent environmental changes.

### Character State

- attributes;
- class;
- level/XP;
- HP;
- equipment;
- encumbrance;
- spells;
- conditions;
- retainers or followers where applicable.

These domains describe authoritative in-memory simulation state. See §7 for how that state relates to persistent storage.

## 7. Persistence Boundary

Persistent consequences — dead characters remaining dead, recovered treasure remaining removed, explored areas remaining explored, changed dungeon conditions persisting, campaign state carrying over between expeditions (Constitution §11) — are fundamental to the game, not an optional later feature.

Persistence is therefore an architectural boundary from the beginning of the project, even though no storage technology is chosen yet and no persistence is implemented in the first vertical slice.

```text
Authoritative Simulation State
        ↓
Persistence Boundary
        ↓
Storage Implementation
```

- The Simulation Engine owns and mutates authoritative in-memory state (§6) and is unaware of how, or whether, that state is durably stored.
- The Persistence Boundary is the sole path by which authoritative state is read from or written to durable storage. Rules procedures must not read or write storage directly.
- Domain/state objects (Campaign, Dungeon, Character, etc.) must be designed around the needs of the simulation and its rules, not around the needs of any particular database, file format, or serialization technology.
- The first storage implementation, when it is built, is expected to be something simple and local. No database or storage technology is chosen at this stage, and no persistence implementation is in scope for the first vertical slice.

## 8. Events

Structured events describe significant simulation outcomes. They exist for testing, logging, future presentation, and possible replay/debugging — not as the mechanism by which state changes occur.

For the initial architecture:

- Simulation state (§6) is authoritative. It is the source of truth for what has happened.
- Rules procedures compute and commit authoritative outcomes and state transitions directly.
- Structured events are produced alongside those committed transitions to describe what significantly happened, in a form suitable for tests, logs, future presentation, and possible replay.
- Event ordering must be deterministic for a given seed and sequence of inputs.
- An emitted event must correspond to an outcome that has actually been committed to simulation state — events do not represent tentative, speculative, or rolled-back outcomes.

This is a deliberately lighter-weight model than full event sourcing. Events are not currently the state-change mechanism, there is no transactional event store, and state is not reconstructed by replaying an event log. That heavier model may be worth revisiting later, but it is not adopted now.

Illustrative examples:

```text
DungeonTurnElapsed
WanderingEncounterTriggered
MonsterGroupGenerated
SurpriseResolved
ReactionResolved
CombatRoundResolved
TrapTriggered
TreasureGenerated
TreasureRecovered
CharacterDied
ExperienceAwarded
```

Events should contain authoritative data, not only prose.

## 9. Encounter Pipeline

The encounter system must avoid assuming combat.

A possible high-level flow is:

```text
Encounter Check
    ↓
Encounter Occurs?
    ↓
Generate Creature Type
    ↓
Generate Number Appearing
    ↓
Resolve Surprise / Distance as Required
    ↓
Resolve Reaction When Required
    ↓
Present Situation
    ↓
Player Decision
    ├── Talk
    ├── Bargain
    ├── Avoid
    ├── Retreat
    ├── Follow
    └── Attack
```

Exact procedures remain governed by approved Rule Cards.

Each step above that corresponds to a historically distinct procedure (surprise, reaction, morale, pursuit/evasion) must remain a separately callable and separately testable rules procedure (§4). This diagram describes sequencing, not a single fused implementation.

## 10. Survivability Architecture

Survivability settings are a policy layer, not a replacement for historical tables.

```text
Historical Procedure
    ↓
Canonical Result
    ↓
Survivability Policy
    ↓
Final Result
```

This must be structural, not merely conventional:

- Only explicitly permitted result types may enter the survivability layer at all. A result type must be deliberately designed to accept a survivability policy; survivability must never be applicable "by default" to an arbitrary rules result.
- Treasure-generation and XP-award procedures must not accept a survivability policy parameter, and must expose no ordinary code path through which a survivability setting can alter their output. The canonical result of treasure generation and XP award **is** the final result, unconditionally, unless the project owner explicitly changes this policy (Constitution §8).
- The engine must retain enough information to distinguish the canonical result from the survivability-modified result for any result type that does pass through the survivability layer, so that the effect of the active policy is auditable (Constitution §9).

**Second-order concern.** Structural isolation of treasure and XP from direct modification is not sufficient by itself. Survivability accommodations must also not be implemented through indirect mechanisms that change reward availability as a side effect — for example, rerolling, suppressing, or substituting canonical encounters specifically because they would have produced treasure, in a way that changes what treasure or XP becomes available compared to the canonical, unmodified procedure. Survivability policy may change danger and survival odds; it must not change what the historical procedures would have made available to a party that survives to recover it.

Exact survivability mechanics — which specific settings exist, what they modify, and how — are not decided by this document and remain to be specified through approved Rule Cards and design decisions.

## 11. Narrative Layer

Narrative presentation is downstream from simulation.

Possible responsibilities:

- room descriptions;
- atmospheric text;
- monster behavior descriptions;
- conversation phrasing;
- summarizing combat outcomes;
- expedition journals.

An LLM may eventually be used here, but the initial game must not require one.

The narrative layer cannot override authoritative simulation results.

## 12. Rule Cards

Rules documentation lives separately from implementation code.

Suggested location:

```text
docs/rules/
    character_creation/
    exploration/
    encounters/
    combat/
    magic/
    monsters/
    treasure/
```

Rule Cards should be sufficiently precise that an implementation agent can code from them without inventing mechanics.

**Rule Cards are a formal human-approval gate, not merely a documentation convention.** A Rule Card's `Status` field (SOURCE_HIERARCHY.md §9) governs whether it may be implemented:

- A Rule Card is not authoritative, and must not be implemented, until a human project owner sets its Status to `APPROVED`.
- Draft, in-review, or otherwise unapproved Rule Cards may be researched, discussed, and iterated on, but implementation must not begin from them.
- Implementation agents may implement only the mechanical specification of an `APPROVED` Rule Card.
- If implementation requires behavior that is absent from, or ambiguous in, an `APPROVED` Rule Card, implementation must stop at that boundary and report the gap rather than inventing or extending a ruling (Constitution §3, AGENTS.md §3).

No specific runtime mechanism (such as a dedicated error type for unresolved-rule boundaries) is defined at this stage. That may become useful once real implementation experience shows a need for it, but it is not designed prematurely.

A Rule Card's documented mechanical test cases are part of the acceptance criteria for its implementation, not a separate, optional addition (`TESTING_STRATEGY.md` §2).

The required Rule Card shape is maintained at `docs/rules/_template.md`. Creating and maintaining that template — and researching and drafting individual Rule Cards from it — is governance/specification documentation, not production code, and is therefore permitted before the Pre-Code Development Gate clears (§16). Implementing a Rule Card's approved mechanical specification is production code and remains gated regardless of the card's own approval status.

## 13. Proposed Minimum Module Layout

For the first vertical slice (§14) only — this is not the full future application, and it will very likely grow additional boundaries once real implementation experience justifies them.

```text
retro-dnd/
├── CLAUDE.md
├── AGENTS.md
├── GAME_CONSTITUTION.md
├── SOURCE_HIERARCHY.md
├── ARCHITECTURE.md
├── DEVELOPMENT_WORKFLOW.md
├── TESTING_STRATEGY.md
├── pyproject.toml       # created — project metadata, dependencies, tool config
├── uv.lock              # created — committed, per DEC-0003
├── .gitignore           # created
├── .github/
│   └── workflows/
│       └── ci.yml       # created — invokes scripts/verify.py (DEC-0003, gate item 8)
├── scripts/
│   ├── verify.py         # created — the canonical verification command (§8 of
│   │                      #   docs/technical/TOOLCHAIN_AND_CI.md)
│   └── check_coverage.py # created — differentiated coverage-threshold enforcement
├── docs/
│   ├── rules/
│   │   └── _template.md        # created — required Rule Card shape
│   ├── decisions/
│   │   ├── INDEX.md            # created
│   │   └── DEC-0001-project-foundation-baseline.md   # created
│   ├── technical/
│   │   ├── TOOLCHAIN_AND_CI.md  # created — approved (DEC-0003; gate item 8)
│   │   └── RNG_CONTRACT.md      # created — approved (DEC-0002; gate item 7)
│   └── completion-records/     # created — see ISSUE-001
├── src/
│   ├── rng/            # created (ISSUE-001) — seedable/injectable RNG abstraction,
│   │                    #   dice expressions
│   ├── rules/           # mechanical procedures: chargen, turns, encounter check,
│   │                     #   monster/number-appearing generation, surprise, reaction,
│   │                     #   morale, combat, treasure generation, XP — generation
│   │                     #   procedures live here too, not in a separate layer
│   ├── state/           # Campaign/Dungeon/Character state types; in-memory for now
│   ├── survivability/    # policy layer; only explicitly permitted result types pass
│   │                     #   through it (see §10); treasure/XP never do
│   └── events/           # event type definitions and in-memory event log
└── tests/
    ├── rng/              # created (ISSUE-001)
    └── rules/           # one test module per rules procedure, deterministic-seed based
```

The `docs/rules/_template.md` and `docs/decisions/` files above now exist, per the foundational governance decisions recorded in `docs/decisions/DEC-0001-project-foundation-baseline.md`. The `docs/technical/` documents are approved (`DEC-0002`, `DEC-0003`), addressing Pre-Code Development Gate items 7–8 (§16). Following Issue 1 (`docs/completion-records/ISSUE-001-rng-dice-infrastructure.md`), the project's toolchain (`pyproject.toml`, `uv.lock`, `.gitignore`), canonical verification scripts, CI workflow, `src/rng/`, `tests/rng/`, and `docs/completion-records/` all now exist. The remaining `src/` and `tests/` subdirectories (`rules`, `state`, `survivability`, `events`) are created as later issues implement them.

This structure is intentionally smaller than earlier drafts of this document proposed. The following divisions are deferred, not rejected — they may be introduced later if the codebase demonstrates a real need for them:

- **Application Layer** — dropped from the initial architecture. Commands/Intent are consumed directly by the Simulation Engine for now (§3).
- **`engine`** — not split out from `rules` initially; there is not yet enough code for the boundary to earn its keep.
- **`generation`** — generation procedures (monster generation, treasure generation, dungeon layout generation) are treated as rules procedures initially, not a separate layer (§4).
- **`world`** — folded into `state` until a real need for separation appears.
- **`presentation`** — deferred entirely for the first vertical slice (§11). The slice's "leave the dungeon" step and similar can be a test assertion or minimal output, not a package.

**No rules-version or historical-edition abstraction.** Do not build a runtime abstraction for switching among historical D&D editions or rules versions (e.g., a generic "ruleset" interface selecting between OD&D/Holmes/B/X/BECMI/Rules Cyclopedia behavior). The source hierarchy (SOURCE_HIERARCHY.md) governs *research methodology* for arriving at a single approved mechanical specification per Rule Card; it does not imply the simulator should support multiple simultaneous rules editions at runtime.

## 14. Initial Vertical Slice

The first playable milestone should prove the core expedition loop with minimal presentation.

Target capabilities:

1. create a small party;
2. purchase or assign basic equipment;
3. enter a dungeon level;
4. advance dungeon turns;
5. consume relevant resources;
6. trigger wandering-monster checks;
7. generate monsters using approved historical procedures;
8. resolve surprise and reaction where applicable;
9. permit combat or noncombat responses;
10. generate treasure using approved procedures;
11. leave the dungeon;
12. award experience.

Do not begin with a large procedural world, graphical polish, or AI narration.

If this loop is historically defensible, reproducible, and enjoyable, the project has validated its core architecture.

## 15. Approved Implementation Sequence

**Issue 1 — RNG and Dice Infrastructure.** Define and implement the simulation-owned RNG abstraction (§5) and dice-expression support. This is infrastructure, not a historical game rule, and requires no Rule Card. The technical design for the RNG contract is approved (`docs/technical/RNG_CONTRACT.md`, `docs/decisions/DEC-0002-rng-contract.md`). **Completed** — `docs/completion-records/ISSUE-001-rng-dice-infrastructure.md` (and its defect-fix follow-up, `docs/completion-records/ISSUE-002-scripted-rng-die-range-validation-fix.md`).

**Issue 2 — Rule Card Infrastructure and First Rule Card.** The Rule Card template (`docs/rules/_template.md`) already exists; this issue is to draft and carry exactly one Rule Card through the full research-and-approval workflow to `APPROVED` status (§12). **Completed** — `docs/rules/exploration/dungeon_wandering_monster_check.md` (Rule ID `EXP-001`) was approved 2026-08-15, demonstrating the complete workflow end to end for the first time:

```text
Historical Source
      ↓
Research
      ↓
Rule Card Draft
      ↓
Human Review
      ↓
APPROVED Rule Card
      ↓
Implementation
      ↓
Deterministic Tests
      ↓
Rules Audit
```

**Issue 3 — V1 Rules Inventory and Dependency Map.** Produce and maintain a master inventory of every Rule Card (or coherent grouping) reachable from the initial vertical slice's dungeon-crawl loop (§14) — proposed Rule Card/grouping, rules domain, key historical source, known dependencies, whether it is required for v1, current research/approval status, ambiguity/research-risk flags, and a suggested research order. This does not require deep research of every item; its purpose is to establish the backlog and make dependency relationships visible before cluster selection (§15.1). **Completed** — `docs/rules/INVENTORY.md` is `APPROVED` and merged, and is the basis for cluster selection going forward.

## 15.1 V1 Rules Inventory and Dependency-Complete Implementation Clusters

Supersedes the section previously written here, which required the entire v1 Rule Card corpus to be `APPROVED` before any historical-rules implementation could begin (`docs/decisions/DEC-0004-full-v1-rules-corpus-before-implementation.md`, itself now superseded — see `docs/decisions/DEC-0005-v1-rules-inventory-and-clustered-implementation.md` for the full rationale). Neither of two considered extremes is the approved policy:

- **not** implementing each Rule Card immediately after its own individual approval — risks discovering, mid-implementation, that a later, dependent rule changes an earlier implementation's assumptions, forcing rework and encouraging premature interfaces;
- **not** requiring the entire v1 corpus to be researched and approved before any implementation begins — defers all implementation/integration feedback until the whole corpus is frozen, and risks specifications that have never been exercised together.

The approved policy is a hybrid, dependency-aware **cluster** workflow:

```text
Complete V1 Rules Inventory
        ↓
Select coherent rules cluster
        ↓
Research all Rule Cards required by that cluster
        ↓
Resolve ambiguities
        ↓
Human-approve the cluster's Rule Cards
        ↓
Implement and integrate the cluster
        ↓
Verify / test / learn from integration
        ↓
Select next cluster
```

**Prerequisite.** Before any cluster is selected, a complete V1 Rules Inventory and Dependency Map must exist and be human-reviewed (`docs/rules/INVENTORY.md`) — every historical rule, table, special case, and dependency reachable from the v1 dungeon-crawl loop (§14) identified and classified. This does not require every item to be researched or approved yet, only identified. Explicitly outside initial v1 scope unless a genuine in-scope dependency requires otherwise: wilderness campaign procedures, the Outdoor Survival map procedure, naval combat, aerial combat, stronghold/domain management, baronies/taxation, large-scale warfare, and other endgame campaign systems unrelated to the dungeon-expedition loop.

**A cluster is ready for implementation only when:**

1. its intended behavioral scope is clearly defined;
2. all historical rules directly required to execute that scope have been identified;
3. all Rule Cards required by that scope are `APPROVED`;
4. any external dependency not implemented in the cluster has a stable approved contract sufficient for integration;
5. no unresolved rules ambiguity remains that the implementation agent would need to adjudicate itself.

Do not implement a historical subsystem while a Rule Card its own cluster requires remains unresolved. An individually approved Rule Card — including `EXP-001` — does not by itself authorize implementation; it waits for its cluster to become dependency-complete, the same way an approved Rule Card never overrides the Pre-Code Development Gate (§16). `EXP-001`'s likely first cluster is an exploration/time subsystem — dungeon-turn accounting, movement/time consumption, searching/time consumption, mandatory rest, combat-round-to-turn accounting, wandering-monster check timing, and light-duration interaction if the dependency analysis shows it belongs — but this list is illustrative, not final; the inventory and dependency analysis determine the actual cluster boundary.

Implementation/integration feedback from a completed cluster is fed back into the inventory and later Rule Cards through the established governance process (Rule Card revision, or a new decision record, as appropriate) — never used to silently adjust a cluster already in progress.

## 15.2 Rules Baseline Migration Gate (added 2026-08-16)

`DEC-0007-rules-cyclopedia-primary-rules-authority.md` replaced the 1974 three-book OD&D core with the Rules Cyclopedia as the project's primary rules authority. See `docs/rules/RULESET_BASELINE_MIGRATION.md` for the full migration record.

This does not erase the fact that a V1 Rules Inventory (`docs/rules/INVENTORY.md`) and a first cluster, `CLUSTER-001` (dungeon exploration time — `EXP-001`, `EXP-002`, `EXP-004`), were previously researched, human-approved, and merged under the superseded 1974-primary policy. Both remain in the repository as a historical record of completed work and are not deleted or rewritten. As of this gate's original 2026-08-16 addition, neither carried implementation authority: both were marked `REVALIDATION_REQUIRED` (`DEVELOPMENT_WORKFLOW.md` §9.7), pending review against the current source hierarchy. **This is no longer true of the revised, two-item `CLUSTER-001` boundary specifically — see "Status update (2026-08-18)" below**, which does not apply to `EXP-004` or to the original three-item boundary referenced in this paragraph.

The progression toward Cluster 1 implementation described in §15.1 is **suspended**, replaced by:

```text
Rules Baseline Migration (this gate)
        ↓
Rules Cyclopedia governance established
        ↓
V1 Rules Inventory revalidated/rebuilt against the Rules Cyclopedia
        ↓
human approval of the revised inventory
        ↓
existing Rule Cards / clusters revalidated, or new ones selected, per §15.1's cluster workflow
        ↓
human approval
        ↓
implementation readiness (re-)approved
        ↓
historical-rules implementation
```

`§15.1`'s cluster-workflow *mechanics* (inventory-first, dependency-complete clusters, the five readiness criteria) remain the approved process and are not superseded by this gate — only the specific inventory and cluster content produced under the prior source authority require revalidation before that process's outputs can authorize implementation again.

**Historical-rules implementation authorization: FROZEN** until: (1) a Rules Cyclopedia V1 Rules Inventory is approved; (2) affected cluster boundaries are approved/revalidated under that inventory; (3) all Rule Cards required by the first revised cluster are approved under the current hierarchy; (4) implementation readiness is (re-)approved for that cluster. No `APPROVED` (or `IMPLEMENTATION_READY`) metadata dated under the superseded policy bypasses this freeze — see `DEC-0007`'s Consequences.

**Status update (2026-08-16).** Step (1) is complete: `docs/rules/INVENTORY.md` (rebuilt against the Rules Cyclopedia, with a companion coverage audit `docs/rules/RC_V1_SCOPE_AUDIT.md` and migration map `docs/rules/INVENTORY_MIGRATION_MAP.md`) is now `APPROVED`. This approval satisfies step (1) only — it does **not** clear this gate as a whole and does **not** reauthorize historical-rules implementation on its own. Steps (2)–(4) remain entirely unaddressed: no cluster boundary has been (re-)approved, no Rule Card has been revalidated under the current hierarchy, and implementation readiness has not been (re-)approved for any cluster. The freeze continues in force.

**Status update (2026-08-18) — `CLUSTER-001` steps (2)–(4) now satisfied.**

- **Step 1 — Rules Cyclopedia V1 inventory:** `COMPLETE / APPROVED` (unchanged from 2026-08-16, above).
- **Step 2 — revised `CLUSTER-001` boundary:** `COMPLETE / APPROVED`. Current boundary: `EXP-001` (Dungeon Wandering-Monster Check) + `EXP-002` (Dungeon Turn / Time Accounting) — see `docs/rules/clusters/CLUSTER-001-dungeon-exploration-time.md`, Current section. `EXP-004` remains `REVALIDATION_REQUIRED` and is **not** part of `CLUSTER-001`.
- **Step 3 — required Rule Cards:** `COMPLETE`. `EXP-001 = APPROVED`, human-approved 2026-08-18. `EXP-002 = APPROVED`, human-approved 2026-08-16.
- **Step 4 — implementation readiness:** `RE-APPROVED`, human-approved 2026-08-18. Authoritative implementation plan: `docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` (Human Implementation-Plan Review: `APPROVED`, 2026-08-18).

**The governance distinction is explicit: this clears the migration-era freeze for `CLUSTER-001` only.** It does not state or imply that historical-rules implementation is now globally unrestricted. Every other cluster, and every Rule Card not part of `CLUSTER-001`'s two-item boundary, remains governed by §15.1 and this gate exactly as before, and must independently satisfy the same four steps — including its own cluster boundary (re-)approval, its own Rule Cards' approval under the current hierarchy, and its own implementation-readiness (re-)approval — before any implementation authorization applies to it. `ARCHITECTURE.md` §16's general Pre-Code Development Gate is unaffected and remains active project-wide; this status update does not weaken or bypass it — it records that `CLUSTER-001` has, in addition, individually satisfied §15.2's own four migration-gate steps.

**`CLUSTER-001` HISTORICAL-RULES IMPLEMENTATION: `AUTHORIZED` — 2026-08-18.** This authorization applies only to the human-approved `EXP-001` + `EXP-002` `CLUSTER-001` boundary and its approved implementation plan (`docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md`). It does not authorize implementation of `EXP-004`, another Rule Card, or another cluster.

**`CLUSTER-001` IMPLEMENTATION / INTEGRATION: `VERIFIED` — 2026-08-18.** The authorized `EXP-001` + `EXP-002` `CLUSTER-001` implementation is complete and verified. Steps 1–4 of the approved implementation plan and their required completion records (`docs/completion-records/ISSUE-003` through `ISSUE-006`, summarized in `ISSUE-007`) are complete, and the cross-card integration gate passes using the real production components. This does not authorize or select another cluster; subsequent historical-rules work must independently satisfy the existing cluster workflow and governance gates above, exactly as before. The general Pre-Code Development Gate (§16) and the per-cluster Rules Baseline Migration Gate requirement are unaffected and remain active project-wide.

**Status update (2026-09-12) — `CLUSTER-002` steps (2)–(4) now satisfied.**

- **Step 1 — Rules Cyclopedia V1 inventory:** `COMPLETE / APPROVED` (unchanged from 2026-08-16, above).
- **Step 2 — `CLUSTER-002` boundary:** `COMPLETE / APPROVED`, human-approved 2026-08-23. Boundary: `CHAR-001` (Ability Score Generation) + `CHAR-002` (Race & Class Eligibility) + `CHAR-003` (Hit Points & Hit Dice) + `CHAR-007` (General Ability Score Mechanical Effects) — see `docs/rules/clusters/CLUSTER-002-character-foundation.md`.
- **Step 3 — required Rule Cards:** `COMPLETE`. All four `APPROVED`, human-approved 2026-09-04; `CHAR-001` additionally **amended 2026-09-05** (trade rule `R11`, the prime-requisite ceiling, and cases `C1`–`C5`), remaining `APPROVED` throughout.
- **Step 4 — implementation readiness:** `RE-APPROVED`, human-approved 2026-09-12. Authoritative implementation plan: `docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` (Human Implementation-Plan Review: `APPROVED`, 2026-09-12, revision 3).

**`CLUSTER-002` HISTORICAL-RULES IMPLEMENTATION: `AUTHORIZED` — 2026-09-12.** This authorization applies only to the human-approved four-card `CLUSTER-002` boundary and its approved implementation plan. It does not authorize another Rule Card or another cluster, and the same governance distinction recorded for `CLUSTER-001` above applies unchanged: clearing these four steps for one cluster states nothing about any other.

**`CLUSTER-002` IMPLEMENTATION / INTEGRATION: `VERIFIED` — merged 2026-09-13.** The approved plan's Slices A–F are complete and verified. All four Rule Cards are implemented, all **189** approved deterministic contract cases are canonically reconciled with exactly one owner each, and the required completion records (`docs/completion-records/ISSUE-008` through `ISSUE-013`, summarized in `ISSUE-014`) are in place.

- **Human final branch review:** `PASS`, 2026-09-12, at `c4e5fc8e54caa08be7f9c57a21bfe3218029277e`.
- **Merged to `main`:** 2026-09-13, by a single `--no-ff` merge.
- **Merge commit:** `8d26eb07e3ccb0c59f1d9e9cc8ffcb1b43f40bf2`.
- **Canonical verification:** `PASS` — `uv run python scripts/verify.py` (tests, coverage, Ruff, mypy strict), run on `main` immediately after the merge.

This does not authorize or select another cluster; subsequent historical-rules work must independently satisfy the cluster workflow and governance gates above, exactly as before. §15.1 and §15.2 remain **readiness** gates — §15.2 step 4 records that implementation readiness was re-approved on 2026-09-12, which is not itself the completion event; this paragraph is. The general Pre-Code Development Gate (§16) and the per-cluster Rules Baseline Migration Gate requirement are unaffected and remain active project-wide.

**Status update (2026-09-24) — `CLUSTER-003` steps (2)–(3) satisfied; step (4) NOT given.**

- **Step 1 — Rules Cyclopedia V1 inventory:** `COMPLETE / APPROVED` (unchanged from 2026-08-16, above).
- **Step 2 — `CLUSTER-003` boundary:** `COMPLETE / APPROVED`, human-re-approved 2026-09-14. Boundary: `CHAR-004` (Starting Equipment & Expedition Preparation) + `CHAR-005` (Encumbrance & Movement Rate) + `EXP-003` (Dungeon Movement) — see `docs/rules/clusters/CLUSTER-003-equipped-dungeon-movement.md`. `CHAR-006`, `CHAR-008`, `CHAR-009` and `EXP-010` are explicitly **outside** the boundary, and the boundary-reopen condition raised on 2026-09-13 was resolved by a narrow ownership correction rather than by adding a card.
- **Step 3 — required Rule Cards:** `COMPLETE`. All three `APPROVED`, human-approved 2026-09-24. The cluster carries five Simulator Rulings (`SR-6`–`SR-10`, continuing the project sequence from `CLUSTER-002`'s `SR-1`–`SR-5`); two further determinations — running speed and exact fractional Mystic encounter movement — are **`Rules Cyclopedia Explicit` interpretation plus necessary consequence and are expressly not rulings**.
- **Step 4 — implementation readiness:** **NOT (RE-)APPROVED.** No authoritative implementation plan exists for `CLUSTER-003`, and none was drafted: drafting one is not a required artifact of this gate (`docs/technical/CLUSTER-003_PRE_CODE_GATE.md` §1.2).

**`CLUSTER-003` PRE-CODE GATE: `PASS` — 2026-09-24.** The per-cluster readiness assessment against §15.1's five criteria and this section's steps 1–3 is recorded at `docs/technical/CLUSTER-003_PRE_CODE_GATE.md`: **no blocking defects**, three non-blocking implementation cautions. **This `PASS` is a readiness finding, not an authorization.**

**`CLUSTER-003` HISTORICAL-RULES IMPLEMENTATION: `NOT AUTHORIZED`.** Step (4) above is outstanding and is a human act. The governance distinction recorded for `CLUSTER-001` and `CLUSTER-002` applies unchanged: clearing steps for one cluster states nothing about any other, and §16's general Pre-Code Development Gate — already `CLEARED` project-wide — is neither re-performed nor weakened by this entry.

**Status update (2026-10-01) — `CLUSTER-004` step (3) satisfied for `EXP-006` only; steps (2)–(4) otherwise outstanding.**

- **Step 1 — Rules Cyclopedia V1 inventory:** `COMPLETE / APPROVED` (unchanged from 2026-08-16, above).
- **Step 2 — `CLUSTER-004` boundary:** `APPROVED` 2026-09-27 — `EXP-006` + `ENC-005`; see `docs/rules/clusters/CLUSTER-004-BOUNDARY-CORRECTION.md`. `EXP-004` and `EXP-010` are explicitly **outside** it. **`ENC-005` Stage B is `DEFERRED`** — five of its six executable checklist steps depend on unresearched provider cards, materially the reason `EXP-010` was deferred — so the cluster's card set is **not** complete.
- **Step 3 — required Rule Cards:** **PARTIAL.** `EXP-006` `APPROVED` 2026-10-01, after a bounded Stage-B remediation of three synthesis defects at the mundane-light / world-illumination boundary. **The card carries exactly one Simulator Ruling — `SR-11`** (the adverse-condition `Fire-Building` branch governs regardless of a tinderbox; added 2026-10-01 to resolve an RC ambiguity the accepted evidence exposed) — and **no `Alternate-Source Compatible Completion` and no `Human-Approved Variant`**. `ENC-005` has `ACCEPTED` Stage-A evidence but **no Rule Card**.
- **Step 4 — implementation readiness:** **`EXP-006` only.** `docs/technical/EXP-006_IMPLEMENTATION_PLAN.md` is **`APPROVED`** (human project owner, 2026-10-01), and its four slices are implemented and human-accepted. **No `CLUSTER-004` plan exists**, and `ENC-005` has none.

> **Correction, 2026-10-03.** This entry previously stated that the card "carries no Simulator Ruling" and that "no implementation plan exists" for `EXP-006`. Both were false when written and are corrected above: `SR-11` is registered in the Rule Card, the `CLUSTER-004` record, `INVENTORY.md` and the plan, and the plan was approved the same day. Found by the independent final implementation review (`HIGH-1`). The denial mattered more than an omission would have: the card's own ID-allocation reasoning treats *prior textual denials* as the evidence distinguishing an allocated `SR` from a free one.

**`EXP-006` IMPLEMENTATION: COMPLETE — 2026-10-03, pending a passing independent final review.** All four plan slices are implemented and human-accepted (A–D). The first independent final implementation review returned **`FAIL`** (2 HIGH, 4 MED, 8 LOW — `docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW.md`, preserved unaltered); **no finding concerned rules logic**, which that review verified against the card by mutation testing. **`EXP-006-PHASE: REVIEW-3-REMEDIATED`.** **Three independent final implementation reviews have now been performed, and all three returned `FAIL`** — review #1 (2 HIGH, 4 MED, 8 LOW), review #2 (2 HIGH, 5 MED, 11 LOW) and review #3 (1 HIGH, 4 MED, 8 LOW), each preserved unaltered at `docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW{,_2,_3}.md`. **None of the three found a rules-conformance defect.** Each independently re-derived the contract from the approved card and ran its own behavioural and state-space mutations; every finding in all three concerned the **self-description layer** — docstrings, audit ledgers, case tables, status records, and the breadth of guard claims. All three remediations are recorded (`EXP-006_REVIEW_REMEDIATION_LEDGER.md`, `..._REVIEW_2_...`, `..._REVIEW_3_...`), and `ISSUE-022` — the authoritative current status — states the issue is **NOT COMPLETE**.

**Two review-#3 findings remain open** and require human adjudication, because both touch **protected** approved Rule Cards: `LOW-3` (`CHAR-005` still carries both "there is no `SR-11`" denials) and `LOW-8` (the `EXP-006` card's retained pre-approval sentence). Both are documentation-only.

**The guard arms race is closed by human direction (2026-10-03).** The project now distinguishes a *machine-enforced invariant*, a *machine-enforced observed surface*, and a *reviewed architectural ownership boundary*, and no longer presents the third as the first. Overbroad guard claims were **narrowed** rather than answered with broader mechanisms; **no fourth-generation universal architecture guard is authorized**, and a future reviewer finding another Python construct outside a guard's explicitly narrow claim is a limitation, not by itself a defect.

A fourth independent review is **not yet authorized**, and acceptance is a human act. **`CLUSTER-004` implementation remains `NOT AUTHORIZED`** — §15.2 step 4 is satisfied for `EXP-006`'s own plan only, and merge is a separate human act.

**`EXP-006` PRE-CODE GATE: `PASS` — 2026-10-01.** The per-card readiness assessment against §15.1's five criteria is recorded at `docs/technical/EXP-006_PRE_CODE_GATE.md`: **no blocking defects**, three non-blocking implementation cautions. The card consumes only **landed** cards (`EXP-002`, `CHAR-004`); every unresearched dependency is **downstream-only** and is never called by `EXP-006`. **This `PASS` is a readiness finding, not an authorization**, and it is scoped to `EXP-006` alone — it states nothing about `ENC-005` or about `CLUSTER-004` as a whole.

**`CLUSTER-004` HISTORICAL-RULES IMPLEMENTATION: `NOT AUTHORIZED`.** Steps (2)–(4) are outstanding and step (4) is a human act. The governance distinction recorded for `CLUSTER-001`, `CLUSTER-002` and `CLUSTER-003` applies unchanged, and §16's general Pre-Code Development Gate — already `CLEARED` project-wide — is neither re-performed nor weakened by this entry.

## 16. Pre-Code Development Gate

Production code must not begin — including Issue 1 (§15) — until a human has reviewed and approved each of the following foundational items:

1. the revised architecture (`ARCHITECTURE.md`);
2. the historical source/provenance workflow (`SOURCE_HIERARCHY.md`);
3. the Rule Card format and approval process (`SOURCE_HIERARCHY.md` §9, `docs/rules/_template.md`, §12 above);
4. the completed-work documentation standard (`DEVELOPMENT_WORKFLOW.md`);
5. the testing and coverage strategy (`TESTING_STRATEGY.md`);
6. the decision-record process (`DEVELOPMENT_WORKFLOW.md` §9, `docs/decisions/`);
7. the RNG technical contract — approved: `docs/technical/RNG_CONTRACT.md`, recorded as `docs/decisions/DEC-0002-rng-contract.md`;
8. the automated verification/CI enforcement model appropriate to the selected implementation toolchain — approved: `docs/technical/TOOLCHAIN_AND_CI.md`, recorded as `docs/decisions/DEC-0003-python-toolchain-and-ci.md` (`TESTING_STRATEGY.md` §9).

The Rule Card template (item 3) is governance/specification documentation, not production code: it may be created and used, and individual Rule Cards may be researched, drafted, and approved, before this gate clears (§12). **Implementing** an approved Rule Card's mechanical specification is production code and remains blocked until this gate clears — an approved individual Rule Card never independently overrides this project-level gate.

### 16.1 Gate Status: CLEARED

As of 2026-08-15, all eight items above have been reviewed and approved by the project owner (`docs/decisions/DEC-0001-project-foundation-baseline.md`, `docs/decisions/DEC-0002-rng-contract.md`, `docs/decisions/DEC-0003-python-toolchain-and-ci.md`). **The Pre-Code Development Gate is CLEARED.**

Clearing this gate is a statement about the foundational documents, not an authorization to begin implementation. Production-code work on Issue 1 (§15) still requires a separate, explicit human authorization to begin — clearing the gate removes the *precondition* for that authorization; it does not substitute for it. A small number of implementation-phase details remain intentionally open even after clearing (e.g., `docs/technical/TOOLCHAIN_AND_CI.md` §12) — these do not block the gate and are expected to be resolved during Issue 1 itself, not before it starts.

This project-level gate remaining `CLEARED` is necessary but not sufficient for any individual cluster's implementation — each cluster additionally requires its own separate authorization under §15.2's Rules Baseline Migration Gate. `CLUSTER-001` (§15.2, "Status update (2026-08-18)") and `CLUSTER-002` (§15.2, "Status update (2026-09-12)") have each received that separate authorization; no other cluster or Rule Card has, and this gate's clearance does not extend implementation authorization to any of them.

## 17. First Agent Assignment (Completed)

*This section records the instructions given for the initial architecture review. That review has been completed, and its findings were incorporated into this revision of the document. It is retained here as a historical record rather than a live instruction.*

Before writing production code, the implementation agent should be asked to review this architecture and report:

- unnecessary complexity;
- missing boundaries;
- testability problems;
- likely coupling risks;
- places where rules ambiguity could leak into code;
- a proposed minimum viable package/module layout.

The agent should not modify files during this first architecture review.
