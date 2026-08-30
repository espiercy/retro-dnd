# Primary-Source Completeness Audit: CLUSTER-002 Stage A (CHAR-001, CHAR-002, CHAR-003, CHAR-007)

> **Retrospective audit artifact** produced under `docs/decisions/DEC-0010-primary-source-completeness-audit.md` and `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` §9.1–§9.4, §10.1.
>
> This audit is the direct consequence of the process defect recorded in `DEC-0010`. It is **not** a synthesis, **not** Stage B, and **not** authorization to change any mechanic. No Rule Card exists for any `CHAR-*` entry and none was created.
>
> **Status of the four Stage-A packets during this audit:** `PREVIOUSLY ACCEPTED — COMPLETENESS AUDIT PENDING`. Human Evidence Review clearance for `CLUSTER-002` is suspended; Stage B is paused.
>
> **Current status (updated 2026-08-29):** the human project owner completed the independent completeness review and returned `CLUSTER-002 STAGE-A PRIMARY-SOURCE COMPLETENESS: INDEPENDENT REVIEW — PASS` for all four cards — see **§7.1**. The Druid maximum-level conflict raised as Finding 11 was **human-adjudicated at 36** — see **§5.2**. With `DEC-0010` approved and landed on 2026-08-29, the **Human Evidence Review clearance is restored** (all four packets `ACCEPTED`) and **Stage B is unpaused — eligible, not begun.** The line above is preserved as the state that obtained while the audit was performed; it is not the current state.

## 1. Method

The object inventory was rebuilt **independently from the Rules Cyclopedia**, starting from its Table of Contents and Tables Index — not from the four accepted evidence packets. Page images were read at full scan resolution (`archive.org/download/TSR1071TheDDRulesCyclopedia/page/n{leaf}.jpg`, leaf = printed page − 1).

`STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED` was **not** triggered.

## 2. The Triggering Defect — RC p. 26 Elf Experience Table

### What the object actually says

**Elf Experience Table (RC p. 26), visually verified.** Columns: Level | XP | Attack Rank | Spells/Level (1–5).

Levels 1–10 are enumerated, ending at **level 10 / 600,000 XP / Attack Rank C**. Below that row the **Level column is empty**: the remaining rows list only XP thresholds (850,000; 1,100,000; 1,350,000; 1,600,000; 1,850,000; 2,100,000; 2,350,000; 2,600,000; 2,850,000; 3,100,000) mapped to **Attack Ranks D through M**.

Immediately beneath it, the **Elf Saving Throws Table** (p. 26) uses level bands **1-3 / 4-6 / 7-9 / 10** — capping identically.

**This is the mechanically authoritative statement of Elf progression: levels 1–10, then Attack Ranks.** It was never inspected during Stage A, while the Stage-A packet escalated the Elf level cap as an unreconciled internal source conflict.

### Why the prior process missed it

Four independent causes, each of which the amended protocol now blocks:

1. **The OCR text stream does not contain the table.** The elf region runs stat block → prose → Special Abilities → Higher Experience Levels → Halfling, with the table's rows absent entirely. No search over that text could have found it.
2. **The search pattern presumed a Hit Dice column.** The researcher searched `9d6 + 1` / `9d6 + 2`. The Elf Experience Table has **no Hit Dice column**. Even had OCR preserved it, that query could not have matched.
3. **A failed search was converted into a positive finding of absence.** All eleven `9d6 + N` hits belonged to the Lich monster entry (Ch. 14); the researcher reported that this "closes the internal RC options." It closed nothing — it established only that one query matched nothing relevant.
4. **The Tables Index pointer was held and not followed.** `Elf Experience Table . 26` was present in the researcher's own working notes and was used to source page citations for *other* tables. It was never opened.

A fifth, compounding consequence: believing RC exhausted, the researcher escalated to BECMI. `SOURCE_HIERARCHY.md` §3 and `RULE_CARD_RESEARCH_PROTOCOL.md` §15 permit that only once a genuine RC gap is documented. **The precondition was manufactured by cause 3.** That alternate-source work is therefore void as to its authorization, independent of what it found.

### How the amended process catches it

| Amended requirement | Where it intercepts |
|---|---|
| §9.1 class B — inspect every Tables Index entry bearing on the mechanic | `Elf Experience Table . 26` is enumerated and must be dispositioned |
| §9.1 class C — inspect every relevant named table directly | The table must be opened, not searched for |
| §9.1 "a failed search is not evidence of absence" | "Closes the internal RC options" is not a permissible finding |
| §9.2 visual verification | A progression table governing numbers must be read as an image |
| §9.4 high-risk classification | Class progression is named high-risk; verification is mandatory |
| §10.1 independent completeness pass starting from the Tables Index | Second, structurally different chance to catch it |
| §9.1 alternate-source precondition | BECMI escalation blocked until the audit is done |

### Human adjudication recorded

Per human ruling, 2026-08-23:

```text
Elf progression:       levels 1–10, then Attack Ranks
Elf maximum class level: 10
RC Ch. 1 p. 12 statement implying Elf level 12:
    treated as erroneous/inconsistent summary text for this project
```

Recorded here as a governance fact. The level-cap question is **not reopened** by this audit, and this ruling triggers no Rule Card or implementation change in this task. Its downstream home is `ADV-002`, whose research is not authorized here.

### What this does *not* resolve

The **Elf fixed-HP `+1` versus `+2` contradiction remains unresolved and is deliberately left so.** The p. 26 table carries no Hit Dice column and contributes nothing to it. See §4, Finding 3.

## 3. Primary-Source Object Inventory

Built from the TOC and Tables Index. **VV** = visually verified as a page image in this audit.

### CHAR-001 — Ability Score Generation

| Object | Class | Location | Status |
|---|---|---|---|
| "Roll for Ability Scores" | F | p. 6 | Prior packet; text-only |
| "Prime Requisites" | F | p. 6 | Prior packet; text-only |
| "Choose a Character Class" | F | pp. 6–7 | Prior packet; text-only |
| "Adjust Ability Scores" | F | p. 7 | Prior packet; text-only |
| "Roll for Hit Points" prose | F | pp. 7–8 | **VV (p. 8)** |
| Ch. 13 "Creating Characters" | F | p. 145 | Prior packet; text-only |
| Ch. 10 "Creating High-Level Player Characters" Step 6 | D/F | pp. 129–131 | Prior packet; text-only |
| Character Classes and Ability Requirements Table | B/C | p. 7 | **Not yet VV** — see §5 |
| Character Height and Weight Table | B | p. 12 | Excluded — not ability generation |

### CHAR-002 — Race & Class Eligibility

