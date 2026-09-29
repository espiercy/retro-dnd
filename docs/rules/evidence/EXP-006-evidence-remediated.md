# `EXP-006` — Light & Exploration Resources — Stage-A Evidence (Remediated, Pass 2)

```text
RULE CARD          EXP-006   Light & Exploration Resources
STAGE              A (EVIDENCE).  Stage B NOT begun, NOT authorized.
PASS               2 -- full DEC-0010 structure-first re-run
SUPERSEDES         docs/rules/evidence/EXP-006-evidence.md  (pass 1, committed e33c4e0)
                   Pass 1 returned PRIMARY-SOURCE COMPLETENESS: FAIL and is preserved
                   unaltered as the audit record of that failure.
PRIMARY SOURCE     D&D Rules Cyclopedia (TSR 1071)
RECOMMENDATION     see section 19
```

> **Why this packet exists.** Pass 1 was independently reviewed under protocol §10.1.2 and
> **failed**. Two of its headline conclusions were falsified by the source: it asserted that
> RC states no consequence for having no light (RC does, at p. 150), and that RC has no
> light-conditioned table (RC does, at p. 93). Three named objects in instruments pass 1
> claimed to have read in full — `Encounter Distances Table . 93`, `Starvation Table . 150`,
> `Timetrack Table . 149` — were never opened.
>
> This pass **does not patch pass 1**. It re-runs the DEC-0010 sequence from the source's own
> structure, and treats pass 1's governing-object list as *not* authoritative. Pass 1's
> Chapter 4 item transcriptions were verified correct by the reviewer and are carried
> forward as evidence; nothing else from pass 1 is assumed.

---

## 1. Rule Card ID / title

`EXP-006` — **Light & Exploration Resources**.

`INVENTORY.md` attributes the source to a *"Dungeon Adventures chapter."* **RC has no chapter
of that name.** Pass 1 found this and it is confirmed: the card's governing material is
distributed across **Chapter 4 (Equipment)**, **Chapter 7 (Encounters and Evasion)** and
**Chapter 13 (Dungeon Master Procedures)**. Pass 1 located only the Chapter 4 part.

---

## 2. Primary source accessed

```text
PAGE IMAGES (authoritative for every mechanically significant object in this packet)
    https://iiif.archive.org/iiif/TSR1071TheDDRulesCyclopedia$<leaf>/full/1400,/0/default.jpg
    leaf = printed_page - 1
OCR (LOCATOR ONLY -- never sole evidence, protocol §9.2/§9.5)
    https://archive.org/stream/TSR1071TheDDRulesCyclopedia/TSR-1071-The-DD-Rules-Cyclopedia_djvu.txt
```

Every page cited in this packet was read **as a page image**. There are **no OCR-only
findings in this packet.** (Pass 1 had OCR-only findings; that is one of the defects
remediated here.)

### 2.1 Correction of a false access claim in pass 1

Pass 1 §7.1 stated that pp. 302–303 could not be verified because of remote `504` responses.
**That statement was false when written** — those images were already on local disk before
pass 1's packet was drafted. The `504`s were real and did occur earlier in the session, but
they did not prevent verification of those pages. Corrected here; pass 1's text is left
standing as the record.

---

## 3. Structure-first inventory (DEC-0010 order, re-run from zero)

### 3.1 Table of Contents — chapters that could govern light / exploration resources

```text
Ch. 4   Equipment                    pp. 62-74    item catalog + item descriptions
Ch. 6   The Adventure (land travel)  pp. 87-90    time, scale, movement, travel
Ch. 7   Encounters and Evasion       pp. 91-101   game turn, encounter distance, evasion
Ch. 13  Dungeon Master Procedures    pp. 144-155  timekeeping, special conditions
Ch. 14  Monsters                     pp. 152-...  special attacks (blindness)
App. 4  Indices                      pp. 301-304  Tables/Checklists index; General Index
```

### 3.2 `Index to Tables and Checklists` (p. 301) — read visually, in full

Entries capable of governing this card, **each dispositioned**:

| Object | Page | Disposition |
|---|---|---|
| `Adventuring Gear Table` | 69 | **OPENED / VISUALLY INSPECTED.** Cost + Enc columns → `CHAR-004` **[LANDED]**. Description column → this card |
| `Encounter Distances Table` | **93** | **OPENED / VISUALLY INSPECTED.** **Light-conditioned.** §5.2. *Missed entirely by pass 1* |
| `Starvation Table` | **150** | **OPENED / VISUALLY INSPECTED.** §5.4. *Missed entirely by pass 1* |
| `Timetrack Table` | **149** | **OPENED / VISUALLY INSPECTED.** §5.5. *Missed entirely by pass 1* |
| `Chance of Encounter Table` | 92 | OPENED. Wandering-monster frequency. **Routed → `EXP-005`/`ENC-001`.** Light is *not* an input to it (§6.3) |
| `Game Turn Checklist` | 91 | **OPENED / VISUALLY INSPECTED.** `EXP-001` **[LANDED]** owns it. Its step 1 is evidence here (§5.3) |
| `Game Day Checklist` | 91 | **OPENED / VISUALLY INSPECTED.** Travel-scale. Routed → wilderness (gated) |
| `Encounter Checklist` | 93 | **OPENED / VISUALLY INSPECTED.** `ENC-001`/`ENC-005` providers |
| `Land Transportation Gear Table` | 70 | OPENED. No light source, no consumable resource. **Excluded** — vehicles/animals, no owner in this cluster |
| `Measurements of Game Time Table` | 87 | OPENED. `EXP-002` **[LANDED]** |
| `Movement, Missile, and Spell Ranges` | 87 | OPENED. `EXP-003`/`CHAR-005` **[LANDED]** |
| `Character Movement Rates and Encumbrance Table` | 88 | `CHAR-005` **[LANDED]**. Not re-derived |
| `Terrain Effects on Movement Table` | 88 | **Excluded** — wilderness terrain; unowned; explicitly not imported (§10) |
| `Traveling Rates by Terrain Table` | 88 | **Excluded** — wilderness travel; gated on the Wilderness reachability decision |
| `Water Movement Modification Table` | 90 | **Excluded** — water travel; out of scope |
| `Forced Marches Table` | 121 | **Excluded** — War Machine / mass movement, not adventurer resources |
| `Room Contents Table` / `Unguarded Treasure Table` | 261 | **Excluded** — `EXP-008`/`TREAS-001` knot, untouched by direction |
| `Passage Table` | 72 | OPENED. Siege equipment. **Excluded** — not a light or exploration resource |
| `Sailing Vessels Table` | 71 | **Excluded** — water transport |
| `Weapons Table` | 62-63 | `CHAR-004` **[LANDED]**. Torch-as-weapon row lives here (§6.5) |
| `Ammunition Table` | 63 | `CHAR-004` **[LANDED]** |
| `Magical Item Subtable: 5. Miscellaneous Items` | 229 | **Excluded** — `MAGIC-*`; magical light is not this card (§6.6) |
| `Natural Events Table` / `Unnatural Events Table` | 142 | **Excluded** — dominion/ruler events, not exploration |
| `Pre-Game Checklist` | 262 | OPENED. DM campaign prep. No mechanic for this card |

