# Stage-A Evidence Packet — `ENC-005` Retreat, Pursuit & Evasion

```text
STAGE:   A (EVIDENCE) -- DEC-0009
STATUS:  EVIDENCE READY FOR HUMAN REVIEW
         -- carrying one BOUNDARY QUESTION the human project owner must settle
            before Stage B (§9 Q1)
CARD:    ENC-005 -- Retreat, Pursuit & Evasion (underworld)
SOURCE:  Dungeons & Dragons Rules Cyclopedia (TSR 1071, 1991) -- primary
```

> **No Rule Card is drafted here.** Stage B has not begun and is not authorized.
>
> Researched 2026-09-27 under `CLUSTER-004`'s human-approved boundary.

---

## 1. Headline findings

1. **The procedure is not underworld-specific.** The inventory titles this card
   *"(underworld)"*. RC's procedure is **general** — one table and one checklist governing
   dungeon, wilderness and (by a separate table) sea. The `(underworld)` qualifier is a
   project-side narrowing, not a source distinction. **§9 Q1 — human decision required.**
2. **Two printed defects, both visually verified** on p. 99 — a self-referential checklist
   step, and a prose/table numerical contradiction. §6.
3. **The procedure cannot be made executable from landed cards alone.** Four of its six
   steps depend on cards that are unresearched: surprise, morale, encounter distance and
   initiative. §8.2.
4. **It needs party *size*, not marching order.** `EXP-010` is not required. §8.3.
5. **RC's terrain content here is an evasion-specific condition inside the Evasion Table,
   not a general terrain subsystem.** §7.5.

---

## 2. Source structure inspected (audit classes A, B)

### A — Table of Contents

**Chapter 7: Encounters and Evasion (p. 91)**, whose sub-sections are: Exploration and the
Game Turn (91), Travel and the Game Day (91), Encounters (91), Surprise (92), Monster
Reactions (93), Wandering Monster Encounters (93), **Evasion and Pursuit (98)**, Balancing
Encounters (Optional) (100).

**The card's material is one named TOC sub-section**, and the chapter's other sub-sections
are the neighbouring unresearched cards.

### B — Index to Tables and Checklists (p. 301), **visually inspected in full**

Every table and checklist bearing on this card:

| Object | Page | Disposition |
|---|---|---|
| **`Evasion Table`** | **99** | **Governing** — inspected visually |
| **`Evasion Checklist`** | **99** | **Governing** — inspected visually |
| `Ship Evasion Table` | 100 | **Excluded** — naval; §7.6 |
| `Castle Reactions Table` | 99 | **Excluded** — wilderness/castle reaction; §7.6 |
| `Encounter Checklist` | 93 | `ENC-001`/`ENC-002` |
| `Encounter Distances Table` | 93 | `ENC-001` |
| `Monster Reactions Table` | 93 | `ENC-003` |
| `Morale Scores Table` | 103 | `ENC-004` |
| `Combat Sequence Checklist` | 102 | `COMBAT-006` |
| `Character Movement Rates and Encumbrance Table` | 88 | **`CHAR-005` — LANDED**, consumed |
| `Terrain Effects on Movement Table` | 88 | **Excluded** — per-day/outdoor; already excluded by landed `EXP-003` |
| `Traveling Rates by Terrain Table` | 88 | **Excluded** — same |
| `Forced Marches Table` | 121 | **Excluded** — Ch. 9 War Machine, mass combat |

**No evasion or pursuit table exists outside pp. 99–100.**

### General Index (OCR — see the `EXP-006` packet §7.1 for the visual-access caveat)

```text
Evasion .91, 98-100          Evasion Table .99
Pursuit.98-100               Evasion Checklist .99
Running speed.88, 103        Encounter speed . 88, 95, 100, 103
```

The `91` and `100` page references were both followed: **p. 91** is the Encounters
introduction (no evasion mechanic), **p. 100** is the Ship Evasion continuation plus
Balancing Encounters. Neither adds an underworld rule.

---

## 3. Governing source objects (audit classes C–I)

