# CLUSTER-003 Stage-A Remediation Pass 1 (CHAR-004, CHAR-005, EXP-003)

> **✅ ACCEPTED. The second independent completeness / boundary review returned `PASS` on this remediation, with a `CONDITIONAL PASS` on primary-source completeness whose one condition — visual verification of the Nets Table — was closed on 2026-09-14.**
>
> **The boundary question this document prepared has been decided.** The human project owner selected **option B of the governance menu — "change ownership of a narrow mechanic" — for both dependencies**, which is the possibility this document's **§9E** set out. Option A, adding an existing whole Rule Card, was **not** taken:
>
> ```text
> No additional whole Rule Card is required for CLUSTER-003.
>
> Decision 1  CHAR-004 owns mundane equipment legality
> Decision 2  CHAR-005 owns the authoritative movement-rate mechanic,
>             including the Mystic level-dependent MV
> Decision 3  EXP-003 is renamed and narrowed to "Dungeon Movement"
> Decision 4  Chapter 10 high-level equipment material is
>             researched / preserved / NOT V1-WIRED
> Decision 5  condition effects split -- causation elsewhere,
>             movement-rate effect to CHAR-005
> ```
>
> **This document's §3.5 and §4.3 posed the ownership questions; §9 assembled the evidence. Both are preserved exactly as written** — including §9F, the record of what would have gone wrong had the cluster been implemented on the pre-decision boundary. The decisions themselves are recorded at `docs/rules/clusters/CLUSTER-003-equipped-dungeon-movement.md` §3.1, and closure at `docs/rules/evidence/CLUSTER-003-completeness-audit.md` §14.
>
> **§5.3's General Index finding is now a cross-cluster process precedent, `P-001` in `docs/rules/RESEARCH_PROCESS_PRECEDENTS.md`.**
>
> **Nothing in §6's preserved defects and gaps was resolved by the governance decisions.** Ownership moved; the source's contradictions and silences did not.
>
> **Status: ~~`REMEDIATION COMPLETE / RESEARCHER SELF-REVIEW COMPLETE / AWAITING SECOND INDEPENDENT COMPLETENESS / BOUNDARY REVIEW`~~ → `ACCEPTED; STAGE-A RESEARCHER CLOSURE COMPLETE 2026-09-14; AWAITING FINAL INDEPENDENT DEC-0010 COMPLETENESS CERTIFICATION`.**
>
> This artifact records the narrow Stage-A remediation pass performed after the independent completeness review returned **`REMEDIATION REQUIRED`** against the Stage-A package committed at `e26a1e0`. It does **not** supersede the three evidence packets or the completeness audit — it closes the structural inspection those documents declared unfinished, and records what changed as a result.
>
> **Stage B was not begun. No Rule Card was drafted. No alternate source was consulted. No card was added to, removed from, or renamed in `CLUSTER-003`. No production code was written.**

## 0. Governance Correction Accepted

The independent review corrected a reading in the prior researcher report. The prior report said, in substance, that because `CHAR-009` is not one of the three explicitly deferred cards (`CHAR-006`, `CHAR-008`, `EXP-010`), the Mystic `MV` finding did not trigger the boundary-reopen condition.

**That was wrong, and the correction is accepted without reservation.** The approved boundary rule is not restricted to the deferred trio: it fires whenever Stage-A completeness work establishes that an included card has a **mechanically indispensable dependency on any unlanded Rule Card not currently in `CLUSTER-003`** — and the original Stage-A prompt named *"`CHAR-005` genuinely requiring an unlanded class/race movement rule"* as its worked example. The Mystic `MV` finding is that example.

Consequently:

```text
CLUSTER-003 boundary   PROVISIONAL -- reopened, awaiting human governance
CHAR-009               NOT added. A dependency is documented, not adopted.
```

This pass gathers evidence to characterize the dependency precisely. It does not choose among the five governance options (A–E) the review enumerated.

## 1. Method and Access

Same primary source and access method as the original pass — *D&D Rules Cyclopedia* (TSR, 1991), OCR at `archive.org/stream/TSR1071TheDDRulesCyclopedia/TSR-1071-The-DD-Rules-Cyclopedia_djvu.txt` for navigation and prose, IIIF page images at `iiif.archive.org/iiif/TSR1071TheDDRulesCyclopedia$<leaf>/…` for §9.2 visual verification (`leaf = printed_page − 1`).

Neither access stop condition was triggered. **No alternate source was consulted; AD&D was not consulted; `DEC-0011` was not activated.**

**Objects visually verified in this pass (17 new, beyond the 11 in the original pass):**

| # | Object | Printed page | Leaf | Purpose |
|---|---|---|---|---|
| 12 | Ch. 2 "About the Classes" — class-entry structure statement | 13 | n12 | Where restrictions live |
| 13 | Cleric boxed material | 13 | n12 | Equipment legality |
| 14 | **Cleric Experience Table** | 14 | n13 | Movement-column test |
| 15 | Fighter boxed material + **Fighter Experience Table** | 16 | n15 | Both |
| 16 | Magic-User boxed material + **Magic-User Experience Table** | 19 | n18 | Both |
| 17 | Thief boxed material | 21 | n20 | Equipment legality |
| 18 | **Thief Experience Table** + **Thief Special Abilities Table** + Thief Saving Throws Table | 22 | n21 | Movement-column test |
| 19 | Dwarf boxed material | 23 | n22 | Equipment legality |
| 20 | **Dwarf Experience Table** | 24 | n23 | Movement-column test |
| 21 | Elf boxed material | 25 | n24 | Equipment legality |
| 22 | **Elf Experience Table** + Elf Saving Throws Table | 26 | n25 | Movement-column test |
| 23 | Halfling boxed material | 26 | n25 | Equipment legality |
| 24 | **Halfling Experience Table** | 27 | n26 | Movement-column test |
| 25 | Druid boxed material | 28 | n27 | Equipment legality |
| 26 | **Druid Experience Table** + **Mystic Experience Table** | 29 | n28 | Movement-column test |
| 27 | Mystic boxed material (incl. `Maximum Level: 16`) | 29 | n28 | Both |
| 28 | **Ch. 8 "Movement"** (combat sequence) | 103 | n102 | **NEW GOVERNING OBJECT** |
| 29 | **Chapter 19 in full — both pages** | 266–267 | n265, n266 | Variant sweep |

## 2. Complete Chapter 2 Class Inspection (remediation item 1)

**Structural instruments used before reading any class entry:**

- **RC Ch. 2 p. 13, "About the Classes"** (visually verified) states the entry format: *"**Boxed Material:** This box shows **abbreviated** information about the character class for players who are already familiar with the game"*; *"**Class Details:** This text talks about many of the class' special characteristics: its prime requisite, its Hit Dice, **restrictions or advantages with armor and weapons**, and any other significant details."*
  → RC itself assigns equipment restrictions to Class Details, and marks the box as a **summary** (audit class E), so the box is not authoritative over the detail paragraph.
- **RC Ch. 2 p. 13, "Understanding the Tables"** (audit class E) enumerates the columns that appear in class experience tables: **`Level`, `XP`, `Attack Rank` (demihuman tables only), `Spells/Level` (spellcasting classes only)**. **No movement column is listed.**
- **Index to Tables and Checklists (p. 301)** enumerates every named Chapter 2 table: each class has an Experience Table and a Saving Throws Table; the **only** additional per-class tables are `Turning Undead Table` (15), `Thief Special Abilities Table` (22), `Halfling Combat Bonuses Table` (26), `Mystic Unarmed Attack Equivalents Table` (30), and **`Mystic Special Abilities Table` (31)**.
- **General Index (p. 302)**: `Weapon restrictions 14, 17, 19, 21, 23, 25, 26, 28, 29` — **nine page references, every one a Chapter 2 class page. Chapter 4 (pp. 62–66) is not listed under this entry at all.** There is **no** "Armor restrictions" entry; armour is indexed only as `Armor. 67, 68, 230, 242, 243, 251`.

### Per-class disposition

