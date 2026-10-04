# Rule Card Research Protocol — Evidence-First

## 1. Status and Authority

> **Supersession notice (`DEC-0013`, drafted 2026-10-04).** The Stage-A **evidence-packet
> mechanism** described in this document — the Coverage Manifest, the general Negative
> Claim Record requirement, the Repository Fact Gate's prose rows, the blanket
> self-falsification pass, the hand-maintained coverage counts and the
> Research-Completion Gate's self-declared checklist — was adopted by `DEC-0012` and is
> **superseded by** `docs/decisions/DEC-0013-externally-derived-stage-a-evidence-checks.md`.
>
> `DEC-0012`'s pilot (`ENC-001`) did not pass its own fixed success criteria. The
> diagnosis was right and is retained: *evidentiary closure, not rules interpretation*,
> is what fails. The remedy was not, because those instruments are the researcher's own
> account of the researcher's own work — **internal consistency is not external
> completeness**. Page-seed obligations are now derived from `INVENTORY.md` and accepted
> neighbour packets, citations are matched mechanically against page transcriptions, and
> counts are derived rather than written.
>
> **What still binds, unchanged:** everything in this document about *how to research* —
> the two-stage Evidence-First structure, the primary-source visual-access hard stop, the
> confidence vocabulary (§6), the open-question closure vocabulary (§10.2), the
> hard-stop conditions (§17), the prohibition on self-certification (§10.1.2), and the
> rule that an original researcher never certifies its own packet.
>
> **What no longer binds:** the packet *shape* in §11.2 and the `DEC-0012` instrument list.
> Use `docs/rules/evidence/_TEMPLATE.md`, which is the canonical packet form, and
> `scripts/lint_evidence.py`, which is its gate.
>
> `DEC-0012` references below are **historical** — they record what was done and why, and
> are deliberately not rewritten. Where this document's packet-shape instructions conflict
> with `DEC-0013`, `DEC-0013` governs.

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
RESEARCH-START GATE                                ◄── §5.1 (DEC-0012)
        ↓
PRIMARY-SOURCE ACQUISITION                         ◄── hard gate (§4)
        ↓
EVIDENCE COLLECTION                                ◄── §5
        ↓
SOURCE-STRUCTURE / FINDING-AID REVIEW              ◄── §9.1.1; TOC / Tables Index
        ↓
INDEX-INSTRUMENT ENUMERATION                       ◄── §9.9 (DEC-0012)
        ↓
COVERAGE MANIFEST                                  ◄── §9.3.1 (DEC-0012)
        ↓
PRIMARY-SOURCE OBJECT / TABLE COMPLETENESS AUDIT   ◄── §9.1 (DEC-0010)
        ↓
VISUAL INSPECTION OF MECHANICALLY
SIGNIFICANT OBJECTS                                ◄── §9.2, §9.2.1
        ↓
COMPLETE-ENTRY / DETAILED GOVERNING MATERIAL       ◄── §9.7 (DEC-0010)
        ↓
EXPLICIT CROSS-REFERENCES                          ◄── §9.1 audit class G
        ↓
WHOLE-SOURCE CROSS-REFERENCE SEARCH                ◄── §9
        ↓
FALSIFICATION / CHALLENGE PASS                     ◄── §10
        ↓
NEGATIVE CLAIM LEDGER                              ◄── §10.4 (DEC-0012)
        ↓
REPOSITORY-FACT VERIFICATION PASS                  ◄── §10.5 (DEC-0012)
        ↓
OPEN-QUESTION CLOSURE GATE                         ◄── §10.2 (DEC-0010)
        ↓
PRE-REVIEW SELF-FALSIFICATION PASS                 ◄── §10.6 (DEC-0012)
        ↓
ADVERSARIAL SELF-REVIEW                            ◄── §10.1.1 (DEC-0010)
        ↓
RESEARCH-COMPLETION GATE                           ◄── §11.1 (DEC-0012);
        ↓                                              the evidence linter passes
INDEPENDENT COMPLETENESS REVIEW                    ◄── §10.1.2 hard gate;
        ↓                                              NOT by the original researcher
HUMAN EVIDENCE REVIEW                              ◄── hard gate (§11)
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

**This is the project's single canonical Stage-A order.** §9.1.1 states the same sequence at finer granularity, with the structure-first rationale. There is no alternative or interchangeable ordering of these stages.

> **Amended by `DEC-0012` (`Approved` 2026-10-01).** The gates marked `DEC-0012` above are additions. `DEC-0010` item 13 stated this sequence in its pre-`DEC-0012` form and is **superseded as to the sequence only**; that record's own text is preserved rather than rewritten (`DEVELOPMENT_WORKFLOW.md` §9.4), and `DEC-0012` Decision item 13 carries the amended sequence. Where `DEC-0010` item 13 and this section differ, **this section governs.**

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

## 5.1 Research-Start Gate

> Added by `DEC-0012`. Cheap to discharge, and it prevents the expensive discovery — made four times in `CLUSTER-004` — that the source cannot be completely inspected, or that the project boundary being researched is stale, *after* a full research pass has already been written.

Before substantive Stage-A research begins, establish and record each of the following. "Establish" means *verified this pass*, not *recalled*:

| Item | What must be established |
|---|---|
| **Exact card scope** | The card's currently registered scope, read from `docs/rules/INVENTORY.md` this pass — not from memory and not from a cluster document's summary of it |
| **Known ownership seams** | The neighbouring Rule IDs and what each owns, so a consequence can be routed rather than absorbed |
| **Authoritative primary source** | Edition, printing, and the exact access method for page images |
| **Required structural / index instruments** | Which instruments this source provides — TOC, Tables/Checklists Index, General Index, specialist indexes (§9.9) |
| **Current repository dependencies** | The card's incoming/outgoing dependencies and each one's actual status, verified under §10.5 |
| **Primary-source visual-access availability** | That page images for the expected governing region actually render (§9.2.1) — spot-checked, not assumed from the access method having worked for another card |

If visual access is already known to be unavailable for a region the card plainly needs, the correct outcome is `STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED` at the start of the task, not after it.

This gate is recorded as the packet's first section (§11.2). It is not a substitute for any later gate.

## 6. Confidence Vocabulary

Every evidence-map row's Confidence column uses exactly one of:

- **DIRECT PRIMARY TEXT** — quoted or closely paraphrased directly from inspected RC primary text.
- **PRIMARY TEXT + CROSS-REFERENCE CONFIRMED** — direct primary text, independently corroborated by a second passage or internal cross-reference within the same primary source (e.g., a stated page reference that was itself checked).
- **NECESSARY CONSEQUENCE** — not itself stated by RC, but a logically forced arithmetic/mechanical consequence of two or more DIRECT PRIMARY TEXT facts, with the derivation shown.
- **SECONDARY SOURCE LOCATOR ONLY** — found only via a secondary source; primary text has not (yet) been directly inspected for this specific fact. **May guide further research. Cannot authorize mechanics** — a row at this confidence level blocks Stage A from closing on that question.
- **NOT YET VERIFIED** — a plausible reading not yet checked against primary text at all; a placeholder, not a finding.
- **NOT YET ESTABLISHED** — *added by `DEC-0012`.* The correct classification for a **suspected absence** whose §10.4 enumeration is not complete. It says *"the enumeration required to claim the source is silent here has not been finished"* — never *"the source is silent."* A row at this level blocks Stage A from closing on that question, exactly as the two levels above it do.
- **REPOSITORY FACT — NOT A SOURCE CLAIM** — *added by `DEC-0012`.* For a row asserting something about **this project** rather than about the source (ownership, landed status, inventory content). Such a row is verified under §10.5, not by source inspection, and none of the labels above describes it. Recorded because `CLUSTER-004` review 5 Finding 8 found four cells where a project fact had been forced into a source-confidence column, and observed that forcing one would be worse than the plain wording.

