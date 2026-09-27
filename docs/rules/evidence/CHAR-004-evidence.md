# Stage-A Evidence: CHAR-004 — Starting Equipment & Expedition Preparation

> **✅ STAGE B COMPLETE, 2026-09-24. This packet's two blocking defects are adjudicated and the Rule Card is drafted.**
>
> | §10 defect | Determination |
> |---|---|
> | **Defect 1 — belt pouch `2 + 50 = 52` vs. the printed `55 cn`** | **`SR-6`** — a fully loaded belt pouch weighs **`52 cn`**. Empty `2 cn` and capacity `50 cn` are preserved independently; the printed worked total is **erroneous** |
> | **Defect 8 — Magic-User dagger** (recorded in the remediation record) | **`SR-7`** — the dagger is **unconditional**; the expanded list stays optional; Ch. 4's note `w`, **as to the dagger**, is a compilation defect |
> | Defect 2 — "Clothes, plain" carries the quiver footnote | **Read as a typographic defect**; the `**` rule applies. **Not** elevated to a ruling — no mechanic turns on it. See the Rule Card's Open Questions 1 |
> | Defect 4 — free-kit stated twice, differently | **Closed.** The Rule Card adopts Ch. 4 p. 62's enumerated kit, which is strictly the more specific |
>
> **Rule Card drafted:** `docs/rules/character_creation/starting_equipment_and_expedition_preparation.md` — `AWAITING_APPROVAL`.
>
> **The RC's internal inconsistencies are NOT resolved by these rulings.** The printed page still disagrees with itself; only the simulator's behaviour is settled. **This packet's body is preserved as researched and is not rewritten to anticipate the outcomes.**
>
> ---
>
> **✅ STAGE-A RESEARCHER CLOSURE (2026-09-14). The last outstanding inspection item is closed and human ownership governance is applied.**
>
> - **Nets Table (RC p. 65, leaf n64) — VISUALLY VERIFIED.** This was the single item the second independent review left as a `CONDITIONAL PASS`. Three columns, seven rows, two footnotes; **agrees with this packet's OCR record exactly**; no new mechanic, contradiction or dependency. **§11 row 1 is closed** and every identified primary-source inspection item for this packet is now complete.
> - **GOVERNANCE DECISION 1 APPLIED — `CHAR-004` canonically owns equipment-facing class restrictions.** The human project owner has assigned this card the class-specific mechanics required to determine authoritative **mundane** equipment legality: weapon-permission predicates, armour/shield legality where relevant to equipment selection, class-specific equipment prohibitions, equipment-specific class pricing adjustments, and other class-dependent mundane equipment rules. **§9 Challenge 1 and §7's first bullet are superseded on ownership** — they routed these to `CHAR-009`, and that pointer is corrected. **The whole of `CHAR-009` is NOT an incoming dependency**; `CHAR-009` may describe these as class features but must not become a second canonical implementation owner. **Magic-item-specific restrictions remain with `TREAS-004`.**
> - **GOVERNANCE DECISION 4 APPLIED — the Chapter 10 high-level pathway is `researched / preserved / NOT V1-WIRED`.** The findings in the remediation record §5.4 stand as evidence; the pathway is **not** made executable by `CLUSTER-003` and `CHAR-004` was **not** expanded to absorb it.
> - **Source location versus ownership is preserved.** Every citation showing that RC prints these restrictions in Chapter 2 (Thief p. 21, Dwarf p. 23, Halfling p. 26, Druid p. 28, Magic-User p. 19) remains intact. Ownership moved; evidence did not.
> - **No mechanic, case, table reading, or open RC question in this packet is changed by the governance decisions.** All §10 defects survive.
>
> **⚠ REMEDIATION PASS 1 APPLIED (2026-09-13). Three findings below are superseded; two are new.** The independent completeness review returned **`REMEDIATION REQUIRED / FAIL — unfinished structural inspection`** against this packet as committed at `e26a1e0`. The remediation record is `docs/rules/evidence/CLUSTER-003-remediation-pass-1.md`; **read it alongside this packet.** The original text below is preserved unaltered as audit history.
>
> **What the independent reviewer found incomplete here:** §11 items 3 (Chapter 2 class entries), 4 (Chapter 10 high-level creation) and 6 (General Index) were unfinished source inspection, and §9 Challenge 1 was left `QUALIFIED` when the underlying question was answerable.
>
> **What changed as a result:**
>
> - **§9 Challenge 1 is now answered, and the answer is stronger than "qualified".** `CHAR-004` **cannot** determine legal starting equipment from Chapter 1 + Chapter 4 + Chapter 13 alone. Five of nine classes carry restrictions stated **only** in their Chapter 2 entries — Thief weapons, Dwarf weapons, Halfling weapons and armour-fit, the Druid **+50% pricing rule** for commissioned wooden weapons, and the Mystic protective-device prohibition. RC's own General Index routes `Weapon restrictions` to **nine class pages and not to Chapter 4**, and RC Ch. 2 p. 13 assigns *"restrictions or advantages with armor and weapons"* to Class Details. **Armour permissions are genuinely duplicated; weapon permissions are not.** See remediation §4.
> - **NEW DEFECT — magic-user dagger.** Ch. 4's note `w` marks **both dagger rows** "at the DM's discretion", while Ch. 2 p. 19 makes the dagger the magic-user's one **unconditional** weapon. Chapter 4's `w` set is exactly Chapter 2's optional set **plus the dagger**. Remediation §6 Defect 8.
> - **NEW MATERIAL — Chapter 10 high-level creation (§11 item 4, now closed).** Starting money is **1% of XP in gp**, explicitly *"not used for purchasing items"*; equipment is **granted**, not bought; there is an alternate cash method at DM-set prices, two magic-item methods, and a Magical Item Price Ranges Table. It also contains **the only RC statement distinguishing equipment owned from equipment carried**. Since `CHAR-001` §5 already lands Step 2 of this same procedure, the gap is concrete. `CHAR-004` was **not** expanded. Remediation §5.4.
> - **This packet's §9 Challenge 4 (derived encumbrance) and §10 Defects 1, 2 and 4 all survive re-testing unchanged.**
>
> **This is a Stage-A evidence artifact, not a Rule Card.** Produced under `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` (`DEC-0009`) and the primary-source completeness requirements adopted by `DEC-0010`. It is not mechanically authoritative, is not `APPROVED`, and authorizes nothing. **Stage B was not begun.**
>
> **Completeness status: `PREPARED FOR INDEPENDENT COMPLETENESS REVIEW` (protocol §10.1.1).** The researcher who collected this evidence has performed the adversarial self-review and may not certify its own completeness. The independent completeness review required by protocol §10.1.2 / `DEC-0010` item 14 has **not** been performed. Human Evidence Review follows that review, not this artifact.
>
> **Research-risk classification: HIGH** (protocol §9.4 — *equipment* is a named high-risk responsibility, and per-item mechanically significant tables drive the procedure). §9.2 visual verification of structured objects is therefore **mandatory, not discretionary**, for this packet.