| # | Object | Page | Class | Visually verified |
|---|---|---|---|---|
| 1 | **"Evasion and Pursuit" prose + Definitions** | **98–99** | F | **Yes** (leaves n97, n98) |
| 2 | **Evasion Checklist** (boxed, 6 steps) | **99** | E/C | **Yes** (leaf n98) |
| 3 | **Evasion Table** (party size × monsters; conditions) | **99** | C | **Yes** (leaf n98) |
| 4 | Ship Evasion Table + naval prose | 99–100 | C | OCR — **excluded**, §7.6 |
| 5 | Castle Reactions Table | 99 | C | **Yes** (leaf n98) — **excluded**, §7.6 |

**§9.7 complete-entry inspection.** Objects 1–3 were read **in full from the page images**,
including the prose columns flanking the boxed checklist — which is where the −10% scouts
figure that contradicts the table lives.

---

## 4. The procedure, as printed

**Facts only. No consequence is derived** (§7 of the protocol).

### 4.1 Frame

> *"When two groups encounter one another, one or both may decide to evade the other, or one
> group may decide to pursue the evading group… as soon as the groups spot one another, the
> evading group turns and runs, trying to get out of the pursuers' sight. **Time is measured
> in rounds** for as long as the chase occurs."*

### 4.2 The Evasion Checklist (p. 99), transcribed from the page image

```text
1. Contact             The two parties encounter one another.

2. Decision to Evade   One party decides to evade. If the evading party is
                       not surprised and the other party is surprised,
                       evasion is AUTOMATICALLY SUCCESSFUL; go to Step 6.
                       If the other party is not surprised, "go to Step 2".
                                                        ^^^^^^^^^^^^^^^^^^
                                                        printed defect -- §6.1

3. Decision to Pursue  PCs decide for themselves; monsters must make a
                       MORALE CHECK (defined in Chapter 8). Success -> give
                       chase (Step 4). Failure -> no chase (Step 6).

4. Attempt to Evade    The DM rolls on the Evasion Table. Success -> evaded
                       (Step 6). Failure -> pursuit continues (Step 5).

5. Pursuit Continues   Movement measured in ROUNDS, conducted at RUNNING
                       SPEED; both sides roll 1d6 for INITIATIVE once per
                       round; higher roll moves first. Chase continues until:
                         a. pursuers give up -- monsters make a NEW MORALE
                            CHECK EVERY FIVE ROUNDS, giving up on failure
                         b. evaders are caught -> COMBAT (Combat Checklist,
                            Chapter 8)
                         c. evaders escape

6. Regain Bearings     Evaders rest and determine where they now are.
```

### 4.3 The Evasion Table (p. 99), transcribed from the page image

| Party Size | No. of Monsters Encountered | Chance of Evasion |
|---|---|---|
| 1–4 | 1 | 50% |
| | 2–3 | 70% |
| | 4+ | 90% |
| 5–12 | 1–3 | 35% |
| | 4–8 | 50% |
| | 9+ | 70% |
| 13–24 | 1–6 | 25% |
| | 7–16 | 35% |
| | 17+ | 50% |
| 25+ | 1–10 | 10% |
| | 11–30 | 25% |
| | 31+ | 35% |

| Condition in Effect | Adjustment to Chance |
|---|---|
| Wooded terrain | **+25%** |
| Featureless terrain | **−15%** |
| Pursuers are twice as fast as evaders | **−25%** |
| Evaders are twice as fast as pursuers | **+25%** |
| Pursuers have scouts in place | **−15%** |

**The chance improves as the monsters outnumber the party** — a relationship that is
counter-intuitive on first reading and that the column layout makes unambiguous. RC's own
worked example confirms the reading: *"A PC party of eight… runs into a scouting party of 12
orcs. Comparing the 'Party Size 5-12' entry to the 'Number of Monsters Encountered 9 +'
line, the PCs have a **70%** chance to evade."*

### 4.4 The floor

> *"**Important Note:** Regardless of the number of evasion penalties, the evading group
> always has at least a **5%** chance to evade."*

### 4.5 Escape routes RC names

- **Spells** — *teleport*, *pass wall* (+ *dispel magic*), *wall of iron* (`MAGIC-*`).
- **A second Evasion Table roll** when evaders are temporarily out of vision range and reach
  *"an area of difficult terrain (for example, thick woods, a long dungeon corridor riddled
  with doors and side passages, etc.)"*; success means *"the pursuers fail to follow their
  tracks."*