| Object | Class | Location | Status |
|---|---|---|---|
| **Character Classes and Ability Requirements Table** | B/C | p. 7 | **Not yet VV** — see §5 |
| Ch. 2 class stat blocks (Cleric…Mystic) | D | pp. 13–31 | **VV for Dwarf (p. 24), Elf (p. 25), Halfling (p. 26), Mystic (p. 31)** |
| **Dwarf Experience Table** | B/C | p. 23 | **VV (p. 24)** — levels 1–12, then Attack Ranks C–M |
| **Elf Experience Table** | B/C | **p. 26** | **VV** — see §2 |
| **Halfling Experience Table** | B/C | p. 27 | Not yet VV |
| Cleric/Fighter/Magic-User/Thief Experience Tables | B/C | pp. 14, 16, 19, 22 | Cleric & Fighter read as OCR table text; not VV |
| Druid / Mystic Experience Tables | B/C | pp. 29, 29 | Not yet VV |
| **Mystic Special Abilities Table** | B/C | p. 31 | **VV** — levels 1–16, confirms Mystic cap 16 |
| Experience Bonuses and Penalties Table | B/C | p. 12 | Not yet VV — boundary only (`ADV-001`) |

### CHAR-003 — Hit Points & Hit Dice

| Object | Class | Location | Status |
|---|---|---|---|
| **Character Class and Hit Dice Table** | B/C | **p. 8** | **VV** — Cleric d6, Fighter d8, Magic-user d4, Thief d4, Dwarf d8, Elf d6, Halfling d6, Druid *, Mystic d6 |
| "Roll for Hit Points" prose | F | pp. 7–8 | **VV (p. 8)** |
| Ch. 1 "Constitution" | F | p. 10 | **VV** — 1-hp floor per roll; high-level cutoff |
| Ch. 1 "Hit Dice and Hit Points" | F | p. 12 | Not yet VV |
| Ch. 2 per-class "Hit Dice:" lines | D | pp. 13–31 | **VV for Dwarf, Elf, Halfling, Mystic** |
| Elf expanded "Hit Dice:" description | F | **p. 25** | **VV** — see Finding 3 |
| **Maximum Hit Points (Humans) Table** | B/C | p. 129 | Not yet VV — see §5 |
| **Maximum Hit Points (Demihumans) Table** | B/C | p. 129 | Not yet VV — see §5 |
| Ch. 10 "Creating High-Level PCs" Step 6 per-class list | D/F | pp. 130–131 | Prior packet; text-only |

### CHAR-007 — General Ability Score Mechanical Effects

| Object | Class | Location | Status |
|---|---|---|---|
| **Bonuses and Penalties for Ability Scores Table** | B/C | **p. 9** | **VV** — 2-3:−3, 4-5:−2, 6-8:−1, 9-12:none, 13-15:+1, 16-17:+2, 18:+3 |
| **Abilities and Adjustments Table** | B/C | **p. 10** | **VV** — see Finding 1 (citation error) |
| **Intelligence and Languages Table** | B/C | p. 10 | **VV** |
| **Charisma Adjustment Table** | B/C | p. 10 | **VV** — Reaction Adj / Max Retainers / Retainer Morale |
| Per-ability prose (Str, Int, Wis, Dex, Con, Cha) | F | pp. 9–10 | **VV** |
| "High Wisdom and Saving Throws" | E/F | **p. 9** | **VV** — see Finding 2 |
| "Saving Throws" (five categories named) | F | p. 9 | **VV** — newly inspected |
| "Armor Class" / Armor Type and Armor Class Table | B/C/F | p. 8 | **VV** — Dex→AC application; `COMBAT-002` boundary |
| AC / Attack Roll strip | B | p. 9 | **VV** — `COMBAT-002` boundary |
| Ch. 13 "Ability Checks" | F | p. 143 | Prior packet; text-only |
| Ch. 19 "Ability Scores and Saving Throws" | F | p. 266 | Prior packet; text-only |

## 4. Findings

### Finding 1 — `CHAR-007` miscites its own principal table
**Category: B — INCOMPLETE BUT NON-CONTRADICTORY.** Packet correction required.

`docs/rules/evidence/CHAR-007-evidence.md` cites the **Abilities and Adjustments Table** at **p. 9**. It is on **p. 10**. Page 9 carries the Bonuses and Penalties for Ability Scores Table and the Strength write-up; the Abilities and Adjustments Table opens page 10.

The table's **content** is confirmed correct in every row (Strength → attack/damage/opening doors; Intelligence → languages, general skills (optional); Wisdom → saving throws vs. spells; Dexterity → attack rolls (thrown and missile), Armor Class; Constitution → hit points per experience level; Charisma → reactions from NPCs). Only the page reference is wrong — precisely the class of error that arises when a table is cited from a linearized text stream rather than from the page.

### Finding 2 — Wisdom's saving-throw effect is narrower than recorded
**Category: B — INCOMPLETE BUT NON-CONTRADICTORY.**

RC p. 9, "High Wisdom and Saving Throws" (visually verified): a Wisdom of 13 or more gives *"a bonus to **one of** his saving throws"*, and 8 or less gives a penalty; the adjustment affects saving throws vs. spells.

The `CHAR-007` packet records the effect as "Wisdom → saving throws vs. spells" without the "one of" framing. Non-contradictory, and it does not disturb the `CHAR-007`/`COMBAT-004` ownership boundary — but it sharpens what `CHAR-007` actually owns, and should be carried into any future synthesis.

Also newly inspected on p. 9: RC names the five saving-throw categories there (Poison or Death Ray; Magic Wand; Turning to Stone or Paralysis; Dragon Breath; Spells or Magic Staff), and gives a worked 1st-level **elf** example (12/13/13/15/15) that **exactly matches** the Elf Saving Throws Table's levels 1-3 column on p. 26 — an independent cross-confirmation obtained only by reading both pages.

### Finding 3 — Elf `+1` vs `+2` is real, printed, and same-page
**Category: D — INTERNAL SOURCE CONFLICT (previously recorded; now upgraded in precision). REMAINS UNRESOLVED BY DIRECTION.**

Visually verified on **RC p. 25**, both statements appear on the **same printed page**:

- Elf stat block: *"Hit Dice: 1d6 per level up to 9th level. 10th level, **+1 hit point**, and Constitution adjustment does not apply. Maximum Level: 10."*
- Elf Class Details prose: *"An elf starts with 1d6 (1-6) hit points (plus Constitution bonus, if any) and gains 1d6 more hit points (plus bonus) with each level of experience. **Two additional hit points are gained at 10th level.**"*

This **corrects a speculation** raised during the defect investigation that the contradiction might itself be an OCR artifact. It is not. It is printed, and it is intra-page — a tighter and more damning form of the conflict than the Stage-A packet's "each chapter contradicts itself" framing.

Per direction, this conflict is **not resolved here**. No passage was privileged, no majority counted, no arithmetic used to select a value, and the void BECMI escalation (§2) is not relied upon.

### Finding 4 — Elf maximum level: completeness failure, not a genuine RC conflict
**Category: C-adjacent — SPECIFICATION-AFFECTING, but affecting no approved specification.**

