# Stage-A Evidence Packet — `EXP-006` Light & Exploration Resources

```text
STAGE:   A (EVIDENCE) -- DEC-0009
STATUS:  EVIDENCE READY FOR HUMAN REVIEW
CARD:    EXP-006 -- Light & Exploration Resources
SOURCE:  Dungeons & Dragons Rules Cyclopedia (TSR 1071, 1991) -- primary
```

> **No Rule Card is drafted here.** Stage B has not begun and is not authorized. Nothing
> below is a mechanical specification; §7's findings are evidence, and their synthesis into
> an executable contract is a separate, separately authorized task.
>
> Researched 2026-09-27 under `CLUSTER-004`'s human-approved boundary.

---

## 1. Headline finding

**The inventory's own source attribution for this card is wrong, and the card is
substantially narrower than its title suggests.**

`INVENTORY.md` records `EXP-006`'s RC Source as *"Dungeon Adventures chapter"*. **The Rules
Cyclopedia has no chapter by that name**, and its light material is not in any exploration
chapter. Every governing object for this card is in **Chapter 4: Equipment**, inside the
Adventuring Gear *descriptions* — the same pages `CHAR-004` was researched from.

**`EXP-006` has no governing table and no checklist.** The Index to Tables and Checklists
(p. 301) was read in full, visually: it lists **no** table or checklist for light,
illumination, torches, lanterns, vision or darkness. The General Index carries **no `Light`
entry** as a rules topic and **no `Lantern` entry** at all.

This is a **structural finding, not a research gap**: RC governs light through four item
descriptions totalling roughly two hundred words, and nothing else.

---

## 2. Source structure inspected (audit classes A, B)

### A — Table of Contents (pp. 3–4), read in full

Every chapter and sub-section heading was read. **No heading anywhere in the RC names
light, illumination, vision, darkness or exploration resources.** The chapters that could
plausibly have held such a section, and what they actually contain:

| Chapter | Sub-sections | Bearing |
|---|---|---|
| Ch. 4 Equipment (62) | Money, Weapons, Armor, **Adventuring Gear (68)**, Land Transportation, Water Transportation, Siege | **Contains every governing object** |
| Ch. 6 Movement (87) | Time, Distance, Movement, Land/Water/Aerial Travel | No light material |
| Ch. 7 Encounters and Evasion (91) | Exploration and the Game Turn, Travel and the Game Day, Encounters, Surprise, Monster Reactions, Wandering Monster Encounters, Evasion and Pursuit, Balancing Encounters | No light material |
| Ch. 13 DM Procedures (143) | 26 topics incl. Doors, Listening, Mapping, Climbing | **No light topic** |

### B — Index to Tables and Checklists (p. 301), **visually inspected in full**

Both columns of tables and the complete checklist list were read from the page image.

```text
LIGHT-BEARING TABLES OR CHECKLISTS FOUND:  NONE
```

The nearest entries are `Adventuring Gear Table . 69` (CHAR-004's, already landed) and
`Land Transportation Gear Table . 70` (out of V1). **This is the strongest available
structural evidence that RC gives light no tabular mechanic**, and it comes from the
completeness instrument precedent `P-001` exists to enforce.

### General Index (pp. 302–304)

| Entry | Pages |
|---|---|
| `Torch` | **62, 66, 69, 70** |
| `Oil` | **62, 65, 69** |
| `Infravision` | 24, 25 |
| `Light` as a rules topic | **no entry** (only `Lightship . 146` and the spells `light (C 1, MU 1)`) |
| `Lantern` | **no entry located** |

**The `Torch . 70` entry resolved a live question.** It is not a Land Transportation row —
p. 70 was inspected visually and its Land Transportation Gear Table contains only Saddle &
Tack, Saddle Bags, Cart and Wagon. `Torch . 70` is the **item description**, which sits on
p. 70 while the Lantern and Oil descriptions sit on p. 69.

---

## 3. Governing source objects (audit classes C–I)

| # | Object | Page | Class | Visually verified |
|---|---|---|---|---|
| 1 | **Torch description** | **70** | F detailed prose | **Yes** (leaf n69) |
| 2 | **Lantern description** | **69** | F detailed prose | **Yes** (leaf n68) |
| 3 | **Oil description** | **69** | F detailed prose | **Yes** (leaf n68) |
| 4 | **Tinderbox description** | **70** | F detailed prose | **Yes** (leaf n69) |
| 5 | Adventuring Gear Table rows (torch, torches, lantern, oil, tinder box) | 69 | C named table | **Yes** — **`CHAR-004`'s, landed** |
| 6 | Torch weapon description | 66 | F | Not re-verified — **`COMBAT-*`'s**, see §8 |
| 7 | Infravision (racial) | 24–25 | F | OCR read — **`CHAR-009`'s**, see §8 |
| 8 | Ethereal Plane light statement | ~264 | I duplicate presentation | OCR read — corroborative only |

### 3.1 Complete-entry inspection (§9.7)

Objects 1–4 were read **in full from the page images**, not from OCR snippets, and the
surrounding Adventuring Gear description run (Sack through Wolfsbane, and Backpack through
Rope on the preceding page) was read in full to confirm no fifth light-bearing description
was missed.

---

## 4. Mechanical findings — facts, as printed

**Recorded as source facts. No consequence is derived here** (§7 of the protocol).

### 4.1 Torch (p. 70)

> *"This is any 1' to 2' long piece of wood, its head sometimes covered with an inflammable
> substance such as pitch. It casts light in a **30' radius** and burns for **one hour (six
> turns)**. See the description from the Weapons Table for information on using a torch as a
> weapon; clerics can use it as a weapon."*

