# Retro D&D Simulator — Agent Instructions

## 1. Mission

You are contributing to a historically grounded simulator of the original 1974 Dungeons & Dragons game.

Your job is to implement and support the project's approved design. You are not authorized to modernize, rebalance, reinterpret, or complete game rules without documented approval.

Before performing rules-related work, read:

- `GAME_CONSTITUTION.md`
- `SOURCE_HIERARCHY.md`
- the relevant approved Rule Card(s)
- `ARCHITECTURE.md` when implementation is involved
- `DEVELOPMENT_WORKFLOW.md` and `TESTING_STRATEGY.md` before starting or completing any implementation issue

**Pre-Code Development Gate.** No production code may be written — not even infrastructure such as the RNG abstraction — until a human has approved the foundational documents listed in `ARCHITECTURE.md` §16: this architecture, the source hierarchy, the Rule Card format/approval process, `DEVELOPMENT_WORKFLOW.md`, `TESTING_STRATEGY.md`, the decision-record process, the RNG technical contract, and the CI/build enforcement model. Research, drafting, and Rule Card approval workflow may proceed before that gate clears; implementation may not.

## 2. Rules Are Specifications

Treat approved Rule Cards as executable specifications.

A Rule Card is not authoritative until a human project owner sets its `Status` field to `APPROVED` (`SOURCE_HIERARCHY.md` §9). Draft or in-review Rule Cards may be researched and discussed, but must not be implemented. Implementation agents may implement only the mechanical specification of an `APPROVED` Rule Card. If implementation requires behavior that is absent from, or ambiguous in, an approved Rule Card, stop at that boundary rather than extending or reinterpreting the approved specification — this is a form of the silent rules decision prohibited in §3.

Do not implement behavior merely because:

- it is familiar from later D&D editions;
- it seems reasonable;
- it is common in modern role-playing games;
- it improves balance;
- it simplifies implementation;
- it appears in AD&D.

If required behavior is not specified, stop at the ambiguity and report it.

## 3. No Silent Rules Decisions

Never silently decide:

- how an ambiguous spell works;
- what an unspecified saving throw should be;
- how surprise should interact with another procedure;
- whether a monster attacks;
- how treasure should scale;
- what a trap should do;
- whether a modern convenience should replace a historical procedure;
- any comparable unresolved game-rule question.

Instead provide:

1. the implementation boundary reached;
2. the missing behavior;
3. why the existing specification is insufficient;
4. any historical source candidates if research was requested.

## 4. AD&D Is Excluded by Default

Do not use AD&D as rules authority unless a specific approved project decision explicitly authorizes it.

Prefer the source hierarchy in `SOURCE_HIERARCHY.md`.

If no compatible D&D-lineage answer exists, escalate for a Simulator Ruling.

## 5. Preserve Historical Procedures

Do not replace historical procedures with modern abstractions.

Examples:

- wandering-monster generation is not "spawn a balanced encounter";
- a random encounter is not automatically combat;
- treasure generation is not "award level-appropriate loot";
- reaction and morale are independent systems where the approved rules require them;
- survivability settings do not authorize reward scaling.

## 6. Canonical Simulation Before Presentation

Core rules logic must not depend on UI, narrative prose, animation, or an LLM.

The simulation determines authoritative game state.

Presentation systems describe or expose that state.

Never allow flavor text or AI narration to create, remove, or alter authoritative outcomes unless an approved rule explicitly permits that behavior.

## 7. Randomness

Use the project's injectable/seedable random-number abstraction for simulation randomness.

Do not introduce uncontrolled global randomness into rules code.

The current architecture uses a single simulation-owned RNG stream, seeded per campaign/session (`ARCHITECTURE.md` §5). Do not introduce per-procedure or per-entity RNG streams without an approved architecture change.

Tests for random procedures should use deterministic seeds or controlled test doubles wherever practical.

## 8. Survivability Modifiers

Survivability features must be implemented as explicit policies applied after canonical historical generation whenever practical.

Do not alter treasure generation or XP awards as a side effect of survivability settings — including indirectly, such as by rerolling or suppressing canonical encounters because they would have produced treasure. Treasure-generation and XP-award procedures must not accept a survivability policy at all (`ARCHITECTURE.md` §10).

Preserve the canonical result so tests and diagnostics can identify how the survivability policy changed the presented result.

## 9. Implementation Workflow

The full path from source to shipped behavior is:

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

For each implementation issue:

1. Read the governing documents and the relevant Rule Card; confirm its `Status` is `APPROVED`. If it is not, stop and request approval before proceeding.
2. Inspect the existing code before proposing changes.
3. Identify the minimum required implementation surface.
4. State any rule ambiguity before editing — including ambiguity the approved Rule Card itself does not resolve.
5. Implement only the behavior specified in the approved Rule Card.
6. Add or update tests for every mechanical case specified (`TESTING_STRATEGY.md` §2).
7. Run the relevant tests and other required verification (unit, integration, regression, lint, type-check, coverage — as configured; `TESTING_STRATEGY.md` §9).
8. Report what changed and any unresolved issues.
9. Produce a completion record for the issue (`DEVELOPMENT_WORKFLOW.md` §5) before representing it as complete.

Do not make unrelated refactors unless required for the task.

An issue must not be represented as complete when required tests are failing, required verification has not been run, the implementation differs from an approved Rule Card without human authorization, a rules ambiguity was silently resolved, or known incomplete behavior is undocumented (`DEVELOPMENT_WORKFLOW.md` §5.1).

## 10. Rules Research Workflow

When asked to research a rule:

1. Separate explicit 1974 behavior from omissions.
2. Search sources in the approved hierarchy.
3. Address the exact unresolved question rather than importing an entire later rule.
4. Distinguish clarification from revision.
5. Report compatibility concerns.
6. Do not convert research conclusions into approved rules unless authorized.

## 11. Testing Expectations

`TESTING_STRATEGY.md` is the authoritative testing standard; the points below summarize it.

Tests should emphasize behavior rather than implementation details.

Rules tests should demonstrate:

- correct inputs and outputs;
- boundary cases;
- historical table behavior where applicable;
- deterministic random outcomes;
- interaction between canonical generation and survivability policies;
- preservation of treasure and XP behavior under survivability settings.

Regression tests are required whenever a rules bug is fixed.

## 12. Protected Design Authority

The following are protected authority and process documents:

- `GAME_CONSTITUTION.md`
- `SOURCE_HIERARCHY.md`
- `AGENTS.md` (this document)
- `DEVELOPMENT_WORKFLOW.md`
- `TESTING_STRATEGY.md`
- the Rule Card template (`docs/rules/_template.md`)
- approved Rule Cards
- project-wide difficulty policy
- rules provenance decisions

An agent may identify a problem in a protected document, recommend a modification, and draft a proposed change when asked to do so. An agent may not autonomously modify a protected document — including this one — merely because doing so would make another task easier. Actual modification requires explicit human direction.

This protects the project's governing rules, including the rules governing agent behavior itself, from being silently weakened by the agent operating under them.

`ARCHITECTURE.md` is treated differently: it is expected to evolve as implementation experience accumulates and may be revised when a human explicitly assigns an architecture task authorizing changes. It is not on the protected list, but that does not license casual, task-of-convenience edits — a dedicated architecture-review task is the normal path for changing it.

## 13. Preferred Agent Behavior

When uncertain, be conservative.

A correct response may be:

> Implementation cannot proceed because the current approved rule specification does not define this behavior.

That is preferable to inventing a plausible rule.
