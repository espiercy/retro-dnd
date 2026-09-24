# Rule Card: Encumbrance & Movement Rate

## Rule ID

`CHAR-005`

## Title

Encumbrance & Movement Rate

## Status

`AWAITING_APPROVAL`

> **Drafted 2026-09-24.** Stage-A evidence (`docs/rules/evidence/CHAR-005-evidence.md`) passed independent `DEC-0010` completeness review; `DEC-0011` BECMI gap research and its remediation are complete; the human project owner issued the governing adjudications on 2026-09-24.
>
> **This card is the authoritative owner of the numerical character movement rate** — normal, encounter and running — including encumbrance derivation, the Mystic level-dependent `MV`, and the movement effect of conditions whose causation is owned elsewhere. `CHAR-009` may *reference* Mystic movement but **must not** be a second implementation owner.
>
> **This card carries three Simulator Rulings — `SR-8`, `SR-9`, `SR-10`** — and **two determinations that are explicitly NOT Simulator Rulings** (Q4 running speed; Q6 exact fractional encounter movement). That distinction is load-bearing and is preserved throughout.
>
> **Approval of this card would not authorize implementation.** `CLUSTER-003` implementation is **NOT AUTHORIZED**. The Pre-Code Gate has not been begun for this cluster.
>
> **`READY FOR HUMAN RULE-CARD REVIEW`.**

## Rules Domain

`character_creation`

---

## Rules Cyclopedia Source

