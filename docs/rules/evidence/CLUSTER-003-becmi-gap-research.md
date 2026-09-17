# CLUSTER-003 — DEC-0011 Alternate-Source (BECMI) Gap Research

> **Status: `BECMI ENUMERATION COMPLETE / SEVEN AUTHORIZED QUESTIONS RESEARCHED / RESEARCHER SELF-REVIEW COMPLETE / AWAITING HUMAN / INDEPENDENT EVIDENCE REVIEW`.**
>
> **This is alternate-source evidence, not authority.** `SOURCE_HIERARCHY.md` §3 places BECMI below the Rules Cyclopedia. Nothing here replaces an RC rule, resolves an RC contradiction by fiat, or converts a finding into a Rule Card. **No Simulator Ruling is drafted or proposed.** Stage B is not begun; the Pre-Code Gate is not begun; no production code was written; no card was added to `CLUSTER-003`.
>
> **Scope.** Authorized by the human project owner for **exactly seven** RC questions, and for **BECMI only**. No B/X, Holmes, OD&D, AD&D or other lineage was consulted. `DEC-0011` is activated for this pass and for these questions alone.
>
> **Companion artifacts** — this document does **not** supersede them and they remain the RC-primary record: `CHAR-004-evidence.md`, `CHAR-005-evidence.md`, `EXP-003-evidence.md`, `CLUSTER-003-completeness-audit.md`, `CLUSTER-003-remediation-pass-1.md`, `docs/rules/clusters/CLUSTER-003-equipped-dungeon-movement.md`.

## 1. Provenance Vocabulary Used Throughout

Every finding below is tagged with one of these, and the tags are not interchangeable:

```text
RC RULE / DEFECT        the Rules Cyclopedia statement under investigation
BECMI EVIDENCE          what a named BECMI core source unit actually prints
DERIVED CONSEQUENCE     arithmetic that follows necessarily from stated values
RESEARCH INFERENCE      the researcher's reading, defeasible
HUMAN GOVERNANCE        a question no researcher may settle
```

## 2. BECMI Source Enumeration (`DEC-0011` items 1–3)

### 2.1 Hierarchical corpus, enumerated before opening anything

```text
LINEAGE            BECMI -- the Frank Mentzer revision, 1983-1986,
                   the direct lineage ancestor the RC consolidates
       |
       v
STRUCTURAL UNITS   five boxed sets: Basic, Expert, Companion,
                   Master, Immortals
       |
       v
CORE SOURCE UNITS  the rulebooks within each set -- NINE in total
       |
       v
GOVERNING OBJECTS  class entries, equipment tables, movement tables,
                   stat blocks, table footnotes (DEC-0010 SS9.1)
```

**Corpus boundary (`DEC-0011` item 2).** The corpus is BECMI's **core rules** — the rulebooks packaged in the five boxed sets. Adventure modules, accessories, `AC`/`B`/`X`/`CM`/`M`/`O` products and magazine material are **outside** it and are not swept.

### 2.2 Source access

| Structural unit | archive.org identifier | Access |
|---|---|---|
| Basic Set | `dungeons-and-dragons-set-1-basic-rules` | Open; OCR + JP2 + IIIF |
| Expert Set | `dungeons-and-dragons-set-2-expert-rules` | Open; OCR + JP2 + IIIF |
| Companion Set | `dungeons-and-dragons-set-3-companion-rules` | Open; OCR + JP2 + IIIF |
| Master Set | `dungeons-and-dragons-set-4-masters-rules` | Open; OCR + JP2 + IIIF |
| Immortals Set | `dungeons-and-dragons-set-5-players-guide-to-immortals` | Open; OCR + JP2 + IIIF |

Each scan was opened and its **internal book structure verified from the title pages and tables of contents** before any question was researched — the five scans contain **nine core source units plus one adventure module**, and each unit's text range was fixed before searching. Page images are served at `https://iiif.archive.org/iiif/<identifier>$<leaf>/…`, so `DEC-0010` §9.2 visual verification is available and was used.

### 2.3 Per-core-source-unit disposition

**Every core source unit receives its own disposition. A parent-level disposition is not used.**

| # | Structural unit | Core source unit | Status | Applies to |
|---|---|---|---|---|
| U1 | Basic Set | **Players Manual** | **INSPECTED — relevant governing material present** | Q1, Q2, Q3, Q4 |
| U2 | Basic Set | **Dungeon Masters Rulebook** | **INSPECTED — relevant structure checked, no governing material** for the seven questions. Contains the sample dungeon, monster list, treasure and DM guidance; its only movement/equipment content is monster stat blocks and a magic-user class note repeating U1's restriction | — |
| U3 | Expert Set | **Expert Rulebook** | **INSPECTED — relevant governing material present** | Q1, Q3, Q4, Q7 |
| — | Expert Set | *X1 The Isle of Dread* (bound into the same scan) | **EXCLUDED — verified reason:** an **adventure module**, not a core rulebook. `DEC-0011` item 2 places adventures outside the corpus. Its title page and TOC were read to confirm identity, and its one `pouch` occurrence was checked and is module flavour text, not a rule | — |
| U4 | Companion Set | **Players Companion: Book One** | **INSPECTED — relevant structure checked, no governing material.** Adds levels 15–25 content: new spells, Strongholds, weapon-mastery-adjacent material. Carries **no equipment price/encumbrance list**, **no character movement table**, **no Mystic**, **no starvation rule** | — |
| U5 | Companion Set | **Dungeon Masters Companion: Book Two** | **INSPECTED — relevant structure checked, no governing material.** Its three `pouch` occurrences are the magic item *pouch of security*; its movement content is War Machine **mass-combat troop** movement and spell effects | — |
| U6 | Master Set | **Master Players' Book** | **INSPECTED — relevant governing material present** | Q2, Q3 |
| U7 | Master Set | **Master DM's Book** | **INSPECTED — relevant governing material present** | Q5, Q6 |
| U8 | Immortals Set | **Players' Guide to Immortals** | **INSPECTED — corroborating material present** | Q4 |
| U9 | Immortals Set | **DM's Guide to Immortals** | **INSPECTED — relevant structure checked, no governing material.** Planar/Immortal mechanics; its single `suit armor` occurrence is a passing reference, not a rule statement | — |

