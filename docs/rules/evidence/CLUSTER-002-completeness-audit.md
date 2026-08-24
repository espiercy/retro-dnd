# Primary-Source Completeness Audit: CLUSTER-002 Stage A (CHAR-001, CHAR-002, CHAR-003, CHAR-007)

> **Retrospective audit artifact** produced under `docs/decisions/DEC-0010-primary-source-completeness-audit.md` and `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` §9.1–§9.4, §10.1.
>
> This audit is the direct consequence of the process defect recorded in `DEC-0010`. It is **not** a synthesis, **not** Stage B, and **not** authorization to change any mechanic. No Rule Card exists for any `CHAR-*` entry and none was created.
>
> **Status of the four Stage-A packets during this audit:** `PREVIOUSLY ACCEPTED — COMPLETENESS AUDIT PENDING`. Human Evidence Review clearance for `CLUSTER-002` is suspended; Stage B is paused.

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

## 5. Objects Not Yet Visually Verified — remaining audit work

Recorded honestly rather than certified. Under §9.2 these require visual verification before `CLUSTER-002` Stage A can be certified complete:

| Object | Location | Bears on |
|---|---|---|
| Character Classes and Ability Requirements Table | p. 7 | `CHAR-002` (its single governing table), `CHAR-001` |
| Maximum Hit Points (Humans) Table | p. 129 | `CHAR-003` |
| Maximum Hit Points (Demihumans) Table | p. 129 | `CHAR-003`, Finding 3 |
| Ch. 1 "Hit Dice and Hit Points" / "Maximum Levels and Experience Points" | p. 12 | `CHAR-003`, Finding 4's outlier statement |
| Halfling / Cleric / Fighter / Magic-User / Thief / Druid / Mystic Experience Tables | pp. 14, 16, 19, 22, 27, 29 | `CHAR-002`, `CHAR-003` |
| Ch. 13 "Creating Characters", "Ability Checks" | pp. 143, 145 | `CHAR-001`, `CHAR-007` |
| Ch. 19 "Ability Scores and Saving Throws" | p. 266 | `CHAR-007`/`COMBAT-004` boundary |
| Ch. 10 "Creating High-Level PCs" Step 6 | pp. 130–131 | `CHAR-001`, `CHAR-003` |

This audit deliberately prioritized the objects bearing on the triggering defect and on the most mechanically decisive tables. It does **not** claim `CLUSTER-002` Stage-A completeness.

## 6. Independent Completeness Pass

Started from the RC Table of Contents and Tables Index, not from the packets.

**What the first pass inspected:** Chapter 1 pp. 8–10; Chapter 2 pp. 24–26, 31.

**What it could plausibly have missed:** the remaining per-class Experience Tables; the p. 7 requirements table; the p. 129 maximum-HP tables; Chapter 13 and 19 objects.

**Additional objects found by the second pass:** the Tables Index enumerates a per-class Experience Table and a per-class Saving Throws Table for **every** class (Cleric 14, Dwarf 23, Elf 26, Fighter 16, Halfling 27, Magic-User 19, Thief 22, Druid 29, Mystic 29–30). The Stage-A packets inspected **none** of these as objects. Two of them (Elf, Dwarf) have now been verified and proved structurally decisive for level caps; the remainder are listed in §5 as outstanding.

**Did new material change the evidence picture?** Yes, materially: Finding 4 converts a reported unresolved conflict into a completeness failure, and Finding 1 corrects a citation in an accepted packet. No approved mechanic changed, because none exists.

**Not certified on keyword grounds.** Every claim of verification above names a page that was read as an image.

## 7. Status After This Audit

```text
CHAR-001 Stage-A evidence:  PREVIOUSLY ACCEPTED — COMPLETENESS AUDIT PENDING
CHAR-002 Stage-A evidence:  PREVIOUSLY ACCEPTED — COMPLETENESS AUDIT PENDING
CHAR-003 Stage-A evidence:  PREVIOUSLY ACCEPTED — COMPLETENESS AUDIT PENDING
CHAR-007 Stage-A evidence:  PREVIOUSLY ACCEPTED — COMPLETENESS AUDIT PENDING
                            (citation correction required — Finding 1)

Elf maximum level:          human-adjudicated at 10; not reopened
Elf fixed HP +1 vs +2:      UNRESOLVED, deliberately
BECMI escalation:           void as to authorization (§2)

CLUSTER-002 Stage B:        PAUSED
CLUSTER-002 completeness:   AWAITING HUMAN REVIEW
```