```text
illumination   30' radius
duration       one hour = SIX TURNS
```

**The parenthetical "(six turns)" is RC stating its own conversion**, and it agrees with
landed `EXP-002`'s 10-minute turn. This is RC-explicit, not a derivation.

### 4.2 Lantern (p. 69)

> *"This is a simple oil lantern that casts light in a **30' radius**, burning **one flask
> of oil in four hours (24 turns)**. Most types are shuttered or enclosed against wind."*

```text
illumination   30' radius            -- identical to a torch
duration       one flask = four hours = 24 TURNS
construction   "shuttered or enclosed against wind"
```

### 4.3 Oil (p. 69)

> *"Oil is burned in a lantern for light. A flask of oil may also be thrown as a missile
> weapon or poured out and ignited to delay pursuit."*

Oil has three printed roles. **Only the first is this card's.** The second is `COMBAT-*`'s
(the Weapons Table's `Oil, Burning` row, already catalogued by `CHAR-004`), and the third
is a direct cross-reference into **`ENC-005`** — see §8 and the `ENC-005` packet.

### 4.4 Tinderbox (p. 70) — the one die roll in the card

> *"The tinderbox is a small box containing flint, steel, and tinder (wood shavings).
> Characters use this to start any fires, be it for their camp or their torches. To use a
> tinderbox, roll **1d6**; under normal (comparatively dry) circumstances, a fire is
> successfully ignited on a result of **1 or 2**. Someone with a tinderbox may try to use it
> **once per round**."*

```text
roll        1d6
success     1 or 2         (a 1-in-3 chance)
condition   "under normal (comparatively dry) circumstances"
cadence     once per round
```

**This is the only randomised mechanic in `EXP-006`'s scope**, and it is a *relighting /
ignition* mechanic, which the authorization asked about explicitly. Note that RC qualifies
the 1-or-2 figure with *"under normal (comparatively dry) circumstances"* and **states no
other circumstance's chance** — see §9 Open Question 1.

### 4.5 Corroborating duplicate presentation (Ch. 18, Ethereal Plane)

> *"All light sources function normally (a torch or lantern shining light to **30' range**,
> magical light to greater ranges, etc.)"*

An independent restatement of the 30' figure for both items, in a different chapter. Class-I
duplicate presentation; consistent, no conflict.

---

## 5. Whole-source cross-reference pass (§9)

Searches performed over the complete OCR text, used as **locator and falsification tool
only**:

```text
"Infravision"/"infravision"  42 hits   all Ch. 2 racial / Ch. 14 monster / Ch. 18 planar
"casts light"                 1 hit    the torch description
"light in a"                  5 hits   torch, lantern, fire beetle, odic plant,
                                       Illumination scroll
"light source"                3 hits   invisibility spell, phantom monster, Ch. 18
"burns for"                   1 hit    the torch description
"30' radius"                  4 hits   torch, lantern, darkness spell, +1 monster
"Light Sources"               0 hits
"normal light"                0 hits   (the phrase appears as "normal and magical light")
"without light"               0 hits
"cannot see"                  4 hits   druid tree spell, Ch. 18, 2 monster entries
"darkness"                   37 hits   overwhelmingly the darkness spell and monsters
```

**Every light hit outside Chapter 4 belongs to another responsibility**: a spell
(`MAGIC-*`), a monster ability (`MON-*`), a magical item (`TREAS-*`), a racial ability
(`CHAR-009`), or the planar chapter (out of V1).

---

## 6. Falsification pass (§10)

The authorization set four challenges. Each was attempted as a genuine attempt to **disprove**
the current ownership assumption.

