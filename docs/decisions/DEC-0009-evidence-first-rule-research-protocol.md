# DEC-0009: Evidence-First Rule Research Protocol

## Decision ID
DEC-0009

## Title
Evidence-First Rule Research Protocol

## Status
Approved

## Date
2026-08-16

## Context

`EXP-002`'s (Dungeon Turn / Time Accounting) Rules Cyclopedia revalidation exposed a repeated failure mode in which mechanical synthesis began before the complete governing Rules Cyclopedia procedure had actually been located and read. Two compounding problems produced plausible-looking, but wrong, specifications and required repeated correction cycles across multiple passes:

1. **Incomplete primary-source acquisition treated as sufficient.** An initial revalidation pass relied on secondary-source corroboration and search-engine summaries after direct primary-text fetches repeatedly failed (connection refusals, content-length truncation, blocked mirrors), and proceeded to propose an executable Simulator Ruling anyway. A subsequent pass, once direct primary-text access actually succeeded, found that the Rules Cyclopedia itself directly and explicitly resolved the exact question the self-generated ruling had been invented to cover — the earlier synthesis had not been forced by a genuine gap in the source, only by an access failure that was treated as though it were one.
2. **Legacy-card anchoring.** Detailed comparison against the superseded 1974-primary Rule Card shaped the research questions asked of the Rules Cyclopedia from early in the process, rather than the Rules Cyclopedia's own governing procedure being understood independently first and the legacy card consulted only afterward, for provenance and completeness comparison.

The existing single-pass workflow (`Historical Source → Research → Rule Card Draft → Human Review`, `AGENTS.md` §9 prior to this record; `DEVELOPMENT_WORKFLOW.md` §9.7's revalidation description prior to this record) did not structurally separate "evidence has been gathered and is sufficient" from "a polished mechanical specification has been written," and did not require a human checkpoint between them. This let an agent's desire to produce a complete artifact substitute for actually closing the evidentiary gap first.

## Decision

**Rules research now requires primary-source acquisition, evidence collection, a whole-source cross-reference pass, a falsification/challenge pass, and human evidence review — before Rule Card mechanical synthesis begins.**

This replaces the single-pass pipeline with a two-stage lifecycle:

```text
PRIMARY-SOURCE ACQUISITION
        ↓
EVIDENCE COLLECTION
        ↓
WHOLE-SOURCE CROSS-REFERENCE SEARCH
        ↓
FALSIFICATION / CHALLENGE PASS
        ↓
HUMAN EVIDENCE REVIEW                      ◄── hard gate
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

Core principle: **evidence must close before mechanical synthesis begins.** A research agent must not produce a polished executable specification from incomplete primary evidence, and must not cross from the Evidence stage into the Synthesis/Draft stage without explicit human authorization.

The full, detailed procedure — the primary-source hard gate, the confidence vocabulary, the whole-source cross-reference requirement, the falsification-pass format, the RC-first/legacy-card-later ordering for revalidation, the "do not preserve simulator machinery by inertia" principle, the gap-directed-only rule for alternate-source research, the last-resort rule for Simulator Rulings, the required Stage-A evidence-report contents, and the complete set of hard-stop conditions — is specified in `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md`, which this decision adopts as the canonical, detailed research protocol. This record does not duplicate that document's content.

`AGENTS.md` §9–§10 and `DEVELOPMENT_WORKFLOW.md` §9.7 are updated to bind agents to this protocol and to reference it rather than restate it.

## Rationale

Preventing premature synthesis is worth the added process overhead. Rules research for a source-authoritative simulator is only as trustworthy as its worst-verified fact; a single unverified assumption smuggled into an otherwise well-written Rule Card is difficult to catch during human review of the finished artifact, precisely because the artifact reads as authoritative. Separating evidence-gathering from drafting, and inserting a human checkpoint between them, makes the unverified state of a research pass visible *before* it is dressed up as a specification, not after.

Requiring Rules Cyclopedia research to start from the current source's own governing procedure — rather than from the superseded Rule Card's framing — directly addresses the anchoring failure mode: a legacy card's existing structure, vocabulary, and even its named variables shape what an agent thinks to look for, independent of whether that structure is actually what the new authority requires. RC-first research avoids importing 1974-shaped assumptions merely because they were already written down somewhere convenient.

Making "stop, evidence is inadequate" an explicitly successful, expected outcome — rather than a failure state to be avoided by finishing the artifact anyway — directly targets the pattern this decision responds to: an access failure or a genuine gap should produce a stop-and-report, not a self-generated Simulator Ruling invented to keep the task moving.

## Consequences

- Rule Card research and revalidation normally becomes two separate agent tasks (Stage A — Evidence, and Stage B — Synthesis/Draft) rather than one, with a human review point between them. A trivial Rule Card may collapse the two stages only when a human explicitly authorizes doing so for that specific card.
- `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` is created as the canonical, detailed protocol document. Stage-A evidence reports are committed as durable repository artifacts under `docs/rules/evidence/<RULE-ID>-evidence.md` (protocol §12) — not itself a Rule Card, not mechanically authoritative, and never assigned `APPROVED` Rule Card status, but preserved after human evidence review so Stage-B drafting and future audits can see exactly what evidence supported synthesis.
- `AGENTS.md` §9's implementation-workflow diagram and §10's Rules Research Workflow are updated to reference the new protocol rather than describing the single-pass pipeline.
- `DEVELOPMENT_WORKFLOW.md` §9.7's description of revalidation is updated to reflect the same two-stage lifecycle, replacing its prior "same research→draft→human-review workflow already used for a new Rule Card" framing.
- Individual research tasks should see fewer downstream correction cycles and higher source confidence, at the cost of more research tasks stopping short of a finished artifact and awaiting further human direction — this is treated as the protocol working as intended, not as a shortfall.
- This decision does not change which source is primary (`DEC-0007`) or which RC-optional systems this project has selected for V1 (`DEC-0008`); it operationalizes how research under the existing source hierarchy is conducted, and complements both records rather than reopening either.
- No Rule Card's own mechanical content, status, or approval is changed by this decision. `EXP-001`, `EXP-004`, and every other `REVALIDATION_REQUIRED` or unresearched inventory entry are unaffected; their future research is simply expected to follow this protocol going forward, starting with `EXP-001`.
- `ARCHITECTURE.md` is not modified by this decision.

## Supersedes

None.

## Superseded By

None.

This decision complements `DEC-0007-rules-cyclopedia-primary-rules-authority.md` and `DEC-0008-rules-cyclopedia-v1-rules-profile.md` — it does not revise, reopen, or supersede either. `DEC-0007` decided which source governs; `DEC-0008` decided which of that source's own offered configurations this project's V1 uses; this record decides how research under that governing source is actually performed and verified before a Rule Card may rely on it.
