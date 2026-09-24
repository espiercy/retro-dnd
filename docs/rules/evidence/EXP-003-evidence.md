# Stage-A Evidence: EXP-003 — Dungeon Movement

> **✅ STAGE B COMPLETE, 2026-09-24. Rule Card drafted: `docs/rules/exploration/dungeon_movement.md` — `AWAITING_APPROVAL`.**
>
> **This packet required no human adjudication and produced no Simulator Ruling.** None of the seven adjudicated questions belonged to it. Its two scope findings had already been settled by the 2026-09-14 governance decision and are carried into the card unchanged:
>
> - **Mapping** owns no separate time procedure, roll, failure mechanic or movement penalty. Ordinary dungeon movement already encompasses it — RC Ch. 6 p. 88 states the rate *"includes many assumed actions—**mapping**, peeking around corners, resting"*. The card records the consequence as a hard constraint: **charging time for mapping would double-count**.
> - **Special Terrain** is not this card's responsibility. The terrain rules RC states remain with wilderness movement, `ENC-005`, and `COMBAT-*`/`MON-*`. **No terrain mechanic is created from the Mystic Acrobatics wording** — it remains unowned, deliberately.
>
> **One dependency flows in from the adjudications:** `CHAR-005` may now yield a **fractional** movement rate for an active Mystic `MV` (e.g. `43⅓'`). `EXP-003` **consumes that rate and does not quantise it**; spatial snapping to map squares is a separate, unowned execution concern.
>
> ---
>
> *(Packet originally titled "EXP-003 — Dungeon Movement, Mapping & Special Terrain". That title is **no longer approved**; see the closure note immediately below. The body text below still uses the old title in places and is preserved unaltered as audit history.)*
>
> **✅ STAGE-A RESEARCHER CLOSURE (2026-09-14). The card is renamed and narrowed by human governance decision.**
>
> - **GOVERNANCE DECISION 3 APPLIED — the approved card name is now `EXP-003 — Dungeon Movement`.** The previous three-part title is no longer approved. This resolves the `CARD TITLE / RESPONSIBILITY BOUNDARY REVIEW REQUIRED` flag this packet raised at §7 and §11 item 2 — **raised by the researcher, decided by the human, applied here.**
> - **Mapping** remains documented as an activity **already encompassed by ordinary exploration movement**, on this packet's own evidence: RC Ch. 6 p. 88 states normal speed *"includes many assumed actions—**mapping**, peeking around corners, resting"*, and all four located presentations contain no die, no time cost and no failure state. **No separate mapping mechanic, time cost, roll, or failure state is to be created.** The §9 Challenge 2 warning stands: charging exploration time for mapping would double-count.
> - **"Special Terrain" is no longer an `EXP-003` responsibility.** The terrain rules RC actually states remain with the procedures that govern them — the per-day Terrain Effects on Movement and Traveling Rates by Terrain tables with **wilderness movement**; the dungeon *"difficult terrain"* evasion condition (Ch. 7 p. 98) with **`ENC-005`**; and the *"cannot charge in… broken, heavy forest, jungle, mountain, swamp"* prohibition (Ch. 14 p. 153, *"20 yards (20 feet indoors)"*) with **`COMBAT-*`/`MON-*`**.
> - **The rough/broken-terrain rate modifier presupposed by Mystic Acrobatics (Ch. 2 p. 31) is PRESERVED as an open RC question.** It is **not** assigned to a card and **not** invented. Narrowing `EXP-003` does not dispose of it.
> - **No mechanic, table reading, or open RC question in this packet is changed by the governance decision.** The Dungeon Movement findings are unaffected.
>
> **⚠ REMEDIATION PASS 1 APPLIED (2026-09-13). Two findings qualified, one citation corrected, both structural items closed.** The independent completeness review returned **`REMEDIATION REQUIRED / FAIL — unfinished structural inspection`** against the `CLUSTER-003` package committed at `e26a1e0`. The remediation record is `docs/rules/evidence/CLUSTER-003-remediation-pass-1.md`; **read it alongside this packet.** The original text below is preserved unaltered as audit history.
>
> **What changed as a result:**
>
> - **Special Terrain — QUALIFIED, not overturned.** Remediation located **RC Ch. 14 p. 153 "Charge"**: *"If a monster can run toward its opponent for 20 yards (**20 feet indoors**), it inflicts double damage… **A monster cannot charge in certain types of terrain: broken, heavy forest, jungle, mountain, swamp, etc.**"* This is **the first located RC rule in which terrain constrains movement at the round scale with the indoor case explicitly contemplated.** It constrains an **action**, not a rate or a turn cost, and it is a monster-side combat rule owned by `COMBAT-*`/`MON-*`. **`EXP-003`'s Special-Terrain gap therefore stands** — but the negative finding is now narrower and more precise than "no dungeon-scale terrain mechanic exists". Remediation §5.5, §7.
> - **Map scale — the 10′ square is a DEFAULT, not a constant.** RC Ch. 17 p. 260 (previously uninspected) adds *"with each square normally representing a 10' × 10' area, **or any other scale you prefer**"*. Three presentations are now located: Ch. 6 p. 87, Ch. 13 p. 148, Ch. 17 p. 260. Remediation §5.2.
> - **Mapping — finding unchanged and strengthened.** Two further presentations were located and read in full (**RC p. 5 "Mapping and Calling"** and the **Ch. 17 p. 262 Pre-Game Checklist**); neither contains a die, a time cost, or a failure state. Four presentations, no mechanic.
> - **CITATION CORRECTED.** "Mapping and Calling" is on **p. 5** (front matter / Setting Up), **not** Chapter 1, per the General Index entry `Mapping . 5, 148, 256, 257`. This packet's §4 and §6 cite it as Ch. 1; the quoted text is accurate, the location was not.
> - **Dungeon Movement — better bounded.** Newly located **RC Ch. 8 p. 103** states *"A character's normal speed is **never used during the combat sequence**"*, which positively confines normal speed to the exploration turn.
> - **§9 Challenge 4 (`EXP-010`) is CONFIRMED and additionally supported:** the General Index has **no** `Marching`, `Formation`, or `Carrying capacity` entry.
> - **Verdict unchanged and now raised formally: `CARD TITLE / RESPONSIBILITY BOUNDARY REVIEW REQUIRED`.** The card was **not** renamed; no governance authorizes a researcher to do so.
>
> **This is a Stage-A evidence artifact, not a Rule Card.** Produced under `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` (`DEC-0009`) and the primary-source completeness requirements adopted by `DEC-0010`. It is not mechanically authoritative, is not `APPROVED`, and authorizes nothing. **Stage B was not begun.**
>
> **Completeness status: `PREPARED FOR INDEPENDENT COMPLETENESS REVIEW` (protocol §10.1.1).** The independent completeness review required by §10.1.2 / `DEC-0010` item 14 has **not** been performed and may not be performed by this researcher.
>
> **Headline finding.** This card's `INVENTORY.md` title names three sub-responsibilities. On the evidence gathered, **one of them is a substantial RC procedure, one is a DM technique with no mechanic, and one appears to have no RC dungeon-scale rule at all.** That is a finding about the source, recorded with the objects that were inspected to reach it — not a recommendation to redraw the card.