Every row below was read as a complete entry (boxed material **and** Class Details), and every class's tables were located through the Tables Index and inspected.

| Class | Complete entry inspected? | Relevant tables visually inspected? | Equipment restriction? | Movement rule / modifier? | Encumbrance interaction? | Cross-reference? | Disposition |
|---|---|---|---|---|---|---|---|
| **Cleric** (pp. 13–16) | **Yes** — box (n12, visual) + Class Details | **Yes** — Cleric Experience Table (n13): `Level \| XP \| Spells/Level 1–7`; Cleric Saving Throws; Turning Undead Table | **Yes.** Box: *"Armor: Any, plus shield. Weapons: No edged or pointed weapons; all others permitted."* Details add: *"this is forbidden by the cleric's beliefs. **This includes arrows and quarrels.**"* | **None** | **None** | Ch. 4 note `c` marks cleric-usable weapons row by row | **Silent on movement.** The experience table carries no movement column, as "Understanding the Tables" predicts. Equipment restriction is a **principle** (no edged/pointed) whose row-level data is in Ch. 4. |
| **Fighter** (pp. 16–19) | **Yes** — box (n15, visual) + Class Details | **Yes** — Fighter Experience Table (n15): `Level \| XP` only | **No restriction.** *"Armor: Any; shields allowed. Weapons: Any."* | **None** | **None** | Ch. 8 Combat Options | **Silent on movement and unrestricted on equipment.** |
| **Magic-User** (pp. 19–21) | **Yes** — box (n18, visual) + Class Details | **Yes** — Magic-User Experience Table (n18): `Level \| XP \| Spells/Level 1–9` | **Yes, and it conflicts with Ch. 4.** *"Armor: None; no shield permitted. Weapons: **Dagger only.** Optional (DM's discretion): staff, blowgun, flaming oil, holy water, net, thrown rock, sling, whip."* | **None** | **None** | Ch. 4 note `w` | **Silent on movement.** **NEW CONTRADICTION — see §6 Defect 8.** |
| **Thief** (pp. 21–23) | **Yes** — box (n20, visual) + Class Details | **Yes** — Thief Experience Table + **Thief Special Abilities Table** (n21): `Level \| Open Locks \| Find Traps \| Remove Traps \| Climb Walls \| Move Silently \| Hide in Shadows \| Pick Pockets \| Hear Noise`, all percentages | **Yes, and the weapon half exists only here.** *"Armor: Leather armor only; shield not permitted. Weapons: Any missile weapon; any one-handed melee weapon"* (Details: *"two-handed weapons are prohibited"*). Ch. 4's Armor Table carries a `T` note for leather; **Ch. 4's Weapons Table has no thief code at all.** | **No movement rate.** `Climb Walls` is a **special locomotion capability** (percentage, sheer surfaces), not a rate. | **None** | Open Locks requires **thieves' tools** — *"Without lockpicks, he may not use this ability"* → `CHAR-004`. DM may modify Move Silently *"trying to move silently **while running at full speed**"* — a discretionary movement touchpoint | **Silent on movement rate.** Carries a **class-entry-only weapon restriction** and a hard **equipment prerequisite**. |
| **Dwarf** (pp. 23–24) | **Yes** — box (n22, visual) + Class Details | **Yes** — Dwarf Experience Table (n23): `Level \| XP \| Attack Rank` | **Yes, and it exists only here.** *"Armor: Any; shields permitted. Weapons: Any Small or Medium melee weapon; short bows and crossbows permitted, **but longbows forbidden**."* Ch. 4 has `S`/`M`/`L` size codes but **no dwarf code**. | **None** | **None** | Details explicitly send the reader to Ch. 4: *"(If you're unsure as to whether a weapon is small or medium, see the Weapons Table in Chapter 4.)"* | **Silent on movement.** **Complementary, not duplicative**: Ch. 2 supplies the restriction, Ch. 4 supplies the size data it operates on. |
| **Elf** (pp. 24–26) | **Yes** — box (n24, visual) + Class Details | **Yes** — Elf Experience Table (n25): `Level \| XP \| Attack Rank \| Spells/Level 1–5`; Elf Saving Throws | **No restriction.** *"Armor: All; shields permitted. Weapons: Any."* | **None** | **None** | Infravision (60′ in the dark; fails in normal or magical light) → `EXP-006` | **Silent on movement and unrestricted on equipment.** |
| **Halfling** (pp. 26–28) | **Yes** — box (n25, visual) + Class Details | **Yes** — Halfling Experience Table (n26): `Level \| XP \| Attack Rank`; Halfling Combat Bonuses Table (−2 AC vs. larger-than-man-size, +1 missile attack, +1 individual initiative — no movement term), corroborated verbatim by the visually verified box | **Yes, and partly only here.** *"Armor: Any; shield is permitted; **armor must be designed specifically for halflings**"* — Details add *"**Even dwarf-sized armor is too large for them.**"* *"Weapons: Any **Small** melee weapon; short bow; light crossbow"* — **stricter than Ch. 4's `2H`/`HH` notes**, which address only two-handed use. | **None directly.** The armour-fit rule is the trigger for Ch. 4's racial-armour penalty (§6 Defect 7). | **Indirect** — a halfling in human armour must save vs. paralysis each round (Ch. 4 p. 67) | Details send the reader to Ch. 4 for size: *"see the Weapons Table found in Chapter 4."* | **Silent on movement rate.** Carries a **purchase-availability rule** (armour must be halfling-made) that Ch. 4 does not state. |
| **Druid** (pp. 28–29) | **Yes** — box (n27, visual) + Class Details | **Yes** — Druid Experience Table (n28): `Level \| XP \| Spells/Level 1–7`, beginning at level 9; Druid Saving Throws | **Yes, and it includes a COST rule found only here.** *"Armor: Leather armor; shield permitted if made only of wood and leather. Weapons: Any non-edged/non-piercing weapon made with no metal."* Details: *"He can commission craftsmen to make all-wooden versions of appropriate weapons; **they cost 50% more than their counterparts**, but otherwise behave identically."* | **None** | **None** | Ch. 4 note `c`: *"Druids may, too, if they can find a form of this weapon with no metal or stone parts."* | **Silent on movement.** **A pricing mechanic living in a class entry** — squarely `CHAR-004` subject matter. Not reachable at creation (`CHAR-002`, landed). |
| **Mystic** (pp. 29–31) | **Yes** — box (n28, visual, `Maximum Level: 16`) + Class Details | **Yes** — Mystic Experience Table (n28): `Level \| XP`, levels 1–16; Mystic Saving Throws; Mystic Unarmed Attack Equivalents; **Mystic Special Abilities Table (n30): `Level \| AC \| MV \| #AT \| Damage \| Abilities`** | **Yes.** *"Armor: None; shield not permitted. Weapons: Any."* Details: *"Mystics can **never** wear armor of any type, **nor can they ever use protective magical devices** (such as rings, cloaks, etc.)"*; *"Mystics are trained to use all weapons, but not all mystics carry them."* | **YES — the `MV` column.** 120′ (L1) → 320′ (L16). Box lists *"**increased movement**"* as a named special ability. | **UNSTATED** — see §3 | Box → Mystic Special Abilities Table; Acrobatics → Ch. 5 | **The sole class-specific movement rule in Chapter 2.** Also the only class with an **equipment-ownership** framing (§6 Defect 9). |

### Falsification result for remediation item 1

```text
PROPOSITION   "Mystic is the only class with a movement exception."
DISPOSITION   CONFIRMED -- on structural evidence, not on search.

Basis:  (a) RC's own "Understanding the Tables" enumerates the experience-
            table columns and lists no movement column;
        (b) the Tables Index enumerates every named Chapter 2 table, and
            only one -- Mystic Special Abilities -- is a per-level special-
            abilities table;
        (c) all nine experience tables were opened as page images and
            their column headers read directly;
        (d) all nine boxed-material blocks were opened as page images;
        (e) all nine Class Details paragraphs were read in full.
```

