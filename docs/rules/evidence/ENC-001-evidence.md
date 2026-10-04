# `ENC-001` — Encounter Distance — Stage-A Evidence

> **Re-entered under `DEC-0013`** (approved 2026-10-04). This packet replaces the
> `DEC-0012`-format packet at `b880ffd`. The substantive research is **reused, not
> re-done**: two independent reviews confirmed the Encounter Distances Table transcription
> exact, all eight index absences true, every repository fact checked true, the
> `ENC-001`/`ENC-002` boundary intact, and **no rules-conformance defect**. Those
> conclusions stand unless new inspection contradicts them, and none did.
>
> The `DEC-0012` pilot is over and its result is historical: Review #1 `FAIL`, Review #2
> `FAIL`, criteria 3 and 4 failed. The review that follows this packet is the **first**
> `DEC-0013` semantic review, not a third review under a closed pilot.

```text
PACKET-STATUS
RULE-ID:              ENC-001
INDEPENDENT-REVIEW:   PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
RECOMMENDATION:       EVIDENCE READY FOR HUMAN REVIEW
```

---

## 1. Scope and Seams

**This card owns:** how far apart two groups are when an encounter takes place.

**It does not own, and routes to:** `ENC-002` — surprise determination; `ENC-005` — evasion
and pursuit, including pursuit **starting** distance; `EXP-001` — whether an encounter
occurs; `EXP-006` — mundane light sources; `EXP-008`/`MON-001` — which monster;
`COMBAT-*` — attack-roll effects of cover and sight; `MAGIC-*` — magical light.

**Neighbour Rule IDs:** derived from `INVENTORY.md` edges in both directions. `ENC-001`'s
own row carries an em dash in both dependency columns, so the forward walk yields nothing;
`ENC-005`'s row names `ENC-001` in its notes, and that reverse edge is what reaches the
accepted packets. No seam needed declaring.

**Subject terms:** encounter distance, visibility, surprise, infravision, feet, yards.

## 2. Primary Source

| Source | Access method | Role |
|---|---|---|
| *D&D Rules Cyclopedia* (TSR, 1991; ISBN 1-56076-085-0) | page images — `https://iiif.archive.org/iiif/TSR1071TheDDRulesCyclopedia$<leaf>/full/1400,/0/default.jpg`, `leaf = printed_page − 1` | authoritative |
| OCR / full text | **not used at any point in this packet** | not used |

**Access limitations:** None encountered. Every page recorded `INSPECTED` below was read as
a page image and confirmed by its body text, not by HTTP status.

## 3. Seeds

```text
SEEDS
SUBJECT-TERMS:  encounter distance, visibility, surprise, infravision
SEAMS:          none
LEADS:          infravision -> 24, 25
```

> `SEAMS: none` is deliberate and is itself a finding: the `INVENTORY.md` reverse edge
> alone reaches `ENC-005` and `EXP-006`, so the externally-derived obligation set needed no
> researcher declaration at all. The tool derived **43** pages; §4 dispositions every one.

## 4. Page Dispositions