**No named table or checklist in the p. 301 index is left undispositioned.** (Guardrail C.)

### 3.3 `General Index` (pp. 302–304) — used as an **enumeration** instrument, not a citation source

Precedent `P-001` applies: this instrument has now caught material **three times** in this
project. Pass 1 used it to cite; this pass enumerates it. Every entry below was read off the
printed index pages and its target **opened**.

| Index entry | Pages | Inspected | Disposition |
|---|---|---|---|
| `Adventuring gear` | **68**-70 | yes | Pass 1 recorded "69–70". The index says **68**–70; p. 68 opened — it is the Armor/Barding tables, no light or resource content. **Harmless, but pass 1's range was narrower than the index's** |
| `Blindness` | **150, 154** | yes | **GOVERNING.** §5.1. *Never followed by pass 1* |
| `Dehydration` | **150** | yes | **GOVERNING** (jointly with Starvation). §5.4 |
| `Starvation` | **150** | yes | **GOVERNING** (boundary). §5.4 |
| `Timekeeping` | **149** | yes | **GOVERNING** (boundary). §5.5 |
| `Torch` | **62, 66, 69, 70** | yes | pp. 69–70 → this card (descriptions). pp. 62, 66 → `CHAR-004` **[LANDED]** weapon rows |
| `Oil` | **62, 65, 69** | yes | p. 69 → this card. pp. 62, 65 → `CHAR-004` **[LANDED]** (oil as thrown weapon) |
| `Rations` | **69** | yes | **GOVERNING.** §5.6. Pass 1 raised rations as an open question without opening the index entry |
| `Food` | **89, 121, 125** | yes | p. 89 travel/foraging (wilderness, gated); p. 121 forced march (War Machine); p. 125 `create food` spell (`MAGIC-*`). **All routed away** |
| `Infravision` | 24, 25 | yes | `CHAR-009` **[UNRESEARCHED]**. Recorded as a cross-reference, **not claimed** (§7.1) |
| `Encounter speed` | 88, 95, 100, 103 | yes | `CHAR-005` **[LANDED]** |
| `Encounters` | 91-96 | yes | `ENC-001` / `EXP-005` |
| `Evasion` | **91**, 98-100 | yes | `ENC-005`. The index's own p. 91 entry is the Game Day Checklist hook |
| `Exploration` | **91** | yes | `EXP-001` **[LANDED]** — the Game Turn |
| `Game time` / `Turns` / `Rounds` / `Days` / `Real time` | 87, 91 | yes | `EXP-002` **[LANDED]** |
| `Feet` / `Yards` / `Map scales` | 87 | yes | `EXP-003` **[LANDED]** |
| `Exhaustion` | 88 | yes | `CHAR-005` §9 **[LANDED]** |
| `Fatigue` | 119 | yes | War Machine morale. **Excluded** |
| `Doors` / `Open doors` / `Secret door` | 10, 147 | yes | p. 147 is Ch. 13 DM procedures on doors; **no light input stated**. Routed → unowned dungeon-interaction responsibility (§8 open item) |
| `Listening` | 147 | yes | Ch. 13. **No light input stated.** Routed |
| `Lost` | **89** | yes | **Wilderness, per-day.** §6.4. Pass 1's finding stands, **refined** by p. 100 (§6.4) |
| `Drowning` / `Swimming` | 89 | yes | Wilderness/water hazard. **Excluded** |
| `Mapping` | 5, 148, 256, 257 | yes | Player-facing advice + DM prep. **No executable mechanic**; no light input |
| `Record keeping` | 148, 149 | yes | **GOVERNING for §5.5's disposition.** DM bookkeeping |
| `Oil of darkness` / `Oil of moonlight` / `Oil of sunlight` | 146 | yes | **Magical** light items, Ch. 12. **Routed → `MAGIC-*`.** Explicitly *not* absorbed (§10) |
| `Invisibility` / `Sleep` / `Stunning` / `Paralysis` / `Prone character` | 150 | yes | Same p. 150 section as Blindness. **Routed → `COMBAT-*`/`CHAR-011`.** §7.2 |
| `Wandering monsters check` | 91 | yes | `EXP-005`. **Light is not an input** — clean negative, §6.3 |

**Enumerated negatives — entries that do not exist.** The RC General Index has **no `Light`
entry, no `Lantern` entry, no `Tinderbox` entry, and no `Flask` entry.** This is a
research-operation fact about the instrument, recorded because it partly explains — but does
not excuse — pass 1's failure to reach p. 93 and p. 150 through the index. The bridge to
those pages runs through `Blindness` and `Torch`, not through `Light`.

---

## 4. Research questions this pass set out to answer