This is stated as coverage over the objects inspected. It is stronger than "not located" because RC's own structural statement (a) positively describes the column set.

## 3. Precise Characterization of the Mystic `MV` Dependency (remediation item 2)

### 3.1 What `MV` represents — three RC definitions, all located

| Location | Text | Status |
|---|---|---|
| Ch. 2 p. 31 (Mystic legend) | *"MV: This column shows the mystic's movement rate. **First level mystics move as fast as any other unarmored characters**, but higher level mystics learn to move very, very fast indeed."* | Visually verified |
| **Ch. 6 p. 88** | *"Movement is sometimes written as **'MV 120' (40')'** or 'Movement 120' (40')'."* — first number = feet per **turn** (normal speed); parenthesised number = feet per **round** (encounter speed) | Visually verified |
| **Ch. 14 p. 152 ("Move (MV)")** | *"Usually, on this line, you'll see two numbers, with the second number in parentheses. The first number is the number of feet the monster moves in **one 10-minute turn**; the second number is the movement rate **per round (for encounters)**."* | Located this pass |

**The Mystic table prints a single number per row** — `120'`, `130'`, … `320'` — **with no parenthesised second member** (visually verified, leaf n30). Under all three definitions, a bare `MV` number is the **normal speed in feet per turn**.

### 3.2 Which scales it applies to

| Scale | RC position | Basis |
|---|---|---|
| **Normal (dungeon exploration) speed** | **Directly supplied** by the `MV` column | The bare number is the per-turn value by RC's own notation |
| **Encounter speed** | **Derivable, not printed** — Ch. 6: encounter speed = ⅓ normal; Ch. 8 p. 103 restates it | Necessary mechanical consequence of a stated rule, *not* RC-explicit for the Mystic |
| **Running speed** | **Derivable, and the two statements disagree** — see §6 Defect 10 | Ch. 6 vs. Ch. 8 p. 103 |
| **Dungeon movement** | Follows from normal speed (Ch. 7 p. 91) | Landed `EXP-002` + `EXP-003` |
| **Wilderness / overland** | Follows from normal speed ÷ 5 = miles/day (Ch. 6 p. 88) | Out of cluster |
| **All derived scales** | RC states no Mystic-specific exception to any derivation | Negative finding over the complete Mystic entry |

**Arithmetic observation (recorded as evidence, not as a ruling):** nine of the sixteen `MV` values — 130, 140, 160, 170, 190, 200, 210, 220, 260, 280 — are not divisible by 3, so the Ch. 6 encounter-speed derivation yields non-integral feet (e.g. 130 ÷ 3 = 43⅓). RC gives no rounding rule for this. This is concrete evidence that the composition was not worked through in the source; it is **not** a licence to choose a rounding convention.

### 3.3 Interaction with encumbrance — **UNSTATED after complete inspection**

Both governing objects have now been inspected in full and neither addresses the other:

```text
RC Ch. 6 p. 88    Character Movement Rates and Encumbrance Table
                  six cn bands -> normal / encounter / running speed
                  prose: "Any character will have a movement rate of
                  '120' (40')' unless he is weighed down by a lot of gear."

RC Ch. 2 p. 31    Mystic MV: 120' at L1 ... 320' at L16
                  legend: "First level mystics move as fast as any other
                  UNARMORED characters"
```

Searches performed for a reconciling statement, all returning nothing: `movement rate` read at every whole-source occurrence including out-of-domain hits; `unarmored`; `MV`; `encumbrance` (93 occurrences); the complete Mystic entry; Ch. 19's Mystic sub-entry; the General Index entries `Encumbrance .63, 88 / Effect on movement . 88` (**only two locations, both inspected**) and `Movement . 87, 88, 103, 263, 264` (all five inspected or dispositioned).

**Disposition: `RETAINED AS GENUINE SOURCE AMBIGUITY` — and now defensible as such**, because §10.2.2 case 3's conditions are met: all relevant governing objects inspected, contradictory/silent passages recorded verbatim, and no unfinished inspection disguised as ambiguity.

**Two readings exist in the source's own terms, and neither is adopted here:**