```text
PAGE-DISPOSITIONS
3: INSPECTED
24: INSPECTED
25: INSPECTED
26: INSPECTED
27: INSPECTED
62: ROUTED_EXTERNAL EXP-006                 # Ch. 4 equipment catalog
66: ROUTED_EXTERNAL COMBAT-*                # weapons table
68: ROUTED_EXTERNAL CHAR-004                # armor / barding
69: ROUTED_EXTERNAL EXP-006                 # lantern and oil descriptions
70: ROUTED_EXTERNAL EXP-006                 # torch, tinderbox
81: ROUTED_EXTERNAL CHAR-012                # general skills
82: ROUTED_EXTERNAL CHAR-012                # Sample Skills Table
83: ROUTED_EXTERNAL CHAR-012                # Caving, Endurance
84: ROUTED_EXTERNAL CHAR-012                # skill descriptions
85: ROUTED_EXTERNAL CHAR-012                # Tracking
86: ROUTED_EXTERNAL CHAR-012                # skill slot acquisition
87: INSPECTED
88: ROUTED_EXTERNAL CHAR-005                # movement rates, exhaustion
89: ROUTED_EXTERNAL EXP-004                 # travel, foraging, drowning
91: INSPECTED
92: INSPECTED
93: INSPECTED
94: INSPECTED
95: INSPECTED
96: INSPECTED
97: INSPECTED
98: INSPECTED
99: ROUTED_EXTERNAL ENC-005                 # Evasion Checklist, Evasion Table
100: INSPECTED
101: IRRELEVANT_AFTER_INSPECTION            # Balancing Encounters (Optional) -> ENC-007
103: ROUTED_EXTERNAL ENC-004                # Morale Scores Table
104: ROUTED_EXTERNAL COMBAT-*               # Retreat / Fighting Withdrawal
108: INSPECTED
115: INSPECTED
119: ROUTED_EXTERNAL ENC-004                # War Machine; morale at mass scale
121: ROUTED_EXTERNAL EXP-004                # forced march
125: ROUTED_EXTERNAL MAGIC-*                # create food spell
143: ROUTED_EXTERNAL EXP-002                # Ch. 13 timekeeping
145: ROUTED_EXTERNAL MAGIC-*                # Demihuman Clan Relics
146: ROUTED_EXTERNAL MAGIC-*                # oils of darkness / moonlight / sunlight
147: ROUTED_EXTERNAL EXP-005                # doors, listening
149: ROUTED_EXTERNAL EXP-002                # Timetrack
150: INSPECTED
152: ROUTED_EXTERNAL MON-003                # Ch. 14 monster statistics
153: INSPECTED
154: ROUTED_EXTERNAL COMBAT-*               # special defenses, blindness in combat
215: INSPECTED
300: OUTSIDE_CARD_SCOPE MAGIC-*             # Index to Spells
301: INSPECTED
302: INSPECTED
303: INSPECTED
304: INSPECTED
305: INSPECTED
```

> 43 pages were externally derived; 9 more are dispositioned because this packet cites
> them. **No page here rests on an uninspected claim about RC content**: a `ROUTED_EXTERNAL`
> line asserts only *whose* responsibility the page carries, established from the accepted
> packet that cited it, not what the page says.

## 5. Governing Objects

| Object | Page | Kind | Disposition | Owner |
|---|---|---|---|---|
| Encounter Distances Table | 93 | table | GOVERNING | |
| "Encounter Distance" prose section | 92 | prose | GOVERNING | |
| Game Turn Checklist step 1 | 91 | checklist | GOVERNING | |
| "Wandering Monsters" prose | 91 | prose | GOVERNING | |
| "Feet vs. Yards" / Distance | 87 | prose | GOVERNING | |
| "Encounters" definition (visual range) | 91 | prose | GOVERNING | |
| `Wandering Monster Encounters` prose (setting selection, City) | 93 | prose | GOVERNING | |
| Infravision (dwarf; elf identical) | 24 | prose | GOVERNING | |
| `Contact` (Evasion and Pursuit → Definitions) | 98 | prose | GOVERNING | |
| `Evasion at Sea` — pursuit start distance | 100 | prose | ROUTED | `ENC-005` |
| Encounter Checklist | 93 | checklist | ROUTED | `ENC-002` |
| Chance of Encounter Table | 92 | table | ROUTED | `EXP-001` |
| Monster Reactions Table | 93 | table | ROUTED | `ENC-003` |
| Wilderness / Dungeon Encounters subtables | 94–97 | table | ROUTED | `EXP-008` |

## 6. Index Enumeration

> **Manual, semantic instrument.** `DEC-0013` records that index seeding is **not**
> mechanically external — no structured RC index transcription exists outside Stage-A
> packets. These findings are the pilot's, re-confirmed by two independent reviews, and are
> not described as machine-checked.