## 1. Research Scope

**Investigating:** what the Rules Cyclopedia establishes about a character acquiring and carrying equipment before and between expeditions — how starting wealth is determined, what may be bought, at what cost, at what encumbrance, what a character is assumed to own without purchase, what restricts purchase, and what RC does when an item is not on its lists.

**Cluster context:** `CLUSTER-003` — Equipped Dungeon Movement. `CHAR-004` is the incoming dependency of `CHAR-005` (Encumbrance & Movement Rate), which is in turn the incoming dependency of `EXP-003`. The cluster's interest in `CHAR-004` is therefore **primarily the `Enc (cn)` column and the money procedure that populates it** — but the whole responsibility is researched, because a partial pass is exactly the failure `DEC-0010` exists to prevent.

**Assigned falsification target** (task instruction): *test the assumption that `CHAR-004` does not require an unlanded class-ability card such as `CHAR-009`.* See §9, Challenge 1. **The assumption did not survive unqualified.**

**Deliberately excluded from this pass, with reasons, recorded in §6:** siege equipment, water transportation, the Weapon Special Effects Table's combat resolution, magical-item acquisition, and between-expedition town services (`ADV-003`).

## 2. Primary-Source Access

*Dungeons & Dragons Rules Cyclopedia* (TSR, 1991; ISBN 1-56076-085-0).

| Purpose | Access method |
|---|---|
| Navigation, whole-source search, prose reading | Full OCR transcription, `https://archive.org/stream/TSR1071TheDDRulesCyclopedia/TSR-1071-The-DD-Rules-Cyclopedia_djvu.txt`, loaded in-browser and searched programmatically with surrounding context read in full |
| §9.2 visual verification of structured objects | IIIF page images, `https://iiif.archive.org/iiif/TSR1071TheDDRulesCyclopedia$<leaf>/pct:<x>,<y>,<w>,<h>/<width>,/0/default.jpg`, where `leaf = printed_page − 1` |

`STOP — PRIMARY SOURCE ACCESS REQUIRED` was **not** triggered. `STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED` was **not** triggered. Access limitations are recorded in §15.

**Alternate sources were not consulted.** No RC gap was established that would authorize gap-directed alternate-source research (protocol §15). AD&D was not consulted (`AGENTS.md` §4).

## 3. Research Questions

- **A.** How is a beginning character's starting wealth determined?
- **B.** What does a character own without spending that wealth?
- **C.** What is the complete set of purchasable equipment RC provides, and what mechanical columns does each catalog carry?
- **D.** How is encumbrance expressed per item, and what unit conversions does RC state?
- **E.** What restricts what a character may buy or use — and where does RC state those restrictions?
- **F.** What does RC do when an item is not on its lists?
- **G.** Which parts of Chapter 4 belong to `CHAR-004` at all, and which belong to other responsibilities?

## 4. Evidence Map

