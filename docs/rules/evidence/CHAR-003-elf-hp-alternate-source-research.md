# Stage-B Gap-Directed Alternate-Source Research: Elf Fixed Hit-Point Gain (`CHAR-003`)

> **Stage-B artifact.** Produced under `RULE_CARD_RESEARCH_PROTOCOL.md` §15 with `DEC-0010`'s structure-first process applied. It is **not** a Rule Card and authorizes nothing.
>
> **Prior BECMI research (pre-2026-08-29) remains `NOT VALID AS CURRENT SYNTHESIS INPUT`** (human ruling). It was not consulted and no conclusion was inherited from it. Nothing below cites it.

---

## 0. Revision history — the first version of this document was WRONG

**Revision 2 — 2026-08-29 (corrected).** **Revision 1's conclusion is withdrawn.**

| | Revision 1 (withdrawn) | Revision 2 (current) |
|---|---|---|
| Volumes inspected | Expert, Companion **only** | Basic, Expert, Companion, Master, Immortals — **all five dispositioned** |
| Claim | *"BECMI is unanimous at +2. No +1 statement located. No internal BECMI conflict."* | **BECMI is NOT unanimous.** Expert/Companion say `+2`; **Master says `+1`** |
| Outcome | **A** — lineage clearly supports `+2`; `+2` proposed for the Rule Card | **C** — lineage does not cleanly disambiguate RC → **`HUMAN RULING REQUIRED`** |

**The withdrawn claim, quoted exactly so it is not softened:**

```text
BECMI is unanimous at +2.
No BECMI statement supporting +1: None located (Finding E4).
Internally conflicting BECMI statements: None.
```

**Why it was invalid.** BECMI is a five-volume lineage — Basic, Expert, Companion, Master, Immortals. Revision 1 inspected two volumes, found them to agree, and declared the *lineage* unanimous. **It never identified the Master Set as a required source object, and never dispositioned it.** The Master Players' Book contains a directly governing Elf hit-point statement that says `+1`, and the Master Set carries an explicit conflict-precedence rule favouring itself over earlier sets. Revision 1's Finding E4 — "no `+1` statement located" — was true only of the volumes it happened to open, and was stated as though it were a property of the lineage.

This is the **same failure class as `DEC-0010`'s founding defect**, relocated from the primary source to the alternate source: treating "the first sources that answer the question" as "the complete relevant corpus." See §10 (postmortem) and §11 (proposed guardrail).

Revision 1's findings that survive are re-verified and retained below with their original identifiers where the evidence is unchanged. Nothing is deleted.

---

## 1. The question, and why the research is authorized

```text
RC establishes:
    Elf Hit Dice are 1d6 per level through 9th level.
    Constitution applies to each rolled die and ceases thereafter.
    A fixed hit-point gain applies at 10th level, the Elf's maximum level.

RC does not establish:
    The VALUE of that gain — RC states it as +1 twice and as +2 twice.

Executable simulation requires it because:
    CHAR-003 cannot compute an Elf's hit points at 10th level without it.
```

**This is not an RC silence. It is an RC self-contradiction**, so an alternate source is being used to *disambiguate* rather than to *complete*. RC remains primary (`DEC-0007`). Object-level RC exhaustion is established: `CLUSTER-002` Stage-A completeness passed independent human review 2026-08-29, and all four RC statements are visually verified.

**RC Stage-A source completeness is not reopened by this correction.** The defect is Stage-B alternate-source incompleteness.

## 2. The RC conflict being disambiguated

| RC location | Object type | Value | Verified |
|---|---|---|---|
| p. 25, Elf stat block "Hit Dice:" line | Stat block | **+1** | Visually |
| p. 25, Elf Class Details prose | Detailed prose | **+2** ("Two additional hit points are gained at 10th level") | Visually |
| p. 129, Maximum Hit Points (Demihumans), Elf row | Table | **+2** (54 + 27 + 2 = 83) | Visually |
| p. 130, Creating High-Level PCs, Step 6 | Procedural list | **+1** | Visually |

Two and two, with one pair contradicting **on the same printed page**.

## 3. Corrected BECMI source inventory — every core volume dispositioned

`SOURCE_HIERARCHY.md` §3 names BECMI as the first alternate source. BECMI is **five** boxed sets. All five are accounted for below; **none is dispositioned on assumption**.

