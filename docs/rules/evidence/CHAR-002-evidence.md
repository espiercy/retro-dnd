# Stage-A Evidence: CHAR-002 — Race & Class Eligibility

> **⚠ Open-question closure (2026-08-23) — §9 item 2 is now ANSWERED, and the answer is "no" for Druid.**
>
> This packet recorded as an open question: *"Whether 'Other Requirements' is exhaustive for druid/mystic… Druid and mystic entries were not read in full in this pass."* A first remediation pass then certified `CHAR-002` complete and called the p. 7 table its **"single governing object"** while that question was still open. **That certification and that phrase are both withdrawn** — see `docs/rules/evidence/CLUSTER-002-completeness-audit.md` §5.1a.
>
> Both entries have now been read as complete source units (RC pp. 28–31, visually verified):
>
> - **Druid — p. 7 is NOT exhaustive.** The entry adds a **9th-to-29th-level upper bound** on the originating cleric (p. 7 gives no upper bound), a requirement to **find and live in a woodland home**, a **1d4-month meditation** period rolled by the DM, and **being found, tested for worthiness, and taught** by a higher-level druid (usually 25th+), followed by admission to the realm of the druids — plus ongoing alignment and residence maintenance. **Proposed owner: `CHAR-013`** (later class-transition procedure), with `CHAR-008` and `ADV-002` dependencies. **Proposed, not adopted; `CLUSTER-002` is not expanded.**
> - **Druid — new Category D conflict.** Ch. 1 p. 12 says Druids may only achieve **30th** level; the stat block, Higher Experience Levels, the **Druid Experience Table (levels 9–36)** and the Druid Saving Throws Table (bands to 33-36) all say **36**. **Unruled**; owner `ADV-002`.
> - **Mystic — p. 7 IS complete for creation eligibility.** Wisdom 13 / Dexterity 13 restated verbatim at p. 29. Additional entry material (Strength-only XP-bonus disambiguation, armor/protective-magic prohibition, tithe-and-donate XP condition, oath sanction, 75%-Lawful tendency) is all **downstream**, none of it creation eligibility.
>
> **This packet's executable eligibility conclusions are unchanged.** Procedure A already returns *not eligible at creation* for Druid; the Druid Experience Table starting at level 9 **strengthens** that. §9 item 2 is closed; §9 item 1 (Ch. 13 switch vs. demihuman minimum) is **retained as a genuine source ambiguity**.
>
> **This is a Stage-A evidence artifact, not a Rule Card.** Produced under `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` (`DEC-0009`). It is not mechanically authoritative, is not `APPROVED`, and authorizes nothing. Stage B was **not** begun.

> **Independent completeness review — PASS (human, 2026-08-29).** The human project owner completed the independent primary-source completeness review required by `DEC-0010` item 14 / protocol §10.1.2 and returned **`CHAR-002: source coverage PASS`**. The prior source-completeness defect recorded above — the withdrawn self-certification over an open Druid/Mystic question — is **remediated**.
>
> **Human Evidence Review — `ACCEPTED` (human, 2026-08-29).** With `DEC-0010` `Approved` and landed, this packet's clearance is **restored**. Stage B is **unpaused — eligible, not begun**; it proceeds only under a separate assignment. The suspension is preserved in the clearance history at `docs/rules/clusters/CLUSTER-002-character-foundation.md` §3.
>
> **Druid maximum level — human adjudication (2026-08-29).** The Category D conflict raised above is confirmed genuine and is now adjudicated:
>
> ```text
> Standard RC Druid progression:   levels 9–36
> Maximum Druid level:             36
> Special challenge / limited-rank progression:
>                                  begins with advancement to 30th level
> RC Ch. 1 p. 12 ("Druids may only achieve 30th level"):
>                                  treated as erroneous summary text
> ```
>
> **Source of truth: the detailed Druid class progression material and the Druid Experience Table (RC pp. 28–29).** This is a **human adjudication**, not an agent-derived resolution, and no alternate-source research is needed or permitted for it. **Ownership is downstream (`ADV-002`), recorded in `docs/rules/INVENTORY.md` "Human-adjudicated class level caps"; `CLUSTER-002` is not expanded and this packet's executable eligibility conclusions are unchanged** — Procedure A already returns *not eligible at creation*, which a progression table beginning at level 9 strengthens.

## 1. Research Scope