| Q | RC Location | What RC Establishes | Provenance | Confidence |
|---|---|---|---|---|
| A | Ch. 1, step 5 "Roll for Money", p. 8 | "Roll 3d6 and multiply by 10 to find your character's starting gold pieces." Stated twice in the same section — as a step heading and as worked prose with an example (roll 12 → 120 gp). | RC Explicit | DIRECT PRIMARY TEXT |
| A | Ch. 4, "Money — Starting Gold", p. 62 | Duplicate presentation: "Beginning characters receive a one-time sum of 3d6 × 10 gold pieces." Adds the fiction (savings / family money) and a DM-recommendation note. **Numerically identical to Ch. 1.** | RC Explicit (audit class I) | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED |
| B | Ch. 1 p. 8 **vs.** Ch. 4 p. 62 | Two non-identical statements of the free starting kit. Ch. 1: "no possessions except for normal clothes and a little money." Ch. 4: "two or three sets of plain clothes, a pair of shoes, a belt, and a belt-pouch." Ch. 4 is strictly more specific. | RC Explicit ×2 (audit class I) | PRIMARY TEXT; see §10 Defect 4 |
| B | Ch. 4, Adventuring Gear descriptions, p. 69 | Third presentation: "A character is presumed to start play with two or three sets of clothes of the plain variety." | RC Explicit (audit class I) | DIRECT PRIMARY TEXT |
| C/D | **Weapons Table, pp. 62–63** | Columns, **visually verified**: `Damage | Range S/M/L | Cost (gp) | Enc (cn) | Notes`. No hidden sixth column; no dropped rows at the page break. | RC Explicit | **VISUALLY VERIFIED** (leaf n61) |
| C/E | **Weapons Table (Notes), p. 63** | Twelve note codes, **visually verified**: `a` ammunition load included; `c` clerics (and druids, if a form with no metal or stone parts exists); `m` missile only; `n` net cost/enc by size; `r` throwable only at Expert+ mastery; `s` see description; `t` hand weapon that may also be thrown; `v` may be set vs. charge; `w` magic-users **at the DM's discretion**; `HH` usable one- or two-handed, **halflings and other small races can use**; `2H` two hands, loses individual initiative, **halflings and small races cannot use**; `S`/`M`/`L` weapon size. | RC Explicit | **VISUALLY VERIFIED** (leaf n62) |
| D | Weapons Table note `a`, p. 63 | Normal ammunition load is **already inside** the weapon's `Enc`: bow 20 arrows, crossbow 30 quarrels, sling 30 stones, blowgun 3 darts. Variable loads: 2 arrows = 1 cn, 3 quarrels = 1 cn, 5 sling stones = 1 cn, 5 darts = 1 cn. Worked results: long bow without arrows = 20 cn; light crossbow without quarrels = 40 cn. | RC Explicit | **VISUALLY VERIFIED**; arithmetic internally consistent with the Weapons Table values |
| C/D | **Ammunition Table, p. 63** | Columns, **visually verified**: `Weapon | Type of Ammunition | Standard Load (# of Shots) | Cost (gp) | Enc (# of shots per cn)`. **The Enc column is an inverse rate, not a cn value** — a column semantic OCR linearization destroys. Rows: Blowgun/Dart 5/1/5; Bow/Arrow 20/5/2; silver-tipped arrow 1/5/2; Crossbow/Quarrel 30/10/3; silver-tipped quarrel 1/5/3; Sling/stone or lead pellet 30/1/5; silver pellet 1/5/5. | RC Explicit | **VISUALLY VERIFIED** (leaf n62) |
| C/D | Nets Table, p. 65; Weapons Table note `n` | A net has **no fixed cost or encumbrance**: 1 sp and 1 cn **per square foot**. Worked example: a 6′×6′ medium net = 36 sp (3.6 gp) and 36 cn. The Nets Table maps victim size → net size. Whip is likewise per-foot: 1 gp/ft, 10 cn/ft. | RC Explicit | DIRECT PRIMARY TEXT (OCR; table not visually verified — see §11) |
| C/D | **Armor Table, p. 67** | Columns, **visually verified**: `AC | Armor Type | Cost (gp) | Enc (cn) | Notes`. Rows: Shield (−1)\* / 10 / 100 / D; Leather 7 / 20 / 200 / D,T; Scale Mail 6 / 30 / 300; Chain Mail 5 / 40 / 400; Banded Mail 4 / 50 / 450; Plate Mail 3 / 60 / 500; Suit Armor 0 / 250 / 750 / S. | RC Explicit | **VISUALLY VERIFIED** (leaf n66) |
| E | Ch. 4, Armor prose, p. 67 | "All fighters, clerics, dwarves, elves, and halflings can use any of the types of armor… Thieves and druids can use the types indicated in the 'Notes' column. **Magic-users and mystics can use none of these armor types.**" | RC Explicit | DIRECT PRIMARY TEXT |
| C/D | **Barding Table and Barding Encumbrance Table, p. 68** | Barding Table: `Armor Type | Cost (gp) | Enc (cn) | AC`. Barding Encumbrance Table columns, **visually verified**: `Movement Rate | Encumbrance: Full Movement (cn) | Encumbrance: Half Movement (cn)` — e.g. Draft Horse 90′ (30′) / 4,500 / 9,000; Riding Horse 240′ (80′) / 3,000 / 6,000. **This is a second, structurally different encumbrance system** (two bands, not six) applying to animals, not characters. | RC Explicit | **VISUALLY VERIFIED** (leaf n67) |
| C/D | **Adventuring Gear Table, p. 69** | Columns, **visually verified** across both halves: `Item | Description | Cost | Enc (cn)`, with three footnote markers. Capacity-bearing containers: Backpack cap. 400 cn / enc 20\*; Pouch, belt cap. 50 cn / 5 sp / enc 2\*; Sack small cap. 200 cn / enc 1\*; Sack large cap. 600 cn / enc 5\*; Quiver enc 5\*\*\*. Footnotes: `*` encumbrance **when empty**, and when filled includes both the container and its contents; `**` encumbrance **if packed** — "If the clothes are worn, **disregard the encumbrance**"; `***` quiver empty, filled up to 10 cn total. | RC Explicit | **VISUALLY VERIFIED** (leaf n68); two printed defects recorded in §10 |
| D | Ch. 4 p. 63 (Weapons Table legend) **and** Ch. 6 p. 88 | "**One coin weighs one-tenth of a pound.**" Restated in Ch. 6 as "1 coin equals approximately 1/10 of a pound in weight **and awkwardness**." Two presentations; Ch. 6 adds *awkwardness*, which is not merely a mass claim. | RC Explicit ×2 (audit class I) | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED |
| C | Ch. 4, Money — Conversions, p. 62 | `1 pp = 5 gp = 10 ep = 50 sp = 500 cp`. Abbreviations pp/gp/ep/sp/cp. | RC Explicit | DIRECT PRIMARY TEXT |
| E | **Ch. 1, step 6 "Buy Equipment", p. 8** | "There are restrictions on what items your character is allowed to have, especially on armor and weapons. **Before you go shopping, be sure you have read the full description of your character class, later in this chapter.**" Also: the complete list is in Chapter 4; "**Be sure to ask your Dungeon Master if everything on that list is available in his campaign**"; a magic-user "cannot wear any armor at all and can only use a few types of weapons"; "Thieves, however, **must buy thieves' tools** to use their Open Locks ability"; if the total exceeds available money, remove items. | RC Explicit | DIRECT PRIMARY TEXT — **this is the routing statement that drives §9 Challenge 1** |
| F | Ch. 13, "Equipment Not Listed", p. 147 | Beginning players are restricted to the Chapter 4 lists unless the DM decides otherwise; when the DM allows an unlisted item, he "must decide on its **cost, encumbrance**, and other characteristics." | RC Explicit | DIRECT PRIMARY TEXT |
| C | Ch. 4, Land Transportation, pp. 70–71 | Riding Animal Costs Table (camel 100, draft horse 40, riding horse 75, war horse 250, mule 30, pony 35 gp) and Land Transportation Gear Table. Cart: max safe MV 60′ (20′), capacity 4,000 cn (one horse) / 8,000 cn (two); above 60′ the DM checks 1d6 per turn — 1 breaks down, 2–3 tips over. Wagon: same rate, 2 tips over. **Vehicle Movement Speeds:** if the vehicle load ≤ the animal's normal encumbrance value it moves at normal speed; if greater, at **half** the animal's normal speed. Neither vehicle can cross desert, forest, mountain or swamp except by road. | RC Explicit | DIRECT PRIMARY TEXT (OCR; tables not visually verified — deliberately, see §6) |
| G | Ch. 14, monster listings ("Load" paragraph, "Barding Multiplier") | Animal and monster carrying capacity is defined **in Chapter 14**, per creature, not in Chapter 4 or Chapter 6. Ch. 4 p. 68 explicitly forwards to it for optional barding of other creatures. | RC Explicit | DIRECT PRIMARY TEXT (cross-reference followed to its statement of location; the Ch. 14 entries themselves are out of scope — §6) |