**Nine of nine core source units dispositioned by inspection. No unit is excluded on a level-range or subject-matter assumption** (`DEC-0011` item 4) — U4, U5, U8 and U9 were opened and their structures read, not assumed silent.

### 2.4 Structural instruments used (precedent `P-001`)

`P-001` (`docs/rules/RESEARCH_PROCESS_PRECEDENTS.md`) requires General Index inspection where the source provides one. Applied to BECMI:

| Unit | TOC | Index | Notes |
|---|---|---|---|
| U1 Players Manual | **Yes** — read | No general index | Uses a **centre pull-out reference spread**, which was located and read; it carries duplicate presentations of the movement and container tables |
| U2 DM Rulebook | **Yes** — read | No general index | — |
| U3 Expert Rulebook | **Yes** — read | No general index | Equipment and encumbrance located through the TOC, not by search |
| U4/U5 Companion | **Yes** — both read | **U5 has an index** — swept for equipment/movement/encumbrance headwords | — |
| U6/U7 Master | **Yes** — both read | No general index located | — |
| U8/U9 Immortals | **Yes** — both read | **U8 has an index** (`Index for IMMORTAL PLAYERS' BOOK`) — swept | — |

**BECMI provides no volume-spanning General Index comparable to the RC's**, so `P-001`'s instrument is only partly available. Where an index exists it was swept; where none exists, the TOC and the pull-out spread were used and that limitation is recorded here rather than left implicit.

### 2.5 Conflict-precedence statements (`DEC-0011` item 6)

**No global conflict-precedence statement was located in the nine core source units inspected.** BECMI's own organisation is **additive**: later sets extend earlier ones and cross-reference them by book and page (e.g. U6 cites *"the Companion Set Players Book, page 18"*; U7 cites *"the revised D&D Basic Set"* and *"the revised D&D Expert Set"*), rather than declaring precedence over them.

**Scope of this negative:** it is scoped to the nine core source units listed in §2.3 and to the TOC/index instruments in §2.4. It is **not** a claim about the BECMI lineage as a whole, and it is not restated as one.

## 3. Question 1 — Belt Pouch Encumbrance

**RC RULE / DEFECT.** RC Adventuring Gear Table (p. 69) prints `Pouch, belt | Capacity 50 cn | 5 sp | 2*`; footnote `*` states that a filled container's encumbrance includes both the container and its contents, and gives the worked example *"a fully filled belt pouch has an encumbrance of **55 cn**."* `2 + 50 = 52`, not 55. Both sides visually verified at RC leaf n68.

**BECMI structural units inspected:** U1, U2, U3, U4, U5, U6, U7, U8, U9 — all nine, for any general equipment price/encumbrance list.

**Governing objects located:**

| Object | Unit | Page |
|---|---|---|
| `WEAPONS AND EQUIPMENT` (solo-adventure shopping list; cost only) | U1 | 22 |
| `Complete list: weapons and equipment` (centre pull-out; cost only) | U1 | pull-out |
| `CONTAINER VOLUME` table (pull-out) | U1 | pull-out |
| **`NORMAL EQUIPMENT` table + `Capacities` note** | **U3** | **19** |
| `HORSE ARMOR (BARDING)`, siege and fortification tables | U6 | 14, 24+ |

**Tables visually verified:**

- **U3 Expert Rulebook p. 19 (leaf n21), `NORMAL EQUIPMENT`** — read from the page image, in full, in alphabetical order:

```text
Backpack 5 / 20        Mirror, hand-sized steel 5 / 5
Garlic 5 / 1           Oil (1 flask) 2 / 10
Grappling Hook 25 / 80 Pole, Wooden (10' long) 1 / 100
Hammer (small) 2 / 10  Rations, Iron 15 / 70
Holy Symbol 25 / 1     Rations, Standard 5 / 200
Holy Water 25 / 1      Rope (50' length) 1 / 50
Iron Spikes (12) 1/60  Sack, small 1 / 1
Lantern 10 / 30        Sack, large 2 / 5
                       Stakes (3) and Mallet 3 / 10
                       Thieves' Tools 25 / 10
                       Tinder Box 3 / 5
                       Torches (6) 1 / 120
                       Waterskin (1 quart) 1 / 5
                       Wine (1 quart) 1 / 30
                       Wolfsbane (1 bunch) 10 / 1

Capacities: Backpack 400 cn   Sack, small 200 cn   Sack, large 600 cn
```

**There is no `Pouch` row.** The list is alphabetical and runs **`Pole, Wooden` → `Rations, Iron`** with nothing between — exactly where a belt pouch would fall. **This absence is established on the page image, not by a failed search.**

**Cross-references followed:** U3 p. 19 `Capacities` note ↔ U1 pull-out `CONTAINER VOLUME` (Small sack 200 cn, Backpack 400 cn, Large sack 600 cn, Saddle bag 1000 cn) — a **duplicate presentation** (`DEC-0011` item 5), recorded separately and **numerically identical**.

**Exact mechanical findings:**

```text
empty belt-pouch encumbrance   NOT PRESENT IN BECMI
carrying capacity              NOT PRESENT IN BECMI
filled encumbrance             NOT PRESENT IN BECMI
worked example explaining 55   NOT PRESENT IN BECMI

container values RC did inherit, unchanged:
    Backpack     enc 20    capacity 400 cn
    Sack, small  enc  1    capacity 200 cn
    Sack, large  enc  5    capacity 600 cn
    coin weight  1 cn = about 1/10 pound  (U1 p. 61, visually verified)
```

**Changes across BECMI sources:** none — U1 and U3 agree; U4–U9 add no general equipment list at all (U6 adds only suit armor, barding, weapon-mastery and siege/fortification tables).

**Compatibility with RC.** The **container rule** RC states (empty encumbrance, plus contents when filled) is a direct and faithful continuation of BECMI's `Capacities` structure. The **belt pouch itself is an RC-era addition** with no BECMI ancestor, and the `55 cn` figure therefore has no lineage source.

**RESEARCH INFERENCE, offered as such:** the discrepancy appears **introduced at RC compilation**, not inherited — because the object itself does not exist upstream. That is an inference from absence-of-ancestor, and it is weaker than a positive finding.

**Does BECMI resolve the RC question?** **No.** It removes one hypothesis (inheritance) and supplies neither 52 nor 55.