A Stage A evidence report is not ready for human review while any consequential row still carries `SECONDARY SOURCE LOCATOR ONLY`, `NOT YET VERIFIED` or `NOT YET ESTABLISHED` — either the primary text must be located and inspected, or the row must be reported as an unresolved research question (§4, §11) rather than smoothed over.

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

This is the **formal** whole-source search pass. It occurs **after** the source's structure and governing objects have been mapped and inspected (§9.1, §9.2, §9.7) — exploratory searching may of course happen earlier, but an incidental search is not this stage and never closes the evidence (§9.1.1). Once that structural work is done, deliberately search the **entire** available primary text for related terminology before treating the evidence map as complete. Do not assume the full mechanic is located in one chapter merely because the first relevant passage was found there.

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

## 9.1 Mandatory Primary-Source Object / Table Completeness Audit

> **Adopted by `docs/decisions/DEC-0010-primary-source-completeness-audit.md`, `Approved` 2026-08-29. §9.1–§9.8, §10.1–§10.3, the corresponding Stage-A sequence steps in §3, and the §17 hard stops added by that record are in force.** They were drafted after `CLUSTER-002` Stage A produced an apparently thorough whole-source cross-reference report while never opening the Elf Experience Table (RC p. 26) — the object that mechanically governs the very question being escalated.

### 9.1.0 The recorded defect this section exists to prohibit

Stated once, precisely, so the prohibited behavior is unambiguous:

```text
Stage A surfaced the Tables Index entry:  Elf Experience Table . 26
The table was not opened.
Stage B later substituted guessed formula searches (9d6 + 1, 9d6 + 2).
Those searches returned only Ch.14 Lich material.
The null/irrelevant result was promoted into an RC-exhaustion conclusion.
That conclusion improperly licensed alternate-source (BECMI) escalation.
```

The point is not to shame prior research; it is to fix exactly which behaviors are now prohibited.

### 9.1.1 Structure-first order of operations

```text
RESEARCH-START GATE                                ◄── §5.1
        ↓
SOURCE STRUCTURE FIRST
        ↓
TOC / TABLES INDEX                                 ◄── §9.1 audit classes A, B
        ↓
INDEX-INSTRUMENT ENUMERATION                       ◄── §9.9 (General Index,
        ↓                                              specialist indexes)
COVERAGE MANIFEST                                  ◄── §9.3.1; before conclusions
        ↓
GOVERNING SOURCE-OBJECT INVENTORY                  ◄── §9.1 audit classes C–I
        ↓
VISUAL INSPECTION OF TABLES / STRUCTURED OBJECTS   ◄── §9.2, §9.2.1
        ↓
COMPLETE-ENTRY / DETAILED GOVERNING MATERIAL       ◄── §9.7
        ↓
EXPLICIT CROSS-REFERENCES                          ◄── §9.1 audit class G
        ↓
WHOLE-SOURCE CROSS-REFERENCE SEARCH                ◄── §9
        ↓
FALSIFICATION / CHALLENGE PASS                     ◄── §10
        ↓
NEGATIVE CLAIM LEDGER                              ◄── §10.4
        ↓
REPOSITORY-FACT VERIFICATION PASS                  ◄── §10.5
        ↓
OPEN-QUESTION CLOSURE GATE                         ◄── §10.2
        ↓
PRE-REVIEW SELF-FALSIFICATION PASS                 ◄── §10.6
        ↓
ADVERSARIAL SELF-REVIEW                            ◄── §10.1.1
        ↓
RESEARCH-COMPLETION GATE                           ◄── §11.1; linter passes
        ↓
INDEPENDENT COMPLETENESS REVIEW                    ◄── §10.1.2; NOT by the
        ↓                                              original researcher
HUMAN EVIDENCE REVIEW                              ◄── §11
```

**This is the same Stage-A sequence as §3, at finer granularity — not a second, competing one.** Every required gate appears in the same order. The gates added by `DEC-0012` appear in both.

**Exploratory search may occur opportunistically, whenever it is useful.** The **formal whole-source cross-reference search pass (§9)** shown here occurs *after* structural mapping and governing-object inspection, and **only the formal sequence governs evidence-completeness closure.** An incidental search that happens earlier is a research convenience; it is not this stage, and it never closes the evidence.

Full-text search remains valuable. Its role is **locator, cross-reference finder, and falsification tool** — never primary completeness mechanism.

> **A full-text search hit is a locator, not an authority category.**
>
> **A null search result is information about the query, not automatically about the source.**

**OCR text and full-text search are locators, not proof of coverage.** Completing §9's keyword pass does **not** establish that the relevant primary-source material has been reviewed. Full-text search tells you where to look. It does not tell you that you have looked.

This matters because mechanically authoritative content routinely lives in objects that keyword search over linearized text cannot reliably reach:

```text
tables                    class/monster/item/spell stat blocks
charts                    experience tables
saving-throw tables       attack tables
equipment tables          Weapon Mastery tables
spell tables              sidebars and summary boxes
chapter summaries         appendices
indexes                   table indexes
cross-reference lists     page-layout structures OCR flattens
```

A table's meaning often lies in its **column relationships** and in **where its rows stop** — neither of which survives linearization, and neither of which a substring query can interrogate.

### Required audit contents

For every Rule Card or coherent research responsibility, Stage A must explicitly inspect and account for all potentially governing primary-source objects:

| # | Object class | Requirement |
|---|---|---|
| A | **Table of Contents** | Identify every chapter/section plausibly relevant to the mechanic. |
| B | **Tables Index / List of Tables** | Search for every table whose title or subject may bear on the mechanic. This is a completeness instrument, not a citation convenience. |
| C | **Named tables** | Inspect every relevant table **directly**. |
| D | **Stat blocks** | Where relevant, inspect class/monster/item/spell blocks separately from surrounding prose. |
| E | **Summary boxes** | Do not assume summary material duplicates detailed prose correctly. It demonstrably sometimes does not. |
| F | **Detailed prose** | Read the complete governing section, not OCR search snippets. |
| G | **Cross-references** | Follow every explicit "see Chapter X", "see table", "see page" reference. |
| H | **Appendices / index entries** | Use as completeness locators; follow any mechanically relevant reference. |
| I | **Duplicate/parallel presentations** | When the same mechanic appears in a summary, a table, a class entry, a later chapter, a high-level procedure, and/or an optional rule, **record each separately**. Do not treat any one representation as automatically authoritative over another. |

### A failed search is not evidence of absence

Record negative findings as *"not located by the searches performed"* — never as a positive claim that the source does not address the question — unless the objects in class A–I above have themselves been inspected and found silent. Converting a search miss into a finding of absence is the specific error that produced `DEC-0010`.

### Consequence for alternate-source escalation

The precise RC gap statement §15 requires **may not** be written on the strength of keyword-search exhaustion. This audit must be performed for that responsibility first. Escalating to an alternate source on a manufactured precondition is a governance breach, not merely a research miss.

## 9.2 Visual Verification of Mechanically Significant Objects

Mechanically significant tables and structured objects must be verified against the **visual page or PDF**, not OCR alone. Visual verification is required whenever:

- the object governs numbers or progression;
- column relationships matter;
- OCR formatting is degraded or the object appears mangled;
- the object conflicts with prose, or prose conflicts with it;
- a stat block, chart, or checklist is mechanically operative;
- OCR may have flattened columns, lost alignment, or dropped rows.

OCR remains fully usable for search and navigation. It must not be the **sole** evidence for a mechanically significant object where a visual page is available.

If the current access method cannot provide usable page images:

```text
STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED
```