- **Dropping goods** — *"the DM rolls 1d6 if he or she feels that the item dropped is indeed
  appealing to the monster. On a **1–3**, the monster stops to consume (or retrieve) the
  proffered goods and is delayed long enough for the evaders to get away."*
- **Monsters' local knowledge** — *"If monsters are familiar with an area, they may be able
  to evade pursuers by rapidly turning corners, closing doors behind them, and so forth."*
  **Stated of monsters evading, and given no numeric effect.**

### 4.6 Being caught

> *"If the pursuers end one round having caught up to the evaders (**the DM should be keeping
> track of their relative positions to determine this**) and then win initiative the next
> round, they can attack, forcing the evaders to turn and fight."*

Or an obstacle — *"a sheer cliff face, a dead-end hallway, a magically locked door, another
party of enemies"*. *"In these situations, combat usually results, though the evaders might
choose to surrender instead."*

### 4.7 Regain Bearings

> *"For every round the chase lasted, the evaders moved at full running speed in directions
> chosen or assumed by the DM. **They didn't have time to consult their map, and the DM
> should enforce this fact rigorously.** … at the DM's discretion, their attempts at evasion
> could have carried them deep into unknown territory (such as wilderness off the posted
> roads and trails or **unexplored dungeon levels**), and now the characters are lost."*

---

## 5. Whole-source cross-reference pass (§9)

```text
"Evasion and Pursuit"   2 hits    TOC + the section heading
"Evasion"              36 hits    TOC, Ch. 7 section, Evasion/Ship Evasion Tables,
                                  Evasion Checklist, index
"Pursuit"               6 hits    TOC, section, Castle Reactions "Pursue" column, index
"evade"                35 hits    concentrated in Ch. 7 pp. 98-100; scattered monster
                                  entries describing creatures that flee
"outdistance"           0 hits
"vision range"          1 hit     the escape clause, §4.5
```

**No second evasion or pursuit procedure was located anywhere in the source.** The only
other pursuit-flavoured objects are the Castle Reactions Table's `Pursue` column (a
wilderness/castle **reaction** result, not a chase procedure) and the naval material.

---

## 6. Printed defects — both visually verified

### 6.1 The Evasion Checklist step 2 refers to itself

> *"2. Decision to Evade: … If the other party is not surprised, **go to Step 2**."*

Step 2 directs the reader back to step 2. Read literally it is an infinite loop. The
surrounding prose and the checklist's own ordering make the intent legible — the next step
is **Decision to Pursue**, step 3 — but **RC prints `Step 2`**, and this packet does not
correct it. `POTENTIAL TRANSCRIPTION/COMPILATION DEFECT`, recorded for Stage B.

### 6.2 Scouts adjustment: prose `−10%`, table `−15%`

| Location | Value |
|---|---|
| Prose, p. 99 left column | *"a **- 10%** penalty is applied to the evasion chance"* |
| **Evasion Table**, p. 99 | `Pursuers have scouts in place` … **`-15%`** |

**Both were read from the same page image.** RC states two different numbers for one
adjustment. **`INTERNAL SOURCE CONFLICT REQUIRES REVIEW`** — not resolved here, and not to
be resolved by an implementation agent.