## 1. Research Scope

**Investigating:** what the Rules Cyclopedia establishes about moving through a dungeon during exploration — what rate is used, against what time unit, what the rate is deemed to already include, how the map is produced, and whether dungeon terrain modifies movement.

**Cluster context:** `CLUSTER-003` — Equipped Dungeon Movement. `EXP-003` consumes `CHAR-005`'s rate and the landed `EXP-002` dungeon-turn machinery, and is the point at which the cluster's capability becomes visible in play.

**Assigned falsification target** (task instruction, scope protection): *test whether material here belongs instead to `EXP-005` (doors/searching), `EXP-006` (light), `EXP-007` (traps), `EXP-010` (party formation), `ENC-005` (retreat/pursuit/evasion), the deferred generic Ability Check item `P3`, or wilderness movement.* See §9. **Four reallocations and one probable source gap were found.**

**Random Encounter Principle (`AGENTS.md` §5, task instruction).** Nothing in this packet encodes movement automatically becoming combat. RC's Game Turn Checklist routes a positive wandering-monster result to the **Encounter Checklist**, which begins with detection, surprise and reaction — not with attacks. That routing is recorded in §4 and is owned by landed `EXP-001`/`EXP-002` and by `ENC-002`/`ENC-003`, not by this card.

## 2. Primary-Source Access

*Dungeons & Dragons Rules Cyclopedia* (TSR, 1991; ISBN 1-56076-085-0). Same source, access method and session as `CHAR-004-evidence.md` §2 — OCR transcription at `https://archive.org/stream/TSR1071TheDDRulesCyclopedia/TSR-1071-The-DD-Rules-Cyclopedia_djvu.txt`, with IIIF page images at `https://iiif.archive.org/iiif/TSR1071TheDDRulesCyclopedia$<leaf>/…` for §9.2 visual verification.

Neither access stop was triggered. Limitations in §15. **No alternate source was consulted; AD&D was not consulted.**

## 3. Research Questions

- **A.** What rate do characters use while exploring a dungeon, and against what time unit?
- **B.** What is that rate deemed to already include?
- **C.** What map scale and distance unit govern a dungeon?
- **D.** What is the turn-by-turn exploration procedure?
- **E.** Does RC define a mapping **mechanic** — dice, time cost, failure — or only a technique?
- **F.** Does dungeon terrain modify movement rate or time cost?
- **G.** What within this card's stated title belongs to a different card?

## 4. Evidence Map

