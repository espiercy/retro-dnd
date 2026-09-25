# CLUSTER-003 — Independent Second-Pass Catalog Transcription Review

**Scope:** the executable equipment catalogs in `src/rules/character_creation/equipment.py`
(`WEAPONS`, `AMMUNITION`, `ARMOR`, `ADVENTURING_GEAR`, and the derived / non-row entries).

**Reviewer status:** I am an **independent second-pass reviewer**. I did **not** author the
transcription under review, and this document is **not** a re-certification of the author's
self-check. Every value below was compared against the *D&D Rules Cyclopedia* page images
directly. No production code or test was modified by this review; no test suite was run; no
rules question was adjudicated here.

**Branch reviewed:** `cluster-003-stage-a-evidence`.
**Date:** 2026-09-25.

---

## 1. Primary-source evidence base

Per `DEC-0010` ("OCR text and full-text search are locators, not proof of coverage"), every
finding below rests on **visual inspection of page images**, not OCR.

### Pages verified VISUALLY (full page render)

| Printed page | Leaf | Content verified | Legible? |
|---|---|---|---|
| **62** | `leaf61.jpg` | Money section; complete **Weapons Table** (all 42 printed item rows, all columns) | Yes |
| **63** | `leaf62.jpg` | **Weapons Table (Notes)** a/c/m/n/r/s/t/v/w/HH/2H/S/M/L; **Ammunition Table** (all 7 rows); Enc-column footnote; Ammunition prose | Yes |
| **65** | `leaf64.jpg` | **Nets Table** (7 rows + 2 footnotes); Net description; Polearm/Poleaxe/Pike/Halberd descriptions | Yes |
| **67** | `leaf66.jpg` | **Armor Table** (7 rows, AC/Cost/Enc/Notes) + footnotes `*`, `D`, `S`, `T` | Yes |
| **69** | `leaf68.jpg` | **Adventuring Gear Table** (all 38 printed rows) + footnotes `*`, `**`, `***`; gear prose | Yes |

### Magnified crops additionally read VISUALLY (to defeat small-type misreads)

| Crop | Source | What it confirmed |
|---|---|---|
| `notea.jpg` | p. 63 | Note `a` verbatim, including "blowgun: 5 darts" and "5 darts equal 1 cn" |
| `torchrow.jpg` | p. 62 | Weapons-Table Torch cost glyph `1/6`; Dagger rows |
| `otherrow.jpg` | p. 62 | Other Weapons block: Net `n`/`n`, Rock `1/10`, Sling `2`, Whip `1/ft` / `10/ft` |
| `wnotes1.jpg` | p. 62 (IIIF, leaf 61, pct:60,18,32,40) | Cost / Enc / **Notes** columns, Axes → Trident, at ~4x |
| `wnotes2.jpg` | p. 62 (IIIF, leaf 61, pct:60,56,32,38) | Cost / Enc / **Notes** columns, Shield Weapons → Whip, at ~4x |
| `armortbl.jpg` | p. 67 (IIIF, leaf 66) | Armor Table note markers `D`, `D,T`, `S` per row |
| `ammotbl.jpg` | p. 63 (IIIF, leaf 62) | Ammunition Table header wording and Blowgun/Dart row `5 / 1 / 5` |
| `gear1.jpg` | p. 69 | Gear rows Backpack → Holy symbol, incl. `50+gp` / `30**` |
| `gear2.jpg` | p. 69 | Gear rows Hat or cap → Tinder box, incl. `2*`, `5***`, `1*`, `5*`, `8**` |

### Pages I could NOT verify

**None.** Every page required by the review scope was read visually at full-page resolution,
and every value flagged as a trouble spot was additionally read from a magnified crop. The
IIIF endpoint returned intermittent 504s; all crops above were nevertheless obtained.

### Note on a moving target

The module was **being edited by another session while this review ran**. Row-level source
values below are stable and reviewer-verified regardless. Where the "implemented value" column
describes code, it describes the file **as of the final read in this session**, and the three
rows under active remediation are marked `[REMEDIATION]`.

---

## 2. WEAPONS — RC p. 62, Weapons Table

Printed item rows on p. 62: **42**. Catalogued as `Item` objects: **40** (39 fixed-price
weapon rows + the shared `TORCH` object). Net and Whip are built by `net()` / `whip()`.

Columns compared: item name/label, cost, denomination/notation, Enc (cn), size (S/M/L),
note codes. (Damage and Range are deliberately out of scope — COMBAT-\*.)

