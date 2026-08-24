# DEC-0010: Primary-Source Completeness Audit Required for Rule Research

## Decision ID
DEC-0010

## Title
Primary-Source Completeness Audit Required for Rule Research

## Status
PROPOSED — AWAITING HUMAN APPROVAL

## Date
2026-08-23

> **Lifecycle note.** This record is **not approved and is not active authority.** It was previously drafted with `Status: Approved`; that was an error — an implementation agent has no authority to approve a project-wide process decision (`DEVELOPMENT_WORKFLOW.md` §9, `AGENTS.md` §12). The repository's decision-record lifecycle (§9.4) had no prior pre-approval status, so this record adopts `PROPOSED — AWAITING HUMAN APPROVAL`, aligned with the Rule Card lifecycle's existing `AWAITING_APPROVAL` term. Until a human project owner approves it, `DEC-0009` and the pre-amendment protocol remain the operative process, and the amendments this record proposes are drafted-but-not-in-force.

## Context

`DEC-0009` adopted the Evidence-First research protocol (`docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md`) after `EXP-002`'s revalidation exposed that mechanical synthesis had begun before the governing Rules Cyclopedia procedure was fully located. That protocol added a mandatory whole-source cross-reference pass (§9), a falsification pass (§10), and a human evidence-review gate (§11).

Those additions were necessary but, as `CLUSTER-002` Stage A demonstrated, not sufficient.

During `CLUSTER-002` Stage-A research into `CHAR-003` (Hit Points & Hit Dice), the researcher identified an apparent internal Rules Cyclopedia contradiction over the Elf's maximum level: Chapter 1 (p. 12) states dwarves and elves may not progress beyond 12th level, while the Chapter 2 Elf entry and Chapter 10 both state 10th. The contradiction was escalated to human review as an unreconciled internal source conflict.

**The Elf Experience Table on RC p. 26 was never inspected.** That table is the mechanically authoritative statement of Elf progression: its Level column terminates at 10 (600,000 XP, Attack Rank C), after which it lists only XP thresholds mapped to Attack Ranks C through M. The Elf Saving Throws Table immediately beneath it uses level bands 1-3 / 4-6 / 7-9 / 10, capping identically. Two structurally decisive tables sat on a single page that the "whole-source cross-reference" pass reported as covered.

Three compounding process failures made this possible, and none is caught by the protocol as it stood:

1. **OCR/full-text search was treated as equivalent to source inspection.** Research was conducted against a flattened OCR transcription. That transcription had dropped the Elf Experience Table's rows from the elf section entirely.
2. **A failed keyword search was recorded as a positive finding of absence.** The researcher searched for a Hit Dice column pattern, found none, and reported that this "closes the internal RC options." The table has no Hit Dice column at all, so no keyword search of that shape could ever have found it.
3. **That false absence then licensed escalation to alternate sources.** Believing RC exhausted, the researcher proceeded to BECMI — which `SOURCE_HIERARCHY.md` §3 and `RULE_CARD_RESEARCH_PROTOCOL.md` §15 permit only once a genuine RC gap is documented. The precondition was manufactured by the failed search.

The Tables Index entry `Elf Experience Table . 26` was present in the researcher's own working notes and was used to source page citations for other tables. It was not followed.

This is a fidelity failure of exactly the kind this project exists to prevent, and it is not adequately addressed by asking researchers to search harder. Tables, stat blocks, and charts are simultaneously the artifacts most likely to carry decisive mechanical content and the artifacts least likely to survive OCR linearization intact.

## Decision

**Stage-A rules research must include a formal Primary-Source Object / Table Completeness Audit, and mechanically significant tables and structured objects must be verified visually, before Human Evidence Review.**

Specifically:

**1. OCR and full-text search are locators, not proof of coverage.** A researcher may not claim primary-source completeness on the basis that keyword searches have been exhausted. Full-text search establishes where to look; it does not establish that everything relevant has been looked at.

**2. A Primary-Source Object / Table Completeness Audit becomes a required Stage-A step**, inserted between the whole-source cross-reference search and the falsification pass. For each rules responsibility, the researcher must enumerate and account for every potentially governing primary-source object — Table of Contents entries, Tables Index entries, named tables, class/monster/item/spell stat blocks, summary boxes, complete governing prose sections, followed cross-references, and appendix/index entries — recording each as inspected or deliberately excluded with a reason.

**3. Mechanically significant tables and structured objects must be verified against the visual page**, not OCR alone, whenever the object governs numbers or progression, column relationships matter, OCR formatting is degraded, the object conflicts with prose, or the object is otherwise mechanically operative. If usable page images cannot be obtained, Stage A stops with `STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED`.

**4. Every Stage-A evidence packet must carry a Primary-Source Coverage Checklist**, so that a reviewer can ask "what objects could govern this mechanic, and did the researcher inspect each one?" and get an auditable answer.

**5. An Independent Evidence-Completeness Review pass is required before Human Evidence Review.** Its objective is to discover material the original pass failed to inspect, starting from the source's own Table of Contents and Tables Index rather than from the evidence packet. It is not a second synthesis pass, and it is not a confirmation pass.

**6. Table-heavy responsibilities are high-risk research.** Where mechanically significant tables drive the procedure — character advancement, combat, saving throws, Weapon Mastery, spells, treasure, monster statistics and generation, equipment, encumbrance/movement, experience, class progression — visual table verification and independent completeness review are mandatory rather than discretionary.

**7. A failed search is not evidence of absence.** Negative findings must be recorded as "not located by the searches performed," never as a positive claim that the source does not address the question, unless the relevant objects have themselves been inspected and found silent.

