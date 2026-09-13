# Stage-A Evidence: CHAR-005 — Encumbrance & Movement Rate

> **⚠ REMEDIATION PASS 1 APPLIED (2026-09-13). A governing object was missed; one gap is withdrawn; two contradictions are new.** The independent completeness review returned **`REMEDIATION REQUIRED / FAIL — unfinished structural inspection`** and **`BOUNDARY INTEGRITY: REOPEN REQUIRED`** against this packet as committed at `e26a1e0`. The remediation record is `docs/rules/evidence/CLUSTER-003-remediation-pass-1.md`; **read it alongside this packet.** The original text below is preserved unaltered as audit history.
>
> **Governance correction accepted.** §9 Challenge 1 of this packet concluded that the Mystic `MV` finding was *"not a boundary-reopen condition… `CHAR-009` is not among the three deliberately deferred items."* **That reading was wrong.** The approved boundary rule fires on a mechanically indispensable dependency on **any** unlanded Rule Card outside `CLUSTER-003`, and the original assignment named *"`CHAR-005` genuinely requiring an unlanded class/race movement rule"* as its worked example. **The `CLUSTER-003` boundary is reopened and provisional. `CHAR-009` was NOT added.**
>
> **What changed as a result:**
>
> - **A GOVERNING OBJECT WAS MISSED: RC Ch. 8 p. 103, "Movement"** (visually verified, leaf n102). RC flags it itself as *"additional details"* to Chapter 6. It adds a hard scale boundary — *"A character's normal speed is **never used during the combat sequence**"* — plus movement-budget rules, and it contains a **factor-of-3 inconsistency** with Ch. 6 on running speed. **It was reached only through the General Index**, because the section is headed simply "Movement" inside the combat sequence. This is the clearest single justification for the reviewer's `FAIL`. Remediation §5.5.
> - **§9 Challenge 1 is CONFIRMED, now on structural evidence rather than search.** All nine class experience tables were opened as page images; all nine boxed blocks were opened as page images; all nine Class Details were read in full; and RC's own "Understanding the Tables" (p. 13) enumerates the experience-table column set — `Level`, `XP`, `Attack Rank`, `Spells/Level` — with **no movement column**. **The Mystic is the only class with a movement exception.** Remediation §2.
> - **§10 Gap 1 (racial-armour movement reduction) is WITHDRAWN as a gap.** The complete sentence reads *"**The DM can impose penalties** on a character who wears the armor of a different race"*, and the movement reduction is offered as an **example of an optional penalty**. RC delegates this by design. This packet quoted the parenthetical without its governing sentence. Remediation §6 item 7.
> - **§10 Gap 2 (Mystic `MV` × encumbrance) survives, and is now defensible** as `RETAINED AS GENUINE SOURCE AMBIGUITY` under protocol §10.2.2 case 3 — both objects inspected in full, Ch. 8, Ch. 14, Ch. 19 and the General Index all checked for a reconciling statement. One sub-item is **closed**: the "above 16th level" question is moot, because the visually verified Mystic box gives `Maximum Level: 16`. Remediation §3.
> - **NEW CONTRADICTION — running speed stated twice with a factor-of-3 discrepancy.** Ch. 6 p. 88: running *"is equal to their normal speed in feet per round… or three times their encounter speed"*. Ch. 8 p. 103: *"his full running speed movement (**3 × normal movement**)"*. Both visually verified. Remediation §6 Defect 10.
> - **NEW MINOR TENSION — standing up:** "one round of movement" (Ch. 13 p. 150) vs. "an action in a combat round" (Ch. 8 p. 103).
> - **§10 Conflicts 1 and 2 (Suit Armor, Starvation Table) survive re-testing unchanged.**
>
> **This is a Stage-A evidence artifact, not a Rule Card.** Produced under `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` (`DEC-0009`) and the primary-source completeness requirements adopted by `DEC-0010`. It is not mechanically authoritative, is not `APPROVED`, and authorizes nothing. **Stage B was not begun.**
>
> **Completeness status: `PREPARED FOR INDEPENDENT COMPLETENESS REVIEW` (protocol §10.1.1).** The independent completeness review required by §10.1.2 / `DEC-0010` item 14 has **not** been performed and may not be performed by this researcher.
>
> **Research-risk classification: HIGH** (protocol §9.4 — *encumbrance/movement* is a named high-risk responsibility; a mechanically significant table drives the entire procedure; **Guardrail D trigger 1 fires** — a per-class table for the researched subject exists, namely the Mystic `MV` column, see §9 Challenge 1).

## 1. Research Scope

**Investigating:** what the Rules Cyclopedia establishes about how much a character can carry, how carried weight translates into a rate of movement, what the resulting rates mean in the game's time units, and what else in RC modifies a character's movement rate.

**Cluster context:** `CLUSTER-003` — Equipped Dungeon Movement. `CHAR-005` consumes `CHAR-004`'s `Enc (cn)` values and produces the rate that `EXP-003` spends against the landed `EXP-002` dungeon turn.

**Assigned falsification target** (task instruction): *test the assumption `CHAR-005 → CHAR-004` without requiring another unlanded character card (Mystic / class / race movement rules).* See §9, Challenge 1. **The assumption was DISPROVED.**