## 5. Governing Procedure, as RC States It

RC does not present equipment acquisition as a table lookup. It presents it as **two ordered steps inside the character-creation sequence**, with the catalog held in a separate chapter:

```text
Chapter 1 "Steps in Character Creation", steps 5 and 6 (p. 8)

  5. Roll for Money        3d6 x 10 = starting gold pieces
                           character otherwise owns only clothes
                           (Ch. 4 p. 62 enumerates: 2-3 sets of plain
                            clothes, a pair of shoes, a belt, a belt-pouch)

  6. Buy Equipment         catalog is Chapter 4
                           DM controls availability in his campaign
                           class restrictions apply, especially armour
                           and weapons -- read the class description
                           total cost may not exceed money held
```

Chapter 4 then supplies the catalogs, and Chapter 13 p. 147 supplies the escape hatch for items RC does not list. **The encumbrance value is carried on the catalog row, not computed by this card**; what consumes it is `CHAR-005`.

## 6. Primary-Source Coverage Checklist (protocol §9.3)

**TOC sections inspected (audit class A):** Ch. 1 "Roll for Money" p. 8, "Buy Equipment" p. 8; Ch. 4 Equipment p. 62 in full — Money 62, Weapons 62, Armor 67, Adventuring Gear 68, Land Transportation 70, Water Transportation 70, Siege Equipment 72; Ch. 13 "Equipment Not Listed" p. 147; Ch. 16 Treasure p. 224 (boundary check only).

**Tables Index entries inspected (audit class B) — every entry whose title or subject could bear on equipment:** Weapons Table 62; Weapon Special Effects Table 63; Ammunition Table 63; Nets Table 65; Armor Table 67; Armor Type and Armor Class Table 8; Barding Table 68; Barding Encumbrance Table 68; Adventuring Gear Table 69; Land Transportation Gear Table 70; Riding Animal Costs Table 70; Sailing Vessels Table 71; Passage Table 72; Siege Weapons Table 72; Miscellaneous Siege Equipment Table 74; Miscellaneous Siege Machine Equipment Table 124; Siege Machine Weapons Table 124; Character Movement Rates and Encumbrance Table 88; Additional Weapon Modifiers Table 231; Magical Weapon Generation Table 230; Levels of Weapon Mastery Table 75; Weapons Mastery Table 78; Weapon Choices by Experience Level Table 75.

**Named tables inspected directly (audit class C):** Weapons Table; Weapons Table (Notes); Ammunition Table; Nets Table; Armor Table; Barding Table; Barding Encumbrance Table; Adventuring Gear Table; Riding Animal Costs Table; Land Transportation Gear Table.

**Stat blocks (audit class D):** not applicable to this responsibility; the per-class armour/weapon permissions that live in Ch. 2 class entries were located but **not** read as complete entries — see §11, item 3, and §9 Challenge 1.

**Summary boxes / parallel presentations (audit classes E, I):** three separate statements of starting money and the free kit (Ch. 1 p. 8, Ch. 4 p. 62, Ch. 4 p. 69 description) recorded **separately**; the coin-weight statement recorded in both Ch. 4 p. 63 and Ch. 6 p. 88; class weapon/armour permissions recorded in both Ch. 4 (table notes and armour prose) and — by explicit forward reference — Ch. 2.

