# `ENC-005` — Retreat, Pursuit & Evasion — Stage-A Evidence (Remediated, Pass 2)

```text
RULE CARD          ENC-005   Retreat, Pursuit & Evasion (underworld)
STAGE              A (EVIDENCE).  Stage B NOT begun, NOT authorized.
PASS               4 -- remediates the THIRD independent review's findings: the rest
                   of Chapter 5 (pp. 84-86), the DEC-0008 error, and two elided
                   quotations.
SUPERSEDES         docs/rules/evidence/ENC-005-evidence.md  (pass 1, committed e33c4e0)
                   Pass 1 returned PRIMARY-SOURCE COMPLETENESS: FAIL and is preserved
                   unaltered as the audit record of that failure.
REVIEW HISTORY     pass 1  FAIL   CLUSTER-004-stage-a-completeness-review.md
                   pass 2  FAIL   CLUSTER-004-stage-a-completeness-review-2.md
                   pass 3  FAIL   CLUSTER-004-stage-a-completeness-review-3.md
                   pass 4  pending fourth independent review
PRIMARY SOURCE     D&D Rules Cyclopedia (TSR 1071)
RECOMMENDATION     see section 19
```

> **Scope of this remediation.** The independent reviewer confirmed pass 1's Evasion Table and
> Evasion Checklist transcriptions as exact, both p. 99 printed defects as genuine, the
> four-of-six dependency finding as accurate, the terrain distinction as well drawn, and found
> **no scope creep**. Those conclusions are carried forward.
>
> What failed was the **coverage record**: p. 100 col. 1 was marked excluded while being quoted
> from; the `d100` resolution direction was absent; the p. 104 `Retreat` quote stopped one
> paragraph short of its operative sentence; the General Index was cited rather than
> enumerated; the §6 confidence vocabulary was not used; and the packet carried **no
> `Primary-Source Coverage Checklist` at all**, which §9.3 requires. All are fixed here.
>
> **Remediation did not falsify any substantive pass-1 conclusion**, so the bounded assumption
> held. Three findings were **sharpened**, one materially (§5.6).

---

## 1–2. Rule Card and primary source accessed

`ENC-005` — **Retreat, Pursuit & Evasion (underworld)**.

```text
PAGE IMAGES (authoritative for every object in this packet)
    https://iiif.archive.org/iiif/TSR1071TheDDRulesCyclopedia$<leaf>/full/1400,/0/default.jpg
OCR (LOCATOR ONLY)
    https://archive.org/stream/TSR1071TheDDRulesCyclopedia/.../djvu.txt
```

### 2.1 Correction of a pass-1 access statement

**p. 104 is now visually verified.** Pass 1's §14.1 `Retreat` material was **OCR-grounded**
after the IIIF endpoint refused that leaf across roughly twenty attempts; the reviewer flagged
this. The page image was obtained on the first attempt this pass. The OCR text was accurate,
but it was **incomplete** — see §5.6. No finding in this packet rests on OCR.

---

## 3. Structure-first inventory

### 3.1 The source's own boundary for this responsibility

RC's General Index gives two entries that between them delimit the card:

```text
Evasion  . . . . 91, 98-100
Pursuit  . . . . 98-100
```

plus the two named maneuvers at p. 104. **This is the source's own enumeration of the
responsibility**, and it matches the section RC prints under the heading `Evasion and
Pursuit` (pp. 98–100), entered from the checklists on pp. 91 and 93.

### 3.2 Named objects — Guardrail C attestation

| Object | Page | OPENED | VISUALLY INSPECTED | DISPOSITIONED |
|---|---|---|---|---|
| `Evasion Checklist` | 99 | yes | yes | **GOVERNING** — the operational object (§5.2) |
| `Evasion Table` | 99 | yes | yes | **GOVERNING** (§5.3) |
| `Ship Evasion Table` | **100** | yes | yes | **EXCLUDED — naval.** §5.5. *Pass 1 never dispositioned this named table* |
| `Combat Maneuvers Table` | **104** | yes | yes | **EXCLUDED — `COMBAT-*` owns it.** Routing evidence (§5.6). *Pass 1 never dispositioned this named table* |
| `Encounter Checklist` | 93 | yes | yes | **PROVIDER** — step 5c is an entry condition (§5.1) |
| `Game Day Checklist` | 91 | yes | yes | **PROVIDER** — step 4b is an entry condition (§5.1) |
| `Game Turn Checklist` | 91 | yes | yes | `EXP-001` **[LANDED]** |
| `Encounter Distances Table` | 93 | yes | yes | **CONSUMED** by step 1 `Contact` (§5.1) |
| `Monster Reactions Table` | 93 | yes | yes | `ENC-003`. Excluded |
| `Morale Scores Table` | 103 | yes | yes | `ENC-004` **[UNRESEARCHED]** — step 3 / step 5a provider |
| `Combat Sequence Checklist` | 102 | yes | yes | `COMBAT-006` **[UNRESEARCHED]** — step 5b exit |
| `Castle Reactions Table` | 99 | yes | yes | **EXCLUDED** — wilderness castle encounters, `EXP-008`/`MON-001` |
| `Balancing Encounters Checklist` | 101 | yes | yes | **EXCLUDED** — `ENC-007`, optional system |
| `Character Movement Rates and Encumbrance Table` | 88 | yes | yes | `CHAR-005` **[LANDED]**. Consumed, not re-derived |
| `Sample Skills Table` | **82** | **yes — pass 3; read ROW BY ROW in pass 4** | **yes** | **GOVERNING for step 6** via `Caving`; `Tracking` bears on N-17 (N-37); `Endurance` bears on Q4; all other rows inspected and **excluded as unrelated to retreat, pursuit or evasion**. Skill ownership `CHAR-012`. §5.7 |
| `Skill Slot Acquisition (Humans)` / `(Demihumans)` Tables | 86 | **yes — pass 4** | **yes** | **EXCLUDED** — skill acquisition/progression, wholly `CHAR-012` |
| `Attack Roll Modifiers Table` | **108** | **yes — pass 3** | **yes** | **EXCLUDED — `COMBAT-*`.** Its exhaustion rows are routed and a p. 88 wording tension is reported (§5.5a) |
| `Terrain Effects on Movement Table` | 88 | yes | yes | **EXCLUDED** — wilderness movement terrain. **Not** the Evasion Table's terrain (§5.4) |

### 3.3 General Index — **enumerated**, not cited (precedent `P-001`)