| # | Challenge | Attempt | Result |
|---|---|---|---|
| 1 | *Is there an exploration-resource mechanic that belongs to another existing card?* | Searched rations, waterskin, rope, spikes, pole, thieves' tools for exploration-time or depletion mechanics | **Yes — and it is not light.** Rations carry a **spoilage rule** (standard rations *"spoil overnight"* in a dungeon; iron rations last *"two months… up to a week in bad conditions"*). That is a resource-depletion mechanic with a time base. **It is not claimed for `EXP-006` here** — see §9 Open Question 3 |
| 2 | *Is light duration tied to a procedure currently outside scope?* | Followed "six turns"/"24 turns" to their time base | **No.** The turn is landed `EXP-002`'s and the card consumes it. No burn-tracking procedure exists in RC — there is no rule saying *when* a torch is checked or *who* decrements it |
| 3 | *Are visibility rules broader than resource use?* | Searched for any general sight/visibility rule | **No general visibility rule was located.** Vision rules that exist are the infravision racial ability, spell-induced blindness, and encounter-distance/surprise (`ENC-001`/`ENC-002`). RC states **no penalty for having no light** — see §9 Open Question 2 |
| 4 | *Does any resource introduce combat, spell, or retainer dependencies that should stay routed away?* | Followed the torch and oil weapon roles | **Yes, two, and both stay routed away.** The lit/unlit torch does 1d4 / 1d2 and interacts with Weapon Mastery (`COMBAT-002`, `CHAR-011`); burning oil is a missile weapon (`COMBAT-*`). `EXP-006` owns whether a torch is *lit*; it does not own what a lit torch does to a monster |

### 6.1 The strongest disconfirming attempt

**Hypothesis tested: "RC must have a dungeon light procedure somewhere; the researcher has
simply not found it."**

Three independent instruments were used to try to confirm that hypothesis, and all three
failed to produce one: the **TOC** (no heading), the **Index to Tables and Checklists**
(no table or checklist, visually confirmed), and the **General Index** (no `Light` rules
entry, no `Lantern` entry). A fourth check — reading the complete Adventuring Gear
description run on pp. 69–70 — found the four descriptions and no fifth.

**Recorded per §9.1 as a negative finding with its basis stated**, not as a bare claim of
absence: *three structural instruments and a complete-entry read of the governing section
located no light rules outside the four item descriptions.*

---

## 7. Primary-Source Coverage Checklist (§9.3)

| Requirement | Status |
|---|---|
| Relevant TOC sections inspected | **Yes** — complete TOC read; four candidate chapters checked |
| Tables Index entries inspected | **Yes — visually, in full**, p. 301 |
| Named tables inspected | Adventuring Gear Table (p. 69) — **`CHAR-004`'s**; Land Transportation Gear Table (p. 70) — excluded, out of V1 |
| Structured stat blocks | **N/A** — no stat block governs light |
| Chapter sections read in full | Ch. 4 Adventuring Gear descriptions, pp. 69–70, complete run |
| Cross-references followed | *"See the description from the Weapons Table"* → p. 66 (routed to `COMBAT-*`); *"delay pursuit"* → `ENC-005`; *"six turns"/"24 turns"* → landed `EXP-002` |
| Appendices / index entries | **Yes** — Index to Tables and Checklists **visually**; General Index via OCR |
| Visual verification | **pp. 69, 70, 301** verified from page images |
| Deliberately excluded, with reason | Ch. 18 planar light (out of V1); `light`/`continual light`/`darkness` spells (`MAGIC-*`); Illumination scroll and light-bearing magical items (`TREAS-*`); fire beetle and odic glands (`MON-*`); Land Transportation Gear Table (out of V1) |

### 7.1 One coverage item not completed visually

**The General Index (pp. 302–304) was read via OCR, not from page images** — repeated IIIF
region requests for those leaves returned HTTP 504. The Index to Tables and Checklists
(p. 301), which is the mechanically load-bearing completeness instrument here, **was**
verified visually.

Per §9.1, the General Index negatives above are therefore recorded as **"not located by the
searches performed"**, not as positive claims of absence. **This does not trigger §9.2's
`STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED`**: that gate governs *mechanically
significant objects*, and no mechanically significant object for this card went unverified.
Flagged here so a reviewer can close it if they wish.

---

## 8. Ownership and dependency findings

### 8.1 The `CHAR-004` seam — no duplication, and none proposed

The boundary is already decided and is **not reopened**. Both cards read the same two
printed pages, and they read different things from them:

| Fact | Page | Owner |
|---|---|---|
| Torch cost (`2 sp`; six for `1 gp`), encumbrance `20 cn` | 69 **table** | **`CHAR-004`** — landed, `TORCH` with `QuantityPrice` |
| Lantern cost `10 gp`, encumbrance `30 cn` | 69 **table** | **`CHAR-004`** — landed |
| Oil cost `2 gp`, encumbrance `10 cn` | 69 **table** | **`CHAR-004`** — landed |
| Tinder box cost `3 gp`, encumbrance `5 cn` | 69 **table** | **`CHAR-004`** — landed |
| Torch **30' radius, six turns** | 70 **description** | **`EXP-006`** |
| Lantern **30' radius, 24 turns per flask** | 69 **description** | **`EXP-006`** |
| Oil **as lantern fuel** | 69 **description** | **`EXP-006`** |
| Tinderbox **1d6, ignites on 1–2, once per round** | 70 **description** | **`EXP-006`** |

**The split is the source's own**: the table carries price and weight, the description
carries behaviour. **No duplication was found** — RC does not state radius or burn time in
the table, and does not state cost or encumbrance in the descriptions. Landed `CHAR-004`
already records the seam in its §A: *"Light-source radius and burn duration → `EXP-006`.
This card owns torch and lantern cost and encumbrance only."*

### 8.2 Dependencies

| Direction | Card | Nature |
|---|---|---|
| **Consumes** | `EXP-002` **[LANDED]** | The turn. RC states burn time in hours **and turns**; the turn is EXP-002's |
| **Routes away** | `COMBAT-*` | Lit/unlit torch damage (1d4 / 1d2); burning oil as a missile |
| **Routes away** | `CHAR-011` | Weapon Mastery treats torch mastery as club mastery |
| **Routes away** | `MAGIC-*` | `light`, `continual light`, `darkness` spells |
| **Routes away** | `TREAS-*` | Illumination scroll; light-bearing magical items |
| **Routes away** | `MON-*` | Fire beetle glands; odic; monster light/darkness |
| **Interacts with** | `CHAR-009` | *"Infravision does not work in the presence of normal and magical light"* (p. 24) — a **light-source consequence** whose vision ability is CHAR-009's. Recorded, not claimed |
| **Cross-references** | `ENC-005` | Oil *"poured out and ignited to delay pursuit"* |

**No retainer (`CHAR-006`) dependency was found**, and none is implied: RC nowhere says a
retainer carries the light.

---

## 9. Open questions

**Every question is either closed with its reason, or explicitly retained** (§10.2).

### Retained — require human decision

1. **RC states the tinderbox's ignition chance only for *"normal (comparatively dry)
   circumstances"* and gives no other figure.** Wet, windy or magical circumstances have no
   stated chance. **`PRIMARY PROCEDURE NOT YET ESTABLISHED` for non-normal circumstances.**
   No number may be invented; whether V1 models only the normal case is a scoping decision.
2. **RC states no consequence for having no light.** Radius and duration are given; no rule
   says what a party without illumination can or cannot do in a dungeon. Searched for and
   not located. **This is the single largest apparent gap in the card**, and it may be
   deliberate DM delegation rather than an omission — RC delegates comparably elsewhere
   (climbing, racial-armour penalties). **Not resolved here.**
3. **Do rations belong to `EXP-006`?** The card's title says *"& Exploration Resources"*.
   Rations carry a real depletion rule (spoilage). **No ownership is claimed or proposed** —
   this is a boundary question for the human project owner, and answering it inside Stage A
   would be exactly the silent scope expansion `AGENTS.md` §3 forbids.
4. **Is a burn-tracking procedure in scope at all?** RC gives durations but **no procedure**
   for decrementing them, no statement of who tracks them, and no rule for what happens at
   expiry. Whether `EXP-006` owns an executable depletion contract, or only the durations,
   is a scoping decision.

### Closed, with the reason

5. ~~Does RC have a light rules section?~~ **Closed — no.** Three structural instruments
   and a complete-entry read (§6.1).
6. ~~Is the `Torch . 70` index entry a Land Transportation row?~~ **Closed — no.** p. 70
   inspected visually; that table holds only Saddle & Tack, Saddle Bags, Cart, Wagon.
7. ~~Does the lantern's *"shuttered or enclosed against wind"* imply a wind mechanic?~~
   **Closed — no mechanic located.** Descriptive; no rule, roll or condition attaches.
8. ~~Do torch and lantern radii differ?~~ **Closed — they do not.** Both `30'`, stated
   independently on two pages and corroborated in Ch. 18.

---

## 10. Provenance candidates (for Stage B, not decided here)