**Chapter sections read in full (audit class F):** Ch. 1 "Roll for Money" and "Buy Equipment"; Ch. 4 "Money", Weapons Table legend and full weapon descriptions A–W, Armor section including the complete Suit Armor entry, Barding and Barding-and-Encumbrance, Adventuring Gear descriptions A–W, Land Transportation Equipment descriptions and Vehicle Movement Speeds; Ch. 13 "Equipment Not Listed".

**Cross-references followed (audit class G):** Ch. 1 p. 8 → Ch. 4 (catalog); Ch. 1 p. 8 → Ch. 2 class description (permissions) — **followed to the point of establishing that Ch. 2 carries governing material, then stopped at this cluster's boundary (§9 Challenge 1)**; Ch. 4 p. 62 → "the more encumbrance a character is carrying, the slower he moves" → Ch. 6 p. 88; Ch. 4 p. 68 → Ch. 14 "Load" / "Barding Multiplier"; Ch. 4 weapon notes → Weapon Mastery (Ch. 5) for note `r`; Ch. 4 Adventuring Gear → thieves' tools → `CHAR-010`.

**Appendices / index entries (audit class H):** Appendix 4 "Index to Tables and Checklists" p. 301 used as the class-B instrument above. General Index p. 302 not separately swept — recorded as a limitation in §15.

**Visual-page verification completed (protocol §9.2), with printed page numbers:**

| Object | Printed page | Leaf | Result |
|---|---|---|---|
| Weapons Table (column structure and values) | 62 | n61 | Confirmed; five columns; OCR values matched |
| Weapons Table (Notes) | 63 | n62 | Confirmed; twelve note codes; matched OCR |
| Ammunition Table | 63 | n62 | Confirmed; **Enc column is "# of shots per cn"** |
| Armor Table | 67 | n66 | Confirmed |
| Barding Encumbrance Table | 68 | n67 | Confirmed; three-column two-band structure |
| Adventuring Gear Table (both halves) | 69 | n68 | Confirmed; **two printed defects found, §10** |
| **Nets Table + both footnotes** *(added 2026-09-14, Stage-A closure)* | **65** | **n64** | Confirmed; 3 columns × 7 rows; agrees with OCR exactly; no new mechanic |
| Net weapon description — *"halflings and small nonhumans… cannot use nets larger than 6′ × 6′"* *(added 2026-09-14)* | 65 | n64 | Confirmed; a **class/race mundane equipment restriction stated in Chapter 4**, now owned by `CHAR-004` under Decision 1 |

**Potentially relevant objects deliberately excluded, with reasons:**

| Object | Reason for exclusion |
|---|---|
| Water Transportation; Sailing Vessels Table 71; Passage Table 72 | Water travel is not dungeon movement and is not reached by `CLUSTER-003`'s dependency spine. Recorded as located and uninspected, not as absent. |
| Siege Weapons Table 72; Miscellaneous Siege Equipment Table 74; Ch. 9 siege-machine tables 124 | Mass-combat/siege responsibility; no dungeon-movement or encumbrance interaction located. |
| Weapon Special Effects Table 63 (knockout/stun/delay/entangle/slow resolution) | Combat resolution — `COMBAT-002`/`COMBAT-003`. Its *existence and columns* were confirmed visually in passing; its mechanics were not researched. |
| Ch. 5 Weapon Mastery tables 75–81 | `CHAR-011`. Reached only as the referent of Weapons Table note `r`. |
| Ch. 16 Treasure; Additional Weapon Modifiers Table 231; Magical Weapon Generation Table 230 | Magical-item acquisition and generation — `TREAS-003`/`TREAS-004`. |
| Ch. 14 per-creature "Load" paragraphs and Barding Multipliers | Monster statistics — `MON-*`. The **forward reference** was followed; the entries were not. |
| Ch. 11 Retainers/Mercenaries/Specialists costs | `CHAR-006`, **explicitly deferred out of `CLUSTER-003`**. Not researched. |
| Between-expedition resupply and town services | `ADV-003`. Not researched. |

## 7. Questions Belonging to Other Rule Cards' Own Scope

- ~~Per-class and per-race weapon/armour **permission** rules as a system → `CHAR-009`~~ → **SUPERSEDED 2026-09-14 by human governance Decision 1: mundane weapon/armour/shield permissions, class equipment prohibitions and equipment-specific class pricing are owned by `CHAR-004` — this card.** Magic-item use restrictions (e.g. the Mystic protective-device prohibition) remain with **`TREAS-004`**. `CHAR-002`'s downstream pointer has been corrected in `docs/rules/character_creation/race_and_class_eligibility.md` §A and in `CHAR-002-evidence.md` §6 — **an ownership-reference correction only; no `CHAR-002` mechanic changed.**
- Thieves' tools as a prerequisite for Open Locks → `CHAR-010`.
- Weapon Mastery levels gating whether a weapon may be thrown (note `r`) → `CHAR-011`.
- Weapon damage, ranges, two-handed initiative loss, set-vs-charge, net entanglement, blackjack knockout → `COMBAT-002`, `COMBAT-003`, `COMBAT-006`, `COMBAT-007`.
- Suit Armor's surprise and saving-throw effects → `ENC-002`, `COMBAT-004`. **Its movement-rate statement is `CHAR-005`'s** — see `CHAR-005-evidence.md` §10.
- Torch and lantern **duration and radius** → `EXP-006`. Located here because both are Chapter 4 catalog items; their *cost and encumbrance* are this card's, their *burn time and light radius* are not.
- Iron/standard rations and starvation → `ADV-*`/survival; the Starvation Table's movement column is recorded in `CHAR-005-evidence.md`.
- Mount, cart, wagon and animal carrying capacity → a transport responsibility not yet identified in `INVENTORY.md`; **raised as an open governance question, not assigned** (§11, item 5).

