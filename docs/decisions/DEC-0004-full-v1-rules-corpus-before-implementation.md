# DEC-0004: Full V1 Rules Corpus Required Before Historical-Rules Implementation

## Decision ID
DEC-0004

## Title
Full V1 Rules Corpus Required Before Historical-Rules Implementation

## Status
Superseded

## Date
2026-08-15

## Context

`ARCHITECTURE.md` §15 originally planned a three-issue sequence: RNG infrastructure (Issue 1), Rule Card infrastructure plus one approved Rule Card (Issue 2), and implementation of that single approved rule (Issue 3) — explicitly framed as a way to *validate the complete research→approval→implementation workflow* on one small procedure before expanding into larger systems. Issues 1 and 2 are complete: the RNG abstraction is implemented (`docs/completion-records/ISSUE-001-rng-dice-infrastructure.md`, with a defect-fix follow-up in `ISSUE-002-scripted-rng-die-range-validation-fix.md`), and the first Rule Card, `EXP-001` (Dungeon Wandering-Monster Check), is researched and `APPROVED`.

Before authorizing implementation of `EXP-001` (the originally planned Issue 3), the project owner revised the sequencing policy: historical-rules implementation should not begin piecemeal, rule by rule, but only once the complete set of Rule Cards needed for the initial vertical slice (`ARCHITECTURE.md` §14) has itself been researched and resolved.

## Decision

**Historical-rules implementation does not begin until the complete Rule Card corpus required for the v1 dungeon-crawler game has been researched, resolved, and human-approved.**

"Complete" does not mean every procedure ever published for OD&D. It means: every historical rule, table, special case, and dependency *reachable* during the intended v1 dungeon-crawl loop —

```text
Create / maintain party
        ↓
Prepare and equip expedition
        ↓
Enter generated/stocked dungeon
        ↓
Explore under dungeon-turn procedures
        ↓
Encounter creatures / traps / features
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

— has an approved specification before implementation of *any* of it begins. If a v1 procedure can generate, invoke, reference, or depend upon another mechanical behavior, that behavior is also in scope (e.g., a dungeon treasure table that can generate a magic sword brings magic-sword generation/effects into scope; a monster table entry with a special ability brings that ability into scope). Implementation agents must not leave reachable behavior for a later agent to resolve on the fly.

Explicitly **outside** v1 scope unless a v1 dungeon procedure genuinely depends on them: wilderness campaign procedures, the Outdoor Survival map procedure, naval combat, aerial combat, stronghold/domain construction and management, taxation/barony rules, large-scale domain warfare, and other endgame campaign systems unrelated to the dungeon expedition loop. If an apparently excluded rule turns out to be a required dependency of an in-scope procedure, that dependency is surfaced for human review rather than silently expanding scope.

**Completion standard.** Before historical implementation begins, a master rules inventory/dependency map (`docs/rules/INVENTORY.md`) identifies every v1-reachable item. Each item must end in one of two states:

```text
APPROVED
```

or

```text
OUT OF V1 SCOPE — HUMAN APPROVED
```

No v1-reachable item may remain `DRAFT`, `RESEARCHED`, `AWAITING_APPROVAL`, or unidentified/unresolved when implementation begins. Rule Cards may depend on other Rule Cards while research is underway — that is expected — but the inventory's purpose is to ensure those dependencies eventually close.

**Immediate consequence.** `EXP-001` is not implemented as part of this decision, despite being `APPROVED`. The next task is to produce the V1 Rules Inventory and Dependency Map (`docs/rules/INVENTORY.md`) — identifying proposed Rule Cards/groupings, domains, key sources, dependencies, v1-required status, current status, risk flags, and a suggested research order — without deep-researching every item. That inventory is submitted for human review before rules-research work continues.

## Rationale

Implementing one rule at a time risks discovering, mid-implementation, that an adjacent or dependent rule was never resolved — forcing either a pause to research it under implementation pressure (exactly the condition under which rules ambiguity is most likely to be silently resolved rather than escalated, `GAME_CONSTITUTION.md` §3) or a de facto invention of behavior to keep moving. Requiring the full v1-reachable corpus to be resolved first — even though it takes longer before any code exists — means every dependency an implementation agent encounters is already answered by an approved source, not improvised. This is a stricter application of the same principle that produced the Pre-Code Development Gate (§16 of `ARCHITECTURE.md`): foundational readiness before code, now extended from infrastructure/process readiness to rules-content readiness specifically.

This revises, rather than contradicts, `DEC-0001`'s general statement that "implementation occurs through small, dependency-ordered, bounded issues" (`docs/decisions/DEC-0001-project-foundation-baseline.md`) — that principle still holds; what changes is *when the first such issue may begin*, not the shape of the issues themselves once they do.

## Consequences

- `ARCHITECTURE.md` §15 is revised: Issues 1 and 2 are marked complete; the original Issue 3 ("implement the first approved rule") is replaced by a new Issue 3 ("V1 Rules Inventory and Dependency Map"); a new §15.1 ("V1 Rules-Corpus Completion Gate") states this decision's gate explicitly and supersedes the original single-rule-validates-the-workflow framing.
- `EXP-001`'s `APPROVED` status is unaffected — it remains approved, and remains one entry (now the first complete one) in the v1 inventory. It is simply not implemented yet.
- The next unit of work is the inventory itself, not further Rule Card research in depth, and not implementation.
- A significant amount of rules-research work now precedes any implementation. This is an accepted tradeoff, not an oversight — see Rationale.
- This decision does not itself resolve any individual rule's ambiguity; it only changes when implementation may begin relative to the corpus of resolved rules.

## Supersedes

None as a decision record. This revises the more specific sequencing detail previously written directly in `ARCHITECTURE.md` §15 (not itself a decision record) — that document has been updated accordingly. `DEC-0001`'s general development-governance principles remain accurate at their original level of generality (see Rationale).

## Superseded By

`DEC-0005-v1-rules-inventory-and-clustered-implementation.md`. That decision retains this one's inventory-first requirement but replaces the full-corpus-before-any-implementation requirement with a dependency-complete cluster workflow — see `DEC-0005`'s Context and Rationale for why. This record's Context, Decision, and Rationale above are preserved unchanged as a historical account of what was decided and why on 2026-08-15, prior to that refinement.
