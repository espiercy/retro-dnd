# Research Process Precedents

> **What this document is.** An auditable register of **procedural precedents** established by completed rules-research work — practices that proved necessary in a real cluster and that a future researcher should follow.
>
> **What this document is NOT.** It is **not** a governing document, it does **not** amend `docs/decisions/DEC-0009-*`, `DEC-0010-*`, `DEC-0011-*`, `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md`, `AGENTS.md`, or any other protected authority, and it creates no new obligation on its own. Each entry records what happened, what it cost, and what a future pass should therefore do. **A human project owner may elevate any entry into the protocol or a decision record; until that happens, an entry is precedent and rationale, not law.**
>
> Created 2026-09-14 at `CLUSTER-003` Stage-A closure, because the repository had no process-learnings location and the precedent below is cross-cluster rather than specific to `CLUSTER-003`.

## Register

| # | Precedent | Established by | Status |
|---|---|---|---|
| **P-001** | **When a primary source provides a General Index, General Index inspection is a required source-structure completeness instrument for `DEC-0010` research, alongside the Table of Contents and the Tables Index.** | `CLUSTER-003` Stage-A remediation pass 1, 2026-09-13 | **Precedent recorded.** Not yet elevated into `DEC-0010` or the research protocol. |

---

## P-001 — The General Index is a required completeness instrument

### The statement

```text
When a primary source provides a General Index, General Index inspection
is a REQUIRED source-structure completeness instrument for DEC-0010
research, alongside the TOC and the Tables Index.
```

### What happened

`CLUSTER-003`'s first Stage-A pass followed `DEC-0010`'s structure-first order and used two structural instruments thoroughly: the **Table of Contents** (audit class A) and the **Index to Tables and Checklists** (audit class B). It recorded the **General Index** (audit class H) as *"only partially discharged"* and did not treat that as blocking. It then performed a whole-source keyword pass, a falsification pass, and an adversarial self-review.

The independent completeness review returned `FAIL — unfinished structural inspection`. Remediation swept the General Index, and the sweep located **two governing objects all three earlier methods had missed**:

| Object | Why the other instruments missed it |
|---|---|
| **RC Ch. 8 p. 103, "Movement"** — states that a character's normal speed is *never used during the combat sequence*, adds movement-budget rules, and contains a factor-of-3 contradiction with Ch. 6 on running speed | Ordinary prose under the one-word heading "Movement", sitting inside **another procedure's** section (the combat sequence). It carries **no table**, so the Tables Index cannot reach it; the TOC lists only the chapter's major sections; and a topic-driven search for `movement rate` did not surface it because the section does not use that phrase. |
| **RC Ch. 14 p. 153, "Charge"** — *"A monster cannot charge in certain types of terrain: broken, heavy forest, jungle, mountain, swamp"*, with *"20 yards (**20 feet indoors**)"* | Filed under a combat-attack heading in the monsters chapter. Reached only via the index entry `Terrain. 119, 153`. |

The General Index also produced the decisive ownership evidence for a separate question — `Weapon restrictions 14, 17, 19, 21, 23, 25, 26, 28, 29`, nine class pages with the equipment chapter absent — and corrected two citations.

### Why the failure mode is general, not incidental

A mechanic named by a **common word** will be distributed across a source under headings that neither a chapter list nor a table list enumerates. The TOC indexes *structure*; the Tables Index indexes *structured objects*; only a General Index indexes **subjects wherever they are discussed**, including in plain prose belonging to some other procedure.

```text
TOC            -> chapters and major sections
Tables Index   -> named tables and checklists
General Index  -> SUBJECTS, wherever they appear, including prose
                  subordinate to an unrelated procedure
Keyword search -> strings the researcher already thought to try
```

`DEC-0010`'s own warning — *"a failed search is not evidence of absence"* and *"OCR text and full-text search are locators, not proof of coverage"* — is what this precedent extends. The General Index is the one instrument that can answer *"where else does this source talk about X?"* without the researcher having to guess the phrasing first.

### What a future pass should do

1. Treat audit class H (appendices/index) as **blocking**, not as a formality discharged last.
2. Sweep the General Index for the mechanic's name **and its synonyms and variants** — for `CLUSTER-003` that meant equipment, weapons, armor, encumbrance, load, carrying, movement, speed, running, walking, mapping, terrain, dungeon, climbing, and the individual class names.
3. **Follow every plausible page reference to the governing text.** The index is a locator, never proof; an index entry that is not followed has discharged nothing.
4. Record the **absence** of an index entry too. `CLUSTER-003` strengthened a negative finding by recording that the RC General Index contains no `Marching`, `Formation`, or `Carrying capacity` entry.
5. Where a source provides no General Index, say so explicitly rather than leaving the class silently undischarged.

### Cost of learning it

One independent-review `FAIL`, one full remediation pass, and — had the defect survived — a cluster that would have specified movement without the rule bounding which scale applies in combat.

### Provenance

- `docs/rules/evidence/CLUSTER-003-remediation-pass-1.md` §5.3, §5.5
- `docs/rules/evidence/CLUSTER-003-completeness-audit.md` §13.3
- `docs/rules/clusters/CLUSTER-003-equipped-dungeon-movement.md` §3.0a

### Elevation status

```text
PRECEDENT RECORDED -- NOT YET ELEVATED
```

Elevating P-001 into `DEC-0010` or into `RULE_CARD_RESEARCH_PROTOCOL.md` §9.1's audit-class table would make it binding. Both are protected/authority documents, and neither was modified by this pass. **That elevation is a human decision.** It was not taken here because the assigning task directed a process note in preference to a constitutional rewrite.
