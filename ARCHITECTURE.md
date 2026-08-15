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

**Issue 3 — V1 Rules Inventory and Dependency Map.** Produce and maintain a master inventory of every Rule Card (or coherent grouping) reachable from the initial vertical slice's dungeon-crawl loop (§14) — proposed Rule Card/grouping, rules domain, key historical source, known dependencies, whether it is required for v1, current research/approval status, ambiguity/research-risk flags, and a suggested research order. This does not require deep research of every item; its purpose is to establish the backlog and make dependency relationships visible before cluster selection (§15.1). Drafted — `docs/rules/INVENTORY.md` — pending human review before further Rule Card production or cluster selection proceeds.

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
