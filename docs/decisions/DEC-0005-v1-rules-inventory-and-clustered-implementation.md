# DEC-0005: V1 Rules Inventory and Dependency-Complete Implementation Clusters

## Decision ID
DEC-0005

## Title
V1 Rules Inventory and Dependency-Complete Implementation Clusters

## Status
Approved

## Date
2026-08-15

## Context

`DEC-0004` (2026-08-15) required the complete v1 Rule Card corpus to be researched and `APPROVED` before any historical-rules implementation could begin, to prevent an implementation agent from encountering an unresolved dependency mid-task. The V1 Rules Inventory and Dependency Map produced under that decision (`docs/rules/INVENTORY.md`) exists and has been drafted.

On further consideration, requiring the *entire* corpus to be resolved before *any* implementation begins defers all implementation and integration feedback until the whole corpus is frozen — risking specifications that have never been exercised together, and delaying the discovery of integration problems far longer than necessary. This decision refines the sequencing policy to a hybrid, dependency-aware cluster model that keeps `DEC-0004`'s core discipline (no implementation-agent rules invention; dependencies known before code is written) while allowing implementation experience from an early, coherent subsystem to inform later specification work.

## Decision

**Do not adopt a policy requiring the entire v1 Rule Card corpus to be researched and approved before any historical-rules implementation may begin. Likewise, do not return to implementing individual Rule Cards immediately after each one is approved. The approved approach is a hybrid, dependency-aware cluster workflow.**

**1. Inventory first, retained from `DEC-0004`.** Before further historical-rules implementation begins, a complete V1 Rules Inventory and Dependency Map must exist and be human-reviewed. "Complete" means every historical rule, table, special case, and dependency reachable through the intended v1 dungeon-crawl loop is *identified and classified* — not that each is yet researched or approved:

```text
Create / maintain party
        ↓
Prepare and equip expedition
        ↓
Enter generated / stocked dungeon
        ↓
Explore under dungeon procedures
        ↓
Encounter monsters / traps / features
        ↓
Negotiate / evade / fight / otherwise resolve
        ↓
Find and recover treasure
        ↓
Exit dungeon
        ↓
Award XP / level / recover / resupply
        ↓
Begin another expedition
```

If an in-scope procedure can generate, invoke, or depend upon another mechanical behavior, that dependency must appear in the inventory (e.g., dungeon treasure generation may produce a magic item, bringing applicable magic-item behavior into scope; dungeon monster generation may produce a monster with a special ability, bringing that ability into scope).

Explicitly outside initial v1 scope, unless required by an in-scope dungeon-crawler dependency: wilderness campaign procedures, the Outdoor Survival map procedure, naval combat, aerial combat, stronghold/domain management, baronies/taxation, large-scale warfare, and other endgame campaign systems unrelated to the dungeon-expedition loop. If an apparently excluded system becomes a genuine dependency of an in-scope rule, that is flagged for human review, not silently absorbed.

**2. After the inventory is reviewed and accepted, work proceeds in dependency-complete clusters**, not corpus-wide and not card-by-card:

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

Do not implement a historical subsystem while a Rule Card its own cluster requires remains unresolved. Implementation/integration feedback may reveal missing dependencies or specification issues; that feedback refines the inventory and later Rule Cards through the established governance process (Rule Card revision, or a new decision record), not by silently altering a cluster already in progress.

**3. A cluster is ready for implementation only when:**

1. its intended behavioral scope is clearly defined;
2. all historical rules directly required to execute that scope have been identified;
3. all Rule Cards required by that scope are human-approved;
4. any external dependency not implemented in the cluster has a stable approved contract sufficient for integration;
5. no unresolved rules ambiguity remains that the implementation agent would need to adjudicate itself.

The goal: no rules invention during implementation, while still obtaining implementation/integration feedback before the entire v1 corpus is finished.

**4. Example (illustrative, not final).** `EXP-001` (Dungeon Wandering-Monster Check) is `APPROVED` but is not implemented on its own. Its likely first cluster is an exploration/time subsystem, which may include — subject to the dependency analysis actually determining the boundary — dungeon-turn accounting, movement/time consumption, searching/time consumption, mandatory rest, combat-round-to-turn accounting, wandering-monster check timing, and light-duration interaction if the dependency analysis shows it must be included for a coherent subsystem. `EXP-001` remains approved and waits for its required exploration dependencies.

## Rationale

Two failure modes are being deliberately avoided:

**Failure Mode A — rule-by-rule implementation:** approve one Rule Card → implement immediately → later discover a dependent rule changes its assumptions → rework earlier implementation. This creates unnecessary integration churn and encourages premature interfaces.

**Failure Mode B — entire-corpus freeze before any implementation** (`DEC-0004`'s original policy): research every v1 rule → approve everything → only then discover integration/interface problems. This delays implementation feedback too long and risks freezing specifications that have never been exercised together.

The approved middle ground: know the whole v1 rules landscape, finish one coherent dependency set, implement and integrate it, use what is learned on the next dependency set. This preserves historical rigor (no card is implemented with an unresolved dependency) while allowing implementation experience to inform later specification work — closer in spirit to the project's general anti-premature-complexity stance (`ARCHITECTURE.md` §13) than a full-corpus freeze is.

## Consequences

- `DEC-0004`'s full-corpus-before-any-implementation requirement is superseded (see that record's own Status/Superseded By fields). Its inventory-first requirement is retained and carried forward unchanged in substance.
- `ARCHITECTURE.md` §15/§15.1 updated: §15's Issue 3 description and the whole of §15.1 now describe the cluster workflow instead of the full-corpus gate.
- `docs/rules/INVENTORY.md` (already drafted under `DEC-0004`) remains the correct artifact for this decision too — its content does not need to change; only how it is used (cluster selection, not a monolithic gate) does. Its header and closing "Maintenance" section were updated to reflect that.
- `EXP-001` remains `APPROVED`, still not implemented — now waiting for its cluster to become dependency-complete, not for the entire corpus.
- The next substantive task is human review of the existing V1 Rules Inventory (`docs/rules/INVENTORY.md`), not producing a new one from scratch — it already exists as of this decision, on an as-yet-unmerged branch. See the accompanying report for the discrepancy between this decision's drafting instructions (written as though the inventory did not yet exist) and actual project state.

## Supersedes

`DEC-0004-full-v1-rules-corpus-before-implementation.md`.

## Superseded By

None.