| catalog | item | implemented value(s) | RC page/table | result | notes |
|---|---|---|---|---|---|
| WEAPONS | Axe, Battle | 7 gp / 60 cn / M / r,2H | p.62 Weapons | MATCH | |
| WEAPONS | Axe, Hand | 4 gp / 30 cn / S / t | p.62 Weapons | MATCH | |
| WEAPONS | Bow, Short | 25 gp / 20 cn / M / a,m,2H | p.62 Weapons | MATCH | |
| WEAPONS | Bow, Long | 40 gp / 30 cn / L / a,m,2H | p.62 Weapons | MATCH | |
| WEAPONS | Crossbow, Lt | 30 gp / 50 cn / M / a,m,s,2H | p.62 Weapons | MATCH | abbreviation "Lt" as printed |
| WEAPONS | Crossbow, Hvy | 50 gp / 80 cn / L / a,m,s,2H | p.62 Weapons | MATCH | abbreviation "Hvy" as printed |
| WEAPONS | Blackjack | 5 gp / 5 cn / S / c,r,s | p.62 Weapons | MATCH | |
| WEAPONS | Club | 3 gp / 50 cn / M / c,r | p.62 Weapons | MATCH | |
| WEAPONS | Hammer, Throwing | 4 gp / 25 cn / M / c,t | p.62 Weapons | MATCH | |
| WEAPONS | Hammer, War | 5 gp / 50 cn / M / c,r | p.62 Weapons | MATCH | |
| WEAPONS | Mace | 5 gp / 30 cn / M / c,r | p.62 Weapons | MATCH | |
| WEAPONS | Staff | 5 gp / 40 cn / M / c,r,w,2H | p.62 Weapons | MATCH | |
| WEAPONS | **Torch** (weapon form) | `QuantityPrice` offers 1→2 sp, 6→1 gp; `printed_unit_notation="1/6 gp"`; 20 cn / S / c,r | p.62 Weapons | MATCH `[REMEDIATION]` | **RC prints `1/6` in a `Cost (gp)` column, Enc `20`, Notes `c,r,S`** — visually confirmed at ~4x in `wnotes1.jpg` and `torchrow.jpg`. `1/6 gp` = 16⅔ cp; RC names no unit below cp (p.62 conversions: 1 gp = 100 cp). Reviewer confirms the printed notation is preserved, not replaced. |
| WEAPONS | Dagger, Normal | 3 gp / 10 cn / S / t,w | p.62 Weapons | MATCH | printed under group header "Daggers:" as "Normal" |
| WEAPONS | Dagger, Silver | 30 gp / 10 cn / S / t,w | p.62 Weapons | MATCH | printed as "Silver" |
| WEAPONS | Halberd | 7 gp / 150 cn / L / s,2H | p.62 Weapons | MATCH | |
| WEAPONS | Javelin | 1 gp / 20 cn / M / t | p.62 Weapons | MATCH | |
| WEAPONS | Lance | 10 gp / 180 cn / L / s,v | p.62 Weapons | MATCH | |
| WEAPONS | Pike | 3 gp / 80 cn / L / s,v,2H | p.62 Weapons | MATCH | |
| WEAPONS | Polearm | 7 gp / 150 cn / L / s,2H | p.62 Weapons | MATCH | spelling "Polearm" (one word) as printed |
| WEAPONS | Poleaxe | 5 gp / 120 cn / L / s,2H | p.62 Weapons | MATCH | spelling "Poleaxe" (one word) as printed |
| WEAPONS | Spear | 3 gp / 30 cn / L / t,v | p.62 Weapons | MATCH | size **L**, verified at 4x |
| WEAPONS | Trident | 5 gp / 25 cn / M / s,t | p.62 Weapons | MATCH | |
| WEAPONS | Shield, Horned | 15 gp / 20 cn / S / s | p.62 Weapons | MATCH | |
| WEAPONS | Shield, Knife | 65 gp / 70 cn / S / s | p.62 Weapons | MATCH | |
| WEAPONS | Shield, Sword | 200 gp / 185 cn / M / s,v | p.62 Weapons | MATCH | |
| WEAPONS | Shield, Tusked | 200 gp / 275 cn / L / s,2H | p.62 Weapons | MATCH | |
| WEAPONS | Sword, Short | 7 gp / 30 cn / S / r | p.62 Weapons | MATCH | printed as "Short" under "Swords:" |
| WEAPONS | Sword, Normal | 10 gp / 60 cn / M / r | p.62 Weapons | MATCH | |
| WEAPONS | Sword, Bastard, One-Handed | 15 gp / 80 cn / L / r,HH | p.62 Weapons | MATCH | **"Bastard" is printed as an unpriced group header with two indented sub-rows** ("One-Handed", "Two-Handed"). Both sub-rows carry cost 15 / Enc 80 and differ in damage (1d6+1 vs 1d8+1) and note (HH vs 2H). Both are catalogued; the header itself is correctly **not** catalogued. |
| WEAPONS | Sword, Bastard, Two-Handed | 15 gp / 80 cn / L / r,2H | p.62 Weapons | MATCH | see above |
| WEAPONS | Sword, Two-Handed | 15 gp / 100 cn / L / 2H | p.62 Weapons | MATCH | printed notes are `2H,L` only — **no `r`**; code correctly omits `r` |
| WEAPONS | Blowgun, up to 2' | 3 gp / 6 cn / S / a,m,s,w | p.62 Weapons | MATCH | label "Blowgun, up to 2'" as printed |
| WEAPONS | Blowgun, 2' + | 6 gp / 15 cn / M / a,m,s,w,2H | p.62 Weapons | MATCH | label "Blowgun, 2' +" as printed (space before `+`) |
| WEAPONS | Bola | 5 gp / 5 cn / M / s,t | p.62 Weapons | MATCH | |
| WEAPONS | Cestus | 5 gp / 10 cn / S / s | p.62 Weapons | MATCH | |
| WEAPONS | Holy Water | 25 gp / 1 cn / S / c,s,t,w | p.62 Weapons | MATCH | capitalised "Holy Water" in Weapons Table vs "Holy water" in Gear Table; both appear, both as printed — two separate catalog rows, correct |
| WEAPONS | **Net** | `net(side)`: 1 sp/sq ft, 1 cn/sq ft; traits s,t,w; **size = None** | p.62 Weapons + p.63 note `n` | **SOURCE-AMBIGUOUS** | Cost and Enc cells both print the literal `n`. Note `n` (p.63) states the rate and the worked example (6'×6' → 36 sp = 3.6 gp, 36 cn) — code MATCHES both. **But the printed Notes cell is `s,t,w,M or L`** — a *dual* size that `WeaponSize` cannot express. The code drops it silently and, unlike its other two withholdings, does **not** document the omission. Needs human escalation: either record the raw printed marker neutrally, or record the withholding. |
| WEAPONS | **Whip** | `whip(ft)`: 1 gp/ft, 10 cn/ft; size M; traits s,w | p.62 Weapons | MATCH (values) | Printed: Cost `1/ft`, Enc `10/ft`, Notes `s,w,M`. Values correct. See DEFECT-1 for the accompanying docstring error. |
| WEAPONS | Oil, Burning | 2 gp / 10 cn / S / c,s,t,w | p.62 Weapons | MATCH | |
| WEAPONS | Rock, Thrown | 10 cp / 10 cn / S / c,t,w | p.62 Weapons | MATCH | printed `1/10` in the `Cost (gp)` column; 1/10 gp = 10 cp exactly (p.62: 1 gp = 100 cp) |
| WEAPONS | **Sling** | 2 gp / 20 cn / S / c,m,w — **no `a` trait** | p.62 Weapons + p.63 note `a` | **SOURCE-AMBIGUOUS** | The Sling row's printed Notes are **`c,m,w,S` — it does NOT carry note `a`** (verified at 4x, `wnotes2.jpg`). But note `a`'s own text names *"sling: 30 stones"* as a normal load. RC is internally inconsistent. The code reproduces the row faithfully (no `a`) **and** lists `"Sling": 30` in `STANDARD_LOAD_SHOTS`, making that entry unreachable: `missile_weapon_encumbrance` refuses any weapon lacking `a`. Needs human escalation; not a transcription fix. |