| Entry | Pages | Inspected | Disposition |
|---|---|---|---|
| `Evasion` | **91**, 98-100 | yes | **GOVERNING.** p. 91 is the Game Day hook — *pass 1 had only 98–100* |
| `Pursuit` | 98-100 | yes | **GOVERNING** |
| `Retreat maneuver` | 104 | yes | **CROSS-REFERENCE / ROUTED → `COMBAT-*`** (§5.6) |
| `Fighting withdrawal maneuver` | 104 | yes | **CROSS-REFERENCE / ROUTED → `COMBAT-*`** (§5.6) |
| `Maneuvers` / `Combat maneuvers` | 103-105 | yes | `COMBAT-*`. Excluded |
| `Encounter speed` | 88, 95, **100**, 103 | yes | `CHAR-005` **[LANDED]**. Consumed. Note p. 100 — another index pointer into the page pass 1 excluded |
| `Running speed` | 88, 103 | yes | `CHAR-005` **[LANDED]**. Consumed |
| `Normal speed` | 88, 103 | yes | `CHAR-005` **[LANDED]** |
| `Monster movement rate` | 88, 152 | yes | `MON-003` **[UNRESEARCHED]** — step 5's speed comparison |
| `Surprise` | 92, 93 | yes | `ENC-002` **[UNRESEARCHED]** — step 2 provider, p. 93 Encounter Checklist step 2 |
| `Morale` | 102, 103, 119 | yes | `ENC-004` **[UNRESEARCHED]**. p. 119 is War Machine — excluded |
| `Initiative` | 102 | yes | `COMBAT-006` **[UNRESEARCHED]** — step 5's `1d6` |
| `Lost` | 89 | yes | **Wilderness, per-day.** Refined by p. 100 (§5.4) |
| `Terrain` | 119, 153 | yes | p. 119 War Machine, p. 153 monster habitat. **Neither is the Evasion Table's terrain.** Excluded |
| `Charge` | 154 | yes | *"A monster cannot charge in certain types of terrain: broken, heavy forest, jungle, mountain, swamp"* — **monster combat, `MON-*`. Explicitly NOT imported as a generic terrain mechanic** |
| `Move silently` | 22 | yes | Thief skill, `CHAR-012`. Excluded |
| `Skills` / `Skill check` | 82-85, 92 | **yes — pass 3, visually** | **GOVERNING for step 6.** `Sample Skills Table` (82); `Caving`, `Endurance` (83). §5.7, §5.5a. Skill **ownership** is `CHAR-012` **[UNRESEARCHED]**; the step-6 trigger is recorded here. *Pass 2 listed this entry and did not open it* |
| `Exhaustion` | **88** | **yes — pass 3** | **GOVERNING for step 5.** §5.5a. `CHAR-005` §9 **[LANDED]** owns it. *Not enumerated by pass 2* |
| `Endurance` (via `Skills`) | 83, 88 | **yes — pass 3** | The RC-named exception to the 30-round running maximum. `CHAR-012`. Bears on Q4 |
| `High-level player characters` | 96, **98**, 129 | yes | p. 98 is DM advice on scaling encounters, **not** an evasion mechanic. Excluded with reason |
| `Balancing encounters` | 100, 101 | yes | `ENC-007`. Excluded |
| `Encounters` | 91-96 | yes | `ENC-001` / `EXP-005` |

---

## 4. Research questions

1. What is RC's printed evasion/pursuit procedure, exactly?
2. How is the evasion roll **resolved** — which direction succeeds? *(absent from pass 1)*
3. What are the section's **entry** and **exit** conditions? *(unfollowed in pass 1)*
4. Which of the checklist's six steps depend on unresearched cards?
5. Is the card underworld-only, or does it own RC's general procedure?
6. Where is the `COMBAT-*` boundary for `Retreat` and `Fighting Withdrawal`?

---

## 5. Evidence map

§6 confidence vocabulary, verbatim.

### 5.1 Entry conditions — **two printed doorways**, both now followed

| # | Fact | Object | Confidence |
|---|---|---|---|
| N-1 | `Encounter Checklist` step 5c: *"If the PCs run away, make a **morale check** for the monsters or NPCs to see if they give chase. If so, **use the pursuit and evasion rules later this chapter** to see if the PCs get away."* | p. 93 | **DIRECT PRIMARY TEXT** |
| N-2 | `Game Day Checklist` step 4b: *"If the characters want to **evade or pursue** encountered monsters, the DM goes to the **'Evasion and Pursuit' section** later in this chapter."* | p. 91 | **DIRECT PRIMARY TEXT** |
| N-3 | RC's own definition: *"**'Evasion' is what happens when an encounter occurs and one side wants to escape the other; that side turns and runs.**"* | p. 91 | **DIRECT PRIMARY TEXT** |
| N-4 | `Contact` (step 1): *"Contact occurs when the two parties encounter one another, as per the earlier encounter rules. They do not have to be near one another, **only within visual range**. When the encounter occurs, the DM determines the **encounter distance** and the parties' relative states of surprise."* | p. 98 | **PRIMARY TEXT + CROSS-REFERENCE CONFIRMED** (targets pp. 92–93 opened) |
| **N-4a** | Step 1's encounter distance is **gated on surprise**, p. 92: **both** surprised → `1d4 x 10'`; **one** surprised → unsurprised side notices at that distance, surprised side **not until half**; **neither** surprised → consult the `Encounter Distances Table` (p. 93), which is light-keyed | p. 92 | **DIRECT PRIMARY TEXT** |
| **N-4b** | Step 2's automatic success has its source here: p. 92, *"One Group Is Surprised: The unsurprised group can take advantage of the situation by **evading (automatic success, meaning that the other group doesn't notice them at all)**"* | p. 92 | **PRIMARY TEXT + CROSS-REFERENCE CONFIRMED** (matches checklist step 2, N-6) |
| **N-4c** | Surprise itself: *"both sides roll `1d6`. Each side that rolls a **1 or 2** is surprised."* Asymmetric-notice detail as in N-4a | pp. 92–93 | **DIRECT PRIMARY TEXT** — recorded as `ENC-002`'s, **not claimed** |

**N-4 is a new cross-reference in this pass.** It is the printed link from `ENC-005` step 1 to
the **`Encounter Distances Table` (p. 93)** — which is keyed on a light/**Visibility** column.
This connects the two cards in this cluster through the source rather than through analysis:
`EXP-006`'s light state feeds the table that sets the distance `ENC-005` step 1 needs.

**N-3 also confirms a standing project principle.** RC p. 91: *"An encounter can result in
combat between the two sides, conversation, cooperation, a chase, or similar event."*
**A random encounter is not automatically combat**, and evasion is one of RC's printed
alternatives to it.

### 5.2 `Evasion Checklist`, p. 99 — the governing operational object

Verbatim, visually verified. **This is pass 1's transcription, confirmed by the independent
reviewer as exact, and re-verified here.**

```text
Evasion Checklist
 1. Contact: The two parties encounter one another.
 2. Decision to Evade: One party decides to evade. If the evading party is not sur-
    prised and the other party is surprised, evasion is automatically successful; go
    to Step 6. If the other party is not surprised, go to Step 2.
 3. Decision to Pursue: The other party decides whether to pursue. The PCs decide
    for themselves; monsters must make a morale check (defined in Chapter 8). On a
    successful morale check, the monsters give chase (go to Step 4). On an unsuc-
    cessful morale check, the monsters do not chase (go to Step 6).
 4. Attempt to Evade: The DM rolls on the Evasion Table. If the PCs succeed, they
    have evaded the pursuers (go to Step 6). If they fail, pursuit continues (Step 5).
 5. Pursuit Continues: Movement is measured in rounds and conducted at running
    speed; both sides roll 1d6 for initiative once per round; the side with the higher
    roll moves first each round. The chase continues until one of the following
    happens:
    a. The pursuers decide to give up. Monsters must make a new morale check
       every five rounds and give up the chase if they fail the check. Go to Step 6.
    b. The evading party is caught by the pursuers (because of superior speed or
       terrain obstacles); Combat occurs; go to the Combat Checklist in Chapter 8.
    c. The evading party escapes (by using magic spells or by finally making a
       successful evasion roll on the Evasion Table when terrain and circum-
       stances warrant). Go to Step 6.
 6. Regain Bearings: Evaders rest and determine where they now are.