1. `MV` is the Mystic's **unencumbered baseline**, replacing the 120′ of the `0–400 cn` band, with the encumbrance table's bands then applying as reductions. Textual support: the legend's word *"unarmored"*, which is an encumbrance-flavoured qualifier.
2. `MV` is a **flat movement rate** for the Mystic, as Suit Armor's `30' (10')` is a flat rate for its wearer. Textual support: the table prints an absolute number, and the box calls it a special ability.

### 3.4 Does any other part of the Mystic entry or another chapter resolve it?

**No.** Checked and recorded:

- Mystic Class Details, read in full — no encumbrance statement.
- Mystic Acrobatics (p. 31) — addresses **terrain**, not encumbrance.
- Mystic "Higher Experience Levels" — the *"armor class, **movement rate**, number of attacks… no longer improve"* statement is in **Ch. 19's variant** for advancing Mystics past 16th level. Since the **visually verified box gives `Maximum Level: 16`** and the Mystic Experience Table stops at 16, **the table's sixteen rows are complete for standard V1 rules**, and the Ch. 19 statement belongs to a variant `DEC-0008` declined. *This removes one item the original pass had listed as open.*
- Ch. 8 p. 103, Ch. 14 p. 152 — define the notation; neither mentions encumbrance.
- Chapter 19 read in full (both pages visually verified) — no encumbrance or movement variant exists anywhere in it.

### 3.5 Ownership characterization — evidence only, no decision

```text
Does correct CHAR-005 operation require...

1. the whole CHAR-009 contract?
   NOT SUPPORTED BY THE EVIDENCE. CHAR-009 as scoped in INVENTORY.md
   covers class special abilities and racial abilities/limitations for
   the whole roster. CHAR-005 consumes exactly ONE datum from it: a
   per-class, per-level base movement rate that exists for ONE class.
   Nothing else in CHAR-009's scope is reachable from CHAR-005.

2. only a class-provided base-movement VALUE?
   STRONGLY SUPPORTED. What CHAR-005 needs is a single number keyed by
   (class, level), defaulting to 120' for the other eight classes. The
   Mystic Special Abilities Table is its only non-default source in the
   whole of RC.

3. only a narrow Mystic-specific movement RULE?
   SUPPORTED, and slightly wider than (2): besides the value, a rule is
   needed for how it composes with encumbrance -- and RC does not supply
   one (SS3.3). So a narrow rule cannot be lifted whole from the source;
   part of it would have to come from Stage B or human adjudication.

4. some other existing owner?
   POSSIBLE, NOT ESTABLISHED. INVENTORY.md contains no entry that
   currently owns "base movement rate by class". CHAR-005 is titled
   "Encumbrance & Movement Rate", which on its face could own a
   class-keyed base-rate lookup; CHAR-009 currently owns the Mystic's
   class abilities, of which RC's own boxed material names "increased
   movement" as one.
```

**The decision among (1)–(4) is the human governance question this pass exists to inform. It is not made here.**

## 4. `CHAR-004` / Class Equipment-Legality Result (remediation item 3)

### 4.1 Classification of every restriction located

| Class | (A) Duplicated in Ch. 4 **and** class entry | (B) Ch. 4 only | (C) **Class entry only** | (D) Contradiction | (E) Cross-reference |
|---|---|---|---|---|---|
| Cleric | Armour ("any, plus shield" ↔ Ch. 4 prose naming clerics); weapon permission per row via note `c` | Row-level `c` marks | The **principle** *"no edged or pointed weapons… includes arrows and quarrels"* | — | Ch. 4 `c` implements Ch. 2's principle |
| Fighter | Armour and weapons unrestricted in both | — | — | — | — |
| Magic-User | Armour ("none" ↔ Ch. 4 *"Magic-users… can use none of these armor types"*) | Note `w` set | *"**Dagger only**"* as an **unconditional** base permission | **YES — §6 Defect 8** | Note `w` ↔ optional list |
| Thief | Armour (leather; Ch. 4 Armor Table note `T`) | `T` note | **Weapons entirely**: *"any missile weapon; any one-handed melee weapon"*; two-handed prohibited. **Ch. 4's Weapons Table has no thief code.** | — | — |
| Dwarf | — | Size codes `S`/`M`/`L` | **Weapons entirely**: Small/Medium melee only; **longbows forbidden**; short bows and crossbows allowed | — | Ch. 2 → *"see the Weapons Table in Chapter 4"* for size |
| Elf | Unrestricted in both | — | — | — | — |
| Halfling | Two-handed use (Ch. 4 notes `2H`/`HH`) | `2H`/`HH` | **Stricter weapon list** (any Small melee; short bow; light crossbow) and the **armour-fit rule** (*"must be designed specifically for halflings… Even dwarf-sized armor is too large"*) | — | Ch. 2 → Ch. 4 Weapons Table for size |
| Druid | Weapon material via note `c` | `c` clause | **+50% cost** for commissioned all-wooden weapons; shield *"made only of wood and leather"* | — | Ch. 4 `c` ↔ Ch. 2 material rule |
| Mystic | Armour ("none" ↔ Ch. 4 prose) | — | **Protective magical devices prohibition** (rings, cloaks) → also `TREAS-004` | — | — |

### 4.2 Answer

```text
Can CHAR-004 determine legal starting equipment without an unlanded rule?

                    NO
```

**Evidence, three independent lines:**

1. **Column (C) is non-empty for five of nine classes.** Thief weapons, Dwarf weapons, Halfling weapons and armour-fit, Druid weapon pricing, and Mystic protective-device prohibition are stated **only** in Chapter 2. A `CHAR-004` implementation reading only Chapter 1, Chapter 4 and Chapter 13 would permit a thief a two-handed sword, a dwarf a longbow, and a halfling a Medium weapon.
2. **RC's own General Index routes the subject away from Chapter 4.** `Weapon restrictions 14, 17, 19, 21, 23, 25, 26, 28, 29` — nine class pages, Chapter 4 absent.
3. **RC's own structural statement.** Ch. 2 p. 13: Class Details carries *"restrictions or advantages with armor and weapons"*; and Ch. 1 p. 8 instructs *"Before you go shopping, be sure you have read the full description of your character class."*

### 4.3 Which kind of dependency this is

```text
whole-card dependency         NOT SUPPORTED
narrow ownership overlap      SUPPORTED for armour
duplicated RC authority       SUPPORTED for armour, NOT for weapons
unresolved ownership conflict SUPPORTED -- and now sharper than before
```

The picture is **asymmetric, and that asymmetry is the finding**:

- **Armour permissions are genuinely duplicated** (Ch. 4 p. 67 prose names all nine classes; each class entry restates it). Either location alone would serve. This is duplicated RC authority — an ownership choice, not a dependency.
- **Weapon permissions are not duplicated.** Chapter 4 supplies *data* (per-row `c`/`w`/`2H`/`HH` marks and `S`/`M`/`L` sizes); Chapter 2 supplies the *predicates* that consume that data, and for Thief and Dwarf supplies them **exclusively**. Chapter 2 even cross-references Chapter 4 for the size data — the two are **complementary by RC's own construction**.
- **One pricing rule (Druid, +50%) sits in a class entry**, which is `CHAR-004` subject matter by any reading.

**Governance question enabled, not answered:** is `CHAR-009` an incoming dependency of `CHAR-004`, or is the correct correction to move the narrow weapon/armour-permission predicate into `CHAR-004` (leaving `CHAR-009` the rest of the class-abilities contract)? Both are consistent with the evidence. Rules were **not** moved between cards.

> **ANSWERED 2026-09-14 by human governance Decision 1 — the second reading.** `CHAR-004` canonically owns mundane equipment legality; `CHAR-009` retains the rest of the class-abilities contract and may describe these restrictions as class features **without** becoming a second canonical implementation owner. **`CHAR-009` is not an incoming dependency of `CHAR-004`.** Magic-item-specific restrictions remain with `TREAS-004`.

## 5. Newly Completed Structural Inspection (remediation items 4–7)

### 5.1 Chapter 19 — inspected in full (item 4)

**Chapter 19 is exactly two printed pages (266–267). Both were read in OCR in full and both were visually verified as whole pages.** Complete section list:

```text
1. Ability Scores and Saving Throws
2. Death in the Campaign                    <- not in the TOC sub-headings
3. Keeping Characters Alive                 <- not in the TOC sub-headings
4. Demihuman and Mystic Experience Levels   (Dwarf / Elf / Halfling / Mystic)
   + Extended Experience Table
5. Nonlethal Combat
```

```text
optional encumbrance systems          NONE
simplified encumbrance                NONE
movement variants                     NONE
armor movement variants               NONE
dungeon movement variants             NONE
relevant optional character movement  NONE
```

**One movement-adjacent item exists** and is recorded rather than discarded: the Mystic sub-entry restates that above 16th level *"the mystic's armor class, **movement rate**, number of attacks, and hand-to-hand damage no longer improve."* This belongs to the variant that `DEC-0008` **declined for V1**, and — as §3.4 notes — it is moot for standard rules because the Mystic's maximum level **is** 16.

> The original pass's caveat was justified: the TOC lists three Chapter 19 sub-headings and the chapter contains five sections. Inferring absence from the TOC alone would have been the error `DEC-0010` prohibits. **Absence is now asserted on complete inspection, not on a search.** This task is source completeness, not variant selection: **no optional rule is proposed for V1.**

### 5.2 Chapter 17 — inspected (item 5)

`Designing Adventures and Dungeons` (259–261) and `Running Adventures` (261–262) read; `Designing the Setting` (256–257) read after the General Index flagged `Mapping . 5, 148, **256, 257**`.

| Material | Bearing | Disposition |
|---|---|---|
| **Dungeon map scale** — *"If the site is underground (such as a dungeon), use graph paper (with each square normally representing a 10' × 10' area, **or any other scale you prefer**)"* | **YES — material to `EXP-003`** | **NEW.** A **third** presentation of the map scale, and the only one that makes it explicitly DM-variable. Ch. 6 p. 87 gives "one square representing 10'"; Ch. 13 p. 148 gives the 10′×10′ standard corridor. **The 10′ square is a default, not a constant.** |
| `Designing the Setting` / `Designing the Map` (256–257) | No | **Campaign-world** map design — hex paper, terrain *types* for world-building. Not dungeon movement, not a mapping mechanic. Out of scope, reason verified. |
| Room Contents Table (261), Unguarded Treasure Table (261) | No | Dungeon stocking / treasure — `EXP-007`, `TREAS-*`. |
| "Special" room contents incl. **Movement** (a room, stairs, door or item that moves) and **Map Change** (a shifting wall cutting off the exit) | No | **Dungeon tricks**, resolved by surprise rolls — `EXP-007`. They affect *the map*, not *movement rate*. Recorded so a reviewer can see they were seen and routed. |
| **Pre-Game Checklist (262)** — item 4 *"Are all the characters ready to go and **equipped for the adventure**?"*; item 5 *"Have the players chosen a **caller and a mapper**? Do they have a piece of graph paper and a pencil, to map with?"* | Weakly | **A fourth presentation of the mapper/caller roles**, and a play-setup check. **No mechanic.** Minor tension with Ch. 5's *"it's not a game rule that players have to use"* — the checklist is DM advice, Ch. 5 is the rule statement. |

**No Chapter 17 character-scale movement rule was located.**

### 5.3 General Index — inspected as a completeness instrument (item 6)

Every entry capable of locating relevant material was read and its page references followed.

| Index entry | References | Followed to | Result |
|---|---|---|---|
| `Encumbrance .63, 88` / `Effect on movement . 88` | 2 | Ch. 4 legend, Ch. 6 table | **Confirms only two encumbrance locations exist.** Both already inspected. |
| **`Movement . 87, 88, 103, 263, 264`** | 5 | Ch. 6; **Ch. 8 p. 103**; Ch. 18 | **`p. 103` WAS NOT INSPECTED IN THE ORIGINAL PASS. It is a governing object — §5.5.** 263–264 = Ethereal/Elemental planes, out of scope. |
| `Running speed. 88, 103` | 2 | Ch. 6; **Ch. 8 p. 103** | Same new object. |
| `Movement` sub-entries: Aerial travel rates 90; Character movement rates 88; Monster movement rates 88, **152**; Overland movement rates 88; Water travel rates 89, 90 | — | Ch. 14 p. 152 | `Move (MV)` definition located — §3.1. Others out of cluster. |
| **`Weapon restrictions 14, 17, 19, 21, 23, 25, 26, 28, 29`** | 9 | All nine Ch. 2 class pages | **Decisive for §4.** Chapter 4 not listed. |
| `Mapping . 5, 148, 256, 257` / `Map scales.87` | 5 | Ch. 5 roles; Ch. 13 p. 148; Ch. 17 pp. 256–257; Ch. 6 p. 87 | **`p. 5` corrects a citation**: "Mapping and Calling" is in the front matter/Setting Up, **not** Chapter 1. 256–257 → §5.2. |
| `Blindness . 150, **154**` | 2 | Ch. 13 p. 150; **Ch. 14 p. 154** | Ch. 14 adds a **cause** — *"fighting in the dark without infravision can result in blindness"* (→ `EXP-006`) — and explicitly refers back: *"See 'Special Character Conditions' in Chapter 13 for more details."* **p. 150 remains the governing location.** |
| `Terrain. 119, 153` | 2 | Ch. 9 War Machine; **Ch. 14 p. 153** | p. 119 = mass-combat battle modifiers, out of scope. **p. 153 → the `Charge` rule, a NEW finding — §5.5.** |
| `Starvation.150`, `Stunning.150`, `Swimming.89`, `Exhaustion.88`, `Speed.88`, `Movement rate .88`, `Terrain effects on movement . 88`, `Climbing . 145`, `Equipment . 8, 62-74, 147`, `Adventuring gear .68-70`, `Armor. 67, 68, 230, 242, 243, 251`, `Barding.68`, `Torch . 62, 66, 69, 70`, `Infravision . 24, 25`, `Time (rounds, turns, days) .87`, `Turns.87, 91`, `Timekeeping.149` | — | — | All already inspected or already routed to another card. **No new object.** |
| Searched for and **absent from the index**: `Marching order`, `Formation`, `Load` (as a character concept), `Carrying capacity`, `Walking`, `Armor movement` | 0 | — | Strengthens §8 Challenge 9. `Load` exists only as a Ch. 14 monster statistic. |
| `Armor restrictions` | **no such entry** | — | Asymmetry recorded: RC indexes *weapon* restrictions per class but not *armour* restrictions — consistent with §4.3's finding that armour is duplicated and weapons are not. |

### 5.4 Chapter 10 high-level character creation — inspected (item 7)

`Creating High-Level Player Characters` (pp. 129–131) read in full.

```text
Step 5: Find Current Cash Total
    "Assign each new character cash equal to 1% of his experience points
     in gold pieces. THIS MONEY IS NOT USED FOR PURCHASING ITEMS. It is
     the amount the character has left over WHEN FULLY EQUIPPED."
    DM may vary from 1/10 of 1% up to 25%.

Step 7: Choose Normal Equipment
    "A high-level character should be given ANY NONMAGICAL ITEMS HE
     DESIRES, WITHIN REASON."
    "Note that characters keep many common supplies IN STORAGE AND DON'T
     CARRY THEM AROUND ON ADVENTURES."
    DM may forbid or limit large or unusual items (sailing vessels,
     castles, etc.).
    Alternate Equipping Method: a cash amount (e.g. 20,000 gp total, or
     1,000 gp per experience level) for nonmagical supplies, WITH DM-SET
     PRICES.

Step 8: Find Magical Equipment
    Method One (Buying): gp equal to XP, magical items only, priced from
     the Magical Item Price Ranges Table (p. 131) or a rule-of-thumb
     formula.
    Method Two (Assortment): DM-selected counts, strengths rolled on the
     Chapter 16 tables.
```

| Question | Answer | Evidence |
|---|---|---|
| Different starting money? | **YES** | 1% of XP in gp, not `3d6 × 10` |
| Different equipment acquisition? | **YES** | Granted by the DM, explicitly **not purchased**; or an alternate cash method at **DM-set prices** |
| Equipment allowances? | **YES** | Step 7 alternate method; Step 8 Method One |
| Magic-item assumptions? | **YES** | Two methods + a price table, noted as *"somewhat inflated"* versus Chapter 16 |
| Class-specific equipment packages? | **NO** | Step 7 is class-agnostic; Step 8's worked example is class-flavoured but not a package |
| **Encumbrance implications?** | **YES — and materially** | *"characters keep many common supplies in storage and don't carry them around on adventures"* is **the only RC statement distinguishing equipment OWNED from equipment CARRIED** — exactly the distinction `CHAR-005` needs, since it totals carried `cn` |

**Ownership observation, raised not decided.** Chapter 10's high-level creation procedure is **already partly landed**: `CHAR-001` §5 owns and implements Step 2's two ability-score methods (`roll_and_keep_six`, `assign_scores`, `roll_point_allocation_total`, `allocate_points`), verified in `CLUSTER-002`. So this pathway **is** in the V1 creation route. That makes the gap concrete rather than hypothetical:

```text
A high-level character generated by landed CHAR-001 SS5 code today has
NO landed rule for starting money or starting equipment, because
Chapter 10 Steps 5, 7 and 8 are owned by no card.
```

Whether those steps belong to `CHAR-004`, to a separate high-level-creation responsibility, or are out of the intended V1 pathway is a **human governance question**. `CHAR-004` was **not** expanded.

### 5.5 Two genuinely new governing objects the original pass missed

**NEW OBJECT 1 — RC Ch. 8 p. 103, "Movement" (in the combat sequence). Visually verified, leaf n102.**

> *"You learned about movement in Chapter 6. Here are some additional details:*
> • ***Encounter Speed:** A character or monster may move his full encounter speed movement (1/3 normal movement in one round) **and still make his attacks this round**.*
> • ***Running Speed:** A character or monster may move his full running speed movement (**3 × normal movement**) this round **if he is not already engaged in combat but cannot attack if he does so**.*
> • ***Normal Speed:** A character's normal speed is **never used during the combat sequence**.*
> *Simple, quick actions such as drawing a new weapon do not subtract from a character's movement score; the DM may choose to deduct some of a character's movement for the round if he performs any more complicated maneuvers. **Standing up after a fall, however, does count as an action in a combat round.***"

Why it matters:

1. RC flags it itself as *"additional details"* to Chapter 6 — an **additive duplicate presentation** (audit class I), not a restatement.
2. It adds a **hard scale boundary**: normal speed is *never* used in combat. That positively bounds `EXP-003` — normal speed is the exploration-turn rate, full stop.
3. It adds **movement-budget rules** (free vs. costly actions; standing up).
4. It contains a **factor-of-3 inconsistency** with Chapter 6 — §6 Defect 10.

**This object was reached only through the General Index.** The original pass's whole-source `movement rate` sweep did not surface it because the section is headed simply "Movement" and sits inside the combat-sequence description. This is the clearest single vindication of the independent reviewer's `FAIL — unfinished structural inspection`.

**NEW OBJECT 2 — RC Ch. 14 p. 153, "Charge" (Special Attacks).**

> *"If a monster can run toward its opponent for 20 yards (**20 feet indoors**), it inflicts double damage if it hits. **A monster cannot charge in certain types of terrain: broken, heavy forest, jungle, mountain, swamp, etc.**"*

Why it matters: this is **the first located RC rule in which terrain constrains movement at the round scale, with the indoor case explicitly contemplated.** It is a monster-side combat rule (`COMBAT-*`/`MON-*`), and it constrains an *action* (charging), not a *rate* — so it does not close `EXP-003`'s Special-Terrain gap. But it **qualifies** the original pass's negative finding and must be on the record. It also supplies the closest located analogue to the terrain vocabulary Mystic Acrobatics uses ("broken").

## 6. Re-tested Source Defects and Gaps

| # | Question | Outcome after remediation | Evidence |
|---|---|---|---|
| 1 | **Belt pouch** — `2*` empty enc + `Capacity 50 cn` vs. footnote *"a fully filled belt pouch has an encumbrance of **55 cn**"* | **STILL CONTRADICTORY.** `55 cn` occurs exactly once in the whole source; no reconciling text exists. `2 + 50 = 52`. | Both sides visually verified, leaf n68; whole-source `55 cn` sweep |
| 2 | **Suit Armor** — `Enc 750 cn` → `90' (30')` by the p. 88 table vs. its own *"movement rate is `30' (10')`"* | **STILL CONTRADICTORY.** One new sentence located — *"If a fighter in suit armor is **mounted and has assistance from others**, the disadvantages of encumbrance, slow movement, and surprise can be minimized"* — which acknowledges both encumbrance *and* slow movement as separate disadvantages but reconciles neither. No override language ("regardless of encumbrance", "instead of") exists. | Three objects visually verified (n66, n67 prose, n87) |
| 3 | **Starvation Table** movement column non-monotonic (`No Penalty / ×¾ / ×½ / ×¾`) | **STILL A PRINTED DEFECT.** No clarifying prose located. | Visually verified, leaf n149 |
| 4 | **"Clothes, plain"** prints `***` (the quiver footnote) where other clothing rows print `**` | **STILL A TYPOGRAPHIC DEFECT.** The Clothes description (p. 69) carries no encumbrance statement that would explain it. | Visually verified, leaf n68 |
| 5 | **Mystic `MV` × encumbrance** composition | **STILL UNSPECIFIED — but the classification is now defensible.** Both governing objects inspected in full; Ch. 19, Ch. 8, Ch. 14 and the General Index all checked for a reconciling statement. `RETAINED AS GENUINE SOURCE AMBIGUITY` under §10.2.2 case 3. One sub-item **closed**: the "above 16th level" question is moot, since the Mystic's maximum level is 16 (visually verified box). | §3.3, §3.4 |
| 6 | **Mystic Acrobatics** references a rough/broken-terrain effect whose governing rule was not located | **STILL A POSSIBLE GAP, now qualified.** RC *does* state one terrain constraint that applies indoors — the Ch. 14 Charge prohibition in "broken… terrain" (§5.5 Object 2) — but it prohibits an action rather than modifying `encounter speed and running speed`, which is what Acrobatics negates. **The referent of the Acrobatics text remains unlocated.** | §5.5 |
| 7 | **Racial armour movement reduction** — asserted but unquantified | **CLASSIFICATION CHANGED — NO LONGER A GAP.** Reading the **complete** sentence rather than the clause: *"**The DM can impose penalties** on a character who wears the armor of a different race. For example, an elf would find a dwarf's chain mail awkward and heavy (for an additional reduction to movement beyond what the armor's encumbrance calls for)…"* The movement reduction is an **example of a penalty a DM may elect**, not a rule RC failed to quantify. **RC delegates this by design.** The original pass quoted the parenthetical without its governing sentence. | Ch. 4 p. 67, read in full |
| 8 | **NEW — Magic-user dagger permission** | **NEW CONTRADICTION.** Ch. 2 p. 19 (visually verified): *"Weapons: **Dagger only.** Optional (DM's discretion): staff, blowgun, flaming oil, holy water, net, thrown rock, sling, whip."* Ch. 4 note `w` (visually verified): *"Magic-users may use this weapon **at the DM's discretion**."* Ch. 4's Weapons Table marks **both dagger rows** `t,w,S` — i.e. Chapter 4's `w` set is exactly Chapter 2's optional set **plus the dagger**. Chapter 4 alone would make a magic-user's dagger discretionary; Chapter 2 makes it unconditional. | Leaves n18, n61, n62 |
| 9 | **NEW — Mystic "personal possessions"** | **NEW INTERNAL TENSION.** Ch. 2 p. 30: *"Mystics have a lot of special abilities, which help compensate for their inability to wear armor **or own personal possessions**."* But the Mystic entry's operative rules are only: never wear armour; never use protective magical devices; XP from treasure only if donated; tithe 10%. **No rule bars a mystic from owning or buying ordinary equipment**, and a mystic still rolls `3d6 × 10` gp. Recorded as flavour framing the entry's own rules do not implement. Bears on `CHAR-004`. | Mystic entry read in full |
| 10 | **NEW — running speed stated twice, with a factor-of-3 discrepancy** | **NEW CONTRADICTION.** Ch. 6 p. 88 (visually verified): running speed *"is equal to their normal speed in feet per round (rather than turn) **or three times their encounter speed**"* → 120′/round for a 120′ (40′) character. Ch. 8 p. 103 (visually verified): *"his full running speed movement (**3 × normal movement**)"* → 360′/round if "normal movement" bears the meaning it carries in the immediately preceding bullet (*"encounter speed… 1/3 normal movement"*). The same two-word phrase is used with two different referents in one three-bullet list. | Leaves n87, n102 |
| 11 | **NEW — standing up, stated twice** | **MINOR TENSION.** Ch. 13 p. 150: *"A character on the ground takes **one round of movement** to stand up."* Ch. 8 p. 103: *"Standing up after a fall… does count as **an action** in a combat round."* Movement-budget cost vs. action cost. | Leaves n102, n149 |
| 12 | **NEW — dungeon map scale is a default, not a constant** | **CLASSIFICATION CHANGED.** Ch. 17 p. 260 adds *"or any other scale you prefer"* to the 10′ square. Three presentations now located (Ch. 6 p. 87, Ch. 13 p. 148, Ch. 17 p. 260). | §5.2 |

**None of these is resolved, and no alternate source was consulted for any of them.**

## 7. `EXP-003` Scope Re-test (remediation item 8)

Re-tested against the complete evidence, including the three newly inspected regions.

### Dungeon Movement

```text
governing object located?    YES
independent procedure?       YES
mechanical effect?           YES
ownership supported by RC?   YES
```

- **Governing objects:** Ch. 7 p. 91 *"Exploration and the Game Turn"* + the **Game Turn Checklist**; Ch. 6 pp. 87–88 for the rate, the foot/yard rule and the map scale; **now also Ch. 8 p. 103**, which bounds the scale from the other side — *"A character's normal speed is **never used during the combat sequence**."*
- **Mechanics:** spend normal speed against 10-minute turns; feet indoors; 10′ per map square **by default**; the rate already includes mapping, peeking around corners and resting.
- **Unchanged by remediation, and now better bounded.**

### Mapping

```text
governing object located?    YES (four presentations)
independent procedure?       NO
mechanical effect?           NONE -- and RC states the cost is already
                             inside the movement rate
ownership supported by RC?   NO independent mechanic exists to own
```

Four presentations now located and all read in full: **RC p. 5 "Mapping and Calling"** (the General Index corrected this citation from Chapter 1), Ch. 7 p. 91 checklist step 3b, **Ch. 13 p. 148 "Mapping"**, and **Ch. 17 p. 262 Pre-Game Checklist**. None contains a die roll, a time cost, or a failure state. Ch. 6 p. 88 states normal speed *"includes many assumed actions—**mapping**, peeking around corners, resting."*

**Finding unchanged and now stronger** — the two additional presentations found in remediation are also mechanic-free.

### Special Terrain

```text
governing object located?    NO dungeon-turn-scale movement object
independent procedure?       NO
mechanical effect?           NONE on movement rate or turn cost.
                             ONE action prohibition located (Ch. 14 Charge),
                             owned elsewhere.
ownership supported by RC?   NO
```

**Qualified by remediation, not overturned.** The complete picture:

| RC text | What it does | Owner |
|---|---|---|
| Ch. 6 p. 88 bounding sentence — terrain *"makes no difference to the combat round or the 10-minute turn"* | Positively excludes terrain at both `EXP-003` scales | — |
| Terrain Effects on Movement Table + Traveling Rates by Terrain Table (p. 88, both visually verified) | Modify **miles per day** | wilderness movement |
| Ch. 7 p. 98 — a dungeon corridor *"riddled with doors and side passages"* is *"difficult terrain"* | Modifies an **evasion chance** | **`ENC-005`** |
| **Ch. 14 p. 153 Charge — NEW** — *"A monster cannot charge in certain types of terrain: broken, heavy forest, jungle, mountain, swamp"*, with *"20 yards (**20 feet indoors**)"* | **Prohibits an action** at round scale, indoors included | `COMBAT-*` / `MON-*` |
| Ch. 2 p. 31 Mystic Acrobatics — crossing *"rough, broken terrain at no modification to his movement rate… only affects his **encounter speed and running speed**"* | **Presupposes** a rate modifier RC never publishes | unowned — §6 item 6 |

**No rate or turn-cost modifier exists in the objects inspected. The negative is now supported by RC's own positive exclusion, by both terrain tables, by an exhaustive Tables Index sweep, and by a General Index sweep — not by a failed search.**

### Verdict

```text
CARD TITLE / RESPONSIBILITY BOUNDARY REVIEW REQUIRED
```

Two of three named sub-responsibilities are not independent mechanics. **The card was not renamed.** No governance in this repository authorizes a researcher to rename an inventory entry, so the flag is raised and the title left alone.

## 8. Falsification Results — the nine required challenges

| # | Proposition challenged | Evidence | Disposition |
|---|---|---|---|
| 1 | **Mystic is the only class with a movement exception** | All nine experience tables opened as page images; all nine boxed blocks opened as page images; all nine Class Details read in full; Tables Index enumerates every Ch. 2 table; "Understanding the Tables" enumerates the experience-table column set and lists no movement column | **CONFIRMED** on structural evidence |
| 2 | **`CHAR-005` requires the entire `CHAR-009` rule rather than only a narrow class-provided movement datum/rule** | `CHAR-005` consumes exactly one datum — a `(class, level) → base rate` value, non-default for one class — plus a composition rule RC does not supply | **REJECTED as stated.** The whole-card reading is not supported; a narrow datum plus an unsupplied composition rule is. **Ownership decision not made.** |
| 3 | **`CHAR-004` requires `CHAR-009` for equipment legality** | Column (C) of §4.1 is non-empty for five of nine classes; the General Index routes `Weapon restrictions` to nine class pages and not to Chapter 4; Ch. 2 p. 13 assigns restrictions to Class Details | **CONFIRMED that an unlanded rule is required.** **REJECTED that it must be `CHAR-009` specifically** — a narrow ownership correction is equally consistent. Armour is duplicated; weapons are not. |
| 4 | **Chapter 19 contains no relevant encumbrance/movement option** | Two printed pages, both visually verified and both read in OCR in full; five sections enumerated; the TOC's three sub-headings were incomplete, which is why inspection was required | **CONFIRMED on complete inspection.** One movement-adjacent item (the Mystic 16th-level cap) recorded, belonging to a declined variant and moot under standard rules. |
| 5 | **Chapter 17 contains no relevant character-scale movement rule** | pp. 256–257 and 259–262 read; Room Contents and Unguarded Treasure tables and the Pre-Game Checklist inspected | **CONFIRMED for movement rules.** **QUALIFIED:** Ch. 17 p. 260 materially changes the map-scale finding — 10′ per square is explicitly *"or any other scale you prefer."* |
| 6 | **High-level character creation introduces no `CHAR-004` mechanic relevant to V1** | Ch. 10 Steps 5, 7, 8 + Magical Item Price Ranges Table read in full; `CHAR-001` §5 already lands Step 2 of the same procedure | **REJECTED.** Different starting money (1% of XP), equipment by grant rather than purchase, an alternate cash method, two magic-item methods, and the **only RC owned-vs-carried distinction**. Relevance to V1 is established by `CHAR-001` §5 already being landed. **`CHAR-004` not expanded.** |
| 7 | **`EXP-003` really owns an independent mapping procedure** | Four presentations located and read in full; Ch. 6 p. 88 prices mapping into the rate | **REJECTED.** No die, time cost, or failure state anywhere. |
| 8 | **`EXP-003` really owns an independent special-terrain procedure** | Five terrain-related texts catalogued in §7; two terrain tables visually verified as per-day; RC's own bounding sentence | **REJECTED, with one qualification** — Ch. 14's Charge prohibition is a genuine indoor terrain constraint, but it is an action prohibition owned by `COMBAT-*`/`MON-*`, not a rate or turn-cost rule. |
| 9 | **`EXP-010` remains unnecessary for executing dungeon movement** | Ch. 5 *"Mapping and Calling"* read in full — *"Any player can be the mapper or caller"*, *"**it's not a game rule** that players have to use"*; `marching order` occurs once in the whole source, in **NPC party generation**; `single file` / `front rank` / `order of march` / `abreast` return nothing; **the General Index has no `Marching`, `Formation`, or `Carrying capacity` entry**; the Tables Index has no formation table | **CONFIRMED.** `EXP-010` remains deferred and un-researched; the review's `DISPROVED` stands, now additionally supported by a General Index sweep. |

## 9. Boundary-Reopen Evidence Package

> Prepared for human governance. **No boundary is chosen here.**

**A. Is there an indispensable unlanded dependency?**
**YES — two, and they are different in kind.**

**B. Which card(s) exhibit it?**
`CHAR-005` (movement) and `CHAR-004` (equipment legality). `EXP-003` exhibits none: its inputs are `CHAR-005` and landed `EXP-002`.

**C. What exact mechanic crosses the boundary?**

```text
CHAR-005   A per-class, per-level BASE MOVEMENT RATE.
           Non-default for exactly one class in the whole of RC:
           Mystic MV, 120' at L1 rising to 320' at L16
           (RC p. 31, visually verified).
           Default 120' (40') for the other eight.
           PLUS an unsupplied composition rule for MV x encumbrance.

CHAR-004   A per-class WEAPON-PERMISSION PREDICATE, stated only in the
           Chapter 2 class entries for Thief (missile + one-handed melee;
           no two-handed), Dwarf (Small/Medium melee; no longbows),
           Halfling (Small melee; short bow; light crossbow), and a
           Druid +50% PRICING rule for commissioned wooden weapons.
           Armour permissions are duplicated in Chapter 4 and are NOT
           a dependency.
```

**D. Is there evidence that the whole external Rule Card is required?**
**No.** For `CHAR-005`, one datum plus one composition rule. For `CHAR-004`, a permission predicate and one pricing rule. `CHAR-009`'s scope — class special abilities and racial abilities/limitations across the roster, plus the Ch. 13 thief-skill touchpoint — is far larger than either, and nothing else in it is reachable from these two cards.

**E. Could a narrower ownership correction solve it?**
**The evidence is consistent with that, and with at least three shapes of it.** Stated as options for the human decision, not as a recommendation:

- a `(class, level) → base movement rate` datum owned by `CHAR-005` itself, since the card is titled *"Encumbrance & **Movement Rate**"*;
- a per-class weapon/armour-permission predicate owned by `CHAR-004`, since Chapter 4 is where the data it consumes lives and since one of the rules is a **price**;
- both left in `CHAR-009` with `CHAR-004` and `CHAR-005` declared to depend on it — which makes `CLUSTER-003` un-implementable until `CHAR-009` lands.

Note that RC's own boxed material names *"increased movement"* as one of the Mystic's **special abilities**, which is textual support for the `CHAR-009` reading; and RC's own index routes `Weapon restrictions` to class pages, which is textual support for the same reading on the equipment side. The counter-consideration is scope: both are narrow slices of a large card.

**F. Would the current three-card cluster produce incorrect behavior for any required V1 character if implemented unchanged?**

**YES — demonstrably, for at least four of the nine required V1 classes.**

```text
MYSTIC    A 10th-level mystic carrying no gear would be assigned 120' (40')
          by the CHAR-005 table. RC p. 31 says 210'. WRONG BY 90 FEET PER
          TURN, and the error grows with level (320' vs 120' at L16).

THIEF     CHAR-004 built from Chapter 1 + Chapter 4 + Chapter 13 alone would
          permit a thief to buy and use a two-handed sword. RC p. 21
          prohibits it. Chapter 4 carries no thief weapon code at all.

DWARF     Same construction would permit a dwarf a long bow. RC p. 23
          forbids it.

HALFLING  Same construction would permit a halfling any Medium weapon.
          RC p. 26 restricts halflings to Small melee, short bow and
          light crossbow -- and requires halfling-made armour, which
          Chapter 4 does not mention.

MAGIC-USER  Chapter 4's note `w` alone would make the dagger DM-discretionary;
          RC p. 19 makes it the magic-user's one unconditional weapon
          (SS6 Defect 8).
```

The Mystic error is a **wrong number**; the others are **permitted-illegal purchases**. Both are the class of defect this project's governance exists to prevent, and both are reachable from `CLUSTER-003`'s own stated scope.

## 10. Remaining Open Questions

| Classification | Item |
|---|---|
| **RC contradiction** | Belt pouch `52 ≠ 55` (§6.1) |
| **RC contradiction** | Suit Armor `750 cn` → `90' (30')` vs. its own `30' (10')` (§6.2) |
| **RC contradiction** | Starvation Table non-monotonic movement column (§6.3) |
| **RC contradiction** | **NEW** — magic-user dagger: Ch. 4 note `w` vs. Ch. 2 *"Dagger only"* (§6.8) |
| **RC contradiction** | **NEW** — running speed: Ch. 6 `= normal per round` vs. Ch. 8 p. 103 `3 × normal movement` (§6.10) |
| **RC contradiction** (minor, typographic) | "Clothes, plain" carries the quiver footnote (§6.4) |
| **RC ambiguity** | Mystic `MV` × encumbrance composition (§3.3) — `RETAINED AS GENUINE SOURCE AMBIGUITY` |
| **RC ambiguity** | **NEW** — Mystic *"or own personal possessions"* framing unimplemented by the entry's own rules (§6.9) |
| **RC ambiguity** (minor) | **NEW** — standing up: "one round of movement" vs. "an action" (§6.11) |
| **Possible RC gap** | The rough/broken-terrain rate modifier presupposed by Mystic Acrobatics (§6.6) — qualified but not closed |
| **Possible RC gap** | Rounding for non-integral Mystic encounter speeds (§3.2) |
| ~~**Ownership/governance question**~~ **DECIDED 2026-09-14 (Decision 2)** | Who owns the per-class base movement rate (§3.5) → **`CHAR-005`** |
| ~~**Ownership/governance question**~~ **DECIDED 2026-09-14 (Decision 1)** | Who owns per-class weapon-permission predicates and the Druid pricing rule (§4.3) → **`CHAR-004`** |
| ~~**Ownership/governance question**~~ **DECIDED 2026-09-14 (Decision 4)** | Ch. 10 Steps 5/7/8 (§5.4) → **`researched / preserved / NOT V1-WIRED`**; not made executable by `CLUSTER-003`, and `CHAR-004` not expanded |
| ~~**Ownership/governance question**~~ **DECIDED 2026-09-14 (Decision 5)** | Ch. 13 p. 150 condition movement multipliers → **split**: causation keeps its owner, the movement-rate effect belongs to `CHAR-005` |
| **Ownership/governance question — STILL OPEN** | Whether `CHAR-004` extends to mounts, vehicles, ships and siege equipment (carried forward). **Not addressed by the 2026-09-14 decisions**, which concerned class-restriction ownership rather than chapter scope. Non-blocking: those objects are recorded as located and deliberately uninspected, with reasons |
| ~~**Ownership/governance question**~~ **DECIDED 2026-09-14 (Decision 3)** | `EXP-003` title (§7) → renamed and narrowed to **`EXP-003 — Dungeon Movement`** |
| ~~**Boundary-reopen issue**~~ **RESOLVED 2026-09-14** | `CHAR-005` → unlanded class movement rule (§9). Narrow ownership correction; **no card added** |
| ~~**Boundary-reopen issue**~~ **RESOLVED 2026-09-14** | `CHAR-004` → unlanded class weapon-permission rule (§9). Narrow ownership correction; **no card added** |
| **Future alternate-source question** | None authorized. `DEC-0011` is not activated, and no gap statement has been approved for escalation. The two "possible RC gap" rows above are the only candidates, and they may not be escalated on this researcher's initiative. |

**Closed by this pass:** the Mystic "above 16th level" question (moot — maximum level is 16); the racial-armour reduction reclassified from *possible gap* to **DM discretion by design, not a gap** (§6.7); `Mapping and Calling`'s citation corrected from Chapter 1 to **p. 5**; the Dwarf Experience Table's printed location corrected from the Tables Index's p. 23 to **p. 24**.

## 11. Items the Original Pass Declared Open — Final Disposition

| Original open row | Now |
|---|---|
| `CHAR-004` §11.3 — Ch. 2 class entries not read as complete entries | **CLOSED** — all nine read; §2, §4 |
| `CHAR-004` §11.4 — Ch. 10 high-level creation not re-inspected | **CLOSED** — §5.4. Result: a real, unowned mechanic set |
| `CHAR-004` §11.6 / `CHAR-005` §11.4 / `EXP-003` §11.4 — General Index not swept | **CLOSED** — §5.3. Result: two new governing objects |
| `CHAR-005` §11.1 — other eight class entries not checked for a movement statement | **CLOSED** — §2. Result: all silent; Mystic confirmed unique |
| `CHAR-005` §11.3 — Ch. 19 body not read in full | **CLOSED** — §5.1. Result: no encumbrance or movement variant |
| `EXP-003` §11.3 — Ch. 17 pp. 259–262 not inspected | **CLOSED** — §5.2. Result: map scale is DM-variable |
| `CHAR-004` §11.1 — Nets Table not visually verified | ~~**STILL OPEN**~~ → **CLOSED 2026-09-14.** Visually verified at RC p. 65 (leaf n64); agrees with the OCR record exactly; no new mechanic, contradiction or dependency. See `CLUSTER-003-completeness-audit.md` §14.2 |
| `CHAR-004` §11.2 / §11.5 — mount and vehicle tables; `CHAR-004` scope | **STILL OPEN** — a human scope decision, unchanged |
| `CHAR-005` §11.5 — ownership of the p. 150 condition multipliers | **STILL OPEN** — a human ownership decision, unchanged |
| `EXP-003` §11.2 — whether "Mapping" survives in the title | **STILL OPEN** — now joined by "Special Terrain"; §7 |

## 12. Researcher Constraint

This pass was performed by the original researcher. Per protocol §10.1.1 and the independent-reviewer constraint restated in the assignment, the maximum status available is:

```text
REMEDIATION COMPLETE
RESEARCHER SELF-REVIEW COMPLETE
AWAITING SECOND INDEPENDENT COMPLETENESS / BOUNDARY REVIEW
```

`STAGE-A PASS`, `STAGE-A COMPLETENESS PASS`, or any equivalent is **not** claimed and must not be inferred from the closure of items in §11. Six structural items closed; four remain open, three of which are human decisions rather than reading tasks.

> **Superseded 2026-09-14.** The second independent review returned `PASS` on this remediation; the one conditional item (the Nets Table) is closed; and three of the four remaining items were decided by human governance. The current researcher status is:
>
> ```text
> RESEARCHER CLOSURE COMPLETE
> ALL IDENTIFIED PRIMARY-SOURCE INSPECTION ITEMS COMPLETE
> HUMAN BOUNDARY / OWNERSHIP GOVERNANCE APPLIED
>
> AWAITING FINAL INDEPENDENT DEC-0010 COMPLETENESS CERTIFICATION
> ```
>
> The researcher constraint is unchanged: `STAGE-A COMPLETENESS PASS` remains the independent reviewer's certification to make, not mine.