### Weapons Table cost-notation summary (reviewer-verified glyphs)

| Printed cell | Row | Exact printed form |
|---|---|---|
| Cost | Torch | `1/6` (small fraction glyph, in a `Cost (gp)` column) |
| Cost | Rock, Thrown | `1/10` (small fraction glyph) |
| Cost | Whip | `1/ft` (italic) |
| Cost | Net | `n` |
| Enc | Net | `n` |
| Enc | Whip | `10/ft` |
| Cost | Sling | `2` **set in italic** where all neighbouring integers are roman. No note attaches to it and the value is an ordinary 2 gp; recorded here only so a later reader does not mistake it for a marker. |

### Weapons Table note codes — printed text (RC p. 63), for the record

| Code | Printed meaning (abridged) | Code's enum member |
|---|---|---|
| `a` | normal load of ammunition already included in the weapon's Enc (bow: 20 arrows; crossbow: 30 quarrels; sling: 30 stones; blowgun: **5 darts**); 2 arrows = 1 cn, 3 quarrels = 1 cn, 5 sling stones = 1 cn, 5 darts = 1 cn; long bow without arrows = 20 cn; light crossbow without quarrels = 40 cn | `AMMUNITION_INCLUDED` |
| `c` | "Clerics may use this weapon. Druids may, too, if they can find a form of this weapon with no metal or stone parts." | `CLERIC_PERMITTED` |
| `m` | "Missile weapon; never used as a melee weapon." | `MISSILE_ONLY` |
| `n` | "A **net's** cost and encumbrance are based on its size." (rate + 6'×6' example) | *(no member — documented)* |
| `r` | can be thrown, but rarely; only Expert-or-greater weapon mastery may throw it in combat | `RARELY_THROWN` |
| `s` | has special features; read the weapon description | `SPECIAL_FEATURES` |
| `t` | hand weapon that may also be thrown | `THROWN` |
| `v` | may be set vs. a charge | `SET_VS_CHARGE` |
| `w` | magic-users may use at the DM's discretion | `MAGIC_USER_DISCRETIONARY` |
| `HH` | usable one- or two-handed; two-handed use behaves like a 2H weapon but keeps individual initiative; small races **can** use it | `HAND_OR_TWO_HANDED` |
| `2H` | two hands; no shield; loses individual initiative; small races **cannot** use it | `TWO_HANDED` |
| `S` / `M` / `L` | Small / Medium / Large weapon | `WeaponSize` |

All 13 codes are accounted for. No code is invented, and no code is missing.

---

## 3. AMMUNITION — RC p. 63, Ammunition Table