| Page | Object | Bearing | Visually verified |
|---|---|---|---|
| Ch. 6 p. 88 | **Character Movement Rates and Encumbrance Table** | The governing object: six `cn` bands → normal / encounter / running | **Yes** (leaf n87) |
| Ch. 6 p. 88 | "Character Movement Rates" prose | `cn` = *"weight **and awkwardness**"*; `1 cn ≈ 1/10 lb`; the `120' (40')` baseline; worked example `600 cn → 90' (30')` | — |
| Ch. 6 p. 88 | "Normal, Encounter, and Running Speeds" | Normal = feet/**turn**; encounter = **⅓** normal, feet/**round**; running = the normal *number*, feet/**round**, = 3 × encounter | — |
| Ch. 6 p. 88 | "Important Note" | *"Groups of characters, if they intend to stay together, move at the rate of the **slowest** character."* | — |
| Ch. 6 p. 88 | "Exhaustion" | 30-round running limit; 3-turn rest; forced-fight and forced-run consequences | — |
| Ch. 6 p. 87 | "Distance" / "Feet vs. Yards" | Indoors feet; outdoors the same numbers as yards | — |
| **Ch. 8 p. 103** | **"Movement"** (combat sequence) | Normal speed is **never** used in the combat sequence; encounter speed permits attacks; running forbids them; free vs. costly actions; standing up | **Yes** (leaf n102) |
| Ch. 2 p. 31 | **Mystic Special Abilities Table, `MV` column** | Level-dependent `120'` → `320'` | **Yes** (leaf n30) |
| Ch. 2 p. 31 | `MV` legend | *"First level mystics move as fast as any other **unarmored** characters…"* | — |
| Ch. 4 p. 67 | Armor prose | Racial-armour penalty is **DM-discretionary** | — |
| Ch. 4 p. 68 | Suit Armor entry | `Enc 750 cn`; the contested *"movement rate is `30' (10')`"* | **Yes** |
| Ch. 13 p. 150 | **"Special Character Conditions"** | Blindness, stunning, prone movement effects | **Yes** (leaf n149) |
| Ch. 13 p. 150 | **Starvation Table**, `Movement Rates` column | The contested `×3/4 / ×1/2 / ×3/4` progression | **Yes** (leaf n149) |
| Ch. 6 p. 89 | "By Swimming (and Drowning)" | Swim rate = ⅕ outdoor running speed; `>400 cn` drags a swimmer down | — |
| Ch. 6 p. 88 | "Monster Movement Rates" | Monster/animal encumbrance is a **separate two-band system**, Ch. 14 | — |

## Rules Cyclopedia Explicitly Establishes

1. **The encumbrance → movement table** (p. 88), visually verified:

| `Enc (cn)` | Normal Speed (feet per turn) | Encounter Speed (feet per round) | Running Speed (feet per round) |
|---|---|---|---|
| 0–400 | 120 | 40 | 120 |
| 401–800 | 90 | 30 | 90 |
| 801–1,200 | 60 | 20 | 60 |
| 1,201–1,600 | 30 | 10 | 30 |
| 1,601–2,400 | 15 | 5 | 15 |
| 2,401+ | 0 | 0 | 0 |

2. **The unit.** `cn` measures *"weight **and awkwardness**"*, not mass alone; `1 cn ≈ 1/10 pound`.
3. **The three rates and their time units.** Normal per **turn**; encounter = normal ÷ 3 per **round**; running = the normal *number* per **round** = 3 × encounter.
4. **Distance units.** Indoors feet; outdoors the same numbers read as yards.
5. **The group rule.** A party staying together moves at its **slowest** member's rate.
6. **The running limit and exhaustion.** 30 rounds maximum; then rest **at least 3 turns**. Forced to fight unrested: monsters gain **+2** to hit and the character subtracts **2** from damage (minimum 1). Forced to keep running: drops to **encounter speed**.
7. **The combat-sequence boundary** (Ch. 8 p. 103): *"A character's normal speed is **never used** during the combat sequence."*
8. **The Mystic `MV` progression** (p. 31): `120'` at 1st level rising to `320'` at 16th, by level.
9. **Condition movement effects** (Ch. 13 p. 150): blindness, stunning, prone, starvation — values in §7.
10. **Suit Armor's encumbrance:** `750 cn`.

## Rules Cyclopedia Leaves Undefined / Ambiguous

Narrowly, and only these four:

1. **Suit Armor.** `750 cn` falls in the `401–800` band → `90' (30')`, while the item's own description states `30' (10')` — the `1,201–1,600` band. RC supplies **no override language** in either direction and no rule for composing the special rate with additional carried weight. → **`SR-8`**.
2. **Running speed, stated twice.** Ch. 6 says running is the normal *number* per round; Ch. 8 p. 103 says *"(3 × normal movement)"* in a bullet list whose preceding bullet uses *"normal movement"* for the **per-turn** value. Read literally the two differ by a factor of 3. → **Q4 — resolved as an interpretation, not a ruling.**
3. **Mystic `MV` × encumbrance.** RC gives the Mystic a level-dependent `MV` and separately states that *"any character"* moves `120' (40')` unless weighed down. It never composes them. → **`SR-9`**.
4. **Starvation movement column.** The printed progression is non-monotonic: `×3/4 → ×1/2 → ×3/4`, while rest hours and attack penalties both worsen monotonically. → **`SR-10`**.

**Not ambiguous, recorded to prevent re-raising:** the **racial-armour movement penalty** is not an unquantified gap. RC states *"The DM **can** impose penalties…"*, offering an unquantified movement reduction as an example of a penalty the DM **may elect**. RC delegates it by design; this card treats it as a **DM-discretionary input** and quantifies nothing.

---

## Alternate-Source Completion Research

Performed under `DEC-0011`, authorized for four of this card's questions. Record: `docs/rules/evidence/CLUSTER-003-becmi-gap-research.md`. Nine BECMI core source units enumerated and dispositioned; remediation 1 applied after an independent review found a missed precedence object.

| Question | BECMI finding | Classification |
|---|---|---|
| **Running speed** | Five governing objects across three structural units. The Expert Rulebook's worked pursuit example — war horse `180'/turn` = `60'/round`, pursuit `180'/round` — establishes that the `3 ×` operation applies to the **per-round** value. Basic's table is **identical to RC's**, including the `Running Speed` column | **`A` — BECMI resolves the RC defect** |
| **Suit Armor** | Master Players' Book prints `750 cn` **and** *"movement rate is 30 feet per turn"*; Basic's table — identical to RC's — puts `750 cn` at `90'`. **The contradiction is inherited, not introduced by RC.** Master Players' Book p. 2 states: *"If you discover a contradiction between this set and previous sets, the rules given here should be used"*, so **BECMI resolves its own conflict in favour of the `30'` value** | **`B` — BECMI supports one RC reading** |
| **Mystic `MV` × encumbrance** | The BECMI Mystic is a **monster** in the Master DM's Book, optionally promotable to a PC; RC preserves its sixteen `MV` values exactly. BECMI states **no** relationship to the encumbrance bands and gives no worked example. RC's *"as fast as any other unarmored characters"* gloss is an **RC-era addition with no BECMI ancestor** | **`E` — BECMI silent** |
| **Starvation** | **No starvation table exists in any BECMI core source unit.** The sole ancestor is one Expert Rulebook sentence naming four effects — more rest, **traveling slower**, Hit-roll penalties, hit-point loss — the four RC table columns, **with no numbers** | **`E` — BECMI silent** |

## Compatibility Analysis

| Candidate | Vocabulary (`SOURCE_HIERARCHY.md` §6) | Imported? |
|---|---|---|
| BECMI `SPEED VS. ENCUMBRANCE TABLE` | **Preserved** — RC carries it forward unchanged, including column semantics | **Not an import.** RC states it; BECMI confirms continuity and disambiguates Ch. 8 |
| BECMI Master-set precedence resolution of Suit Armor | **Conflicting with the RC framework as a resolution mechanism** | **NOT IMPORTED.** Its instrument is scoped to boxed sets; the RC is a single volume with no such structure. See `SR-8` |
| A BECMI Mystic-encumbrance composition rule | **Does not exist** | Nothing to import |
| A BECMI starvation multiplier | **Does not exist** | Nothing to import |
| BECMI's printed Mystic `320'(80')` | **Defective** — `80'` is ⅓ of `240'`, not `320'`; BECMI's own convention is otherwise 3:1 | **NOT IMPORTED.** RC already drops the parenthetical |

**No `Alternate-Source Compatible Completion` is claimed by this card.**

---

## Simulator Ruling

### `SR-8` — Suit Armor has no special movement rate

**Ruling.** **Do not apply the Suit Armor-specific `30' (10')` rate.** Suit Armor contributes its printed **`750 cn`** to total character encumbrance, and movement is then determined normally from the standard table (§3). A character whose **total** encumbrance is exactly `750 cn` therefore moves **`90' (30')`**. Additional carried weight continues to affect movement through the ordinary system.

**Rationale, recorded honestly.** The `30'` value is **not** an unsupported number:

```text
BECMI Master Players' Book  "movement rate is 30 feet per turn"
BECMI Basic table           750 cn -> 90 feet per turn
BECMI Master p. 2           "If you discover a contradiction between
                             this set and previous sets, the rules
                             given here should be used."

=> Within BECMI, the 30' value WINS.
```

The ruling declines to follow it anyway, for reasons that are about the simulator rather than about history:

1. **BECMI's precedence rule does not govern the RC.** Its trigger names *"this set and previous sets"*; the RC is a later single-volume compilation with continuous chapters and no boxed-set structure, and it carries no precedence rule of its own.
2. **Neither RC nor BECMI supplies a rule for composing `30' (10')` with additional carried weight.** A suit-armour wearer also carries other gear; no source says what happens then.
3. **Preserving it would require inventing a mechanic** — either a general "specific equipment movement overrides general encumbrance" framework, or proportional scaling — and would make ordinary encumbrance behave incoherently for exactly one item.

**Reading rejected.** That the Suit Armor line is a flat override. **Not taken**, despite having genuine historical ancestry and despite BECMI's own rule selecting it.

**Constraint this ruling imposes:**

```text
Do NOT invent a generic "specific equipment movement overrides
general encumbrance" rule.
Do NOT create proportional scaling for Suit Armor.
Suit Armor is 750 cn for movement/encumbrance purposes, and
nothing else.
```

### `SR-9` — Mystic enhanced `MV` is gated on the unencumbered band

**Ruling.** The Mystic's level-dependent enhanced `MV` applies **only while the Mystic remains in the ordinary normal-movement encumbrance state** — that is, while total encumbrance would leave an ordinary character at `120'`.

If total encumbrance enters **any** band that would reduce an ordinary character below `120'`, the enhanced `MV` **no longer applies**, and movement is read directly from the standard table (§3).

```text
total encumbrance <= 400 cn   ->  use the Mystic MV for the level  (SS6)
total encumbrance >  400 cn   ->  use the standard table row       (SS3)
```

**Rationale.** RC gives the Mystic exceptional increasing movement but **no** composition rule with encumbrance. The class description frames the increase **relative to ordinary unarmored movement**, and the class is built around remaining lightly equipped — no armour and no protective magical devices, with source language about personal possessions that the source's own rules do **not** mechanically enforce. The adopted interpretation treats exceptional Mystic mobility as a **benefit of remaining sufficiently unburdened**.

**Readings rejected.** Proportional scaling of `MV` under encumbrance, **and** Mystic immunity to encumbrance. Both were coherent and available; the ruling takes neither. It is a **threshold**, not a curve and not an exemption.

**Constraints:**

```text
Do NOT proportionally scale Mystic MV under encumbrance.
Do NOT make the Mystic immune to encumbrance.
Later-edition Monk design was considered only as comparative evidence
that this interpretation is coherent. It is NOT implementation
authority and MUST NOT appear as mechanical provenance.
Do NOT convert the Mystic "personal possessions" flavour into an
ownership restriction.
```

### `SR-10` — Starvation movement progression is `×3/4 → ×1/2 → ×1/4`

**Ruling.** The final `×3/4` entry in the RC Starvation Table is a **printed defect**. The progression for the three worsening starvation states is:

```text
25%-49% of hp lost to starvation    x 3/4
50%-74%                             x 1/2
75%-99%                             x 1/4      [SR-10; RC prints x 3/4]
```

The `0%–24%` band remains **No Penalty**, as printed.

**Rationale.** The printed progression would make the most severely starved character move **faster** than in the preceding state, while every other column continues to worsen (rest 6→8→10→12 hours; attack penalty none→−2→−4→−6). BECMI establishes only the **qualitative** progression — more rest, **slower travel**, attack penalties, hit-point loss — and supplies **no numerical multipliers**. BECMI therefore confirms the *direction* of worsening movement but cannot supply the missing value. `×1/4` preserves both the evident quarter-step progression and monotonic worsening.

**Reading rejected.** That the printed `×3/4` governs. **Not taken** — and this is the ruling that overrides a **visually verified printed value**, so it is flagged as such rather than presented as a transcription fix.

## Human-Approved Variant

**Not applicable.** None of the three rulings deviates from a coherent explicit RC rule; each adjudicates between RC statements that cannot all be true simultaneously, or fills a composition RC never states.

---

## Approved Mechanical Specification

### 1. Inputs

```text
total carried encumbrance   integer cn      from CHAR-004
character class and level   from CHAR-002 / ADV-*
active conditions           from their owning cards (SS7)
setting                     indoors | outdoors
```

### 2. Total encumbrance

The sum of the `Enc (cn)` of every **carried** item, as supplied by `CHAR-004`. Worn clothing contributes `0`; a filled container contributes container **plus** contents; Suit Armor contributes `750` (**`SR-8`**) and nothing else.

### 3. Base movement from encumbrance

```text
band(enc):
      0 <= enc <=   400  ->  normal 120,  encounter 40,  running 120
    401 <= enc <=   800  ->  normal  90,  encounter 30,  running  90
    801 <= enc <= 1,200  ->  normal  60,  encounter 20,  running  60
  1,201 <= enc <= 1,600  ->  normal  30,  encounter 10,  running  30
  1,601 <= enc <= 2,400  ->  normal  15,  encounter  5,  running  15
  2,401 <= enc          ->  normal   0,  encounter  0,  running   0
```

Normal is **feet per turn**; encounter and running are **feet per round**.

### 4. The three rates and their relationship

```text
normal speed      N   feet per TURN
encounter speed   N / 3   feet per ROUND
running speed     N       feet per ROUND   ( = 3 x encounter speed )
```

**Q4 — the Chapter 8 restatement.** RC Ch. 8 p. 103's *"(3 × normal movement)"* is interpreted in the historically evidenced sense of **three times the per-round (encounter) rate**, not three times the per-turn number:

```text
40' encounter movement x 3 = 120' running movement per round
```

This **preserves the Ch. 6 table**. It is classified **`Rules Cyclopedia Explicit` interpretation/correction, reinforced by `Necessary Mechanical Consequence`** and by BECMI lineage evidence. **It is not a Simulator Ruling** and must not be summarised as one.

### 5. Scale boundary (Ch. 8 p. 103)

```text
normal speed     NEVER used during the combat sequence
encounter speed  may be moved in full AND still attack that round
running speed    may be moved only if not already engaged in combat,
                 and the character CANNOT attack that round
```

Free actions (e.g. drawing a weapon) do not subtract from the movement score; the DM may deduct movement for more complicated manoeuvres. Standing up after a fall costs an action in a combat round.

### 6. Mystic level-dependent `MV`

**Gate (`SR-9`):**

```text
if total encumbrance <= 400 cn   ->  Mystic MV applies (table below)
else                             ->  use SS3 exactly, as an ordinary character
```

**Values** (RC Ch. 2 p. 31, visually verified) — normal speed, feet per turn:

| Level | `MV` | Level | `MV` |
|---|---|---|---|
| 1 | 120′ | 9 | 200′ |
| 2 | 130′ | 10 | 210′ |
| 3 | 140′ | 11 | 220′ |
| 4 | 150′ | 12 | 240′ |
| 5 | 160′ | 13 | 260′ |
| 6 | 170′ | 14 | 280′ |
| 7 | 180′ | 15 | 300′ |
| 8 | 190′ | 16 | 320′ |

16 is the Mystic's maximum level; the table is complete for V1.

**Derived rates while `MV` is active:**

```text
encounter speed = MV / 3       EXACT. Retain fractional thirds.
running speed   = MV           feet per round   [derived -- see SS6.1]
```

**Q6 — exact fractional retention.** BECMI's printed `320' (80')` is an **inherited source defect** and is **not imported**: `80'` is exactly ⅓ of `240'`, not of `320'`; BECMI's convention is otherwise unbroken 3:1; BECMI supplies no separate Mystic encounter formula and no rounding convention; and RC drops the defective parenthetical entirely.

| `MV` | Encounter speed |
|---|---|
| 120′ | **40′** |
| 130′ | **43⅓′** |
| 140′ | **46⅔′** |
| 210′ | **70′** |
| 320′ | **106⅔′** |

```text
Do NOT round up. Do NOT round down. Do NOT round to nearest whole foot.
```

The ⅓ relationship is **`Rules Cyclopedia Explicit`**; exact fractional retention is the **`Necessary Mathematical Consequence`** of applying it. **Neither is a Simulator Ruling.**

**Architecture constraint.** The authoritative movement allowance may remain rational/fractional internally. **Any later snapping or conversion to discrete map or grid units is a separate spatial execution / presentation concern and must not silently change the authoritative rate.** No such conversion is specified by this card.

#### 6.1 One derivation flagged for human confirmation

The rulings specify the Mystic's **normal** movement (`SR-9`) and **encounter** movement (Q6). They do **not** explicitly address **running** movement. §4's general rule, applied to the Mystic's normal speed, gives `running = MV feet per round`. This is classified **Necessary Mechanical Consequence**, and is **flagged rather than assumed** — see Open Questions 1.

### 7. Condition movement effects

**This card owns the numerical movement effect. It does NOT own how or why a condition was acquired** — causation stays with the condition's owning card (human ownership Decision 5, 2026-09-14).

| Condition | Movement effect | Source |
|---|---|---|
| **Blindness**, unguided, travelling far | **⅓** normal speed, and that speed is measured in **feet**, indoors *or* outdoors | RC Ch. 13 p. 150 Explicit |
| **Blindness**, guided by a sighted character | **⅔** normal rate; measured in yards outdoors | RC Ch. 13 p. 150 Explicit |
| **Blindness**, mounted with someone else guiding the horse | **No penalty** | RC Ch. 13 p. 150 Explicit |
| **Stunned** | **⅓** the normal movement rate **for whatever speed is being attempted** | RC Ch. 13 p. 150 Explicit |
| **Prone → standing** | costs **one round of movement** (Ch. 13) / **an action in a combat round** (Ch. 8 p. 103) | RC Explicit ×2 — see Open Questions 2 |
| **Starvation**, 0–24% hp lost | **No Penalty** | RC Explicit |
| **Starvation**, 25–49% | **× 3/4** | RC Explicit |
| **Starvation**, 50–74% | **× 1/2** | RC Explicit |
| **Starvation**, 75–99% | **× 1/4** | **`SR-10`** — RC prints `× 3/4` |

### 8. Group movement

```text
A party that intends to stay together moves at the rate of its
SLOWEST member.
```

### 9. Running limit and exhaustion

```text
running may be sustained at most 30 rounds (5 minutes)
then: EXHAUSTED

exhausted -> must rest at least 3 turns (30 minutes) before running
             or fighting again

exhausted and forced to fight without rest:
    monsters gain +2 to attack rolls against the character
    the character subtracts 2 from all damage rolls
    a successful hit still inflicts at least 1 point

exhausted and forced to keep running:
    drops to ENCOUNTER speed; cannot move faster until rested
```

The optional **Endurance** general skill extends the limit — owned by `CHAR-012`, **not specified here**.

### 10. Distance units

```text
indoors   the table's numbers are FEET
outdoors  the same numbers are read as YARDS
```

### 11. Explicitly not modelled by this card

```text
racial-armour penalty     DM-discretionary input; RC delegates by design.
                          This card quantifies NOTHING.
swimming                  1/5 outdoor running speed; >400 cn drags a
                          swimmer down. Water-travel responsibility.
monster / animal / vehicle
  encumbrance             a separate TWO-BAND system (Ch. 14). NOT this
                          card's six-band character system.
spatial quantisation      separate concern -- SS6.
```

---

## Scope Boundaries

### A. What this card does **not** own

- Item `Enc` values → **`CHAR-004`**. This card consumes a total.
- Spending the rate against the dungeon turn → **`EXP-003`**.
- Turn/round time accounting → landed **`EXP-002`**.
- **Causation** of blindness, stunning, starvation → their owning cards.
- Exhaustion's **combat penalties** as combat mechanics → `COMBAT-002`/`003`. This card records them because they are the consequence of a movement choice.
- Halfling save vs. paralysis in oversized armour → `COMBAT-004`.
- Endurance skill → `CHAR-012`.
- Suit Armor's surprise effects → `ENC-002`.
- **Mystic class abilities generally** → `CHAR-009`, which **may reference** `MV` but must not re-specify it.

### B. Source location versus ownership

The Mystic `MV` values are printed in **RC Chapter 2**, inside the class entry. **Source location and canonical ownership are distinct**: the provenance is preserved, and the authoritative numerical rule is this card's.

---

## Deterministic Test Cases

### The encumbrance table — bands and boundaries

| # | Input | Expected |
|---|---|---|
| M1 | `0 cn` | `120' (40')`, running `120'` |
| M2 | `400 cn` — upper boundary | `120' (40')` |
| M3 | `401 cn` — lower boundary | `90' (30')` |
| M4 | `800 cn` | `90' (30')` |
| M5 | `801 cn` | `60' (20')` |
| M6 | `1,200 cn` | `60' (20')` |
| M7 | `1,201 cn` | `30' (10')` |
| M8 | `1,600 cn` | `30' (10')` |
| M9 | `1,601 cn` | `15' (5')` |
| M10 | `2,400 cn` | `15' (5')` |
| M11 | `2,401 cn` | `0' (0')` — immobile |
| M12 | `10,000 cn` | `0' (0')` |
| M13 | `600 cn` (RC's own worked example) | `90' (30')` |
| M14 | negative or non-integer `cn` | **ERROR** |

### Rate relationships (Q4)

| # | Input | Expected |
|---|---|---|
| M15 | normal `120'` → encounter | `40'` per round |
| M16 | normal `120'` → running | **`120'` per round** — *not* `360'` |
| M17 | `encounter × 3` | equals running, at every band |
| M18 | normal `90'` → encounter / running | `30'` / `90'` |
| M19 | normal `15'` → encounter / running | `5'` / `15'` |
| M20 | **Ch. 8 `"3 × normal movement"` applied** | resolves to `3 × encounter`, never `3 × per-turn number` |

### Scale boundary (Ch. 8 p. 103)

| # | Input | Expected |
|---|---|---|
| M21 | normal speed requested **during the combat sequence** | **ERROR / refused** — never used in combat |
| M22 | move full encounter speed, then attack | both permitted in the same round |
| M23 | move full running speed, then attack | **attack refused** |
| M24 | run while already engaged in combat | **refused** |

### Suit Armor (`SR-8`)

| # | Input | Expected |
|---|---|---|
| M25 | **Suit Armor alone, total `750 cn`** | **`90' (30')`** — the `401–800` band. Must **not** be `30' (10')` |
| M26 | Suit Armor + `100 cn` of gear = `850 cn` | `60' (20')` — ordinary banding continues |
| M27 | Suit Armor + `500 cn` = `1,250 cn` | `30' (10')` — reached by **encumbrance**, not by an item rule |
| M28 | **Any request for a Suit Armor-specific movement rate** | **ERROR** — no such rate exists |
| M29 | **Any generic "equipment overrides encumbrance" pathway** | **MUST NOT EXIST** — guard test |
| M30 | Suit Armor encumbrance value | exactly `750 cn`; no scaling, no proportional adjustment |

### Mystic `MV` gate (`SR-9`)

| # | Input | Expected |
|---|---|---|
| M31 | Mystic L1, `0 cn` | `120'` normal |
| M32 | Mystic L10, `0 cn` | **`210'`** normal |
| M33 | Mystic L16, `400 cn` — boundary | **`320'`** normal — `MV` still active |
| M34 | **Mystic L16, `401 cn`** | **`90' (30')`** — `MV` **off**; standard table. Must **not** be `320'`, and must **not** be a scaled `MV` |
| M35 | Mystic L10, `900 cn` | `60' (20')` |
| M36 | Mystic L16, `2,401 cn` | `0' (0')` — no immunity |
| M37 | **Any proportional scaling of `MV` by encumbrance** | **MUST NOT EXIST** — guard test |
| M38 | **Mystic treated as immune to encumbrance** | **MUST NOT EXIST** — guard test |
| M39 | Non-Mystic of any level, `0 cn` | `120'` — `MV` is Mystic-only |
| M40 | Mystic level above 16 requested | **ERROR** — 16 is the maximum |

### Mystic encounter movement — exact fractions (Q6)

| # | Input | Expected |
|---|---|---|
| M41 | `MV 120'` | encounter **`40'`** exactly |
| M42 | **`MV 130'`** | encounter **`130/3 = 43⅓'`** — exact rational, **not** `43`, **not** `44` |
| M43 | **`MV 140'`** | encounter **`140/3 = 46⅔'`** |
| M44 | `MV 210'` | encounter **`70'`** exactly |
| M45 | **`MV 320'`** | encounter **`320/3 = 106⅔'`** — must **not** be BECMI's defective `80'` |
| M46 | **Any rounding of a Mystic encounter rate** | **MUST NOT OCCUR** — guard test, in either direction or to nearest |
| M47 | Representation of `43⅓'` | exact rational; **not** a lossy float that changes the value |
| M48 | Mystic running speed while `MV` active, `MV 130'` | **`130'` per round** — flagged derivation, §6.1 |

### Condition effects

| # | Input | Expected |
|---|---|---|
| M49 | Blind, unguided, normal `120'` | `40'`, **measured in feet indoors *and* outdoors** |
| M50 | Blind, guided, normal `120'` | `80'`; yards outdoors |
| M51 | Blind, mounted and led | **no penalty** |
| M52 | Stunned, normal `120'` | `40'`; the ⅓ applies to **whatever speed is attempted** |
| M53 | Stunned while running at `120'`/round | `40'`/round |
| M54 | Starvation 0–24% | **No Penalty** |
| M55 | Starvation 25–49%, normal `120'` | `90'` |
| M56 | Starvation 50–74%, normal `120'` | `60'` |
| M57 | **Starvation 75–99%, normal `120'`** | **`30'`** — `× 1/4` per `SR-10`. Must **not** be `90'` |
| M58 | **Starvation multipliers are monotonic** | `3/4 > 1/2 > 1/4` — guard test |
| M59 | Card asked *why* a character is blind/stunned/starving | **ERROR** — causation is not owned here |

### Group movement

| # | Input | Expected |
|---|---|---|
| M60 | Party at `120'`, `90'`, `60'`, intending to stay together | **`60'`** |
| M61 | Party including an immobile member (`0'`) | **`0'`** |
| M62 | Party **not** intending to stay together | each member uses their own rate |

### Exhaustion

| # | Input | Expected |
|---|---|---|
| M63 | Running for 30 rounds | permitted; exhausted at the end |
| M64 | Running for 31 rounds | **refused** — the limit is 30 |
| M65 | Exhausted, rest 3 turns | may run or fight again |
| M66 | Exhausted, rest 2 turns | still exhausted |
| M67 | Exhausted, forced to fight | monsters `+2` to hit; character `−2` damage |
| M68 | Exhausted, `−2` reduces damage below 1 | **minimum 1** |
| M69 | Exhausted, forced to keep running | drops to **encounter speed** |

### Units

| # | Input | Expected |
|---|---|---|
| M70 | `90'` indoors | 90 **feet** per turn |
| M71 | `90'` outdoors | 90 **yards** per turn |

### Guard cases

| # | Input | Expected |
|---|---|---|
| M72 | **Racial-armour penalty requested as a number** | **ERROR / not specified** — DM-discretionary by RC's own design |
| M73 | Monster or mount encumbrance submitted to this card | **ERROR** — the two-band system is not this card's |
| M74 | Caller requests quantisation to 10′ map squares | **not provided** — separate spatial concern |
| M75 | Mystic *"personal possessions"* treated as an ownership limit | **MUST NOT EXIST** — guard test |
| M76 | Terrain modifier requested from this card | **ERROR** — no terrain mechanic exists here |

---

## Provenance Classification

| Element | Classification |
|---|---|
| §3 table; §4 rate definitions; §5 scale boundary; §6 `MV` values; §7 blindness, stunning, prone, and the first three starvation rows; §8 group rule; §9 exhaustion; §10 units | **Rules Cyclopedia Explicit** |
| §4 Q4 interpretation of Ch. 8's `"3 × normal movement"` | **Rules Cyclopedia Explicit interpretation/correction**, reinforced by **Necessary Mechanical Consequence**. **NOT a Simulator Ruling** |
| §6 `encounter = MV ÷ 3` | **Rules Cyclopedia Explicit** (the ratio) + **Necessary Mathematical Consequence** (exact fractional retention). **NOT a Simulator Ruling** |
| §6.1 Mystic running speed | **Necessary Mechanical Consequence** — flagged derivation |
| §M25 consequence that Suit Armor alone yields `90' (30')` | **Necessary Mechanical Consequence** of `SR-8` + the table |
| **§2/§6 Suit Armor has no special rate** | **Simulator Ruling `SR-8`** |
| **§6 Mystic `MV` encumbrance gate** | **Simulator Ruling `SR-9`** |
| **§7 starvation 75–99% = `× 1/4`** | **Simulator Ruling `SR-10`** |
| BECMI running-speed, Suit Armor, Mystic and starvation findings | **Alternate-source evidence used only to interpret a defect.** Not imported; **no Compatible Completion claimed**. BECMI's `320'(80')` explicitly **not** imported |
| §11 racial-armour penalty | **RC delegates to DM discretion by design.** Not a gap, not quantified |
| §6 spatial quantisation; §11 swimming, monster encumbrance | **Intentionally deferred / not owned here** |
| §A, §B ownership statements | **Not rules** — repository boundaries settled by human decision 2026-09-14 |

---

## Open Questions

**None block approval.**

1. **Mystic running speed while enhanced `MV` is active.** The rulings specified normal (`SR-9`) and encounter (Q6) movement and stopped. §6.1 derives running as `MV` feet per round by direct application of §4's explicit rule. **Flagged rather than assumed.** If a reviewer intends something different, say so at approval — the derivation is visible, not buried.
2. **Prone → standing is stated twice**, as *"one round of movement"* (Ch. 13 p. 150) and as *"an action in a combat round"* (Ch. 8 p. 103). Both are RC Explicit and both are recorded. They may describe the same cost in different vocabularies; they may not. **No mechanic in this card turns on the difference**, because neither statement changes a movement *rate*. Left open deliberately rather than harmonised by assumption.
3. **The rough/broken-terrain modifier presupposed by RC's Mystic Acrobatics wording is unowned**, and deliberately so. **No terrain mechanic is created from it here** — guard test M76.
4. **Spatial quantisation** of fractional movement is unspecified and unowned. Recorded so its absence is not mistaken for an omission.

**Explicitly closed, recorded so they are not re-raised:** the running-speed factor-of-3 (**resolved by Q4 as an interpretation**, not a ruling); the Suit Armor contradiction (**`SR-8`** — and note that BECMI *did* resolve it internally and the ruling still declines to follow it); Mystic `MV` × encumbrance (**`SR-9`** — previously the cluster's most likely Stage-B blocker, no longer a blocker); Mystic encounter rounding (**Q6** — no rounding rule is needed because none is applied); the starvation column (**`SR-10`**); the racial-armour penalty (**not a gap** — RC delegates by design).

**In every case the RC's internal inconsistency is unresolved and remains so. Only the simulator's behaviour is settled.**

## Approval

- Approved by: `<pending>`
- Date: `<pending>`
- Notes: `<pending>`

**Submitted contract:** the §1–§11 mechanical specification, carrying **`SR-8`**, **`SR-9`** and **`SR-10`**; treating Q4 and Q6 as **RC-explicit interpretation plus necessary consequence and not as rulings**; and asserting **no** `Alternate-Source Compatible Completion` and **no** `Human-Approved Variant`.