```text
CLASSIFICATION: E -- BECMI IS SILENT / DOES NOT RESOLVE
```

**Confidence / residual uncertainty.** High that no belt pouch exists in the nine core source units (verified on the page image for the one list that carries encumbrance values, and by TOC-led inspection elsewhere). The RC-origin inference is **moderate**: BECMI-era accessories and modules were not swept and are outside the authorized corpus, so an intermediate ancestor outside the core rules is not excluded.

## 4. Question 2 — Magic-User Dagger Permission

**RC RULE / DEFECT.** RC Ch. 2 p. 19 (visually verified): *"Weapons: **Dagger only.** Optional (DM's discretion): staff, blowgun, flaming oil, holy water, net, thrown rock, sling, whip."* RC Ch. 4 note `w` (visually verified): *"Magic-users may use this weapon **at the DM's discretion**"* — and RC's Weapons Table marks **both dagger rows** `t,w,S`, placing the dagger inside the discretionary set.

**BECMI structural units inspected:** U1 (class entry + both equipment lists), U2 (magic-user DM guidance), U3 (class material + equipment-table notes), U4, U5, U6, U7 — for any magic-user weapon rule.

**Governing objects located:**

| Object | Unit | Page |
|---|---|---|
| **Magic-User class entry, `Weapons:` line** | **U1** | 14 |
| `Complete list: weapons and equipment` — weapon restriction marks | U1 | pull-out |
| **`*Notes on all Equipment Lists`** — the full note-code set | **U3** | 19 |
| **`Weapon Mastery Magic-User Option`** | **U6** | 15 |

**Exact mechanical findings:**

**U1 Basic Players Manual, Magic-User class entry:**
> *"…may not use a shield. **Weapons: A magic-user can only use a dagger for a weapon.**"*

Unconditional. No optional set. No DM discretion.

**U1 pull-out equipment list** carries exactly one weapon restriction mark: `*These weapons may be used by a cleric`. **No magic-user mark exists.**

**U3 Expert Rulebook, `*Notes on all Equipment Lists`** — the complete note-code set, read on the page image:
```text
a  Ammunition is included in encumbrance.
b  Encumbrance is for mules or horses towing the wheeled catapult...
c  This weapon is permitted for clerics.
d  Figures are: maximum capacity for normal movement / and capacity
   for half normal movement.
e  Capacity varies with number of horses...
f  Encumbrance (Enc) is for empty item; add for items carried...
g  Encumbrance is 1,000 cn if carried by one person, 300 cn each for 2...
h  Capacity figures are for purchased vs. made by characters.
```
**There is a cleric note. There is no magic-user note.** RC's note `w` has **no BECMI ancestor**.

**U6 Master Players' Book, `Weapon Mastery Magic-User Option`:**
> *"The following option may be used with or without weapon mastery. The DM may, if desired, **widen the number of weapons permitted to magic-users to include the following: blowgun, net, whip, and staff.** However, **many campaigns function perfectly well with magic-users restricted to dagger only.**"*

**Changes across BECMI sources:**

```text
Basic (1983)   dagger only, unconditional, class entry only
Master (1985)  DM MAY WIDEN the permitted set to add
               blowgun, net, whip, staff
               -- the dagger is what is being widened FROM,
                  and is named as the fallback baseline
```

**Compatibility with RC.** RC Ch. 2 **preserves the BECMI structure exactly**: an unconditional dagger permission plus a DM-discretionary expansion. RC *extends* the optional list (adding flaming oil, holy water, thrown rock, sling), which is an RC-era change, but the two-tier structure is inherited intact.

**DERIVED CONSEQUENCE.** RC's Chapter 4 `w` set = BECMI's Master optional set (blowgun, net, whip, staff) **plus RC's four additions plus the dagger**. The dagger is the only member of RC's `w` set that BECMI's lineage places **outside** the discretionary tier.

**Does BECMI resolve the RC question?** It does not address RC's note `w`, which post-dates it. But it establishes across **two structural units** that the dagger is the magic-user's unconditional weapon and that the optional list is an addition to it.

```text
CLASSIFICATION: B -- BECMI SUPPORTS ONE RC READING
```

**Compatibility test.** Reading RC Ch. 2 as governing and note `w`'s application to the dagger rows as a tagging error would **preserve** every other RC mechanic, require changing **no** explicit RC rule (Ch. 2 already says it), and conflict with no other RC governing object. **This is the profile of a defect interpretation, not of an alternate-source import** — so the eventual provenance would be an RC-internal reading, not `Alternate-Source Compatible Completion`.

**Confidence.** High on the BECMI facts (four governing objects, three visually verified). **The classification remains B rather than A** because BECMI cannot speak to a note code that did not exist when it was written.

## 5. Question 3 — Suit Armor Movement

**RC RULE / DEFECT.** RC Armor Table: Suit Armor `Enc 750 cn`. RC Character Movement Rates and Encumbrance Table: `401–800 cn → 90' (30')`. RC Suit Armor description: *"The wearer's movement rate is **30' (10')**"* — the `1,201–1,600` band. All three visually verified during RC-primary research.

**BECMI structural units inspected:** U6 (suit armor), U1 and U3 (the encumbrance→movement table and its Expert restatement), U9 (its one `suit armor` occurrence).

**Governing objects located:**

| Object | Unit | Page | Visually verified |
|---|---|---|---|
| **Suit Armor entry** (`Advantages` / `Disadvantages`) | **U6** | 14 | **Yes** (leaf n17) |
| **`SPEED VS. ENCUMBRANCE TABLE`** | **U1** | 61 | **Yes** (leaf n63) |
| `ENCUMBERED MOVEMENT RATES TABLE` (pull-out duplicate) | U1 | pull-out | OCR; values identical to the verified table |
| `Encumbrance (Optional Expert System)` | U3 | 21–22 | OCR |
| `HORSE ARMOR (BARDING)` | U6 | 14 | Partially (in the p. 14 page view) |

**Exact mechanical findings — U6 Master Players' Book, Suit Armor (visually verified):**

