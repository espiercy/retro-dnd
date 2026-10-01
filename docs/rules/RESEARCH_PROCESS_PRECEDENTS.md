# Research Process Precedents

> **What this document is.** An auditable register of **procedural precedents** established by completed rules-research work — practices that proved necessary in a real cluster and that a future researcher should follow.
>
> **What this document is NOT.** It is **not** a governing document, it does **not** amend `docs/decisions/DEC-0009-*`, `DEC-0010-*`, `DEC-0011-*`, `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md`, `AGENTS.md`, or any other protected authority, and it creates no new obligation on its own. Each entry records what happened, what it cost, and what a future pass should therefore do. **A human project owner may elevate any entry into the protocol or a decision record; until that happens, an entry is precedent and rationale, not law.**
>
> Created 2026-09-14 at `CLUSTER-003` Stage-A closure, because the repository had no process-learnings location and the precedent below is cross-cluster rather than specific to `CLUSTER-003`.

## Register

| # | Precedent | Established by | Status |
|---|---|---|---|
| **P-001** | **When a primary source provides a General Index, General Index inspection is a required source-structure completeness instrument for `DEC-0010` research, alongside the Table of Contents and the Tables Index.** | `CLUSTER-003` Stage-A remediation pass 1, 2026-09-13 | **ELEVATED** into `RULE_CARD_RESEARCH_PROTOCOL.md` §9.9 by `DEC-0012`, `Approved` 2026-10-01 — **binding**. See "Elevation" below. |
| **P-002** | **A `DEC-0011` mandatory source object — a conflict-precedence statement — must be sought by opening the front matter of every core source unit. A keyword sweep cannot establish that none exists.** | `CLUSTER-003` `DEC-0011` BECMI remediation 1, 2026-09-24 | **Precedent recorded; PARTIALLY covered, not elevated.** Its general lesson now binds for primary-source claims through `DEC-0012` §10.4; its alternate-source front-matter requirement is **not** elevated. See "Elevation" below. |

## Elevation record (added 2026-09-30)

`DEC-0012` was drafted after `CLUSTER-004` Stage A required five independent completeness reviews. Its root-cause analysis found that **`P-001`'s failure mode recurred**: `CLUSTER-004` pass 1 *cited* the RC General Index and missed `Blindness . 150, 154` sitting in it — the entry that falsified the packet's own headline conclusion. That made the cost of leaving the precedent unelevated concrete:

```text
P-001 recorded at CLUSTER-003 closure     cost: 1 independent-review FAIL, 1 remediation pass
P-001 still not binding at CLUSTER-004    cost: recurred, contributing to 4 more FAIL cycles
```

**`P-001` is therefore elevated** into `RULE_CARD_RESEARCH_PROTOCOL.md` §9.9 as binding protocol, with its four required operations (sweep synonyms, follow every plausible reference, record absent entries, state explicitly when a source provides no such instrument) carried across substantially as this register stated them, and extended to specialist indexes such as a spell index.

**`P-002` is deliberately not elevated here.** Its general half — that a negative finding must rest on structural inspection rather than a keyword sweep — is now binding for **primary-source** claims through §10.4's Negative Claim Gate, which requires structural instruments and indexes checked before any absence may be asserted. Its specific half — that a conflict-precedence statement must be sought by opening the **front matter of every core alternate-source unit** — remains precedent only, because **alternate-source research was outside the authorization of the task that drafted `DEC-0012`**, and elevating a `DEC-0011` obligation is a change to alternate-source governance rather than to Stage-A primary research.

**That remains a human decision**, and it is worth taking: `P-002`'s second-order lesson — that a falsification pass offering itself only the readings it already has in mind can reject the wrong one and still reach a false conclusion — is a general defect that §10.6 does not fully close.

---

## P-002 — Precedence statements are found by reading front matter, not by searching for the concept

### The statement

```text
DEC-0011 item 6 makes conflict-precedence statements MANDATORY source
objects. They must be located by opening the introduction / front
matter of EVERY core source unit. A keyword sweep for the CONCEPT
cannot establish that no such statement exists, because such
statements are routinely written in plain prose that uses none of
the words a researcher would think to search for.
```

### What happened

The `CLUSTER-003` BECMI gap-research pass discharged `DEC-0011` item 6 with a whole-corpus regular-expression sweep for:

```text
supersede | replaces the | instead of the (rules|version)
         | take precedence | these rules replace | revised (rules|version)
```