## 8. Whole-Source Cross-Reference Pass (protocol §9)

> Performed **after** structural mapping and governing-object inspection, per §9.1.1. Full-text search is used here as locator and falsification tool only.

**Search terms used:** `encumbrance` (93 occurrences reviewed in context); `cn`; `Enc (cn)`; `coin weighs`; `one-tenth of a pound`; `Starting Gold`; `3d6 x 10`; `one-time sum`; `Buy Equipment`; `Roll for Money`; `Equipment Not Listed`; `Capacity`; `encumbrance when empty`; `if it is worn`; `disregard the encumbrance`; `Barding`; `Load`; `Barding Multiplier`; `thieves' tools`; `magic-users and mystics`; `Suit Armor`; `movement rate is 30`; `Torch:`; `Lantern:`; `burns for`; `Nets Table`; `per square foot`; `optional rule`.

**Cross-references discovered:**

1. **Ch. 1 p. 8 → Ch. 2 class descriptions**, for what a character is allowed to buy. This is RC routing its own purchase step through class-entry material.
2. **Ch. 4 p. 62 → Ch. 6 p. 88**: "Remember that the more encumbrance a character is carrying, the slower he moves." RC itself draws the `CHAR-004` → `CHAR-005` edge.
3. **Ch. 4 p. 68 → Ch. 14**, for non-standard mounts' Load and Barding Multiplier.
4. **Ch. 4 Weapons Table note `r` → Ch. 5 Weapon Mastery.**
5. **Ch. 4 Adventuring Gear → Ch. 2 Thief** (thieves' tools ↔ Open Locks).
6. **Ch. 13 p. 147 → Ch. 4**, closing the catalog: unlisted items are a DM decision over cost and encumbrance.

**Negative findings, stated as coverage rather than absence:** across audit classes A, B, C, F and G as inspected above, **no third character-carried-equipment catalog beyond the Weapons/Ammunition/Nets/Armor/Barding/Adventuring-Gear/Land-Transportation set was located**, and **no per-class starting-equipment package or starting-equipment kit table was located**. Both are recorded as *not located by the objects inspected*, not as proof that RC contains none. The Ch. 2 class entries were not read as complete entries in this pass (§11, item 3).

## 9. Falsification Pass (protocol §10)

**Challenge 1 — the assigned target: "`CHAR-004` does not require an unlanded class-ability card such as `CHAR-009`."**

*Sought:* whether any RC statement makes equipment acquisition depend on class-entry material this cluster does not contain.
*Searched:* Ch. 1 step 6 in full; Ch. 4 Weapons Table Notes; Ch. 4 armour prose; the Tables Index for a permissions table; `magic-users and mystics`, `can use none of these`, `thieves' tools`.
*Found:* RC states class weapon and armour permissions in **two places at once**, and explicitly routes the buying step to the second one:

- **Chapter 4 itself** carries operative permissions — note `c` (clerics; druids only in a form with no metal or stone parts), note `w` (magic-users at the DM's discretion), notes `2H`/`HH` (halflings and small races cannot / can), and the armour prose naming fighters, clerics, dwarves, elves, halflings, thieves, druids, magic-users and mystics.
- **Chapter 1 p. 8** nonetheless instructs: *"Before you go shopping, be sure you have read the full description of your character class, later in this chapter,"* and gives a class-specific worked consequence (a magic-user "cannot wear any armor at all and can only use a few types of weapons").
- The landed `CHAR-002` boundary already assigns "weapon/armor permissions" to `CHAR-009`/`TREAS-004`, and `CHAR-009`'s `INVENTORY.md` row already carries the Mystic armour prohibition (P2, recorded 2026-08-29). *(**State of the repository as at 2026-09-13**, which is what made this a live ownership conflict. **Superseded 2026-09-14:** `CHAR-002`'s pointer now routes mundane weapon/armour/shield permissions to `CHAR-004`, and `CHAR-009`'s row carries an explicit non-ownership boundary. Retained because the conflict this bullet documents is the evidence the human decision rested on.)*

**Disposition: QUALIFIED — the assumption does not survive unqualified.**

```text
CHAR-004 WITHOUT CHAR-009    money roll, free kit, catalog, costs,
                             encumbrance values, capacity rules,
                             unlisted-item procedure
                             -> all fully specified in RC Ch. 1, Ch. 4, Ch. 13

CHAR-004 WITHOUT CHAR-009    whether a given purchase is legal for a
                             given class
                             -> RC states this in Ch. 4 AND routes it to Ch. 2
```

This is a **duplicate-ownership question** (audit class I), not a missing dependency: the restriction is not absent from `CHAR-004`'s own chapter. **It is raised for human governance and is not resolved here.** It is **not** a boundary-reopen condition of the kind the task defined — `CHAR-009` is not one of the three deliberately deferred items (`CHAR-006`, `CHAR-008`, `EXP-010`) — but it is a genuine unlanded-dependency question that a human must settle before Stage B.

**Challenge 2 — "starting money is 3d6 × 10 gp."**

*Sought:* any second or contradicting starting-wealth rule; any per-class variation; any high-level-character starting-wealth rule.
*Searched:* `Starting Gold`, `3d6`, `one-time sum`, Ch. 1 step 5 in full, Ch. 4 Money in full, Ch. 10 "Creating High-Level Player Characters" (located during `CLUSTER-002` research).
*Found:* Ch. 1 and Ch. 4 agree exactly. No per-class variation was located in the objects inspected.
**Disposition: CONFIRMED**, with the qualification that Chapter 10's high-level-character creation path was **not** re-inspected for an equipment or wealth provision in this pass (§11, item 4).

**Challenge 3 — "a container's encumbrance is its own encumbrance plus its contents."**

*Sought:* whether RC's own worked example agrees with its own table values.
*Searched:* Adventuring Gear Table footnote `*` and the Pouch, belt row, **visually verified**.
*Found:* the rule states the sum; the worked example does not equal the sum of the printed values.
**Disposition: CONFIRMED AS A RULE, CONTRADICTED BY ITS OWN EXAMPLE.** Recorded as §10 Defect 1. Not resolved.

**Challenge 4 — "encumbrance is always a number on a catalog row."**

*Sought:* catalog items whose encumbrance is not a fixed number.
*Searched:* Weapons Table for non-numeric `Enc` cells; note `n`; `per square foot`; `per ft`.
*Found:* nets (`n` in both Cost and Enc — 1 sp and 1 cn per square foot) and whips (1 gp/ft, 10 cn/ft) are **computed from size**, and containers change encumbrance when filled (footnote `*`), while packed clothing's encumbrance is **disregarded entirely when worn** (footnote `**`).
**Disposition: REJECTED as stated.** Encumbrance is a *derived* quantity for at least four item classes. Any `CHAR-004` specification that models `Enc` as a constant per item is incomplete.

**Challenge 5 — "Chapter 4 is `CHAR-004`."**

*Sought:* whether the chapter's scope and the card's scope coincide.
*Searched:* the chapter's own TOC sub-entries; the Tables Index; the `INVENTORY.md` row title.
*Found:* Chapter 4 also contains siege engines, sailing vessels, passage fares, barding, and a mount/vehicle carrying-capacity system with its **own two-band encumbrance structure** distinct from the character six-band table. `INVENTORY.md` titles `CHAR-004` "Starting Equipment & Expedition Preparation", which does not obviously extend to siege trains or naval charter.
**Disposition: REJECTED.** The chapter is broader than the card. The boundary needs a human decision (§11, item 5).

## 10. Internal Source Defects and Conflicts — Recorded, Not Resolved

> Per protocol §10.2.2, a fully mapped genuine conflict is `RETAINED AS GENUINE SOURCE AMBIGUITY` and does not itself block source completeness. None of the following is resolved here, and none is silently adopted.

**Defect 1 — belt pouch arithmetic. VISUALLY VERIFIED ON BOTH SIDES.**

```text
printed row       Pouch, belt | Capacity 50 cn | 5 sp | 2*      (leaf n68)
printed footnote  "...the encumbrance includes both the item's
                   encumbrance and the encumbrance of the goods
                   within it. Thus, a fully filled belt pouch has
                   an encumbrance of 55 cn."                     (leaf n68)

2 + 50 = 52, not 55.
```

The rule and its own worked example disagree by 3 cn. Both are on the same page. `RETAINED AS GENUINE SOURCE AMBIGUITY` — a Stage-B/human problem, not evidence of unfinished inspection.

**Defect 2 — "Clothes, plain" carries the wrong footnote marker. VISUALLY VERIFIED.**

The Adventuring Gear Table prints `20***` for Clothes, plain, while Clothes middle-class, fine and extravagant all print `20**`/`30**`. Footnote `***` is the **quiver** footnote and is meaningless for clothing; footnote `**` ("encumbrance if packed; if the clothes are worn, disregard the encumbrance") is plainly the applicable one. Recorded as a **typographic defect in the printed source**, not as a rule that plain clothes behave like quivers.

**Defect 3 — Suit Armor movement override.** Recorded in full in `CHAR-005-evidence.md` §10, since the conflict is with the Chapter 6 encumbrance table. `CHAR-004`'s contribution is the visually verified `Enc 750 cn` value.

**Defect 4 — free starting kit stated twice, differently.** Ch. 1 p. 8 "no possessions except for normal clothes and a little money" versus Ch. 4 p. 62's enumerated clothes + shoes + belt + belt-pouch. Compatible in direction, not identical in content. Material because a belt-pouch and shoes have printed encumbrances (2\* and 8\*\*) that a starting character would carry without paying for them. Recorded as an audit-class-I divergence.

## 11. Open-Question Closure Inventory (protocol §10.2)

| # | Open statement | Source region implicated | Inspection completed? | Result | Owner | Still blocks completeness? |
|---|---|---|---|---|---|---|
| 1 | Nets Table not visually verified | RC p. 65 | ~~No~~ → **YES, 2026-09-14 (Stage-A closure)** | **CLOSED.** Visually verified at leaf n64: three columns (`Victim's Size \| Equivalent* \| Net Size**`), seven rows, two footnotes — **exactly as previously recorded from OCR.** Footnote `**` *"Or equivalent in square feet"* is the linkage to Weapons Table note `n` (1 sp and 1 cn **per square foot**), and RC's own worked example (medium 6′×6′ = 36 sq ft → 36 sp, 36 cn) is consistent with the Medium row. Footnote `*` calibrates the categories to PC races. **No new mechanic, no contradiction, no new dependency** | `CHAR-004` / `COMBAT-003` | **No** — closed |
| 2 | Riding Animal Costs and Land Transportation Gear Tables not visually verified | RC p. 70 | No | Deliberate: mount/vehicle scope is itself unsettled (item 5). Recorded as located and uninspected | pending item 5 | **Yes, if mounts are ruled in scope** |
| 3 | Ch. 2 class entries not read as complete entries for weapon/armour permissions | RC pp. 13–31 | ~~No~~ → **YES, remediation pass 1** | ~~Deliberately stopped at the cluster boundary~~ → **CLOSED.** All nine entries read as complete entries (box + Class Details) and all nine boxed blocks visually verified. Five classes carry class-entry-only restrictions; one carries a pricing rule. Remediation §2, §4 | `CHAR-009` (proposed) / **human governance** | **No longer blocks on inspection.** Now a pure ownership decision — see remediation §9 |
| 4 | Ch. 10 high-level character creation not re-inspected for a wealth/equipment provision | RC pp. 129–131 | ~~No~~ → **YES, remediation pass 1** | ~~Not re-opened here~~ → **CLOSED, and it was not empty.** Steps 5, 7 and 8 supply a different money rule (1% of XP), equipment by grant, an alternate cash method, two magic-item methods, a price table, and the only RC owned-vs-carried distinction. Remediation §5.4 | `CHAR-001` §5 / `CHAR-004` / **human governance** | **No longer blocks on inspection.** Now an ownership/V1-scope decision |
| 5 | Whether `CHAR-004` extends to mounts, vehicles, ships and siege equipment | RC Ch. 4 pp. 70–74 | Partially (land transport read; water and siege not) | Scope question, not a source question | **Human governance** | **Yes** — the answer determines whether items 2 and the water/siege exclusions are legitimate |
| 6 | General Index (p. 302) not swept as a completeness locator | RC Appendix 4 | ~~No~~ → **YES, remediation pass 1** | **CLOSED.** Swept in full and every relevant reference followed. It produced the decisive `Weapon restrictions 14, 17, 19, 21, 23, 25, 26, 28, 29` entry — nine class pages, **Chapter 4 absent** — and confirmed there is no `Armor restrictions` entry at all. Remediation §5.3 | `CHAR-004` | **No** — audit class H discharged |

**Items 3, 4, 5 and 6 are unfinished source inspection, not ambiguity, and are declared as such.** Item 5 additionally requires a human scope decision that no amount of further reading can supply. Consistent with protocol §10.2, this packet therefore **does not** claim completeness, and the independent completeness reviewer is asked to treat these six rows as the starting point rather than the conclusion.

## 12. Alternate-Source Research Requirement (protocol §15)

**Not established, and not permitted on the current evidence.** RC supplies explicit, tabulated cost and encumbrance values for every catalog it contains, an explicit money procedure, and an explicit procedure for items it does not list. The two defects in §10 are **internal source conflicts**, which protocol §10.2.2 routes to human/Stage-B resolution — not gaps, and therefore not a licence for gap-directed alternate-source research.

No precise RC gap statement is written, because no RC gap has been established.

## 13. Possible Simulator Ruling Areas (named, not drafted)

- The belt-pouch arithmetic in §10 Defect 1, **if** human review finds no reading that reconciles 52 and 55 and no alternate-source completion applies.
- The plain-clothes footnote marker in §10 Defect 2, if the obvious typographic reading is not accepted.

Neither is drafted, bundled, proposed, or self-approved. Both are named only.

## 14. Legacy Rule Card Withholding (protocol §13)

**Not applicable.** `CHAR-004` is `Unresearched` in `docs/rules/INVENTORY.md`; no prior `CHAR-004` Rule Card exists in this repository, and none was consulted. The card is not `REVALIDATION_REQUIRED`.

## 15. Access Limitations Encountered

- The archive.org OCR renders hyphenated line breaks as `¬` and flattens multi-column tables into a single run. Every mechanically significant table in §6's verification list was therefore read from page images, not from OCR.
- OCR corrupted several values that visual verification corrected — for example the Terrain Effects on Movement Table's `1 1/2 normal` appeared as `1 F2 normal` (recorded in `EXP-003-evidence.md`), and the Weapons Table's Torch cost appeared as `'/6`.
- The IIIF endpoint serves crops reliably; the Browser pane's `zoom` region-crop action is unavailable in this environment, so each close reading required a separate IIIF request. This slowed verification but did not prevent it.
- The General Index (p. 302) was not swept — see §11 item 6.

## 16. Confidence Assessment

| Area | Confidence | Basis |
|---|---|---|
| Starting money procedure | **High** | Two independent RC presentations, numerically identical, both read in full |
| Catalog structure, costs, encumbrance values | **High** | Six mechanically significant tables visually verified against the printed page |
| Derived-encumbrance cases (nets, whips, containers, worn clothing) | **High** | Stated in visually verified notes and footnotes |
| Unlisted-item procedure | **High** | Single explicit Ch. 13 provision |
| Free starting kit | **Moderate** | Two non-identical statements; §10 Defect 4 |
| Purchase legality / class permissions ownership | **Low as a boundary; high as source text** | RC's content is clear; *which card owns it* is unsettled (§9 Challenge 1) |
| Mounts, vehicles, ships, siege | **Not assessed** | Deliberately excluded pending the scope decision in §11 item 5 |

## 17. Recommendation

Per protocol §11.19, exactly one token applies to this packet. Four rows of the §11 closure inventory are **unfinished source inspection**, which §10.2 forbids carrying past a completeness claim:

```text
MORE PRIMARY RESEARCH REQUIRED
```

The outstanding work is bounded and named: §11 items 3, 4 and 6, plus items 2 and 5 conditional on a human scope decision. **This packet is not blocked on access, and not blocked on ambiguity** — it is blocked on inspection it declares rather than conceals.

**Cluster-level status of this packet:**

```text
PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
```