| # | Volume | Level range | Archive identifier | Disposition |
|---|---|---|---|---|
| 1 | **Basic** (Set 1) | 1–3 | `dungeons-dragons-set-1-basic-rules` | **INSPECTED → NOT MATERIALLY RELEVANT.** The Elf entry states only `Hit Dice: 1d6 per level`. **Zero occurrences of "10th level" in the volume.** Verified by inspection, not inferred from its level range |
| 2 | **Expert** (Set 2) | 4–14 | `dungeons-dragons-set-2-expert-rules` | **INSPECTED → GOVERNING.** Elf class entry, p. 18 |
| 3 | **Companion** (Set 3) | 15–25 | `dungeons-dragons-set-3-companion-set` | **INSPECTED → GOVERNING.** Demihuman maximum hit points, DM's Book p. 22 |
| 4 | **Master** (Set 4) | 26–36 | `dungeons-dragons-set-4-master-rules` | **INSPECTED → GOVERNING. Missed entirely by revision 1** |
| 5 | **Immortals** (Set 5) | post-36 | `tsr01017ddimmortalrulesboxedset` | **INSPECTED → NOT MATERIALLY RELEVANT.** **Zero occurrences of "elf"** in the entire volume; every `Hit points:` line belongs to a monster or Immortal stat block. Verified by inspection |

**B/X, Holmes and OD&D remain not consulted.** BECMI sits above them in the hierarchy and is now fully mapped; the disagreement is *inside* BECMI, and a lower-priority edition cannot settle which BECMI branch RC intended.

## 4. Method — structure-first, applied to the alternate source

| Step | What was done |
|---|---|
| **Volume identification** | The five BECMI sets enumerated **first**, from the lineage's own structure, before any volume was opened. This is the step revision 1 omitted |
| Source structure / finding aids | Contents inspected per volume; the governing Elf entry located structurally |
| Governing object inventory | Per volume: Elf class entry, Elf Experience Table, Elf Saving Throw table, Hit Dice/Hit points line, demihuman maximum-HP material, Attack Rank tables |
| **Visual verification** | Every governing object below read as a page image. The Expert OCR for the Dwarf/Elf columns is severely degraded (Cyrillic substitution), which is exactly why §9.2 makes this mandatory |
| Complete-entry inspection (§9.7) | Each Elf entry read as a unit, not as a search window |
| **Duplicate presentations** (§9.1 class I) | Every `Hit points:` / `Hit Dice:` line and every `10th level` occurrence enumerated **per volume**, to find second statements. Expert: one Elf statement. Companion: none in class form, one in the max-HP table. Master: one, and only one |
| **Conflict-precedence statements** | Searched for explicitly — this is a new step revision 1 did not perform. Master p. 2 carries one |
| Negative-finding discipline (Guardrail B) | Every absence below is stated as "not located after inspecting *these* objects", never as a property of the lineage |

**Pages visually verified this revision:** Master Players' Book **p. 2** and **p. 12**; RC **p. 26**. Carried forward from revision 1, re-checked: Expert Players Manual **p. 18**; Companion DM's Book **pp. 22–23**.

## 5. Findings

### Finding E1 (retained) — BECMI **Expert** p. 18, Elf class entry: **+2**

```text
Hit Dice: 1d6 per level, 9d6 maximum; +2 hit points at 10th level.
```

Elf Experience Table: levels **1–10**, ending `10* 10th Level Lord Wizard 600,000`, footnote *"Constitution adjustments no longer apply."* Spells/Level columns **1–6**, level 10 = **3 3 3 3 2 —**.

Adjacent Dwarf entry: `Hit Dice: 1d8 per level, 9d8 maximum; +3 hit points per level thereafter.`

### Finding E2 (retained) — BECMI **Companion** DM's Book p. 22: **+2**

| | Dice Rolls | Con. Bonus | L 10-12 | Maximum Total |
|---|---|---|---|---|
| Dwarf | 72 | 27 | +9 | 108 |
| **Elf** | **54** | **27** | **+2** | **83** |
| Halfling | 48 | 24 | - | 72 |

Every number is identical to RC p. 129, including the shared `L 10-12` column header and the explanatory note. The Companion contains **no** Elf class-entry hit-point line — this table is its only Elf HP statement.

### Finding E3 (retained) — BECMI Companion p. 23: Elf Attack Ranks C–M at 600k–3,100k XP

Matches RC p. 26's continuation. Bears on descent, **not** on the HP value.

### Finding E6 (NEW, decisive) — BECMI **Master** Players' Book p. 12, Elf class entry: **`+1`**

Visually verified, printed beneath the Elf Experience Table:

```text
Hit points: 1d6 per level through 9th level, modified by Constitution
if applicable. Add 1 hp at 10th level, with no Constitution effect.
```

On the same page, for contrast:

- **Dwarf:** *"1d8 per level through 9th level… Thereafter, add 3 hp per level, with no Constitution effect."* — **unchanged** from Expert's `+3`.
- **Halfling:** *"1d6 per level throughout, modified by Constitution if applicable."* — no fixed gain, consistent.

**Master's Elf Experience Table is also materially revised.** Spells columns **1–5**, level 10 = **5 4 3 2 1** — against Expert's six columns and level 10 = **3 3 3 3 2**. Master changed the Elf's spell progression *and* its 10th-level hit points in the same table. **This is a deliberate revision, not a transcription slip.**

**Exactly one** Elf hit-point statement exists in the Master Set. No internal Master conflict.

### Finding E7 (NEW) — Master carries an explicit conflict-precedence rule

Visually verified, Master Players' Book **p. 2**, "The Ultimate Game":

```text
These rules are written to maintain balanced play at high level.
If you discover a contradiction between this set and previous sets,
the rules given here should be used.
```

The same page states the set *"can only be used with the rules from the previous three sets"* and that the series runs Basic (1–3) → Expert (4–14) → Companion (15–25) → Master (26–36).

**This is recorded as a source fact. It is not applied to RC — see §7.3.**

### Finding E8 (NEW, incidental but relevant to `CHAR-001`) — the Mystic is not a BECMI core class

Master p. 2 describes, among the Dungeon Master's Book contents: *"Suggestions are given for converting a new monster, the mystic, into a character class if the DM desires."* The Mystic enters BECMI as an optional DM conversion, not as a core class. **Consequence: BECMI cannot resolve a Mystic-specific rules question** — see `CHAR-001` U3.

### Finding E4 — **WITHDRAWN**

Revision 1's *"no BECMI statement supporting +1 was located"* is **false**. Finding E6 is that statement. The claim was made after inspecting two of five volumes.

### Finding E5 (retained, but its force is reduced)

RC preserves BECMI's fixed gain unchanged for Cleric (+1), Fighter (+2), Magic-user (+1) and Dwarf (+3). Revision 1 used this to argue the Elf `+1` must be an anomaly. **It no longer supports that inference**: for those four classes Expert and Master agree, so "RC matches BECMI" does not discriminate between branches. The Elf is the one class where the two BECMI branches disagree — which is precisely why RC is inconsistent about it and consistent about the others.

## 6. Corrected lineage table

| Source | Object | Fixed HP rule | Visual verification | Relationship to earlier source |
|---|---|---|---|---|
| Basic (Set 1) | Elf entry | *none stated* | OCR inspection; no `10th level` in volume | **NOT COMPARABLE** — out of level range |
| **Expert (Set 2)** | Elf class entry, p. 18 | **+2 at 10th level** | **Yes** | Originating statement |
| **Companion (Set 3)** | Demihuman max HP, DM p. 22 | **+2** (total 83) | **Yes** | **PRESERVED** from Expert |
| **Master (Set 4)** | Elf class entry, p. 12 | **+1 at 10th level** | **Yes** | **REVISED** — and the same table also revises Elf spell progression |
| Master (Set 4) | Introduction, p. 2 | *precedence rule* | **Yes** | **SUPERSEDING** as to BECMI-internal contradictions |
| Immortals (Set 5) | — | *none* | OCR inspection; no `elf` in volume | **NOT COMPARABLE** |

```text
BECMI lineage:  NOT UNANIMOUS
                +2 (Expert, Companion)  →  REVISED to  +1 (Master)
```

## 7. Rule evolution and textual genealogy

### 7.1 Source facts

1. Expert (1983) states **+2**; Companion (1984) preserves **+2**; Master (1985) states **+1** and revises the Elf Experience Table's spell progression in the same object.
2. Master p. 2 instructs that its rules govern contradictions with previous sets.
3. **RC p. 26's Elf Experience Table matches EXPERT, not Master.** Visually verified this revision: RC's level-10 spell row is **3 3 3 3 2**, identical to Expert; Master's is **5 4 3 2 1**. RC simply drops Expert's all-dashes sixth column.
4. RC p. 129's demihuman maximum-HP table matches **Companion** p. 22 number for number, including header and note, and its `83` is consistent only with `+2`.
5. RC p. 25's stat block reads *"10th level, +1 hit point, and Constitution adjustment does not apply"* — closely tracking **Master**'s *"Add 1 hp at 10th level, with no Constitution effect."*
6. RC p. 25's Class Details prose reads *"Two additional hit points are gained at 10th level"* — closely tracking **Expert**'s *"+2 hit points at 10th level."*
7. RC p. 130 Step 6 lists the Elf at **+1**, consistent with Master.