**Investigating:** what the Rules Cyclopedia requires when determining which race/class options are available to a newly generated character — the choices that exist, whether ability scores restrict eligibility, whether prime requisites gate eligibility or something else, whether race and class are unified or separate concepts, and what prerequisites are genuinely required versus merely referenced.

**Mandatory open question this task must answer at the evidence level** (`docs/rules/clusters/CLUSTER-002-character-foundation.md` §8, question 2): *does RC race/class eligibility depend on ability-score minimums, prime-requisite thresholds, or other authoritative values supplied by the general ability-score-effects responsibility (`CHAR-007`)?*

**Excluded:** class special abilities, spell lists, level progression, saving-throw tables, weapon/armor permissions — referenced only where they mark this card's boundary.

## 2. Primary-Source Access

As recorded in `CHAR-001-evidence.md` §2 (same source, same access method, same session): *Dungeons & Dragons Rules Cyclopedia* (TSR, 1991) full OCR transcription via `archive.org/stream/TSR1071TheDDRulesCyclopedia/TSR-1071-The-DD-Rules-Cyclopedia_djvu.txt`, loaded in-browser and searched by in-page full-text search, with surrounding context read in full.

No access failure occurred. `STOP — PRIMARY SOURCE ACCESS REQUIRED` was **not** triggered.

## 3. Research Questions

A. What race/class choices exist for a new PC?
B. Are race and class unified or separate concepts?
C. Do ability scores restrict eligibility — and if so, raw scores or adjustments?
D. What do prime requisites actually govern?
E. What non-ability prerequisites exist?
F. What is merely referenced (downstream) rather than required by this card?

## 4. Evidence Map