The Stage-A packet's Conflict A escalated a 3-to-1 split on the Elf level cap. With p. 26 inspected, the picture is **5 authoritative statements at 10** (Elf Experience Table's terminating Level column; Elf Saving Throws Table's level bands; Elf stat block "Maximum Level: 10"; Elf prose "may only advance to 10th level"; Elf Special Abilities "After reaching maximum level (10th)") **against one Chapter 1 p. 12 summary sentence at 12**.

The human has adjudicated the cap at 10 and Ch. 1 p. 12 as erroneous summary text.

**No approved specification is affected**, because no `CHAR-*` Rule Card exists and `CHAR-003` was never synthesized. The finding is that the *escalation itself* was an artifact of incomplete inspection — Stage A should have presented a lopsided weight of evidence plus one outlier, not a balanced unresolved conflict.

### Finding 5 — Dwarf and Mystic caps independently corroborated
**Category: A — COMPLETE.**

Newly inspected structural objects confirm caps the packets asserted from prose: the **Dwarf Experience Table** (p. 24) enumerates levels 1–12 then Attack Ranks C–M, and the Dwarf Saving Throws Table uses bands 1-3/4-6/7-9/**10-12**; the **Mystic Special Abilities Table** (p. 31) enumerates levels 1–16. Both match `DEC-0008` and the packets.

### Finding 6 — `CHAR-002` and `CHAR-003` core content confirmed
**Category: A — COMPLETE (for the objects visually verified).**

The **Character Class and Hit Dice Table** (p. 8) is confirmed exactly as recorded, including Druid's "*Does not apply*". The p. 8 "Roll for Hit Points" prose confirms the `CHAR-003 → CHAR-007` dependency in RC's own words (it directs the reader to the Bonuses and Penalties for Ability Scores Table for the Constitution adjustment). The p. 10 Constitution write-up confirms the 1-hit-point-per-roll floor and the high-level cutoff.

## 5. Outstanding-Object Disposition — completed 2026-08-23

Every object listed as outstanding by the first audit pass is now dispositioned. **No `outstanding object class` remains.**

| Object | Location | Disposition | Result |
|---|---|---|---|
| **Character Classes and Ability Requirements Table** | p. 7 | **OPENED / VISUALLY INSPECTED** | All nine rows, three columns. **No footnotes, symbols, or columns lost in OCR.** All `CHAR-002` claims **CONFIRMED** |
| **Adjust Ability Scores** box + numbered rules + worked examples | p. 7 | **OPENED / VISUALLY INSPECTED** | All four trade rules and both worked examples **CONFIRMED** |
| **Maximum Hit Points (Humans) Table** | p. 129 | **OPENED / VISUALLY INSPECTED** | Cleric 54/27/87/97/108; Fighter 72/27/111/131/153; Magic-user 36/27/69/79/90; Thief 36/27/75/95/117 — **CONFIRMED** |
| **Maximum Hit Points (Demihumans) Table** | p. 129 | **OPENED / VISUALLY INSPECTED** | Dwarf 72/27/+9/108; **Elf 54/27/+2/83**; Halfling 48/24/—/72. Column header reads literally "Lvl 10-12", shared across rows — **CONFIRMED**, no OCR distortion |
| Ch. 1 "Hit Dice and Hit Points" / "Maximum Levels and Experience Points" | p. 12 | **OPENED / VISUALLY INSPECTED** | Con-applies-only-to-rolled-dice **CONFIRMED**; the "dwarves and elves… 12th level" outlier **CONFIRMED AS GENUINELY PRINTED** |
| **Experience Bonuses and Penalties Table** | p. 12 | **OPENED / VISUALLY INSPECTED** | New structure captured — see Finding 9 |
| **Halfling Experience Table** + Halfling Saving Throws Table | p. 27 | **OPENED / VISUALLY INSPECTED** | Levels 1–8 then Attack Ranks A–K; save bands 1-3/4-6/**7-8**. Cap 8 **CONFIRMED** |
| **Dwarf Experience Table** + Dwarf Saving Throws Table | p. 24 | **OPENED / VISUALLY INSPECTED** | Levels 1–12 then Ranks C–M; save bands cap **10-12**. Cap 12 **CONFIRMED** |
| **Elf Experience Table** + Elf Saving Throws Table | p. 26 | **OPENED / VISUALLY INSPECTED** | See §2. Cap 10 **CONFIRMED** |
| **Mystic Special Abilities Table** | p. 31 | **OPENED / VISUALLY INSPECTED** | Levels 1–16. Cap 16 **CONFIRMED** |
| Ch. 13 "Creating Characters" | p. 145 | **OPENED / VISUALLY INSPECTED** | Both non-equivalent discard criteria and the switch provision **CONFIRMED AS PRINTED** |
| Ch. 19 "Ability Scores and Saving Throws" | p. 266 | **OPENED / VISUALLY INSPECTED** | Six-ability mapping + `* Combined modifier cannot exceed +/− 3` **CONFIRMED**; boundary sentence **CONFIRMED** |
| **Extended Experience Table** | p. 266 | **OPENED / VISUALLY INSPECTED** | **NEWLY DISCOVERED OBJECT** — see Finding 8 |
| Ch. 10 "Creating High-Level Player Characters" Steps 1–8 | pp. 129–130 | **OPENED / VISUALLY INSPECTED** | **CONTRADICTS a `CHAR-001` negative finding** — see Finding 7 |
| Cleric / Fighter / Magic-User / Thief Experience Tables | pp. 14, 16, 19, 22 | **EXCLUDED WITH REASON** | Human classes; cap 36 for all four is stated at p. 12 (visually verified) and corroborated per-class at pp. 13–22. Their table **schema** is confirmed by the three visually verified demihuman tables and by the Cleric/Fighter tables read in full as OCR table text, which retained their rows. No cap dispute exists for any human class. Risk assessed **low**; re-open if any human-class progression question arises |
| ~~Druid / Mystic Experience Tables — EXCLUDED WITH REASON~~ | p. 29 | **EXCLUSION WITHDRAWN 2026-08-23 — OPENED / VISUALLY INSPECTED** | **This exclusion was wrong and is retracted.** It excluded the very objects `CHAR-002`'s own open question named as unread. Both entries have now been read as complete source units — see §5.2. **Druid cap is 36, not 30**; the entries carry material requirements beyond p. 7 |
| **Complete Druid class entry** (stat block, transition prose, Class Details, Abilities and Restrictions, Higher Experience Levels, Druid Experience Table, Druid Saving Throws Table) | pp. 28–29 | **OPENED / VISUALLY INSPECTED** | See §5.2 — **material findings** |
| **Complete Mystic class entry** (stat block, Class Details, detailed prose, Mystic Experience Table, Mystic Special Abilities Table) | pp. 29–31 | **OPENED / VISUALLY INSPECTED** | See §5.3 |
| Ch. 13 "Open Doors" Ability / Doors / Secret Doors / Listening | p. 147 | **OPENED / VISUALLY INSPECTED** | Closes `CHAR-007` open question 1 — see §5.4 |
| Ch. 8 Initiative / "Dexterity Adjustments (Optional)" | p. 102 | **OPENED / VISUALLY INSPECTED** | Closes `CHAR-007` open question 4 — see §5.4 |
| Ch. 13 Mapping / Multiple Characters / Overusing Dice / Reality Shifts / Record Keeping | p. 148 | **OPENED / VISUALLY INSPECTED** | Closes `CHAR-001`'s residual "sections not exhaustively read" — none bears on ability-score generation |

## 5.1a Withdrawal of the "single governing object" claim

The previous remediation described the p. 7 Character Classes and Ability Requirements Table as `CHAR-002`'s **"single governing object."** **That claim is withdrawn. It was too strong, and it was made while `CHAR-002`'s own packet recorded that the Druid and Mystic entries had not been read in full.**

The p. 7 table is the **principal** governing object for the *common creation-eligibility matrix*. It does **not** exhaust class-specific entry rules. For class-related responsibilities the source must be mapped structurally, entry by entry (protocol §9.7, §9.8).

## 5.2 Complete Druid Entry — findings (RC pp. 28–29)

**Objects read as one unit:** stat block (p. 28); transition prose (p. 28); Class Details (p. 28); Abilities and Restrictions (p. 28); Higher Experience Levels (pp. 28–29); **Druid Experience Table** (p. 29); **Druid Saving Throws Table** (p. 29).

### Finding 10 — the p. 7 "Other Requirements" column is NOT exhaustive for Druid
**Category: C-adjacent — SPECIFICATION-AFFECTING, but affecting no approved specification** (no `CHAR-*` Rule Card exists).

p. 7 states only *"Neutral alignment, obtain 9th level as a cleric."* The p. 28 entry adds:

| Requirement | RC text (p. 28) | Not in p. 7 |
|---|---|---|
| **Upper level bound** | "A Neutral cleric of **9th to 29th level** may choose to study nature…" | **Yes** — p. 7 gives no upper bound |
| **Woodland residence** | "the cleric **must find and live in a woodland home**" | **Yes** |
| **Meditation period** | "**meditating for one to four (1d4, rolled by the DM) months**" | **Yes** — and it is a *random duration* |
| **Instruction and testing** | "a higher level druid (usually 25th level or greater) will find the cleric, **test him for worthiness**, and teach him the principles of druidic philosophy and magic" | **Yes** |
| **Admission** | "The new druid may then join the realm of the druids" | **Yes** |
| **Ongoing alignment maintenance** | On changing alignment the druid "will lose all druid benefits including druidic spells **unless he returns to Neutral alignment**" | **Yes** — an ongoing condition, not only an entry condition |
| **Ongoing residence** | "He **must live in a woodland home**, rather than in a town or city" | **Yes** |

### Finding 11 — NEW INTERNAL SOURCE CONFLICT: Druid maximum level
**Category: D — NEW INTERNAL SOURCE CONFLICT.**

| RC location | Statement | Verified |
|---|---|---|
| Ch. 1, p. 12 | "Druids may only achieve **30th** level (and only then after a special challenge)" | **Visually** |
| Ch. 2, p. 28, Druid stat block | "**Maximum Level: 36**; Druid must challenge and defeat another Druid of the newly-attained experience level starting at 30th level" | **Visually** |
| Ch. 2, p. 28, Higher Experience Levels | nine druids of 30th, seven of 31st, five of 32nd, four of 33rd, three of 34th, two of 35th, and **one of 36th (the Great Druid)** | **Visually** |
| **Ch. 2, p. 29, Druid Experience Table** | Level column enumerates **9 through 36** | **Visually** |
| Ch. 2, p. 29, Druid Saving Throws Table | bands 9-12 … **33-36** | **Visually** |

**Four objects at 36 against one Ch. 1 p. 12 summary sentence at 30.** This is the **same p. 12 passage** that states the Elf cap as 12 against six statements at 10. That passage is now demonstrably unreliable on **two of its five** class-cap claims.

**Not resolved by this audit** — this artifact made no ruling and had no authority to. Reported as a new Category D finding, owner `ADV-002`.

#### Human adjudication recorded — 2026-08-29

The independent human review confirmed the conflict is genuine and adjudicated it. **This is a human adjudication, not an agent-derived resolution.**

```text
Standard RC Druid progression:            levels 9–36
Maximum Druid level:                      36
Special challenge / limited-rank progression:
                                          begins with advancement to 30th level
RC Ch. 1 p. 12, "Druids may only achieve 30th level":
                                          treated as erroneous summary text
```

**Source of truth for this question: the detailed Druid class progression material and the Druid Experience Table (RC pp. 28–29).** The Ch. 1 p. 12 sentence is **not deleted from this record** — it is real, printed, and retained in the table above; it is simply not authoritative for this project on this point.

**No alternate-source research is needed or permitted for this conflict.** It is resolved from RC's own detailed material, exactly as the Elf cap was (§8).

**Ownership is unchanged and `CLUSTER-002` is not expanded.** The cap governs advancement, so it belongs downstream to `ADV-002`; recorded there via `docs/rules/INVENTORY.md` "Progression-Scope Findings". Nothing in `CHAR-001`/`CHAR-002`/`CHAR-003`/`CHAR-007` changes: `CHAR-002` already returns *Druid not selectable at creation*, which this adjudication **strengthens rather than alters** (the Druid Experience Table begins at level 9).

### Finding 12 — Druid HP is consistent (no new conflict)
**Category: A — COMPLETE.** p. 28: "Starting with 10th level, +1 hit point per level, and Constitution adjustments do not apply"; "A character cannot become a druid until… Name (9th) experience level as a cleric. Therefore, from then on, he will receive only 1 hit point per experience level gained after 9th level." Consistent with p. 129 ("same as those for a cleric") and p. 130 ("As cleric… +1/level thereafter"). `CHAR-003` unaffected.

### Ownership — proposed, not adopted

| Evidence | Proposed owner | Why | Dependency implication |
|---|---|---|---|
| Druid **not selectable at creation** | **`CHAR-002`** (already so) | Druid Experience Table starts at level 9; p. 28 "you can't start a character off as a druid" | **None** — `CHAR-002` Procedure A already returns *not eligible at creation*. **Strengthened, not changed** |
| Cleric→Druid **transition procedure** (9th–29th, woodland home, 1d4 months, testing, instruction, admission) | **`CHAR-013`** (High-Level Class Branches — `INVENTORY.md` already lists Druid under it) | It is a later class-change procedure, not creation eligibility | Would need `CHAR-008` (alignment) and `ADV-002` (level) |
| Ongoing alignment/residence maintenance | `CHAR-013` with `CHAR-008` | Ongoing conditions on retaining druid status | — |
| 30th-level challenge progression | `ADV-002` | Advancement mechanic | — |

**PROPOSED — NOT ADOPTED.** `CLUSTER-002` is **not** expanded; no boundary change is made. `CHAR-002`'s executable eligibility rule is **unaffected**.

## 5.3 Complete Mystic Entry — findings (RC pp. 29–31)

**Objects read as one unit:** stat block (p. 29); Class Details (p. 29); detailed prose (p. 29); **Mystic Experience Table** (p. 29); **Mystic Special Abilities Table** (p. 31).

### Finding 13 — Mystic creation eligibility is CONFIRMED complete at p. 7
**Category: A — COMPLETE.** p. 29 Class Details restates exactly: *"A mystic character must have scores of 13 or better in both his Wisdom and Dexterity abilities."* Mystic **is** a 1st-level creation class (Experience Table runs 1–16, XP 0 at level 1). `CHAR-002`'s Mystic claim **stands** — but it is only now established by entry inspection rather than assumed from the summary table.

### Finding 14 — Mystic carries material downstream requirements, none of them creation eligibility
**Category: B — INCOMPLETE BUT NON-CONTRADICTORY**, all owned outside `CLUSTER-002`:

- **Two-prime-requisite XP disambiguation** (p. 29): "since he must have a score of at least 13 in Dexterity to be a mystic in the first place, it is **his Strength score that determines his bonus to experience**." → `ADV-001`. Materially qualifies the general two-prime-requisite rule for this class.
- **Equipment prohibition** (p. 29): "Mystics can **never** wear armor of any type, nor can they ever use protective magical devices (such as rings, cloaks, etc.)" → `CHAR-009`/`TREAS-004`.
- **Treasure/XP condition** (p. 29): "Mystics receive experience from treasure **only if they donate it to the needy**. Also, they must **donate (tithe) ten percent** of their treasure to their cloister." → `ADV-001`. A genuine XP-award condition.
- **Oath sanction** (p. 29): forswearing → expelled from cloister, "**may not gain any new experience levels, loses one level per year** away from the cloister" → `ADV-002`.
- **Alignment tendency** (p. 29): "Most mystics (75%) are Lawful, though other alignments are represented" — a tendency, **not a requirement** → `CHAR-008`.
- **HP** (p. 29): 1d6/level to 9th; **+2/level** from 10th; Con no longer applies; Max Level 16 — consistent with p. 130 and p. 129. `CHAR-003` unaffected.

**None is creation eligibility.** `CHAR-002` is not expanded.

## 5.4 Closure of `CHAR-007` unfinished inspection

- **Open Doors ownership (open question 1).** Ch. 13 p. 147 carries a dedicated **"Open Doors" Ability** section: 1d6, success on 5–6, **modified by the Strength score adjustment**, natural 6 always opens — and **adds** two rules Ch. 1 omits: the attempt may be made **once per round per character**, and **a failed attempt forfeits surprise** ("monsters on the other side of the door cannot be surprised; they have heard the noise"). **Disposition: RESOLVED BY SOURCE INSPECTION → CONFIRMED OUT OF SCOPE for `CHAR-007`.** `CHAR-007` owns the Strength **adjustment value**; the **procedure** belongs to `EXP-005`, which is where p. 147 sits (alongside Doors, Secret Doors, Special Doors, Listening). New dependency noted: `ENC-002` (surprise).
- **Ability effect on initiative (open question 4).** Ch. 8 p. 102 carries **"Dexterity Adjustments (Optional)"**: at DM option, Dexterity modifies the **individual** initiative roll per the Bonuses and Penalties table, and "does not affect the party's roll in group initiative." Individual initiative is itself optional and is **declined for V1** by `DEC-0008`. **Disposition: RESOLVED BY SOURCE INSPECTION → CONFIRMED OUT OF SCOPE** (owner `COMBAT-006`). `CHAR-007`'s V1 effect list is correct. RC's own cross-reference here cites the table as "on **page 9**", independently confirming the p. 9 / p. 10 split corrected in Finding 1.
| Ch. 13 "Ability Checks" | p. 143 | **EXCLUDED WITH REASON** | Short prose, **no structured object, no table, no columns**; read in full in context via text. Fails every §9.2 visual-verification trigger. Risk assessed **low** |

## 5.1 Additional Findings from the Outstanding-Object Pass

### Finding 7 — `CHAR-001`'s "no non-random alternative" negative finding is CONTRADICTED
**Category: B — INCOMPLETE BUT NON-CONTRADICTORY as to the 1st-level procedure; but the packet's negative claim is falsified.**

`CHAR-001-evidence.md` §7 records as a negative result: *"no non-random ability-generation alternative; no 'roll 4d6 drop lowest'-style variant."*

RC p. 130, "Creating High-Level Player Characters," **Step 2: Generate Ability Scores**, visually verified, gives **two** alternatives:

- **First Method: Rolling And Assigning Scores** — the player rolls 3d6 **eight times**, keeps the **six best scores**, and assigns them to abilities **in whatever order he chooses**.
- **Second Method: Point Allocation** — the DM gives a point total (60 + 5d6, or an equal allotment of at least 60 and no more than 90) which the player distributes; the 3–18 range still applies.

The second is an explicitly **non-random** generation method. Both are scoped to creating characters above 1st level, so `CHAR-001`'s **baseline 1st-level procedure is unaffected**. But the packet's negative claim was stated unconditionally and is false as written — a textbook instance of the defect Guardrail B now prohibits.

This also **resolves** `CHAR-001-evidence.md` open question 2 ("whether Ch. 10 high-level creation alters the ability-score step"): **yes, materially.**

### Finding 8 — Extended Experience Table (p. 266) never dispositioned
**Category: B — INCOMPLETE BUT NON-CONTRADICTORY.**

A newly discovered named object, listed in the Tables Index as `Extended Experience Table . 266` and never dispositioned by Stage A. It tabulates Dwarf / Elf / Halfling / Mystic XP for levels **1–36** under the Chapter 19 "Demihuman and Mystic Experience Levels" variant.

That variant is **NOT ENABLED for V1** (`DEC-0008`), so it governs nothing in current scope. It is recorded because (a) a named table must not sit outside the coverage checklist, and (b) its accompanying text is precise about per-level hit points under the variant (e.g. the dwarf gets 2, not 3, per level; Constitution still does not apply), which future `ADV-002`/`CHAR-003` work must not confuse with the core rules.

**It does not bear on the core-rules Elf `+1`/`+2` conflict and must not be used to resolve it.**

### Finding 9 — Experience Bonuses and Penalties Table carries per-class structure OCR flattened
**Category: B — INCOMPLETE BUT NON-CONTRADICTORY.** Belongs to `ADV-001`.

Visually verified at p. 12, the table is not uniform across classes:

- **Elf** uses a *conjunctive two-ability* rule (Str 13-18 **and** Int 13-15 → +5%; Str 13-18 **and** Int 16-18 → +10%).
- **Halfling** distinguishes **or** from **and** (either → +5%; both → +10%).
- **Mystic**'s penalties are **halved** relative to every other class (−10% / −5% rather than −20% / −10%).

`CHAR-002` correctly treats prime-requisite XP effects as an `ADV-001` boundary pointer, so this is not a `CHAR-002` defect. It is recorded as newly captured structure for `ADV-001`, and as further evidence that these tables carry relationships linearization destroys.

## 6. Independent Completeness Pass

Started from the RC Table of Contents and Tables Index, not from the packets.

**What the first pass inspected:** Chapter 1 pp. 8–10; Chapter 2 pp. 24–26, 31.

**What it could plausibly have missed:** the remaining per-class Experience Tables; the p. 7 requirements table; the p. 129 maximum-HP tables; Chapter 13 and 19 objects.

**Additional objects found by the second pass:** the Tables Index enumerates a per-class Experience Table and a per-class Saving Throws Table for **every** class (Cleric 14, Dwarf 23, Elf 26, Fighter 16, Halfling 27, Magic-User 19, Thief 22, Druid 29, Mystic 29–30). The Stage-A packets inspected **none** of these as objects. Two of them (Elf, Dwarf) have now been verified and proved structurally decisive for level caps; the remainder are listed in §5 as outstanding.

**Did new material change the evidence picture?** Yes, materially: Finding 4 converts a reported unresolved conflict into a completeness failure, and Finding 1 corrects a citation in an accepted packet. No approved mechanic changed, because none exists.

**Not certified on keyword grounds.** Every claim of verification above names a page that was read as an image.

## 6.2 Independent Completeness Pass — Second Round (post-remediation)

**Procedural separation.** Performed after the §5 outstanding-object work closed, restarting from the Rules Cyclopedia's **Table of Contents** and **Tables Index** and from the per-class table listings — deliberately **not** from §3's inventory, §5's disposition table, or the four evidence packets. Method: re-read the Tables Index end-to-end, extract every entry whose title names an ability, a class, hit points, experience, or a saving throw, and check each against what the audit already holds.

**Per responsibility:**

| | `CHAR-001` | `CHAR-002` | `CHAR-003` | `CHAR-007` |
|---|---|---|---|---|
| **Additional objects discovered** | Ch. 10 Step 2 alternative generation methods (p. 130) | Extended Experience Table (p. 266) | Extended Experience Table (p. 266); Ch. 19 elf/dwarf variant HP statements | Experience Bonuses table structure (p. 12, → `ADV-001`) |
| **Objects independently confirmed** | p. 7 Adjust box; p. 145 discard/switch | p. 7 requirements table; three demihuman experience tables | p. 8 HD table; p. 129 both max-HP tables; p. 12 progression prose | pp. 9–10 all four tables; p. 266 mapping |
| **Omissions found** | **Yes — Finding 7** (negative claim falsified) | **None** | Reframing only (Finding 4); no new mechanic | **Yes — Finding 1** (citation) |
| **Evidence conclusions changed?** | **Yes** — one negative finding struck; one open question resolved | **No** — all claims confirmed | **No mechanic changed**; conflict A reframed, conflict B unchanged | **No content change**; citation only |
| **Completeness certifiable?** | **Yes**, after correction | **Yes** | **Yes**, after reframing | **Yes**, after citation fix |

**Tables Index entries checked and dispositioned in this round** (beyond those already held): `Character Height and Weight Table . 12` (excluded — not an in-scope mechanic); `Armor Type and Armor Class Table . 8` (inspected on p. 8; `COMBAT-002` boundary); `Saving Throws Table: All Characters . 109` (excluded — `COMBAT-004`); `Attack Rolls Table . 106` (excluded — `COMBAT-002`); `Skill Slot Acquisition (Humans/Demihumans) Tables . 86` (excluded — `CHAR-012`); `Sample Skills Table . 82` (excluded — `CHAR-012`); `Levels of Weapon Mastery Table . 75` (excluded — `CHAR-011`); `Duration of Charm Table . 145` (inspected on p. 145; the NPC-Intelligence context `CHAR-001` cites); `Extended Experience Table . 266` (**newly captured**, Finding 8); every per-class Experience and Saving Throws Table (dispositioned in §5).

**This pass did not merely re-affirm the first.** It falsified a `CHAR-001` negative finding and surfaced a named table (`Extended Experience Table`) that neither Stage A nor the first audit round held. That is the outcome an adversarial pass is supposed to produce.

**Residual risk, stated plainly.** Both passes were executed by the same agent. Procedural separation (restart from finding aids, not from prior work) mitigates but does not eliminate correlated blind spots. A genuinely independent reviewer remains preferable, and the §5 reasoned exclusions (four human-class experience tables; two special-class tables; Ch. 13 Ability Checks prose) are the most likely place a further omission would hide.

## 6.1 Negative-Finding Re-Audit (Guardrail B)

Every negative claim across the four packets, classified by what actually supported it.

| Packet | Claim | Basis | Disposition |
|---|---|---|---|
| `CHAR-001` | "no non-random ability-generation alternative; no roll-and-drop variant" | **B — keyword exhaustion** | **CONTRADICTED** by RC p. 130 (Finding 7). Must be struck |
| `CHAR-001` | "no re-roll-individual-scores provision distinct from whole-character discard" | B | Rephrase: *not located after inspecting Ch. 1 pp. 6–8 and Ch. 13 p. 145* |
| `CHAR-002` | "no ability-score *maximum* gating any class" | **A — object inspection** (p. 7 table now visually verified) | **STANDS** — the table's "Other Requirements" column contains only minimums |
| `CHAR-002` | "no requirement expressed in adjustment terms" | **A — object inspection** | **STANDS** |
| `CHAR-002` | "no Ch. 19 variant alters class eligibility" | **A** — Ch. 19 visually inspected (p. 266); its three sections do not touch eligibility | **STANDS** |
| `CHAR-003` | "no hit-point reroll provision located" | B | Rephrase to research-operation claim |
| `CHAR-003` | "no ability other than Constitution modifies hit points" | **A** — Abilities and Adjustments Table (p. 10) visually verified; Constitution is the only HP row | **STANDS** |
| `CHAR-003` | "no HP variant in Ch. 19's enabled content" | **A** — p. 266 visually inspected | **STANDS**, with Finding 8 noted |
| `CHAR-007` | "no seventh ability; no alternative adjustment table; no per-class variation of the shared table" | **A** — pp. 9–10 visually verified | **STANDS** |
| `CHAR-007` | "no ability-score effect on initiative located" | B — Ch. 8 not searched exhaustively | Rephrase; flag for `COMBAT-006` |

**Pattern:** every claim that **stands** does so because a governing object was inspected. Every claim requiring correction rested on keyword exhaustion. This is precisely the distinction Guardrail B encodes.

## 6.3 Open-Question Closure Gate — reconciliation table (protocol §10.2.1)

Built by reading the **original** Stage-A packets' unresolved/challenge sections, not their corrected banners.

| # | Original open question (packet, §) | Source region implicated | Inspected? | Result | Owner | Blocks completeness? |
|---|---|---|---|---|---|---|
| 1 | `CHAR-001` §9.1 — discard criterion threshold | Ch. 13 p. 145 | **Yes, visually** | Both non-equivalent criteria confirmed **printed** in one passage | `CHAR-001` | **RETAINED AS GENUINE SOURCE AMBIGUITY** — no |
| 2 | `CHAR-001` §9.2 — Ch. 10 high-level creation effect on score step ("not established") | Ch. 10 pp. 129–130 | **Yes, visually** | **RESOLVED** — Step 2 gives roll-8-keep-6-assign and point-allocation; falsifies a packet negative finding | `CHAR-001` | No |
| 3 | `CHAR-001` §9.3 — trade ↔ switch interaction/order | Ch. 1 p. 7; Ch. 13 p. 145 | **Yes, visually (both)** | Neither cross-references the other; RC is silent on the interaction | `CHAR-001` | **RETAINED AS GENUINE SOURCE AMBIGUITY** — no |
| 4 | `CHAR-001` §9.4 — does "no adjustments later" bind the Ch. 13 provision | Ch. 1 p. 7; Ch. 13 p. 145 | **Yes, visually (both)** | RC silent | `CHAR-001` | **RETAINED AS GENUINE SOURCE AMBIGUITY** — no |
| 5 | `CHAR-001` §14 — "further DM-facing qualifications may exist in sections not exhaustively read" | Ch. 13 section list (TOC); pp. 143, 145, 147, 148 | **Yes** — list enumerated; generation-relevant sections read | **RESOLVED BY SOURCE INSPECTION** — Mapping / Multiple Characters / Overusing Dice / Reality Shifts / Record Keeping bear on nothing in scope; remaining Ch. 13 sections owned elsewhere by subject | `CHAR-001` | No |
| 6 | `CHAR-002` §9.1 — can a Ch. 13 switch satisfy a demihuman minimum? | Ch. 1 p. 7; Ch. 13 p. 145 | **Yes, visually (both)** | RC silent on the interaction; Ch. 1 trade cannot touch Constitution at all | `CHAR-002` | **RETAINED AS GENUINE SOURCE AMBIGUITY** — no |
| 7 | **`CHAR-002` §9.2 — "Other Requirements" exhaustive for druid/mystic? "entries were not read in full"** | **Ch. 2 pp. 28–31** | **Yes, visually — both entries as complete units** | **RESOLVED BY SOURCE INSPECTION. Answer: NO for Druid** (Findings 10–11); **YES for Mystic** creation eligibility (Finding 13) | `CHAR-002` (creation) / `CHAR-013`, `ADV-002` (transition) | **No — this was the defect; it is now closed** |
| 8 | `CHAR-003` §10.1 — Conflict A, Elf max level | Ch. 1 p. 12; Ch. 2 pp. 25–26; Ch. 10 p. 129 | **Yes, visually (all)** | Human-adjudicated: **10, then Attack Ranks** | `ADV-002` | No — closed by ruling |
| 9 | `CHAR-003` §10.2 — Conflict B, Elf +1 vs +2 | Ch. 2 p. 25; Ch. 10 pp. 129, 130 | **Yes, visually (all four statements)** | Genuinely irreducible; 2 vs 2, all printed | `CHAR-003` | **RETAINED AS GENUINE SOURCE AMBIGUITY** — no |
| 10 | `CHAR-003` §10.3 — first-level special HP treatment? | Ch. 1 pp. 7–8, 10, 12 | **Yes, visually** | **RESOLVED** — no special first-level rule in any governing object | `CHAR-003` | No |
| 11 | `CHAR-003` §10.4 — does the 1-hp floor govern fixed gains? | Ch. 1 p. 10; p. 12; Ch. 2 entries | **Yes, visually** | RC states the floor in terms of rolls only; silent for fixed gains | `CHAR-003` | **RETAINED AS GENUINE SOURCE AMBIGUITY** — no |
| 12 | `CHAR-003` §10.5 — is Ch. 10 Step 6 an alternative or a restatement? ("not established") | Ch. 10 p. 130 | **Yes, visually** | **RESOLVED** — Step 6 is an explicit alternative high-level-creation procedure with its own DM conventions (averaging, Con multiplier) | `CHAR-003` | No |
| 13 | `CHAR-003` §4 — "no hit-point reroll provision located" (search-based) | Ch. 1 pp. 8, 10, 12; Ch. 10 pp. 129–130 | **Yes, visually (all)** | **RESOLVED BY SOURCE INSPECTION** — no reroll in any governing object | `CHAR-003` | No |
| 14 | **`CHAR-007` §9.1 — Open Doors ownership; "Ch. 13 Doors (p. 147) not read in full"** | **Ch. 13 p. 147** | **Yes, visually** | **RESOLVED → CONFIRMED OUT OF SCOPE** (§5.4). Value stays with `CHAR-007`; procedure to `EXP-005`; new `ENC-002` surprise dependency | `EXP-005` | No |
| 15 | `CHAR-007` §9.2 — Armor Class ownership | Ch. 1 pp. 8–9 | **Yes, visually** | **CONFIRMED OUT OF SCOPE** — AC procedure is `COMBAT-002`; `CHAR-007` owns the Dex adjustment value | `COMBAT-002` | No |
| 16 | `CHAR-007` §9.3 — Charisma retainer columns ownership | Ch. 1 p. 10 | **Yes, visually** | **CONFIRMED OUT OF SCOPE** — retainer count/morale procedures are `CHAR-006`; `CHAR-007` owns the table values | `CHAR-006` | No |
| 17 | **`CHAR-007` §9.4 — ability effect on initiative; "Ch. 8 not exhaustively searched"** | **Ch. 8 p. 102** | **Yes, visually** | **RESOLVED → CONFIRMED OUT OF SCOPE** — Dexterity affects only the *optional* individual initiative, declined for V1 by `DEC-0008` | `COMBAT-006` | No |
| 18 | `CHAR-007` §9.5 — Wisdom `CHAR-007`/`COMBAT-004` overlap | Ch. 1 pp. 9–10; Ch. 19 p. 266 | **Yes, visually** | Boundary preserved per human ruling; one-row overlap recorded | `CHAR-007` / `COMBAT-004` | No |

**Every row is dispositioned. Zero items remain `BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED`. Zero silent unresolved research tasks.**

Six items are **RETAINED AS GENUINE SOURCE AMBIGUITY** — each verified as a real RC silence or a real printed contradiction with the governing objects inspected, **not** unfinished inspection disguised as ambiguity.

## 6.4 Final Adversarial Self-Review (protocol §10.1.1) — this round

Restarted from the TOC, Tables Index, chapter structure, class-entry headings, and cross-reference targets.

**Does any packet still claim completeness while containing "not checked / not read / not exhaustively searched / needs later research / source region not inspected"?**

Checked by re-grepping the original packets for that wording and matching each hit to §6.3. **Result: no.** All eighteen items are dispositioned; the four items that named an *unread source region* (rows 5, 7, 14, 17) have all had that region inspected visually.

**Additional omissions found this round:** the Druid/Mystic entries (row 7 — the triggering defect), Ch. 13 p. 147 (row 14), Ch. 8 p. 102 (row 17), Ch. 13 p. 148 (row 5). Also newly surfaced: **Finding 11**, a previously unrecorded Category D conflict on the Druid cap.

**Unresolved research tasks remaining: none.** Remaining open items are genuine rule ambiguities (rows 1, 3, 4, 6, 9, 11) plus one new unruled conflict (Finding 11, Druid cap, owned by `ADV-002`).

**Residual risk:** the §5 reasoned exclusions (four human-class Experience Tables) are the only remaining un-opened named tables in scope. They carry no cap dispute and their schema is confirmed by three visually verified sibling tables — but they are the likeliest place a further omission would hide, and an independent reviewer should test that exclusion first.

## 7. Status After This Audit

```text
CHAR-001 Stage-A evidence:  COMPLETENESS AUDITED — CORRECTION REQUIRED (Finding 7)
CHAR-002 Stage-A evidence:  COMPLETENESS AUDITED — CONFIRMED, no correction required
CHAR-003 Stage-A evidence:  COMPLETENESS AUDITED — CORRECTION REQUIRED (Finding 4 reframing)
CHAR-007 Stage-A evidence:  COMPLETENESS AUDITED — CORRECTION REQUIRED (Finding 1 citation)

Outstanding object classes:  NONE — all dispositioned (§5)
Open-question closure gate:  ALL 18 ITEMS DISPOSITIONED (§6.3)
Objects visually verified:   pp. 7, 8, 9, 10, 12, 24, 25, 26, 27, 28, 29,
                             31, 87, 91, 92, 93, 102, 129, 130, 145,
                             147, 148, 266

NEW Category D conflict:     Druid maximum level — Ch.1 p.12 says 30;
                             stat block, Higher Experience Levels, Druid
                             Experience Table and Druid Saving Throws
                             Table all say 36.
                             HUMAN-ADJUDICATED 2026-08-29 at 36, with the
                             special-challenge hierarchy beginning at 30th
                             (§5.2 Finding 11). Owner ADV-002.

Elf maximum level:          human-adjudicated at 10; not reopened
Elf fixed HP +1 vs +2:      UNRESOLVED, deliberately (all four statements
                            now visually verified as printed)
                            GENUINE PRIMARY-SOURCE CONFLICT
                            STAGE-B RESOLUTION REQUIRED
BECMI escalation:           void as to authorization; excluded from
                            current evidence and synthesis (§2)

CLUSTER-002 completeness:   INDEPENDENT REVIEW — PASS (human, 2026-08-29)
CLUSTER-002 evidence gate:  CLEARED (human, 2026-08-29)
CLUSTER-002 Stage B:        UNPAUSED — eligible, not begun (2026-08-29)
```

**This audit did not, and could not, certify its own completeness.** Under `DEC-0010` item 14 and protocol §10.1.2, the researcher that gathered this evidence may not issue the final completeness certification for its own package. It was prepared and submitted as `PREPARED FOR INDEPENDENT COMPLETENESS REVIEW`.

## 7.1 Independent Review Result — recorded 2026-08-29

The human project owner completed the independent primary-source completeness review and returned:

```text
CLUSTER-002 STAGE-A PRIMARY-SOURCE COMPLETENESS:
INDEPENDENT REVIEW — PASS

CHAR-001:  source coverage PASS   (genuine ambiguities retained)
CHAR-002:  source coverage PASS
CHAR-003:  source coverage PASS   (Elf fixed-HP conflict retained)
CHAR-007:  source coverage PASS
```

**The certification is the human reviewer's, not this artifact's.** The lifecycle is retained in order — self-issued claim withdrawn → `PREPARED FOR INDEPENDENT COMPLETENESS REVIEW` → independent `PASS` — because that ordering is the substance of `DEC-0010`, not a formality to be compressed after the fact.

**The prior source-completeness defect is considered remediated.**

### What this PASS does and does not mean

```text
Evidence completeness   and   rules ambiguity   are separate concepts.
```

| | Status at the completeness gate |
|---|---|
| **Unfinished source inspection** | **NOT ACCEPTABLE** — none remains (§6.3: all 18 items dispositioned, zero `BLOCKED`) |
| **Fully mapped but contradictory source** | **ACCEPTABLE** — carried forward as a documented Stage-B problem |

A source-complete evidence packet **may** contain a real contradiction. `CLUSTER-002` does: the Elf `+1` vs `+2` fixed-HP conflict (§4 Finding 3) survives this PASS untouched, classified `GENUINE PRIMARY-SOURCE CONFLICT — STAGE-B RESOLUTION REQUIRED`. So do the retained `CHAR-001` procedural ambiguities (§6.3 rows 1, 3, 4, 6, 9, 11). **This PASS certifies that the source was fully mapped. It does not assert that RC speaks with one voice where it does not.**

**Update — 2026-08-29.** `DEC-0010` is `Approved` and landed, and on that basis the human project owner **restored `CLUSTER-002`'s Human Evidence Review clearance** (all four packets `ACCEPTED`) and **unpaused Stage B**. Stage B is now **eligible to begin under a separate assignment; it has not begun.** Nothing in this artifact authorizes mechanical synthesis, legacy comparison, alternate-source research, a Simulator Ruling, or Rule Card drafting — those proceed only under that assignment. Implementation remains unauthorized (`ARCHITECTURE.md` §15.2). The full clearance history, including the suspension, is preserved at `docs/rules/clusters/CLUSTER-002-character-foundation.md` §3.

## 8. Elf Level-Cap — Complete Evidence Record and Human Adjudication

Recorded per direction. **The Chapter 1 p. 12 statement is real, printed, and is not erased from this record.**

| RC location | Statement | Verified |
|---|---|---|
| Ch. 1, p. 12, "Maximum Levels and Experience Points" | "Dwarves and elves may not progress beyond **12th** level" | **Visually** |
| Ch. 2, p. 25, Elf stat block | "Maximum Level: **10**" | **Visually** |
| Ch. 2, p. 25, Elf prose | "An elf may only advance to **10th** level" | **Visually** |
| Ch. 2, p. 25, Elf Special Abilities | "After reaching maximum level (**10th**)" | **Visually** |
| **Ch. 2, p. 26, Elf Experience Table** | Level column enumerates **1–10**, then XP→Attack Ranks C–M with no level numbers | **Visually** |
| **Ch. 2, p. 26, Elf Saving Throws Table** | Highest level band = **10** | **Visually** |
| Ch. 10, p. 129 | "elves **10th** level" | **Visually** |

**Characterization:** this is a **genuine Rules Cyclopedia textual inconsistency** — six statements at 10, one at 12 — not a research artifact and not a mere summary imprecision to be waved away.

**Human ruling (2026-08-23):**

```text
For this project:
    Elf maximum class level = 10
    Further standard progression = Attack Ranks
```

**The p. 26 Elf Experience Table is the source of truth for Elf progression.** The operational resolution is established by human adjudication using the detailed Elf progression table and class material. **No alternate-source research is needed or permitted for this question.** Not reopened by this audit.
