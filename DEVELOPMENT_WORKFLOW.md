# Retro D&D Simulator — Development Workflow

## 1. Purpose

Agent chat responses and commit messages are not durable documentation. This document establishes how completed implementation work, and significant standalone architecture/process decisions, are recorded in the repository so that a future developer or agent — human or AI — can determine what changed, why, under what authority, and with what evidence of correctness, without reconstructing that history from a chat transcript.

This document governs *process*, not code. It does not implement anything and does not choose a programming language, test framework, or storage technology.

## 2. Relationship to Other Governing Documents

- `GAME_CONSTITUTION.md` and `SOURCE_HIERARCHY.md` govern *what* is true about the game's rules.
- `ARCHITECTURE.md` governs *how the system is structured*.
- `AGENTS.md` governs *how an implementation agent is expected to behave*.
- `TESTING_STRATEGY.md` governs *how correctness is demonstrated and enforced*.
- `docs/rules/_template.md` governs the required shape of a Rule Card.
- This document governs *how development work is proposed, executed, verified, and recorded* — completion records for implementation work, and decision records for standalone architecture/process decisions.

## 3. Completion Records Are Mandatory, Permanent Repository Artifacts

Every completed implementation issue must produce a **completion record** before the issue is considered done. A chat response summarizing the work is not a substitute, even if the transcript is preserved elsewhere. Completion records are committed to the repository, versioned alongside the code they describe, and form part of the permanent project audit trail.

### 3.1 What requires a completion record

Required for:

- any change under `src/` (once it exists) that adds, modifies, or removes behavior;
- implementation of an approved Rule Card;
- a fix to a confirmed defect in rules-significant behavior (paired with a regression test — `TESTING_STRATEGY.md` §7);
- any other unit of work meeting the criteria above, even if not tied to a numbered implementation issue.

Not required for:

- pure documentation edits to the governing documents themselves — those changes are their own record, tracked by normal version control and, where applicable, the Rule Card approval trail or a decision record (§9);
- trivial non-behavioral changes (typo fixes, comment corrections, formatting).

When it is unclear whether a change is significant enough to warrant a completion record, err toward writing one. A short record costs little; a missing record for significant work is a durable audit gap.

## 4. Do Not Write a Diary

A completion record documents the **final state** of completed work and the **evidence** that it is correct. It is not a chronological log of every action taken, dead end explored, or intermediate attempt. Keep it concise — a reader should be able to determine everything required by §5 in a few minutes.

## 5. Completion Record Contents

Every completion record must contain the following, in order. Where a category legitimately has no entries, state that explicitly (e.g., "Deviations: None.") rather than omitting it — an omitted category is ambiguous; an explicit "none" is not.

1. **Issue/task identifier and objective** — which implementation issue this is, and what it set out to do.
2. **Approved inputs/specifications** — the relevant Rule Card(s), technical design documents, and architectural or decision-record inputs this work was authorized by (e.g., "Rule Card `ENC-001`, Status: APPROVED").
3. **Files created, modified, or deleted** — grouped accordingly.
4. **Behavior actually implemented** — a concise description of what the system now does, not a description of code structure or internal design.
5. **Rules provenance, where applicable** — the approved Rule Card governing the behavior and its provenance classification (`GAME_CONSTITUTION.md` §5).
6. **Tests added or modified** — what behavior each important test protects, not merely a file list.
7. **Exact verification commands executed** — the literal commands run (tests, lint, type-check, coverage, etc.).
8. **Verification results** — the pass/fail outcome of each command in §5 item 7.
9. **Coverage results** — relevant statement/branch coverage numbers. State "Not applicable — coverage tooling not yet configured" until coverage tooling exists.
10. **Deviations** — anything implemented differently from the approved specification, and why, including any one-off approved coverage exception (`TESTING_STRATEGY.md` §8): affected file/location, affected branch or behavior, technical reason normal automated coverage is impractical or inappropriate, what alternate verification exists (if relevant), and who/what human approval authorized it. State "None." when true.
11. **Known limitations/unresolved issues** — anything left open. State "None known." when true.
12. **Architectural consequences, where relevant** — only when the work introduced or materially changed an architectural boundary. This is the one category that may be omitted entirely rather than marked "none," since most issues will not touch architecture.

### 5.1 Completion gate

An implementation issue must **not** be represented as complete when:

- required tests are failing;
- required verification (§5 items 7–8) has not been run;
- a required automated gate has failed (`TESTING_STRATEGY.md` §9);
- the implementation differs from an approved Rule Card without human authorization;
- a rules ambiguity was encountered and silently resolved rather than escalated;
- known incomplete behavior exists and is not documented in §5 item 11.

If any of these apply, the work is **in progress**, not complete, regardless of how much of it is functional. A completion record documents the evidence that the automated gates passed; it does not itself substitute for them (`TESTING_STRATEGY.md` §9–§10).

## 6. Completion Record Location and Naming

```text
docs/completion-records/
    INDEX.md
    ISSUE-001-<slug>.md
    ISSUE-002-<slug>.md
    ...
```

