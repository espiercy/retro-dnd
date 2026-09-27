# Rule Card: Dungeon Movement

## Rule ID

`EXP-003`

## Title

Dungeon Movement

> **Renamed 2026-09-14 by human governance decision.** The previous title — *"Dungeon Movement, Mapping & Special Terrain"* — is **no longer approved**. Stage-A research established that of its three named sub-responsibilities, only one is an independent RC mechanic.

## Status

`APPROVED`

> **Approved by the human project owner, 2026-09-24.** Stage-A evidence passed independent `DEC-0010` completeness review. No `DEC-0011` question was authorized for this card — none was needed.
>
> **Ratified as approved, without change to the submitted contract:** the §1–§8 mechanical specification, **carrying no Simulator Ruling**; the treatment of **mapping as owning no mechanic**; the removal of **Special Terrain** from this card's responsibilities; and the **rough/broken-terrain modifier remaining unowned** (Open Questions 1 — expressly approved; no generic terrain mechanic is to be invented).
>
> **Approval of this card does not authorize implementation.** `CLUSTER-003` implementation is **NOT AUTHORIZED** and requires separate explicit human authorization under `ARCHITECTURE.md` §15.2 step 4.
>
> **Originally drafted 2026-09-24.** Stage-A evidence (`docs/rules/evidence/EXP-003-evidence.md`) passed independent `DEC-0010` completeness review. No `DEC-0011` question was authorized for this card — none was needed.
>
> **This card carries no Simulator Ruling.** Every clause is `Rules Cyclopedia Explicit` or a necessary consequence of one. It is the simplest of the three `CLUSTER-003` cards, and that is a finding rather than an omission.
>
> **Approval of this card would not authorize implementation.** `CLUSTER-003` implementation is **NOT AUTHORIZED**. The Pre-Code Gate has not been begun for this cluster.
>
> **`READY FOR HUMAN RULE-CARD REVIEW`.**

## Rules Domain

`exploration`

---

## Rules Cyclopedia Source

| Page | Object | Bearing | Visually verified |
|---|---|---|---|
| **Ch. 7 p. 91** | **"Exploration and the Game Turn"** | The governing sentence: *"…the DM measures time in turns. Each turn represents 10 minutes; **customarily characters will travel at their normal speed during game turns**."* | — |
| **Ch. 7 p. 91** | **Game Turn Checklist** | The four-step exploration loop | — |
| Ch. 7 p. 91 | "Leaving the Game Turn" | Exit condition | — |
| Ch. 6 p. 87 | "Time" / Measurements of Game Time Table | 1 round = 10 s; 1 turn = 10 min; 1 day = 144 turns | — |
| Ch. 6 p. 87 | "Distance" / "Feet vs. Yards" / "Map Scales" | Indoors feet; dungeon maps on graph paper, **one square = 10′** | — |
| **Ch. 6 p. 88** | "Normal, Encounter, and Running Speeds" | *"…this rate includes many assumed actions—**mapping, peeking around corners, resting**, and so forth."* | — |
| **Ch. 8 p. 103** | **"Movement"** (combat sequence) | *"A character's normal speed is **never used** during the combat sequence."* — bounds this card's scale from the other side | **Yes** (leaf n102) |
| Ch. 13 p. 148 | "Mapping" | Four DM description guidelines; the `10′ × 10′` standard-corridor convention. **No die, no time cost, no failure state** | — |
| RC p. 5 | "Mapping and Calling" | Mapper and caller are **player roles**; *"the caller is just a convenience… **it's not a game rule** that players have to use"* | — |
| Ch. 17 p. 260 | "Draw the Map" | *"use graph paper (with each square normally representing a 10′ × 10′ area, **or any other scale you prefer**)"* | — |
| Ch. 17 p. 262 | Pre-Game Checklist | A fourth mapper/caller presentation; a play-setup check, **not a mechanic** | — |