```

| # | Fact | Confidence |
|---|---|---|
| N-5 | **PRINTED DEFECT — self-loop.** Step **2**'s own text ends *"go to Step 2"* | **DIRECT PRIMARY TEXT** — confirmed at magnification, verbatim |
| N-6 | Automatic success: evader unsurprised **and** pursuer surprised → skip to step 6 | **DIRECT PRIMARY TEXT** |
| N-7 | Pursuit is at **running speed**, time in **rounds**, `1d6` initiative each round | **DIRECT PRIMARY TEXT** |
| N-8 | Pursuer morale re-check **every five rounds** | **DIRECT PRIMARY TEXT** |

**N-5 remains unadjudicated.** Protocol §10.2.2 case 2 forbids picking a reading. Recorded, not resolved.

### 5.3 `Evasion Table`, p. 99 — and the resolution direction *(pass 1 omitted the latter)*

```text
Evasion Table
Party   No. of Monsters   Chance of      Condition              Adjustment
Size    Encountered       Evasion        in Effect              to Chance
 1-4      1                50%           Wooded terrain            +25%
          2-3              70%           Featureless terrain       -15%
          4 +              90%           Pursuers are twice
 5-12     1-3              35%             as fast as evaders      -25%
          4-8              50%           Evaders are twice as
          9 +              70%             fast as pursuers        +25%
13-24     1-6              25%           Pursuers have
          7-16             35%             scouts in place         -15%
          17 +             50%
25 +      1-10             10%
          11-30            25%
          31 +             35%
```

| # | Fact | Confidence |
|---|---|---|
| N-9 | Chance is keyed on **party size × number of monsters encountered** | **DIRECT PRIMARY TEXT** |
| **N-10** | **Resolution is ROLL-UNDER on `d100`.** RC's worked example: *"The DM rolls a d100; on a **01-70**, the PCs have **successfully evaded** the monsters, and on a **71-00**, the monsters successfully pursue"* — for a stated 70% chance | **DIRECT PRIMARY TEXT** |
| N-11 | **Floor:** *"Regardless of the number of evasion penalties, the evading group **always has at least a 5% chance** to evade."* | **DIRECT PRIMARY TEXT** |
| N-12 | Large parties may split: *"If a large party breaks up into small parties, roll for each small party separately; in this way, **some parties could evade while others could be caught**."* | **DIRECT PRIMARY TEXT** |
| N-13 | Speed adjustment is **symmetric and explained in prose**: the faster group adjusts by 25% in its favour, whichever side it is | **DIRECT PRIMARY TEXT** |
| **N-14** | **PRINTED DEFECT — scouts.** Prose: *"a **- 10%** penalty is applied to the evasion chance"*. Table: `Pursuers have scouts in place` **`-15%`**. Both printed on **p. 99**, in adjacent columns | **DIRECT PRIMARY TEXT** — both confirmed at magnification |

**N-10, N-11 and N-12 are new in this pass.** N-10 in particular is mechanically essential —
without it the table's percentages cannot be resolved at all, and pass 1 shipped without it.

### 5.3a Governing mechanics on pp. 98–99 that had no evidence row until pass 3

The section was read as a complete unit, but five operative statements inside it were described
only in prose rather than recorded as evidence. Added:

| # | Fact | Object | Confidence |
|---|---|---|---|
| **N-32** | **Catch-up is a DM-tracked positional determination, not a roll:** *"If the pursuers end one round having caught up to the evaders **(the DM should be keeping track of their relative positions to determine this)** and then **win initiative the next round**, they can attack, **forcing the evaders to turn and fight**."* | p. 99 col. 3 | **DIRECT PRIMARY TEXT** |
| **N-33** | **Obstacle branch:** *"the evaders could run into some obstacle that prevents them from continuing (a sheer cliff face, a dead-end hallway, a magically locked door, another party of enemies, and so on). In these situations, combat usually results, though **the evaders might choose to surrender instead**."* | p. 99 col. 3 | **DIRECT PRIMARY TEXT** |
| **N-34** | **DM adjustment, quoted in full:** *"The DM may adjust evasion chances for terrain, differences in speed, and other factors **as noted in the Evasion Table**."* | p. 99 col. 1 | **DIRECT PRIMARY TEXT** |
| **N-35** | **Area familiarity:** *"If monsters are familiar with an area, they may be able to evade pursuers by **rapidly turning corners, closing doors behind them**, and so forth."* No value is attached | p. 99 col. 1 | **DIRECT PRIMARY TEXT** |
| **N-36** | **Step 2's automatic evasion has a printed duration and direction:** the surprising group *"may automatically evade the surprised group by **turning away and moving off at another direction at running speed for one round**"*, after which *"The nonsurprised group has enough time to get clear of the area before the surprised group can recover enough to give chase"* | pp. 98–99 | **DIRECT PRIMARY TEXT** |

**N-32 matters for Stage B**: step 5b's *"caught"* is not a die roll. RC delegates it to DM
position-tracking plus an initiative win.

**N-34 is corrected in pass 4.** Pass 3 quoted it as *"…and other factors"* with the trailing
clause dropped, and concluded the adjustment list was *"explicitly open-ended."* The full
sentence ends **"as noted in the Evasion Table"**, which points the reader **back to the table's
five printed conditions** rather than away from them. **That conclusion is withdrawn.**

The sentence is genuinely ambiguous — *"and other factors as noted in the Evasion Table"* can be
read as *(other factors) as noted in the table* (closed) or as *terrain, speed and other factors,
as [those are] noted in the table* (open, with the table as exemplar). **`ENC-005` does not
choose**, and the immediately following prose supplies unlisted adjustments anyway — the `25%`
woods example and the `+/-25%` double-speed rule (N-13) — which is evidence but not a resolution.
Recorded at §8 Q3 as part of the terrain question rather than settled here.

**N-14 remains unadjudicated.** `INTERNAL SOURCE CONFLICT REQUIRES REVIEW`.

### 5.4 Terrain — the distinction pass 1 drew, confirmed and held

| # | Fact | Confidence |
|---|---|---|
| N-15 | The Evasion Table's `Condition in Effect` column adjusts an **evasion percentage**. It is **not** a movement-rate modifier | **DIRECT PRIMARY TEXT** |
| N-16 | *"Difficult terrain"* is given by **example only** — *"thick woods, a long dungeon corridor riddled with doors and side passages, etc."* — with **no criterion** | **DIRECT PRIMARY TEXT** |
| N-17 | Terrain also appears as an **escape trigger**: evaders temporarily out of vision range who reach difficult terrain get **a second Evasion Table roll**, success meaning *"the pursuers fail to follow their tracks"* | **DIRECT PRIMARY TEXT** |
| N-17a | RC has a separate **`Tracking`** skill (N-37) whose success the DM varies by *"age of the tracks, type of terrain"* — a second, **skill-based** route to the same question N-17 resolves with a percentage. **Recorded, not reconciled**; owner `CHAR-012` | **DIRECT PRIMARY TEXT** |
| N-18 | Terrain also appears as a **capture** cause: step 5b, *"caught … because of superior speed **or terrain obstacles**"* | **DIRECT PRIMARY TEXT** |

**No generic terrain mechanic is created, proposed, or imported.** The `Terrain Effects on
Movement Table` (p. 88), the `Charge` terrain list (p. 154) and the previously rejected Mystic
rough-terrain material are each **enumerated and excluded by name** (§3.3, §9.3).

### 5.5 p. 100 — **correcting pass 1's exclusion**

**Pass 1 marked p. 100 column 1 excluded while quoting from it.** That was wrong. Column 1 is
the direct continuation of the dungeon/wilderness evasion procedure and carries the section's
**sixth and final definition**.

| # | Fact | Object | Confidence |
|---|---|---|---|
| N-19 | **Dropped goods:** *"Evaders can drop goods that the monsters might want; a hungry monster might want meat rations, for example, while a vampire might be more content with magical treasures. In these cases, the DM rolls **1d6** **if he or she feels that the item dropped is indeed appealing to the monster**. On a **1-3**, the monster stops to consume (or retrieve) the proffered goods and is **delayed long enough for the evaders to get away**."* | p. 100 col. 1 | **DIRECT PRIMARY TEXT** |

**N-19's gating condition was elided in pass 2** and is restored: the `1d6` is rolled **only if
the DM judges the dropped item appealing to that monster**. The die is not unconditional, and a
specification that treated it as such would be wrong.
| N-20 | **`Regain Bearings`** is a printed subheading — step 6's content: *"If the evaders do get away, they need to **rest from their exertions** and regain their bearings—that is, determine where they now are."* | p. 100 col. 1 | **DIRECT PRIMARY TEXT** |
| N-21 | *"**For every round the chase lasted, the evaders moved at full running speed** in directions chosen or assumed by the DM. They didn't have time to consult their map, and the DM should enforce this fact rigorously."* | p. 100 col. 1–2 | **DIRECT PRIMARY TEXT** |
| N-22 | *"They didn't have time to consult their map, and the DM should enforce this fact rigorously. **If their movement carried them into areas they already knew or had mapped, they're fine.** But, at the DM's discretion, their attempts at evasion could have carried them deep into unknown territory (such as … **unexplored dungeon levels**), and **now the characters are lost**; they'll have to explore their way back to the areas they know."* | p. 100 col. 2 | **DIRECT PRIMARY TEXT** |

**N-22's negative branch was elided in pass 3** and is restored: *"If their movement carried them
into areas they already knew or had mapped, **they're fine**."* Becoming lost is **not** an
automatic consequence of a chase — it is conditioned on the flight having crossed into unmapped
territory, at DM discretion. A specification built on pass 3's truncated quote would have got
this wrong.

**Correct classification of p. 100:**

```text
col. 1        GOVERNING -- dropped goods (N-19) + Regain Bearings (N-20, N-21)
col. 1-2      GOVERNING -- the lost-in-a-dungeon outcome (N-22)
col. 2        EXCLUDED  -- "Evasion at Sea", naval
col. 3        EXCLUDED  -- Ship Evasion Table (naval) + "Balancing Encounters
                          (Optional)" (ENC-007)