| Instrument | Entry | Pages | Disposition |
|---|---|---|---|
| Tables / Checklists | Encounter Distances Table | 93 | GOVERNING — the principal object |
| Tables / Checklists | Chance of Encounter Table | 92 | ROUTED `EXP-001` |
| Tables / Checklists | Encounter Checklist | 93 | GOVERNING context; carries **no** distance step |
| Tables / Checklists | Game Turn / Game Day Checklist | 91 | GOVERNING — step 1 carries a distance |
| Tables / Checklists | Evasion Checklist / Ship Evasion Table | 99, 100 | ROUTED `ENC-005` |
| Tables / Checklists | Movement, Missile, and Spell Ranges | 87 | GOVERNING — the unit rule |
| General | Encounters | 91–96 | GOVERNING range |
| General | Distance / Feet / Yards / Ranges | 87 | GOVERNING — unit convention |
| General | Surprise | 92, 93 | ROUTED `ENC-002` — consumed as input |
| General | Infravision | 24, 25 | GOVERNING — footnote `**` selector |
| General | Evasion / Pursuit | 91, 98–100 | ROUTED `ENC-005` |
| General | Nocturnal | 153 | OPENED — bears on Q-1 |
| General | Blindness / Invisibility | 150 | ROUTED `EXP-006` / `COMBAT-*` |
| General | Underwater combat | 115 | OPENED — unit tension, Q-6 |

**Enumerated absences:** the General Index has **no** entry for `Encounter distance`,
`Visibility`, `Light`, `Lantern`, `Darkness`, `Ocean`, `Sea` or `Undersea`. Each was
established by reading the alphabetical neighbourhood the term would occupy, never by a
failed text search, and each was independently re-verified by two reviewers. The
**Tables/Checklists Index does** list `Encounter Distances Table … 93`, so the two
instruments are not interchangeable for this card.

## 7. Transcriptions

```text
TRANSCRIPTION p. 93
Encounter Distances Table
Setting        Visibility          Encounter      Distance
Dungeon*       Very good light     DM's choice    4d6x 10'
Dungeon*       Dim light**         DM's choice    2d6x 10'
Dungeon*       No lightt           DM's choice    1d4x 10'
Wilderness     Clear daylight      DM's choice    4d6 x 10 yards
Wilderness     Dim light**         DM's choice    2d6 x 10 yards
Wilderness     No lightt           DM's choice    1d4 x 10 yards
Ocean/sea      Clear daylight      Ship           300 yards
Ocean/sea      Clear daylight      Monster        4d6 x 10 yards
Ocean/sea      Dim light**         Ship           120 yards
Ocean/sea      Dim light**         Monster        2d6 X 10 yards
Ocean/sea      No lightt           Ship           40 yards
Ocean/sea      No lightt           Monster        1d4 x 10 yards
Undersea       Any light           DM's choice    1d6 x 10 yards
  *  Or other indoor setting.
 **  Or full darkness with infravision used.
  t  Or very poor visibility (heavy snow or fog, sandstorm, etc.).

When a random encounter is to occur, the DM first needs to know where the
characters are--dungeon or wilderness. "City" is treated just like any other
wilderness terrain.
```

```text
TRANSCRIPTION p. 92
Once the Dungeon Master has determined that an encounter will take place and
has determined the relative conditions of surprise for the two groups, he or
she can decide how far apart the two parties are when the encounter takes
place.
    When both parties are surprised, the encounter distance is 1d4 x 10' (or
yards if outdoors).
    When one party is surprised, the unsurprised party notices the surprised
party at the 1d4 X 10' (or yards) distance rolled; the surprised party won't
notice the unsurprised party until they reach half that distance.
    When neither party is surprised, take a look at the Encounter Distances
Table. When the type of terrain (dungeon, wilderness, ocean/sea, or
underwater) is known, the DM can find out how far apart the groups are when
the encounter takes place.
```

```text
TRANSCRIPTION p. 91
1. Wandering Monsters: If the wandering monsters check at the end of the
previous turn was positive, the monsters arrive now. Under normal dungeon
conditions, they appear 2d6 x 10' away in a direction of the DM's choice (see
the "Encounter Distance" section, below, for more information).

When a DM's roll indicates that wandering monsters will appear, they appear
the following turn. The DM rolls 2d6 and multiplies this number by 10; the
result is the distance, in feet, at which the monsters are detected.
    This is the distance at which the DM first begins keeping track of them
and the distance at which both sides first have a chance to notice one
another. Once the monsters appear, the DM should switch to the Encounter
Checklist (on page 93) to determine what happens next.

An "encounter" occurs when two or more groups come within visual range of one
another and at least one group becomes aware of the other.
```