Do not declare evidence complete. This is a hard gate on the same footing as §4's `STOP — PRIMARY SOURCE ACCESS REQUIRED`.

## 9.2.1 Discharging the Visual-Access Gate — operational rules

> Added by `DEC-0012`. §9.2's hard gate is unchanged; what follows is **how it is discharged**, because `CLUSTER-004` showed the gate being silently walked past rather than disputed.
>
> **The recorded defect this section exists to prohibit.** RC p. 84 renders columns 2 and 3 **blank** in the digitisation this project had been using — at every size tried, with HTTP 200 and payloads up to 1.05 MB, and with the OCR truncating at the same point mid-sentence. Two consecutive passes presented that page as inspected, cited it as the object for an evidence row, stated *"All pages cited were ultimately obtained as images"*, and recorded **no access limitation**. The page's content was eventually obtained from a second digitisation, and the region turned out to hold four general skills that bore on both cards' open questions.

**HTTP success is not visual access.** A `200` response, a full-size payload, and a well-formed image prove that a *file* was served. They prove nothing about whether the page's body text is legible in it. Confirm the text, not the transfer.

**Permitted attempts, in any order:**

- an alternate rendering (different size, format, or derivative);
- magnification or a region crop of the affected columns;
- a local copy of the source already held by the project;
- **another digitisation of the same edition/printing.**

**A second digitisation of the same edition is still primary-source access.** It is the same edition, the same printing, the same primary source, obtained through a different scan. It does **not** engage `SOURCE_HIERARCHY.md`'s alternate-source ordering and does **not** trigger `DEC-0011`. Record which digitisation each affected page came from.

**Prohibited:**

- inferring **absence** from a failed render — an unrenderable region is unknown content, never empty content;
- substituting OCR as proof for a mechanically significant object;
- treating a successful HTTP response as evidence the contents were visible;
- a blanket disposition (*"all remaining rows unrelated"*) covering a region that could not be read. This is the strongest form of the §9.1 error, because the research operation the claim describes was impossible.

**Recording is mandatory whether or not a workaround succeeded** (§11 item 17). Every affected page is recorded with the defect, what was attempted, and how it resolved — in the packet's Visual Inspection Record (§11.2), including on the machine-readable `ACCESS-BLOCKED` line, which is empty only when nothing is blocked.

If no attempt succeeds:

```text
STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED
```

and every evidence row depending on that region is reclassified — not carried forward.

## 9.3 Primary-Source Coverage Checklist (required packet section)

Every Stage-A evidence packet must contain a section titled **Primary-Source Coverage Checklist** recording:

- relevant TOC sections inspected;
- Tables Index entries inspected;
- named tables inspected;
- structured stat blocks inspected;
- relevant chapter sections read in full;
- cross-references followed;
- appendices/index entries checked where applicable;
- visual-page verification completed for significant objects, with page numbers;
- any potentially relevant object **deliberately excluded, with the reason**.

The purpose is auditability: a future reviewer must be able to ask *"what primary-source objects could govern this mechanic, and did the researcher actually inspect each one?"* and get a checkable answer.

## 9.3.1 Coverage Manifest — required before conclusions

> Added by `DEC-0012`. §9.3's checklist says what a finished packet must *contain*. This section fixes **when** it is written, because in `CLUSTER-004` the checklist was repeatedly assembled *after* the conclusions it was supposed to license, and then disagreed with the packet's other two coverage lists across three consecutive passes.

**The required order is fixed:**

```text
enumerate  →  inspect  →  disposition  →  falsify  →  conclude
```

**This is prohibited:**

```text
write conclusions
then reconstruct coverage afterward
```

**Before any substantive mechanical conclusion may be written**, the packet must carry a completed **Coverage Manifest** enumerating, as applicable to the source and the responsibility:

- source chapters / structural units;
- Table of Contents entries;
- Tables / Checklists Index entries;
- General Index entries;
- specialist indexes, such as a spell index (§9.9);
- governing tables;
- governing prose sections;
- cross-references;
- visually inspected pages;
- source pages that could **not** yet be visually inspected (§9.2.1);
- repository dependencies and ownership claims requiring verification (§10.5).

**Every item receives an explicit disposition**, drawn from the vocabulary this repository already uses:

```text
OPENED
VISUALLY INSPECTED
DISPOSITIONED
ROUTED TO <RULE-ID>
EXCLUDED — <stated reason>
ACCESS BLOCKED
NOT YET ESTABLISHED
```

A manifest row may not be blank, and **a row may not be added after the conclusion it would have governed.** Adding one late is not a tidy-up; it is evidence that the conclusion was written without it, and the honest response is to re-derive the conclusion.

**The manifest, the Visual Inspection Record and the Primary-Source Coverage Checklist must agree with each other.** Three lists that disagree are not three sources of assurance; they are proof that at least one is unmaintained. `scripts/lint_evidence.py` checks the machine-readable part of this agreement (§11.1), which is why the packet carries page lists in a fixed block rather than in prose.

## 9.4 Research-Risk Classification

> **Independent completeness review is universally required by §10.1.2 for every substantial Stage-A evidence package under this protocol.** It is **not** conditional on the high-risk classification below, and nothing in this section makes it so. What this section adds for high-risk responsibilities is **heightened scrutiny** and the removal of any discretion over §9.2 visual verification.

**If mechanically significant tables drive the procedure, the responsibility is high-risk research**, and §9.2 visual verification of structured objects is **mandatory, not discretionary** — as is the heightened scrutiny described below. The §10.1.2 independent completeness review applies regardless.

Responsibilities presumed high-risk include: character advancement, combat, saving throws, Weapon Mastery, spells, treasure, monster statistics, monster generation, equipment, encumbrance/movement, experience, and class progression.

**Additional mandatory high-risk triggers (Guardrail D):**

1. **A per-class / per-entity table exists for the researched subject.**
2. **Searches return only out-of-domain or obviously irrelevant hits.**

For trigger 2 the required response is to **question the search strategy before drawing any conclusion about the source**. Lich results from an Elf progression query are evidence that the query is poorly targeted — never evidence that Elf material is absent.

No scoring framework is introduced; the rules above are the whole test.

## 9.5 Prohibited Research Shortcuts

**Guardrail A — no guessed-answer searches as substitutes for locating governing objects.**

> Do not search for a guessed *rendering of an answer* — a dice expression, XP total, level title, formula, numeric total, or expected table-cell representation — as a substitute for locating the governing source object.
>
> Such searches may be used **later**, as supplementary searches or falsification tools. **They may not establish source completeness.**
>
> A failed guessed-formula search is evidence about the **query**, not evidence that the rule, table, or value is absent. A query that presupposes an object's schema cannot succeed if the schema differs, and its failure carries no information about the source.

**Guardrail B — negative findings must describe the research performed.**

> Distinguish:
>
> ```text
> "Not located after inspecting X, Y, Z…"        ← research-operation claim
> "The Rules Cyclopedia contains no such rule."  ← source-property claim
> ```
>
> The source-property claim is permitted **only** after the relevant governing objects have been enumerated and inspected sufficiently to support it. Exhausted keyword searches alone never establish absence.

**Guardrail C — per-class / per-entity table attestation.**

> Where a Rule Card concerns a subject possessing a named class table, experience table, saving-throw table, monster table or stat block, spell table, item table, equipment table, progression table, or analogous per-entity structured object, the evidence packet must explicitly record it as:
>
> ```text
> OPENED
> VISUALLY INSPECTED
> DISPOSITIONED
> ```
>
> — or explicitly excluded with a stated reason. **A named table may not silently exist outside the packet's coverage checklist.**

## 9.6 Evidence Types Within a Single Source

Distinct from `SOURCE_HIERARCHY.md`, which ranks *editions*. This ranks *object types within one primary source*, as a **guide to locating and weighing governing evidence** — not a mechanical precedence rule.