**Excluded:** overland travel rates, water and aerial travel, monster and mount movement, and the dungeon-turn accounting that consumes the rate — each recorded with its owner in §6 and §7.

## 2. Primary-Source Access

*Dungeons & Dragons Rules Cyclopedia* (TSR, 1991; ISBN 1-56076-085-0). Same source, access method and session as `CHAR-004-evidence.md` §2 — OCR transcription at `https://archive.org/stream/TSR1071TheDDRulesCyclopedia/TSR-1071-The-DD-Rules-Cyclopedia_djvu.txt` for navigation and prose, IIIF page images at `https://iiif.archive.org/iiif/TSR1071TheDDRulesCyclopedia$<leaf>/…` for §9.2 visual verification (`leaf = printed_page − 1`).

Neither `STOP — PRIMARY SOURCE ACCESS REQUIRED` nor `STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED` was triggered. Limitations in §15.

**Alternate sources were not consulted.** AD&D was not consulted (`AGENTS.md` §4).

## 3. Research Questions

- **A.** What is the unit of encumbrance, and what is its relationship to real weight?
- **B.** What is the governing encumbrance → movement-rate procedure?
- **C.** What movement rates does RC define, and what time unit does each use?
- **D.** What is a character's rate when carrying nothing significant, and is that value universal?
- **E.** How does a group of characters move?
- **F.** What are the limits on the fastest rate, and what happens at those limits?
- **G.** **What else, anywhere in RC, modifies a character's movement rate?**

## 4. Evidence Map