| Question | RC Location | What RC Establishes | Provenance | Confidence |
|---|---|---|---|---|
| A. Available classes | Ch. 1, "Choose a Character Class," pp. 6–7 | Nine PC classes, grouped by RC into four human (cleric, fighter, magic-user, thief), three demihuman (dwarf, elf, halfling), and two special/optional (druid, mystic). | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| B. Race/class unification | Ch. 1, p. 6 | For demihumans, race **is** the class: RC states demihumans are more limited in options than humans, so the entire race is represented by a single character class. There is no separate race-selection step for demihumans. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| C. Human classes — no ability gate | Ch. 1, p. 6 | Any new character may belong to one of the four human classes **regardless of his ability scores**. Stated as an explicit universal. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| C. Demihuman/special classes — ability minimums | **Character Classes and Ability Requirements Table, p. 7** (also restated per class in Ch. 1 prose and in the Ch. 2 class entries) | Minimum **raw ability scores** gate the non-human classes: Dwarf requires Constitution 9; Elf requires Intelligence 9; Halfling requires Dexterity 9 and Constitution 9; Mystic requires Wisdom 13 and Dexterity 13. Cleric, Fighter, Magic-User and Thief have no listed ability requirement. | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED (table, Ch. 1 prose, Ch. 2 class entries) |
| C. **The gate is the raw score, not the adjustment** | Same table and prose, p. 6–7 | RC expresses every requirement as a score threshold — e.g. a dwarf character must have a Constitution score of 9 or more, and a character with Constitution 8 or less cannot be a dwarf. No eligibility requirement anywhere is expressed as a bonus/penalty value from the `CHAR-007` adjustment table. | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED |
| D. What prime requisites govern | Ch. 1, "Prime Requisites," p. 6; Character Classes and Ability Requirements Table, p. 7; **Experience Bonuses and Penalties Table, p. 12** | The prime requisite is the ability of greatest importance to a class, named per class. Mechanically it governs (i) eligibility to *raise* a score in the Ch. 1 point-trade, and (ii) an **experience-point bonus or penalty**. It is **not** itself an eligibility threshold: no class is gated on a minimum prime-requisite value. (Mystic's Wisdom 13 / Dexterity 13 are listed under "Other Requirements," and Wisdom is not a Mystic prime requisite.) | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED |
| E. Non-ability prerequisites | Character Classes and Ability Requirements Table, p. 7 | Druid requires Neutral alignment **and** attainment of 9th level as a cleric — the only class whose requirements reach outside ability scores. Dwarf/elf/halfling/mystic requirements are ability-score minimums only. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E. Druid is not a 1st-level entry point | Same table; Ch. 1 Hit Dice table, p. 8 | Consistent with the 9th-level-cleric prerequisite, the Character Class and Hit Dice Table marks the Druid's starting Hit Die as not applicable. Druid is therefore not reachable at character creation. | Rules Cyclopedia Explicit (both facts) / Necessary Mechanical Consequence (that it is unreachable at creation) | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED |
| F. Optionality of druid/mystic | Ch. 1, p. 7; TOC ("Druid (Optional)," "Mystic (Optional)," pp. 28–29) | RC sets druid and mystic aside as classes a DM may decline to use in his campaign. Both are nonetheless project-selected as REQUIRED V1 content by `DEC-0008` — a project configuration decision, not an RC finding, and not revisited here. | Rules Cyclopedia Explicit (RC's own optional framing) | DIRECT PRIMARY TEXT |
| C/F. Class choice precedes score adjustment | Ch. 1, pp. 6–7 | RC states the class must be decided **before** the ability-score point-trade, because the trade may only raise the prime requisite. Eligibility is therefore evaluated against **as-rolled** scores, before any trade. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |

## 5. Mandatory Open Question — Answered at the Evidence Level

**Question:** Does RC race/class eligibility depend on ability-score minimums, prime-requisite thresholds, or values supplied by `CHAR-007`'s general ability-score-effects responsibility?

**Evidence-supported answer, in three parts:**

1. **Ability-score minimums: YES.** Four of the nine classes are gated on minimum ability scores (Character Classes and Ability Requirements Table, p. 7).
2. **Prime-requisite thresholds: NO.** No class is gated on a prime-requisite minimum. Prime requisites govern the point-trade and an XP bonus/penalty (p. 12), both of which are distinct from eligibility.
3. **`CHAR-007`-supplied values: NO — on the evidence located.** Every eligibility requirement RC states is a **raw score threshold**, not an adjustment value. `CHAR-007` owns the mapping from score to bonus/penalty; that mapping is never the eligibility criterion. `CHAR-002` therefore appears to depend on `CHAR-001`'s raw scores, not on `CHAR-007`'s effects table.

**Consequence for repository metadata:** this evidence **supports** the current `INVENTORY.md` dependency row for `CHAR-002` (`CHAR-001` only) and gives no basis for adding a `CHAR-007` dependency. **No metadata was changed** (task §14).

**Caveat preserved:** this is a negative finding across the eligibility requirements located. It is stated as "no eligibility requirement expressed in adjustment terms was found," not as proof that none exists.

## 6. Research Questions Belonging to Other Rule Cards

- Prime-requisite XP bonus/penalty magnitudes (Experience Bonuses and Penalties Table, p. 12) → `ADV-001`/`ADV-002`. Located here only to establish that prime requisites are *not* an eligibility gate.
- Alignment as a system, and the Neutral requirement's meaning → `CHAR-008` (Druid's prerequisite creates a genuine cross-reference).
- Attaining 9th level as a cleric → `ADV-002`.
- Class special abilities, weapons/armor permissions, spell access, saving throws, level caps → `CHAR-009`, `CHAR-010`, `COMBAT-*`, `MAGIC-*`, `ADV-002`.
- Hit Dice by class → `CHAR-003` (see `CHAR-003-evidence.md`).

## 7. Whole-Source Cross-Reference Pass

**Search terms used:** `Choose a Character Class`; `Character Classes and Ability Requirements`; `prime requisite` (56 occurrences reviewed); `Prime Requisites`; `Other Requirements`; `Constitution 9`; `Intelligence 9`; `Dexterity 9`; `Wisdom 13`; `demihuman`; `Maximum Level`; `maximum level` (8 hits reviewed); `Experience Bonus`; `Attack Rank`; `9th level as a cleric`; `Druid (Optional)`; `Mystic (Optional)`.

**Sections inspected:** TOC; Tables index; Ch. 1 pp. 6–12 in full; Ch. 2 class entries (cleric, fighter, magic-user, thief, dwarf, elf, halfling) including their Requirements/Prime Requisite/Hit Dice/Maximum Level lines; Ch. 10 pp. 127–129; Ch. 13 "Creating Characters" p. 145; Ch. 19 p. 266.

**Cross-references discovered:**
- Ch. 1 p. 7 table ↔ Ch. 2 per-class "Requirements" lines — independently consistent for the ability minimums checked.
- Ch. 1 p. 6 → forward reference to Chapter 2 for choosing a class.
- **Ch. 13 p. 145 → a DM may permit score-switching so a player can qualify for/suit a desired class** — a genuine eligibility-adjacent provision outside Chapter 1 (shared finding with `CHAR-001-evidence.md`).
- Druid → alignment (`CHAR-008`) and 9th-level-cleric (`ADV-002`) prerequisites.
- Demihuman "Attack Rank" columns → post-maximum-level advancement (`ADV-002`), not eligibility.

**Negative results:** no ability-score *maximum* gating any class was located; no racial requirement expressed in adjustment/bonus terms was located; no Chapter 19 variant altering class eligibility was located (Ch. 19's three named sections do not address eligibility).

## 8. Falsification Pass

**Challenge 1 — "Ability scores restrict class choice."**
*Sought:* whether this is true generally or only for some classes. *Searched:* the p. 7 table in full, all Ch. 2 class Requirements lines, `regardless of his ability scores`.
*Found:* RC explicitly exempts all four human classes.
**Disposition: QUALIFIED.** True only for demihuman and special classes; explicitly false for human classes.

**Challenge 2 — "Prime requisite is an eligibility threshold."**
*Sought:* any minimum prime-requisite value gating class entry. *Searched:* `prime requisite` (all 56 hits scanned by context), the p. 7 table's "Other Requirements" column, `Experience Bonus`.
*Found:* prime requisites appear as (a) the trade's raise-target, (b) an XP modifier. Mystic's stated requirements (Wisdom 13, Dexterity 13) sit in the "Other Requirements" column, and Wisdom is not a Mystic prime requisite — so even the highest thresholds in the table are not prime-requisite gates.
**Disposition: REJECTED.** Prime requisites do not gate eligibility. This is the specific misreading the mandatory open question was posed to test, and the evidence does not support it.

**Challenge 3 — "Eligibility might be evaluated against adjusted (post-trade) scores."**
*Sought:* RC's stated ordering. *Searched:* Ch. 1 pp. 6–7 read in sequence; `Adjust Ability Scores`.
*Found:* RC requires the class to be chosen before the trade, and the trade may only raise the prime requisite — so a trade cannot be used to reach a demihuman minimum in a non-prime-requisite ability (e.g. a dwarf's Constitution 9, since Constitution may not be exchanged at all).
**Disposition: CONFIRMED.** Eligibility is evaluated on as-rolled scores.

**Challenge 4 — "Race and class are separate choices."**
*Sought:* any separate race-selection step. *Searched:* `demihuman`, Ch. 1 pp. 6–7, Ch. 2 entries.
*Found:* RC unifies them for demihumans and describes humans by class alone.
**Disposition: REJECTED as stated.** RC presents a single class choice, not two orthogonal selections.

## 9. Unresolved RC Questions

1. **Whether the Ch. 13 p. 145 score-switching provision may be used to satisfy a demihuman ability minimum**, or only to favour a prime requisite. RC's wording at that location speaks of switching the highest rolled score into the desired class's prime requisite; it does not address minimum-requirement abilities, and dwarf/halfling requirements are in Constitution — an ability the Ch. 1 trade explicitly cannot touch. The two provisions are stated in different chapters with no cross-reference.
2. **Whether a character failing every demihuman/special requirement has any constrained outcome at all**, beyond the human classes being universally available. (RC's universal human availability appears to make this moot, but RC does not say so explicitly.)
3. **Whether "Other Requirements" is exhaustive** for druid/mystic, or whether the Ch. 2 class entries add further entry conditions not reflected in the p. 7 table. Druid and mystic entries were not read in full in this pass.

`POTENTIAL COMPLETION QUESTION — NOT YET RESEARCHED` applies to item 1. No alternate-source research was performed.

## 10. Alternate-Source Research Requirement

**Not established as required.** RC supplies an explicit, tabulated eligibility rule for every class. Item §9.1 is an interaction question between two RC provisions, which is a reconciliation/Stage-B matter before it is a gap.

## 11. Possible Simulator Ruling Areas (named, not drafted)

- The interaction in §9.1, if RC and compatible sources leave it open.

Not drafted or proposed.

## 12. Legacy Rule Card Withholding

**Not applicable** — no prior `CHAR-002` Rule Card exists in this repository; none was consulted.

## 13. Confidence Assessment

**High.** The governing rule is a single explicit table (p. 7), independently corroborated by Chapter 1 prose and by the Chapter 2 per-class Requirements lines, with the human-class exemption stated in unambiguous universal terms. The mandatory open question is answered by direct primary text rather than by inference.

**Moderate** only for §9.3 (druid/mystic entries not exhaustively read).

## 14. Recommendation

```text
EVIDENCE READY FOR HUMAN REVIEW
```