**Bounding objects located and deliberately excluded:** Terrain Effects on Movement Table and Traveling Rates by Terrain Table (Ch. 6 p. 88, both **visually verified** as per-day and outdoor); the dungeon *"difficult terrain"* evasion condition (Ch. 7 p. 98); the *"cannot charge in… broken, heavy forest, jungle, mountain, swamp"* prohibition (Ch. 14 p. 153). See §Scope Boundaries.

## Rules Cyclopedia Explicitly Establishes

1. **The rate used.** During dungeon exploration, characters **customarily travel at their normal speed** (Ch. 7 p. 91).
2. **The time unit.** The **10-minute turn** — already landed and verified as `EXP-002`.
3. **The distance unit.** Indoors, **feet**.
4. **The default map scale.** Dungeon maps on graph paper, **one square = 10′** — and Ch. 17 p. 260 makes that scale explicitly **DM-variable** (*"or any other scale you prefer"*).
5. **What the rate already includes.** *"…this rate includes many assumed actions—**mapping**, peeking around corners, **resting**, and so forth."*
6. **The exploration loop** — the Game Turn Checklist, in four ordered steps.
7. **The scale boundary.** Normal speed is **never** used during the combat sequence (Ch. 8 p. 103). Normal speed is therefore the exploration-turn rate and nothing else.
8. **That mapping is a player/DM technique, not a mechanic.** Four presentations located and read in full; **none** contains a die roll, a time cost, or a failure state.
9. **That terrain does not modify movement at this card's scales.** RC Ch. 6 p. 88: *"Though it makes no difference to the combat round or the 10-minute turn, the terrain may affect the distance a party travels in a day."*

## Rules Cyclopedia Leaves Undefined / Ambiguous

**Nothing that this card must resolve.**

This is a substantive finding, not a gap in the research. Stage A inspected every structural instrument — TOC, Tables Index, General Index, the four mapping presentations, both terrain tables, Ch. 13's DM-procedures list, and Ch. 17 pp. 256–262 — and located **no** unresolved question inside this card's scope.

One RC tension sits **adjacent** to this card and is recorded rather than resolved:

- **The rough/broken-terrain modifier presupposed by RC's Mystic Acrobatics wording** (Ch. 2 p. 31 — *"cross rough, broken terrain at no modification to his movement rate… it only affects his encounter speed and running speed"*) refers to a rule RC never publishes. **It is unowned, deliberately.** This card does **not** create a terrain mechanic from it. See §Open Questions 1.

---

## Alternate-Source Completion Research

**Not applicable — the Rules Cyclopedia is fully explicit for this card's scope.**

No `DEC-0011` question was authorized for `EXP-003`, and none was needed. One incidental BECMI corroboration was encountered while researching `CHAR-005`'s running-speed question and is recorded for provenance only: the RC Ch. 6 terrain sentence appears in the BECMI Expert Rulebook p. 21 in near-identical words, which **corroborates** finding 9 above. **It is not relied upon** — RC states the rule itself.

## Compatibility Analysis

**Not applicable.** No alternate-source candidate was considered for import.

---

## Simulator Ruling

**Not applicable.** No ruling was required for any clause of this card.

## Human-Approved Variant

**Not applicable.**

---

## Approved Mechanical Specification

### 1. Inputs

```text
party normal speed      feet per turn   from CHAR-005
                                        (the party rate -- slowest member,
                                         CHAR-005 SS8)
dungeon turn            from EXP-002 [LANDED / VERIFIED]
map scale               feet per square, DEFAULT 10
                                        DM-configurable (Ch. 17 p. 260)
```

### 2. The rate used

```text
During dungeon exploration, the party moves at its NORMAL SPEED,
expressed in FEET PER TURN, measured in FEET.
```

**Not** encounter speed. **Not** running speed. Those belong to the combat sequence and to flight respectively, and are `CHAR-005`'s to define.

### 3. Distance spent per turn

```text
distance_available_this_turn = party_normal_speed      feet

squares_available = distance_available_this_turn / map_scale
                    (default map_scale = 10 feet per square)
```

