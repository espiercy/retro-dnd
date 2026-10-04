# Retro D&D Simulator — Agent Instructions

> **Migration note (2026-08-16).** This document was revised under `DEC-0007-rules-cyclopedia-primary-rules-authority.md`, which replaced the 1974 three-book OD&D core with the *Dungeons & Dragons Rules Cyclopedia* as the simulator's primary rules authority. See `docs/rules/RULESET_BASELINE_MIGRATION.md` for the full migration record and `SOURCE_HIERARCHY.md` for the current hierarchy.

## 1. Mission

You are contributing to a retro Dungeons & Dragons dungeon-crawler simulator grounded primarily in the *Dungeons & Dragons Rules Cyclopedia*, using historically compatible alternate D&D sources where necessary to complete or clarify the executable rules.

Your job is to implement and support the project's approved design. You are not authorized to modernize, rebalance, reinterpret, or complete game rules without documented approval. This includes not silently preferring an earlier-edition rule (including the project's own prior 1974-primary research) over an explicit Rules Cyclopedia mechanic merely because it is more historically primary, more familiar, or was the project's superseded 1974-primary governance baseline — that is itself a form of the silent rules decision prohibited in §3.

A Rule Card, cluster, or inventory previously `APPROVED` under a since-superseded source authority does not retain implementation authority merely because it still says `APPROVED`. See `REVALIDATION_REQUIRED` (`DEVELOPMENT_WORKFLOW.md` §9.7, `docs/rules/_template.md`) for the status such artifacts carry until reviewed against the current hierarchy.

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

Prefer the source hierarchy in `SOURCE_HIERARCHY.md`, which begins with the Rules Cyclopedia (§3) and treats BECMI, B/X, Holmes, and original OD&D as alternate-source completion material, not as authority earlier sources are checked against ahead of the Rules Cyclopedia.

If no compatible D&D-lineage answer exists, escalate for a Simulator Ruling. If a compatible-but-conflicting alternate-source rule is nonetheless desired, escalate it as a candidate Human-Approved Variant (`SOURCE_HIERARCHY.md` §7) rather than importing it as ordinary completion.

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
Evidence-First Research (Stage A → Stage B — docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md)
      ↓
Rule Card Draft / Revalidation
      ↓
Human Rule Card Approval
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

Rule research follows the **Evidence-First** two-stage protocol in `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` (adopted by `docs/decisions/DEC-0009-evidence-first-rule-research-protocol.md`), not a single research→draft pass. This section states what binds every rules-research agent; the linked protocol is the full, authoritative procedure — do not treat this summary as a substitute for reading it before starting substantial rules research.

1. **Stage A (Evidence) and Stage B (Synthesis/Draft) are separate tasks.** Do not rewrite an active Rule Card's specification during Stage A. Evidence must close before mechanical synthesis begins.
2. **Primary Rules Cyclopedia text is a hard gate.** Secondary sources may only locate material or suggest terminology/pages worth checking — they cannot themselves establish RC mechanics. If usable primary text cannot be accessed, stop: `PRIMARY SOURCE ACCESS REQUIRED`.
3. **Search the whole primary source, not just the chapter that answers part of the question**, before treating evidence as complete.
4. **Actively attempt to falsify every consequential tentative conclusion** before proposing it; a rejected interpretation stops the task rather than being silently replaced with another guess.
5. **For `REVALIDATION_REQUIRED` cards, research the current Rules Cyclopedia procedure from scratch before consulting the superseded Rule Card in detail** — legacy cards are provenance and a completeness check, not a template that survives unless disproven.
6. **Human evidence review is a hard gate.** Stage A ends with either `EVIDENCE READY FOR HUMAN REVIEW` or `MORE PRIMARY RESEARCH REQUIRED`; Stage B may not begin without explicit human authorization.
7. **Alternate-source research is gap-directed only** — performed after a precise RC gap is documented, never a broad browse of earlier editions. **Simulator Rulings are proposed only after that research fails**, are never bundled, and are never self-approved.
8. Classify each alternate-source comparison using the compatibility vocabulary (`SOURCE_HIERARCHY.md` §6) — Preserved, Compatible Completion, Evolved/Different, or Conflicting — and, when revalidating, classify each inherited legacy mechanic using the protocol's disposition vocabulary (PRESERVED / CHANGED / REMOVED / MOVED TO ANOTHER RESPONSIBILITY / RC DOES NOT SPECIFY / POTENTIAL COMPLETION QUESTION).
9. Report compatibility concerns, and flag any Evolved/Different or Conflicting finding as a candidate Human-Approved Variant rather than importing it.
10. Do not convert research conclusions into approved rules, and do not create a Human-Approved Variant, unless authorized.