1. What does RC state about light sources' **radius**, **duration**, and **ignition**?
2. **What happens when a party has no light?** (Pass 1 answered "RC says nothing." Falsified.)
3. Does any RC **table or checklist** take light as an input? (Pass 1 answered "none." Falsified.)
4. Does RC supply a **duration/burn-tracking procedure**? (Pass 1's premise was falsified by p. 149.)
5. Do **rations** belong to this card, and what is the resource mechanic if so?
6. Where is the boundary against `CHAR-004`, `EXP-002`, `EXP-003`, `CHAR-009`, `ENC-001`, `CHAR-005`?

---

## 5. Evidence map

Confidence column uses the protocol §6 vocabulary verbatim.

### 5.1 No-light consequences — **RC states them** (p. 150; corroborated p. 154)

| # | Fact | Object | Confidence |
|---|---|---|---|
| E-1 | *"a character without `infravision` may find himself in an area of complete darkness"* is listed by RC as a **cause of blindness** | p. 150 `Blindness`, Ch. 13 `Special Character Conditions` | **PRIMARY TEXT + CROSS-REFERENCE CONFIRMED** (p. 154 restates it; its own stated cross-reference back to Ch. 13 was followed) |
| E-2 | A completely blind character suffers **−4 to all saving throws**, **−6 to all attack rolls**, **+4 penalty to armor class**, for the duration | p. 150 | **DIRECT PRIMARY TEXT** |
| E-3 | Travelling great distances while blind: **one-third normal speed**, and *"whether he is indoors or outdoors, that speed is measured in **feet**, not yards"* | p. 150 | **DIRECT PRIMARY TEXT** |
| E-4 | **Guided by a sighted character: two-thirds** normal rate, measured in yards when outdoors | p. 150 | **DIRECT PRIMARY TEXT** |
| E-5 | A character mounted on a horse suffers **no** movement penalty if someone else guides the horse | p. 150 | **DIRECT PRIMARY TEXT** |
| E-6 | *"Certain monster powers, spells, special actions, or **fighting in the dark without infravision** can result in blindness"* | p. 154 `Blindness`, Ch. 14 `Special Attacks` | **DIRECT PRIMARY TEXT** |

Verbatim, p. 150:

```text
Characters can be blinded by a variety of effects. For example, a light or
continual light spell may be cast directly on a character's eyes, or a character
without infravision may find himself in an area of complete darkness.
    A character who is completely blind, for whatever reason, suffers a -4 penalty
to all saving throws, a - 6 penalty to all attack rolls (he has to guess where his
target is by hearing), and a +4 penalty to his armor class for the duration of his
blindness.
    A character who is forced to travel great distances while blind must move very
slowly. If he is to walk slowly enough that he will not fall down steps and walk
unknowing into pits, he must move at one-third his normal speed . . . and, whether
he is indoors or outdoors, that speed is measured in feet, not yards.
    A blind character who is guided by a sighted character can move safely at
two-thirds his normal rate, and his movement is measured in yards when outdoors.
A character mounted on a horse suffers no movement penalty if someone else is
guiding that horse.
```

**Pass 1's §9 Q2 — *"RC states no consequence for having no light"*, described there as
"the single largest apparent gap in the card" — is FALSE and is withdrawn.**

Aggravating circumstance, recorded because DEC-0010 exists to surface exactly this: the
project had **already transcribed these multipliers**. `CHAR-005` §7 — implemented in
`CLUSTER-003` Slice D this same session — carries the ⅓ / ⅔ blindness rates sourced to
RC Ch. 13 p. 150. Pass 1 copied them into a `NOT V1-WIRED` note and then asserted the
opposite about the same page.

### 5.2 A light-conditioned table **does** exist — `Encounter Distances Table`, p. 93

Transcribed from the page image and confirmed at magnification.

```text
Encounter Distances Table
Setting      Visibility          Encounter    Distance
Dungeon*     Very good light     DM's choice  4d6x 10'
Dungeon*     Dim light**         DM's choice  2d6x 10'
Dungeon*     No light(dagger)    DM's choice  1d4x 10'
Wilderness   Clear daylight      DM's choice  4d6 x 10 yards
Wilderness   Dim light**         DM's choice  2d6 x 10 yards
Wilderness   No light(dagger)    DM's choice  1d4 x 10 yards
Ocean/sea    Clear daylight      Ship         300 yards
Ocean/sea    Clear daylight      Monster      4d6 x 10 yards
Ocean/sea    Dim light**         Ship         120 yards
Ocean/sea    Dim light**         Monster      2d6 X 10 yards
Ocean/sea    No light(dagger)    Ship         40 yards
Ocean/sea    No light(dagger)    Monster      1d4 x 10 yards
Undersea     Any light           DM's choice  1d6 x 10 yards

 *        Or other indoor setting.
 **       Or full darkness with infravision used.
 (dagger) Or very poor visibility (heavy snow or fog, sandstorm, etc.).
```

| # | Fact | Confidence |
|---|---|---|
| E-7 | RC keys encounter distance on a **`Visibility`** column with three light states | **DIRECT PRIMARY TEXT** |
| E-8 | Dungeon: very good light `4d6x10'`; dim light `2d6x10'`; no light `1d4x10'` | **DIRECT PRIMARY TEXT** |
| E-9 | Footnote `**`: **full darkness with infravision used is resolved as `Dim light`** | **DIRECT PRIMARY TEXT** |
| E-10 | Dungeon rows are in **feet**; wilderness/ocean rows in **yards** | **DIRECT PRIMARY TEXT** |
| E-11 | The evasion procedure reaches this table: p. 98 `Contact` — *"They do not have to be near one another, only within **visual range**. When the encounter occurs, the DM determines the **encounter distance**"* | **PRIMARY TEXT + CROSS-REFERENCE CONFIRMED** |

**Pass 1's headline "LIGHT-BEARING TABLES OR CHECKLISTS FOUND: NONE" is FALSE and is
withdrawn.** It was also a Guardrail-B breach: a source-property claim made from keyword
searches without enumerating the Tables Index entry that carried the answer.

### 5.3 The mapping from a lit party to a `Visibility` row — partially stated

| # | Fact | Object | Confidence |
|---|---|---|---|
| E-12 | Game Turn Checklist step 1: wandering monsters appear *"Under **normal dungeon conditions** … **2d6 x 10'** away in a direction of the DM's choice"* | p. 91 | **DIRECT PRIMARY TEXT** |
| E-13 | `2d6 x 10'` is the **`Dim light`** row, and the only Dungeon row bearing that value. Therefore RC treats *"normal dungeon conditions"* as **`Dim light`** | pp. 91 + 93 | **NECESSARY CONSEQUENCE** (derivation: the Dungeon setting has exactly three rows, `4d6x10'` / `2d6x10'` / `1d4x10'`; step 1's value matches exactly one) |

**But the finer mapping is not stated.** RC nowhere defines how many torches or lanterns
produce `Very good light` rather than `Dim light`. E-13 establishes the *default*; it does
not establish a function from carried light sources to a visibility category. Recorded as an
open question (§8 Q3), **not resolved here**.

### 5.4 `Starvation Table`, p. 150 — boundary object, with a **newly discovered printed defect**

```text
Starvation Table
Character Has          Hit Point Loss
No Food                1d2/day
No Water               1d8/day
No Food & No Water     1d10/day

Percentage of hp     Must Rest    Movement     Penalty to
Lost to Starvation   (per day)    Rates        Attack Rolls
  0%-24%             6 hours      No Penalty   No Penalty
 25%-49%             8 hours      X 3/4        -2
 50%-74%            10 hours      X 1/2        -4
 75%-99%            12 hours      X 3/4        -6
```

| # | Fact | Confidence |
|---|---|---|
| E-14 | *"A character begins to starve after one full day without food."* Per full day without food **or** water, roll the indicated die for hp lost | **DIRECT PRIMARY TEXT** |
| E-15 | While starving, the character **cannot heal naturally**, and healing spells do not restore hp lost to starvation **until he is no longer starving** | **DIRECT PRIMARY TEXT** |
| E-16 | Severity is `hp lost to starvation ÷ unmodified hp total`, as a percentage, compared to the table. RC's worked example: 10/32 = 0.3125 ≈ 31% | **DIRECT PRIMARY TEXT** |
| E-17 | The table also applies to monsters (*"You can also use this table to determine the effects of starvation on monsters"*) | **DIRECT PRIMARY TEXT** |
| **E-18** | **PRINTED DEFECT.** The `Movement Rates` column reads `No Penalty` / `× 3/4` / `× 1/2` / **`× 3/4`**. The `75%-99%` row is **less severe than the `50%-74%` row** and identical to `25%-49%`, while every other column in that row worsens monotonically (12 hours rest, −6 attack) | **DIRECT PRIMARY TEXT** — confirmed at magnification on the page image |

**E-18 is NOT a new finding, and this packet does not claim it as one.** It was located by
`CHAR-005` Stage A, recorded there as `RETAINED AS GENUINE SOURCE AMBIGUITY` (Conflict 2),
escalated rather than resolved, and **adjudicated by the human project owner as Simulator
Ruling `SR-10`**:

```text
SR-10   The final x3/4 entry in the RC Starvation Table is a printed defect.
        The progression is  x 3/4  ->  x 1/2  ->  x 1/4.
        OWNER: CHAR-005 §7.  Approved, implemented, merged.
        Guarded by approved cases M57 (75-99% of 120' = 30', "must not be 90'")
        and M58 (multipliers are monotonic).
```

E-18 is therefore recorded here only as **independent visual re-confirmation that RC's
printed value really is `× 3/4`** — the factual premise `SR-10` rests on. **`EXP-006` makes
no claim on it and proposes nothing about it.** An earlier draft of this packet called E-18
a new third printed defect; that was wrong, and the error is recorded rather than quietly
removed, because pass 1 failed in precisely this way — by asserting a source property
without checking what the project had already established.

**Ownership.** This table is **not claimed by `EXP-006`.** Per the governing direction and
`ARCHITECTURE.md` seams:

```text
Starvation CAUSATION (days without food/water -> hp loss)   NO RULE ID EXISTS
Starvation MOVEMENT consequence                             CHAR-005 §7  [LANDED]
Ration supply, spoilage, consumption rate                   EXP-006      (§5.6)
```

The absence of a starvation-causation Rule ID is a **standing open ownership issue**
(`CLUSTER-004-BOUNDARY-CORRECTION.md` §6 item 8), confirmed still true. It is **not** closed
by this packet and **not** absorbed into `EXP-006`.

**Consistency check against landed work — performed, and it passes.** `CHAR-005` §7 was read
directly. It records RC's printed `× 3/4` as the source fact, records the non-monotonicity as
a conflict, and applies `SR-10` to reach `× 1/4` — with the provenance table marking
*"§7 starvation 75–99% = `× 1/4`"* as **Simulator Ruling `SR-10`**, distinct from the three
rows above it marked `Rules Cyclopedia Explicit`. **No silent correction occurred.** The
facts and the ruling are separated exactly as protocol §7 requires.

### 5.5 `Timetrack Table`, p. 149 — a **record-keeping aid**, not a procedure

The table is four printed rows of consecutive integers:

```text
Timetrack Table
Days in a Month    1 .. 28        (then two em-dashes, filling the 30-cell grid)
Hours in a Day     1 .. 24
Turns in an Hour   1 .. 6
Rounds in a Turn   1 .. 60
```

| # | Fact | Confidence |
|---|---|---|
| E-19 | *"Make a **timetrack**, a simple list of numbers, and **mark off time as it passes**. Rounds, turns, hours, and days can thus be accounted for."* | **DIRECT PRIMARY TEXT** |
| E-20 | *"The timekeeping note sheets **can be discarded after the adventure is over**"* | **DIRECT PRIMARY TEXT** |
| E-21 | The table's row lengths encode **28 days/month, 24 hours/day, 6 turns/hour, 60 rounds/turn** | **DIRECT PRIMARY TEXT** |
| E-22 | RC's stated method for tracking a duration: *"As game time passes, deduct from all magical effects durations"*; alternately *"mark on the timetrack the exact game time when the effect disappears. When that much time has been marked off, the DM knows that the spell effect has ended."* | **DIRECT PRIMARY TEXT** |

**Disposition — the question the direction asked.**

```text
The Timetrack Table is PRESENTATION / TRACKING.

It is a physical tally sheet the DM marks off. It is not a procedure, it takes no
input, produces no output, and has no entry or exit condition. It creates NO second
time authority: EXP-002 [LANDED] remains sole authority for dungeon time, and the
Timetrack's row lengths CORROBORATE EXP-002's ratios rather than restating them as a
rival rule.

EXP-006 owns NO executable part of it.
```

**Pass 1's open question — *"does RC supply any duration-tracking procedure?"* — is answered:
RC supplies a manual bookkeeping instrument (E-19, E-22) and no executable decrement
procedure.** The question's premise ("RC is silent") was wrong; its mechanical conclusion
(no procedure to implement) survives, for a different and now-evidenced reason.

E-22 is stated for *magical effect* durations specifically. Whether RC intends the same
instrument for **torch and lantern burn time** is **not stated**; the general Timekeeping
prose (*"keep track of durations of effects, movement, and when foes can enter or leave
combat"*) is broader but does not name light. Recorded as §8 Q4.

### 5.6 Rations — RC states a real, dungeon-conditioned resource mechanic (p. 69)

| # | Fact | Confidence |
|---|---|---|
| E-23 | *"A single ration is enough food to sustain one vigorous adult for a week—that is, about **21 meals**."* | **DIRECT PRIMARY TEXT** |
| E-24 | **Standard rations**: untreated food; last up to a week travelling outdoors. *"Carried into a dank, unhealthy dungeon, **they spoil overnight**."* | **DIRECT PRIMARY TEXT** |
| E-25 | **Iron rations**: preserved; *"last for **two months** (eight weeks) in normal travel and **up to a week in bad conditions** (such as dungeons)"* | **DIRECT PRIMARY TEXT** |
| E-26 | Table rows: `Rations, iron` 15 gp / 70 cn; `Rations, standard` 5 gp / 200 cn | `CHAR-004` **[LANDED]** — not restated as this card's fact |

**This is structurally the same mechanic as torch burn time**: a purchased consumable with a
printed duration that is **shorter inside a dungeon than outside it**. It is the clearest
candidate content for the card's *"& Exploration Resources"* half. **Ownership is still not
claimed here** — that is a Stage-B / human boundary decision (§8 Q5) — but pass 1 raised it
as an open question *without having opened the index entry*, and it is now evidenced.

### 5.7 Light sources — Chapter 4 descriptions (carried forward from pass 1, re-verified)

All four re-read on the page images this pass. The independent reviewer verified these
transcriptions as correct in pass 1; they are unchanged.

| # | Fact | Object | Confidence |
|---|---|---|---|
| E-27 | **Torch**: *"any 1' to 2' long piece of wood, its head sometimes covered with an inflammable substance such as pitch. It casts light in a **30' radius** and burns for **one hour (six turns)**."* | p. 70 | **DIRECT PRIMARY TEXT** |
| E-28 | **Lantern**: *"a simple oil lantern that casts light in a **30' radius**, burning one flask of oil in **four hours (24 turns)**. Most types are shuttered or enclosed against wind."* | p. 69 | **DIRECT PRIMARY TEXT** |
| E-29 | **Oil**: *"Oil is burned in a lantern for light. A flask of oil may also be thrown as a missile weapon or **poured out and ignited to delay pursuit**."* | p. 69 | **DIRECT PRIMARY TEXT** |
| E-30 | **Tinderbox**: *"To use a tinderbox, roll **1d6**; under **normal (comparatively dry) circumstances**, a fire is successfully ignited on a result of **1 or 2**. Someone with a tinderbox may try to use it **once per round**."* | p. 70 | **DIRECT PRIMARY TEXT** |
| E-31 | **Mirror**: *"**The area must be lit** for the mirror to work this way."* (−2 attack penalty when fighting via mirror; cannot use a shield) | p. 69 | **DIRECT PRIMARY TEXT** |

E-31 is **new in this pass** — a second item whose mechanic is explicitly conditioned on
light, found by reading the p. 69 description column as a complete unit (§9.7) rather than
by searching for light terminology.

**Torch and lantern radii are equal (30').** No RC statement distinguishes their
illumination quality, which is what §5.3's open mapping would need.

---

## 6. Whole-source cross-reference pass (§9)

Performed **after** §3's structural work, not instead of it.

### 6.1 Search terms used

```text
light  /  lights  /  lit  /  unlit  /  lantern  /  torch  /  torches  /  flame
fire  /  ignite  /  ignited  /  tinderbox  /  flint  /  burn  /  burns  /  burning
dark  /  darkness  /  dim  /  no light  /  blind  /  blinded  /  blindness
infravision  /  visibility  /  visual range  /  sight  /  see in the dark
radius  /  30'  /  duration  /  turns  /  hours  /  expire  /  goes out
ration  /  rations  /  food  /  water  /  spoil  /  starve  /  starvation  /  dehydration
timetrack  /  timekeeping  /  mark off  /  keep track
```

### 6.2 Cross-references found and followed

| From | To | Followed? | Result |
|---|---|---|---|
| p. 154 `Blindness` → *"See 'Special Character Conditions' in Chapter 13"* | p. 150 | **yes** | §5.1. This is what raises E-1 to `PRIMARY TEXT + CROSS-REFERENCE CONFIRMED` |
| p. 70 `Torch` → *"See the description from the Weapons Table"* | pp. 62–66 | **yes** | `CHAR-004` **[LANDED]**. Torch-as-weapon, not re-opened |
| p. 91 Game Turn step 1 → *"see the 'Encounter Distance' section, below"* | pp. 92–93 | **yes** | §5.2, §5.3. **Pass 1 did not follow this** |
| p. 93 Encounter Checklist step 5c → *"use the pursuit and evasion rules later this chapter"* | pp. 98–100 | **yes** | `ENC-005` entry condition |
| p. 91 Game Day step 4b → *"the DM goes to the 'Evasion and Pursuit' section"* | pp. 98–100 | **yes** | `ENC-005` entry condition |
| p. 98 `Contact` → *"the DM determines the encounter distance"* | p. 93 | **yes** | E-11 — the printed link from evasion back to the light-conditioned table |
| p. 69 `Oil` → *"poured out and ignited to delay pursuit"* | pp. 98–100 | **yes** | **RC states no mechanic.** No adjustment, no delay value, no Evasion Table row. Recorded from both sides; nothing invented |
| p. 150 `Blindness` → *"without `infravision`"* | pp. 24–25 | **yes, to ownership only** | `CHAR-009` **[UNRESEARCHED]**. §7.1 |
| p. 149 Timekeeping → *"mark on the timetrack"* | p. 149 table | **yes** | §5.5 |

### 6.3 Negative results — recorded as research operations, not as source properties (Guardrail B)

- **Light is not an input to wandering-monster frequency.** p. 91 lists what raises the check
  rate: *"Loud noises, battles, cursed items, or exploring special areas."* Light is absent
  from that list, and the `Chance of Encounter Table` (p. 92) has no light column. **Not
  located after inspecting p. 91, p. 92 and the p. 301 Tables Index.**
- **No RC rule makes carried light a surprise or reaction modifier.** Not located after
  inspecting the Encounter Checklist steps 2 and 4 (p. 93), the `Monster Reactions Table`
  (p. 93) and the General Index entries `Surprise . 92, 93` and `Reaction . 93, 262`.
- **No RC rule states what happens when a torch or lantern burns out mid-turn.** Not located
  after inspecting pp. 69–70, p. 91, p. 149 and the `Timetrack Table`. RC gives durations and
  a tally instrument, and stops.
- **No RC rule states an ignition chance for non-normal (wet) circumstances.** p. 70 qualifies
  its 1-in-3 to *"normal (comparatively dry) circumstances"* and supplies no other figure.
  Not located after inspecting pp. 69–70, p. 89 (weather/travel) and the General Index.

### 6.4 `Lost . 89` — pass 1's finding, **refined by p. 100**

Pass 1 concluded: *"RC provides no dungeon getting-lost mechanic; `Becoming Lost` is per-day,
wilderness, and sits in the Game Day Checklist."* Confirmed at p. 91 (Game Day step 2:
*"Getting Lost: DM rolls 1d6 … If so, see the 'Land Travel' section in Chapter 6"*).

**Refinement.** p. 100 `Regain Bearings` states that a dungeon party *can* end up lost — *"their
attempts at evasion could have carried them deep into unknown territory (such as … unexplored
dungeon levels), and **now the characters are lost**; they'll have to explore their way back
to the areas they know."* So RC states the **condition** in a dungeon, at DM discretion, while
supplying a **die-roll procedure** only for wilderness travel. The pass-1 claim is narrowed
from "no dungeon getting-lost material" to "**no dungeon getting-lost procedure**."

### 6.5 Chapter 4 boundary against `CHAR-004` **[LANDED]** — unchanged and not reopened

```text
p. 69 TABLE   cost, encumbrance                       ->  CHAR-004  [LANDED]
p. 69-70 PROSE  radius, burn time, ignition, spoilage ->  EXP-006
```

No price, encumbrance, `Coin`, quantity-pricing or legality fact is restated or re-derived
in this packet. Pass 1's finding that RC states radius/duration **only** in the descriptions
and cost/encumbrance **only** in the table is confirmed.

### 6.6 Magical light — enumerated and routed, not absorbed

`Oil of darkness`, `Oil of moonlight`, `Oil of sunlight` (p. 146), and the `light` /
`continual light` spells named at p. 150. All **routed to `MAGIC-*`**. Opened only far enough
to confirm they are Chapter 12 magical items and Chapter 3 spells, i.e. that they are not
Chapter 4 equipment. **No magical light mechanic is transcribed into this packet.**

---

## 7. Ownership and boundary findings

### 7.1 What `EXP-006` does **not** absorb

```text
Encounter generation / distance    ENC-001.  EXP-006 supplies a light state; it does
                                   NOT own the Encounter Distances Table, its dice,
                                   or when it is consulted.  (§9 guardrail)
Surprise / Reaction / Initiative   ENC-002 / ENC-003 / COMBAT-006.  Untouched.
Blindness CAUSATION generally      p. 150 covers spell-blinding, monster powers and
                                   darkness together.  EXP-006 owns at most the
                                   DARKNESS PATH INTO it, never the condition itself.
Generic condition infrastructure   p. 150's Deafness / Invisibility / Paralysis /
                                   Prone / Sleep / Stunning are NOT claimed.
Starvation causation               No Rule ID exists.  NOT absorbed.  §5.4
Infravision                        CHAR-009.  Recorded, not claimed.
Movement arithmetic                CHAR-005 [LANDED] owns rates; EXP-003 [LANDED]
                                   owns ordinary dungeon movement.  Not re-derived.
Dungeon time                       EXP-002 [LANDED].  No second authority created.
EXP-004 / EXP-010 / stocking knot  DEFERRED.  Not researched.
```

### 7.2 The seam this pass actually establishes

```text
EXP-006  owns  ->  whether a light source is LIT, its RADIUS, its REMAINING DURATION,
                   whether it can be IGNITED, and (candidate) ration supply/spoilage.

              ->  It therefore PRODUCES a party light state.

CHAR-009 owns ->  whether a character has infravision at all.

ENC-001  owns ->  the Encounter Distances Table, which CONSUMES a Visibility
                  category (Very good light / Dim light / No light).

CHAR-005 owns ->  the blindness movement multipliers (§7, landed) that the
                  no-light path triggers.
```

**The unstated link is the arrow from "party light state" to "Visibility category."** RC
gives the default (E-13) and the infravision case (E-9) and nothing between. That gap is
`EXP-006`-shaped, and it is §8 Q3.

---

## 8. Unresolved questions (protocol §10.2 vocabulary, verbatim)

| # | Question | Disposition |
|---|---|---|
| Q1 | Does a party with torches produce `Very good light` or `Dim light`? RC states only that *"normal dungeon conditions"* = `2d6x10'` = `Dim light` (E-13), and that infravision in full darkness also = `Dim light` (E-9). No rule distinguishes 1 torch from 6, or a torch from a lantern (both 30'). | **RETAINED AS GENUINE SOURCE AMBIGUITY** — all governing objects (p. 91, p. 93, pp. 69–70, p. 301 index) inspected; RC simply does not state it |
| Q2 | Is a burn-tracking procedure in scope? RC gives durations (E-27, E-28) and a **manual tally instrument** (E-19, E-22), and no executable decrement or expiry rule. | **RESOLVED BY SOURCE INSPECTION** as to the source-property question (RC supplies no procedure). The **scope** half is a Stage-B/human decision, not an evidence gap |
| Q3 | Is E-22's timetrack method intended for **light durations**, or only magical-effect durations? RC names only magical effects explicitly; the surrounding Timekeeping prose is broader. | **RETAINED AS GENUINE SOURCE AMBIGUITY** |
| Q4 | Do **rations** belong to this card? Evidence now exists (E-23–E-25): a dungeon-conditioned consumable duration, structurally parallel to torch burn time. | **CONFIRMED OUT OF SCOPE for Stage A** — this is a card-boundary decision reserved to the human owner. Ownership **not claimed**; answering it here would be silent scope expansion |
| Q5 | Tinderbox ignition outside *"normal (comparatively dry) circumstances"* (E-30). | **RETAINED AS GENUINE SOURCE AMBIGUITY.** `PRIMARY PROCEDURE NOT YET ESTABLISHED` for non-normal conditions |
| Q6 | `Starvation Table` `75%-99%` movement reads `× 3/4`, non-monotonic (E-18). | **CONFIRMED OUT OF SCOPE** — owned by `CHAR-005` §7 and **already adjudicated** as `SR-10`. `EXP-006` re-confirmed the printed value visually and claims nothing further |
| Q7 | Does landed `CHAR-005` §7 record RC's printed `× 3/4`, or a silently corrected value? | **RESOLVED BY SOURCE INSPECTION.** It records the printed value as RC Explicit and the `× 1/4` separately as `SR-10`. **No defect in the landed card** |
| Q8 | Who owns starvation **causation**? No Rule ID exists anywhere in `INVENTORY.md`. | **CONFIRMED OUT OF SCOPE** — standing open ownership issue, `BOUNDARY-CORRECTION` §6 item 8. Confirmed still true |
| Q9 | Does light modify surprise, reaction, or wandering-monster frequency? | **RESOLVED BY SOURCE INSPECTION — negative.** §6.3, with the objects inspected named |
| Q10 | What happens when a light source burns out mid-turn? | **RETAINED AS GENUINE SOURCE AMBIGUITY** — RC gives durations and stops |

**There are zero silent unresolved research tasks at this gate.** Every item pass 1 left
open is dispositioned in §8.1.

### 8.1 Required reconciliation table (§10.2.1) — pass 1's own open statements

| Pass-1 open question | Source region implicated | Inspection completed? | Result | Owner | Still blocks completeness? |
|---|---|---|---|---|---|
| Q7 "tinderbox non-normal circumstances" | pp. 69–70, 89 | **yes** | RC gives no second figure | `EXP-006` | No — genuine ambiguity |
| Q8 **"RC states no consequence for having no light"** | **pp. 150, 154** | **yes** | **FALSIFIED.** RC states it (§5.1) | `CHAR-005` §7 / `EXP-006` path | **No — resolved** |
| Q9 "do rations belong to this card?" | p. 69, index `Rations . 69` | **yes** | Evidenced (§5.6); ownership still a human call | human | No |
| Q10 "is a burn-tracking procedure in scope?" | **p. 149**, pp. 69–70 | **yes** | RC supplies a tally aid, no procedure (§5.5) | `EXP-006` | No |
| Pass-1 claim "no governing table or checklist" | **p. 93**, p. 301 index | **yes** | **FALSIFIED** (§5.2) | `ENC-001` owns the table | **No — resolved** |
| Pass-1 claim "Tables Index read visually in full" | p. 301 | **yes** | **Instrument was read; three entries on it were not followed.** §3.2 now dispositions all | — | No |
| Pass-1 §7.1 "pp. 302–303 unverified due to 504s" | pp. 302–303 | **yes** | **FALSE when written**; images were local. §2.1 | — | No |

---

## 9. Primary-Source Coverage Checklist (§9.3 — required)

### 9.1 Structural units inspected

```text
VISUALLY INSPECTED (page images)
    p. 68    Ch. 4   Armor / Barding tables            (index said gear = 68-70)
    p. 69    Ch. 4   Adventuring Gear Table + descriptions A-S
    p. 70    Ch. 4   descriptions S-W; Land Transportation
    p. 91    Ch. 7   Exploration and the Game Turn; Game Turn & Game Day Checklists
    p. 92    Ch. 7   Chance of Encounter Table
    p. 93    Ch. 7   Encounter Checklist; ENCOUNTER DISTANCES TABLE; Monster Reactions
    p. 98    Ch. 7   Evasion and Pursuit; Definitions; Contact
    p. 99    Ch. 7   Evasion Checklist; Evasion Table
    p. 100   Ch. 7   Regain Bearings; Evasion at Sea; Ship Evasion Table
    p. 104   Ch. 8   Combat Maneuvers Table (for the ENC-005 boundary)
    p. 149   Ch. 13  Timekeeping; TIMETRACK TABLE; Record keeping
    p. 150   Ch. 13  Special Character Conditions: BLINDNESS; STARVATION TABLE
    p. 154   Ch. 14  Special Attacks: Blindness
    p. 301   App. 4  Index to Tables and Checklists   -- read in full
    p. 302   App. 4  General Index  A-H               -- read in full
    p. 303   App. 4  General Index  H-S               -- read in full
    p. 304   App. 4  General Index  S-Z               -- read in full
```

### 9.2 Named tables / checklists — Guardrail C attestation

| Object | OPENED | VISUALLY INSPECTED | DISPOSITIONED |
|---|---|---|---|
| `Adventuring Gear Table` (69) | yes | yes | split `CHAR-004` / `EXP-006` |
| `Encounter Distances Table` (93) | yes | yes | governing input; owner `ENC-001` |
| `Starvation Table` (150) | yes | yes | boundary; owner `CHAR-005` §7 + unowned causation |
| `Timetrack Table` (149) | yes | yes | presentation/tracking; no owner claim |
| `Game Turn Checklist` (91) | yes | yes | `EXP-001` **[LANDED]**; step 1 is evidence |
| `Game Day Checklist` (91) | yes | yes | travel scale; gated |
| `Encounter Checklist` (93) | yes | yes | `ENC-001`; step 5c routes to `ENC-005` |
| `Chance of Encounter Table` (92) | yes | yes | `EXP-005`; no light input |
| `Monster Reactions Table` (93) | yes | yes | `ENC-003`; excluded |
| `Land Transportation Gear Table` (70) | yes | yes | excluded, reason stated §3.2 |
| `Riding Animal Costs Table` (70) | yes | yes | excluded — `CHAR-004`-shaped, no owner in cluster |

### 9.3 Deliberate exclusions, with reasons

```text
Wilderness travel tables (88, 90)        Gated on the Wilderness reachability decision.
Terrain Effects on Movement (88)         Unowned; explicitly NOT imported (guardrail).
Forced Marches (121)                     War Machine mass movement, not adventurers.
Magical light items (146) + spells       MAGIC-*; opened only to confirm chapter.
Room Contents / Unguarded Treasure (261) EXP-008 / TREAS-001 knot -- untouched by direction.
City / Castle encounter subtables (97-98) EXP-008 / MON-001 -- excluded by name.
Ship Evasion Table (100)                 Naval; ENC-005-adjacent, not EXP-006.
p. 150 Deafness/Invisibility/Paralysis/  Same section as Blindness; COMBAT-*/CHAR-011.
  Prone/Sleep/Stunning                   Read, not claimed.
```

### 9.4 Unresolved items

All ten are in §8, each carrying a §10.2 disposition. **None is unfinished source
inspection disguised as ambiguity.**

---

## 10. Falsification pass (§10)

| Tentative conclusion | Falsification attempted | Outcome |
|---|---|---|
| *"RC states no no-light consequence"* (pass 1) | Opened `Blindness . 150, 154` from the General Index | **REJECTED — falsified.** §5.1 |
| *"No light-conditioned table exists"* (pass 1) | Opened every Ch. 7 entry in the p. 301 Tables Index | **REJECTED — falsified.** §5.2 |
| *"RC supplies no duration-tracking procedure"* (pass 1's premise) | Opened `Timetrack Table . 149` | **PREMISE REJECTED**, conclusion survives on new evidence. §5.5 |
| "The Timetrack is a second time authority" | Compared its ratios to landed `EXP-002`; read the surrounding Timekeeping prose | **REJECTED.** It is a tally sheet; ratios corroborate, do not rival |
| "*Normal dungeon conditions* = `Very good light`" | Compared p. 91 step 1's `2d6x10'` against all three Dungeon rows | **REJECTED.** `2d6x10'` is uniquely the `Dim light` row (E-13) |
| "Torch radius differs from lantern radius" | Re-read both descriptions as complete units | **REJECTED.** Both 30' |
| "The Starvation Table's `× 3/4` at 75–99% is an OCR artifact" | Magnified the page image | **REJECTED.** The defect is **printed** (E-18) |
| "Light modifies surprise / reaction / wandering-monster rate" | Inspected pp. 91–93 + the named tables + index entries | **NOT LOCATED** after those inspections (§6.3) |

---

## 11–18. Remaining §11 report contents

- **(11) Conclusions rejected** — pass 1's Q2 and its "no light-bearing table" claim; see §10.
- **(12) Unresolved RC questions** — §8, Q1–Q10.
- **(13) Questions belonging to another card** — §7.1.
- **(14) Alternate-source research required?** — **No.** Every question in §8 is either a
  fully mapped RC ambiguity or a governance/ownership decision. **No RC gap in `EXP-006`
  currently justifies a `DEC-0011` request.** (`ENC-005`'s two p. 99 defects remain the only
  flagged candidate, and are that card's.)
- **(15) Possible Simulator Ruling areas** — **none proposed.** Q1 and Q5 are the only
  mechanical gaps, and protocol §16 places rulings after gap-directed alternate-source
  research, which is neither authorized nor performed.
- **(16) `REVALIDATION_REQUIRED` legacy-card withholding** — **not applicable.** `EXP-006`
  carries no approved legacy card; no legacy specification was consulted.
- **(17) Access limitations** — earlier in this session the IIIF endpoint returned intermittent
  `504`s; p. 88 required four attempts this pass. **All pages cited were ultimately obtained
  as images.** No finding in this packet rests on OCR. (See §2.1 for pass 1's false claim
  about this.)
- **(18) Overall confidence** — **High** for §5.1, §5.2, §5.4, §5.5, §5.7 (all `DIRECT PRIMARY
  TEXT` from page images, several cross-reference-confirmed). **Moderate** for §5.3's E-13,
  which is a `NECESSARY CONSEQUENCE` with its derivation shown. The card's principal
  remaining uncertainty is Q1, which is a genuine source silence, not a coverage gap.

---

## 19. Recommendation

```text
EVIDENCE READY FOR HUMAN REVIEW
```

subject to the mandatory §10.1.2 **independent completeness review of this remediated
packet** (pass 2), which has been requested separately and whose verdict is recorded in
`docs/rules/evidence/CLUSTER-004-stage-a-completeness-review-2.md`.

**Stage B has not begun and is not authorized. No Rule Card is drafted. No production code
is touched.**

**No new printed RC defect was found by this card.** E-18 re-confirms a defect already owned,
escalated and adjudicated as `SR-10` under `CHAR-005`. The cluster's printed-defect count
remains **two**, both in `ENC-005`, both unadjudicated.

The substantive matters for the human reviewer are:

```text
1. Q1   RC does not state how a party's carried light maps to a Visibility
        category beyond the default (Dim light) and the infravision case.
        Genuine source silence, fully mapped.  Bears on whether EXP-006 can
        produce the input ENC-001's table consumes.

2. Q4   Whether RATIONS belong to this card.  Evidence now exists (E-23 - E-25);
        the ownership decision is reserved to the human owner and is NOT taken here.

3. Q8   Starvation CAUSATION still has no Rule ID anywhere in INVENTORY.md.
        Confirmed still true.  NOT absorbed into EXP-006.
```