```text
"Suit armor alone is AC 0. It may be used with a shield for AC -1."
"Its encumbrance is 750 cn ... the cost is 250 gp."
"Suit armor is noisy and slow. Its common creaks and clanks can be
 heard up to 120 feet away and negate chances for surprise.
 The wearer's movement rate is 30 FEET PER TURN."
"An unarmored fighter needs THREE FULL TURNS to dress in suit armor."
"If a fighter in suit armor is mounted and has assistance from others,
 the disadvantages of encumbrance, slow movement, and surprise
 (see below) can be minimized."
```

**U1 Basic Players Manual p. 61, `SPEED VS. ENCUMBRANCE TABLE` (visually verified):**

```text
Encumbrance      Normal Speed      Encounter Speed   Running Speed
                 (Feet per turn)   (Feet per round)
up to 400 cn          120                40               120
401-800 cn             90                30                90
801-1200 cn            60                20                60
1201-1600 cn           30                10                30
1601-2400              15                 5                15
2401 and more           0                 0                 0
```

**U3 Expert Rulebook:** *"In the D&D Basic Set, a simple total encumbrance was based on the type of armor worn. With Expert rules, **the same movement rates are used**, but the system for finding the total encumbrance is more detailed."* — the Expert set changes **how** encumbrance is totalled, **not** the bands.

**DERIVED CONSEQUENCE.** `750 cn` falls in BECMI's `401–800 cn` band → **90 feet per turn**. The Suit Armor entry says **30 feet per turn**.

```text
THE CONTRADICTION ALREADY EXISTED IN BECMI,
across two structural units (Basic 1983 and Master 1985),
with both sides visually verified.
RC did not introduce it. RC inherited it.
```

**Changes across BECMI sources:**

| | BECMI | RC | Change |
|---|---|---|---|
| Encumbrance | 750 cn | 750 cn | none |
| Cost | 250 gp | 250 gp | none |
| Movement statement | **"30 feet per turn"** | **"30' (10')"** | **RC converted a single per-turn value into the paired normal/encounter notation** |
| Time to don | **three full turns** | **two full turns** (+ one to remove) | changed |
| Rising / mounting alone | 1 in 6 | 1 in 6 **per round** | RC adds the per-round qualifier |

**Is it an override?** The falsification challenge was that the explicit movement line is *automatically* an override. **BECMI does not support that.** It supplies **no** override language — no *"regardless of encumbrance"*, no *"instead of"*, no cross-reference in either direction between the Master suit-armor entry and the Basic encumbrance table. The one adjacent sentence — *"the disadvantages of **encumbrance, slow movement**, and surprise can be minimized"* — names encumbrance and slow movement as **two separate disadvantages**, which is at least as consistent with a drafting oversight as with a deliberate override.

**RESEARCH INFERENCE, offered as such and defeasible:** the `30 feet per turn` figure equals the movement of a character in the `1,201–1,600 cn` band. A plausible reading is that the Master author wrote a flavour-driven "slow" figure without checking it against the Basic table. **No BECMI text supports or refutes this**, and it is not adopted.

**Does BECMI resolve the RC question?** **No** — but it changes the question's character decisively: this is not an RC compilation error to be repaired against the lineage. It is a **pre-existing lineage contradiction the RC faithfully carried forward**.

```text
CLASSIFICATION: D -- BECMI IS INTERNALLY CONFLICTED
```

**Compatibility test.** Adopting either side would **conflict with the other RC governing object**, exactly as it does in BECMI. No import is available; there is nothing upstream to import. **This is a human-adjudication candidate, not an `Alternate-Source Compatible Completion` candidate.**

**Confidence.** High — both sides visually verified in both sources.

## 6. Question 4 — Running Speed

**RC RULE / DEFECT.** RC Ch. 6 p. 88: running speed *"is equal to their normal speed in feet per round (rather than turn) **or three times their encounter speed**."* RC Ch. 8 p. 103: *"his full running speed movement (**3 × normal movement**)"*, in a bullet list whose preceding bullet uses *"normal movement"* to mean the per-turn value. Taken literally the two differ by a factor of 3. Both visually verified during RC-primary research.

**BECMI structural units inspected:** U1 (movement rules, table, combat movement), U2, U3 (wilderness pursuit), U4, U5, U6, U7, U8.

**Governing objects located:**

| # | Object | Unit | Page | Verified |
|---|---|---|---|---|
| 1 | **`Encumbered Movement Rates` prose** | U1 | 61 | **Visually** |
| 2 | **`SPEED VS. ENCUMBRANCE TABLE`** | U1 | 61 | **Visually** |
| 3 | `ENCUMBERED MOVEMENT RATES TABLE` (pull-out duplicate) | U1 | pull-out | OCR, values identical |
| 4 | **Combat/flight movement passage** | U1 | ~56 | OCR |
| 5 | **Wilderness pursuit rule with worked example** | U3 | 21 | OCR |
| 6 | Immortal standard-form movement gloss | U8 | — | OCR |

**Exact mechanical findings.**

**(1) U1 p. 61, visually verified:**
> *"'Normal speed' is used when your characters are walking through a dungeon."*
> *"'Encounter speed' is used whenever time is kept in rounds, such as during a battle."*
> *"'**Running speed' is used whenever the party is running away from an encounter. Time is still kept in rounds, rather than turns**, and the party must rest afterward."*

**(2) The table, visually verified:** `120 / 40 / 120`, `90 / 30 / 90`, `60 / 20 / 60`, `30 / 10 / 30`, `15 / 5 / 15`, `0 / 0 / 0`, with `Normal Speed (Feet per turn)` and `(Feet per round)` spanning Encounter and Running. **Running speed is the normal-speed number, read per round. It is 3 × encounter speed. It is never 3 × the normal-speed number.**

**(4) U1 combat/flight passage:**
> *"characters can move ⅓ their movement rate per round, up to **40' per round** during battles (20' per round if in armor). In addition, you may run away from creatures, at the even faster rate of **120'** (or 60' if armored) per round."*

**(5) U3 p. 21 — the decisive object, because it carries BECMI's own worked example:**
> *"…if all characters are riding lightly encumbered war horses (**180' per turn**), the party may cover 36 miles per day (180 ÷ 5 = 36)."*
> *"**Pursuit speed in the wilderness is equal to 3 times normal speed per round.** For example, **a war horse (60' per round)** may pursue or flee at a maximum rate of **180' per round**."*