Note the contrast with the *wooded terrain* figure, where prose (*"woods might add a 25%
chance"*) and table (`+25%`) **agree** — so the scouts discrepancy is not a systematic
prose/table mismatch but a specific one.

---

## 7. Findings on scope and boundaries

### 7.1 The procedure is general, not underworld-specific

RC's evasion procedure names **both** environments inside one rule set:

```text
DUNGEON    "a long dungeon corridor riddled with doors and side passages"
           "unexplored dungeon levels"
           "a dead-end hallway", "a magically locked door"
WILDERNESS "Wooded terrain +25%", "Featureless terrain -15%"
           "thick woods", "wilderness off the posted roads and trails"
           "a sheer cliff face"
SEA        a SEPARATE table and procedure (Ship Evasion Table, p. 100)
```

**RC separates naval evasion into its own table and does not separate dungeon from
wilderness at all.** The `(underworld)` in the card title therefore describes a project
scoping choice, not a source boundary. **§9 Q1.**

### 7.2 What it consumes from landed cards

| Value | Owner | State |
|---|---|---|
| **Running speed**, feet per round | **`CHAR-005`** | **LANDED** — `MovementRate.running` |
| The round as a time unit | `EXP-002` / `COMBAT-006` | Round is combat-scale; landed `EXP-002` owns the turn |
| Party size | — | An input the caller supplies; no card owns it |

**Nothing is re-derived.** The procedure asks for a running speed and a party size, and
states neither itself.

### 7.3 Speed comparison needs monster movement rates

*"If one group can move at least **twice as fast** as the other…"* requires a **monster's**
movement rate. Monster statistics are **`MON-003`**, unresearched, and are catalog-closure
work the research order places near-last. Recorded as a dependency; **not** researched here.

### 7.4 Party size, not formation

> *"If a large party breaks up into small parties, roll for each small party separately; in
> this way, **some parties could evade while others could be caught**."*

The procedure's only party input is **size**, plus the option to split into sub-parties.
**No marching order, formation or rank is referenced anywhere in the section.** `EXP-010`
is **not** required, which is consistent with landed `EXP-003`'s case `D32`.

### 7.5 Terrain — an evasion condition, not a subsystem

The guardrail's distinction, applied:

```text
WHAT RC GIVES HERE          an adjustment column INSIDE the Evasion Table
                            Wooded terrain      +25%
                            Featureless terrain -15%
                            plus "difficult terrain" as a DM-judged trigger
                            for a SECOND evasion roll

WHAT RC DOES NOT GIVE HERE  any rule that terrain modifies a movement RATE
                            any definition of "difficult terrain"
                            any list of terrain types beyond wooded/featureless
                            any dungeon terrain classification
```

**These adjust an evasion percentage, not a movement rate.** They are self-contained within
the Evasion Table and require no general terrain mechanic to apply. **`ENC-005` can be
specified without owning terrain.**

**The unowned rough/broken-terrain modifier is *not* imported.** It was expressly left
unowned at `CLUSTER-003`'s approval, it concerns movement *rates*, and nothing in this
section references it. The Mystic Acrobatics material is **not** consulted.

**One genuine gap is flagged rather than filled:** *"difficult terrain"* in §4.5 is
undefined — RC gives examples (*thick woods; a long dungeon corridor riddled with doors and
side passages*) and no criterion. Implementing the second-roll escape would require either a
DM-input flag or an undefined generic terrain mechanic. **§9 Q3.**

### 7.6 Deliberate exclusions, with reasons

| Object | Reason |
|---|---|
| **Ship Evasion Table** and naval pursuit (pp. 99–100) | Water transportation is out of V1 (`CHAR-004` §B); a separate procedure with its own table and closing-rate rules |
| **Castle Reactions Table** `Pursue` column (p. 99) | A wilderness/castle **reaction** result feeding `ENC-003`, not the chase procedure |
| Wilderness/City Encounter subtables (pp. 97–98) | `MON-001`/`EXP-008` coupled knot — untouched by instruction |
| `Terrain Effects on Movement` / `Traveling Rates by Terrain` (p. 88) | Per-day and outdoor; already excluded by landed `EXP-003` |
| Balancing Encounters (p. 100) | `ENC-007`, default-OFF |
| Piloting general skill (p. 100) | `CHAR-012`; naval only |

---

## 8. Ownership and dependency findings

### 8.1 `EXP-003` / `CHAR-005` seam — consumed, not re-derived

Landed `EXP-003` owns **ordinary dungeon movement per turn**; `ENC-005` governs a chase
measured in **rounds at running speed**. They do not overlap: RC's own scale boundary
(Ch. 8 p. 103, *"normal speed is never used during the combat sequence"*) puts the chase on
the combat side of the line, and landed `CHAR-005` already implements and guards that
boundary (cases `M21`–`M24`).

### 8.2 Hard dependencies on unresearched cards

**Four of the checklist's six steps cannot execute without a card that does not exist.**

| Step | Requires | Card | State |
|---|---|---|---|
| 1 Contact | encounter distance; *"within visual range"* | **`ENC-001`** | Unresearched |
| 2 Decision to Evade | **relative surprise states** | **`ENC-002`** | Unresearched |
| 3 Decision to Pursue | **morale check** (Chapter 8) | **`ENC-004`** | Unresearched — RC-optional, **DEC-0008 REQUIRED** |
| 5 Pursuit Continues | **1d6 initiative each round** | **`COMBAT-006`** | Unresearched |
| 5a | morale check **every five rounds** | `ENC-004` | Unresearched |
| 5b | *"go to the Combat Checklist in Chapter 8"* | `COMBAT-*` | Unresearched |
| 5 speed comparison | monster movement rates | `MON-003` | Unresearched |
| 4.5 escapes | *teleport*, *pass wall*, *wall of iron* | `MAGIC-*` | Unresearched — **examples, not requirements** |

**This is the central finding for boundary purposes.** `ENC-005` is dependency-unblocked in
the inventory's sense — its listed dependencies `EXP-002` and `EXP-003` are landed — but the
**procedure text** depends on four unresearched cards. The inventory's dependency cell is
narrower than the source. **§9 Q2.**

### 8.3 The rest cross-reference, followed only to ownership

Step 6 *"Regain Bearings"*: *"Evaders **rest** and determine where they now are… they need
to rest from their exertions."*

Followed **only far enough to establish ownership**, per instruction: a chase is run at
running speed for a counted number of rounds, and landed **`CHAR-005` §9** already owns the
running limit (**30 rounds**), the rest requirement (**3 turns**) and `ExhaustionPenalty`.
**`EXP-004` is not reopened**, and no wilderness rest material was researched.

**Recorded, not resolved:** RC's evasion section does not say whether the chase's rounds
count against `CHAR-005` §9's 30-round running limit, nor whether *"rest from their
exertions"* is that card's 3-turn rest or ordinary narration. **§9 Q4.**

### 8.4 `EXP-006` cross-reference received

The oil description (p. 69) says a flask may be *"poured out and ignited to **delay
pursuit**."* **The evasion section itself states no mechanic for this** — no adjustment, no
table row, no delay value. Recorded from both sides; **no mechanic is invented.**

---

## 9. Open questions

### Retained — require human decision

1. **Is `ENC-005` underworld-only, or does it own RC's general evasion procedure?**
   The source does not separate dungeon from wilderness; it separates *sea*. Narrowing to
   underworld would mean owning part of one indivisible procedure. **This is a boundary
   decision, not a rules decision**, and it interacts with the standing Wilderness
   Adventures reachability question. **Stage B cannot begin without it.**
2. **Can `ENC-005` be specified at all before `ENC-001`/`ENC-002`/`ENC-004`/`COMBAT-006`?**
   Four of six steps reference them. A Rule Card could be written that *names* those inputs
   as caller-supplied, but it would be a contract with four unresearched counterparties —
   the same concern that deferred `EXP-010`. **Recorded as a sequencing question for the
   human project owner**, not answered here.
3. **"Difficult terrain" is undefined** (§7.5). The second-roll escape cannot be made
   executable without either a DM-input flag or a terrain mechanic RC does not supply.
4. **Do chase rounds count against `CHAR-005` §9's 30-round running limit?** (§8.3.)
5. **Which scouts figure governs, −10% or −15%?** (§6.2.) `INTERNAL SOURCE CONFLICT`.
6. **Does the checklist's `go to Step 2` mean step 3?** (§6.1.)

### Closed, with the reason

7. ~~Is there a second evasion procedure elsewhere?~~ **Closed — no.** §5, plus the Tables
   Index read visually.
8. ~~Does the procedure need marching order?~~ **Closed — no.** §7.4; it needs party size.
9. ~~Is the Castle Reactions `Pursue` column part of this procedure?~~ **Closed — no.**
   A reaction result, §7.6.
10. ~~Is the pursuit rule wilderness-only?~~ **Closed — no.** It names dungeon corridors,
    dead-end hallways and unexplored dungeon levels explicitly. §7.1.
11. ~~Does evasion chance improve or worsen as monsters outnumber the party?~~
    **Closed — it improves**, confirmed by the table's columns and RC's worked example. §4.3.

---

## 10. Provenance candidates (for Stage B, not decided here)

| Element | Likely classification |
|---|---|
| The checklist's six steps; the Evasion Table's percentages and conditions; the 5% floor; the every-five-rounds morale cadence; running speed and rounds; the 1d6 dropped-goods delay | **Rules Cyclopedia Explicit** |
| `go to Step 2` read as step 3 | **Printed-notation / compilation-defect reading** — the category `CHAR-004`'s "Clothes, plain" marker was approved under. **Not** a Simulator Ruling if the human project owner agrees it is a defect |
| Scouts −10% vs −15% | **Genuine internal conflict.** Would require a **Simulator Ruling** if RC cannot be read to prefer one. Compare `SR-6` |
| Any definition of "difficult terrain" | **None available.** Do not invent |

**No Simulator Ruling is proposed.** Rulings come last, after gap-directed alternate-source
research, and none is requested (§11).

---

## 11. Alternate-source research

**None performed, and none requested.**

The two defects in §6 are **internal RC conflicts**, which `DEC-0011` gap research addresses
only after a precise gap is documented and human authorization is given. The BECMI Expert
set is known to carry an evasion procedure, and a lineage check might well disambiguate the
−10%/−15% conflict and the step-2 loop — **but that lookup is not authorized by the current
boundary, and this packet does not perform it.**

**Flagged for human authorization** as a candidate `DEC-0011` question if, and only if, the
human project owner decides the conflicts must be resolved from lineage rather than adjudicated
as Simulator Rulings. AD&D remains excluded.

---

## 12. Adversarial self-review (§10.1.1)

Performed by the original researcher. **This is not the independent review.**

| Challenge to myself | Answer |
|---|---|
| Did I accept the card's `(underworld)` title as a source fact? | **No — I tested it and it failed.** §7.1 is the result, and I have raised it as Q1 rather than quietly scoping the card to dungeons |
| Did I read the boxed checklist and skip the prose? | **No.** §6.2 exists precisely because the flanking prose column carries a number the box does not |
| Did I invent a terrain mechanic? | **No.** §7.5 distinguishes the Evasion Table's condition column from a subsystem and flags the undefined *"difficult terrain"* as a gap |
| Did I import the unowned Mystic rough-terrain material? | **No.** Not consulted |
| Did I absorb marching order? | **No.** §7.4 establishes the procedure needs size, not order |
| Did I follow the rest reference too far? | Followed to ownership only; `EXP-004` untouched, wilderness rest unresearched |
| Did I touch the stocking knot? | **No.** The wilderness/city encounter subtables on the same pages were excluded by name |
| Is my dependency claim over-stated? | The four hard dependencies are quoted from the checklist itself. **I think §8.2 is the finding most likely to change the cluster's shape, and the independent reviewer should attack it first** |

---

## 13. Independent completeness review (§10.1.2)

```text
REQUIRED -- may NOT be performed by the original researcher
RESULT:   see docs/rules/evidence/CLUSTER-004-stage-a-completeness-review.md
```

---

## 14. Addendum — two governing objects the first pass missed (2026-09-27)

**Added after §1–§13 were drafted. Recorded as an addendum rather than folded in, so the
order of discovery stays visible: both were found by the General Index visual pass, which
is exactly the completeness instrument precedent `P-001` exists to enforce, and neither was
found by the TOC, the Tables Index or the whole-source keyword pass.**

**My §12 adversarial self-review did not catch either.** They are recorded here as gaps in
the first pass, not presented as though the packet had always contained them.

### 14.1 `Retreat maneuver . 104` — the card's own title word, on a page not inspected

The card is titled ***Retreat***, Pursuit & Evasion. The General Index carries a
**`Retreat maneuver . . . 104`** entry, and p. 104 is **Chapter 8's Combat Maneuvers Table**
— which the first pass did not inspect.

RC's **Retreat** is a *within-combat* maneuver:

> *"A character can only perform this maneuver when he begins his combat round in
> hand-to-hand combat with an enemy. The character runs away from his enemy at greater than
> half his encounter speed, up to his full encounter speed. He forfeits the armor class
> bonus of his shield. Any enemy attacking him later in the combat round … receives a +2
> attack roll bonus this round."*

And the adjacent **Fighting Withdrawal** maneuver ends with the bridge into a chase:

> *"…if [he] is not in hand-to-hand combat with his enemy when his movement phase comes
> around in the next round, he **can go to running speed that next round**."*

**Assessment, stated as a boundary question rather than a claim.** The Retreat maneuver sits
in the Combat Maneuvers Table alongside Parry, Disarm, Smash and Lance Attack; it is
governed by combat phases, forfeits a shield bonus, and grants an attack bonus. **On its
face it is `COMBAT-*`'s**, and Fighting Withdrawal is the printed seam by which a combat
maneuver becomes a chase at running speed.

**But the card's title claims the word**, and nothing in this packet settles which
"retreat" `ENC-005` is named for: the Ch. 8 maneuver, or the *"turns and runs"* that opens
the Ch. 7 evasion procedure. **§9 gains Q12.** No ownership is assigned here, and Chapter 8
was **not** researched beyond establishing this boundary.

### 14.2 `Lost . 89` — there is no dungeon getting-lost mechanic

Checklist step 6 ends *"now the characters are lost; they'll have to explore their way back
to the areas they know"*, naming *"unexplored dungeon levels"* as one way that happens. The
index carries a **`Lost . . . 89`** entry, and p. 89 is Ch. 6 **Land Travel**:

> **Becoming Lost** — *"A party following a road, trail, or river or led by a reliable guide
> will not become lost… the DM must check each day to see if the adventurers become lost by
> rolling 1d6 before the party begins movement for the day"*, with per-terrain target
> numbers (clear/grasslands 1; swamp, jungle or desert 1–3; all other terrain 1–2).

```text
RC's Becoming Lost mechanic is PER DAY and WILDERNESS.
It sits in the Game DAY Checklist (p. 91), not the Game Turn Checklist.
```

**Therefore RC provides no dungeon getting-lost procedure**, and step 6's *"lost"* is
narrative for the underworld case. Recorded as a **negative finding with its basis**: the
index entry was followed to its page and the mechanic found there is wilderness-scoped.

**This sharpens §9 Q1.** The evasion procedure's own tail leads into a rule that exists only
for wilderness — further evidence that RC did not intend a dungeon/wilderness split here.

### 14.3 A `CHAR-012` interaction, recorded not claimed

The **Caving** general skill (Ch. 5) states: *"If he is forced to flee for a long stretch, he
must make a skill check to keep from being lost. (Characters without this skill
automatically become lost in such a situation.)"*

**This is a general skill that triggers on fleeing** — a direct interaction with this card's
step 6. `CHAR-012` General Skills is unresearched and **RC-optional, project-selected
REQUIRED** under `DEC-0008`. Recorded as a dependency; **not** researched.

### 14.4 Correction to §7.3

§7.3 attributed monster movement rates to `MON-003` alone. The index shows
**`Monster movement rate . . . 88, 152`** — p. 88 is the Movement chapter and p. 152 is
*"How to Read Monster Descriptions"*. The *per-monster values* remain catalog-closure work,
but the **rate's definition and presentation** have stated locations outside `MON-003`.
The dependency stands; its owner is less settled than §7.3 implied.

### 14.5 Additional retained open questions

12. **Which "retreat" does this card own?** The Ch. 8 combat maneuver (p. 104), the Ch. 7
    *"turns and runs"* that opens evasion, or neither — with the title simply being loose?
    **§14.1.** This bears directly on whether `COMBAT-*` must precede this card.
13. **Does the Fighting Withdrawal → running speed bridge belong here or to `COMBAT-*`?**
    It is the printed transition from a combat round into a chase. **§14.1.**
14. **Does `CHAR-012`'s Caving skill modify step 6?** **§14.3.**

### 14.6 Effect on the packet's verdict

The two missed objects are **boundary evidence, not procedure evidence**: neither changes a
percentage, a step or a die roll in §4. The transcription of the Evasion Checklist and
Evasion Table stands unaltered.

**But they were missed, and the completeness claim in §7 was made before they were found.**
The independent completeness review should treat §14 as evidence that the first pass's
index handling was too thin, and judge the packet accordingly.