```

**N-21 materially sharpens pass-1 open question Q4** (*"do chase rounds count against
`CHAR-005` §9's 30-round running limit?"*). RC states plainly that the evaders **moved at full
running speed for every round the chase lasted**, and that they **must then rest**. Both halves
of `CHAR-005` §9's exhaustion contract are therefore engaged by the printed text. **RC still
does not say the chase rounds count against the 30-round maximum**, so the question stays open
— but it is now an open question with direct primary text on both sides of it, not an
inference.

**N-22 and the getting-lost conclusion — corrected in pass 3.** Pass 1 concluded RC has no
dungeon getting-lost material. Pass 2 narrowed that to *"no dungeon getting-lost **procedure**;
RC supplies a die-roll procedure only for wilderness travel."* **That is falsified by p. 83
(§5.7). RC supplies a dungeon-side procedure, and it is keyed to exactly the flight case this
card governs.**

### 5.7 `Caving` (p. 83) — a governing object for checklist step 6

**Pass 2 never inspected Chapter 5.** `Sample Skills Table . 82` is a named object in the p. 301
Tables Index; the second independent review reached it by reading that index entry by entry.

| # | Fact | Object | Confidence |
|---|---|---|---|
| **N-28** | **`Caving`**: *"an ability to always know where one is while exploring underground caves, cavern complexes, rivers, etc. … The Caving skill can also be used in a maze. Skill checks are necessary when the character has become disoriented. **If he is forced to flee for a long stretch, he must make a skill check to keep from being lost. (Characters without this skill automatically become lost in such a situation.)**"* | p. 83 | **DIRECT PRIMARY TEXT** |
| N-29 | A skill check is **`1d20` ≤ the governing ability score**; `20` always fails. `Caving` is a **Wisdom** skill | pp. 82 | **DIRECT PRIMARY TEXT** |
| N-30 | **RC** calls the system optional: *"Using general skills is **optional**. If the DM doesn't want to use them in his or her campaign, they won't be used."* | p. 81 | **DIRECT PRIMARY TEXT** |
| **N-30a** | **The project already required it.** `INVENTORY.md`'s `CHAR-012` row: *"RC Optional/Additional system → **Project-Selected: REQUIRED (`DEC-0008`)**"* | `INVENTORY.md`, `DEC-0008` | **repository fact, not a source fact** |
| **N-37** | **`Tracking`**: *"The character can follow tracks. The DM is free to increase or penalize the chance of success depending on the circumstances (**age of the tracks, type of terrain**, number of tracks being followed, and so forth)."* p. 86 adds that when one tracker fails, *"there are no tracks to find,"* so others may not re-roll | pp. 85–86 | **DIRECT PRIMARY TEXT** |
| **N-31** | **`Endurance`**: a successful check lets a character *"**run** (or perform some demanding task) **for an hour** without collapsing"*, re-checked each hour at a cumulative `+1` penalty; on completion or failure he *"must rest for **three times** the amount of time he was performing that task"* | p. 83 | **DIRECT PRIMARY TEXT** |

**N-28 is step 6.** Checklist step 6 reads *"Regain Bearings: Evaders rest and determine where
they now are"*, and p. 100 says evasion may leave the party *"lost"* (N-22). p. 83 supplies the
**determination**: *forced to flee for a long stretch* → a `Caving` check, or **automatic loss
without the skill**. The trigger condition is the chase itself.

**Corrected statement of the negative**, with the condition made explicit:

```text
WRONG (pass 2)   "RC supplies no dungeon getting-lost procedure."

WRONG (pass 3)   The above, corrected -- but made CONDITIONAL on whether the
                 optional general-skills system is in use, and escalated to the
                 human owner as an undecided question.  DEC-0008 had already
                 decided it (N-30a).

CORRECT          RC supplies a dungeon-side procedure for becoming lost while
                 fleeing: a Caving skill check (1d20 <= Wisdom), with AUTOMATIC
                 loss for characters lacking the skill (p. 83).  It is not a
                 die-roll-against-a-table procedure like the wilderness Game Day
                 step 2 (1d6, p. 91); it is a skill check.

                 DEC-0008 selected General Skills as project-REQUIRED, so this
                 procedure is IN FORCE for V1.  It is not conditional on an
                 open decision, and there is no open decision to escalate.

                 p. 100's negative branch still applies and pass 3 elided it:
                 "If their movement carried them into areas they already knew or
                 had mapped, THEY'RE FINE."  Becoming lost is not automatic on a
                 chase; it applies when the flight carried the party into
                 unknown territory.