| Q | RC Location | What RC Establishes | Provenance | Confidence |
|---|---|---|---|---|
| A | Ch. 6, "Character Movement Rates", p. 88 | "The weight and clumsiness of gear is called encumbrance and is measured in 'cn,' which are coin-weight equivalents; **1 coin equals approximately 1/10 of a pound in weight and awkwardness.**" Encumbrance is explicitly **not** pure mass. | RC Explicit | DIRECT PRIMARY TEXT |
| A | Ch. 4, Weapons Table legend, p. 63 | Duplicate presentation: "Enc (cn) shows how much encumbrance the weapon has, measured in coin-weights (cn). **One coin weighs one-tenth of a pound.** Remember that the more encumbrance a character is carrying, the slower he moves." Omits *awkwardness*. | RC Explicit (audit class I) | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED |
| B/C | **Character Movement Rates and Encumbrance Table, p. 88** | The governing object. Columns, **visually verified**: `Enc (cn) | Normal Speed (feet per turn) | Encounter Speed (feet per round) | Running Speed (feet per round)`. Rows: `0–400 → 120 / 40 / 120`; `401–800 → 90 / 30 / 90`; `801–1,200 → 60 / 20 / 60`; `1,201–1,600 → 30 / 10 / 30`; `1,601–2,400 → 15 / 5 / 15`; `2,401+ → 0 / 0 / 0`. **No lost column, no hidden footnote, no row beyond `2,401+`.** | RC Explicit | **VISUALLY VERIFIED** (leaf n87) |
| C | Ch. 6, "Normal, Encounter, and Running Speeds", p. 88 | Normal speed is per **turn**; encounter speed is **1/3** of normal, per **round**; running speed equals the normal *number* in feet per **round**, i.e. **3×** encounter speed. The parenthesised second number in `120' (40')` **is** the encounter speed. | RC Explicit | DIRECT PRIMARY TEXT |
| C | Ch. 6, p. 88 | "Though the normal speed of 120' per turn seems very slow, this rate includes many **assumed actions—mapping, peeking around corners, resting**, and so forth." The rate is not raw walking pace. | RC Explicit | DIRECT PRIMARY TEXT — **load-bearing for `EXP-003`** |
| C | Ch. 6, "Feet vs. Yards" / "Distance", p. 87 | Indoors the unit is the **foot**; outdoors the same number is read as **yards** (×3). Spell *effects* are always feet. So `90'` normal speed is 90 feet/turn in a dungeon and 90 yards/turn outdoors. | RC Explicit | DIRECT PRIMARY TEXT |
| D | Ch. 6, p. 88 | "**Any character will have a movement rate of '120' (40')' unless he is weighed down by a lot of gear.**" Stated as a universal. | RC Explicit | DIRECT PRIMARY TEXT — **falsified as a universal by the Mystic table, §9 Challenge 1** |
| D | Ch. 6, p. 88 worked example | "A character carrying 60 lbs. (600 cn) of armor and equipment will be slowed to a MV of 90' (30')." Consistent with the table's `401–800` band and with the 1 cn = 1/10 lb conversion. | RC Explicit | DIRECT PRIMARY TEXT; arithmetic self-consistent |
| E | Ch. 6, "Important Note", p. 88 | "**Groups of characters, if they intend to stay together, move at the rate of the slowest character.**" | RC Explicit | DIRECT PRIMARY TEXT |
| F | Ch. 6, p. 88 | Running may be sustained **30 rounds at most (5 minutes)** before exhaustion. "(Characters with the optional **Endurance** skill can maintain this pace for longer periods of time.)" | RC Explicit | DIRECT PRIMARY TEXT; Endurance → `CHAR-012` |
| F | Ch. 6, "Exhaustion", p. 88 | An exhausted character must rest **at least three turns (30 minutes)** before running or fighting again. Forced to fight without rest: monsters gain **+2** to hit him and he subtracts **2** from all damage rolls (a hit still inflicts at least 1 point). Forced to keep running: he **drops to encounter speed** and cannot go faster until rested. | RC Explicit | DIRECT PRIMARY TEXT |
| G | **Ch. 2, Mystic Special Abilities Table, p. 31** | An `MV` column giving a **class- and level-dependent base movement rate**, **visually verified**: L1 120′, L2 130′, L3 140′, L4 150′, L5 160′, L6 170′, L7 180′, L8 190′, L9 200′, L10 210′, L11 220′, L12 240′, L13 260′, L14 280′, L15 300′, L16 320′. Its legend: "MV: This column shows the mystic's movement rate. **First level mystics move as fast as any other unarmored characters, but higher level mystics learn to move very, very fast indeed.**" Above 16th level the mystic's movement rate "no longer improve[s]". | RC Explicit | **VISUALLY VERIFIED** (leaf n30) — **decisive for §9 Challenge 1** |
| G | Ch. 4, Suit Armor description, p. 68 | "**The wearer's movement rate is 30' (10')**" — a flat statement attached to an item whose **visually verified** encumbrance is 750 cn, which the p. 88 table places at 90′ (30′). See §10 Conflict 1. | RC Explicit | **VISUALLY VERIFIED on both sides** |
| G | Ch. 4, Armor prose, p. 67 | Armour is made for a specific race; wearing another race's armour causes "**an additional reduction to movement beyond what the armor's encumbrance calls for**" (example: an elf in a dwarf's chain mail), and a halfling in human-sized armour must additionally save vs. paralysis each round. **The reduction is never quantified.** | RC Explicit (that a reduction exists); **RC does not specify** (its size) | DIRECT PRIMARY TEXT |
| G | **Ch. 13, "Special Character Conditions — Blindness", p. 150** | A blind character travelling far "must move at **one-third his normal speed** . . . and, whether he is indoors or outdoors, **that speed is measured in feet, not yards**." Guided by a sighted character: "**two-thirds his normal rate**", measured in yards outdoors. Mounted, with someone else guiding the horse: **no movement penalty**. | RC Explicit | DIRECT PRIMARY TEXT — a movement rule **outside Chapter 6** |
| G | **Ch. 13, "Special Character Conditions — Stunning", p. 150** | Penalty 2 of 7: "He moves at **one-third the normal movement rate for whatever speed he is attempting.**" | RC Explicit | DIRECT PRIMARY TEXT — a movement rule **outside Chapter 6** |
| G | **Starvation Table, p. 150** | A `Movement Rates` column keyed to percentage of hit points lost to starvation, **visually verified**: `0%–24% → No Penalty`; `25%–49% → × 3/4`; `50%–74% → × 1/2`; `75%–99% → × 3/4`. The 75–99% row is **non-monotonic as printed** — see §10 Conflict 2. | RC Explicit | **VISUALLY VERIFIED** (leaf n149) |
| G | Ch. 13, "Prone Characters", p. 150 | "A character on the ground takes **one round of movement to stand up**." A movement-budget cost rather than a rate modifier. | RC Explicit | DIRECT PRIMARY TEXT |
| G | Ch. 2, Mystic "Acrobatics", p. 31 | With a successful ability check a mystic "can cross **rough, broken terrain at no modification to his movement rate**… This doesn't affect his long-distance movement rates; **it only affects his encounter speed and running speed.**" | RC Explicit | DIRECT PRIMARY TEXT — **presupposes a terrain modifier RC does not state; see `EXP-003-evidence.md` §10** |
| G | Ch. 6, "Water Travel — By Swimming (and Drowning)", p. 89 | A swimming character's movement rate is **1/5 his outdoor running speed** (120 yards/round ÷ 5 = 24 yards/round); underwater the rate is always measured **in feet**. Separately: carrying **more than 400 cn**, "sheer weight will drag him down." | RC Explicit | DIRECT PRIMARY TEXT — an **encumbrance threshold outside the p. 88 table** |
| G | Ch. 13, "Climbing", p. 145 | "Generally, any characters in **metal armor will not be able to climb well**. Characters in leather or no armor should be able to climb easily." The DM sets a base chance; Dexterity checks are offered as a convenience. **No movement rate, no fixed procedure.** | RC Explicit (that armour matters); **RC does not specify** (any number) | DIRECT PRIMARY TEXT |
| G (boundary) | Ch. 6, "Monster Movement Rates", p. 88 | Monster and animal encumbrance is tallied only when carrying heavy prey or riders; the guidelines are in **Chapter 14** and "are somewhat simpler than those for player character encumbrance" — full rate to a threshold, half rate to twice that, then immobile. **A structurally different, two-band system.** | RC Explicit | DIRECT PRIMARY TEXT |
| G (boundary) | Ch. 4, Barding Encumbrance Table, p. 68; Vehicle Movement Speeds, p. 70 | Mounts use the same **two-band** structure (`Full Movement (cn)` / `Half Movement (cn)`), **visually verified**; vehicles inherit it (load ≤ animal's normal encumbrance → normal speed; above → half speed). | RC Explicit | **VISUALLY VERIFIED** (leaf n67) |

## 5. Governing Procedure, as RC States It

```text
CHAR-004 supplies:      an Enc (cn) value per carried item
                        (fixed, or derived -- nets, whips, containers,
                         worn-vs-packed clothing: see CHAR-004 SS9 Challenge 4)

CHAR-005 then:          total the carried cn
                        look the total up in the Character Movement Rates
                          and Encumbrance Table (RC p. 88)
                        read three rates off one row:
                            normal    speed  feet per TURN
                            encounter speed  feet per ROUND   (= normal / 3)
                            running   speed  feet per ROUND   (= normal, as a
                                                                number)

                        indoors  -> read as feet
                        outdoors -> read the same numbers as yards

                        a group staying together moves at the rate of its
                          slowest member
```

**What the table does not contain, and RC supplies elsewhere:** a class-based base rate (Mystic, Ch. 2 p. 31), an item-level flat override (Suit Armor, Ch. 4 p. 68), an unquantified racial-armour reduction (Ch. 4 p. 67), three condition multipliers (blindness, stunning, starvation — all Ch. 13 p. 150), a swimming derivation and a separate 400 cn drowning threshold (Ch. 6 p. 89), and a standing-up cost (Ch. 13 p. 150).

**This is the central Stage-A finding of the card: the p. 88 table is the principal governing object, and it is demonstrably not the only one.** Protocol §9.8 forbids calling it a "single governing object", and this packet does not.

## 6. Primary-Source Coverage Checklist (protocol §9.3)

**TOC sections inspected (audit class A):** Ch. 6 Movement p. 87 — Time 87, Distance 87, Movement 87, Land Travel 88, Water Travel 89, Aerial Travel 90; Ch. 4 Armor 67, Adventuring Gear 68, Land Transportation 70; Ch. 2 class entries (targeted at movement statements); Ch. 7 "Exploration and the Game Turn" 91; Ch. 13 Climbing 145, Special Character Conditions 150; Ch. 14 "How to Read Monster Descriptions" 152 (boundary only); Ch. 18 "Effects on Magic" / Ethereal Plane 263–264 (boundary only).

**Tables Index entries inspected (audit class B) — every entry whose title or subject could bear on encumbrance or movement:** **Character Movement Rates and Encumbrance Table 88**; Terrain Effects on Movement Table 88; Traveling Rates by Terrain Table 88; Water Movement Modification Table 90; Measurements of Game Time Table 87; Barding Encumbrance Table 68; Barding Table 68; Adventuring Gear Table 69; Armor Table 67; Weapons Table 62; Ammunition Table 63; Land Transportation Gear Table 70; Riding Animal Costs Table 70; Sailing Vessels Table 71; **Starvation Table 150**; Timetrack Table 149; **Movement in the Ethereal Plane Table 264**; **Mystic Special Abilities Table 31**; Mystic Saving Throws Table 30; Mystic Experience Table 29; Mystic Unarmed Attack Equivalents Table 30.

> The Tables Index is what surfaced the **Mystic Special Abilities Table** and the **Movement in the Ethereal Plane Table**. Neither would have been reached by searching Chapter 6. This is the class-B instrument working as `DEC-0010` intends.

**Named tables inspected directly (audit class C):** Character Movement Rates and Encumbrance Table; Mystic Special Abilities Table; Starvation Table; Barding Encumbrance Table; Terrain Effects on Movement Table; Traveling Rates by Terrain Table; Measurements of Game Time Table.

**Stat blocks (audit class D):** the Mystic class table was inspected as a structured object **separately from its prose**, and the prose legend was then read — which is how the "first level mystics move as fast as any other unarmored characters" qualification was captured. Other class entries were **not** read as complete entries for a movement statement (§11 item 1).

**Summary boxes / duplicate presentations (audit classes E, I):** the coin-weight statement recorded in **both** Ch. 4 p. 63 and Ch. 6 p. 88, with the wording difference (*awkwardness*) preserved; the `120' (40')` notation explained in both Ch. 6 p. 88 and the Ch. 2 class-table legend; character encumbrance (six bands) and animal/vehicle encumbrance (two bands) recorded as **separate systems**, not as one.

**Chapter sections read in full (audit class F):** Ch. 6 Time, Distance, Feet vs. Yards, Map Scales, Movement, Normal/Encounter/Running Speeds, Exhaustion, Character Movement Rates, Monster Movement Rates, Land Travel (Overland Movement Rates, terrain, Long-Distance Travel and Rest, Becoming Lost), Water Travel (By Swimming and Drowning); Ch. 4 Armor including the complete Suit Armor entry, Barding and Barding-and-Encumbrance, Vehicle Movement Speeds; Ch. 13 Climbing, Special Character Conditions (Blindness, Deafness, Paralysis, Prone, Sleep/Unconsciousness, Starvation and Dehydration, Stunning, Invisibility); Ch. 2 Mystic special-abilities text.

**Cross-references followed (audit class G):** Ch. 4 p. 63 → Ch. 6 p. 88 (encumbrance slows movement); Ch. 6 p. 88 → Ch. 14 (monster encumbrance guidelines); Ch. 6 p. 88 → Endurance general skill → Ch. 5 / `CHAR-012`; Ch. 6 p. 87 → Measurements of Game Time Table (landed `EXP-002`); Ch. 4 p. 68 → Ch. 14 Load/Barding Multiplier; Ch. 2 Mystic Acrobatics → Ch. 5 Acrobatics general skill.

**Appendices / index entries (audit class H):** Appendix 4 "Index to Tables and Checklists" p. 301 swept in full as the class-B instrument. General Index p. 302 **not** swept — §11 item 4.

**Visual-page verification completed (protocol §9.2):**

| Object | Printed page | Leaf | Result |
|---|---|---|---|
| Character Movement Rates and Encumbrance Table | 88 | n87 | Confirmed; four columns, six rows, no footnote |
| Mystic Special Abilities Table (`MV` column) | 31 | n30 | Confirmed; 16 rows, 120′ → 320′ |
| Starvation Table (`Movement Rates` column) | 150 | n149 | Confirmed; **`× 3/4` at 75–99% is genuinely printed** |
| Barding Encumbrance Table | 68 | n67 | Confirmed; two-band animal structure |
| Terrain Effects on Movement Table | 88 | n87 | Confirmed; **OCR `1 F2 normal` is really `1 ½ normal`** |
| Armor Table (Suit Armor `Enc 750`) | 67 | n66 | Confirmed |

**Potentially relevant objects deliberately excluded, with reasons:**

| Object | Reason |
|---|---|
| Terrain Effects on Movement Table 88, Traveling Rates by Terrain Table 88 | **Inspected and visually verified, then excluded on RC's own statement** that terrain "makes no difference to the combat round or the 10-minute turn". Full treatment in `EXP-003-evidence.md`. |
| Water Movement Modification Table 90; Sailing Vessels Table 71 | Water travel; not dungeon movement. Located, not inspected. |
| Aerial Travel p. 90 | Not reached by this cluster. Located, not inspected. |
| Movement in the Ethereal Plane Table 264 | Ch. 18 Planes of Existence. Located via the Tables Index and **recorded rather than silently dropped**; no V1 dungeon-movement reachability. |
| Ch. 14 per-monster `Load` paragraphs and movement rates | `MON-*`. RC states the *location* of the rule; the entries themselves are out of scope. |
| Spell-borne movement effects (e.g. *transmute rock to mud* — "slowed to 10% of their normal movement rate"; *haste*) | `MAGIC-*`. Located during the whole-source sweep and recorded so a later reviewer knows they were seen and routed, not missed. |
| Weapon Mastery / General Skills tables | `CHAR-011`, `CHAR-012`. Endurance is reached only as a named cross-reference. |

## 7. Questions Belonging to Other Rule Cards' Own Scope

- Spending a movement rate against the 10-minute dungeon turn → `EXP-003`, consuming landed `EXP-002`.
- The Endurance general skill's extension of the 30-round running limit → `CHAR-012`.
- Saving throw vs. paralysis for a halfling in human-sized armour → `COMBAT-004`.
- Suit Armor's surprise effects (heard at 120′, negates surprise, −1 to be surprised) → `ENC-002`.
- Exhaustion's combat penalties (+2 monster attack, −2 damage) → `COMBAT-002`/`COMBAT-003`; the *rate* consequence is this card's.
- Blindness, stunning, paralysis and prone as **conditions** → a status-condition responsibility not yet identified in `INVENTORY.md`; their **movement-rate components** are this card's (§11 item 5).
- Starvation and dehydration as a survival system → an `ADV-*` responsibility; the Starvation Table's movement column is this card's.
- Swimming, drowning and the 400 cn threshold → water-travel responsibility; the **derivation from running speed** is this card's.
- Monster, mount and vehicle carrying capacity → `MON-*` and the unassigned transport responsibility raised in `CHAR-004-evidence.md` §11 item 5.
- Climbing adjudication → `CHAR-010` (thief Climb Sheer Surfaces) and the deferred generic Ability Check item `P3`. **`P3` was not absorbed.**

## 8. Whole-Source Cross-Reference Pass (protocol §9)

> Performed after structural mapping and governing-object inspection, per §9.1.1.

**Search terms used:** `encumbrance` (93 occurrences reviewed in context); `cn`; `coin weighs`; `one-tenth of a pound`; `movement rate` (all occurrences scanned by context, including every non-character hit); `Movement Rates`; `normal speed`; `encounter speed`; `running speed`; `exhausted`; `Endurance`; `slowest character`; `120' (40')`; `MV`; `unarmored`; `swim`; `drag him down`; `stair`; `climb`; `one-third his normal speed`; `two-thirds`; `Starvation Table`; `Must Rest`; `optional rule`; `ignore encumbrance`; `keep track of encumbrance`.

**Cross-references discovered:**

1. **Ch. 4 → Ch. 6**, explicitly: encumbrance slows movement.
2. **Ch. 6 → Ch. 14**, for monster/animal encumbrance, with RC itself noting the two systems differ.
3. **Ch. 6 → Ch. 5 Endurance skill**, as the only stated extension of the running limit.
4. **Ch. 2 Mystic → Ch. 5 Acrobatics**, and Mystic Acrobatics → an unstated rough-terrain movement modifier (`EXP-003-evidence.md` §10).
5. **Ch. 4 Suit Armor → its own movement statement**, bypassing the Ch. 6 table.
6. **Ch. 13 p. 150 → normal speed**, three times (blindness ×2, stunning), without any back-reference from Chapter 6.

**Negative findings, stated as coverage rather than absence:**

- Across audit classes A, B, C, F and G as inspected, **no optional or simplified encumbrance variant** (an armour-class-based or "if you don't want to track coins" alternative) **was located**. The `optional rule` sweep returned two-weapon combat, polearm individualisation, and optional languages — not encumbrance. Recorded as *not located by the objects inspected*.
- **No second character encumbrance table** was located; the p. 88 table appears once. Recorded the same way.
- **No statement was located** reconciling the Mystic `MV` progression with the p. 88 encumbrance bands — that is, RC does not say whether a 10th-level mystic carrying 900 cn moves at 210′, at 60′, or at some combination. **This is a genuine gap, not a search miss**: the two governing objects were both inspected, and neither addresses the other. See §11 item 2.

## 9. Falsification Pass (protocol §10)

**Challenge 1 — the assigned target: "`CHAR-005` depends only on `CHAR-004` and needs no other unlanded character card."**

*Sought:* any class- or race-specific movement rule that the encumbrance table does not produce.
*Searched:* the **Tables Index** first (not Chapter 6), for every table whose subject could bear on movement; then `movement rate` across the whole source with every hit read in context; then the Ch. 2 Mystic entry as a structured object plus its prose legend.
*Found:* the **Mystic Special Abilities Table** (RC p. 31) carries an `MV` column rising from 120′ at 1st level to 320′ at 16th, with the legend stating that first-level mystics move as fast as any other *unarmored* character "but higher level mystics learn to move very, very fast indeed," and the Higher Experience Levels text confirming that above 16th level "the mystic's armor class, **movement rate**, number of attacks, and hand-to-hand damage no longer improve."

**Disposition: REJECTED. The assumption is disproved.**

```text
RC p. 88   "Any character will have a movement rate of '120' (40')'
            unless he is weighed down by a lot of gear."

RC p. 31    Mystic MV: 120' at L1 ... 320' at L16, by class and level.

The p. 88 universal is false for one of the nine V1 classes, and that
class is REQUIRED V1 content under DEC-0008.
```

**Consequences, stated as findings rather than decisions:**

- `CHAR-005` has an **incoming dependency on an unlanded class-abilities responsibility** — on the evidence, `CHAR-009` (whose `INVENTORY.md` row already scopes "Mystic's class abilities"), not `CHAR-004`.
- `INVENTORY.md`'s `CHAR-005` dependency cell (`CHAR-004`) is, on this evidence, **incomplete**.
- This is **not** a boundary-reopen condition as the task defined it: `CHAR-009` is not one of the three deliberately deferred items (`CHAR-006`, `CHAR-008`, `EXP-010`). It is nonetheless a genuine unlanded incoming dependency and is raised for human governance, **not resolved**.
- The interaction between the Mystic `MV` value and the encumbrance bands is **unstated by RC** (§8, third negative finding; §11 item 2).

**Challenge 2 — "the p. 88 table is the governing object for movement rate."**

*Sought:* movement-rate rules elsewhere in RC.
*Searched:* Tables Index in full; `movement rate` whole-source with out-of-domain hits read rather than discarded (protocol §9.4 Guardrail D trigger 2).
*Found:* six further character-applicable movement provisions — Mystic `MV`, Suit Armor's flat 30′ (10′), the unquantified racial-armour reduction, blindness (⅓ unguided / ⅔ guided), stunning (⅓), starvation (×¾ / ×½ / ×¾), plus the swimming derivation and the prone standing cost.
**Disposition: QUALIFIED.** The table is **principal, not sole**. Protocol §9.8's prohibition on "single governing object" claims applies directly and is honoured.

**Challenge 3 — "encumbrance is a straightforward weight total."**

*Sought:* whether RC treats cn as mass.
*Searched:* both coin-weight statements; container footnotes; the worn-clothing footnote.
*Found:* Ch. 6 defines cn as "weight **and awkwardness**", and `CHAR-004`'s footnote `**` discards a packed garment's encumbrance entirely once it is **worn** — a rule no mass model produces.
**Disposition: REJECTED as stated.** Encumbrance is a bulk-and-awkwardness abstraction with at least one state-dependent term.

**Challenge 4 — "an unencumbered character always moves 120′ (40′)."**

*Sought:* counter-examples within the character encumbrance system itself.
*Searched:* the p. 88 table's own bands; Suit Armor; the racial-armour prose.
*Found:* Suit Armor at a **visually verified 750 cn** states 30′ (10′) while the table's `401–800` band gives 90′ (30′); and RC elsewhere imposes a movement reduction it never quantifies.
**Disposition: REJECTED**, and escalated to §10 Conflict 1.

**Challenge 5 — "RC offers a simplified encumbrance option, as earlier D&D editions do."**

*Sought:* an optional armour-based or no-tracking encumbrance rule.
*Searched:* `optional rule`, `ignore encumbrance`, `keep track of encumbrance`, `encumbrance is optional`; Ch. 19 Variant Rules section headings; the Tables Index.
*Found:* nothing in the objects inspected.
**Disposition: NOT LOCATED** — recorded per protocol §9.1 as *not located by the objects inspected*, explicitly **not** as a finding that RC contains no such option. Ch. 19 Variant Rules was reached only through its three TOC sub-headings (Ability Scores and Saving Throws; Demihuman and Mystic Experience Levels; Nonlethal Combat), none of which names encumbrance; the section body was not read in full (§11 item 3).

## 10. Internal Source Conflicts — Recorded, Not Resolved

> Protocol §10.2.2 case 3: all relevant governing objects inspected, contradictory passages accurately recorded, nothing obviously governing left uninspected. `RETAINED AS GENUINE SOURCE AMBIGUITY`. **Neither is resolved, and neither side is silently preferred.**

**Conflict 1 — Suit Armor movement rate. VISUALLY VERIFIED ON BOTH SIDES.**

```text
Armor Table, RC p. 67 (leaf n66)        Suit Armor ... Enc 750 cn
Character Movement Rates and
  Encumbrance Table, RC p. 88 (n87)     401-800 cn -> 90' (30')
Suit Armor description, RC p. 68        "The wearer's movement rate is 30' (10')."
                                        -> the 1,201-1,600 cn band
```

Two readings are available and **neither is adopted here**: (i) the item description is a **flat override** of the table for this one item, or (ii) the two statements genuinely contradict. RC provides no override language ("regardless of encumbrance", "instead of") that would settle it, and no cross-reference in either direction. Note that the suit-armour wearer is also carrying other gear, which cannot *reduce* the rate to 30′ by any reading of the table that starts at 750 cn and stays under 1,201.

**Conflict 2 — Starvation Table movement column is non-monotonic as printed. VISUALLY VERIFIED.**

```text
Percentage of hp       Must Rest     Movement
Lost to Starvation     (per day)     Rates
  0%- 24%              6 hours       No Penalty
 25%- 49%              8 hours       x 3/4
 50%- 74%             10 hours       x 1/2
 75%- 99%             12 hours       x 3/4     <-- less severe than the band above
```

Every other column worsens monotonically (rest hours 6 → 8 → 10 → 12; attack penalty none → −2 → −4 → −6). The movement column does not. The page image was read directly to exclude an OCR artifact: **the printed table really says `× 3/4`.** Recorded as a printed-source defect; not corrected, not reinterpreted.

**Conflict 3 — the p. 88 universal versus the Mystic `MV` table.** Recorded in §9 Challenge 1. RC states "any character" moves 120′ (40′) unencumbered, and separately tabulates a mystic moving up to 320′. The two objects never reference each other.

**Gap 1 — the racial-armour movement reduction is unquantified.** RC asserts "an additional reduction to movement beyond what the armor's encumbrance calls for" and gives no number, no fraction, and no procedure. This is `RC DOES NOT SPECIFY`, not a conflict.

**Gap 2 — Mystic `MV` × encumbrance interaction is unstated.** See §8 and §11 item 2.

## 11. Open-Question Closure Inventory (protocol §10.2)

| # | Open statement | Source region implicated | Inspection completed? | Result | Owner | Still blocks completeness? |
|---|---|---|---|---|---|---|
| 1 | The other eight class entries were not read as complete entries for a movement statement | RC Ch. 2 pp. 13–29 | ~~No~~ → **YES, remediation pass 1** | **CLOSED.** All nine entries read as complete entries; all nine experience tables and all nine boxed blocks opened as page images; RC's own "Understanding the Tables" enumerates the column set and lists no movement column. **All eight non-Mystic classes are silent on movement.** Remediation §2 | `CHAR-009` / `CHAR-005` | **No** — closed by inspection |
| 2 | How the Mystic `MV` value interacts with the encumbrance bands | RC p. 31 + RC p. 88 | **Yes — both objects inspected** | RC does not address it | `CHAR-005` (Stage B) or human | No — `RETAINED AS GENUINE SOURCE AMBIGUITY` |
| 3 | Ch. 19 Variant Rules body not read in full | RC pp. 266–267 | ~~No~~ → **YES, remediation pass 1** | **CLOSED.** Chapter 19 is exactly two printed pages; both read in OCR in full and both visually verified as whole pages. Its five sections are Ability Scores and Saving Throws, Death in the Campaign, Keeping Characters Alive, Demihuman and Mystic Experience Levels, Nonlethal Combat — **the TOC's three sub-headings were indeed incomplete, so the caveat was justified.** **No encumbrance or movement variant exists.** Remediation §5.1 | `CHAR-005` | **No** — closed on complete inspection |
| 4 | General Index not swept as a completeness locator | RC Appendix 4 p. 302 | ~~No~~ → **YES, remediation pass 1** | **CLOSED, and it was not empty.** `Encumbrance .63, 88 / Effect on movement . 88` confirms only two encumbrance locations; `Movement . 87, 88, **103**, 263, 264` surfaced **RC Ch. 8 p. 103**, a governing object this packet missed. Remediation §5.3, §5.5 | `CHAR-005` | **No** — audit class H discharged |
| 5 | Whether the blindness / stunning / starvation movement multipliers belong to `CHAR-005` or to an unassigned condition responsibility | RC p. 150 | **Yes — text inspected** | Ownership question, not a source question | **Human governance** | **Yes** — a Rule ID may need assigning, and this researcher may not assign one |
| 6 | Water Movement Modification Table and Aerial Travel not inspected | RC pp. 90 | **No** | Deliberately excluded as out of cluster; recorded as located | water/air travel responsibility | No — excluded with reason, not silently dropped |
| 7 | Suit Armor conflict | RC pp. 67, 68, 88 | **Yes — all three visually verified** | Genuine printed contradiction | human / Stage B | No — §10.2.2 case 3 |
| 8 | Starvation Table non-monotonicity | RC p. 150 | **Yes — visually verified** | Genuine printed defect | human / Stage B | No — §10.2.2 case 3 |

**Items 1, 3 and 4 are unfinished source inspection and are declared as such; item 5 requires a human decision.** Per protocol §10.2 there are **zero silent unresolved research tasks** in this packet, and completeness is therefore not claimed.

## 12. Alternate-Source Research Requirement (protocol §15)

**Not established, and not permitted on the current evidence.** Two candidate gaps exist — the unquantified racial-armour reduction (§10 Gap 1) and the Mystic `MV` × encumbrance interaction (§10 Gap 2) — but protocol §9.1 forbids writing the precise RC gap statement that would authorise alternate-source work until the §9.1 audit is complete for the responsibility, and §11 items 1, 3 and 4 show it is not.

**If** a gap statement is later authorised, it must be written at this precision, and not more broadly:

```text
CANDIDATE GAP A  RC states that wearing armour made for another race causes
                 "an additional reduction to movement beyond what the armor's
                 encumbrance calls for" (Ch. 4 p. 67) and nowhere quantifies it.

CANDIDATE GAP B  RC gives the Mystic a class/level movement rate (Ch. 2 p. 31)
                 and an encumbrance-driven movement table (Ch. 6 p. 88), and
                 nowhere states how the two combine.
```

These are recorded as **candidates for a later authorised pass**, not as an alternate-source plan, and no alternate source was opened.

## 13. Possible Simulator Ruling Areas (named, not drafted)

- Suit Armor's 30′ (10′) versus its 750 cn encumbrance band (§10 Conflict 1).
- The Starvation Table's 75–99% movement multiplier (§10 Conflict 2).
- The magnitude of the racial-armour movement reduction (§10 Gap 1), **only if** alternate-source completion fails.
- Mystic `MV` × encumbrance composition (§10 Gap 2), on the same condition.

Named only. None drafted, bundled, or self-approved. Protocol §16 places Simulator Rulings last, after gap-directed alternate-source research fails — which has not been attempted, let alone failed.

## 14. Legacy Rule Card Withholding (protocol §13)

**Not applicable.** `CHAR-005` is `Unresearched`; no prior Rule Card exists and none was consulted. The card is not `REVALIDATION_REQUIRED`.

## 15. Access Limitations Encountered

As `CHAR-004-evidence.md` §15: OCR hyphenation artefacts (`¬`), column flattening in every multi-column table, and no region-crop support in the Browser pane (each close reading required a separate IIIF request). Two OCR corruptions were caught by visual verification and are recorded above (`1 F2 normal` → `1 ½ normal`; the Starvation Table movement column, which OCR rendered ambiguously and the page image resolved). The General Index was not swept (§11 item 4).

## 16. Confidence Assessment

| Area | Confidence | Basis |
|---|---|---|
| The encumbrance → rate table and its three rate definitions | **High** | Visually verified governing object; Ch. 6 prose read in full; RC's own worked example is arithmetically consistent |
| Time-unit semantics (turn vs. round) and feet-vs-yards | **High** | Explicit, and consistent with landed `EXP-002` |
| Slowest-member group rule | **High** | Single explicit statement, no competing text located |
| Running limit and exhaustion consequences | **High** | Single explicit section read in full |
| That the p. 88 table is **not** the only governing object | **High** | Six further provisions located, four of them visually verified |
| Mystic class movement rate | **High as a fact; unresolved as a composition** | Table visually verified; its interaction with encumbrance is unstated by RC |
| Completeness of the set of movement modifiers | **Moderate** | Tables Index swept in full, but §11 items 1, 3 and 4 remain — the other class entries, Ch. 19's body, and the General Index |

## 17. Recommendation

Per protocol §11.19:

```text
MORE PRIMARY RESEARCH REQUIRED
```

Bounded and named: §11 items 1, 3 and 4 (other class entries as complete entries; Ch. 19 body; General Index sweep), plus the human scope decision in item 5. The card's **core procedure is fully established and visually verified**; what is outstanding is the completeness perimeter around the modifiers, which is precisely where this card has already been shown to extend beyond its principal table.

**Cluster-level status of this packet:**

```text
PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
```