It returned nothing relevant, and the package recorded *"no global conflict-precedence statement was located in the nine core source units inspected."*

**An explicit precedence statement existed**, in the **Master Players' Book, p. 2**, under the section heading *"The Ultimate Game"*:

> *"If you discover a contradiction between this set and previous sets, the rules given here should be used."*

**It contains none of the six search terms**, and no plausible seventh. It says *"contradiction"*, *"previous sets"*, and *"should be used"* — ordinary words that carry the rule without ever naming it. This same object was one of the motivating facts behind `DEC-0011` itself, which makes the miss worse rather than more forgivable: the record that created the obligation quoted the object the pass then failed to find.

The independent completeness review caught it and returned the package for remediation. The consequence was not cosmetic: the missed object **changed a classification**, from `D — BECMI IS INTERNALLY CONFLICTED` to `B — BECMI SUPPORTS ONE RC READING`, because the lineage turned out to resolve internally a conflict the package had reported as unresolved.

### Why the failure mode is general

A precedence rule is a **meta-rule**. Authors state it once, in prose, at the front of a book, in whatever words the sentence happens to want — and they have no reason to use the vocabulary a later researcher will search for. There is no table to find it in, no index entry guaranteed to name it, and no distinctive term it must contain.

```text
What a keyword sweep can find     rules that NAME themselves
What front matter carries          rules that merely STATE themselves
```

The structural location, by contrast, is highly predictable: an introduction, a preface, a "how to use this book" box, or a title-page note.

### What a future pass should do

1. **Open the front matter of every core source unit** — introduction, preface, "how to use this book", title-page notes — and read it. This is cheap: it is one page per unit.
2. **Classify what is found**, and do not collapse the categories. A **prerequisite** statement (*"you must have the Basic set to use this"*), an **additive** statement (*"these rules are designed to add to those in the Basic Set"*), and a **precedence** statement (*"the rules given here should be used"*) are three different things. Only the third allocates priority.
3. **Record the scope** of any precedence statement explicitly, in its own terms, and record what it does **not** reach (`DEC-0011` items 6 and 10).
4. **Use search only to corroborate**, never to establish the negative. If a sweep is performed, record the exact terms used, so a reviewer can see what the negative finding actually rests on.
5. **Where no statement is found, scope the negative to the units whose front matter was read** — not to the lineage.

### A second-order lesson, recorded because it caused the same error

The pass's falsification step framed the suit-armor question as a binary: *is the entry an override, or is it merely an inconsistent value?* It correctly rejected the first, and then treated the second as established by elimination. **A third possibility existed in the source** — that the lineage resolves the conflict at **set level**, by a rule living nowhere near the entry. A falsification pass that offers itself only the readings it already has in mind can reject the wrong one and still reach a false conclusion.

### Cost of learning it

One independent-review rejection, one remediation pass, and one classification published wrongly for eight days.

### Provenance

- `docs/rules/evidence/CLUSTER-003-becmi-gap-research.md` §2.5 (withdrawn and replaced), §5 (re-evaluation), §10.1, §11 challenge 3

### Elevation status

```text
PRECEDENT RECORDED -- NOT YET ELEVATED
```

Elevating `P-002` into `DEC-0011` item 6 or into `RULE_CARD_RESEARCH_PROTOCOL.md` would make it binding. **Neither was modified by this pass** — the assigning task directed a bounded remediation, not a governance change. **That elevation is a human decision.**

> **Partially covered 2026-09-30, still not elevated.** `DEC-0012` §10.4 makes this precedent's *general* half binding for **primary-source** negative claims: an absence may not be asserted without recording the structural instruments and indexes checked, and a failed keyword sweep is never sufficient. Its **alternate-source** half — open the front matter of every core source unit — is **unchanged and still not binding**, because alternate-source research was outside that task's authorization. The register's "Elevation record" section states why, and recommends the remaining elevation to the human project owner.

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

> **Superseded 2026-09-30.** The status above records the state at `CLUSTER-003` closure and is preserved as written. **`P-001` was subsequently ELEVATED** into `RULE_CARD_RESEARCH_PROTOCOL.md` §9.9 by `DEC-0012` (drafted 2026-09-30, **`Approved` 2026-10-01**), under a human-assigned process-remediation task, after the same failure mode recurred in `CLUSTER-004`. See the register's "Elevation record" section above.