```

Note that N-28's second sentence reaches **beyond skill-havers**: *"Characters without this
skill **automatically** become lost in such a situation."* That is a rule about the party at
large whenever the optional system is switched on.

**Ownership: `CHAR-012` [UNRESEARCHED]** owns the skill. **`ENC-005` does not absorb the
general-skills system** and claims no skill mechanic. `CHAR-012` is now named as a **step-6
provider** in §7.1 rather than left as a footnote.

**N-31 bears on Q4.** RC's own p. 88 text names `Endurance` as the exception to the 30-round
running maximum (N-27a), and p. 83 gives its terms. This is recorded because Q4 asks whether
chase rounds count against that maximum; it does **not** answer Q4, and `ENC-005` claims none
of it.

### 5.5a `Exhaustion` (p. 88) — the rules that collide with step 5, enumerated in pass 3

Pass 2 did not enumerate the General Index entry `Exhaustion . 88`, and carried no evidence row
for the p. 88 rules — although step 5 conducts the whole chase **at running speed**, which is
what p. 88 limits. All of this is **landed `CHAR-005` §9's** and is **consumed, not re-derived**.

| # | Fact | Object | Confidence |
|---|---|---|---|
| N-27a | Running is *"toward **or away from an enemy**"*, at normal speed in feet **per round**, i.e. three times encounter speed. *"A character can run at maximum speed for **30 rounds at most (5 minutes)** before becoming exhausted. (Characters with the optional **Endurance** skill can maintain this pace for longer periods of time.)"* | p. 88 | **DIRECT PRIMARY TEXT** |
| N-27b | *"An exhausted character must **rest for at least three turns (30 minutes)** before running or fighting again."* | p. 88 | **DIRECT PRIMARY TEXT** |
| **N-27c** | *"A character who becomes exhausted but is forced to continue running **cannot use his maximum running speed. He drops to encounter speed** and cannot move any faster until he has rested."* | p. 88 | **DIRECT PRIMARY TEXT** |
| N-27d | Exhausted and forced to fight: monsters gain **`+2`** to hit him; he subtracts **`2`** from damage rolls (minimum 1) | p. 88 | **DIRECT PRIMARY TEXT** |

**N-27c is mechanically significant inside the pursuit procedure and pass 2 missed it.** Step 5
is a speed contest run in rounds. If a chase passes 30 rounds, RC drops the exhausted side
**from running speed to encounter speed** — roughly a threefold reduction — which changes the
outcome of the very comparison step 5b decides (*"caught … because of superior speed"*).
Likewise N-27d and N-27b feed step 5b's exit into combat and step 6's rest.

**This does not resolve Q4; it sharpens it further.** RC states the running maximum (N-27a), the
chase's use of running speed (N-7, N-21), the consequence of exceeding it (N-27c) and the rest
requirement (N-27b, N-20) — and **still never says whether chase rounds are counted against the
30**. The objects are now all inspected, so the question is a genuine silence rather than an
uninspected gap (§10.2.2 **case 3**).

**Ownership: `CHAR-005` §9 [LANDED]** owns every row above; `CHAR-012` owns `Endurance`.
**Nothing here is claimed by `ENC-005`.**

One routed observation, reported not absorbed: RC p. 108's `Attack Roll Modifiers Table` prints
`Attacker exhausted −2` as an **attack roll** modifier, while p. 88 (N-27d) puts the `−2` on
**damage** rolls. Landed `CHAR-005` §9 records the p. 88 reading. **Not adjudicated, not
absorbed** — flagged to the human owner; see `EXP-006`'s §8 Q13.

### 5.6 p. 104 — `Retreat` and `Fighting Withdrawal`, now **visually verified and complete**

Pass 1's §14.1 quoted `Retreat`'s first paragraph and stopped. The operative sentence is the
second paragraph. Both maneuvers, verbatim:

```text
Fighting Withdrawal
    A character can only perform this maneuver when he begins his combat round in
hand-to-hand combat with an enemy. With this maneuver, the character backs away
from his enemy at a rate of 5' per round. He makes no attack unless his enemies
follow him later in the same combat round, on the enemies' own movement phase. ...
    If he is not in hand-to-hand combat with his enemy when his movement phase comes
around in the next round, he can go to running speed that next round.

Retreat
    A character can only perform this maneuver when he begins his combat round in
hand-to-hand combat with an enemy. The character runs away from his enemy at
greater than half his encounter speed, up to his full encounter speed. He forfeits
the armor class bonus of his shield. Any enemy attacking him later in the combat
round ... receives a +2 attack roll bonus this round. ...
    If the character is not in hand-to-hand combat with his enemy when his movement
phase comes up in the next round, he can go to running speed that next round.
```

| # | Fact | Confidence |
|---|---|---|
| N-23 | **Both** maneuvers carry the **identical** running-speed bridge. Pass 1 attributed it only to `Fighting Withdrawal` | **DIRECT PRIMARY TEXT** |
| N-24 | `Retreat` speed: *"greater than half his **encounter speed**, up to his full encounter speed"* — consumes `CHAR-005` **[LANDED]** | **DIRECT PRIMARY TEXT** |
| N-25 | `Fighting Withdrawal` speed: **flat `5'` per round** | **DIRECT PRIMARY TEXT** |
| N-26 | `Retreat` costs the shield's AC bonus and grants attackers **`+2`**, *"the same +2 that characters normally get for attacking from behind"* | **DIRECT PRIMARY TEXT** |
| N-27 | The `Combat Maneuvers Table` lists both under **`Hand-to-hand phase`**, `Who Can Perform: All characters` | **DIRECT PRIMARY TEXT** |

**Ownership, stated plainly.**

```text
The maneuvers themselves are COMBAT-*'s.  They are printed in Chapter 8, listed in
the Combat Maneuvers Table, and executed inside a combat round's hand-to-hand phase.
ENC-005 does not own them and does not claim them.

But N-23 is RC's PRINTED TRANSITION from a combat round into a chase: the round after
disengagement, the character "can go to running speed" -- which is exactly the speed
the Evasion Checklist step 5 conducts pursuit at (N-7).  The bridge is EVIDENCE for
ENC-005's entry boundary, and the card's TITLE claims the word "Retreat".
```

**This is a routing question for the human owner, not an evidence gap** (§8 Q6). Pass 1's
routing was defensible; its evidence was incomplete. Both are now on the record.

---

## 6. Whole-source cross-reference pass

### 6.1 Search terms

```text
evade  /  evasion  /  evading  /  evaders  /  elude  /  escape  /  get away
pursue  /  pursuit  /  pursuers  /  pursuing  /  chase  /  give chase  /  flee
retreat  /  withdraw  /  fighting withdrawal  /  turn and run  /  run away
running speed  /  encounter speed  /  initiative  /  morale  /  surprise
terrain  /  difficult terrain  /  obstacles  /  vision range  /  visual range
lost  /  bearings  /  rest  /  exertions  /  drop  /  dropped goods
```

### 6.2 Cross-references found and followed