### 7.2 Editorial inference

**RC is a composite that inherited from both BECMI branches and never reconciled them.**

```text
Expert branch (+2)   →  RC p.25 Class Details prose
                     →  RC p.26 Elf Experience Table (spell progression)
Companion branch(+2) →  RC p.129 Maximum Hit Points (Demihumans)
Master branch (+1)   →  RC p.25 Elf stat block
                     →  RC p.130 Step 6 per-class list
```

This is a **well-supported** inference — it explains all four RC statements, the same-page contradiction, and why RC is consistent for every other class. **But it is an inference, not source text**, and it is explanatory rather than dispositive: knowing *how* RC became inconsistent does not establish *which* value RC intends.

**It specifically does not license choosing `+1`.** Fact 3 is the decisive complication: RC's Elf Experience Table — the very object whose omission caused `DEC-0010` — descends from the **Expert** (`+2`) branch, not Master's. RC therefore did **not** wholesale adopt Master's revised Elf. Any argument that "RC follows Master" has to explain why RC reprinted Expert's spell progression instead of Master's.

### 7.3 Why Master's precedence rule does not settle it

Finding E7 is a **BECMI-internal** instruction: it tells a reader using the four boxed sets together which to prefer. RC is a different, later product that consolidates and supersedes the boxed-set line as a whole; it does not incorporate Master's precedence instruction by reference, and `SOURCE_HIERARCHY.md` gives no basis for importing an alternate source's meta-rule into the interpretation of the primary source.

Treating "Master is later, and Master says its rules win" as decisive for **RC** would be an unauthorized inference of exactly the kind this protocol exists to prevent — and it would be the mirror image of revision 1's error, reaching a confident answer from a partial reading of how the sources relate.

The precedence rule **is** a genuine argument available to the human adjudicator, and it is recorded here for that purpose.

## 8. Outcome — corrected

Revision 1's **Outcome A is withdrawn.** The corrected outcome is **C — inconclusive**.

```text
RC:                        internally conflicting (2 vs 2)
BECMI:                     also conflicting — REVISED across sets
                           +2 (Expert, Companion) → +1 (Master)
Alternate-source research: DOES NOT cleanly disambiguate RC

DISPOSITION:               HUMAN RULING REQUIRED
```

**No value is written into `CHAR-003` as a settled lineage resolution.** Neither `+2` nor `+1` is selected. The card carries `UNRESOLVED — HUMAN RULING REQUIRED`.

### The evidence for each choice, stated for the adjudicator

| For **`+2`** | For **`+1`** |
|---|---|
| RC p. 25 Class Details prose and RC p. 129 table both say it | RC p. 25 stat block and RC p. 130 Step 6 both say it |
| RC p. 129's total `83` is arithmetically consistent only with `+2`, and that total is itself inherited from Companion | Master is the **latest** BECMI statement and deliberately revised the Elf, changing spell progression in the same table |
| **RC p. 26's Elf Experience Table descends from the Expert (+2) branch** — RC did not adopt Master's revised Elf table | Master p. 2 explicitly instructs that its rules govern contradictions with earlier sets |
| The originating statement, preserved across two sets | RC's stat-block wording tracks Master's phrasing closely |

Both columns rest on visually verified source objects. **Neither is obviously stronger, which is why this is the human's call and not the researcher's.**

## 9. What this research does NOT establish

- It does **not** reopen RC Stage-A source completeness (`INDEPENDENT REVIEW — PASS`, 2026-08-29).
- It does **not** reopen the Elf maximum level (10) or the Druid maximum level (36) — both human-adjudicated, both unaffected.
- It does **not** license importing any other BECMI mechanic. Nothing encountered incidentally — strongholds, Clans, Combat Options, breath-weapon resistance, Weapon Mastery, Siege Warfare — is imported.
- It does **not** bear on the Chapter 19 extended demihuman/Mystic progression variant, `NOT ENABLED` for V1.
- It does **not** establish halfling or thief fixed gains; not the question, not researched.

## 10. Postmortem — how the alternate-source research failed

Reported from the observable research trail, not from reconstruction of reasoning.

**1. Why did the research stop after Expert and Companion?**
Because both answered the question, and they agreed. The Expert Elf entry gave a direct `+2`; the Companion max-HP table gave a corroborating `+2` **and** a verbatim genealogical link to RC p. 129. Two independent objects in two volumes agreeing produced a subjectively strong result, and the search stopped at the point of apparent confirmation rather than at the point of coverage.