- `<NNN>` is a zero-padded, sequential three-digit issue number, assigned in the order work begins (e.g., `001`, `002`). It is not reused, even if an issue is abandoned.
- `<slug>` is a short kebab-case description (e.g., `rng-dice-infrastructure`).
- Example: `docs/completion-records/ISSUE-001-rng-dice-infrastructure.md`.
- `docs/completion-records/INDEX.md` lists every completion record in issue order with a one-line description, so the full implementation history can be scanned without opening every file.

This directory does not exist yet and is not created by this document. It is created when the first completion record is written.

## 7. Completion Record Template

```markdown
# ISSUE-<NNN>: <Title>

## 1. Issue/Task Identifier and Objective
<what this issue set out to do>

## 2. Approved Inputs/Specifications
- Rule Card(s): <ID(s), Status: APPROVED>
- Technical design(s): <link/reference>
- Architectural/decision-record inputs relied upon: <reference>

## 3. Files Created, Modified, or Deleted
- Created: <...>
- Modified: <...>
- Deleted: <...>

## 4. Behavior Actually Implemented
<what the system now does, in plain terms>

## 5. Rules Provenance
<approved Rule Card + provenance classification, or "Not applicable — infrastructure only.">

## 6. Tests Added or Modified
- <test name/location> — protects <behavior>

## 7. Exact Verification Commands Executed
- `<exact command>`
- `<exact command>`

## 8. Verification Results
- `<command>` → <pass/fail>
- `<command>` → <pass/fail>

## 9. Coverage Results
<numbers, or "Not applicable — coverage tooling not yet configured.">

## 10. Deviations
<description, or "None.">

## 11. Known Limitations/Unresolved Issues
<description, or "None known.">

## 12. Architectural Consequences
<only if applicable — omit this section otherwise>
```

## 8. Ownership and Review

A completion record is written by the implementing agent as part of finishing the issue. It should be reviewed by a human alongside the code it describes, the same way the code itself is reviewed. A completion record is not itself a Rule Card and does not require the `APPROVED` gate that Rule Cards require (`SOURCE_HIERARCHY.md` §9) — but it is expected to accurately reflect what a human has actually reviewed and accepted.

## 9. Decision Records

### 9.1 Purpose

Some decisions are architectural or process-level rather than tied to a single implementation issue — for example, a change to the module layout, a revision of the testing baseline, or (as with `DEC-0001`) a summary of a foundational review. These are not naturally represented by a completion record (§3–§8), which documents *implementation* work. Decision records exist to give this class of decision the same durability and auditability.

### 9.2 When to create one

Create a decision record for a significant, standalone architectural or process decision — one that changes a governing document's substance, establishes a new project-wide policy, or reverses a prior such decision. Do not create one for routine implementation choices already captured by a completion record, and do not attempt to retroactively reconstruct every prior conversational decision as a separate historical record — `DEC-0001` exists precisely so that backlog does not need to be recreated piecemeal.

A one-off approved coverage exception (`TESTING_STRATEGY.md` §8) is a routine implementation choice for this purpose — it is documented in the completion record (§5 item 10), not a decision record. Create a decision record only when an exception establishes or changes a reusable, project-wide testing policy, not for an individual instance.

### 9.3 Format

Each decision record contains at minimum:

```text
Decision ID
Title
Status
Date

Context

Decision

Rationale

Consequences

Supersedes
Superseded By
```

Additional concise fields may be added when clearly useful. Keep the record focused — it is a decision record, not an implementation guide; detailed mechanics belong in the governing document(s) the decision updates.

### 9.4 Lifecycle

Approved decision records are historical. Do not rewrite an accepted record merely because the project later decides differently — supersede it instead:

```text
DEC-0004 — original decision
Status: Superseded
Superseded By: DEC-0012
```

```text
DEC-0012 — replacement decision
Supersedes: DEC-0004
```

This preserves architectural history. Minor clerical corrections (typos, broken links) may be handled sensibly in place; substantive changes must use supersession, not historical rewriting.

### 9.5 Location and Naming

```text
docs/decisions/
    INDEX.md
    DEC-0001-<slug>.md
    DEC-0002-<slug>.md
    ...
```

- IDs are sequential, zero-padded to four digits, and never reused — even for a rejected or abandoned decision.
- `docs/decisions/INDEX.md` is a concise index containing at least ID, title, status, and date for every record. It is not a duplicate copy of every decision's content.

### 9.6 Baseline record

`docs/decisions/DEC-0001-project-foundation-baseline.md` summarizes the foundational decisions adopted before this document's own approval, without attempting to reproduce every prior conversation. Going forward, significant standalone architectural/process decisions receive their own new records rather than edits to `DEC-0001`.

## 10. Relationship to Automated Verification

Completion records (§3–§8) and decision records (§9) are durable, human-readable reports. They are not the enforcement mechanism for testing or coverage requirements. Once the implementation toolchain is selected, automated CI/build gates are the objective enforcement mechanism for those requirements; a completion record documents what those gates showed, after the fact. See `TESTING_STRATEGY.md` §9–§10 for the full model, including the requirement that a failed mandatory gate must fail the build and must not be described as a completed issue.

## 11. Status

This document is a proposed and approved process standard (`docs/decisions/DEC-0001-project-foundation-baseline.md`). No completion records exist yet, and none will be created until implementation begins.