**8. Alternate-source escalation requires object-level RC exhaustion.** The precise RC gap statement required by `RULE_CARD_RESEARCH_PROTOCOL.md` §15 may not be written on the basis of keyword-search exhaustion alone; the completeness audit for that responsibility must have been performed first.

**9. Guardrail A — no guessed-answer searches as substitutes for locating governing objects.** A researcher may not search for a guessed *rendering of an answer* — a dice expression, XP total, level title, formula, numeric total, or expected table-cell representation — in place of locating the governing source object. Such searches are legitimate **later**, as supplementary or falsification tools. They may never establish source completeness. A failed guessed-formula search is evidence about the query, not evidence that the rule, table, or value is absent. *(Motivating defect: the `9d6 + 1` Elf query that returned only Ch. 14 Lich material.)*

**10. Guardrail B — negative findings must describe the research performed.** Distinguish `"Not located after inspecting X, Y, Z"` from `"The Rules Cyclopedia contains no such rule."` The stronger source-property claim is permitted only after the relevant governing objects have actually been enumerated and inspected sufficiently to support it. Exhausted keyword searches alone never establish absence.

**11. Guardrail C — per-class / per-entity table attestation.** Where a Rule Card concerns a subject possessing a named class table, experience table, saving-throw table, monster table or stat block, spell table, item table, equipment table, progression table, or analogous per-entity structured object, the evidence packet must explicitly record that object as `OPENED`, `VISUALLY INSPECTED`, and `DISPOSITIONED` — or explicitly excluded with a stated reason. **A named table may not silently exist outside the packet's coverage checklist.** *(This guardrail alone would have caught the Elf Experience Table immediately.)*

**12. Guardrail D — additional mandatory high-risk triggers.** Beyond the table-heavy classification in item 6, the following independently trigger heightened review:
   - **a per-class/per-entity table exists for the researched subject**;
   - **searches return only out-of-domain or obviously irrelevant hits.** The required response to (b) is to **question the search strategy before drawing any conclusion about the source**. Lich results from an Elf progression query are evidence that the query is poorly targeted — never evidence that Elf material is absent.

**13. Structure-first ordering of research operations.** Full-text search retains its value as a locator, cross-reference finder, and falsification tool. It is not the primary completeness mechanism. The governing order of operations is source structure → finding aids → object inventory → visual inspection → governing prose → cross-references → whole-source search → falsification → independent completeness review → human evidence review.

## Rationale

The failure mode `DEC-0009` addressed was *stopping too early in the pipeline* — synthesizing before evidence closed. The failure mode this record addresses is different and was not covered: *believing evidence had closed when an entire class of source object had never been opened*.

Keyword search over OCR text is a fundamentally lossy instrument with a systematic blind spot precisely where this project's fidelity risk is highest. A table's meaning lives in its column relationships and in the structural fact of where its rows stop — neither of which survives linearization, and neither of which a substring query can interrogate. The Elf Experience Table's decisive content is not a phrase; it is the absence of an eleventh level row. No amount of searching harder finds that. Only looking does.

Requiring an object-level inventory converts completeness from something a researcher asserts into something a reviewer can check. Requiring visual verification of operative tables removes the instrument's blind spot rather than asking researchers to compensate for it. Requiring an independent completeness pass acknowledges that the researcher who missed an object is, by construction, the person least likely to notice its absence.

The cost is real: page-image inspection is slower than text search. That cost is accepted. This project's stated standard is historical fidelity, and a process that can produce a confident, well-formatted, thoroughly-cited evidence report while never opening the governing table does not meet it.

## Consequences

- `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` gains the object/table completeness audit, the visual-verification requirement, the coverage-checklist requirement, the independent completeness-review pass, the research-risk classification, Guardrails A–D, the structure-first operations order, the within-source evidence-type guidance, and a new hard-stop condition. Its Stage-A sequence diagram is amended accordingly. **These amendments take effect only on human approval of this record.**
- **Prior BECMI research disposition (human ruling, 2026-08-23):** the BECMI material produced from the invalid RC-exhaustion conclusion **must not be used** as current evidence or as synthesis input. It is preserved in session/branch history for research provenance only, and is not deleted. If alternate-source research is later properly justified after genuine RC object-level exhaustion, it must be **performed anew** from the corrected RC evidence state; no conclusion may be inherited merely because it was already generated.
- Stage A becomes slower and more expensive. This is intended.
- `CLUSTER-001`'s and `CLUSTER-002`'s existing evidence were audited against this standard as part of adopting it; results are recorded in `docs/rules/evidence/CLUSTER-001-completeness-audit.md` and `docs/rules/evidence/CLUSTER-002-completeness-audit.md`.
- `CLUSTER-002`'s Human Evidence Review clearance is suspended pending review of that audit. `CLUSTER-002` Stage B is paused.
- `CLUSTER-001` remains `VERIFIED` with respect to its approved specification and its 2026-08-18 implementation verification. `VERIFIED` is not a claim that source research can never be reopened, and this record does not alter that status.
- No existing Rule Card, production module, or test is modified by this record. Any specification-affecting audit finding must go through a separate, human-approved governance path.
- This record does **not** weaken RC primary authority, the alternate-source ordering, the falsification requirement, the human evidence-review gate, the RC-first/legacy-later rule, Simulator Rulings as last resort, or human Rule Card approval. It strengthens Stage A only.

## Supersedes

None. This record **amends** `DEC-0009`'s Stage-A process by adding required steps. `DEC-0009` remains `Approved` and in force; its historical text is not rewritten to imply it ever contained these requirements.

## Superseded By

None.