For a party at `120'` normal speed and the default scale, that is **12 squares per turn**.

**The map scale is a default, not a constant.** A DM-configured scale changes the square count and **must not** change the underlying rate in feet.

### 4. What the rate already covers — and therefore must not be charged again

```text
ALREADY INCLUDED in normal speed (RC Ch. 6 p. 88):
    mapping
    peeking around corners
    resting
    "and so forth"
```

```text
CONSEQUENCE, and a hard constraint on implementation:

    Charging additional exploration time for mapping would
    DOUBLE-COUNT a cost the rate already contains.

    This card creates NO mapping time cost, NO mapping roll,
    NO mapping failure state, and NO mapping movement penalty.
```

### 5. The exploration loop (Game Turn Checklist, RC p. 91)

```text
1. WANDERING MONSTERS
   If the previous turn's check was positive, the monsters arrive now,
   at 2d6 x 10 feet in a direction of the DM's choice.
   -> leave this loop for the Encounter Checklist.
   [OWNED BY EXP-001 / EXP-002 -- LANDED]

2. ACTIONS
   The caller, or each player, declares party actions:
   movement, listening, searching, and so forth.
   -> THIS CARD OWNS ONLY THE MOVEMENT SPEND.
      Listening, searching and door-opening resolve in EXP-005/EXP-007.

3. RESULTS
   a. discoveries are announced;
   b. a newly entered area is described so the mapper can map it;
   c. an encounter diverts to the Encounter Checklist.

4. WANDERING MONSTERS CHECK
   1d6 every OTHER turn; in a dungeon, a 1 means monsters arrive at the
   start of the next turn.
   [OWNED BY EXP-001 -- LANDED]
```

**A random encounter is not automatically combat.** Steps 1 and 4 route to the **Encounter Checklist**, which begins with detection, surprise and reaction — `ENC-002`/`ENC-003`. **This card encodes no assumption that movement becomes combat** (`AGENTS.md` §5).

### 6. Scale boundary

```text
normal speed        used HERE, per 10-minute exploration turn
encounter speed     used in the combat sequence -- NOT here
running speed       used in flight -- NOT here

RC Ch. 8 p. 103: "A character's normal speed is never used during
the combat sequence."
```

The boundary runs both ways: this card does not reach into combat, and combat rates do not govern exploration turns.

### 7. Terrain

```text
Terrain does NOT modify movement at this card's scales.

RC Ch. 6 p. 88: "Though it makes no difference to the combat round
or the 10-minute turn, the terrain may affect the distance a party
travels in a day."
```

This is a **positive statement of non-application**, not an absence of evidence. **No terrain mechanic is created here.**

### 8. Exit condition

```text
The DM continues in game turns until the situation changes -- the party
reaches wilderness, an inn, a protected caravan, and so forth -- at
which point the exploration loop is left.
```

---

## Scope Boundaries

### A. Mapping

**Mapping owns no separate time procedure, roll, failure mechanic, or movement penalty** (human governance decision, 2026-09-14).

RC's four mapping presentations were located and read in full:

| Presentation | Content |
|---|---|
| RC p. 5 "Mapping and Calling" | Mapper and caller are **player roles**; the caller is *"just a convenience… not a game rule"* |
| Ch. 7 p. 91 checklist step 3b | The DM describes new areas *"so that the mapper can map it"* — a DM description obligation |
| Ch. 13 p. 148 "Mapping" | Four DM description guidelines; the `10′ × 10′` standard-corridor convention |
| Ch. 17 p. 262 Pre-Game Checklist | *"Have the players chosen a caller and a mapper?"* — a play-setup check |

**None contains a mechanic.** Ordinary dungeon movement already encompasses normal exploration behaviour such as mapping, looking and resting, per §4.

### B. Special terrain — **not this card's responsibility**

Removed from this card's scope by the 2026-09-14 governance decision. The terrain rules RC actually states remain with the procedures that govern them:

| RC text | Owner |
|---|---|
| Terrain Effects on Movement / Traveling Rates by Terrain tables (Ch. 6 p. 88) — **per-day, outdoor**, both visually verified | wilderness movement |
| Dungeon *"difficult terrain"* as an **evasion** condition (Ch. 7 p. 98) | **`ENC-005`** |
| *"A monster cannot charge in certain types of terrain: broken, heavy forest, jungle, mountain, swamp"* (Ch. 14 p. 153, with *"20 yards (20 feet indoors)"*) | **`COMBAT-*` / `MON-*`** |
| The rate modifier presupposed by Mystic Acrobatics (Ch. 2 p. 31) | **Unowned** — see §Open Questions 1 |

**No generic "special terrain" subsystem is recreated here.**

### C. What this card does **not** own

- The movement **rate** itself → **`CHAR-005`**. This card consumes it.
- Turn and round accounting → landed **`EXP-002`**.
- Wandering-monster checks → landed **`EXP-001`**.
- Surprise, encounter distance, reaction → `ENC-002`, `ENC-003`.
- Listening, searching, opening doors → `EXP-005`; traps → `EXP-007`.
- Light radius and duration → `EXP-006`.
- Evasion and pursuit → `ENC-005`.
- Party formation and marching order → **`EXP-010`**, deferred and **not** an incoming dependency: RC's mapper and caller are player conveniences, and `marching order` occurs once in the whole source, in NPC generation.
- **Spatial quantisation** of a fractional movement allowance (e.g. a Mystic's `43⅓′`) → a separate execution concern. **This card does not quantise the rate**; §3 divides by the map scale and does not round.

---

## Deterministic Test Cases

### The rate used

| # | Input | Expected |
|---|---|---|
| D1 | Party normal speed `120'` | `120` feet available this turn |
| D2 | Party normal speed `90'` | `90` feet |
| D3 | Party normal speed `0'` (immobile) | `0` feet; the party cannot advance |
| D4 | **Encounter speed offered as the exploration rate** | **ERROR** — exploration uses normal speed |
| D5 | **Running speed offered as the exploration rate** | **ERROR** |
| D6 | **Normal speed requested inside the combat sequence** | **ERROR** — Ch. 8 p. 103 |

### Map scale

| # | Input | Expected |
|---|---|---|
| D7 | `120'`, default scale | **12 squares** |
| D8 | `90'`, default scale | **9 squares** |
| D9 | `15'`, default scale | **1.5 squares** — **not rounded by this card** |
| D10 | `120'`, DM scale of `5'` per square | **24 squares**; the rate is still `120` feet |
| D11 | **A configured map scale changing the underlying rate in feet** | **MUST NOT OCCUR** — guard test |

### Mapping

| # | Input | Expected |
|---|---|---|
| D12 | Party maps as it explores | **no additional time cost** |
| D13 | **Any mapping die roll** | **MUST NOT EXIST** — guard test |
| D14 | **Any mapping failure state** | **MUST NOT EXIST** — guard test |
| D15 | **Any mapping movement penalty** | **MUST NOT EXIST** — guard test |
| D16 | Party declines to appoint a mapper or caller | permitted; neither is a game rule |
| D17 | Resting or peeking around corners during exploration | **already included** in the rate; not charged again |

### Terrain

| # | Input | Expected |
|---|---|---|
| D18 | **Any dungeon terrain modifier applied to the turn** | **MUST NOT EXIST** — guard test |
| D19 | **Any dungeon terrain modifier applied to the round** | **MUST NOT EXIST** — guard test |
| D20 | Overland terrain table applied to a dungeon turn | **ERROR** — those tables are per-day and outdoor |

### The exploration loop

| # | Input | Expected |
|---|---|---|
| D21 | Four checklist steps | executed in order |
| D22 | Positive wandering-monster check on the previous turn | monsters arrive at step 1, `2d6 × 10` feet away |
| D23 | **A wandering-monster result** | routes to the **Encounter Checklist** — **must not** initiate combat directly |
| D24 | Wandering-monster check frequency | every **other** turn, `1d6`, dungeon encounter on a `1` — delegated to `EXP-001` |
| D25 | Party enters a new area | the DM describes it so the mapper can map it |
| D26 | Listening / searching / opening a door declared at step 2 | **declared here, resolved elsewhere** (`EXP-005`/`EXP-007`) |
| D27 | Exit condition met | the exploration loop is left |

### Integration

| # | Input | Expected |
|---|---|---|
| D28 | Turn credit consumed | delegated to landed `EXP-002`; this card does not re-implement it |
| D29 | Party rate derivation | delegated to `CHAR-005` §8 (slowest member); this card does not re-derive it |
| D30 | Mystic at `MV 130'`, `0 cn`, default scale | `130` feet available; **13 squares** — the fractional-rate case flows through unaltered |
| D31 | **This card rounding or snapping a fractional rate** | **MUST NOT OCCUR** — guard test |
| D32 | `EXP-010` party formation requested | **not required** — no formation input exists |

---

## Provenance Classification

| Element | Classification |
|---|---|
| §2 rate used; §3 distance and default map scale; §4 assumed actions; §5 checklist; §6 scale boundary; §7 terrain non-application; §8 exit condition | **Rules Cyclopedia Explicit** |
| §3 squares-per-turn arithmetic | **Necessary Mathematical Consequence** of the rate and the scale |
| §4 "must not double-count mapping" | **Necessary Mechanical Consequence** of RC's own statement that the rate already includes mapping |
| BECMI corroboration of the terrain sentence | **Alternate-source evidence, corroborative only.** Not relied upon; **no Compatible Completion claimed** |
| §A mapping; §B special terrain | **Not rules** — repository responsibility boundaries settled by human decision 2026-09-14 |
| §C spatial quantisation | **Intentionally deferred / not owned here** |

**This card contains no `Simulator Ruling` and no `Human-Approved Variant`.**

---

## Open Questions

**None block approval.**

1. **The rough/broken-terrain rate modifier presupposed by RC's Mystic Acrobatics wording is unowned.** RC Ch. 2 p. 31 says a mystic may *"cross rough, broken terrain at no modification to his movement rate… it only affects his encounter speed and running speed"* — negating a rule RC never publishes. The nearest located analogue is Ch. 14 p. 153's prohibition on **charging** in broken terrain, which constrains an **action**, not a rate, and belongs to `COMBAT-*`/`MON-*`. **No terrain mechanic is created here** — guard tests D18–D19.
2. **The `10′` map square is a default, not a constant** (Ch. 17 p. 260). Recorded so a later reader does not harden it into an invariant.
3. **Spatial quantisation** of a fractional movement allowance is unspecified and unowned — see `CHAR-005` §6. This card divides by the map scale and does not round.

**Explicitly closed, recorded so they are not re-raised:** whether mapping owns a mechanic (**no** — four presentations read in full, none contains one); whether "Special Terrain" belongs to this card (**no** — removed by governance 2026-09-14); whether `EXP-010` is an incoming dependency (**no** — `DISPROVED` in Stage A and accepted by independent review); whether the overland terrain tables reach the dungeon turn (**no** — RC states the exclusion positively, and both tables are visually verified as per-day).

## Approval

- Approved by: **Human project owner**
- Date: **2026-09-24**
- Notes: Ratifies the §1–§8 mechanical contract. **This card owns no Simulator Ruling** — every clause is `Rules Cyclopedia Explicit` or a necessary consequence of one. Mapping owns no separate time procedure, roll, failure mechanic or movement penalty; Special Terrain is not this card's responsibility; the unpublished Mystic Acrobatics terrain modifier **remains unowned by express approval**. Implementation is not authorized by this approval.

**Submitted contract:** the §1–§8 mechanical specification, carrying **no Simulator Ruling**, **no `Alternate-Source Compatible Completion`** and **no `Human-Approved Variant`** — every clause `Rules Cyclopedia Explicit` or a necessary consequence of one.
