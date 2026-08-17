# Rule Card Research Protocol — Evidence-First

## 1. Status and Authority

This is the canonical, detailed research protocol for Rules Cyclopedia (and, when gap-directed, alternate-source) rule research, adopted by `docs/decisions/DEC-0009-evidence-first-rule-research-protocol.md`. `AGENTS.md` §10 and `DEVELOPMENT_WORKFLOW.md` §9.7 bind agents to this document rather than duplicating it; where this document and either of those differ, resolve the conflict by asking a human rather than assuming either wins by default.

This document governs *how* rules research is performed. It does not itself grant Rule Card approval authority (`SOURCE_HIERARCHY.md` §9), does not change which source is primary (`DEC-0007`), and does not change which RC-optional systems this project has selected (`DEC-0008`). It operationalizes the source hierarchy; it does not revise it.

## 2. Why This Exists

`EXP-002`'s revalidation exposed a repeated failure mode: mechanical synthesis began before the complete governing Rules Cyclopedia procedure had actually been located and read. Two compounding problems produced plausible-looking, wrong specifications that required repeated correction cycles:

1. **Incomplete source acquisition treated as sufficient.** A secondary-source snippet, or a single passage located in one chapter, was treated as though it were the whole rule, when the Rules Cyclopedia's actual governing procedure lived partly in a different chapter and included a controlling minimum/exception the initial pass never located.
2. **Legacy-card anchoring.** Detailed comparison against the superseded 1974-primary Rule Card began early enough to shape the research questions asked of the Rules Cyclopedia, rather than the Rules Cyclopedia being understood independently first and *then* compared against the legacy card for provenance.

This protocol exists to make **stopping on inadequate evidence an expected, successful research outcome** — not a failure to be avoided by producing a polished artifact anyway.

## 3. The Two-Stage Lifecycle

This replaces the prior single-pass pipeline (`Source → Research → Rule Card Draft → Human Review`) with:

```text
PRIMARY-SOURCE ACQUISITION
        ↓
EVIDENCE COLLECTION
        ↓
WHOLE-SOURCE CROSS-REFERENCE SEARCH
        ↓
FALSIFICATION / CHALLENGE PASS
        ↓
HUMAN EVIDENCE REVIEW                      ◄── hard gate (§11)
        ↓
MECHANICAL SYNTHESIS
        ↓
LEGACY-CARD COMPARISON, WHEN REVALIDATING
        ↓
GAP-DIRECTED ALTERNATE-SOURCE RESEARCH, IF REQUIRED
        ↓
SIMULATOR RULING, IF STILL REQUIRED
        ↓
RULE CARD DRAFT / REVALIDATION
        ↓
HUMAN RULE CARD APPROVAL
```

**Core principle: evidence must close before mechanical synthesis begins.** Everything above the "Human Evidence Review" gate is **Stage A — Evidence**. Everything from "Mechanical Synthesis" downward is **Stage B — Synthesis / Rule Card Draft**. A research agent must not produce a polished executable specification from incomplete primary evidence, and must not cross from Stage A into Stage B without explicit human authorization (§11).

In practice, Stage A and Stage B are normally two separate agent tasks. A trivial Rule Card may collapse the two stages into one task only when a human explicitly authorizes doing so for that specific card — an agent may not decide unilaterally that a card is "trivial enough" to skip the gate.

## 4. Primary Source Is a Hard Gate

For Rules Cyclopedia research, the relevant Rules Cyclopedia primary text must actually be accessed and inspected before mechanical synthesis begins. Secondary sources (forum threads, wikis, blog posts, AI-search summaries) may be used only to:

- locate likely RC material (which chapter, which section);
- identify terminology worth searching for in the primary text;
- suggest pages worth checking.

**They may not substitute for primary RC evidence when establishing the RC mechanic itself.** A search-engine snippet, an AI-generated summary of a search result, or a secondary source's paraphrase is not primary evidence, no matter how confident or specific it sounds — it is, at best, a locator (see the confidence vocabulary in §6).

If usable primary text cannot be accessed after a genuine attempt:

```text
STOP — PRIMARY SOURCE ACCESS REQUIRED
```

Report:

- every source attempted;
- the exact access failure for each (connection refused, size limit, 403, truncation, etc.);
- the exact research question(s) that remain unanswered as a result.