| Q | RC Location | What RC Establishes | Provenance | Confidence |
|---|---|---|---|---|
| A | **Ch. 7, "Exploration and the Game Turn", p. 91** | "When characters are exploring a specific area (such as a dungeon)… the DM measures time in turns. Each turn represents 10 minutes; **customarily characters will travel at their normal speed during game turns.**" | RC Explicit | DIRECT PRIMARY TEXT — the card's governing sentence |
| A | Ch. 6, p. 88; Measurements of Game Time Table, p. 87 | Normal speed is expressed **per turn**; 1 turn = 10 minutes; 1 round = 10 seconds; 1 day = 144 turns. The turn machinery itself is landed (`EXP-002`). | RC Explicit | PRIMARY TEXT + landed cross-card confirmation |
| B | **Ch. 6, p. 88** | "Though the normal speed of 120' per turn seems very slow, this rate includes many **assumed actions—mapping, peeking around corners, resting**, and so forth." | RC Explicit | DIRECT PRIMARY TEXT — **decisive for §9 Challenge 2** |
| B | Ch. 6, "Assumed and Defined Actions", p. 87 | RC states the general principle that players need not narrate every action a character takes inside a coarser time unit. | RC Explicit | DIRECT PRIMARY TEXT |
| C | Ch. 6, "Distance" / "Map Scales", p. 87 | Indoors, distances and ranges are **feet**; outdoors the same numbers read as **yards**. "Dungeon maps are usually done on graph paper, **one square representing 10'**." With miniatures, 1″ = 10′ indoors or out. | RC Explicit | DIRECT PRIMARY TEXT |
| C | Ch. 13, "Mapping", p. 148 | A standard corridor is offered as "**10' wide and 10' high**" — as a suggested standing description a DM sets at the start of the adventure, not as a dimension rule. | RC Explicit (as a DM convention) | DIRECT PRIMARY TEXT |
| D | **Game Turn Checklist, RC p. 91** | Four steps: **1. Wandering Monsters** (if the previous turn's check was positive they arrive now, `2d6 × 10` feet away, then leave for the Encounter Checklist); **2. Actions** — "The caller (or each player) describes party actions (**movement, listening, searching, etc.**)"; **3. Results** — (a) discoveries announced, (b) "If the PCs entered a new area, the DM describes it **so that the mapper can map it**", (c) an encounter diverts to the Encounter Checklist; **4. Wandering Monsters Check** — 1d6 every **other** turn, dungeon encounter on a 1. | RC Explicit | DIRECT PRIMARY TEXT — steps 1 and 4 are landed `EXP-001`/`EXP-002` |
| D | Ch. 7, "Leaving the Game Turn", p. 91 | The DM continues in game turns until the situation changes (reaching wilderness, an inn, a patron's caravan), at which point the checklist is dropped. | RC Explicit | DIRECT PRIMARY TEXT |
| E | **Ch. 13, "Mapping", p. 148** | Four numbered **guidelines addressed to the DM**: describe areas clearly and correct mistakes immediately; use consistent terms and a consistent order (RC names *side passage / sideroad*, *four-way intersection*, *T-intersection*); set a standard description at the start ("A standard corridor is 10' wide and 10' high"); use straight corridors and square rooms at first. **No die roll. No time cost. No success or failure state. No player-facing procedure.** | RC Explicit — and explicitly non-mechanical | DIRECT PRIMARY TEXT |
| E | **Ch. 1, "Mapping and Calling"** | "Any player can be the mapper or caller. The mapper is the player who draws a map of the dungeon as it is explored… The map should be kept on the table for all to see… Pencil should be used." And: "**The caller is just a convenience in many campaigns; it's not a game rule that players have to use.**" | RC Explicit | DIRECT PRIMARY TEXT — **decisive for §9 Challenge 4** |
| F | **Ch. 6, Land Travel, p. 88** | "Terrain (the features of the land being explored) affects the rate of travel. **Though it makes no difference to the combat round or the 10-minute turn, the terrain may affect the distance a party travels in a day**, as outlined in the Terrain Effects on Movement Table." | RC Explicit | DIRECT PRIMARY TEXT — **an explicit positive statement of non-application, not an absence** |
| F | **Terrain Effects on Movement Table, p. 88** | **Visually verified.** `Terrain | Movement`: Trail/road\* `1 ½ normal`; Clear/city/grassland `Normal`; Forest/muddy ground/snow `2/3 normal`; Hill/desert/broken terrain `2/3 normal`; Mountain/swamp/jungle `1/2 normal`; Ice/glacier `1/2 normal`. Footnote: unpaved roads ignore every modifier except muddy ground/snow; paved roads ignore every modifier except snow. **Every terrain named is an outdoor terrain type, and the modified quantity is miles per day.** Modifiers are not cumulative — the worst condition governs. | RC Explicit | **VISUALLY VERIFIED** (leaf n87); OCR rendered `1 ½` as `1 F2` |
| F | **Traveling Rates by Terrain Table, p. 88** | **Visually verified.** Column header spans all numeric columns: "**Miles Covered Per Day:**" over `Trail | Clear | Hills | Mountains | Desert`. Rows include `Foot, no enc*` 36/24/16/12/16, keyed by footnote to the **encumbrance bands** (`no enc` = 120′ normal speed, ≤ 400 cn; `lt enc` = 90′; `hvy enc` = 60′). | RC Explicit | **VISUALLY VERIFIED** (leaf n87) |
| F | **Ch. 7, "Evasion and Pursuit", p. 98** | The **only** place the OCR's whole-source text uses the phrase "difficult terrain", and it applies it to a dungeon: evaders may break line of sight "when they reach an area of difficult terrain (for example, thick woods, **a long dungeon corridor riddled with doors and side passages**, etc.)", in which case the DM rolls again on the **Evasion Table**. The effect is on an evasion chance, **not on a movement rate or a time cost**. | RC Explicit | DIRECT PRIMARY TEXT — owned by `ENC-005` |
| F | **Ch. 2, Mystic "Acrobatics", p. 31** | With a successful ability check a mystic "can cross **rough, broken terrain at no modification to his movement rate**… This doesn't affect his long-distance movement rates; **it only affects his encounter speed and running speed.**" | RC Explicit | DIRECT PRIMARY TEXT — **presupposes a rule RC does not state; see §10** |
| G | Ch. 13, "Doors", p. 147 | Opening a stuck door: 1d6, success on 5–6, Strength adjustment applied, once per round per character, a failed attempt forfeits surprise. **Already recorded and assigned to `EXP-005`** in `docs/rules/evidence/CLUSTER-002-completeness-audit.md` §5.4 and in `INVENTORY.md`. Not re-researched here. | RC Explicit | CONFIRMED ALREADY OWNED — `EXP-005` |
| G | Ch. 4, gear descriptions, p. 69 | Torch: 30′ radius, "burns for **one hour (six turns)**". Lantern: 30′ radius, "burning one flask of oil in **four hours (24 turns)**". | RC Explicit | DIRECT PRIMARY TEXT — owned by `EXP-006`; cost/encumbrance owned by `CHAR-004` |
| G | Ch. 2, "Infravision" | Dwarves (and other infravision-bearing races) see 60′ in the dark; infravision does not function in the presence of normal or magical light. | RC Explicit | DIRECT PRIMARY TEXT — owned by `CHAR-009`/`EXP-006` |
| G | Ch. 13, "Climbing", p. 145 | No fixed procedure: the DM decides a base chance; "Dexterity checks (roll Dexterity or less on 1d20) **may allow an easy way** for DMs to check chances"; characters in metal armour "will not be able to climb well"; falling deals 1d6 per 10′. | RC Explicit (that it is DM-set) | DIRECT PRIMARY TEXT — touches deferred item `P3`; **`P3` was not absorbed** |

## 5. Governing Procedure, as RC States It

```text
EXPLORATION, RC Ch. 7 p. 91 + Ch. 6 pp. 87-88

    time unit           the 10-minute TURN            (landed EXP-002)
    rate used           the character's NORMAL SPEED  (CHAR-005)
    distance unit       FEET (indoors)                (Ch. 6 p. 87)
    map scale           graph paper, 1 square = 10'   (Ch. 6 p. 87)

    the normal-speed rate ALREADY INCLUDES mapping, peeking around
    corners, and resting                              (Ch. 6 p. 88)

    per turn, RC's Game Turn Checklist:
        1  arriving wandering monsters -> Encounter Checklist
        2  party declares actions (movement, listening, searching, ...)
        3  DM states results; describes new areas so the mapper can map
        4  wandering-monster check, 1d6 every OTHER turn

    terrain: "makes no difference to the combat round or the 10-minute
             turn"                                    (Ch. 6 p. 88)
```

The executable content `EXP-003` would own is therefore narrower than its title suggests: **spend normal speed against turns at 10 feet per map square, with terrain explicitly excluded at this time scale, and with mapping already priced into the rate.**

## 6. Primary-Source Coverage Checklist (protocol §9.3)

**TOC sections inspected (audit class A):** Ch. 6 Movement p. 87 — Time, Distance, Movement, Land Travel; Ch. 7 Encounters and Evasion p. 91 — Exploration and the Game Turn 91, Travel and the Game Day 91, Encounters 91, Evasion and Pursuit 98; Ch. 13 DM Procedures p. 143 — Climbing 145, **Doors 147**, Equipment Not Listed 147, **Listening 147**, **Mapping 148**, Multiple Characters 148, Record Keeping 148, Special Character Conditions 150; Ch. 1 "Mapping and Calling"; Ch. 17 "Designing Adventures and Dungeons" 259 (boundary only, not inspected).

**Tables Index entries inspected (audit class B):** **Game Turn Checklist 91**; Measurements of Game Time Table 87; Character Movement Rates and Encumbrance Table 88; **Terrain Effects on Movement Table 88**; **Traveling Rates by Terrain Table 88**; Water Movement Modification Table 90; Timetrack Table 149; Starvation Table 150; Evasion Table 98 (boundary); Chance of Encounter Table (boundary, landed `EXP-001`); Movement in the Ethereal Plane Table 264 (boundary). Also checked for, and **not found**: any table named for mapping, corridors, dungeon terrain, dungeon features, or exploration hazards.

> The Tables Index is the completeness instrument for the "Special Terrain" half of this card's title. It lists **two** terrain tables, and both are on p. 88 inside Land Travel. There is no third.

**Named tables inspected directly (audit class C):** Terrain Effects on Movement Table; Traveling Rates by Terrain Table; Game Turn Checklist; Measurements of Game Time Table; Character Movement Rates and Encumbrance Table.

**Stat blocks (audit class D):** the Mystic class table and its Acrobatics prose, because the Acrobatics ability is the only located RC text asserting a dungeon-scale terrain effect on movement.

**Summary boxes / parallel presentations (audit classes E, I):** the mapper's role recorded **twice** — Ch. 1 "Mapping and Calling" (player-procedure) and Ch. 13 p. 148 "Mapping" (DM technique) — and recorded separately rather than merged; the Game Turn Checklist recorded alongside its surrounding prose, which restates steps 1 and 4 in different words.

**Chapter sections read in full (audit class F):** Ch. 7 Exploration and the Game Turn, Game Turn Checklist, Wandering Monsters, Wandering Monsters Check, Leaving the Game Turn, Travel and the Game Day, Encounters (opening); Ch. 6 Time, Distance, Feet vs. Yards, Map Scales, Miniature Figures, Movement, Normal/Encounter/Running Speeds, Land Travel including both terrain tables and their surrounding prose; Ch. 13 Climbing, Mapping; Ch. 1 Mapping and Calling.

**Cross-references followed (audit class G):** Ch. 7 p. 91 → normal speed → Ch. 6 p. 88 → `CHAR-005`; Ch. 7 p. 91 → Encounter Checklist p. 93 → `ENC-002`/`ENC-003` (followed to its boundary only); Ch. 6 p. 88 → Terrain Effects on Movement Table, and the sentence that bounds it; Ch. 13 p. 148 → the standard-corridor convention; Ch. 7 p. 98 → Evasion Table → `ENC-005`.

**Appendices / index entries (audit class H):** Appendix 4 Index to Tables and Checklists p. 301 swept in full. General Index p. 302 **not** swept — §11 item 4.

**Visual-page verification completed (protocol §9.2):**

| Object | Printed page | Leaf | Result |
|---|---|---|---|
| Terrain Effects on Movement Table + footnote | 88 | n87 | Confirmed; six rows, all outdoor terrain; OCR `1 F2` is `1 ½` |
| Traveling Rates by Terrain Table (column header) | 88 | n87 | Confirmed; **every numeric column is "Miles Covered Per Day"** |
| Character Movement Rates and Encumbrance Table | 88 | n87 | Confirmed (shared object with `CHAR-005`) |

**Potentially relevant objects deliberately excluded, with reasons:**

| Object | Reason |
|---|---|
| Encounter Checklist p. 93; Chance of Encounter Table; surprise and reaction procedures | `ENC-002`, `ENC-003`, and landed `EXP-001`. Followed only far enough to record that the Game Turn Checklist routes to them — **and that the route is to detection and reaction, not to automatic combat.** |
| Evasion Table p. 98 and the Evasion and Pursuit procedure | **`ENC-005`.** Its dungeon "difficult terrain" clause was read because it is the whole-source home of that phrase, and then routed, not absorbed. |
| Ch. 13 Doors p. 147, Listening p. 147 | **`EXP-005`**, already recorded in `CLUSTER-002-completeness-audit.md` §5.4. Not re-researched. |
| Torch/lantern duration and radius; infravision | **`EXP-006`** (and `CHAR-009` for infravision). Recorded as located and routed. |
| Traps | **`EXP-007`.** No dungeon-movement or terrain interaction was located in the objects inspected. |
| Ch. 13 Ability Checks p. 143 | **Deferred governance item `P3`.** Reached only because Ch. 13 "Climbing" offers a Dexterity check as a convenience. **Not absorbed, not researched, no Rule ID proposed.** |
| Overland travel rates, getting lost, long-distance rest | Wilderness movement. Inspected only to establish the boundary in §9 Challenge 3, then excluded. |
| Ch. 17 "Designing Adventures and Dungeons" p. 259 | DM campaign-design advice. Located, not inspected — §11 item 3. |

## 7. Questions Belonging to Other Rule Cards' Own Scope

| Question located here | Owner | Basis |
|---|---|---|
| Opening stuck doors | `EXP-005` | Already assigned, `CLUSTER-002-completeness-audit.md` §5.4 |
| Listening at doors | `EXP-005` | `INVENTORY.md` "Listening" row |
| Searching for secret doors and traps | `EXP-005`, `EXP-007`, `CHAR-010` | Named in Game Turn Checklist step 2 as a declarable action; **the resolution procedure is not this card's** |
| Light source radius and duration | `EXP-006` | Ch. 4 p. 69 descriptions |
| Infravision | `CHAR-009` / `EXP-006` | Ch. 2 racial ability |
| Evasion, pursuit, and dungeon "difficult terrain" as an evasion condition | **`ENC-005`** | Ch. 7 p. 98 |
| Wandering-monster checks and their timing | landed `EXP-001` / `EXP-002` | Game Turn Checklist steps 1 and 4 |
| Surprise, encounter distance, reaction | `ENC-002`, `ENC-003` | Encounter Checklist |
| The generic d20 roll-under-ability check | **deferred item `P3`** | Ch. 13 p. 143; **not absorbed** |
| Party formation and marching order | `EXP-010` — **deferred out of `CLUSTER-003`** | See §9 Challenge 4; **no RC prerequisite located** |
| Overland travel, terrain-by-day, becoming lost | wilderness movement responsibility | Ch. 6 Land Travel |
| Movement rate itself, and every modifier to it | `CHAR-005` | `CHAR-005-evidence.md` |

## 8. Whole-Source Cross-Reference Pass (protocol §9)

> Performed after structural mapping and governing-object inspection, per §9.1.1.

**Search terms used:** `Exploration and the Game Turn`; `Game Turn Checklist`; `normal speed`; `game turns`; `mapping`; `mapper`; `caller`; `map scale`; `graph paper`; `one square`; `standard corridor`; `side passage`; `T-intersection`; `terrain` (all occurrences read in context); `difficult terrain`; `rough terrain`; `broken terrain`; `rubble`; `slippery`; `crawl through`; `squeeze`; `marching order`; `single file`; `front rank`; `order of march`; `abreast`; `stair`; `climb`; `swim`; `torch`; `lantern`; `burns for`; `infravision`; `one turn to search`.

**Cross-references discovered:**

1. **Ch. 7 p. 91 → Ch. 6 p. 88** — the exploration turn spends normal speed.
2. **Ch. 6 p. 88 → the Terrain Effects on Movement Table**, together with the sentence that confines it to the day scale.
3. **Ch. 7 p. 91 → the Encounter Checklist p. 93**, which is where a positive wandering-monster result goes.
4. **Ch. 7 p. 91 step 3b → the mapper**, tying the DM's description obligation to a player role defined back in Ch. 1.
5. **Ch. 7 p. 98 → the Evasion Table**, the only RC use of "difficult terrain" applied to a dungeon.
6. **Ch. 2 Mystic Acrobatics → an unstated rough-terrain movement modifier** (§10).

**Negative findings, stated as coverage rather than absence:**

- Across audit classes A, B, C, F and G as inspected, **no dungeon-scale terrain movement modifier — of rate or of turn cost — was located.** This is more than a search miss: the Tables Index lists exactly two terrain tables, both were **visually verified**, both operate on miles per day, and RC states in its own words that terrain "makes no difference to the combat round or the 10-minute turn."
- **No mapping mechanic was located** — no die roll, no time cost, no failure state, no mapping skill. Both mapping passages (Ch. 1 and Ch. 13 p. 148) were read in full, and Ch. 6 p. 88 states that mapping is already inside the normal-speed rate.
- **`marching order` occurs once in the whole OCR text**, in the **NPC party generation** procedure ("6. Decide on the NPC marching order"). `single file`, `front rank`, `order of march` and `abreast` returned nothing. **No PC marching-order procedure was located.**
- Recorded per protocol §9.1 as *not located by the objects inspected* — not as proof that RC contains none. Items 3 and 4 of §11 name what remains uninspected.

## 9. Falsification Pass (protocol §10)

**Challenge 1 — "`EXP-003` has a Special Terrain responsibility."**

*Sought:* any RC rule modifying dungeon movement rate or turn cost for terrain.
*Searched:* the Tables Index for terrain/dungeon-feature tables; both terrain tables **visually verified**; `terrain` read at every occurrence; `difficult|rough|broken terrain`, `rubble`, `slippery`, `crawl through`, `squeeze`; Ch. 13 DM Procedures section list.
*Found:* the two terrain tables are **overland and per-day**, bounded by RC's own sentence; the single dungeon use of "difficult terrain" is an **evasion** condition (`ENC-005`); and the only text implying a dungeon-scale terrain modifier is the **Mystic Acrobatics** ability, which presupposes a rule RC never states.

**Disposition: REJECTED, and escalated to a probable source gap (§10 Gap 1).** The "Special Terrain" third of this card's title has **no located RC dungeon-scale mechanic**. Stated as coverage: the objects that would carry one — the Tables Index, both terrain tables, Ch. 6 Land Travel, Ch. 7 exploration, Ch. 13 DM Procedures — were inspected and are silent.

**Challenge 2 — "mapping costs exploration time."**

*Sought:* a time cost, die roll, or failure state for mapping.
*Searched:* Ch. 13 p. 148 in full; Ch. 1 "Mapping and Calling" in full; Game Turn Checklist step 3b; `mapping`, `mapper`.
*Found:* the opposite, stated explicitly — normal speed "includes many assumed actions—**mapping**, peeking around corners, resting". Ch. 13's mapping entry is four DM-facing description guidelines with no mechanic.

**Disposition: REJECTED.** Charging time for mapping would **double-count** a cost RC has already priced into the rate. Any `EXP-003` Rule Card that adds a mapping time cost would contradict RC p. 88.

**Challenge 3 — "the Terrain Effects on Movement Table might apply in a dungeon."**

*Sought:* whether RC bounds the table or leaves it open.
*Searched:* the table and its footnote **visually verified**; the surrounding Land Travel prose read in full; the Traveling Rates by Terrain Table's column header **visually verified**.
*Found:* every terrain name is outdoor (trail/road, clear/city/grassland, forest/muddy ground/snow, hill/desert/broken terrain, mountain/swamp/jungle, ice/glacier); the companion table's columns are all "Miles Covered Per Day"; and RC bounds it in terms: "**Though it makes no difference to the combat round or the 10-minute turn**, the terrain may affect the distance a party travels in a day."

**Disposition: REJECTED, on an explicit positive statement rather than on an absence.** This is the distinction protocol §9.1 requires and it is available here.

**Challenge 4 — the assigned scope-protection target: "`EXP-003` requires `EXP-010` (Party Formation & Marching Order)."**

*Sought:* any RC rule making dungeon movement depend on formation, order of march, or a party role.
*Searched:* `marching order`, `single file`, `front rank`, `order of march`, `abreast`; Ch. 1 "Mapping and Calling" in full; the Game Turn Checklist; the Tables Index for a formation table.
*Found:* RC's two party roles are **the mapper and the caller**, both defined as player conveniences: "**Any player can be the mapper or caller**", and "**The caller is just a convenience in many campaigns; it's not a game rule that players have to use.**" The only RC occurrence of "marching order" is in **NPC party generation**.

**Disposition: REJECTED. `EXP-010` is not an incoming dependency of `EXP-003` on the evidence located.** The task's boundary-reopen condition is therefore **not** triggered by `EXP-010`. Recorded as coverage: the whole-source phrase searches plus the class-B Tables Index sweep plus the two role-defining passages were inspected; a formation rule living somewhere not reached by those is not excluded, and §11 items 3 and 4 name what was not reached.

**Challenge 5 — "`EXP-003` owns the exploration actions named in Game Turn Checklist step 2."**

*Sought:* whether listening, searching and door-opening resolve here.
*Searched:* Ch. 13 pp. 147–148; the landed `CLUSTER-002` audit's §5.4 record of the Doors procedure; `INVENTORY.md` rows for `EXP-005`, `EXP-007`, `CHAR-010`.
*Found:* RC names those actions in the checklist but resolves them in dedicated Ch. 13 entries already assigned elsewhere.

**Disposition: REJECTED.** `EXP-003` owns the **turn loop and the movement spend**; it does not own the resolution of the actions declared inside it. This is the scope protection the task asked for, and it holds.

**Challenge 6 — "dungeon movement is just Chapter 6 read indoors."**

*Sought:* whether Ch. 7 adds anything Ch. 6 does not.
*Searched:* both sections read in full.
*Found:* Ch. 7 supplies the **turn loop**, the customary-normal-speed statement, the mapper-facing description obligation, and the exit condition; Ch. 6 supplies the **rate, the units, and the map scale**.
**Disposition: QUALIFIED.** The card is genuinely a two-chapter composition, and a pass that read only Chapter 6 would have missed the procedure.

## 10. Source Gaps and Tensions — Recorded, Not Resolved

**Gap 1 — the "Special Terrain" responsibility has no located RC dungeon-scale mechanic.**

```text
RC Ch. 6 p. 88 (visually verified table + bounding sentence)
    terrain affects MILES PER DAY only; explicitly not the round or the turn

RC Ch. 7 p. 98 (Evasion and Pursuit)
    a dungeon corridor "riddled with doors and side passages" is
    "difficult terrain" -- for the EVASION TABLE, owned by ENC-005

RC Ch. 2 p. 31 (Mystic Acrobatics)
    "can cross rough, broken terrain at no modification to his movement
     rate ... it only affects his encounter speed and running speed"
    -> PRESUPPOSES a rough-terrain modifier to encounter and running
       speed that RC states nowhere
```

The Mystic ability is the strongest evidence that RC *intends* a rough-terrain movement modifier to exist, and simultaneously the evidence that RC never publishes one. **This is `RC DOES NOT SPECIFY`, not an internal conflict** — nothing contradicts anything; a referenced rule is simply missing. It is recorded for human review and is **not** resolved, completed, or invented (`AGENTS.md` §3).

**Tension 1 — Ch. 6 p. 88 versus Ch. 2 p. 31 on whether terrain touches the round.** Ch. 6 says terrain "makes no difference to the combat round"; the Mystic Acrobatics text says the ability "only affects his encounter speed and running speed" — both round-scale quantities. Recorded as a tension between a general statement and a class-ability qualifier, `RETAINED AS GENUINE SOURCE AMBIGUITY`.

**Observation 1 — "Mapping" in this card's title names a DM technique, not a mechanic.** Both mapping passages were read in full and neither contains a die, a cost, or a failure state. Recorded as a finding about the source. **Whether the card's title should change is a human governance question and is not decided here.**

## 11. Open-Question Closure Inventory (protocol §10.2)

| # | Open statement | Source region implicated | Inspection completed? | Result | Owner | Still blocks completeness? |
|---|---|---|---|---|---|---|
| 1 | Whether a rough/broken-terrain movement modifier exists somewhere RC does not index | Ch. 2 p. 31 ↔ Ch. 6 p. 88 ↔ Tables Index | **Yes for the indexed objects** | Both terrain tables visually verified and bounded; no third terrain object in the Tables Index | human / Stage B | No — `RETAINED`, §10 Gap 1 |
| 2 | Whether "Mapping" in the card title should survive as a mechanic | RC p. 5 + Ch. 13 p. 148 *(citation corrected in remediation)* | **Yes — all four presentations read in full** | **DECIDED 2026-09-14 (Decision 3): NO.** The card is renamed to **`EXP-003 — Dungeon Movement`**; mapping stays documented as an activity already encompassed by ordinary exploration movement, with no separate mechanic, time cost, roll or failure state. "Special Terrain" is likewise removed from this card's responsibilities | ~~Human governance~~ → **RESOLVED** | **No** — a card-scope decision this researcher may not make |
| 3 | Ch. 17 "Designing Adventures and Dungeons" p. 259 not inspected | RC pp. 259–262 | ~~No~~ → **YES, remediation pass 1** | **CLOSED, and it was not empty.** pp. 256–257 were also read after the General Index flagged them. **Material finding:** the dungeon map scale is explicitly DM-variable (*"or any other scale you prefer"*, p. 260). Room Contents / Unguarded Treasure tables and the "Movement" and "Map Change" room tricks routed to `EXP-007`/`TREAS-*`; the Pre-Game Checklist recorded as a fourth mapper/caller presentation. **No character-scale movement rule.** Remediation §5.2 | `EXP-003` | **No** — closed by inspection |
| 4 | General Index not swept as a completeness locator | RC Appendix 4 p. 302 | ~~No~~ → **YES, remediation pass 1** | **CLOSED.** It corrected the "Mapping and Calling" citation to **p. 5**, flagged Ch. 17 pp. 256–257, and surfaced `Terrain. 119, **153**` → the Ch. 14 Charge rule. It contains **no** `Marching`, `Formation`, or `Carrying capacity` entry. Remediation §5.3 | `EXP-003` | **No** — audit class H discharged |
| 5 | `EXP-005`/`EXP-007` resolution procedures not re-researched | Ch. 13 pp. 147–148 | **No — deliberately** | Already assigned; `EXP-005`'s Doors procedure is recorded in the landed `CLUSTER-002` audit | `EXP-005`, `EXP-007` | No — `CONFIRMED OUT OF SCOPE` with ownership and rationale |
| 6 | `EXP-010` dependency | whole-source phrase sweep + Ch. 1 roles | **Yes for the objects inspected** | No RC prerequisite located; roles are explicitly not game rules | `EXP-010` (deferred) | No — **boundary-reopen condition NOT triggered** |
| 7 | `P3` generic Ability Check | Ch. 13 p. 143 | **No — deliberately not opened** | Reached only as a cross-reference from Climbing | deferred governance item `P3` | No — `CONFIRMED OUT OF SCOPE`; **not absorbed** |

**Items 3 and 4 are unfinished source inspection and are declared as such; item 2 requires a human decision.** Per protocol §10.2 there are **zero silent unresolved research tasks** in this packet, and completeness is therefore not claimed.

## 12. Alternate-Source Research Requirement (protocol §15)

**Not established, and not permitted on the current evidence.** §10 Gap 1 is a genuine candidate — it is a precise, bounded absence rather than an ambiguity — but protocol §9.1 forbids writing the authorising gap statement while the §9.1 audit is incomplete, and §11 items 3 and 4 show it is.

**If** a later pass closes those items and a human authorises gap-directed research, the gap statement must be written at this precision:

```text
CANDIDATE GAP  RC's Mystic Acrobatics ability (Ch. 2 p. 31) states that the
               mystic may cross "rough, broken terrain at no modification to
               his movement rate," affecting "encounter speed and running
               speed." RC's only terrain movement table (Ch. 6 p. 88) is
               explicitly per-day and explicitly "makes no difference to the
               combat round or the 10-minute turn." The modifier the Mystic
               ability negates is therefore never stated.
```

Recorded as a **candidate for a later authorised pass**. No alternate source was opened, and no earlier-edition dungeon-terrain rule was consulted, located, or imported.

## 13. Possible Simulator Ruling Areas (named, not drafted)

- The unstated rough/broken-terrain modifier presupposed by Mystic Acrobatics (§10 Gap 1), **only if** gap-directed alternate-source completion is authorised and fails.

Named only. Not drafted, not bundled, not self-approved. Protocol §16 places Simulator Rulings last.

## 14. Legacy Rule Card Withholding (protocol §13)

**Not applicable.** `EXP-003` is `Unresearched`; no prior Rule Card exists and none was consulted. The card is not `REVALIDATION_REQUIRED`.

## 15. Access Limitations Encountered

As `CHAR-004-evidence.md` §15. One OCR corruption was material here and was corrected visually: the Terrain Effects on Movement Table's trail/road entry reads `1 F2 normal` in OCR and `1 ½ normal` on the page. A pass relying on OCR alone would have recorded a nonsense modifier in the very table this card's scope-protection argument depends on. The General Index was not swept (§11 item 4).

## 16. Confidence Assessment

| Area | Confidence | Basis |
|---|---|---|
| Rate, time unit, distance unit, map scale | **High** | Explicit in two chapters; the turn machinery is already landed and verified (`EXP-002`) |
| The Game Turn Checklist as the exploration procedure | **High** | Single explicit checklist read in full with its surrounding prose |
| That normal speed already includes mapping | **High** | Explicit sentence; no competing text located |
| That terrain does not modify dungeon-scale movement | **High** | An explicit positive statement, plus two visually verified tables that are per-day |
| That mapping has no mechanic | **High** | Both mapping passages read in full |
| That `EXP-010` is not a prerequisite | **Moderate-high** | Explicit "not a game rule" text for the caller; whole-source phrase sweep found no PC marching-order rule; §11 items 3–4 bound the claim |
| That "Special Terrain" has no RC dungeon mechanic | **Moderate-high** | Tables Index is exhaustive for terrain tables and both were verified; the Mystic presupposition is unexplained and is recorded rather than resolved |
| Completeness perimeter | **Moderate** | §11 items 3 and 4 remain |

## 17. Recommendation

Per protocol §11.19:

```text
MORE PRIMARY RESEARCH REQUIRED
```

Bounded and named: §11 items 3 (Ch. 17 pp. 259–262) and 4 (General Index sweep), plus the human card-scope decision in item 2. The card's **core procedure is fully established and its two scope-protection questions are answered on explicit RC text**; what is outstanding is the completeness perimeter and one governance decision.

**Cluster-level status of this packet:**

```text
PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
```