| From | To | Followed? | Result |
|---|---|---|---|
| p. 91 Game Day 4b → *"'Evasion and Pursuit' section"* | 98-100 | **yes** | N-2 |
| p. 93 Encounter Checklist 5c → *"pursuit and evasion rules later this chapter"* | 98-100 | **yes** | N-1 |
| p. 98 `Contact` → *"the DM determines the encounter distance"* | 93 | **yes** | N-4 — the light-conditioned table |
| p. 99 step 3 → *"a morale check (**defined in Chapter 8**)"* | 103 | **yes, to ownership only** | `ENC-004` **[UNRESEARCHED]** |
| p. 99 step 5b → *"go to the **Combat Checklist in Chapter 8**"* | 102 | **yes, to ownership only** | `COMBAT-006` **[UNRESEARCHED]** |
| p. 99 prose → *"the Attack Roll Modifiers Table on page 108"* (via p. 104) | 108 | **yes, to ownership only** | `COMBAT-*` |
| p. 100 → *"they need to rest from their exertions"* | `CHAR-005` §9 | **yes, to ownership only** | **`EXP-004` NOT reopened** |
| p. 69 `Oil` → *"poured out and ignited to **delay pursuit**"* | 98-100 | **yes** | **RC states no mechanic.** No Evasion Table row, no adjustment, no delay value. Recorded from both sides; **nothing invented** |
| `Retreat`/`Fighting Withdrawal` → running speed | `CHAR-005` | **yes** | N-23, N-24 |

### 6.3 Negative results (Guardrail B — research operations, not source properties)

- **RC gives no separate dungeon evasion procedure.** One procedure covers dungeon and
  wilderness; only *naval* evasion is split out (p. 100). **Not located after inspecting**
  pp. 91, 93, 98–100, the p. 301 Tables Index and the General Index entries `Evasion` and
  `Pursuit`.
- **RC states no criterion for "difficult terrain"** — examples only. Not located after
  inspecting pp. 99–100, p. 88 and the `Terrain` index entries.
- **RC states no mechanic for oil poured to delay pursuit.** Not located after inspecting
  pp. 69, 98–100 and the Evasion Table's full condition column.
- **RC does not say whether chase rounds count against the 30-round running maximum.** Not
  located after inspecting pp. 98–100, **p. 88 in full (§5.5a)**, p. 83's `Endurance` entry, and
  the General Index entries `Exhaustion . 88`, `Running speed . 88, 103` and `Skills . 82-85, 92`.
  All governing objects are now inspected, so this is §10.2.2 **case 3**, not case 1.
- **No marching-order or formation input appears anywhere in the section.** The procedure needs
  party **size** (N-9), not order. Confirms landed `EXP-003` case `D32`. **`EXP-010` not
  absorbed.**

---

## 7. The dependency finding — **preserved and sharpened** (direction §12)

Pass 1's most consequential finding stands: **inventory-level dependency status is not
equivalent to executable-procedure readiness.** `INVENTORY.md` lists `ENC-005`'s dependencies
as `EXP-002` and `EXP-003`, both landed, so the card reads as unblocked. **Its printed
procedure is not.**

### 7.1 The six steps, each with its provider and that provider's status