**DERIVED CONSEQUENCE — the two formulations are the same rule.** The same paragraph fixes the war horse at `180' per turn` normal speed, hence `60' per round` encounter speed. `3 × 60 = 180' per round` — which is the normal-speed *number*, per round. **BECMI's "3 times normal speed per round" means 3 × the per-round rate**, and the phrase *"per round"* is load-bearing.

**(6) U8 corroboration:** an Immortal's standard form moves *"at **120 feet per round (the same rate as an unencumbered human)**"*, and may be *"hurried a bit, to **150'(50')**"* — a correctly formed 3:1 pair. A fifth independent statement that an unencumbered human's running rate is 120 feet **per round**.

**Changes across BECMI sources:** none in substance. Basic states it as a table column and as a flat figure; Expert states it as a multiplier **with the disambiguating qualifier and example**; Immortals glosses it in passing. **Terminology differs; the mechanic does not.**

**Compatibility with RC.** RC Ch. 6 preserves BECMI exactly — including both formulations in one sentence (*"equal to their normal speed in feet per round… or three times their encounter speed"*), which is precisely BECMI's Basic and Expert phrasings reconciled. **RC Ch. 8 p. 103 reproduces BECMI's Expert phrasing with the qualifier `per round` dropped and the worked example omitted.**

**Does BECMI resolve the RC question?** **Yes, decisively**, on five governing objects across three structural units, two of them visually verified, with an internal arithmetic cross-check that admits no other reading.

```text
CLASSIFICATION: A -- BECMI RESOLVES RC DEFECT
```

**Compatibility test.** Reading RC Ch. 8's *"3 × normal movement"* as *3 × encounter speed* **preserves** RC Ch. 6, **preserves** the RC movement table, requires changing **no** explicit RC rule, conflicts with **no** other RC governing object, and introduces **nothing** RC removed. It is the reading RC Ch. 6 already states in terms.

**Adjacent finding in the same passages, recorded not resolved.** BECMI U1 states the running limit as *"only **20 rounds** at most (**5 minutes**)"* — internally inconsistent at 10 seconds per round. RC states *"**30 rounds** at most (5 minutes)"*. **RC appears to have corrected a BECMI arithmetic defect.** Exhaustion consequences are otherwise identical in both (`rest 3 turns`; `+2` to monsters' attacks; `−2` damage, minimum 1). This is inside Q4's governing passage, so it is recorded here; **it is not promoted to an eighth question.**

**Confidence.** Very high.

## 7. Question 5 — Mystic MV × Encumbrance

**RC AMBIGUITY.** RC Ch. 2 p. 31 gives the Mystic a level-dependent `MV` of 120′ → 320′; RC Ch. 6 p. 88 states *"**any character** will have a movement rate of `120' (40')` unless he is weighed down"* and supplies six encumbrance bands. RC nowhere states how the two compose.

**BECMI structural units inspected:** U7 (the Mystic), U6, U1, U3 (movement and encumbrance), U4, U5 (checked for a Mystic — **absent**).

**Governing objects located:**

| Object | Unit | Page | Verified |
|---|---|---|---|
| **`Mystics` — cloister life and PC Mystics** | **U7** | 18 | Text |
| **`Mystic` monster entry — stat block + per-HD table** | **U7** | 32 | **Visually** |
| Mystic special abilities and Acrobatics | U7 | 32–33 | **Visually** (p. 33) |
| Martial arts / styles | U7 | 18–19 | Text |

**Exact mechanical findings.**

**The BECMI Mystic is a MONSTER, optionally promotable to a PC:**
> *"Mystics are **NPC humans**… **Special rules allow mystics to be player characters at the DM's option**."*
> *"If the DM desires, he may allow player character mystics. **All the details and rules given in the monster description still apply.**"*

**The `MV` values live in a monster stat block** (U7 p. 32, visually verified):

```text
Mystic
Armor Class:  9 or better (see below)
Hit Dice:     1 to 16********* (d6)
Move:         120'(40') to 320'(80')  (see below)

HD (d6)  AC   MV     #AT     HD (d6)  AC   MV     #AT
1         9   120'    1      9*****    1   200'    3
2*        8   130'    1      10*****   0   210'    3
3*        7   140'    1      11*****  -1   220'    3
4**       6   150'    1      12****** -2   240'    3
5***      5   160'    2      13*******-3   260'    4
6***      4   170'    2      14*******-4   280'    4
7***      3   180'    2      15        -5   300'    4
8****     2   190'    2      16        -6   320'    4
```

**RC preserved these sixteen values exactly**, re-keyed from Hit Dice to experience level.

**What `MV` represents:** the monster-statistic `Move`, whose meaning is fixed by RC Ch. 14's inherited definition and by BECMI's own stat-block convention — first number feet per **turn**, parenthesised number feet per **round**.

**Armour:** *"Mystics **never wear armor of any type**, nor do they ever use protective magical devices… they rely on their discipline for protection."* — so the rate is, in effect, an unarmoured rate; but BECMI **does not say** it is "the unencumbered rate".

**Carried equipment:** *"They are **trained to use all weapons, but often do not carry them**. **All material goods (money, magic items, etc.) are owned by the cloister, not by the mystics themselves**, and are merely loaned or given to the individuals as needed."* — an ownership convention, **not** an encumbrance rule, and it imposes no cn limit.

**Is the interaction addressed anywhere?**

```text
Does BECMI state how Mystic MV composes with encumbrance?   NO
Is there a worked example?                                   NO
Is Mystic movement tied to Acrobatics or level progression?
    Level:      YES -- MV rises with Hit Dice, on the table
    Acrobatics: NO  -- BECMI's Acrobatics list is
                Jumps/Leaps, Tumbles/Flips, DODGES, Catches,
                Swings, Balancing, with NO movement-rate clause
                (RC drops "Dodges" and ADDS the rough/broken
                 terrain clause -- an RC-era addition)
```

**A structural observation that is evidence, not a rule.** In BECMI the Mystic is a **monster**, and monster encumbrance is tallied only when carrying prey or riders — the character encumbrance table does not apply to monsters at all. **BECMI therefore had no occasion to state the interaction**, and the question only arises because BECMI's own "PC Mystics" option, and then the RC, promoted a monster stat line into a player-character movement rate **without revisiting it**.

**Falsification of "Mystic MV is obviously an unencumbered base speed":** BECMI supplies **no** text calling it a base rate, **no** text subjecting it to the bands, and **no** text exempting it. RC's *"First level mystics move as fast as any other unarmored characters"* gloss is **an RC-era addition with no BECMI ancestor** — so the one textual hint pointing toward the "base rate" reading is RC's, not the lineage's.

```text
CLASSIFICATION: E -- BECMI IS SILENT / DOES NOT RESOLVE
```

**Compatibility test.** No candidate rule exists to import, so no compatibility assessment is possible. **This cannot become an `Alternate-Source Compatible Completion`.** It is a **human-ruling candidate** — and the RC-primary assessment that it is the cluster's most likely Stage-B blocker **is strengthened**, not relieved, by this pass.

**No composition rule is invented here.**

**Confidence.** High that BECMI is silent — the complete Mystic entry across three pages was read and two pages visually verified; the Mystic is absent from U1–U6, U8, U9.

## 8. Question 6 — Mystic Encounter Movement / Rounding

**RC CONSEQUENCE.** RC's Mystic table prints single `MV` values; RC's general rule derives encounter speed as ⅓ of normal. Ten of the sixteen values are not divisible by 3, and RC states no rounding rule.

**Governing objects located:** the same U7 p. 32 stat block and table as Q5, **visually verified**.

**Exact mechanical findings.**

**BECMI DOES print a paired value — and it does not obey the ⅓ rule:**

```text
U7 p. 32, stat block, VISUALLY VERIFIED:

    Move:  120'(40')  to  320'(80')  (see below)

    120 / 3 = 40   ✓ consistent
    320 / 3 = 106.67   -- but BECMI prints (80')
    320 / 80 = 4       -- a 4:1 ratio, not 3:1
```

**DERIVED CONSEQUENCE.** `80'` is the correct ⅓ encounter rate for **240′**, which is the **12 HD** row of the same table — not for the 16 HD row of `320′`. The printed upper bound pairs a 16 HD normal rate with a 12 HD encounter rate.

**RESEARCH INFERENCE, offered as such:** this looks like a compositing or revision artefact in BECMI — plausibly a stat line written when the table topped out at 240′. **No BECMI text confirms this**, and it is not adopted.

**What BECMI does NOT supply:**

```text
printed per-level Mystic encounter rates    NO -- the MV column is
                                            single-valued for all 16 rows
an explicit rounding convention             NOT LOCATED in U1-U9
a general movement rounding rule            NOT LOCATED in U1-U9
an alternate derivation avoiding fractions  NOT LOCATED
an example revealing intended treatment     NO
```

**What BECMI does supply, and it matters:** every **other** paired movement value inspected across the corpus is exactly 3:1 — `120'(40')`, `180'(60')`, `240'(80')`, `150'(50')`, `90'(30')`. **The 3:1 relation is the lineage's unbroken convention; the Mystic's `320'(80')` is the single located departure from it**, and it is a departure in a direction arithmetic cannot justify.

**Compatibility with RC.** RC **dropped the parenthetical from the Mystic table entirely**. Whether that was deliberate or incidental, the effect is that **RC does not reproduce BECMI's defective pair** — RC's Mystic table is silent where BECMI is wrong. Importing BECMI's `(80')` would import a value inconsistent with RC's own ⅓ rule and with BECMI's own convention.

**Does BECMI resolve the RC question?** **No.** It supplies one paired value, that value is internally inconsistent, and it supplies no rounding rule.

```text
CLASSIFICATION: D -- BECMI IS INTERNALLY CONFLICTED
```

*(Classified `D` rather than `E` because BECMI is not merely silent: it prints a value that conflicts with its own general relation. `E` would understate what a reviewer needs to see.)*

**Compatibility test.** Adopting `320'(80')` would **conflict with an explicit RC rule** (encounter speed = ⅓ normal) **and** with BECMI's own convention. It is **not** a valid Compatible Completion.

**No rounding convention is chosen here** — not floor, not ceiling, not nearest, not fractional.

**Confidence.** High on what BECMI prints (visually verified twice). The "compositing artefact" reading is **an inference only**.

## 9. Question 7 — Starvation Movement Multipliers

**RC RULE / DEFECT.** RC Starvation Table (p. 150, visually verified) prints a `Movement Rates` column reading `No Penalty / × 3/4 / × 1/2 / × 3/4` against worsening starvation bands, while `Must Rest` (6→8→10→12 hours) and attack penalty (none→−2→−4→−6) both worsen monotonically.

**BECMI structural units inspected:** all nine, for any starvation, hunger, deprivation or special-condition rule.

**Governing object located — exactly one:**

**U3 Expert Rulebook p. 21, under `Food`:**
> *"Foraging: Your characters may forage while traveling, by slowing their movement rate to ½ normal… You usually have a 1 in 3 chance of finding enough food to survive."*
> *"**If they run out of food, your characters will face hunger — needing more rest, traveling slower, being penalized on Hit rolls, and gradual loss of hit points and eventual death from starvation.**"*

**Exact mechanical findings:**

```text
ancestral starvation TABLE          DOES NOT EXIST in U1-U9
exact movement modifiers            NONE PRINTED
whether the final value is
    3/4, 1/4 or another value       BECMI SUPPLIES NO VALUE AT ALL