**This is a hard gate, not a standing bypass.** Do not proceed to mechanical synthesis, Rule Card rewriting, alternate-source substitution, or a Simulator Ruling merely because primary access failed — and do not treat "accept a lower-confidence secondary-source-only pass" as an ordinary, available continuation of this protocol. If usable primary Rules Cyclopedia text cannot be accessed, the Stage A task stops there. Human direction, given after that stop, may:

- provide another primary-source access method to try;
- defer the research until access is available;
- explicitly authorize a separate exceptional governance decision covering that specific case.

**Secondary-source-only evidence does not satisfy this gate and cannot, under this protocol, establish or authorize an RC mechanic on its own — regardless of how a human subsequently chooses to proceed.** A future human directive that changes how a specific case is handled is a governance decision made outside and after this protocol's normal operation, not a discretionary option this protocol itself offers a research agent as a routine escape route. Secondary sources remain locators only (see above), never a substitute for the gate itself.

## 5. Stage A Is Separate From Rule Card Drafting

Every substantial new Rule Card or revalidation begins with a distinct Stage A task. During Stage A:

- **Do not rewrite the active Rule Card specification.** A Rule Card being revalidated keeps its current content and `REVALIDATION_REQUIRED` status untouched throughout Stage A.
- Produce a standalone **evidence report**, committed as a durable evidence artifact (see §11 for the required contents and §12 for the artifact's location and lifecycle), containing, at minimum, an evidence map in this shape:

| Research Question | Primary Source Location | What RC Establishes | Provenance | Confidence |
|---|---|---|---|---|

Provenance classifications used in the evidence map (a subset of `GAME_CONSTITUTION.md` §5 / `SOURCE_HIERARCHY.md` §10's full vocabulary, appropriate to the evidence stage):

- **Rules Cyclopedia Explicit**
- **Necessary Mechanical Consequence**
- **Unresolved by RC**

(Alternate-Source Compatible Completion and Simulator Ruling are not evidence-stage classifications — they are Stage B outcomes, reached only after the process in §15/§16 below, and only for gaps the evidence stage has already precisely documented as unresolved.)

## 6. Confidence Vocabulary

Every evidence-map row's Confidence column uses exactly one of:

- **DIRECT PRIMARY TEXT** — quoted or closely paraphrased directly from inspected RC primary text.
- **PRIMARY TEXT + CROSS-REFERENCE CONFIRMED** — direct primary text, independently corroborated by a second passage or internal cross-reference within the same primary source (e.g., a stated page reference that was itself checked).
- **NECESSARY CONSEQUENCE** — not itself stated by RC, but a logically forced arithmetic/mechanical consequence of two or more DIRECT PRIMARY TEXT facts, with the derivation shown.
- **SECONDARY SOURCE LOCATOR ONLY** — found only via a secondary source; primary text has not (yet) been directly inspected for this specific fact. **May guide further research. Cannot authorize mechanics** — a row at this confidence level blocks Stage A from closing on that question.
- **NOT YET VERIFIED** — a plausible reading not yet checked against primary text at all; a placeholder, not a finding.

A Stage A evidence report is not ready for human review while any consequential row still carries `SECONDARY SOURCE LOCATOR ONLY` or `NOT YET VERIFIED` — either the primary text must be located and inspected, or the row must be reported as an unresolved research question (§4, §11) rather than smoothed over.

## 7. Facts and Consequences Must Be Separate

Never silently convert an arithmetic or logical consequence into a procedural rule. Example, drawn directly from `EXP-002`'s own research:

```text
RC Explicit:
    1 round = 10 seconds
    1 turn  = 10 minutes

can establish —

Necessary Mechanical Consequence:
    60 rounds contain the same amount of clock time as 1 turn.

It does NOT by itself establish —

    Every combat mechanically consumes raw-rounds / 60 exploration turns.
```

A governing procedure elsewhere (in `EXP-002`'s actual case, the Encounter Checklist's explicit "at least one full turn" minimum) may qualify, override, or replace what the raw arithmetic alone would suggest. Record explicit facts and inferred consequences as distinct evidence-map rows with distinct provenance, never merged into one claim.

## 8. Research the Governing Procedure, Not Just the Value

Locating a value, a table, or an individual sentence is not sufficient evidence on its own. For every rules responsibility under research, identify: **how does the Rules Cyclopedia actually instruct the DM to execute the situation?** This means actively researching, not merely noting if stumbled upon:

- checklists and procedure sequences;
- entry conditions and exit conditions;
- cross-references to other chapters/sections;
- exceptions;
- referee/DM guidance framing the rule's intent;
- worked examples that clarify the procedure in use.

A numeric fact must be interpreted inside its governing procedure, not treated as free-floating. (`EXP-002`'s "1 round = 10 seconds" was true and correctly located on the first pass; the failure was not researching the Encounter Checklist procedure that actually governs what that number means for dungeon-turn accounting.)

## 9. Mandatory Whole-Source Cross-Reference Pass

Once initial evidence is collected, deliberately search the **entire** available primary text for related terminology before treating the evidence map as complete. Do not assume the full mechanic is located in one chapter merely because the first relevant passage was found there.

Derive search terms from the rule under research and search for:

- the primary terminology itself;
- synonyms and alternate phrasings;
- related procedures;
- exceptions;
- timing qualifications (when something begins, ends, resets);
- minimums and maximums;
- rounding conventions;
- internal cross-references (e.g., "see page X");
- relevant worked examples;
- later DM/referee-facing sections that might qualify an earlier player-facing statement.

Record, in the evidence report:

- the exact search terms used;
- every cross-reference found, including ones that turned out not to matter (a negative result is still evidence that the search was actually performed);
- every chapter/section inspected as part of this pass.

## 10. Mandatory Falsification Pass

Before proposing any mechanical conclusion of consequence, actively attempt to prove it wrong or incomplete. For every consequential tentative interpretation, record:

```text
Tentative conclusion:
    <interpretation>

Challenge:
    What RC rule could contradict, qualify, round, override,
    or provide an exception to this?

Searches performed:
    <terms / sections>

Result:
    <evidence found, or "none located">

Disposition:
    CONFIRMED / QUALIFIED / REJECTED
```

A major conclusion cannot proceed to Stage B synthesis until it has undergone this challenge pass and reached `CONFIRMED` or `QUALIFIED` (with the qualification itself recorded as its own evidence-map row).

If falsification rejects the interpretation:

```text
STOP — INITIAL INTERPRETATION REJECTED;
MORE PRIMARY RESEARCH REQUIRED
```

Do not immediately replace the rejected interpretation with another speculative model merely to finish the artifact — that reproduces the exact failure mode this protocol exists to prevent. Report the rejection and what would be needed to resolve it, and stop.

## 11. Required Stage-A Evidence Report Contents

Every Stage A task must stop and produce a report containing, at minimum:

1. Rule Card ID/title.
2. Primary source(s) successfully accessed (exact URLs/editions/access method).
3. Exact RC chapters/sections actually reviewed.
4. The research questions the task set out to answer.
5. The evidence map (§5's table shape).
6. Whole-source cross-reference search terms used (§9).
7. Cross-references discovered (§9).
8. Tentative conclusions and their falsification passes (§10), with disposition.
9. Conclusions confirmed.
10. Conclusions qualified, and by what.
11. Conclusions rejected, and what further research they need.
12. Unresolved RC questions.
13. Questions determined to belong to a different Rule Card's own scope, not this one.
14. Whether alternate-source research is actually required for any unresolved question (§15) — and if so, the precise gap statement, not a general "let's also check B/X" plan.
15. Possible Simulator Ruling areas, named but not drafted (§16).
16. Explicit confirmation that, for a `REVALIDATION_REQUIRED` card, the legacy Rule Card was withheld from detailed comparison until RC-first research was independently complete (§13).
17. Access limitations encountered (size limits, blocked hosts, truncation, etc.), even where a workaround succeeded.
18. An overall confidence assessment.
19. A recommendation, exactly one of:
    ```text
    EVIDENCE READY FOR HUMAN REVIEW
    ```
    or:
    ```text
    MORE PRIMARY RESEARCH REQUIRED
    ```

**This report is committed to the repository as the durable evidence artifact defined in §12 — it does not stop at a chat response.** Then stop. Do not continue into Stage B on the same task.

## 12. Evidence Artifacts — Location and Lifecycle

**Location.** Stage-A evidence artifacts live under:

```text
docs/rules/evidence/
```

**Naming convention:**

```text
docs/rules/evidence/<RULE-ID>-evidence.md
```

Examples:

```text
docs/rules/evidence/EXP-001-evidence.md
docs/rules/evidence/COMBAT-004-evidence.md
```

**Definition and treatment:**

- The evidence artifact is the **durable repository record of Stage A** — the committed form of the report required by §11, not merely something described in an agent's chat response.
- It is **committed on the Stage-A research branch**, alongside (or ahead of) any other Stage-A work, exactly as any other documentation change in this project is committed and pushed for review.
- It contains, at minimum, the evidence map, whole-source cross-reference results, falsification passes, unresolved questions, confidence assessment, and recommendation already required by §11 — this section does not add new required contents, only where they live and how they persist.
- **It is not itself a Rule Card.** It does not use `docs/rules/_template.md`'s shape, does not carry a Rule Card `Status` field, and is never assigned `APPROVED` Rule Card status under `SOURCE_HIERARCHY.md` §9.
- **It is not mechanically authoritative.** Nothing in an evidence artifact authorizes implementation, and nothing in it may be treated as an approved mechanical specification — that remains the Rule Card's role, reached only via Stage B and human Rule Card approval.
- It is **preserved after human evidence review**, whether the recommendation was accepted, sent back for more research, or partially revised — so that later Stage-B work, and any future audit, can see exactly what evidence supported (or failed to support) synthesis, without reconstructing it from a chat transcript.
- **Stage B must reference the accepted evidence artifact for audit/provenance continuity, but that reference does not substitute for the Rule Card's own required citations.** The resulting Rule Card must still carry the underlying Rules Cyclopedia citations, and any applicable alternate-source citations, required by `docs/rules/_template.md` — the evidence artifact is not a substitute for those primary/source-hierarchy citations, and does not become mechanical authority merely because the Rule Card references it. Stage B need not redo the accepted Stage-A research; it transfers the verified source locations and conclusions into the Rule Card while linking the evidence artifact (`docs/rules/evidence/<RULE-ID>-evidence.md`) as the durable research record.

The `docs/rules/evidence/` directory itself does not need to exist in advance — it is created (with its first file) when the first Stage-A task under this protocol produces an evidence artifact.

## 13. RC First, Legacy Rule Card Later

For `REVALIDATION_REQUIRED` Rule Cards, do not begin detailed research from the superseded Rule Card's own content, framing, or terminology. Stage A order is fixed:

```text
Current Rule Responsibility (what question this card must answer)
        ↓
Rules Cyclopedia primary research, from scratch
        ↓
whole-source cross-reference pass
        ↓
falsification pass
        ↓
human evidence review
```

Only *after* the RC procedure is independently understood and has cleared human evidence review should detailed legacy-card comparison occur, as part of Stage B. At that point, classify each inherited mechanic using:

- **PRESERVED**
- **CHANGED**
- **REMOVED**
- **MOVED TO ANOTHER RESPONSIBILITY**
- **RC DOES NOT SPECIFY**
- **POTENTIAL COMPLETION QUESTION**

Legacy Rule Cards are provenance, a regression/completeness check, and historical evidence. **They are not templates that survive unless disproven.** This rule exists specifically to prevent anchoring on the superseded 1974-primary specifications — a legacy mechanic earns its place in the revalidated card only by independently surviving the current source-hierarchy process, either because the Rules Cyclopedia supports it, or because a genuine RC gap is later resolved by that mechanic as an approved Alternate-Source Compatible Completion (§15). Its prior presence in the superseded Rule Card gives it no presumption of survival. This does not weaken the RC-first / legacy-card-later rule above: alternate-source consideration for a legacy mechanic still occurs only in Stage B, and only after the RC gap it might fill has been precisely established, exactly as §15 requires — never as a shortcut for reinstating a legacy mechanic RC itself does not support.

## 14. Do Not Preserve Simulator Machinery by Inertia

Existing implementation-shaped concepts carried in a prior draft or a legacy card — ledgers, accumulators, event/boundary models, state variables, rounding schemes, interruption systems, activity-cost abstractions — must each be re-justified against the actual RC procedure during Stage B, not carried forward because they already exist in prose. For each such concept, ask: **does the historical game mechanic require this concept, or is this merely one possible software representation of it?**

Rule Cards specify mechanical behavior. Implementation architecture comes later (`ARCHITECTURE.md`, a separate concern). Prefer statements like:

> Procedures whose cadence depends on completed turns must be able to distinguish those turns.

over statements like:

> Publish `TurnBoundaryEvent` to subscribers.

## 15. Alternate Sources Are Gap-Directed Only

Do not broadly browse earlier editions merely to see what they did, and do not begin alternate-source research until a precise RC gap has been documented in this shape:

```text
RC establishes:
    A
    B
    C

RC does not establish:
    D

Executable simulation requires D because:
    <reason>
```

Only then, follow `SOURCE_HIERARCHY.md` §3 for the highest-priority, most directly relevant compatible treatment of `D` specifically — not an entire alternate-source rule adjacent to it. Do not import unrelated mechanics encountered incidentally during that research merely because they were nearby.

Before accepting a completion, document:

- the exact RC gap being filled;
- the alternate source and its exact treatment;
- why it does not contradict RC (`SOURCE_HIERARCHY.md` §6's compatibility vocabulary);
- any downstream RC assumptions the completion must remain consistent with;
- any dependency the completion introduces.

Only then may it be classified **Alternate-Source Compatible Completion**.

## 16. Simulator Rulings Are Last

A Simulator Ruling may be proposed only after RC primary research, the whole-source cross-reference pass, the falsification pass, and gap-directed compatible-source research (§15) together fail to establish the executable behavior required. Every proposed Simulator Ruling must independently state:

1. The exact missing behavior.
2. Why executable simulation requires an answer at all.
3. Why RC does not answer it (with reference to the evidence map and cross-reference pass, not a bare assertion).
4. Why compatible historical sources do not answer it either.
5. The smallest proposed ruling that closes the gap — not a broader design convenient for implementation.

Do not bundle unrelated rulings into one proposal (each ruling stands or falls on its own). Do not self-approve a Simulator Ruling — it is proposed, in `AWAITING_APPROVAL`, pending explicit human sign-off, exactly as `EXP-002`'s long-encounter ruling was.

## 17. Hard Stop Conditions

An agent performing rules research under this protocol must stop under each of the following conditions, with the corresponding exact message:

| Condition | Stop message |
|---|---|
| Primary source cannot be accessed | `STOP — PRIMARY SOURCE ACCESS REQUIRED` |
| The governing procedure has not actually been located, even if a related value has | `STOP — PRIMARY PROCEDURE NOT YET ESTABLISHED` |
| Two or more RC passages conflict and have not been reconciled | `STOP — INTERNAL SOURCE CONFLICT REQUIRES REVIEW` |
| The falsification pass (§10) rejects a tentative interpretation | `STOP — MORE PRIMARY RESEARCH REQUIRED` |
| An alternate-source completion candidate's compatibility with RC cannot be established with confidence | `STOP — COMPLETION COMPATIBILITY NOT ESTABLISHED` |
| Substantial simulator-level behavior remains undefined after §14–§16 | `STOP — HUMAN RULING REQUIRED` |

**Stopping is a successful research outcome when the evidence does not support synthesis.** Completing a polished artifact is never more important than preserving provenance integrity. An agent that stops correctly under this section has done its job; an agent that pushes through to a plausible-looking Rule Card without clearing the relevant gate has not, regardless of how well-written the result reads.

## 18. Relationship to Other Governing Documents

- `GAME_CONSTITUTION.md` and `SOURCE_HIERARCHY.md` remain the authority on *what* the rules hierarchy is and how compatibility/provenance are classified. This protocol governs the *research process* used to apply them faithfully.
- `docs/rules/_template.md` remains the required shape of a finished Rule Card (Stage B's output). This protocol governs what must be true before that template is filled in with confidence.
- `DEVELOPMENT_WORKFLOW.md` §9.7 (revalidation) and §9 generally (decision records) reference this document rather than duplicating it.
- `AGENTS.md` §10 binds agents to this document's hard gates rather than restating them.
- This document does not change `ARCHITECTURE.md`, the Pre-Code Development Gate, the Rules Baseline Migration Gate, `DEC-0007`, or `DEC-0008` in any way.

## 19. Status

Adopted `docs/decisions/DEC-0009-evidence-first-rule-research-protocol.md`, `APPROVED`, 2026-08-16. This is the default workflow for substantial historical Rule Cards and revalidations going forward. `EXP-001`'s revalidation is the first Rule Card research task expected to follow it in full — expected to produce a committed `docs/rules/evidence/EXP-001-evidence.md` Stage-A artifact, not a rewritten Rule Card, as its first deliverable.
