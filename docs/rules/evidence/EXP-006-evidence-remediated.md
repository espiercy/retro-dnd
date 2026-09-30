# `EXP-006` — Light & Exploration Resources — Stage-A Evidence (Remediated, Pass 2)

```text
RULE CARD          EXP-006   Light & Exploration Resources
STAGE              A (EVIDENCE).  Stage B NOT begun, NOT authorized.
PASS               5 -- remediates the FOURTH independent review's findings: the rest
                   of Chapter 5 (pp. 84-86), the DEC-0008 error, and p. 92's
                   terrain-keyed pointer.
SUPERSEDES         docs/rules/evidence/EXP-006-evidence.md  (pass 1, committed e33c4e0)
                   Pass 1 returned PRIMARY-SOURCE COMPLETENESS: FAIL and is preserved
                   unaltered as the audit record of that failure.
REVIEW HISTORY     pass 1  FAIL   CLUSTER-004-stage-a-completeness-review.md
                   pass 2  FAIL   CLUSTER-004-stage-a-completeness-review-2.md
                   pass 3  FAIL   CLUSTER-004-stage-a-completeness-review-3.md
                   pass 4  FAIL   CLUSTER-004-stage-a-completeness-review-4.md
                   pass 5  pending fifth independent review
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

**Every page that carries an evidence row (`E-1` … `E-40`) in this packet was read as a page
image**, and **no finding in this packet rests on OCR**. Pass 1 had OCR-only findings; that is
one of the defects remediated here.

**Qualification, added in pass 3.** Pass 2's blanket phrasing — *"every page cited … was read as
a page image"* — overstated the record, because §3.2 and §3.3 also mark pages `OPENED` that were
reached only far enough to establish **ownership or exclusion**, without an image:

### 2.2 RC p. 84 — a defective derivative, and the second scan that resolved it

**This is recorded because passes 3 and 4 claimed p. 84 was inspected and it was not.**

```text
DEFECT   In the scan this project has used throughout
         (archive.org item TSR1071TheDDRulesCyclopedia, leaf 83),
         printed p. 84 renders COLUMNS 2 AND 3 BLANK.  Header and footer
         decoration are present; the body text of those columns is not.

VERIFIED as a stable property of that derivative, not a transient 504:
         /full/1400,/   /full/max/   /pct:50,0,50,100/   /full/2000,/gray
         default.png -- all HTTP 200, full payloads up to 1.05 MB, all blank.
         The archive.org OCR truncates at the SAME point, mid-sentence:
         "In areas not normally rich in game he must make a " -> jumps to p. 85.

RESOLVED by a SECOND, INDEPENDENT SCAN:
         archive.org item  rules-cyclopedia,  leaf 83  (same leaf offset).
         Printed p. 84 renders complete.  Its content is at §5.8b.
```

This is **not** an alternate *source* under `DEC-0011` — it is the same edition, the same
printing, the same primary source, obtained through a different digitisation. No
`SOURCE_HIERARCHY` question arises. Had the second scan also failed, the required response was
§9.2's `STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED`, and this packet could not have been
declared complete.

```text
IMAGE-VERIFIED, carries evidence rows
    68, 69, 70, 81, 82, 83, 88, 91, 92, 93, 98, 99, 100, 104, 108,
    149, 150, 154, 301, 302, 303, 304

OPENED VIA OCR ONLY, for routing/exclusion, carrying NO evidence row
    72, 121, 142, 146, 147, 229, 261, 262, 24-25, 89, 125
    Each is EXCLUDED or ROUTED in §3.2/§3.3.  None supports a mechanical claim.
    Per §9.6 line 7 these are LOCATOR-level reads, and they are labelled as such
    rather than presented as inspections.