changes between BECMI sources       none -- only one unit addresses hunger
prose supplying a correction        NO
```

**The one substantive finding.** BECMI's single sentence enumerates **four effect categories**, and they are **exactly the four columns of RC's Starvation Table**, in the same order:

```text
BECMI Expert prose                RC Starvation Table column
------------------------------    --------------------------------
"needing more rest"           ->  Must Rest (per day)
"traveling slower"            ->  Movement Rates
"being penalized on Hit rolls"->  Penalty to Attack Rolls
"gradual loss of hit points"  ->  Hit Point Loss
```

**RESEARCH INFERENCE, offered as such:** RC's table appears to be an **RC-era quantification of a BECMI qualitative statement** — the categories are inherited, the numbers are not. This is an inference from structural correspondence, not from any BECMI text.

**Falsification of "the final 3/4 is obviously meant to be 1/4":** **BECMI gives no support whatever for `1/4`, for `3/4`, or for any number.** The only quantitative movement figure anywhere near the subject is *foraging* at **½ normal** — a different mechanic (a voluntary slowdown to gather food), and the RC table's `50%–74%` band coincidentally also reads `× 1/2`. That coincidence is **not** evidence and is recorded only so a reviewer can see it was considered and rejected.

**Does BECMI resolve the RC question?** **No.**

```text
CLASSIFICATION: E -- BECMI IS SILENT / DOES NOT RESOLVE
```

**Compatibility test.** Nothing to import. The RC defect is **internal to RC** and must be resolved as an RC-internal question — by human adjudication, or by a determination that the printed value is a transcription defect. **Not a Compatible Completion candidate.**

**Confidence.** High that no starvation table exists in the nine core source units: all nine were swept for `starvation|hunger|without food|dehydrat`, every hit was read in context, and the only non-flavour hit is the U3 sentence above. The corresponding RC material sits in RC Chapter 13, a DM-procedures chapter with **no BECMI structural counterpart** — BECMI's DM guidance is distributed across U2, U5, U7 and U9, all of which were inspected.

## 10. Cross-Question Findings

Shared BECMI objects that bear on more than one question. **Recorded explicitly so that no question is silently resolved using evidence discovered under another.**

| Shared object | Questions | How it is used in each |
|---|---|---|
| **U1 p. 61 `SPEED VS. ENCUMBRANCE TABLE`** (visually verified) | **Q3, Q4** | Q3: supplies the `401–800 cn → 90'` band that the Suit Armor entry contradicts. Q4: supplies the `Running Speed` column that fixes running = normal-speed number per round. **Q6 negative use:** establishes the 3:1 convention the Mystic pair departs from |
| **U1 p. 61 `Encumbered Movement Rates` prose** (visually verified) | **Q4** primary; **Q1** incidentally (coin weight `1 cn ≈ 1/10 lb`) | Q1 uses only the coin-weight sentence, nothing else |
| **U3 p. 19 `NORMAL EQUIPMENT` + `Capacities`** (visually verified) | **Q1** primary; **Q2** via the same page's `*Notes on all Equipment Lists` | Q2 uses **only** the note-code set, to establish that no magic-user note exists. The two uses are independent |
| **U3 p. 21 wilderness pursuit + worked example** | **Q4** | Sole disambiguating object for `3 × normal speed per round` |
| **U3 p. 21 `Food` / hunger sentence** | **Q7** primary; **Q4** adjacently (the `Rest` rule on the same page) | Q4 does not rely on it |
| **U6 p. 14 Suit Armor** (visually verified) | **Q3** primary; **Q2** via the same book's `Weapon Mastery Magic-User Option` on p. 15 | Different objects on adjacent pages; not conflated |
| **U7 p. 32 Mystic stat block + table** (visually verified) | **Q5, Q6** | Q5: the values and the absence of an encumbrance statement. Q6: the printed `320'(80')` pair. **Both draw on the same object and this is stated in each section** |
| **U8 Immortal standard-form gloss** | **Q4** | Corroboration only; no finding rests on it alone |