**Evidence-integrity gates (`DEC-0013`, supersedes `DEC-0012`).** `DEC-0012`'s gates were adopted because `CLUSTER-004` Stage A required five independent completeness reviews and the defects were **premature evidentiary closure**, not rules interpretation. That diagnosis still holds. Its remedy did not: its pilot (`ENC-001`) failed two of its four fixed criteria, because instruments the researcher writes about the researcher's own work cannot see what was never enumerated — **internal consistency is not external completeness**. `DEC-0012` remains historical and is not rewritten; what binds now is:

11. **You declare judgment; the tool derives the obligations.** Start every Stage-A packet from `docs/rules/evidence/_TEMPLATE.md`. You declare subject terms, semantic seams and discovered leads. You do **not** declare the page set: `scripts/lint_evidence.py` derives it from `INVENTORY.md` and from accepted neighbour packets, and **deleting a page from your packet does not delete its obligation**. Every derived page needs one disposition — `INSPECTED`, `ROUTED_EXTERNAL`, `IRRELEVANT_AFTER_INSPECTION`, `OUTSIDE_CARD_SCOPE` or `ACCESS_BLOCKED` — and a routed page names where it went.
12. **A seed is an obligation to look, never inherited truth.** Only a page number and the source packet's name travel. An accepted packet may be wrong — `ENC-005`'s called the Encounter Distances Table "light-keyed", and `ENC-001` correctly refuted it against primary text while still owing the inspection.
13. **Absence needs a record only where it is consequential** (§10.4) — a claim a future Rule Card would rely on. A failed keyword or OCR search is never evidence of absence; classify it `NOT YET ESTABLISHED`. Index-entry absences, artifact existence and counts no longer need records.
14. **Index instruments are completeness instruments, not citation aids** (§9.9) — enumerate and disposition the General Index, Tables/Checklists Index and any specialist index, and record absent entries too. **Index seeding is not yet mechanical**: no structured RC index transcription exists outside Stage-A packets, so this remains research the semantic reviewer judges. **HTTP success is not visual access** (§9.2.1) — a served image whose columns are blank is an unresolved blocker, and a second digitisation of the same edition is still primary access.
15. **Never write a count.** Counts are derived by the linter and printed; a hand-maintained tally in a packet is itself a defect. Run `uv run python scripts/lint_evidence.py` before requesting independent review. **A green linter is a floor, never a certification** — independent review is semantic, it remains mandatory, and you may never certify your own packet (§10.1.2).
15a. **Independent review is semantic.** It owns rules interpretation, source-area exclusion, semantic cross-references, ownership assignment, silent ambiguity adjudication, governing-object classification, and whether your subject terms, seams and exclusions were adequate. It is **not** the detector for page numbers, counts, gaps or tallies. A mechanical defect that changes neither the inspected source set nor a rules conclusion is fixed and machine-verified — it does not reopen review. A defect revealing a previously uninspected potentially governing source does. The budget is **two** substantive completeness reviews; if it is exhausted without `PASS`, **stop and evaluate the process** rather than authorizing another.
16. **One active task, one Git worktree** (`DEC-0012` item 16). Before writing anything, establish `WORKTREE`, `BRANCH`, `HEAD`, `MAIN`, `ORIGIN/MAIN` and `STATUS`. An unexpected branch or `HEAD` change is a **hard stop** — report the collision before writing or committing. Never switch the branch of a worktree another active task may be using.
17. **Stage-A research is authorization-gated.** `DEC-0012`'s pilot (`ENC-001`) is complete and its result is recorded in `DEC-0013`. Do not begin Stage-A research on any card without explicit human authorization naming it.

`docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` additionally defines the confidence vocabulary and the complete set of hard-stop conditions (including `PRIMARY PROCEDURE NOT YET ESTABLISHED`, `INTERNAL SOURCE CONFLICT REQUIRES REVIEW`, `COMPLETION COMPATIBILITY NOT ESTABLISHED` and `UNVERIFIED PROJECT FACT`) — not restated here. Its §1 carries a supersession notice marking which of its packet-shape instructions `DEC-0013` replaced; the packet form itself is `docs/rules/evidence/_TEMPLATE.md`.

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