| Element | Likely classification |
|---|---|
| Torch `30'` / six turns; Lantern `30'` / 24 turns per flask; Tinderbox 1d6, 1–2, once per round; oil as lantern fuel | **Rules Cyclopedia Explicit** |
| "one hour = six turns", "four hours = 24 turns" | **RC Explicit** — RC states both the hours and the turns itself |
| Any consequence of unlit exploration | **None available.** Would require a Simulator Ruling or a human scope decision — §9 Q2 |
| Any non-normal tinderbox chance | **None available** — §9 Q1 |

**No Simulator Ruling is proposed.** `AGENTS.md` §10.7 and protocol §16 place rulings last,
after gap-directed alternate-source research, and **no alternate-source research is
requested by this packet** (§11).

---

## 11. Alternate-source research

**None performed, and none requested.**

RC is explicit for everything this card's title's core actually covers. The two genuine
gaps (§9 Q1, Q2) are **not yet established as RC gaps in the sense §15 requires** — Q2 in
particular may be deliberate DM delegation, and the protocol is explicit that a gap
statement may not rest on keyword-search exhaustion. **If the human project owner rules that
V1 needs a no-light consequence, that is the point at which a `DEC-0011` authorization
should be considered — not before.**

AD&D remains excluded.

---

## 12. Adversarial self-review (§10.1.1)

Performed by the original researcher. **This is not the independent review.**

| Challenge to myself | Answer |
|---|---|
| Did I assume the card was broad because its title is broad? | **Initially, yes.** The title says *"& Exploration Resources"* and the inventory says *"Dungeon Adventures chapter"*. Both proved wrong about the source. I have recorded the rations question as **open** rather than resolving it either way |
| Did I treat a failed search as absence? | **No** — §6.1 states the three instruments used and §7.1 records the one instrument I could not verify visually |
| Did I verify the mechanically significant objects visually? | **Yes** — pp. 69, 70, and the Tables Index p. 301 |
| Did I reopen `CHAR-004`? | **No.** §8.1 records the seam and claims nothing the landed card owns |
| Did I follow the oil→pursuit cross-reference too far? | Followed only far enough to establish ownership; the pursuit procedure itself is researched in the `ENC-005` packet, which is separately authorized |
| Is my "no light rules section" claim over-stated? | It is stated as *"located no light rules outside the four item descriptions"* with the instruments named. I believe it is correct; **the independent reviewer should attack it first** |

---

## 13. Independent completeness review (§10.1.2)

```text
REQUIRED -- may NOT be performed by the original researcher
RESULT:   see docs/rules/evidence/CLUSTER-004-stage-a-completeness-review.md
```

---

## 14. Addendum — General Index visual verification completed (2026-09-27)

**Added after §1–§13 were drafted, and recorded as an addendum rather than folded in, so
the order of discovery stays visible.**

§7.1 recorded that the General Index had been read by OCR only, because repeated IIIF
requests for those leaves returned HTTP 504. **Two of the three leaves were subsequently
obtained and inspected visually**, which upgrades the packet's central negative finding
from *"not located by the searches performed"* to **visually confirmed** for the ranges
covered.

| Page | Range | Status | Result |
|---|---|---|---|
| **302** | A–H | **Visually verified** | No `Darkness` entry. `Adventuring gear . 68-70`, `Exhaustion . 88`, `Exploration . 91` confirmed |
| **303** | H–S | **Visually verified** | **No `Lantern` entry. No `Light` entry.** The L run reads `Ladder`, `Lair`, `Lance`, `Land transportation`, `Land travel`, `Languages`, `Lawful alignment`, `Leadership factor`, `Leather armor`, `Lifeboat`, `Lightship . 146`, `Listening . 147`, `Longship`, `Lost . 89`, `Lost spell book`, `Lowlife` — and stops. `Oil . 62, 65, 69` and `Infravision . 24, 25` confirmed |
| **304** | S–Z | **Not obtained** | Contains the `Torch` entry. Still OCR-only |

### 14.1 What this changes

**§1's headline finding is now stronger, not weaker.** The absence of a `Light` rules entry
and of any `Lantern` entry is confirmed from the printed index page, alongside the
visually verified Index to Tables and Checklists. Three of the four structural instruments
§6.1 relies on are now visual.

**The one remaining OCR-only item is the `Torch . 62, 66, 69, 70` entry** on p. 304 — and
all four of those pages were themselves inspected, two of them visually, so nothing rests
on the index line alone.

### 14.2 One new cross-reference located

`Rations . 69` — the index points rations only at the gear page, with no rules-section
entry. **This does not resolve §9 Q3**, which remains a scoping question for the human
project owner, but it does confirm that rations have no governing section of their own
either.