Printed rows: **7**. Implemented: **7**. Columns: Weapon, Type of Ammunition,
**Standard Load (# of Shots)**, **Cost (gp)**, **Enc (# of shots per cn)**.

| catalog | item | implemented value(s) | RC page/table | result | notes |
|---|---|---|---|---|---|
| AMMUNITION | Dart | weapon Blowgun; load **5**; 1 gp; **5** shots/cn | p.63 Ammunition | MATCH `[REMEDIATION]` | **Confirms 5, not 3.** Verified twice: the Ammunition Table row reads `5 / 1 / 5` (magnified, `ammotbl.jpg`), and note `a` reads "blowgun: **5 darts**" and "5 darts equal 1 cn" (magnified, `notea.jpg`). Internally coherent: 5 darts ÷ 5 per cn = exactly 1 cn, and Blowgun (up to 2') Enc 6 − 1 = 5 cn bare. |
| AMMUNITION | Arrow | Bow; 20; 5 gp; 2/cn | p.63 Ammunition | MATCH | |
| AMMUNITION | Silver-tipped arrow | Bow; **1**; 5 gp; 2/cn | p.63 Ammunition | MATCH | load of 1 is printed; prose confirms silver arrows are "sold by the arrow, rather than in batches of 20 or 30" |
| AMMUNITION | Quarrel | Crossbow; 30; 10 gp; 3/cn | p.63 Ammunition | MATCH | |
| AMMUNITION | Silver-tipped quarrel | Crossbow; **1**; 5 gp; 3/cn | p.63 Ammunition | MATCH | |
| AMMUNITION | Stone or lead pellet | Sling; 30; 1 gp; 5/cn | p.63 Ammunition | MATCH | full printed label "Stone or lead pellet" preserved |
| AMMUNITION | Silver pellet | Sling; **1**; 5 gp; 5/cn | p.63 Ammunition | MATCH | |
| AMMUNITION | *(column semantics)* | `shots_per_cn`, inverse rate | p.63 header | MATCH | Header printed verbatim as `Enc (# of shots per cn)`. The code's separate field name and separate type correctly prevent the flat-cn misreading. |
| AMMUNITION | *(Weapon column grouping)* | `weapon` repeated on every row | p.63 Ammunition | MATCH | RC leaves the Weapon cell blank on the silver sub-rows; the code fills it in from the group above, which is the printed grouping, not an invention. |

---

## 4. ARMOR — RC p. 67, Armor Table

Printed rows: **7**. Implemented: **7**.

| catalog | item | implemented value(s) | RC page/table | result | notes |
|---|---|---|---|---|---|
| ARMOR | Shield | 10 gp / 100 cn / `SHIELD` | p.67 Armor | MATCH | printed AC cell is `(-1)*`, i.e. a modifier not an AC — the code's separate `SHIELD` category is faithful to that |
| ARMOR | Leather Armor | 20 gp / 200 cn | p.67 Armor | MATCH | AC 7 |
| ARMOR | Scale Mail | 30 gp / 300 cn | p.67 Armor | MATCH | AC 6 |
| ARMOR | Chain Mail | 40 gp / 400 cn | p.67 Armor | MATCH | AC 5 |
| ARMOR | Banded Mail | 50 gp / 450 cn | p.67 Armor | MATCH | AC 4 |
| ARMOR | Plate Mail | 60 gp / 500 cn | p.67 Armor | MATCH | AC 3 |
| ARMOR | Suit Armor | 250 gp / **750 cn** | p.67 Armor | MATCH | AC 0; 750 confirmed at 4x |

### Armor note codes D / T / S — printed assignment and printed meaning

Requested explicitly. The code deliberately omits these; **this section reports only, and
implements nothing.** Verified at ~4x in `armortbl.jpg` and again on the full page.

| Armor row | Printed Notes cell |
|---|---|
| Shield | `D` |
| Leather Armor | `D,T` |
| Scale Mail | *(blank)* |
| Chain Mail | *(blank)* |
| Banded Mail | *(blank)* |
| Plate Mail | *(blank)* |
| Suit Armor | `S` |

Printed footnote text, verbatim in substance:

- `*` — "Subtract 1 from AC if a shield is used." *(attached to the Shield row's AC cell `(-1)*`, not to the Notes column.)*
- `D` — "A druid can use this type of armor if it contains no metal parts or other nonorganic components (parts that have never been alive)."
- `S` — "Suit armor has some very special characteristics; carefully read the description of this type of armor."
- `T` — "A thief can use this type of armor."

**Reviewer observation (not a defect):** the markers are class-permission and
description-pointer data, and the module's stated reason for omitting them (card §7 states
class permissions directly; reading them is Slice C) is coherent. If the main session chooses
to carry them, the neutral raw form is exactly the table above — `Shield: {D}`,
`Leather Armor: {D, T}`, `Suit Armor: {S}`, the other four empty. Note that `D` on the Shield
row is a *permission* marker and must not be confused with the `*` AC footnote.

---

## 5. ADVENTURING GEAR — RC p. 69, Adventuring Gear Table

Printed rows: **38**. Implemented: **37** `Item` objects — the printed "Torch" and "Torches"
rows are represented by the single shared `TORCH` object carrying both purchase offers.

| catalog | item | implemented value(s) | RC page/table | result | notes |
|---|---|---|---|---|---|
| GEAR | Backpack | 5 gp / 20 cn / CONTAINER / cap 400 | p.69 Gear | MATCH | prints `20*`; desc "Capacity 400 cn" |
| GEAR | Belt | 2 sp / 5 cn / CLOTHING | p.69 Gear | MATCH | prints `5**` |
| GEAR | Boots, plain | 1 gp / 10 cn / CLOTHING | p.69 Gear | MATCH | prints `10**` |
| GEAR | Boots, riding or swash-topped | 5 gp / 15 cn / CLOTHING | p.69 Gear | MATCH | spelling "swash-topped" verified at 4x; prints `15**` |
| GEAR | Cloak, short | 5 sp / 10 cn / CLOTHING | p.69 Gear | MATCH | prints `10**` |
| GEAR | Cloak, long | 1 gp / 15 cn / CLOTHING | p.69 Gear | MATCH | prints `15**` |
| GEAR | Clothes, plain | 5 sp / 20 cn / CLOTHING | p.69 Gear | MATCH | **prints `20***`** — the *quiver* footnote, where every sibling clothing row prints `**`. Reviewer confirms the anomalous marker is real and is on this row only. Treated as a typographic defect by the approved card with express human approval; recorded here as confirmed, not re-adjudicated. |
| GEAR | Clothes, middle-class | 5 gp / 20 cn / CLOTHING | p.69 Gear | MATCH | prints `20**`; desc "See above" |
| GEAR | Clothes, fine | 20 gp / 20 cn / CLOTHING | p.69 Gear | MATCH | prints `20**` |
| GEAR | **Clothes, extravagant** | `OpenEndedPrice(50 gp)` / **30 cn** / CLOTHING | p.69 Gear | MATCH `[REMEDIATION]` | **Printed cost is `50+gp` and printed Enc is `30**` — thirty, not twenty.** Both verified at 4x in `gear1.jpg`. This is the only clothing row whose Enc is not 20, and it is the single easiest value on the page to get wrong. Reviewer confirms 30. |
| GEAR | Garlic | 5 gp / 1 cn | p.69 Gear | MATCH | |
| GEAR | Grappling hook | 25 gp / 80 cn | p.69 Gear | MATCH | |
| GEAR | Hammer | 2 gp / 10 cn | p.69 Gear | MATCH | desc "Small"; distinct from the Weapons-Table hammers |
| GEAR | Hat or cap | 2 sp / 3 cn / **GEAR** | p.69 Gear | MATCH | prints `3` with **no** footnote marker. Correctly **not** `CLOTHING`. |
| GEAR | Holy symbol | 25 gp / 1 cn | p.69 Gear | MATCH | |
| GEAR | Holy water | 25 gp / 1 cn | p.69 Gear | MATCH | desc "Breakable vial"; lowercase "water" as printed here |
| GEAR | Iron spike | 1 sp / 5 cn | p.69 Gear | MATCH | desc "One spike" |
| GEAR | Iron spikes | 1 gp / 60 cn | p.69 Gear | **DEFECT** (see DEFECT-2) | Values correct. Printed desc is "**Twelve** spikes"; the bundle count is not carried anywhere executable, only implied by the plural name. |
| GEAR | Lantern | 10 gp / 30 cn | p.69 Gear | MATCH | desc "Burns oil" |
| GEAR | Mirror | 5 gp / 5 cn | p.69 Gear | MATCH | desc "Hand-sized, steel" |
| GEAR | Oil | 2 gp / 10 cn | p.69 Gear | MATCH | desc "One flask" |
| GEAR | Pole | 1 gp / 100 cn | p.69 Gear | MATCH | desc "Wooden, 10' long"; printed item label is "Pole" (the prose heading is "Pole, Wooden") |
| GEAR | Pouch, belt | 5 sp / **2 cn** / CONTAINER / **cap 50** | p.69 Gear | MATCH | prints `2*`, desc "Capacity 50 cn". Both inputs confirmed independently at 4x. RC's footnote `*` then states a filled total of **55**, which 2 + 50 does not give; the 52-vs-55 conflict is already recorded as `SR-6` on the approved card and is **not** re-adjudicated here. |
| GEAR | Quiver | 1 gp / 5 cn / CONTAINER / **capacity None** | p.69 Gear | MATCH | prints `5***`, desc "For arrows or quarrels". **RC prints no capacity for the quiver** — confirmed; `capacity_cn=None` is correct, and the guard in `filled_container_encumbrance` is the right consequence. |
| GEAR | Rations, iron | 15 gp / 70 cn | p.69 Gear | MATCH | desc "Preserved food for one person for one week" |
| GEAR | Rations, standard | 5 gp / 200 cn | p.69 Gear | MATCH | desc "Unpreserved food for one person for one week" |
| GEAR | Rope | 1 gp / 50 cn | p.69 Gear | MATCH | desc "50' length" |
| GEAR | Sack, small | 1 gp / 1 cn / CONTAINER / cap 200 | p.69 Gear | MATCH | prints `1*` |
| GEAR | Sack, large | 2 gp / 5 cn / CONTAINER / cap 600 | p.69 Gear | MATCH | prints `5*` |
| GEAR | Shoes | 5 sp / **8 cn** / CLOTHING | p.69 Gear | MATCH | prints `8**`; 8 confirmed at 4x |
| GEAR | Stakes (3) and mallet | 3 gp / 10 cn | p.69 Gear | MATCH | quantity is inside the printed item name |
| GEAR | Thieves' tools | 25 gp / 10 cn | p.69 Gear | MATCH | desc "Lockpicks, wire, etc."; apostrophe placement as printed |
| GEAR | Tinder box | 3 gp / 5 cn | p.69 Gear | MATCH | two words as printed; desc "Flint, steel, kindling" |
| GEAR | **Torch** | `TORCH`, offer 1 → 2 sp, 20 cn | p.69 Gear | MATCH `[REMEDIATION]` | **Printed: `Torch / One torch / 2 sp / 20`.** Verified. |
| GEAR | **Torches** | represented as `TORCH`'s 6-count offer, 1 gp | p.69 Gear | MATCH `[REMEDIATION]` | **Printed: `Torches / Six torches / 1 gp / 120`.** Verified. The printed `120 cn` is not stored as a datum; it is recovered as 6 × 20, which is exact. Reviewer notes the collapse loses no value, but the printed second row no longer has a `catalog_item("Torches")` lookup — see AMBIGUITY-3. |
| GEAR | Waterskin/wineskin | 1 gp / 5 cn empty | p.69 Gear | MATCH | printed item label uses a slash with no spaces; desc "One-quart capacity; enc 30 when filled" |
| GEAR | Wine | 1 gp / 30 cn | p.69 Gear | MATCH | desc "One quart, wineskin not included" — a distinct row from the waterskin, correctly separate |
| GEAR | Wolfsbane | 10 gp / 1 cn | p.69 Gear | MATCH | desc "One bunch" |

### Adventuring Gear footnotes — printed text, reviewer-verified

- `*` — "This is the item's encumbrance when empty. When goods are placed within it, the encumbrance includes both the item's encumbrance and the encumbrance of the goods within it. Thus, a fully filled belt pouch has an encumbrance of **55 cn**."
  Rows bearing `*`: Backpack, Pouch belt, Sack small, Sack large. **Exactly four.**
- `**` — "This is the encumbrance if packed. If the clothes are worn, disregard the encumbrance."
  Rows bearing `**`: Belt, Boots plain, Boots riding, Cloak short, Cloak long, Clothes middle-class, Clothes fine, Clothes extravagant, Shoes. **Nine.** (Clothes, plain prints `***` instead — see its row.)
- `***` — "This is the quiver's encumbrance when empty. Filled with arrows or quarrels, it is **up to 10 cn** for encumbrance. A 5-cn encumbrance quiver + 10 cn of missiles (20 arrows or 30 quarrels) still equals only a **10-cn** encumbrance bundle to carry around."
  Rows bearing `***`: Quiver, and (anomalously) Clothes, plain.

The code's `CONTAINER` set is the four `*` rows **plus the Quiver**. The `ItemCategory`
docstring defines `CONTAINER` as "carries the footnote `*` rule", which the Quiver does not.
The behaviour is nonetheless correct (the `capacity_cn is None` guard routes the Quiver away
from `*` arithmetic). Recorded as an observation, not a defect.

---

## 6. Derived and non-row entries

| catalog | item | implemented value(s) | RC page/table | result | notes |
|---|---|---|---|---|---|
| derived | `net(side_feet)` cost rate | `NET_COST_PER_SQUARE_FOOT = 1 sp` | p.63 note `n` | MATCH | "Nets cost 1 sp per square foot of surface area" |
| derived | `net(side_feet)` Enc rate | `NET_ENCUMBRANCE_CN_PER_SQUARE_FOOT = 1` | p.63 note `n` | MATCH | "an encumbrance of 1 cn per square foot" |
| derived | `net()` worked example | 6×6 → 36 sp (3.6 gp), 36 cn | p.63 note `n` | MATCH | RC's own example reproduced exactly |
| derived | `net()` squareness | square only; Nets Table sizes 2'×2' … 25'×25' | p.65 Nets Table | MATCH | Printed Net Size column: 2'X2', 4'X4', 6'X6', 9'X9', 12'x12', 16'x16', 25'X25' — all square; footnote `**` "Or equivalent in square feet." Victim's Size column (Very small … Mammoth) is correctly **not** modelled here. |
| derived | `net()` size class | `size=None` | p.62 Notes `M or L` | **SOURCE-AMBIGUOUS** | see WEAPONS/Net row and AMBIGUITY-1 |
| derived | `whip()` cost rate | `WHIP_COST_PER_FOOT = 1 gp` | p.62 Weapons, Cost `1/ft` | MATCH | the column is `Cost (gp)`, so `1/ft` is 1 gp per foot |
| derived | `whip()` Enc rate | `WHIP_ENCUMBRANCE_CN_PER_FOOT = 10` | p.62 Weapons, Enc `10/ft` | MATCH | |
| derived | `whip()` size / traits | M; s,w | p.62 Weapons, Notes `s,w,M` | MATCH | |
| derived | Torch purchase forms | 1 → 2 sp; 6 → 1 gp; unit notation `1/6 gp` preserved | p.62 + p.69 | MATCH `[REMEDIATION]` | all three printed figures confirmed |
| derived | Clothing price forms | `OpenEndedPrice(50 gp)` floor; `cost_of` raises | p.69 `50+gp` | MATCH `[REMEDIATION]` | RC states a floor and nothing else; refusing to default to the floor is faithful |
| derived | `STANDARD_LOAD_SHOTS` — Bow, Short | 20 | p.63 note `a` | MATCH | "bow: 20 arrows" |
| derived | `STANDARD_LOAD_SHOTS` — Bow, Long | 20 | p.63 note `a` | MATCH | |
| derived | `STANDARD_LOAD_SHOTS` — Crossbow, Lt | 30 | p.63 note `a` | MATCH | "crossbow: 30 quarrels" |
| derived | `STANDARD_LOAD_SHOTS` — Crossbow, Hvy | 30 | p.63 note `a` | MATCH | |
| derived | `STANDARD_LOAD_SHOTS` — Blowgun (both) | **5** | p.63 note `a` + p.63 Ammunition | MATCH `[REMEDIATION]` | both governing objects say 5; verified twice at magnification |
| derived | `STANDARD_LOAD_SHOTS` — Sling | 30 | p.63 note `a` vs p.62 Sling row | **SOURCE-AMBIGUOUS** | see AMBIGUITY-2 |
| derived | `FILLED_QUIVER_ENCUMBRANCE_CN` | 10 | p.69 footnote `***` | MATCH | "still equals only a 10-cn encumbrance bundle" |
| derived | `WATERSKIN_FILLED_ENCUMBRANCE_CN` | 30 | p.69 Waterskin row desc | MATCH | "enc 30 when filled" printed on the row itself, against 5 empty |
| derived | container capacity — Backpack | 400 | p.69 | MATCH | |
| derived | container capacity — Pouch, belt | 50 | p.69 | MATCH | |
| derived | container capacity — Sack, small | 200 | p.69 | MATCH | |
| derived | container capacity — Sack, large | 600 | p.69 | MATCH | |
| derived | container capacity — Quiver | None | p.69 | MATCH | RC prints none |
| derived | `PLAIN_CLOTHES_SETS` | (2, 3) | p.62 Money prose | MATCH | "two or three sets of plain clothes, a pair of shoes, a belt, and a belt-pouch" |
| derived | `starting_gold` | 3d6 × 10 gp | p.62 Money | MATCH | "a one-time sum of 3d6 x 10 gold pieces" |
| derived | currency conversions used | 1 gp = 10 sp = 100 cp | p.62 Money | MATCH | also 1 sp = 10 cp; 1 ep = 5 sp = 50 cp; 1 pp = 5 gp = 10 ep = 50 sp = 500 cp |
| docs | `WEAPONS` docstring, note `n` claim | "Nets **and whips** carry the note code `n`" | p.62 Notes; p.63 note `n` | **DEFECT** | see DEFECT-1 |
| docs | `_WEAPON_ROWS` inline comment | `# "Torch" is withheld …` | — | **DEFECT** | see DEFECT-3 |
| docs | `ADVENTURING_GEAR` docstring | "less the one withheld row" | — | **DEFECT** | see DEFECT-4 |

---

## 7. Summary

| Catalog | Printed rows | Implemented entries | MATCH | DEFECT | SOURCE-AMBIGUOUS |
|---|---|---|---|---|---|
| WEAPONS | 42 | 40 (+ 2 derived by `net()`/`whip()`) | 40 | 0 | 2 |
| AMMUNITION | 7 | 7 | 7 | 0 | 0 |
| ARMOR | 7 | 7 | 7 | 0 | 0 |
| ADVENTURING_GEAR | 38 | 37 | 37 | 1 | 0 |
| Derived / non-row | — | 26 reviewed | 24 | 0 | 1 (Sling; the `net()` size ambiguity is counted under WEAPONS) |
| Documentation claims | — | 3 reviewed | 0 | 3 | 0 |
| **TOTAL** | — | **120 line items reviewed** | **115** | **4** | **3** |

*(The Sling ambiguity is counted once, under WEAPONS. The `net()` size ambiguity is counted
once, under WEAPONS. The third ambiguity is AMBIGUITY-3 below.)*

**No numeric transcription error was found in any of the four catalogs.** Every cost,
denomination, encumbrance, capacity, size class, note code, shots-per-cn rate and standard
load matches the printed page. All four defects are omissions or stale prose, not wrong
numbers.

### Defects — printed value vs implemented value

1. **DEFECT-1 — `WEAPONS` docstring misstates the source about note `n`.**
   *Printed:* the Whip row's Notes cell is **`s,w,M`**; it carries **no `n`**. Note `n` (p. 63)
   reads "A **net's** cost and encumbrance are based on its size" and names only the net. The
   whip's per-foot cost and encumbrance are printed directly in its own cells (`1/ft`, `10/ft`).
   *Implemented:* the `WEAPONS` docstring asserts "Nets **and whips** carry the note code `n` —
   their cost and encumbrance are *'based on size'*". The same claim is repeated in the
   `WeaponTrait` docstring ("the code `n` … marks the two rows this module builds by
   dimension"). This is a false statement about the primary source in a module whose stated
   purpose is faithful transcription. Computed values are unaffected.

2. **DEFECT-2 — "Iron spikes" bundle quantity not transcribed.**
   *Printed:* `Iron spikes / **Twelve spikes** / 1 gp / 60`.
   *Implemented:* `_gear("Iron spikes", _GEAR, _gp(1), 60)` — the count *twelve* survives only
   as an English plural. The module now has a `QuantityPrice` type that exists precisely to
   keep a "this many for this much" pair together (used for the torch), so the omission is
   also internally inconsistent. Nothing computed is wrong; a printed datum is simply absent.

3. **DEFECT-3 — stale inline comment in `_WEAPON_ROWS` (lines ~477–478).**
   `# "Torch" is withheld: its printed cost of 1/6 gp is not a whole number of copper pieces.`
   The torch is no longer withheld; `TORCH` is catalogued and appended to `WEAPONS`. The
   comment now contradicts the code three lines above it.

4. **DEFECT-4 — stale `ADVENTURING_GEAR` docstring (line ~698).**
   "The RC Adventuring Gear Table (p. 69), **less the one withheld row**." No row is withheld
   any more — `Clothes, extravagant` is catalogued with an `OpenEndedPrice`. (The `WEAPONS`
   docstring's "less the two rows RC defines by dimension" is, separately, now inaccurate in a
   different way: only *one* row, the Net, is defined by note `n`; see DEFECT-1.)

> Defects 3 and 4 are in code the main session was actively editing during this review. They
> are reported because they were present in the file at the final read, not as a claim that
> remediation is finished.

### Ambiguities — each needs human escalation, not a transcription fix

1. **AMBIGUITY-1 — the Net's printed size class is `M or L`.**
   *Printed:* Weapons Table Net row, Notes cell: **`s,t,w,M or L`**.
   *Implemented:* `net()` returns an `Item` with `size=None` and no comment.
   `WeaponSize` cannot hold a disjunction. The module documents two other withholdings
   explicitly and this one not at all, so a reader cannot tell whether the size was withheld
   or overlooked. **A rules decision (which size a given net is, or whether the disjunction is
   carried raw) is required; this reviewer does not make it.** A neutral option is to record
   the printed marker as raw text without interpreting it, exactly as this review recommends
   for the armor `D`/`T`/`S` markers.

2. **AMBIGUITY-2 — RC contradicts itself about whether the sling has a normal load.**
   *Printed:* the Sling row's Notes cell is **`c,m,w,S` — no `a`** (verified at ~4x). But note
   `a`'s own text lists **"sling: 30 stones"** among the weapons whose normal load is already
   included, and adds "5 sling stones equal 1 cn". RC states both.
   *Implemented:* the code reproduces the row faithfully (no `AMMUNITION_INCLUDED` trait) and
   *also* registers `"Sling": 30` in `STANDARD_LOAD_SHOTS`. Because
   `missile_weapon_encumbrance` rejects any weapon lacking note `a`, that entry is
   **unreachable**: the sling can never take the varying-load path. The code therefore silently
   picks the row over the note, without saying so. **Whether the sling's printed 20 cn includes
   30 stones is an unresolved rules question and needs human escalation.** Note that RC works
   the arithmetic itself only for the long bow (30→20) and the light crossbow (50→40), never
   for the sling.

3. **AMBIGUITY-3 — the printed "Torches" row has no catalog identity.**
   *Printed:* p. 69 prints **two** adjacent rows, `Torch / One torch / 2 sp / 20` and
   `Torches / Six torches / 1 gp / 120`.
   *Implemented:* one `TORCH` object named `"Torch"`, whose `QuantityPrice` holds both offers.
   The 120 cn is recoverable as 6 × 20 and the 1 gp is an offer, so **no printed value is
   lost**; but `catalog_item("Torches")` — a name RC prints as an item — now raises
   `UnlistedItemError`. This is defensible (the card's §4.1.1 "one commodity" reading was
   human-approved) and is flagged only so the main session can decide deliberately whether a
   printed item name should fail lookup. Not a numeric defect.

### Row-count note

The task brief reported 40 / 7 / 7 / 38 rows. As of the final read:

- `WEAPONS` holds **40** entries (39 fixed-price rows + `TORCH`) — matches. *During the
  review's first read, before the torch remediation landed, it held 39.*
- `AMMUNITION` — **7**. Matches. Printed: 7.
- `ARMOR` — **7**. Matches. Printed: 7.
- `ADVENTURING_GEAR` holds **37** entries against **38** printed rows, because Torch and
  Torches are one object (AMBIGUITY-3). The brief's "38" is correct as a count of *printed
  rows* and incorrect as a count of *implemented entries*.

Cross-check of completeness: 42 printed weapon rows = 39 fixed-price rows + Torch + Net +
Whip. 38 printed gear rows = 35 `_gear()` rows + `Clothes, extravagant` + the two printed
torch rows folded into the one shared `TORCH` object (37 objects in all).
**No printed row of any of the four tables is missing from the implementation.**

---

## Disposition by the implementing session (appended 2026-09-26, after the review)

**This section was written by the implementing session, not by the independent reviewer.**
The review above is preserved unaltered; nothing in it has been edited, softened or removed.

### Defects — all four corrected

| # | Finding | Disposition |
|---|---|---|
| 1 | `WEAPONS` / `WeaponTrait` docstrings claim the whip carries note `n` | **CORRECTED.** Both docstrings now state that note `n` names the net alone, and that the whip's `1/ft` and `10/ft` rates are printed in its own cells. Test: `test_only_the_net_carries_note_n_and_the_whip_prints_its_own_rates`. No value changed |
| 2 | "Iron spikes / **Twelve spikes**" — the printed quantity was dropped | **CORRECTED.** `IRON_SPIKE` is now one commodity with the two printed offers, `1 for 1 sp` and `12 for 1 gp`, encumbrance `5 cn` per spike; the bundle's printed `60 cn` is exactly `12 x 5`. It uses the price form card §4.1 already defines. Unlike the torch it needed no adjudication — both offers are exact whole coin and there is no per-unit fraction to interpret. Test: `test_rcs_twelve_spike_bundle_row_is_the_twelve_count_offer` |
| 3 | Stale comment: `# "Torch" is withheld…` | **CORRECTED.** Deleted |
| 4 | Stale docstring: "less the one withheld row" | **CORRECTED.** Rewritten; it now states the three non-fixed-price rows and reconciles 38 printed rows to 37 entries |

### Ambiguities

| # | Finding | Disposition |
|---|---|---|
| 1 | The net's printed size is the disjunction `M or L`; `net()` sets `size=None` with no comment | **DOCUMENTED, not decided.** `net()`'s docstring now records that RC makes a net's size class follow its dimensions through the Nets Table (p. 65), that a disjunction is not a size, and that `size` is therefore left `None` rather than guessed from `side_feet`. Test: `test_a_net_carries_no_size_because_rc_prints_a_disjunction` |
| 2 | RC contradicts itself about whether the sling has an included normal load | **ESCALATED FOR HUMAN ADJUDICATION. The reviewer is right and the implementing session was wrong.** The earlier remediation had gated `missile_weapon_encumbrance` on `STANDARD_LOAD_SHOTS` and registered `"Sling": 30`, which resolved the contradiction in favour of note `a`'s text — a rules decision that was not the implementing session's to make. `"Sling"` has been **removed** from `STANDARD_LOAD_SHOTS`, and `missile_weapon_encumbrance` now refuses the sling with a message naming the conflict, the same stop-at-the-boundary treatment the blowgun had before its adjudication. Buying sling stones separately is unaffected (approved case E24). Test: `test_the_sling_is_refused_because_rc_contradicts_itself_about_its_load` |
| 3 | The printed "Torches" row has no catalog identity | **LEFT AS IS, flagged.** The one-commodity reading is what the human project owner approved on 2026-09-26 and what card §4.1.1 states, and no printed value is lost. The consequence the reviewer identifies is real and is reported to the human project owner: `catalog_item("Torches")` raises `UnlistedItemError` for a name RC prints. The same is now true of `catalog_item("Iron spikes")` |

### Armor note codes `D` / `T` / `S`

**Recorded in this artifact; deliberately NOT implemented.** The review's transcription —
`Shield: D`, `Leather Armor: D,T`, `Scale`/`Chain`/`Banded`/`Plate`: blank, `Suit Armor: S` — is
accepted as accurate. They are **not** added as row metadata, because `D` and `T` are class
permissions and CHAR-004 §7 already states those permissions directly: carrying both would
create a second authority for one rule, which the card warns against. The reviewer's separate
caution is also accepted — the `*` on Shield's `(-1)*` AC cell is an AC footnote, not a
Notes-column marker, and the two must not be conflated. No armour AC is transcribed at all.

### Net effect on the four catalogs

**No numeric transcription error was found, and none was corrected.** Every cost, denomination,
encumbrance, capacity, size class, note code, shots-per-cn rate and standard load in `WEAPONS`,
`AMMUNITION`, `ARMOR` and `ADVENTURING_GEAR` matched the printed page on independent second-pass
review. The four corrections are one dropped printed quantity and three documentation defects;
the one behavioural change is a **withdrawal** of an over-reach, not an addition.