```text
1. Mechanically operative table for the responsibility
2. Structured stat block for the specific subject
3. Detailed governing procedure text / class-details prose
4. Explicit cross-reference, followed to its target
5. Chapter-level or step-list summary
6. Incidental prose reference elsewhere in the source
7. Full-text search hit outside the governing procedure — LOCATOR ONLY
```

**The governing object depends on the rule type. Do not apply this order mechanically:**

- **Class progression** — the class/experience table and the detailed class material are both first-class evidence.
- **Procedure systems** — a numbered procedure or checklist may itself be the governing operational object, with no table involved. (`EXP-001`'s Game Turn Checklist is of this kind.)
- **Monster / spell / item catalog entries** — the structured entity entry is the principal source object.

**Do not adopt a rule such as "tables always beat prose."** RC p. 25 states the Elf's 10th-level hit-point gain as `+1` in its stat block and as "two additional hit points" in its own Class Details prose, on the same page. A table or stat block and detailed prose can genuinely conflict.

**The requirement is to identify all governing objects before interpreting conflicts among them** — not to resolve conflicts by object type.

## 9.7 Complete-Entry Inspection Rule

> Adopted by `DEC-0010`. Motivated by the `CHAR-002` failure: the p. 7 summary table was treated as exhaustive while the detailed Druid entry — which carries additional transition requirements — went unread.

Where a responsibility concerns a **character class, race/class, monster, spell, item, or similarly structured entity**, the relevant detailed entity entry must be inspected **as a complete source unit**. For a class this may include:

```text
stat block
experience / progression table
saving-throw table
class details
special abilities
entry / transition requirements
explicit cross-references
```

**Do not treat isolated search windows as equivalent to reading the entry. Do not treat one summary table as automatically exhaustive.**

## 9.8 "Single Governing Object" Claims

A researcher may identify a **principal** governing object. A researcher may **not** call it *the single governing object* until all related structured and detailed source objects have been enumerated and dispositioned.

The existence of a summary table does not prove that detailed entity material adds no qualification. RC p. 7's class/ability table is the principal object for creation eligibility; it is **not** the whole of what RC says about class entry.

## 9.9 Index Instruments Are Completeness Instruments

> **Elevated from precedent `P-001` to binding protocol by `DEC-0012`.** `P-001` was recorded at `CLUSTER-003` closure and deliberately left `NOT YET ELEVATED`, so it bound nobody. `CLUSTER-004` pass 1 then *cited* the General Index and missed `Blindness . 150, 154` sitting in it — the entry that falsified the packet's headline conclusion. This is the **third** time in this project that the General Index has caught material three other instruments missed. It is now law, not precedent.

Where the authoritative source provides an index instrument, that instrument is a **completeness instrument, not a citation aid.** Each applicable instrument must be **enumerated and dispositioned**, including:

- the **General Index**;
- the **Tables / Checklists Index**;
- a **spell index**;
- any other **specialist index** relevant to the responsibility.

Each instrument reaches something the others cannot:

```text
TOC              -> chapters and major sections
Tables Index     -> named tables and checklists
General Index    -> SUBJECTS, wherever they appear, including plain prose
                    subordinate to an unrelated procedure
Specialist index -> the entity class it indexes, by name
Keyword search   -> strings the researcher already thought to try
```

**Required operations:**

1. Sweep each instrument for the mechanic's name **and its synonyms and variants**, not one canonical term.
2. **Follow every plausible page reference to the governing text.** An index entry that is not followed has discharged nothing.
3. **Record absent entries.** That a source's General Index has no entry for the mechanic's obvious name is itself a research fact, and it explains where the bridge to the governing pages actually runs.
4. Where the source provides no such instrument, say so explicitly rather than leaving the class silently undischarged.

**A packet may not state that an index was read in full unless its own ledger makes the enumeration auditable** (§9.10). The requirement is **not** to transcribe an entire index into every packet. It is to demonstrate that relevant entries were considered *systematically* rather than encountered opportunistically — which is exactly the difference between the pass that missed `Blindness . 150, 154` and the pass that used the same instrument to reach five governing pages.

## 9.10 Prohibited Completeness Language

> Added by `DEC-0012`. `CLUSTER-004` produced, across four passes, *"read ROW BY ROW"* over rows whose descriptions were unrenderable, *"all remaining rows inspected and EXCLUDED AS UNRELATED"*, and *"All pages cited were ultimately obtained as images"* — each false, and each a sentence rather than a defect in the research that could be pointed at.

The following words and phrases are **completeness claims**:

```text
read in full          fully inspected        complete
exhaustive            all relevant entries   every entry
```

A completeness claim may be used **only where a coverage instrument in this packet makes it auditable** — the Coverage Manifest (§9.3.1), an index-enumeration ledger (§9.9), or the Visual Inspection Record. The reader must be able to check the claim against a list, not take it on trust.

Where no such instrument supports it, **use narrower wording that describes exactly what was inspected**:

```text
PERMITTED   "Entries A, B and C of the Tables Index were opened and dispositioned;
             the remainder were read and judged unrelated on the stated grounds."
PROHIBITED  "The Tables Index was read in full."     (with no ledger behind it)
```

This is §9.5 Guardrail B applied to the *research-operation* claim rather than to the source-property claim: just as *"RC contains no such rule"* requires enumeration, so does *"I inspected all of it."* Both are claims about the world, and both are checkable.

Restate the claim as an **operation**, not a property: *"every entry on p. 301 was read, and each one relevant to this card is dispositioned above"* is auditable; *"nothing on p. 301 is undispositioned"* is a property claim that a reader cannot verify and that `CLUSTER-004` demonstrated was false when made.

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

## 10.1 Adversarial Self-Review vs. Independent Completeness Review

> Adopted by `DEC-0010`. These are **two different gates**. Do not blur them, and do not blur either with ordinary falsification (§10).

### 10.1.1 Adversarial self-review — may be performed by the original researcher

Required. Must restart from **source structure** — TOC, Tables Index, chapter and entry headings, cross-reference targets — rather than from its own prior conclusions or checklists. Starting from prior work reproduces the original pass's blind spots.

It must also ask, explicitly:

```text
What did the original packet say was unfinished?
Did every unfinished region actually get inspected?
Does any packet claim completeness while still containing
  "not checked" / "not read" / "not exhaustively searched" /
  "needs later research" / "source region not inspected"?
```

If yes: **FAIL COMPLETENESS PREPARATION.** Do not paper over it.

### 10.1.2 Independent completeness review — may NOT be performed by the original researcher

```text
INDEPENDENT COMPLETENESS REVIEW:
REQUIRED BEFORE HUMAN EVIDENCE CLEARANCE

ORIGINAL RESEARCHER MAY NOT ISSUE
THE FINAL COMPLETENESS CERTIFICATION
FOR ITS OWN EVIDENCE PACKAGE.
```

Must be performed by a **different reviewer context that did not conduct the evidence collection being certified**: another model/reviewer, a human reviewer, or a genuinely separate research session that does not rely on the original agent's unstated assumptions, if the project later defines that as sufficiently independent.

> **Extended to alternate sources by `DEC-0011` (`Approved` 2026-09-04, in force).** §15.1.6 applies **this same reviewer role** to a materially consequential alternate-source lineage conclusion. It creates no new or parallel reviewer role and does not alter §10.1.1.

**Permitted output of an original researcher:** `PREPARED FOR INDEPENDENT COMPLETENESS REVIEW`.
**Prohibited output of an original researcher:** `SOURCE COMPLETENESS PASSED`, `SOURCE COMPLETENESS CERTIFIED`, `HUMAN EVIDENCE GATE CLEARED`.

## 10.1.3 The Independent Reviewer's Role — restated, not weakened

> Added by `DEC-0012`. **Nothing here reduces §10.1.2.** Independent review remains mandatory for every substantial Stage-A package, the original researcher still may not certify its own packet, and the reviewer remains free — and expected — to return `FAIL`.

What changes is the **expected difficulty of the reviewer's job**:

```text
Observed failure mode (CLUSTER-004 reviews 1-3)
    the independent reviewer discovers basic uninspected governing objects
    -- a light-conditioned table, a page stating the consequence the packet
       called absent, a whole chapter never opened

Desired role
    the independent reviewer adversarially challenges an already exhaustive packet
```

The gates added by `DEC-0012` exist to raise the **floor** of what reaches this reviewer, so that reviewer effort is spent on judgement rather than on bookkeeping. A reviewer who nevertheless finds an uninspected governing object should `FAIL` the packet and say so plainly — that outcome now indicates the earlier gates were not actually discharged, which is itself the finding.

**§10.3's method is retained in full and is the instrument that worked.** The reviewer builds its own candidate-object list **from the source's own structure, before opening the packet.** `CLUSTER-004` reviews 3, 4 and 5 each did this, and it is how they found what the packets had missed. A reviewer that starts from the packet inherits the packet's blind spots and cannot discharge this gate.

**The target process shape** after this remediation:

```text
research pass  →  self-falsification  →  ONE independent review  →  human evidence review
```

A second independent review should be **exceptional**, not routine. Five is a process failure, and it is recorded as one.

## 10.2 Open-Question Closure Gate

> Adopted by `DEC-0010`. **Completeness may not be declared while the packet's own declared unfinished work is outstanding.**

Every Stage-A packet must carry an inventory of its own unresolved statements — wording such as *not yet read in full, not exhaustively checked, not searched, not verified visually, may exist elsewhere, needs later confirmation, open question, unresolved by current research, possible interaction not yet checked*.

Each item must be classified as exactly one of:

```text
RESOLVED BY SOURCE INSPECTION
CONFIRMED OUT OF SCOPE  (with explicit ownership and rationale)
RETAINED AS GENUINE SOURCE AMBIGUITY
BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED
```

**There may be zero silent unresolved research tasks at the completeness gate.**

A packet may contain genuine rule ambiguities. It may **not** contain **unfinished source inspection disguised as an ambiguity**. That distinction must be made explicit for every item.

### 10.2.1 Required reconciliation table

The completeness reviewer must not only ask *what objects do the TOC and Tables Index contain?* but also *what did the original evidence packet itself say had not yet been checked?*

| Original open question | Source region/object implicated | Inspection completed? | Result | Responsibility owner | Still blocks completeness? |
|---|---|---|---|---|---|

**No card may be marked complete until every row is dispositioned.**

### 10.2.2 Genuine source conflict is not source incompleteness

```text
SOURCE COMPLETE  ≠  SOURCE UNAMBIGUOUS
```

A primary source may be **fully mapped and still contradict itself.** Stage A's job is to establish that everything governing has been inspected — not to make the Rules Cyclopedia consistent. Three cases must be distinguished, and only the first two are stops:

| Case | Condition | Disposition |
|---|---|---|
| **1. Incomplete conflict research** | Conflicting passages found **and** potentially governing objects remain uninspected | `BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED` → `STOP — MORE PRIMARY RESEARCH REQUIRED`. **Completeness cannot pass.** |
| **2. Unauthorized mechanical resolution** | The agent would pick one side, silently prefer one object type, or proceed as though the conflict did not exist | `STOP — INTERNAL SOURCE CONFLICT REQUIRES REVIEW` |
| **3. Fully mapped genuine conflict** | All relevant governing objects inspected; contradictory passages accurately recorded; the completeness reviewer confirms no obvious governing material remains uninspected; no unfinished inspection is disguised as ambiguity | `RETAINED AS GENUINE SOURCE AMBIGUITY`. **This may pass source completeness** and proceeds to the appropriate later human/Stage-B resolution path. |

Case 3 is not a loophole for case 1. It requires every one of its listed conditions, and the reconciliation table (§10.2.1) is where a reviewer checks that the difference is real: a row saying *"the source says two different things, and here is each object I opened"* is case 3; a row saying *"the source seems to conflict and I did not check X"* is case 1.

**Live reference case: the Elf 10th-level fixed hit-point gain, `+1` versus `+2`** (`docs/rules/evidence/CLUSTER-002-completeness-audit.md` Finding 3). Four RC statements were located and **visually verified as printed**, including a stat block and its own Class Details prose contradicting each other on a single page (p. 25). Nothing governing it remains uninspected. It is `RETAINED AS GENUINE SOURCE AMBIGUITY`, its card passed source completeness, and its mechanical resolution is a **Stage-B** problem — not evidence of a Stage-A failure.

## 10.3 Independent Evidence-Completeness Review — method

> **Who performs it is fixed by §10.1.2, not by this section.** §10.3 states the *method* only. It does not create a second, self-servable form of independent review: the pass described here **must** be carried out by a reviewer context that did not conduct the evidence collection being certified. An original researcher applying this method is performing **adversarial self-review** (§10.1.1), and its output is `PREPARED FOR INDEPENDENT COMPLETENESS REVIEW` — never a completeness certification.

Before Human Evidence Review, Stage A must include a **distinct completeness-review pass** whose objective is to **identify relevant primary-source material the original research pass may have failed to inspect**.

This is **not** another synthesis pass, and **not** a confirmation pass. It must begin from:

```text
the source's own Table of Contents
the source's own Tables Index
relevant chapter headings
relevant structured tables / stat blocks
```

— **not** from the evidence packet. Starting from the packet reproduces the original pass's blind spots.

The reviewer challenges, at minimum:

```text
Were all relevant tables located?
Were all relevant stat blocks checked?
Did the Tables Index reveal anything absent from the packet?
Did a later chapter restate the mechanic?
Did OCR flatten, mangle, or drop a meaningful table?
Did the researcher treat prose as complete when an operational table exists?
Did the packet follow all explicit cross-references?
Was any negative finding asserted as absence rather than as "not located"?
```

The reviewer is **encouraged to discover omissions rather than confirm the original work**. A completeness review that finds nothing must say what it looked for and where, not merely that it agrees.

Record the result in the evidence packet's Coverage Checklist (§9.3) or in a dedicated completeness-audit artifact (§12), whichever is cleaner for the responsibility in question.

**Do not certify completeness merely because no new keyword hits appear.**

## 10.4 Negative Claim Gate

> Added by `DEC-0012`. This is §9.5 Guardrail B given a **required artifact** instead of a required attitude. Guardrail B was already explicit and already correct; `CLUSTER-004` pass 1 breached it twice, in its two headline conclusions, and both were false.
>
> **The recorded defect this section exists to prohibit.** Pass 1 asserted that RC *"states no consequence for having no light"* — calling it *"the single largest apparent gap in the card"* — and that RC has **no** light-conditioned table. RC states the consequence at p. 150 and prints the table at p. 93. Worse, the project's own landed `CHAR-005` §7 already cited p. 150 for those very movement rates, so the refutation was inside the repository when the claim was written.

**An absence claim requires stronger evidence than a positive finding**, because a positive finding cites an object and an absence claim cites the whole source.

The following are **material negative claims**:

```text
"RC has no ..."                    "no table exists ..."
"no procedure exists ..."          "the source is silent ..."
"there is no dungeon mechanic"     "no dependency exists ..."
```

Such a statement **may not appear as an established finding** unless a **Negative Claim Record** exists for it, recording at minimum:

```text
claim
scope searched
structural instruments checked
indexes checked
search terms used
cross-references followed
visual pages inspected
falsification attempt
confidence classification
```

**A failed keyword or OCR search is never sufficient evidence of absence.** Where the enumeration above has not been completed, the required classification is:

```text
NOT YET ESTABLISHED
```

— **not** source silence. `NOT YET ESTABLISHED` is an honest, non-blocking-to-write, blocking-to-close state (§6): it says the work required to make the claim has not been done. Converting it to silence without doing that work is the `DEC-0010` error repeated.

**Before writing any negative claim, check the repository against it** (§10.5). A negative claim about the source that the project's own landed cards already contradict is the cheapest possible failure to avoid, and it has now occurred.

**Where the ledger carries no material negative claim**, the packet says so explicitly in the ledger's stated `NONE` form rather than omitting the section.

## 10.5 Repository Fact Gate

> Added by `DEC-0012`. This is the one genuinely **missing rule** the `CLUSTER-004` analysis found: the protocol governs source research end to end and said nothing about claims concerning *this project*.
>
> **The recorded defect this section exists to prohibit.** A packet routed RC p. 150's generic conditions to `CHAR-011` — which `INVENTORY.md` defines as **Weapon Mastery**, a card that touches none of them. A second mis-routing followed in the sibling packet, and an earlier pass had called p. 147 *"unowned"* when the inventory assigns it. Each was asserted without opening the file that refutes it, in packets whose source research was otherwise sound.

**Claims about this project require repository evidence.** The following are repository facts, not source facts:

```text
"CHAR-011 owns this"              "this card is landed"
"there is no Rule ID"             "this dependency is unresearched"
"this mechanic has no owner"      "this test already covers X"
"the inventory says ..."          "the implementation contains ..."
```

Each must be **verified against the current repository during the active research pass.** **Model memory does not count as evidence**, and neither does a prior packet's assertion of the same fact — that is how a wrong owner ID propagates.

Every repository-fact entry must **name the artifact actually inspected**, and where practical the relevant identifier or section:

```text
PERMITTED   CHAR-005 §7 owns the blindness movement column
            -> docs/rules/character_creation/encumbrance_and_movement_rate.md §7, read this pass
PROHIBITED  CHAR-011 owns the p. 150 conditions
            -> (no artifact named; INVENTORY.md line 90 in fact says Weapon Mastery)
```

Where a repository fact has not been checked, it is marked:

```text
UNVERIFIED PROJECT FACT
```

rather than asserted. An `UNVERIFIED PROJECT FACT` blocks the Research-Completion Gate (§11.1) exactly as an undischarged source question does.

**A distinct repository-fact verification pass** runs before independent review, separately verifying every concrete project assertion the packet makes. **This is not source-completeness review** — it is project-state verification, and it catches the class of error where the rules research is correct but the routing is wrong. Its results live in the packet's Repository-Fact Verification section (§11.2).

## 10.6 Pre-Review Self-Falsification Pass

> Added by `DEC-0012`. Distinct from §10's per-conclusion falsification (which happens *during* research) and from §10.1.1's adversarial self-review (which restarts from source structure). This is a **final sweep over the packet's conclusions as written**, immediately before requesting independent review.

Before a packet may enter independent completeness review, the researcher must actively search for evidence that would make each of its major conclusions **false** — not merely re-read them for consistency.

**Mandatory coverage.** The pass must cover, at minimum:

- every **material negative claim** (§10.4);
- every **ownership assignment** (§10.5);
- every **source-silence finding**;
- every **dependency conclusion**;
- every **scope exclusion**.

These five are not arbitrary: they are the categories that actually failed. `CLUSTER-004` produced a false negative claim, two wrong ownership assignments, a false source-silence finding, a dependency conclusion stated at the wrong count, and a blanket scope exclusion over a region that could not be read.

**Required record, per conclusion:**

```text
Conclusion:
What evidence would falsify it?
Where was that evidence sought?
Result:
Disposition:
```

`Disposition` uses §10's vocabulary — `CONFIRMED` / `QUALIFIED` / `REJECTED`. A `REJECTED` conclusion triggers `STOP — MORE PRIMARY RESEARCH REQUIRED` and is **not** replaced with a second speculative model (§10).

**A packet may not enter independent review until this pass is complete.** "Complete" means every listed category has been swept, and the sweep is recorded — not that the researcher is satisfied. Note the asymmetry this exploits: it is much easier to ask *"what would make this false, and did I look there?"* than to notice an absence in one's own work, which is precisely why §10.1.2 exists and why this pass does not replace it.

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

## 11.1 Research-Completion Gate

> Added by `DEC-0012`. The gate a packet must clear **before independent completeness review may be requested.** Its purpose is to stop a reviewer's time being spent on defects the researcher could have found deterministically.

Independent review may be requested only once **every** line below is confirmed:

```text
[ ] every Coverage Manifest row is dispositioned            §9.3.1
[ ] no unresolved visual-access blocker remains             §9.2, §9.2.1
[ ] every material negative claim has a Negative Claim Record  §10.4
[ ] every repository fact has been verified this pass        §10.5
[ ] the pre-review self-falsification pass is complete       §10.6
[ ] open questions are explicitly listed and classified      §10.2
[ ] required §6 and §10.2 vocabulary is used verbatim        §6, §10.2
[ ] the evidence linter passes                               below
```

**"Confirmed" means checked, not assumed.** A checklist filled in from memory reproduces the failure this gate exists to prevent.

### The evidence linter

```text
uv run python scripts/lint_evidence.py
```

`scripts/lint_evidence.py` is a **structural** checker, and its limits are part of its definition:

```text
IT DOES        verify that required instruments are present
               verify that the packet's own ledgers agree with each other
               verify controlled vocabulary in the columns that have one
               verify that a blocker or a BLOCKED item forbids a ready recommendation

IT DOES NOT    read the primary source
               judge whether the research is correct
               judge interpretation, ownership, or mechanical synthesis
```

**A green linter is a floor, never a certification.** It cannot see a governing object nobody enumerated, and it is not evidence of completeness — §10.1.2's independent review remains the only thing that certifies that, and only a human project owner accepts the evidence (§11).

The linter runs as a gate in the project's canonical verification operation (`docs/technical/TOOLCHAIN_AND_CI.md` §8), so a non-conforming packet fails verification in the same run as a failing test.

**Grandfathering.** Stage-A packets that existed when `DEC-0012` was adopted are exempt by name, listed in the linter's `GRANDFATHERED` set and pinned by a test. Retro-fitting new ledgers to accepted evidence would rewrite it rather than improve it. **The list is closed** — a packet written after `DEC-0012` is never added to it. Reviewer artifacts (completeness reviews, audits, gap-research records) are not Stage-A packets and are not linted.

**The template is linted as a reference packet on every run**, so this gate is never structurally inert. Because every packet in the repository today is grandfathered, a linter governing only real packets would check nothing and pass vacuously — and a green gate that inspected nothing is worse than no gate, because it is read as enforcement. The template is a real committed artifact, it is what every future packet is copied from, and its absence is itself a finding (§11.2). The gate says explicitly when it has checked only the reference packet, so `Evidence: PASS` is never mistaken for *"a real packet was verified."*

## 11.2 Required Stage-A Packet Template

Every new Stage-A packet is started from:

```text
docs/rules/evidence/_TEMPLATE.md
```

The template structurally requires this protocol's instruments, in the §9.3.1 order, so that conformance is the default rather than something a researcher must remember to supply. Its sections are:

```text
 1. Research-Start Gate                  §5.1
 2. Primary Source Accessed              §4, §11 item 17
 3. Source Structure                     §9.1.1
 4. Coverage Manifest                    §9.3.1
 5. Index Enumeration                    §9.9
 6. Governing Objects                    §9.1, §9.8
 7. Visual Inspection Record             §9.2, §9.2.1
 8. Cross-Reference Ledger                §9, §9.1 class G
 9. Repository-Fact Verification         §10.5
10. Evidence Map                         §5, §6
11. Negative Claim Ledger                §10.4
12. Ownership and Dependency Routing     §10.5
13. Falsification Pass                   §10, §10.6
14. Open-Question Closure                §10.2
15. Primary-Source Coverage Checklist    §9.3
16. Independent Review Status            §10.1.2, §11.1
```

The template's own section numbering may be adapted to a responsibility's shape, but **each instrument must be present and identifiable** — the linter matches on the section names above. §11's required report contents are unchanged by this section; the template is where they live.

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

> **Object-level precondition (`DEC-0010` item 8).** The gap statement below **may not** be written on the strength of keyword-search exhaustion. The §9.1 object/table completeness audit and the §9.7 complete-entry inspection must have been performed for that responsibility first, and the objects they enumerate must have been inspected and found silent. Escalating on a gap statement manufactured by a failed search is a governance breach, not merely a research miss.

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

## 15.1 Multi-Unit Lineage Corpus Completeness

> **IN FORCE.** Adopted by `docs/decisions/DEC-0011-alternate-source-lineage-completeness.md`, `Approved` 2026-09-04. This section is active project governance and applies alongside §15, `DEC-0009` and `DEC-0010`, none of which it supersedes.

### 15.1.0 The recorded defect this section exists to prohibit

```text
The Elf HP question reached Stage B as a fully mapped RC self-contradiction.
Gap-directed research inspected the BECMI Expert Set    → +2
                        and the BECMI Companion Set     → +2
and declared the BECMI lineage "unanimous at +2".
The Master Set was never inspected. Master Players' Book p.12 states +1,
and Master Players' Book p.2 carries an earlier-set conflict-precedence rule.
The lineage is evolved and conflicting, not unanimous.
```

**Object-level rigor existed inside the source units that were selected. No completeness discipline governed the selection of source units.** This is not a "search harder" defect — no additional search of Expert and Companion could have found a statement in Master.

**The same defect has a second, nested form.** A set-only enumeration would permit `Master Set — INSPECTED` while only the Master DM's Book had been opened — and the governing `+1` statement is in the **Master Players' Book**. §15.1.1 is therefore hierarchical, and a parent-level disposition is explicitly insufficient.

### 15.1.1 Required hierarchical corpus inventory

Where gap-directed research relies on a **named multi-unit lineage**, before any lineage-level claim, enumerate the corpus as a **structure**, working down to the level at which a rule can be independently stated:

```text
LINEAGE
    ↓
STRUCTURAL UNITS          stages, sets, editions, printings — whatever
    ↓                     the lineage's own organization uses
CORE SOURCE UNITS         the individual rulebooks/volumes within each
    ↓                     structural unit
GOVERNING OBJECTS         entries, tables, stat blocks, procedures
                          inside each source unit (§9.1)
```

1. **Enumerate structural units** from the lineage's own structure, before opening anything.
2. **Enumerate the core source units within each materially relevant structural unit.** Relevance is assessed against the research question and recorded.
3. **Disposition every enumerated core source unit** as `INSPECTED` or `EXCLUDED WITH VERIFIED REASON` — the lineage analogue of §9.5 Guardrail C.

**A parent-level disposition is insufficient:**

```text
INSUFFICIENT     Master Set — INSPECTED

SUFFICIENT       Master Set
                   ├── Master Players' Book — INSPECTED → GOVERNING
                   └── Master DM's Book     — INSPECTED / EXCLUDED WITH VERIFIED REASON
```

**The vocabulary is generic on purpose.** A lineage packaged as boxed sets, as single volumes, as numbered printings, or as a rulebook plus errata is covered equally; **no packaging model is privileged, and BECMI's boxes are an illustration, not a mandated shape.**

*Illustrative BECMI corpus — not a mandate that every product be inspected:*

```text
BECMI
├── Basic      ├── Players Manual              └── Dungeon Masters Rulebook
├── Expert     └── Expert Rulebook
├── Companion  ├── Players Companion           └── Dungeon Masters Companion
├── Master     ├── Master Players' Book        └── Master DM's Book
└── Immortals  ├── Players' Guide to Immortals └── DM's Guide to Immortals
```

**Scope bound — do not overcorrect.** The corpus is the lineage's **core rules**. Adventures/modules, accessories, magazine articles, setting supplements, and unrelated products are **not** automatically in scope. Identifying what constitutes the core rules corpus is part of the recorded assessment, and anything beyond it remains gap-directed under §15.

### 15.1.2 A level-range or subject assumption excludes nothing, at either level

A structural unit **or a core source unit** whose nominal level range or apparent subject does not reach the question must still be dispositioned **by inspection** where it can **restate, revise, or supersede** earlier rules. Scope-based exclusion requires verification, not inference.

> The Elf caps at level 10; the Master Set covers levels 26–36; the Master **Players' Book** p. 12 nonetheless reprints the **entire Elf class entry** and revises both its hit points and its spell progression.

### 15.1.3 Later duplicate presentations are governing objects

A later source unit reprinting or revising an earlier one's class entry, table, or procedure is a **duplicate presentation** (§9.1 class I). Record each separately. **No presentation is authoritative over another by virtue of position in the lineage.**

### 15.1.4 Conflict-precedence statements — locate them, and bound them

Where any source unit states how contradictions with other units resolve, that statement is a **mandatory source object**, and its **scope must be recorded explicitly**.

> **A lineage-internal precedence rule governs that lineage's own source units. It does not travel to a later consolidating product.** The Master Players' Book p. 2 instruction governs the relationship among the BECMI boxed sets; it does not determine what the Rules Cyclopedia intends. Treating "the later unit says its rules win" as decisive for RC would be the mirror image of the defect in §15.1.0.

### 15.1.5 Negative findings and lineage-level claims

Applying §9.5 Guardrail B one layer up:

```text
"Not located in the core source units inspected: X, Y"   ← permitted
"The lineage contains no such rule"                      ← requires §15.1.1
```

**Naming only the structural units inspected is not sufficient** — a negative finding must name the **core source units** actually opened.

The words **unanimous**, **exhaustive**, **internally consistent**, and **absent from the lineage** are lineage-level claims and are prohibited until every materially relevant **core source unit** is dispositioned.

### 15.1.6 Independent Alternate-Source Completeness Review

Where an alternate-source finding will **materially resolve** a documented RC ambiguity or gap:

```text
INDEPENDENT ALTERNATE-SOURCE COMPLETENESS REVIEW
REQUIRED BEFORE THE COMPLETION MAY BE ADOPTED
```

**This uses the existing §10.1.2 reviewer role** — a reviewer context that did not conduct the evidence collection being certified. **No new or parallel reviewer role is created**, and §10.1.1's adversarial self-review is unchanged and still required.

**Permitted output of an original researcher:** `PREPARED FOR INDEPENDENT COMPLETENESS REVIEW`.
**Prohibited output of an original researcher:** certifying a consequential lineage conclusion as `unanimous`, `exhaustive`, or `complete` for the purpose of resolving the RC gap.

Where the finding is not materially consequential, §15.1.1–§15.1.5 still apply but independent review is not separately required.

**Why:** the Stage-B adversarial self-review restarted from the objects *within the source units already chosen*, so it could not surface a unit that was never on the list. That is the same structural limitation §10.1.2 records for primary sources.

### 15.1.7 Alternate-source authority is unchanged

This section grants alternate sources **no** additional authority. RC remains primary (`DEC-0007`). Lineage research exists only to clarify, complete, or help interpret a documented RC gap or conflict. **A later alternate-source unit never overrides RC**, and an inconclusive lineage is a legitimate outcome — it escalates a genuine historical conflict to human adjudication rather than concealing it.

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
| Usable page images are unavailable for a mechanically significant table or structured object (§9.2) | `STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED` |
| The governing procedure has not actually been located, even if a related value has | `STOP — PRIMARY PROCEDURE NOT YET ESTABLISHED` |
| Two or more RC passages conflict and the agent would choose between them, silently prefer one object type, or proceed as though the conflict did not exist, outside the authorized resolution path (§10.2.2 case 2) | `STOP — INTERNAL SOURCE CONFLICT REQUIRES REVIEW` |
| Two or more RC passages conflict **and** potentially governing objects remain uninspected (§10.2.2 case 1) | `STOP — MORE PRIMARY RESEARCH REQUIRED` |
| The falsification pass (§10) rejects a tentative interpretation | `STOP — MORE PRIMARY RESEARCH REQUIRED` |
| An open-question closure-gate item (§10.2) is classified `BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED` | `STOP — MORE PRIMARY RESEARCH REQUIRED` |
| Adversarial self-review (§10.1.1) finds a packet claiming completeness while a declared unfinished source region remains uninspected | `FAIL COMPLETENESS PREPARATION` |
| An alternate-source completion candidate's compatibility with RC cannot be established with confidence | `STOP — COMPLETION COMPATIBILITY NOT ESTABLISHED` |
| Substantial simulator-level behavior remains undefined after §14–§16 | `STOP — HUMAN RULING REQUIRED` |
| A Coverage Manifest row remains undispositioned at the completion gate (§9.3.1, §11.1) | `STOP — COVERAGE MANIFEST INCOMPLETE` |
| A claim about this project remains unverified against the repository at the completion gate (§10.5, §11.1) | `STOP — UNVERIFIED PROJECT FACT` |

**`STOP — INTERNAL SOURCE CONFLICT REQUIRES REVIEW` prevents an agent silently resolving a conflict. It does not mean a fully mapped conflict can never pass source completeness** — see §10.2.2. A contradiction whose governing objects have all been inspected and accurately recorded is `RETAINED AS GENUINE SOURCE AMBIGUITY` and is a Stage-B problem, not a Stage-A failure.

**Stopping is a successful research outcome when the evidence does not support synthesis.** Completing a polished artifact is never more important than preserving provenance integrity. An agent that stops correctly under this section has done its job; an agent that pushes through to a plausible-looking Rule Card without clearing the relevant gate has not, regardless of how well-written the result reads.

## 18. Relationship to Other Governing Documents

- `GAME_CONSTITUTION.md` and `SOURCE_HIERARCHY.md` remain the authority on *what* the rules hierarchy is and how compatibility/provenance are classified. This protocol governs the *research process* used to apply them faithfully.
- `docs/rules/_template.md` remains the required shape of a finished Rule Card (Stage B's output). This protocol governs what must be true before that template is filled in with confidence.
- `DEVELOPMENT_WORKFLOW.md` §9.7 (revalidation) and §9 generally (decision records) reference this document rather than duplicating it.
- `AGENTS.md` §10 binds agents to this document's hard gates rather than restating them.
- This document does not change `ARCHITECTURE.md`, the Pre-Code Development Gate, the Rules Baseline Migration Gate, `DEC-0007`, or `DEC-0008` in any way.

## 19. Status

Adopted `docs/decisions/DEC-0009-evidence-first-rule-research-protocol.md`, `APPROVED`, 2026-08-16.

**Amendments adopted by `docs/decisions/DEC-0010-primary-source-completeness-audit.md`, `Approved` 2026-08-29 (drafted 2026-08-23)** — §9.1–§9.6 (object/table completeness audit, structure-first ordering, visual verification, coverage checklist, research-risk classification and high-risk triggers, prohibited shortcuts Guardrails A–C, within-source evidence-type guidance), §9.7 (complete-entry inspection), §9.8 ("single governing object" caution), §10.1.1 (adversarial self-review), §10.1.2 (independent completeness review — not by the original researcher), §10.2, §10.2.1 and §10.2.2 (open-question closure gate, reconciliation table, and the genuine-conflict-versus-incompleteness distinction), §10.3 (independent completeness-review method), the object-level precondition note in §15, the corresponding Stage-A sequence steps in §3, and the `STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED`, `STOP — MORE PRIMARY RESEARCH REQUIRED` (closure-gate blockage) and `FAIL COMPLETENESS PREPARATION` hard stops in §17.

**`DEC-0010` is `Approved` and those sections are in force.** `DEC-0009` is not superseded and its protections are unchanged; `DEC-0010` strengthens Stage A only.

**Amendment adopted by `docs/decisions/DEC-0011-alternate-source-lineage-completeness.md`, `Approved` 2026-09-04 (drafted 2026-08-29)** — **§15.1** (multi-unit lineage corpus completeness: **hierarchical** corpus inventory down to core source units, level-range and subject exclusions, duplicate presentations, conflict-precedence scope, lineage-level negative findings, and independent alternate-source completeness review), plus the cross-reference note in §10.1.2. **Amendment adopted by `docs/decisions/DEC-0012-stage-a-evidence-integrity-gates.md`, `Approved` 2026-10-01 (drafted 2026-09-30)** — §5.1 (Research-Start Gate), §9.2.1 (discharging the visual-access gate), §9.3.1 (Coverage Manifest and the required `enumerate → inspect → disposition → falsify → conclude` order), §9.9 (index instruments are completeness instruments — **elevating precedent `P-001`**), §9.10 (prohibited completeness language), §10.1.3 (the independent reviewer's restated role), §10.4 (Negative Claim Gate and the `NOT YET ESTABLISHED` classification), §10.5 (Repository Fact Gate and `UNVERIFIED PROJECT FACT`), §10.6 (pre-review self-falsification pass), §11.1 (Research-Completion Gate and the evidence linter), §11.2 (required Stage-A packet template), two added §6 confidence labels, two added §17 hard stops, and the amended Stage-A sequence in §3 and §9.1.1.

**`DEC-0012` is `Approved` and those sections are IN FORCE.** It was adopted after `CLUSTER-004` Stage A required **five** independent completeness reviews, four of them `FAIL`, for defects that were overwhelmingly evidentiary-closure and bookkeeping failures rather than rules-interpretation failures. It **supersedes `DEC-0010` item 13's Stage-A sequence as amended** and weakens nothing: `DEC-0009`'s protections, `DEC-0010`'s completeness discipline, `DEC-0011`'s lineage discipline, and **§10.1.2's independent-review requirement — named specifically in the approving decision as not weakened** — are all unchanged. `DEC-0010`'s and `DEC-0011`'s historical text is not rewritten.

**Stage-A research is pilot-gated as of that approval.** The blanket Stage-A freeze `DEC-0012` was drafted under is replaced by a **controlled pilot authorization**: exactly one new Stage-A Rule Card, selected by the human project owner, with **no second card** until the pilot has completed its independent-review cycle and received human evaluation. The pilot's four success criteria are fixed at `DEC-0012` Decision item 15 and may not be softened or reinterpreted afterwards — in particular, **if independent review #1 finds a governing object the researcher should have enumerated under this protocol, that counts as evidence the remediation is not yet sufficient.**

**`DEC-0011` is `Approved` and §15.1 is IN FORCE.** It extends `DEC-0010`'s completeness discipline from the primary source to the alternate-source layer; it supersedes neither `DEC-0009` nor `DEC-0010`, and grants alternate sources no additional authority — RC remains primary (`DEC-0007`). This is the default workflow for substantial historical Rule Cards and revalidations going forward. `EXP-001`'s revalidation is the first Rule Card research task expected to follow it in full — expected to produce a committed `docs/rules/evidence/EXP-001-evidence.md` Stage-A artifact, not a rewritten Rule Card, as its first deliverable.