```text
TRANSCRIPTION p. 87
In dungeons and other indoor settings, the basic unit of distance measurement
is the foot. Missile and spell ranges are measured in feet; a character's
normal speed is expressed in feet. In wildernesses, open fields, open city
streets, and other outdoor settings, the basic unit of distance measurement is
the yard. (One yard equals three feet.) In outdoor settings, it is easier to
move quickly due to more open terrain and better lighting.
```

```text
TRANSCRIPTION p. 24
Infravision is the ability to see heat (and the lack of heat). Dwarves have
infravision in addition to normal sight and can see 60' in the dark.
Infravision does not work in the presence of normal and magical light.
    Infravision isn't good enough to read by. A character can use his
infravision to recognize an individual only if they are within 10' distance
. . . unless the individual is very, very distinctive (for example, 8' tall or
walking with a crutch).
```

```text
TRANSCRIPTION p. 98
Contact occurs when the two parties encounter one another, as per the earlier
encounter rules. They do not have to be near one another, only within visual
range. When the encounter occurs, the DM determines the encounter distance and
the parties' relative states of surprise.
```

```text
TRANSCRIPTION p. 100
If the evasion is not successful, the pursuer starts at a distance of 300
yards on a clear day. (At the DM's discretion, if the weather is impairing
vision, the pursuer may start closer.) The pursuing ship closes in.
```

## 8. Evidence Map