| Step | What it needs | Provider | Status | RC page |
|---|---|---|---|---|
| **1 Contact** | encounter occurrence; **encounter distance** (itself **gated on surprise**, N-4a); **surprise states** | `ENC-001` + `ENC-002` | **Unresearched** ×2 | 92–93 |
| **2 Decision to Evade** | **surprise** states of both sides | `ENC-002` | **Unresearched** | 93 |
| **3 Decision to Pursue** | **morale check** (monsters/NPCs) | `ENC-004` | **Unresearched** (`DEC-0008 REQUIRED`) | 103 |
| **4 Attempt to Evade** | party size, monster count, `d100` | **`ENC-005` itself** | **owned here** | 99 |
| **5 Pursuit Continues** | **`1d6` initiative**/round; **running speed**; **relative speed** | `COMBAT-006` + `CHAR-005` **[LANDED]** + `MON-003` | **Unresearched** ×2 | 99, 102, 88 |
| **5a** | **morale** re-check every 5 rounds | `ENC-004` | **Unresearched** | 103 |
| **5b** | **Combat Sequence Checklist** exit | `COMBAT-*` | **Unresearched** | 102 |
| **6 Regain Bearings** | **rest**; position/**lost determination** | `CHAR-005` §9 **[LANDED]** for rest; **`CHAR-012` for the `Caving` check** (N-28) | **Unresearched** ×1 | 83, 91, 100 |

**Five of the six steps cannot be executed without a card that has not been researched** —
step 6 joins the list in pass 3, once `Caving` is enumerated. **Step 4 is the only step
`ENC-005` fully owns.**

The count of distinct unresearched counterparties rises from five to **six**:
`ENC-001`, `ENC-002`, `ENC-004`, `COMBAT-006`, `MON-003`, `CHAR-012`.

### 7.2 The governance question this raises — **evidence presented, decision not taken**

The direction requires this to be put to the human owner rather than answered here.

```text
OPTION A -- Stage B now, as a partially specified procedure with routed dependencies.
    ENC-005 would name encounter distance, surprise, morale, initiative, monster
    speed and the Caving check as CALLER-SUPPLIED INPUTS and specify only step 4
    plus the sequencing.
    COST: a contract with SIX unresearched counterparties.  This is the exact
          concern that DEFERRED EXP-010 (BOUNDARY-CORRECTION §4), where THREE
          unresearched consumers were judged sufficient to defer.

OPTION B -- Defer Stage B until ENC-001/ENC-002/ENC-004/COMBAT-006/MON-003 are
    researched, and treat evasion as part of a later encounter cluster.
    COST: CLUSTER-004 would carry only EXP-006.

The precedent set by EXP-010's deferral points toward B.  That is an OBSERVATION
about consistency, not a recommendation, and NOT a decision taken in Stage A.
```

---

## 8. Unresolved questions (§10.2 vocabulary, verbatim)

| # | Question | Disposition |
|---|---|---|
| Q1 | Underworld-only, or RC's general evasion procedure? RC prints one procedure for both settings and splits out only naval. | **RETAINED AS GENUINE SOURCE AMBIGUITY** — the *source* is unambiguous (one procedure); the **card's** narrowing is a project decision. Interacts with the standing Wilderness reachability decision. **Stage B cannot begin without it** |
| Q2 | Can the card be specified before its five unresearched providers? | **CONFIRMED OUT OF SCOPE** — governance decision. Evidence at §7 |
| Q3 | *"Difficult terrain"* has no criterion (N-16). | **RETAINED AS GENUINE SOURCE AMBIGUITY** — the second-roll escape (N-17) is not executable without a DM-input flag or a terrain mechanic RC does not supply |
| Q4 | Do chase rounds count against `CHAR-005` §9's 30-round running limit? | **RETAINED AS GENUINE SOURCE AMBIGUITY** — **sharpened** by N-21: RC states full running speed for every chase round *and* a rest requirement, but never links them to the 30-round maximum |
| Q5 | Scouts: prose `−10%` vs table `−15%` (N-14). | **RETAINED AS GENUINE SOURCE AMBIGUITY** (§10.2.2 **case 3** — all governing objects inspected, both values visually verified on the same page, nothing uninspected). `INTERNAL SOURCE CONFLICT REQUIRES REVIEW` |
| Q6 | Checklist step 2's *"go to Step 2"* self-loop (N-5). | **RETAINED AS GENUINE SOURCE AMBIGUITY** (§10.2.2 case 3) |
| Q7 | Does the `Retreat` / `Fighting Withdrawal` running-speed bridge (N-23) belong here or to `COMBAT-*`? | **CONFIRMED OUT OF SCOPE for Stage A** — a routing decision. Evidence complete on both sides (§5.6) |
| Q8 | Does `CHAR-012`'s `Caving` skill modify step 6? | **RESOLVED BY SOURCE INSPECTION — pass 3.** **Yes.** p. 83 states it in terms: *"If he is forced to flee for a long stretch, he must make a skill check to keep from being lost. (Characters without this skill automatically become lost in such a situation.)"* (N-28). `CHAR-012` is named as a **step-6 provider** in §7.1. Pass 2 classified this `BLOCKED` **over a single page it had not opened** — see §8.2 |
| Q9 | Who owns "lost in a dungeon"? | **CONFIRMED OUT OF SCOPE**, ownership **`CHAR-012`** for the skill-check path (N-28) and **unowned** for the no-skill-system path, where RC leaves it to DM discretion (N-22). No Rule ID is invented |

**Zero silent unresolved research tasks at this gate**, and — after pass 3 — **zero `BLOCKED`
rows.**

### 8.2 The §17 conflict pass 2 carried, and why it was a real defect

Pass 2 recommended `EVIDENCE READY FOR HUMAN REVIEW` while its own closure gate carried a row
classified `BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED`. **Those cannot coexist.** §10.2
exists to prevent exactly this, and §17 makes the block a stop.

Worse, the block was not real. Pass 2 justified it as *"blocked on `CHAR-012`, which is
unresearched and out of this cluster — not a gap in `ENC-005`'s own coverage."* But the question
was not blocked on a card; **it was blocked on one page**, p. 83, which pass 2 never opened. The
answer was one page away, and the `BLOCKED` label made an uninspected page look like somebody
else's research backlog.

```text
That is the precise failure mode DEC-0010 §10.2 names:

    "A packet may contain genuine rule ambiguities.  It may NOT contain
     UNFINISHED SOURCE INSPECTION DISGUISED AS AN AMBIGUITY."

A BLOCKED row is the strongest form of that disguise, because it reads as diligence.
```

Pass 3 opened the page. Q8 is `RESOLVED BY SOURCE INSPECTION`.

**Rule this packet now holds itself to:** before classifying anything `BLOCKED`, open every page
the source's own indices point at for it. `Caving` was reachable from `Sample Skills Table . 82`
in the p. 301 index and from `Skills . 82-85, 92` in the General Index — both of which pass 2
listed.

### 8.1 Reconciliation table (§10.2.1) — pass 1's open statements

| Pass-1 open statement | Region implicated | Inspection completed? | Result | Owner | Still blocks? |
|---|---|---|---|---|---|
| "p. 100 col. 1 excluded" | **p. 100** | **yes** | **WRONG — it is governing.** §5.5 | `ENC-005` | **No — corrected** |
| "p. 104 Retreat, OCR only" | **p. 104** | **yes, visually** | Quote was **incomplete**. §5.6 | `COMBAT-*` | **No — corrected** |
| d100 direction not stated | p. 99 | **yes** | **Roll-under**, N-10 | `ENC-005` | **No — corrected** |
| `Ship Evasion Table` undispositioned | p. 100 | **yes** | Excluded, naval, reason stated | — | **No** |
| `Combat Maneuvers Table` undispositioned | p. 104 | **yes** | Excluded, `COMBAT-*` | — | **No** |
| General Index cited, not enumerated | 302-304 | **yes** | §3.3, 20 entries dispositioned | — | **No** |
| Q1 underworld scope | 91, 98-100 | **yes** | Source unambiguous; card decision open | human | Yes — Stage B gate |
| Q3 difficult terrain | 99-100, 88 | **yes** | No criterion in RC | `ENC-005` | No — genuine ambiguity |
| Q4 chase rounds vs 30 | 98-100, 88, 103 | **yes** | Sharpened, not closed | human | No |
| Q5 / Q6 printed defects | p. 99 | **yes, magnified** | Case 3 | human | No |

---

## 9. Primary-Source Coverage Checklist (§9.3 — **required; entirely absent from pass 1**)

### 9.1 Structural units inspected — all as page images

```text
p. 81    Ch. 5   General Skills -- "Using general skills is optional"   -- pass 3
p. 82    Ch. 5   How Skills Are Used; SAMPLE SKILLS TABLE                -- pass 3
p. 83    Ch. 5   CAVING; ENDURANCE (Blind Shooting/Fire-Building read,
                 routed to EXP-006)                                      -- pass 3
p. 84-85 Ch. 5   Sample Skills Table read ROW BY ROW; TRACKING, Stealth,
                 Survival, Hunting inspected and routed                  -- pass 4
p. 86    Ch. 5   Positive and Negative Modifiers; Using Skills Together
                 (the Tracking failure example, N-37)                    -- pass 4
p. 88    Ch. 6   Character Movement Rates and Encumbrance; Terrain Effects;
                 RUNNING + EXHAUSTION rules (§5.5a)                       -- pass 3
p. 108   Ch. 8   Attack Roll Modifiers Table -- exhaustion rows only, routed
p. 91    Ch. 7   Ch. 7 opening definition; Game Turn + Game Day Checklists
p. 92    Ch. 7   Chance of Encounter Table; Encounter Distance section; surprise
                 1d6 rule and its three outcomes (N-4a, N-4b, N-4c)
p. 93    Ch. 7   Encounter Checklist; Encounter Distances Table; Monster Reactions
p. 97    Ch. 7   wilderness/castle encounter subtables          (excluded, read to confirm)
p. 98    Ch. 7   EVASION AND PURSUIT opening; Definitions; Contact; Decision to Evade
p. 99    Ch. 7   EVASION CHECKLIST; EVASION TABLE; Castle Reactions; all prose
p. 100   Ch. 7   Regain Bearings; Evasion at Sea; Ship Evasion Table; Balancing Encounters
p. 103   Ch. 8   Morale Scores Table                             (to ownership only)
p. 104   Ch. 8   COMBAT MANEUVERS TABLE; Retreat; Fighting Withdrawal   -- VISUAL, pass 2
p. 301   App. 4  Index to Tables and Checklists                  -- read in full
p. 302-304  App. 4  General Index                                -- read in full
```

### 9.2 Complete-entry inspection (§9.7)

The `Evasion and Pursuit` section was read **as one complete source unit**, pp. 98→100, not as
isolated search windows. Its six `Definitions` subsections map **1:1** onto the six checklist
steps:

```text
Contact  ->  Decision to Evade  ->  Decision to Pursue  ->  Attempt to Evade
         ->  Pursuit Continues  ->  Regain Bearings
```

**`Regain Bearings` is the sixth, and it is on p. 100.** Reading the section as a unit is what
makes pass 1's exclusion of that page visibly wrong.

### 9.3 Deliberate exclusions, with reasons

```text
Ship Evasion Table + Evasion at Sea (100)   Naval.  ENC-005 is underworld-scoped.
Balancing Encounters (100-101)              ENC-007, optional system.
Castle Reactions Table (99)                 Wilderness castle encounters.
Wilderness/City encounter subtables (97-98) EXP-008 / MON-001 -- excluded BY NAME.
Terrain Effects on Movement (88)            Wilderness MOVEMENT terrain; not the
                                            Evasion Table's terrain.  NOT imported.
Charge terrain list (154)                   MON-*/COMBAT-*.  NOT imported.
Mystic rough-terrain material               Previously rejected/unowned.  NOT consulted.
Morale Scores Table (103)                   ENC-004.  Opened to ownership only.
Combat Sequence Checklist (102)             COMBAT-006.  Opened to ownership only.
Attack Roll Modifiers Table (108)           COMBAT-*.  Opened to ownership only.
EXP-004 as a unified card                   DEFERRED.  Step 6's rest followed only far
                                            enough to establish CHAR-005 §9 owns it.