```

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
| `Chance of Encounter Table` | 92 | **OPENED / VISUALLY INSPECTED.** Wandering-monster frequency. **Routed → `EXP-005`/`ENC-001`.** Light is *not* an input to it (§6.3) |
| `Attack Roll Modifiers Table` | **108** | **OPENED / VISUALLY INSPECTED — pass 3.** Carries `Attacker can't see target −4`. **Routed → `COMBAT-*`.** §5.9. *Missed by passes 1 and 2* |
| `Sample Skills Table` | **82** | **OPENED / VISUALLY INSPECTED — pass 3.** Names `Fire-Building`, `Blind Shooting`. **Routed → `CHAR-012`.** §5.8. *Missed by passes 1 and 2* |
| `Attack Rolls Table: All Characters` / `All Monsters` | 106-107 | OPENED. THAC0 progression. **Excluded** — `COMBAT-*`; carries no sight or light circumstance |
| `Target Cover Table` | 108 | **OPENED / VISUALLY INSPECTED.** Cover, **not** darkness — *"soft"*/*"hard"* cover only. **Excluded**, reason stated |
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

**Research-operation statement (Guardrail B), corrected in pass 3.** The p. 301 index was read
**entry by entry** in pass 3, and every entry above is dispositioned. Pass 2 asserted *"No named
table or checklist in the p. 301 index is left undispositioned"* — **an unqualified
source-property claim, and it was false**: `Attack Roll Modifiers Table . 108` and
`Sample Skills Table . 82` were both on that index and both outside the list. They are added at
§5.9 and §5.8. The claim is restated as an operation, not a property: *every entry on p. 301 was
read and each one relevant to light, exploration resources, time or condition consequences is
dispositioned above or in §9.2.*

### 3.3 `General Index` (pp. 302–304) — used as an **enumeration** instrument, not a citation source

Precedent `P-001` applies: this instrument has now caught material **three times** in this
project. Pass 1 used it to cite; this pass enumerates it. Every entry below was read off the
printed index pages and its target **opened**.

| Index entry | Pages | Inspected | Disposition |
|---|---|---|---|
| `Adventuring gear` | **68**-70 | yes | Pass 1 recorded "69–70". The index says **68**–70, and it is right: p. 68 carries Suit Armor, Barding, the `Barding Table` and `Barding Encumbrance Table` **and** — in its third column — the `Adventuring Gear` heading and the **start of `Adventuring Gear Descriptions`** (`Backpack`, `Boots`). **The descriptions section begins on p. 68, not p. 69.** No light source or consumable resource is among the items that start there, so **no `EXP-006` content was lost** by pass 1's narrower range; but the range was wrong and the section boundary is now stated correctly |
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
| `Doors` / `Open doors` / `Secret door` | 10, 147 | yes | p. 147 is Ch. 13 DM procedures on doors; **no light input stated**. **Routed → `EXP-005`**, which `INVENTORY.md` assigns this responsibility. *(Pass 2 called it "unowned" and pointed at a non-existent §8 item; both corrected in pass 3)* |
| `Listening` | 147 | yes | Ch. 13, same page. **No light input stated.** **Routed → `EXP-005`** |
| `Lost` | **89** | yes | **Wilderness, per-day.** §6.4. Pass 1's finding stands, **refined** by p. 100 (§6.4) |
| `Drowning` / `Swimming` | 89 | yes | Wilderness/water hazard. **Excluded** |
| `Mapping` | 5, 148, 256, 257 | yes | Player-facing advice + DM prep. **No executable mechanic**; no light input |
| `Record keeping` | 148, 149 | yes | **GOVERNING for §5.5's disposition.** DM bookkeeping |
| `Oil of darkness` / `Oil of moonlight` / `Oil of sunlight` | 146 | yes | **Magical** light items, Ch. 12. **Routed → `MAGIC-*`.** Explicitly *not* absorbed (§10) |
| `Invisibility` / `Sleep` / `Stunning` / `Paralysis` / `Prone character` | 150 | yes | Same p. 150 section as Blindness. **Routed → `COMBAT-*`** for the combat penalties; the **general status-condition responsibility has no Rule ID** in `INVENTORY.md`, exactly as `CLUSTER-003`'s open question 8 records, and none is invented here. *(Pass 4 routed these to `CHAR-011`, which is **Weapon Mastery**. Wrong ID, corrected in pass 5.)* |
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
| **E-11a** | **The table is GATED ON SURPRISE.** p. 92 `Encounter Distance`: *"When **both** parties are surprised, the encounter distance is **`1d4 x 10'`** (or yards if outdoors). When **one** party is surprised, the unsurprised party notices the surprised party at the `1d4 x 10'` … distance rolled; the surprised party won't notice the unsurprised party until they reach **half that distance**. When **neither** party is surprised, **take a look at the Encounter Distances Table**."* | **DIRECT PRIMARY TEXT** |

**E-11a is the governing procedure the light-conditioned table sits inside** (protocol §8: a
numeric fact must be interpreted inside its governing procedure, not treated as
free-floating). **RC consults the `Visibility` column only when neither side is surprised.**
When either side is surprised, distance is a flat `1d4 x 10'` and **light does not enter the
calculation at all**.

| # | Fact | Object | Confidence |
|---|---|---|---|
| **E-11b** | p. 92's own pointer into the table is phrased on **terrain/setting**, not on light: *"take a look at the Encounter Distances Table. **When the type of terrain (dungeon, wilderness, ocean/sea, or underwater) is known**, the DM can find out how far apart the groups are"* | p. 92 | **DIRECT PRIMARY TEXT** |

**E-11b qualifies this packet's seam claim and is added in pass 4.** The `Visibility` column is
printed and real (E-7), but **RC's own prose introduces the table by its `Setting` column.**
`EXP-006` should not overstate how central light is to that lookup: the table is indexed by
both, RC's narrative emphasis is on setting, and the light row is selected within a setting.
§7.2's arrow from *light state* to *Visibility category* stands, and is **narrower** than pass 3
implied.

This narrows `EXP-006`'s relevance to encounter distance considerably, and it is a
qualification that a reader of the p. 93 table alone would not see. It also means the light
state's mechanical consequence is **conditional on `ENC-002`'s output** — reinforcing, not
weakening, the routing at §7.1: `EXP-006` supplies a light state and owns none of this.

**Pass 1's headline "LIGHT-BEARING TABLES OR CHECKLISTS FOUND: NONE" is FALSE and is
withdrawn.** It was also a Guardrail-B breach: a source-property claim made from keyword
searches without enumerating the Tables Index entry that carried the answer.

### 5.3 The mapping from a lit party to a `Visibility` row — partially stated

| # | Fact | Object | Confidence |
|---|---|---|---|
| E-12 | Game Turn Checklist step 1: wandering monsters appear *"Under **normal dungeon conditions** … **2d6 x 10'** away in a direction of the DM's choice"* | p. 91 | **DIRECT PRIMARY TEXT** |
| E-13 | `2d6 x 10'` is the `Dim light` row's value, and the only Dungeon row bearing it | pp. 91 + 93 | **DIRECT PRIMARY TEXT** (the value match is a reading of two printed tables) |
| E-13a | **The inference that RC therefore *classifies* "normal dungeon conditions" as `Dim light` is QUALIFIED, not forced** | pp. 91, 92, 93 | see below |

**E-13 was classified `NECESSARY CONSEQUENCE` in pass 2. That classification is withdrawn in
pass 3**, because the falsification pass never tested it against two passages this packet
itself transcribes:

```text
p. 91 step 1 states 2d6 x 10' UNCONDITIONALLY for wandering monsters under normal
      dungeon conditions.  It cites the "Encounter Distance" section but does not
      say it is reading the Dim light row.

p. 92 (E-11a) states that the Encounter Distances Table is consulted ONLY when
      NEITHER party is surprised -- and p. 91 step 1 imposes no surprise condition
      at all.
```

So p. 91 step 1 may be a **standing default that bypasses the table**, rather than an
application of its `Dim light` row. A `NECESSARY CONSEQUENCE` must be *logically forced* by two
`DIRECT PRIMARY TEXT` facts (§6); this is not forced — it is the more plausible of two readings.
**Downgraded.** The value match is recorded; the classification claim is withdrawn.

**And the finer mapping is not stated either way.** RC nowhere defines how many torches or
lanterns produce `Very good light` rather than `Dim light`. Recorded as §8 Q1, **not resolved**.

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

**Pass 1's open question — *"does RC supply any duration-tracking procedure?"* — is answered,
and the answer needs stating precisely** (pass 2's phrasing was in tension with its own E-22):

```text
RC DOES supply a METHOD:  mark the timetrack, or deduct from durations as time passes
                          (E-19, E-22).  It is addressed to a human DM with a pencil.

RC does NOT supply an EXECUTABLE PROCEDURE in the sense this project implements:
                          no decrement step tied to a checklist position, no expiry
                          rule, no statement of what happens at the moment a duration
                          reaches zero.
```

So the premise of pass 1's question ("RC is silent") was **wrong**; and the useful conclusion
is **not** "there is no procedure" but "the procedure RC gives is human bookkeeping, and it
stops short of the expiry semantics an implementation would need." That gap is §8 Q10.

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

| # | Fact | Object | Confidence |
|---|---|---|---|
| E-32 | **Waterskin/wineskin**: *"This flexible container is usually made of leather or a preserved animal bladder. It has a liquid capacity of **one quart** and an encumbrance of 30 cn when filled, 5 cn when empty."* | p. 70 | **DIRECT PRIMARY TEXT** |

**E-32 is added in pass 3.** It is the **water-side consumable** answering to `Dehydration . 150`
(E-14: `No Water 1d8/day`, worse than `No Food`'s `1d2`). Pass 2 marked that index entry
`GOVERNING` while recording no container for water — an asymmetry with rations (§5.6) that had
no justification. One quart is **not** a stated day's supply; RC gives capacity and encumbrance
and **no consumption rate for water at all**. Recorded as §8 Q11.

### 5.8 Chapter 5 `General Skills` (pp. 81–86) — an **optional** system that bears on two of this card's conclusions

**Pass 2 never inspected Chapter 5.** It was surfaced by the second independent review, which
reached it by reading the p. 301 Tables Index entry by entry. `Sample Skills Table . 82` is a
named object in that index.

| # | Fact | Object | Confidence |
|---|---|---|---|
| E-33 | **RC** classifies the system as optional: *"Using general skills is **optional**. If the DM doesn't want to use them in his or her campaign, they won't be used."* | p. 81 | **DIRECT PRIMARY TEXT** |
| **E-33a** | **The project has already decided this.** `INVENTORY.md`'s `CHAR-012` row reads: *"RC Optional/Additional system → **Project-Selected: REQUIRED (`DEC-0008`)**"* | `INVENTORY.md`, `DEC-0008` | **repository fact, not a source fact** |
| E-34 | A skill check is **`1d20` against the governing ability score**; *"If the roll on the 1d20 is **equal to or less than** the ability score, the skill use succeeds. A roll of **20 always fails**"* (p. 82), and — **p. 86** — *"**A natural roll of 1 on 1d20 is an automatic success**, just as a roll of 20 is an automatic failure"* | pp. 82, 86 | **DIRECT PRIMARY TEXT** |
| E-35 | `Sample Skills Table` assigns the governing ability: **`Fire-Building` → Intelligence**, **`Blind Shooting` → Dexterity**, `Caving` → Wisdom, `Endurance` / `Food Tasting` → Constitution, `Survival` / `Tracking` / `Hunting` → Intelligence | p. 82 | **DIRECT PRIMARY TEXT** |
| **E-41** | **A third sightlessness modifier.** p. 86 `Positive and Negative Modifiers`: circumstances making a job very hard — *"such as **not being able to see**, working on the rolling deck of a ship during a severe storm"* — *"can warrant penalties of **+5, +10, or even +15** to the roll"* (added, because the roll is under-the-score) | p. 86 | **DIRECT PRIMARY TEXT** |
| **E-42** | **`Survival (choose terrain)`**: *"allows the character to easily find food …, **shelter, and water** in a single type of terrain, selected from … desert, forest/jungle, mountain/hill, open sea, plains, arctic."* Forages automatically in fertile areas; supplying others costs *"a **+1** penalty … for **each additional person**"*; *"He must roll **each day**"* | p. 85 | **DIRECT PRIMARY TEXT** |
| E-43 | **`Hunting`** and **`Tracking`** exist as separate Intelligence skills; `Tracking`'s success chance varies by *"age of the tracks, **type of terrain**, number of tracks"* | pp. 84–85 | **DIRECT PRIMARY TEXT** |

#### E-33a — a correction this packet must make about itself

**Pass 3 wrote that the general-skills system's status was an open project question, and escalated
it to the human owner as a newly discovered optional system. That was false.** `DEC-0008`
selected General Skills as **project-REQUIRED**, and `INVENTORY.md`'s `CHAR-012` row says so in
terms. This packet's own §7.1 and `ENC-005`'s §7.1 both cite `DEC-0008` correctly for `ENC-004`
in the same breath.

**Consequences, applied throughout pass 4:**

```text
WITHDRAWN   "General skills NOT IN USE -> RC supplies nothing" as a live V1 branch.
            DEC-0008 settled it.  The branch is a statement about RC's own framing,
            not about this simulator's configuration.

THEREFORE   Fire-Building's adverse-condition procedure (E-36) is IN FORCE for V1.
            Caving's step-6 lost determination (ENC-005 N-28) is IN FORCE for V1,
            including "characters without this skill automatically become lost."

WITHDRAWN   ENC-005's escalation of a "newly discovered optional system" to the
            human owner.  BOUNDARY-CORRECTION §6 item 2 remains correctly closed.
```

This is the third time in this cluster that a claim was asserted without opening the artifact
that refutes it — pass 1 against the source, pass 2 against the p. 301 index, pass 3 against the
project's own registry. **Recorded rather than quietly fixed.**
| **E-36** | **`Fire-Building`**: *"This is the ability to start a fire **without a tinderbox**. A character **with a tinderbox and this skill** is able to start fires **automatically (no roll necessary) in ordinary conditions**. If the character is trying to build a fire **without** a tinderbox, he will eventually succeed; he must make a `1d6` roll each round, and on a **1 or 2** he ignites the fire. If the character is trying to build a fire **in adverse conditions (during high winds or using wet wood), he must make a skill check with penalties assigned by the DM**."* | p. 83 | **DIRECT PRIMARY TEXT** |
| **E-37** | **`Blind Shooting`**: *"the ability to shoot at a target without being able to see it; it is typically used when the character is **in darkness** or when the target is outside the range of his sight or infravision. The character must be able to **hear** the target… If the character makes his skill check, he can then fire at the target; he needs an attack roll to hit the target, but **the character doesn't suffer the normal darkness penalties**."* | p. 83 | **DIRECT PRIMARY TEXT** |
| E-38 | `Food Tasting`: *"the ability to taste food and water to see if they have **spoiled**"* — avoids food poisoning | p. 83 | **DIRECT PRIMARY TEXT** |

#### What E-36 does to this packet's own conclusions

**Pass 2's §8 Q5 is falsified as stated.** Q5 read `PRIMARY PROCEDURE NOT YET ESTABLISHED` for
tinderbox use outside *"normal (comparatively dry) circumstances."* **RC establishes one**: a
`Fire-Building` skill check with DM-assigned penalties (E-36). Withdrawn.

**The procedure is in force for V1** (E-33a — `DEC-0008` selected General Skills as
project-REQUIRED), and it has a **quantified** penalty scale, which pass 3 did not have because
it never opened p. 86:

```text
character HAS Fire-Building, ordinary conditions, with tinderbox
    -> AUTOMATIC ignition, no roll

character HAS Fire-Building, adverse conditions (high winds, wet wood)
    -> skill check: 1d20 <= Intelligence, DM-assigned penalty ADDED to the roll
    -> p. 86 scales that penalty: +1/+2 slightly harder, +3/+4 substantially,
       +5/+10/+15 very hard
    -> natural 1 always succeeds; natural 20 always fails   (E-34)

character LACKS Fire-Building
    -> p. 70 tinderbox rule governs: 1d6 each round, ignite on 1-2, and it is
       qualified to "normal (comparatively dry) circumstances" and stops there
    -> RC states NOTHING for a skill-less character in adverse conditions
```

**So Q5's gap narrows rather than closing completely**: RC now answers the adverse-conditions
question **for characters who have the skill**, and remains silent for those who do not. That
residue is recorded at §8 Q5 rather than smoothed over.

**E-30 is qualified accordingly**, not replaced: the p. 70 tinderbox rule is the
non-optional-system rule, and E-36 supersedes it for characters who have the skill.

**Ownership: `CHAR-012` [UNRESEARCHED]**, explicitly, not by silence. `EXP-006` owns *whether a
light source can be ignited*; `CHAR-012` owns the skill system that modifies the attempt.
**`EXP-006` does not absorb the general-skills system**, and no skill mechanic is claimed here.

#### What E-37 does

**`Blind Shooting` is the prior review's Finding E-6, unremediated by pass 2 and remediated
here.** Its phrase *"the normal darkness penalties"* is RC referring to its own §5.1 blindness
penalties **as darkness penalties**, from a third chapter. It is therefore additional
`PRIMARY TEXT + CROSS-REFERENCE CONFIRMED` support for E-1: RC treats *being in the dark* and
*being blind* as the same mechanical state, in Chapters 5, 13 and 14 independently.

Ownership of the skill is `CHAR-012`'s; the missile attack is `COMBAT-*`'s. **Neither is claimed.**

### 5.8a `Survival`, `Hunting`, `Tracking` (pp. 84–85) — the food/water skills, enumerated in pass 4

Pass 3 opened only pp. 81–83 — the three pages it had been quoted text from — and then wrote
*"Chapter 5 (81-86) opened and dispositioned."* **That inspection claim was false, and it is
corrected here.** pp. 84–86 were opened in pass 4, and the `Sample Skills Table` was read **row
by row** rather than for the five rows already named to it.

`Survival` (E-42) is the object that matters: a **per-day, per-person, penalty-scaled procedure
for finding food, shelter and water**, sitting in the same responsibility space as this card's
rations (§5.6) and waterskin (E-32). `Hunting` supplies food automatically in fertile areas and
by skill check elsewhere (E-43).

```text
DISPOSITION:  CONFIRMED OUT OF SCOPE for EXP-006, owner CHAR-012 [UNRESEARCHED].

Survival and Hunting are TERRAIN-SELECTED WILDERNESS skills -- desert, forest/jungle,
mountain/hill, open sea, plains, arctic.  NO DUNGEON TERRAIN is offered.  They are
gated behind the standing Wilderness reachability decision as well.

EXP-006 owns PURCHASED, CARRIED consumables and their durations.  It does not own
skill-based resupply, and it does not absorb the general-skills system.
```

**They are recorded rather than omitted**, because Q11 asks where RC puts water supply, and the
honest answer is *"in a wilderness skill this card does not own"* — not *"nowhere."*

`Tracking` (E-43) is routed to `ENC-005` as bearing on its N-17 (*"the pursuers fail to follow
their tracks"*), and to `CHAR-012` for ownership.

### 5.8b RC p. 84 — the columns nobody had read, now inspected (pass 5)

Obtained from the second scan (§2.2). Four `Sample Skills Table` rows that passes 3–4 swept into
a blanket *"excluded as unrelated"* actually live here, and one of them is light-conditioned.

| # | Fact | Confidence |
|---|---|---|
| **E-44** | **`Lip Reading`**: *"The distance to the target and **the available light** should be taken into account—the DM should apply skill roll penalties for difficult situations."* | **DIRECT PRIMARY TEXT** |
| **E-45** | **`Hunting`**, in full: automatic food supply *"if he is in a fairly fertile area and has a missile weapon, spear, or javelin. **In areas not normally rich in game he must make a skill roll and receive penalties to that roll (penalties determined by the DM)**"*; supplying others costs *"a **- 1** penalty for each additional person after the first"*; *"He must roll **each day**"* | **DIRECT PRIMARY TEXT** |
| **E-46** | **`Mapping (Cartography)`**: *"**A character does not have to have this skill in order to map a dungeon as the characters explore it.**"* | **DIRECT PRIMARY TEXT** |
| **E-47** | **`Navigation`**: works *"By taking directions from the position of **the sun and the stars**"* — outdoor determination of position | **DIRECT PRIMARY TEXT** |
| **E-48** | **`Nature Lore`**: per-terrain (desert, forest, jungle, mountain/hill, open sea, plains, arctic) knowledge including *"edible and poisonous plants"*; `−2` in home territory, up to `+4` penalty far from it | **DIRECT PRIMARY TEXT** |
| E-49 | **`Mountaineering`**: rope-and-piton climbing; *"does not replace a thief's special climbing ability"* | **DIRECT PRIMARY TEXT** |

**E-44 is a fourth light-conditioned mechanic in RC**, after the p. 93 Encounter Distances Table,
the p. 69 mirror (E-31) and the p. 86 *"not being able to see"* modifier (E-41). Like E-31 it is
an item/skill whose use RC gates on illumination. **Owner `CHAR-012`; not claimed.**

**E-45 completes the sentence the OCR cut in half** and confirms `Hunting` is the same
shape as `Survival` — per-day, per-person, DM-penalised, wilderness-facing. Same disposition:
**`CONFIRMED OUT OF SCOPE`, owner `CHAR-012`**, gated on Wilderness reachability.

**E-46 is a clean negative and it matters to `ENC-005`.** That card's N-22 branches on whether the
party had *"already knew or **had mapped**"* the area. RC says mapping a dungeon **requires no
skill**, so N-22's condition creates **no `CHAR-012` dependency**. Routed to `ENC-005`.

**E-47 pairs with `Caving`**: `Navigation` is the *outdoor* "where am I" skill and `Caving` the
*underground* one (`ENC-005` N-28). This confirms `ENC-005`'s step-6 routing rather than
complicating it.

E-48 and E-49 are **excluded**: terrain knowledge and climbing, neither a light source, a
carried consumable, nor a duration.

### 5.9 `Attack Roll Modifiers Table` (p. 108) — a named table carrying a second sightlessness penalty

**Pass 2 never opened p. 108**, although its own §6.2 followed a p. 104 cross-reference *to*
p. 108 and recorded it as routed. The table is a named object in the p. 301 Tables Index.

```text
Attack Roll Modifiers Table
Circumstance                                  Attack Roll Modifier
Attacking from behind                          +2 bonus*
Attacker can't see target                      -4 penalty
Larger than man-sized monster attacks halfling -1 penalty
Target exhausted                               +2 bonus
Attacker exhausted                             -2 penalty

* Ignore defender's shield
```

| # | Fact | Confidence |
|---|---|---|
| **E-39** | `Attacker can't see target` — **`−4` penalty** | **DIRECT PRIMARY TEXT** |
| E-40 | The table also carries `Target exhausted +2` and `Attacker exhausted −2`, under the note *"Characters may become **exhausted from running or overexertion**, as described in **Chapter 7**"* | **DIRECT PRIMARY TEXT** |

#### E-39 against E-2 — recorded, **not resolved**

```text
RC states a sightlessness modifier in THREE places, in three different chapters,
at three different magnitudes, against three different roll types:

p. 150  Ch. 13  a completely blind character   "-6 penalty to all attack rolls"
p. 108  Ch. 8   Attacker can't see target      "-4 penalty"      (attack roll)
p.  86  Ch. 5   "not being able to see"        "+5, +10, or +15" (SKILL roll;
                                                added, because skill rolls are
                                                roll-under)      -- E-41
```

**The p. 86 instance was added in pass 4** and is the one the second review predicted would be
missed: it is the penalty scale that E-36's *"penalties assigned by the DM"* actually refers to,
so this packet was relying on it while never having opened it.

It is **not** a fourth value in the same conflict — it modifies a **skill roll**, not an attack
roll, so it does not compete with `−6`/`−4`. It is recorded because a card that owns *whether
there is light* must enumerate every place RC attaches a consequence to there not being any.

**Both are printed. `EXP-006` does not decide which governs, and does not decide whether they
compose or conflict.** They may be the same rule stated twice at different values (an audit
class-I duplicate presentation), or two different conditions — *completely blind* is a
character state, *can't see target* is a per-attack circumstance, and a lit room with an
invisible opponent satisfies the second without the first. RC's `Invisibility` entry on p. 150
supplies exactly that case at **`−6`**, which cuts against the clean reading.

```text
DISPOSITION:  CONFIRMED OUT OF SCOPE
              owner COMBAT-* [UNRESEARCHED], with CHAR-005 §7 [LANDED] holding
              the movement half of the p. 150 condition.

EXP-006 produces a LIGHT STATE.  It has never owned the numerical attack, save or
AC consequences of that state, and does not claim them now.  Stage A's obligation
for an object it does not own is to ENUMERATE, INSPECT and ROUTE it -- which this
section does.  The reasoning is argued in full at §8.2.

The relationship itself is genuinely unresolved, and the OWNING card will inherit a
§10.2.2 case-1 situation when it reaches Stage A: conflicting passages found AND
potentially governing objects (the Chapter 8 attack-roll procedure, the Chapter 13
condition set) still uninspected.  Everything it needs is recorded above.

A packet that chose a number here would trip §17's
STOP -- INTERNAL SOURCE CONFLICT REQUIRES REVIEW.  This one does not choose.
```

**Ownership: `COMBAT-*` [UNRESEARCHED]**, with `CHAR-005` §7 holding the movement half of the
p. 150 condition. `EXP-006` records the object and routes it. See §8 Q12.

#### E-40 — a routed finding for another card, reported not absorbed

The p. 108 exhaustion rows are a **duplicate presentation** of landed `CHAR-005` §9's material
(RC p. 88). `CHAR-005` §9 records, from p. 88, that an exhausted character *"must subtract 2
from all **damage** rolls."* **p. 108 places its `−2` in an `Attack Roll Modifier` column.**

**This is reported, not adjudicated, and not absorbed.** `CHAR-005` is an approved, implemented
card whose evidence packet cites p. 88 and not p. 108, so the tension appears to be unrecorded
there. It is **out of this cluster's authorized scope**; flagged for the human owner as §8 Q13.

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
  from that list. The `Chance of Encounter Table` (p. 92) was **opened and read visually**: its
  columns are `Type of Encounter` / `Roll Method`, plus a `Type of Terrain` / `Chance`
  sub-table. **It has no light or visibility column.** Not located after inspecting p. 91,
  p. 92 and the p. 301 Tables Index.
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
| Q5 | Tinderbox ignition outside *"normal (comparatively dry) circumstances"* (E-30). | **RESOLVED BY SOURCE INSPECTION for skill-havers** (E-36 + E-41's penalty scale; `DEC-0008` makes the system V1-required, E-33a). Pass 2's `PRIMARY PROCEDURE NOT YET ESTABLISHED` is **withdrawn**. **RETAINED AS GENUINE SOURCE AMBIGUITY for a character without `Fire-Building` in adverse conditions** — RC states nothing, and all governing objects (pp. 70, 81–86) are now inspected |
| Q11 | Water supply and consumption. | **Restated in pass 4.** RC gives the `Waterskin` a one-quart capacity (E-32) and **no consumption rate**; `Dehydration` costs `1d8/day`, the harshest Starvation Table row. **`Survival` (E-42) supplies water** — but only in one chosen **wilderness** terrain (desert, forest/jungle, mountain/hill, open sea, plains, arctic; **no dungeon**), per day, at `+1` per additional person. So: **RETAINED AS GENUINE SOURCE AMBIGUITY for the dungeon case**, and **CONFIRMED OUT OF SCOPE for the wilderness case**, which is `CHAR-012`'s skill gated on the Wilderness reachability decision |
| Q12 | p. 150's `−6` (completely blind) against p. 108's `−4` (attacker can't see target) — same rule at two values, or two conditions? p. 150's `Invisibility` entry gives `−6` for a sighted attacker who cannot see his foe, which cuts against the clean reading. | **CONFIRMED OUT OF SCOPE**, ownership `COMBAT-*` **[UNRESEARCHED]**, with `CHAR-005` §7 holding the movement half. **Reasoning stated at §8.2** |
| Q13 | p. 88 says an exhausted character subtracts `2` from **damage** rolls; p. 108's table puts `−2` in the **attack roll** column. Landed `CHAR-005` §9 cites p. 88 and appears not to have opened p. 108. | **CONFIRMED OUT OF SCOPE** — `CHAR-005` / `COMBAT-*`. Reported to the human owner, **not adjudicated, not absorbed** |
| Q6 | `Starvation Table` `75%-99%` movement reads `× 3/4`, non-monotonic (E-18). | **CONFIRMED OUT OF SCOPE** — owned by `CHAR-005` §7 and **already adjudicated** as `SR-10`. `EXP-006` re-confirmed the printed value visually and claims nothing further |
| Q7 | Does landed `CHAR-005` §7 record RC's printed `× 3/4`, or a silently corrected value? | **RESOLVED BY SOURCE INSPECTION.** It records the printed value as RC Explicit and the `× 1/4` separately as `SR-10`. **No defect in the landed card** |
| Q8 | Who owns starvation **causation**? No Rule ID exists anywhere in `INVENTORY.md`. | **CONFIRMED OUT OF SCOPE** — standing open ownership issue, `BOUNDARY-CORRECTION` §6 item 8. Confirmed still true |
| Q9 | Does light modify surprise, reaction, or wandering-monster frequency? | **RESOLVED BY SOURCE INSPECTION — negative.** §6.3, with the objects inspected named |
| Q10 | What happens when a light source burns out mid-turn? | **RETAINED AS GENUINE SOURCE AMBIGUITY** — RC gives durations and stops |

**There are zero silent unresolved research tasks at this gate**, and — after pass 3 —
**zero `BLOCKED` rows.** Every item pass 1 left open is dispositioned in §8.1.

### 8.2 Why Q12 is `CONFIRMED OUT OF SCOPE` and not `BLOCKED`

This distinction decides whether the packet may recommend `EVIDENCE READY` at all (§17), so it
is argued rather than asserted.

```text
A BLOCKED row would mean: EXP-006 cannot be evidence-complete until the p. 108 / p. 150
attack-penalty relationship is resolved.

That is not true.  EXP-006's responsibility is WHETHER A LIGHT SOURCE IS LIT -- its
radius, its remaining duration, whether it can be ignited.  It PRODUCES a light state.
It has never owned, and does not now claim, the numerical CONSEQUENCES of that state:

    movement multipliers from blindness    CHAR-005 §7   [LANDED]
    attack / save / AC penalties           COMBAT-*      [UNRESEARCHED]

Stage A's obligation for an object it does not own is to ENUMERATE, INSPECT and ROUTE it
(§9.1, §9.8).  Pass 3 does all three: p. 108 is opened, transcribed, and routed with the
conflict recorded in full at §5.9 for the owning card to inherit.
```

**What would have been illegitimate** is to leave p. 108 unenumerated — which is precisely what
passes 1 and 2 did, and why the object is here at all. The failure was coverage, and coverage is
now discharged. **When `COMBAT-*` reaches Stage A it will inherit a `§10.2.2` case-1 situation**,
and §5.9 records everything needed for it.

`EXP-006` does **not** decide which number governs, and the packet contains no attack-penalty
mechanic.

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

**This list and §3.2/§3.3 are reconciled in pass 3** (pass 2's checklist named 17 pages while
§3.3 implied more were opened, so the checklist was not the auditable record §9.3 requires).
The split between image-verified pages and locator-level reads is stated at §2; **only the
pages below carry evidence rows.**

```text
VISUALLY INSPECTED (page images)
    p. 81    Ch. 5   General Skills -- "Using general skills is optional"
    p. 82    Ch. 5   How Skills Are Used; SAMPLE SKILLS TABLE
    p. 83    Ch. 5   Fire-Building; Blind Shooting; Food Tasting; (Caving, Endurance
                     -- read here, routed to ENC-005/CHAR-012)
    p. 84    Ch. 5   Hunting (full); Lip Reading; Mapping/Cartography; Navigation;
                     Nature Lore; Mountaineering; Military Tactics; Knowledge; Labor
                     -- SECOND SCAN, see §2.2                           -- pass 5
    p. 85    Ch. 5   Survival; Tracking; Stealth; Piloting Skill: Types of
                     Vessels Table                                      -- pass 4
    p. 86    Ch. 5   Positive and Negative Modifiers (E-41); natural-1 rule;
                     Improving/Learning Skills; Skill Slot Acquisition
                     (Humans) and (Demihumans) Tables; Skills and the DM;
                     Time Use; Using Skills Together / Against Each Other  -- pass 4
    p. 88    Ch. 6   Exhaustion + running rules   (CHAR-005 §9 [LANDED]; for E-40)
    p. 108   Ch. 8   ATTACK ROLL MODIFIERS TABLE; Target Cover Table
    p. 68    Ch. 4   Suit Armor; Barding + Barding Encumbrance Tables; START of
                     "Adventuring Gear Descriptions" (Backpack, Boots)
    p. 69    Ch. 4   Adventuring Gear Table + descriptions A-S
    p. 70    Ch. 4   descriptions S-W; Land Transportation
    p. 91    Ch. 7   Exploration and the Game Turn; Game Turn & Game Day Checklists
    p. 92    Ch. 7   Chance of Encounter Table; ENCOUNTER DISTANCE section (E-11a);
                     surprise 1d6 rule and its three outcomes
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
| `Sample Skills Table` (82) | yes | yes | **read ROW BY ROW in pass 4.** `Fire-Building`, `Blind Shooting`, `Food Tasting` → this card's evidence; `Caving`, `Endurance` → `ENC-005`; `Survival`, `Hunting`, `Tracking` → §5.8a; all remaining rows inspected and **excluded as unrelated to light, time or exploration resources**. Skill ownership `CHAR-012` |
| `Skill Slot Acquisition (Humans) Table` (86) | yes | yes | **excluded** — skill acquisition/progression, wholly `CHAR-012` |
| `Skill Slot Acquisition (Demihumans) Table` (86) | yes | yes | **excluded** — same |
| `Piloting Skill: Types of Vessels Table` (85) | yes | yes | **excluded** — water/air transport |
| `Barding Table` (68) | yes | yes | excluded — mount armor, `CHAR-004`-shaped; no light or resource content |
| `Barding Encumbrance Table` (68) | yes | yes | excluded — mount encumbrance; `CHAR-005`/`CHAR-004` shaped |

### 9.3 Deliberate exclusions, with reasons

```text
Wilderness travel tables (88, 90)        Gated on the Wilderness reachability decision.
Terrain Effects on Movement (88)         Unowned; explicitly NOT imported (guardrail).
Forced Marches (121)                     War Machine mass movement, not adventurers.
Magical light items (146) + spells       MAGIC-*; opened only to confirm chapter.
Room Contents / Unguarded Treasure (261) EXP-008 / TREAS-001 knot -- untouched by direction.
City / Castle encounter subtables (97-98) EXP-008 / MON-001 -- excluded by name.
Ship Evasion Table (100)                 Naval; ENC-005-adjacent, not EXP-006.
p. 150 Deafness/Invisibility/Paralysis/  Same section as Blindness.  Combat penalties
  Prone/Sleep/Stunning                   -> COMBAT-*.  The general status-condition
                                         responsibility has NO Rule ID; none invented.
                                         Read, not claimed.
General skills system (81-86)            OPTIONAL system owned by CHAR-012.  Opened and
                                         dispositioned (§5.8); Fire-Building and Blind
                                         Shooting recorded as evidence bearing on this
                                         card's conclusions.  NO skill mechanic claimed,
                                         and the system itself is NOT absorbed.
Attack Roll Modifiers Table (108)        Opened and transcribed; routed to COMBAT-*.
                                         The -4 / -6 relationship is NOT resolved.
Target Cover Table (108)                 Cover, not darkness.  Excluded.
Attack Rolls Tables (106-107)            THAC0 progression; no sight circumstance.
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
| *"RC establishes no procedure for igniting a fire in adverse conditions"* (pass 2 Q5) | **Pass 3:** read the p. 301 Tables Index entry by entry; opened `Sample Skills Table . 82` and Ch. 5 | **REJECTED — falsified.** `Fire-Building`, p. 83 (E-36) |
| *"No named table in the p. 301 index is undispositioned"* (pass 2 §3.2) | **Pass 3:** same operation | **REJECTED — falsified.** Two were missing (§5.8, §5.9) |
| E-13 as a `NECESSARY CONSEQUENCE` | **Pass 3:** tested against p. 91 step 1's unconditional phrasing and against this packet's own E-11a surprise gate | **DOWNGRADED.** Not logically forced; the classification is withdrawn (§5.3) |
| "p. 108's `−4` and p. 150's `−6` are the same rule stated twice" | Checked p. 150's `Invisibility` entry, which gives `−6` for a sighted character who cannot see his foe | **NOT ESTABLISHED.** The clean duplicate reading does not survive; recorded unresolved and routed (§5.9) |

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
- **(17) Access limitations** — two, both stated rather than smoothed over:
  1. The IIIF endpoint returns intermittent `504`s; p. 88 needed four attempts, p. 104 about
     twenty. All eventually succeeded. (See §2.1 for pass 1's **false** claim about this.)
  2. **RC p. 84's derivative in the primary scan renders columns 2–3 blank, and the OCR
     truncates at the same point.** Passes 3 and 4 asserted the page was inspected; it was not.
     **Resolved in pass 5 from a second, independent scan of the same edition** — see §2.2 and
     §5.8b. Had it not resolved, §9.2's `STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED` applied.

  **No finding in this packet rests on OCR.**
- **(18) Overall confidence** — **High** for §5.1, §5.2, §5.4, §5.5, §5.7, §5.8 and §5.9 (all
  `DIRECT PRIMARY TEXT` from page images, several cross-reference-confirmed). **Lower for
  §5.3's E-13a**, which pass 3 downgraded from `NECESSARY CONSEQUENCE` to a qualified reading
  after testing it. The card's principal remaining uncertainty is Q1 — a genuine source
  silence, not a coverage gap.

---

## 19. Recommendation

```text
EVIDENCE READY FOR HUMAN REVIEW
```

subject to the mandatory §10.1.2 **third independent completeness review**. Per §10.1.2 the
original researcher may **not** restore a ready status on its own certification, so this
recommendation is a submission, not a verdict.

**Pass 3 remediation of the second review's findings:**

```text
 1  Attack Roll Modifiers Table (p. 108) opened, transcribed, routed       §5.9
 2  Chapter 5 (81-86) opened; Fire-Building, Blind Shooting, Sample
    Skills Table dispositioned; Q5 withdrawn; E-30 qualified; CHAR-012
    named explicitly                                                      §5.8
 3  §2's blanket page-image claim qualified; locator-only reads listed     §2
 4  §9.1 reconciled with §3.2/§3.3                                         §9.1
 5  E-13 downgraded from NECESSARY CONSEQUENCE and re-derived              §5.3
 6  Waterskin added as the dehydration-side consumable                     E-32
 7  §3.2 closure sentence restated as a research operation; p. 147
    routed to EXP-005; dangling §8 reference removed                       §3.2/§3.3
 8  §5.5 / E-22 tension resolved by stating method vs procedure            §5.5
 9  Hard-stop vocabulary no longer used as an inline label                 §8
13  Adversarial self-review re-run FROM the p. 301 index, entry by entry   §10
```

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