**One cross-question consequence worth flagging to human review.** Q4's classification `A` and Q3's classification `D` rest on **the same table**. That is not circular — Q4 asks what the table's Running column *means* (BECMI answers), while Q3 asks how the table interacts with a *different book's* flat override (BECMI does not answer, and conflicts with itself). **A reviewer should nonetheless check that separation deliberately**, because a single table carrying two opposite verdicts is exactly the shape a reasoning error would take.

**Recorded, not promoted to a question.** The RC Ch. 6 sentence *"Though it makes no difference to the combat round or the 10-minute turn, the terrain may affect the distance a party travels in a day"* appears in U3 p. 21 in near-identical words. This **corroborates** the `EXP-003` Special-Terrain finding from RC-primary research. It was encountered inside Q4's governing passage and is recorded for provenance only; **Special Terrain is not an authorized question and was not researched.**

## 11. Falsification Results — the seven required challenges

| # | Proposition challenged | Evidence | Disposition |
|---|---|---|---|
| **1** | *The RC belt-pouch 55 cn value is simply a typo* | The belt pouch has **no BECMI ancestor at all** — verified on the U3 p. 19 page image, where the alphabetical list runs `Pole → Rations` with no `Pouch` row, and absent from every other equipment list in the corpus. Nothing upstream prints 52, 55, or the item | **NOT ESTABLISHED.** "Typo" presumes a correct value was corrupted; no such value exists upstream. The discrepancy may equally be an authoring error in a new RC-era entry. **Not resolved** |
| **2** | *The dagger should obviously be unconditional for Magic-Users* | U1: *"A magic-user can only use a dagger for a weapon"*; U6: the DM may *"widen"* the set to add blowgun, net, whip, staff, with *"restricted to dagger only"* named as the baseline; U3's note-code set contains a cleric note and **no magic-user note** | **SUPPORTED BY LINEAGE, not by intuition.** Two structural units make the dagger the unconditional baseline. RC Ch. 4's note `w` has no ancestor. Recorded as classification **B**, not as a resolution |
| **3** | *Suit Armor's explicit movement line is automatically an override* | U6 supplies **no** override language; the adjacent sentence names *"encumbrance, slow movement, and surprise"* as **separate** disadvantages; no cross-reference exists in either direction between U6 p. 14 and U1 p. 61 | **REJECTED.** BECMI gives no basis for specific-over-general here. The contradiction is **pre-existing and unresolved in the lineage itself** |
| **4** | *Running speed has one stable meaning throughout BECMI* | Five governing objects across three structural units. Basic: *"running away… time is still kept in rounds"* + the table's `Running Speed` column. Expert: *"3 times normal speed per round"* **with a worked example** (war horse `180'/turn` = `60'/round`, pursuit `180'/round`). Immortals: *"120 feet per round (the same rate as an unencumbered human)"* | **CONFIRMED — the mechanic is stable; only the wording varies.** And the wording variation is exactly what RC Ch. 8 inherited without its qualifier. This is the finding, not an obstacle to it |
| **5** | *Mystic MV is obviously an unencumbered base speed* | BECMI calls it neither. It is a **monster `Move` statistic**; BECMI states no relationship to the encumbrance bands, gives no worked example, and imposes no cn limit. RC's *"as fast as any other unarmored characters"* gloss is **an RC-era addition with no BECMI ancestor** | **REJECTED as "obvious".** The one textual hint favouring that reading originates in RC, not in the lineage. **Not resolved** |
| **6** | *Mystic encounter movement obviously rounds down* | BECMI prints **no** per-level encounter rates and **no** rounding rule anywhere in U1–U9. Its one printed pair, `320'(80')`, is not ⅓ of 320 in any rounding convention — floor, ceiling or nearest all give ~106 | **REJECTED.** No rounding convention is stated, and the single printed value is inconsistent with all of them. **Not resolved, and no convention chosen** |
| **7** | *The starvation table's final 3/4 value is obviously meant to be 1/4* | BECMI has **no starvation table and no numbers** — only a four-category qualitative sentence. The nearest quantitative figure is *foraging at ½ normal*, a different mechanic | **NOT ESTABLISHED.** BECMI supports neither `1/4` nor `3/4`. The monotonicity intuition is RC-internal reasoning, and this pass supplies no lineage evidence for it. **Not resolved** |

**Summary.** Of the seven common-sense propositions, **one was confirmed** (4), **four were rejected** (3, 5, 6, and 7-as-obvious), and **two were downgraded to "not established"** (1, 2-as-obvious — with 2 nonetheless well supported on lineage grounds). **No question was resolved by intuition standing in for evidence.**

## 12. Candidate Provenance Outcomes

**These are candidate classifications for a future Stage-B provenance decision. None is a final assignment; several require human adjudication and are marked as such.**

| Q | Subject | Candidate provenance | Basis |
|---|---|---|---|
| **1** | Belt pouch `52` vs `55` | **Still unresolved — human ruling candidate.** No `Alternate-Source Compatible Completion` available | The object has no ancestor; there is nothing to complete from |
| **2** | Magic-user dagger | **RC Explicit correction/interpretation** — reading RC Ch. 2 as governing and note `w` on the dagger rows as a tagging defect. **Not** a Compatible Completion: RC already states the rule | Lineage corroborates RC Ch. 2 across two structural units |
| **3** | Suit Armor movement | **Still unresolved — human ruling candidate.** Explicitly **not** a Compatible Completion | The contradiction is inherited; both sides exist upstream and BECMI does not choose between them |
| **4** | Running speed | **RC Explicit correction/interpretation**, reinforced by **Necessary Mechanical Consequence** | RC Ch. 6 already states the rule; BECMI's worked example makes the arithmetic non-optional. Ch. 8's phrasing is a lost qualifier |
| **5** | Mystic `MV` × encumbrance | **Still unresolved — human ruling candidate.** **Not** a Compatible Completion | BECMI is silent; nothing exists to import |
| **6** | Mystic encounter rounding | **Still unresolved — human ruling candidate.** **Not** a Compatible Completion | BECMI's only printed pair is internally inconsistent; importing it would breach an explicit RC rule |
| **7** | Starvation movement column | **Still unresolved — human ruling candidate.** **Not** a Compatible Completion | BECMI supplies categories, not numbers |

**Two questions (2 and 4) could proceed to Stage-B provenance treatment on RC-internal grounds with BECMI as corroboration. Five (1, 3, 5, 6, 7) cannot be closed by lineage evidence.**

**`DEC-0011` item 9 note.** Questions 2 and 4 are the only findings that would **materially resolve** a documented RC defect. Both therefore require the **independent alternate-source completeness review** before any completion is adopted. This researcher **may not** certify the lineage conclusions underlying them as exhaustive or unanimous, and does not.

## 13. Further-Lineage Recommendations

**No further-lineage research was performed, and none is authorized by this document.** `DEC-0011` remains scoped to BECMI for this pass. Recommendations only:

| Q | Recommendation | Reason |
|---|---|---|
| **1** | **PROPOSE NEXT LINEAGE — B/X (Moldvay Basic / Cook Expert)** | Concrete and specific: B/X's Expert equipment list is the direct predecessor of BECMI's, and a `Pouch, belt` entry with capacity and encumbrance **may exist there and have been dropped from BECMI's list while surviving into RC's**. That is a testable hypothesis about a specific table, not a general browse. **If B/X also lacks it, the RC-origin inference in §3 becomes strong** |
| **2** | **STOP — BECMI is sufficient evidence**, even though the final reading is a human call | Two structural units agree; the contested note code is RC-era and has no predecessor to find |
| **3** | **STOP — BECMI is sufficient evidence** | Suit armor is a **Master-set innovation**; there is no earlier lineage in which it exists. Descending to B/X cannot help, because the item did not yet exist |
| **4** | **STOP — BECMI is sufficient evidence** | Resolved at classification `A` with an internal arithmetic cross-check |
| **5** | **PROPOSE NEXT LINEAGE — none useful; STOP at BECMI** | The Mystic is a **Master-set innovation** with no earlier-lineage ancestor. **Descending cannot resolve it.** This is a human-ruling question |
| **6** | **STOP at BECMI** | Same reason as Q5 |
| **7** | **PROPOSE NEXT LINEAGE — B/X (Cook Expert)** | Concrete: BECMI's Expert hunger sentence is a compression of B/X Expert's wilderness survival material, and B/X **may carry the quantified effects BECMI states only qualitatively**. If numbers exist upstream, they would show whether RC's `3/4 / 1/2 / 3/4` is inherited or introduced |

**Three questions (1, 7, and the disposition of 5/6) would benefit from, or are permanently closed to, deeper lineage work. Human governance decides whether to descend. This researcher does not.**

## 14. Researcher Constraint

This pass was performed by the original researcher. Per `DEC-0011` item 9 and `RULE_CARD_RESEARCH_PROTOCOL.md` §10.1.2, the maximum status available is:

```text
BECMI ENUMERATION COMPLETE
SEVEN AUTHORIZED QUESTIONS RESEARCHED
RESEARCHER SELF-REVIEW COMPLETE

AWAITING HUMAN / INDEPENDENT EVIDENCE REVIEW
```

The words **unanimous**, **exhaustive**, **internally consistent** and **absent from the lineage** are **not** used as lineage-level claims anywhere above. Every negative finding names the core source units inspected (§2.3) and is scoped to them.

```text
STAGE B:                    NOT STARTED / NOT AUTHORIZED
FURTHER LINEAGE RESEARCH:   NOT STARTED / NOT AUTHORIZED
SIMULATOR RULINGS:          NONE DRAFTED, NONE PROPOSED
```