EXP-008 / MON-001 / TREAS-001               UNTOUCHED by direction.
CHAR-004                                    NOT reopened.  No price/enc/Coin/legality fact.
```

### 9.4 Unresolved items

All nine are in §8 with a §10.2 disposition. **None is unfinished source inspection disguised
as ambiguity.**

---

## 10. Falsification pass

| Tentative conclusion | Falsification attempted | Outcome |
|---|---|---|
| "p. 100 col. 1 is out of scope" (pass 1) | Read pp. 98–100 as one unit; checked the Definitions↔steps mapping | **REJECTED — falsified.** §5.5 |
| "The running-speed bridge is `Fighting Withdrawal`'s alone" (pass 1) | Obtained p. 104 as an image; read both entries complete | **REJECTED — falsified.** `Retreat` has it too (N-23) |
| "The `go to Step 2` self-loop is an OCR artifact" | Magnified the page image | **REJECTED.** Printed (N-5) |
| "The `−10%`/`−15%` split is an OCR artifact" | Magnified both, separately | **REJECTED.** Both printed on p. 99 (N-14) |
| "The Evasion Table is roll-high-to-succeed" | Read RC's own worked example | **REJECTED.** Roll-**under** (N-10) |
| "The card is underworld-specific in the source" | Searched the whole section + both index entries | **REJECTED.** One procedure, both settings (Q1) |
| "`EXP-010` marching order is needed" | Searched the section for formation/order/rank | **NOT LOCATED.** Party **size** only |
| "A generic terrain mechanic is required" | Enumerated every terrain object in both indices | **REJECTED.** Terrain adjusts a **percentage**, not a rate (N-15) |
| *"RC supplies no dungeon getting-lost procedure"* (pass 2) | **Pass 3:** read the p. 301 Tables Index entry by entry; opened `Sample Skills Table . 82` and Ch. 5 | **REJECTED — falsified.** `Caving`, p. 83 (N-28) |
| *"Q8 is `BLOCKED` on unresearched `CHAR-012`"* (pass 2) | **Pass 3:** opened the one page the question actually turned on | **REJECTED.** It was unfinished inspection, not a block (§8.2) |
| "Step 5's speed contest is unaffected by chase length" | **Pass 3:** read p. 88 in full | **REJECTED.** An exhausted runner **drops to encounter speed** (N-27c), changing the comparison step 5b decides |
| "The Evasion Table's five conditions are the closed adjustment set" | **Pass 4:** re-read p. 99 col. 1 **to the end of the sentence** | **NOT ESTABLISHED EITHER WAY.** Pass 3 rejected it on a truncated quote; the full sentence ends *"as noted in the Evasion Table"*, which cuts the other way. Recorded as part of Q3, **not resolved** (N-34) |
| "Step 5b's *caught* is a die roll" | Re-read p. 99 col. 3 | **REJECTED.** DM position-tracking plus an initiative win (N-32) |

---

## 11–18. Remaining §11 contents

- **(11) Conclusions rejected** — pass 1's p. 100 exclusion; its partial `Retreat` attribution. §10.
- **(12) Unresolved RC questions** — §8, Q1–Q9.
- **(13) Belongs to another card** — §3.2, §3.3, §7.1, §9.3.
- **(14) Alternate-source research required?** — **Candidate, not performed, not authorized.**
  Precise gap statement: *"RC p. 99 prints two different scout adjustments (`−10%` prose,
  `−15%` table) and a step-2 self-loop. The BECMI Expert set carries an ancestor evasion
  procedure that may disambiguate both."* This is a `DEC-0011` **request**, requiring human
  authorization. AD&D remains excluded.
- **(15) Simulator Ruling areas** — Q5 and Q6 are **named** as candidates if lineage research
  is declined. **None drafted, none proposed.** Protocol §16 places rulings last.
- **(16) `REVALIDATION_REQUIRED` withholding** — **not applicable**; no approved legacy card.
- **(17) Access limitations** — p. 104 defeated ~20 IIIF attempts during pass 1 and was
  obtained first attempt in pass 2; p. 88 needed four attempts. **All pages cited are images.**
- **(18) Overall confidence** — **High** for the transcribed procedure, table, checklist,
  entry conditions and the p. 104 maneuvers: all `DIRECT PRIMARY TEXT` from page images, two
  of them magnification-confirmed. The card's uncertainty is **not** coverage — it is (a) two
  genuine printed defects and (b) five unresearched providers.

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
 8  Caving (p. 83) opened and recorded; §5.5/N-22 and §6.3's getting-lost
    negative restated on the corrected premise; Q8 reclassified from BLOCKED
    to RESOLVED BY SOURCE INSPECTION; CHAR-012 named as a step-6 provider   §5.7, §7.1
 9  Exhaustion . 88 enumerated; the 30-round maximum, the RC-named Endurance
    exception, the 3-turn rest and "drops to encounter speed" all recorded;
    Q4 re-attested under §10.2.2 case 3                                     §5.5a
10  "Combat occurs;" restored to step 5b's verbatim block                   §5.2
11  Evidence rows added for the catch-up determination, the obstacle branch,
    the open-ended DM adjustment, area familiarity and step 2's one-round
    run; N-19's gating condition restored                                   §5.3a
12  (discharged mid-review -- p. 92 opened, N-4a/b/c added)                 §5.1
13  Adversarial self-review re-run FROM the p. 301 index, entry by entry    §10
17  N-19 gating condition restored                                         §5.5
```

**The §17 conflict is cleared: this packet now carries no `BLOCKED` row** (§8.2).

**Stage B has not begun and is not authorized. No Rule Card is drafted. No production code is
touched. Neither printed defect is adjudicated.**

Two things must be settled by the human owner before Stage B could begin:

```text
Q1   Is ENC-005 underworld-only, or does it own RC's one general evasion procedure?
§7.2 Does Stage B proceed with SIX routed unresearched counterparties, or defer --
     given that EXP-010 was deferred over THREE?
```

**A third item raised by pass 3 is WITHDRAWN in pass 4.** Pass 3 escalated the general-skills
system to the human owner as a newly discovered optional system whose status the simulator had
not decided, and claimed `BOUNDARY-CORRECTION` §6 item 2's *"none found"* was now falsified.

**That was wrong.** `DEC-0008` selected General Skills as **project-REQUIRED**, and
`INVENTORY.md`'s `CHAR-012` row states it (N-30a) — in the same registry whose `ENC-004` row
this packet quotes `DEC-0008 REQUIRED` from, four sections earlier, in §4.4's own dependency
table. **`BOUNDARY-CORRECTION` §6 item 2 remains correctly closed. There is no decision to
escalate**, and the human owner's time is not asked for.

The substantive consequence is the opposite of an open question: `Caving`'s step-6 determination
is **in force for V1**, not contingent.