**2. Why was Master not identified as a required lineage source?**
Because volume selection was driven by **where the answer was expected**, not by **what the lineage contains**. The documented reasoning was: the Elf caps at level 10, level 10 falls in the Expert Set's 4–14 range, therefore Expert is the governing volume; the Companion was added because it owns demihuman post-maximum progression. Master was filed as "levels 26–36" — a range no Elf reaches — and was never tested against the actual question. That reasoning is wrong: a later volume can **restate and revise** an earlier class entry, and Master p. 12 does exactly that, reprinting the whole Elf entry.

**3. What evidence led to the word "unanimous"?**
Two positive statements and one negative search. Revision 1's Finding E4 recorded that no `+1` statement was located "after inspecting the complete Elf entry, every `Hit Dice:` line and every `10th level` occurrence in the Expert Players Manual, and the Companion's demihuman material." That scope statement was accurate. The error was applying a **volume-scoped** negative result to the **lineage** — the precise move Guardrail B prohibits, committed one level up. Revision 1 even wrote the Guardrail B caveat and then used the word "unanimous" three sentences later.

**4. Was there an explicit alternate-source completeness checklist?**
**No.** `DEC-0010` §9.3 requires a Primary-Source Coverage Checklist. Nothing equivalent exists for alternate sources, and none was constructed. Revision 1 applied §9.1's *object*-level discipline **within** each volume it opened — TOC, governing entry, tables, visual verification, duplicate presentations — and applied **no** discipline at all to the choice of which volumes to open. That is the gap.

**5. Did the research mistake "closest source that answers the question" for "complete relevant lineage"?**
**Yes. That is exactly the error, and it is the whole of it.** `SOURCE_HIERARCHY.md` §15's "highest-priority, most directly relevant compatible treatment" was read as licensing a stop once a directly relevant treatment was found. It does not: relevance selects *which* sources to consult, it does not certify that consultation is complete. Revision 1 then compounded this by recording the decision **not** to consult B/X, Holmes and OD&D as a deliberate, reasoned scope boundary — creating the appearance of considered completeness while an unexamined volume of the *same, higher-priority* source sat undispositioned.

**6. How should `DEC-0010`'s completeness principles apply to multi-volume alternate-source research?**
Identically, one level up. `DEC-0010` §9.1 requires enumerating governing **objects** before claiming a source was covered. A multi-volume lineage has an enumerable structure above the object level — its **volumes** — and the same rule applies: enumerate and disposition every materially relevant volume before any claim about the lineage. Concretely: the volume list is a finding aid in §9.1's sense (class A/B); "no such statement exists in the lineage" is a source-property claim requiring §9.5 Guardrail B treatment; and a later volume that restates an earlier class entry is a **duplicate presentation** under §9.1 class I, which already says to record each separately and treat none as automatically authoritative.

**What actually caught it.** Not the process — a human reviewer. The adversarial self-review in revision 1 restarted from *the objects within the volumes already chosen*, so it could not surface a volume that was never on the list. A self-review that inherits the original scope reproduces the original blind spot; that is the same lesson `DEC-0010` §10.1.2 already drew for primary sources.

## 11. Proposed guardrail — NOT adopted

Offered for human review, deliberately minimal. **No new decision record is proposed** — `DEC-0010` already governs source completeness, and this is a scope extension of its existing principle rather than a new one. If adopted, the natural home is a short subsection of `RULE_CARD_RESEARCH_PROTOCOL.md` §15 (Alternate Sources Are Gap-Directed Only).

> **§15.1 — Multi-volume lineage completeness (proposed).**
>
> Where alternate-source research relies on a named multi-volume rules lineage, the researcher must **enumerate every core volume of that lineage and disposition each one** — inspected, or excluded with a stated reason — **before** claiming the lineage is exhaustive, unanimous, internally consistent, or silent. A volume may be excluded on scope grounds only where that scope is verified, not assumed.
>
> A negative finding about a lineage is a source-property claim and is governed by Guardrail B (§9.5): *"not located in the volumes inspected"* is permitted; *"the lineage contains no such rule"* requires that every materially relevant volume has been dispositioned.
>
> **A later volume that restates or revises an earlier volume's governing entry is a duplicate presentation** (§9.1 class I) and must be inspected, not skipped on the basis that its nominal level range or subject matter appears not to reach the question.
>
> **Where a later volume contains an explicit conflict-precedence rule, that rule is a mandatory source object** when resolving earlier/later disagreement within the lineage — and its scope must be stated: a lineage-internal precedence rule governs that lineage, and does **not** by itself determine what a later consolidating product intends.

**Rationale for the last clause:** without it, this correction's own finding could be misread as "Master wins, therefore `+1`", which would substitute one unauthorized inference for another.