| # | Page | Quote | Paraphrase | Object | Provenance | Confidence |
|---|---|---|---|---|---|---|
| E-1 | 93 | Dungeon*       Very good light     DM's choice    4d6x 10' | | table | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-2 | 93 | Dungeon*       Dim light**         DM's choice    2d6x 10' | | table | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-3 | 93 | Undersea       Any light           DM's choice    1d6 x 10 yards | | table | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-4 | 93 | Or full darkness with infravision used. | | footnote ** | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-5 | 93 | Or very poor visibility (heavy snow or fog, sandstorm, etc.). | | footnote t | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-6 | 93 | Ocean/sea      Clear daylight      Ship           300 yards | | table | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-7 | 92 | the encounter distance is 1d4 x 10' (or | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-8 | 92 | the surprised party won't | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-9 | 92 | When neither party is surprised, take a look at the Encounter Distances | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-10 | 92 | has determined the relative conditions of surprise for the two groups | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-11 | 87 | the basic unit of distance measurement | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-12 | 87 | it is easier to move quickly due to more open terrain and better lighting | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-13 | 91 | they appear 2d6 x 10' away in a direction of the DM's choice | | checklist | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-14 | 91 | the result is the distance, in feet, at which the monsters are detected | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-15 | 91 | come within visual range of one | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-16 | 93 | "City" is treated just like any other | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-17 | 24 | can see 60' in the dark | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-18 | 24 | Infravision does not work in the presence of normal and magical light. | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-19 | 98 | the DM determines the encounter distance and | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-20 | 98 | as per the earlier | | prose | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED |
| E-21 | 100 | the pursuer starts at a distance of 300 | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-22 | 100 | if the weather is impairing | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-23 | 95 | | Wilderness encounters are played out "using the visibility, distance, and surprise factors" and route back to the Encounter Checklist and Encounter Distances Table | prose | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED |
| E-24 | 153 | | The Nocturnal definition states dungeons are often dark as night — a hedged characterisation inside a creature-activity rule, not a visibility rule | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-25 | 115 | | Underwater Combat says undersea missile ranges are read in feet at all times, while the table's Undersea row is in yards | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-26 | 94 | | pp. 94, 96 and 97 carry only monster- and NPC-selection subtables; no row, column or footnote states a distance | tables | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-27 | 92 | | The Chance of Encounter Table lists aerial as a wilderness terrain, but the Encounter Distances Table has no Aerial Setting row | table | Unresolved by RC | DIRECT PRIMARY TEXT |
| E-28 | 3 | | The Contents confirms App. 4 Indices at 300–304: Index to Spells 300, Tables and Checklists 301, General Index 302 | front matter | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-29 | 93 | | RC states no procedure for selecting which visibility category obtains | table | Unresolved by RC | NOT YET ESTABLISHED |
| E-30 | 91 | the distance at which both sides first have a chance to notice one | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-31 | 24 | recognize an individual only if they are within 10' distance | | prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |

## 9. Cross-References

| From | Printed reference | To | Result |
|---|---|---|---|
| 91 | "(see the "Encounter Distance" section, below, for more information)" | 92 | Links the Game Turn Checklist's `2d6 × 10'` to the Encounter Distance section — the basis of Q-2 |
| 91 | "switch to the Encounter Checklist (on page 93)" | 93 | The checklist has six steps; **none** determines distance |
| 92 | "take a look at the Encounter Distances Table" | 93 | The unsurprised-case procedure |
| 92 | "though this may differ with some monsters; see Chapter 14" | 152 | Qualifies **surprise**, not distance — routed to `ENC-002`; per-monster variation is `MON-*` |
| 93 | footnote `**` "full darkness with infravision used" | 24 | Infravision is 60′, suppressed by normal and magical light |
| 95 | "Consult the Encounter Checklist and the Encounter Distances Table" | 93 | Wilderness encounters route **back** to the same table; no separate wilderness procedure |
| 93 | "'City' is treated just like any other wilderness terrain" | 93 | Supplies the Setting the table omits |
| 98 | "as per the earlier encounter rules" | 92 | p. 98 states **no procedure of its own**; it defers to pp. 91–93 |
| 98 | "The Evasion Checklist on page 99" | 99 | Routed to `ENC-005` |
| 100 | "Read the rules for 'Evasion at Sea'" (from p. 115) | 100 | Pursuit start distance — `ENC-005`'s; see §10 |
| 150 | "a character without infravision may find himself in an area of complete darkness" | 24 | Independent confirmation of the infravision↔darkness link the `**` footnote assumes |

## 10. Ownership and Dependency Routing

| Mechanic | Owner | Status | Basis |
|---|---|---|---|
| Encounter-distance determination at contact | **`ENC-001`** | this packet | pp. 92, 93 |
| Surprise determination | `ENC-002` | UNRESEARCHED | p. 92's ordering makes surprise a **settled input**; this card consumes it and claims no part of the mechanic |
| **Pursuit starting distance after a failed evasion** | **`ENC-005`** | Stage A accepted | p. 100 — see the determination below |
| Whether an encounter occurs | `EXP-001` | `VERIFIED`, implemented | Chance of Encounter Table |
| **World visibility category** | **NO RULE ID EXISTS** | — | `EXP-006` owns mundane light *contribution* and its own module states it is "**Not** a statement about the world". Recorded as a gap, not invented |
| Mundane light sources | `EXP-006` | LANDED | approved and implemented |
| Feet/yards unit convention | RC Ch. 6 p. 87 — **no Rule ID claims it** | — | consumed here; recorded as a potential completion question, not assigned |

### p. 100 `Evasion at Sea` — determination: **routed to `ENC-005`, not `ENC-001` governing**

Decided on **structure, procedure position and ownership boundary**, explicitly *not* on
the numeric resemblance to the table's `Ocean/sea | Clear daylight | Ship | 300 yards` row:

- **Structure.** It sits inside `Evasion and Pursuit` (pp. 98–100), under the `Evasion at
  Sea` heading, immediately after the Ship Evasion Table. It is not in the Encounter
  Distance section and not in the Encounter Distances Table.
- **Procedure position.** It applies *"If the evasion is not successful"* — after contact,
  after an encounter distance has already been produced by pp. 92–93, and after an evasion
  attempt has been resolved. It sets where a **chase** begins.
- **Ownership.** `ENC-005` owns evasion and pursuit; `ENC-001` owns the distance at
  contact. Routing it here would absorb a mechanic this card explicitly does not own.

**The distinction is preserved and is load-bearing:** *initial encounter distance* (set
once, at contact, by setting and visibility or by surprise) is a different quantity from
*pursuit starting distance* (set after a failed sea evasion, as a flat 300 yards reducible
at the DM's discretion for impaired vision). An implementer must not collapse them because
one number matches one table cell.

Recorded for `ENC-005`, not resolved here: whether a failed sea evasion **resets** the
separation to 300 yards even when the table had produced a Dim-light `120 yards` or
No-light `40 yards` encounter distance. That is a pursuit question.

## 11. Consequential Negative Claims

```text
NEGATIVE-CLAIM
CLAIM:                  Within the chapters carrying the encounter, movement and
                        dungeon-procedure rules, RC states no procedure for
                        determining WHICH visibility category (Very good light /
                        Dim light / No light) obtains at a given moment.
SCOPE SEARCHED:         Ch. 7 pp. 91-101 -- the chapter's full span, which runs
                        to p. 101 (p. 102 begins Ch. 8, per p. 93's own "see
                        Chapter 8, page 102"). p. 101 was inspected as a page
                        image this pass: it carries Balancing Encounters
                        (Optional) only -- TPL, Individual Adjusted Hit Dice,
                        the Challenge Percentage and Encounter Challenge Tables
                        and Reversing the Process. No visibility, setting or
                        distance content; ENC-007's material, and NOT a
                        governing object for this card.
                        Also the three table footnotes;
                        Ch. 6 p. 87; Ch. 13 p. 150; Ch. 14 pp. 153, 215.
                        NOT searched: Ch. 3 (Spells) or Ch. 4 (Equipment) -- the
                        claim is scoped to what was searched and does not extend
                        over them. Magical light routes to MAGIC-*; mundane light
                        is EXP-006's, whose accepted Stage A established a 30'
                        RADIUS, which is not a category.
INSTRUMENTS CHECKED:    Tables/Checklists Index read for any visibility, light or
                        illumination table -- none is listed. General Index
                        neighbourhoods for Light, Visibility, Darkness -- all
                        absent, each established by reading the neighbourhood.
FALSIFICATION ATTEMPT:  Sought a selector in the four places it would most
                        plausibly sit: the table's own footnotes (which EXTEND
                        categories but never define them); EXP-006's equipment
                        light (a radius); p. 153's Nocturnal definition
                        ("dungeons are OFTEN dark as night" -- hedged, and about
                        creature activity); and p. 100's Evasion at Sea, which
                        conditions a distance on weather impairing vision but
                        defines no category and governs pursuit, not contact.
                        None supplies a selector.
```

> This is the **only** consequential negative claim. The pilot's `N-1` (index absences),
> `N-2` (no visibility index entry) and `N-3` (halfling infravision) are **not** recreated:
> index absences are recorded in §6 as findings, and none of the three is an absence a
> later Rule Card would rely on.

## 12. Targeted Falsification

```text
FALSIFICATION
CONCLUSION:   p. 100 Evasion at Sea is ENC-005's pursuit-start rule, not an
              ENC-001 encounter-distance rule.
SOUGHT:       p. 100 read as a page image; its heading, its position relative to
              the Ship Evasion Table, and its entry condition. Also whether the
              Encounter Distance section or the table cross-references it.
RESULT:       It is under "Evasion at Sea" inside Evasion and Pursuit, triggers
              only on a FAILED evasion, and neither p. 92 nor p. 93 refers to it.
              The 300-yard match with one table cell is a coincidence of value,
              not of procedure.
DISPOSITION:  CONFIRMED
```

```text
FALSIFICATION
CONCLUSION:   "Normal dungeon conditions" (p. 91) is NOT established to mean the
              table's Dim light row, despite both yielding 2d6 x 10'.
SOUGHT:       p. 91 complete; pp. 92-93 complete; the three footnotes; p. 153's
              Nocturnal definition; p. 87's lighting remark; the General Index
              neighbourhoods for Light / Visibility / Darkness.
RESULT:       No equating text found anywhere. p. 153 hedges with "often"; p. 87
              attributes better lighting to the OUTDOORS.
DISPOSITION:  CONFIRMED as an open ambiguity -- retained, not adjudicated.
```

```text
FALSIFICATION
CONCLUSION:   ENC-001 consumes surprise state and does not determine it.
SOUGHT:       p. 92's ordering sentence; p. 93 Encounter Checklist step 2;
              p. 98's Contact, which names both determinations in one sentence;
              INVENTORY.md rows 116 and 117.
RESULT:       p. 92 sequences surprise BEFORE distance, so surprise enters as a
              settled input. p. 98 names both at contact with no sequencing word
              and defers to the earlier rules. Neither makes this card
              responsible for determining surprise.
DISPOSITION:  CONFIRMED
```

## 13. Open Questions

| # | Question | Object | Disposition |
|---|---|---|---|
| 1 | Does "normal dungeon conditions" (p. 91) denote the table's Dim-light row? Both produce `2d6 × 10'`, and RC never equates them | pp. 91, 93 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 2 | Is the p. 91 wandering-monster distance an instance of the p. 93 table, or an independent default bypassing the surprise branches? RC calls it "the distance at which **both sides** first have a chance to notice one another" (E-30) — **mutual** notice — while p. 92's one-surprised branch has the surprised party not noticing "until they reach half that distance". RC does not reconcile the two | pp. 91, 92, 93 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 3 | Is the Dungeon row's "Very good light" the same condition as "Clear daylight"? RC prints two labels and never equates them | p. 93 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 4 | Whose infravision satisfies footnote `**` — any one member's, all, or the noticing side's? RC adds that infravision recognises an individual only within 10′ (E-31), so "seeing by infravision" and "identifying who is there" are different ranges; RC does not say which the footnote means | pp. 24, 93 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 5 | Infravision reaches 60′, but the Dim-light dungeon row rolls 20′–120′. RC does not say what happens when the roll exceeds the range — and p. 91 defines an encounter by groups becoming *aware* of one another, which the 10′ recognition limit (E-31) distinguishes from mere heat-shape detection | pp. 24, 91, 93 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 6 | Undersea distance is in yards (p. 93) while p. 115 reads undersea ranges "in feet at all times" — possibly distinct concepts | pp. 93, 115 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 7 | Which visibility category obtains at a given moment — no selector in the chapters searched, and no Rule ID owns the world state | pp. 92, 93 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 8 | p. 98 names distance **and** surprise in one sentence with no sequencing word, while p. 92 sequences them. Does its word order carry procedural force? | pp. 92, 98 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 9 | The Chance of Encounter Table lists **aerial** terrain, but the table has no Aerial Setting row and RC gives no City-style bridge | pp. 92, 93 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 10 | Does a failed sea evasion reset separation to 300 yards, overriding a distance the table already produced? | p. 100 | CONFIRMED OUT OF SCOPE |
| 11 | Does the table apply when a party is surprised? | p. 92 | RESOLVED BY SOURCE INSPECTION |
| 12 | Is distance determined before or after surprise? | pp. 92, 98 | RESOLVED BY SOURCE INSPECTION |
| 13 | Which Setting governs a City encounter? | p. 93 | RESOLVED BY SOURCE INSPECTION |
| 14 | Is there a separate wilderness distance procedure? | p. 95 | RESOLVED BY SOURCE INSPECTION |
| 15 | Does the Encounter Checklist determine distance? | p. 93 | RESOLVED BY SOURCE INSPECTION |
| 16 | Does any monster-specific rule vary encounter *distance* rather than surprise? | pp. 92, 153 | CONFIRMED OUT OF SCOPE |
| 17 | Do cover, blindness or invisibility modify encounter distance? | pp. 108, 150 | CONFIRMED OUT OF SCOPE |

> **Q-7 is scoped to match the negative claim it rests on.** The pilot's wording asserted
> "no RC selector exists" at RC-wide scope while its own claim had been narrowed to the
> chapters searched. The narrower scope is kept and the broader wording deleted, rather
> than the claim being widened to fit obsolete phrasing.

## 14. Independent Review

```text
INDEPENDENT REVIEW:    NOT YET PERFORMED
HUMAN EVIDENCE REVIEW: NOT GIVEN
```

> The reviews under the closed `DEC-0012` pilot — Review #1 `FAIL`, Review #2 `FAIL` — are
> preserved at `docs/rules/evidence/ENC-001-stage-a-completeness-review.md` and in the
> pilot commits `d24aa3a` and `b880ffd`. They are historical and are not relabelled. The
> review that follows this packet is the **first** `DEC-0013` semantic review.
