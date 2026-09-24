# Cluster 3: Equipped Dungeon Movement

## 1. Cluster ID

`CLUSTER-003`

## 2. Name

Equipped Dungeon Movement

## 3. Status

```text
STAGE A (EVIDENCE)     COMPLETE -- RC primary + DEC-0010 completeness PASS
DEC-0011 (BECMI)       COMPLETE -- seven authorized questions,
                       remediation 1 applied
HUMAN ADJUDICATION     COMPLETE -- 2026-09-24, seven determinations
                       (SR-6 .. SR-10, plus two non-rulings)
STAGE B (SYNTHESIS)    COMPLETE -- three Rule Cards drafted 2026-09-24
RULE CARDS             AWAITING_APPROVAL
CLUSTER BOUNDARY       RE-APPROVED BY HUMAN DECISION, 2026-09-14
OWNERSHIP GOVERNANCE   APPLIED, 2026-09-14 (five decisions -- SS3.1)
STAGE B (SYNTHESIS)    NOT BEGUN, NOT AUTHORIZED
RULE CARDS             NONE DRAFTED, NOT AUTHORIZED
PRE-CODE GATE          NOT AUTHORIZED
IMPLEMENTATION         NOT AUTHORIZED
ALTERNATE-SOURCE WORK  NOT AUTHORIZED -- DEC-0011 NOT ACTIVATED
```

### 3.0 Stage B — COMPLETE, 2026-09-24

The human project owner issued **seven adjudications** on the Stage-A and `DEC-0011` findings, and Stage B was drafted against them. **Five are Simulator Rulings; two are not** — that distinction is preserved in every artifact.

```text
SR-6   Belt pouch filled encumbrance = 52 cn           CHAR-004
SR-7   Magic-User dagger is unconditional              CHAR-004
SR-8   Suit Armor has no special movement rate;
       it is 750 cn and nothing else                   CHAR-005
SR-9   Mystic enhanced MV is gated on remaining in
       the unencumbered band                           CHAR-005
SR-10  Starvation movement progression 3/4, 1/2, 1/4   CHAR-005

Q4 running speed          RC Explicit interpretation + Necessary
                          Mechanical Consequence -- NOT a ruling
Q6 Mystic encounter       RC Explicit ratio + Necessary Mathematical
   movement, exact         Consequence -- NOT a ruling
   fractional retention
```

**Cards drafted, all `AWAITING_APPROVAL`:**

| Card | File |
|---|---|
| `CHAR-004` Starting Equipment & Expedition Preparation | `docs/rules/character_creation/starting_equipment_and_expedition_preparation.md` |
| `CHAR-005` Encumbrance & Movement Rate | `docs/rules/character_creation/encumbrance_and_movement_rate.md` |
| `EXP-003` **Dungeon Movement** | `docs/rules/exploration/dungeon_movement.md` |

**Full Stage-B record, including what each ruling rejected:** `docs/rules/clusters/CLUSTER-003-stage-b-synthesis.md`.

**Implementation remains NOT AUTHORIZED. The Pre-Code Gate has not been begun.**

### 3.0a Second independent completeness / boundary review — result

```text
CLUSTER-003 STAGE-A REMEDIATION:   PASS
PRIMARY-SOURCE COMPLETENESS:       CONDITIONAL PASS
REMAINING COMPLETENESS ITEM:       visual verification of the Nets Table
BOUNDARY GOVERNANCE:               RESOLVED BY HUMAN DECISION
STAGE B / ALTERNATE-SOURCE:        NOT AUTHORIZED
```

**The one conditional item is now closed.** The **Nets Table (RC p. 65, leaf n64)** was visually verified on 2026-09-14 — three columns (`Victim's Size | Equivalent* | Net Size**`), seven rows, two footnotes — and it **agrees with the existing `CHAR-004` evidence exactly**. It introduces no new mechanic, no contradiction, and no dependency. See `docs/rules/evidence/CHAR-004-evidence.md` §6 and §11 row 1.

### 3.1 Human boundary and ownership decisions — applied 2026-09-14

The boundary-reopen condition raised on 2026-09-13 has been **resolved by human decision**:

```text
No additional whole Rule Card is required for CLUSTER-003.
```

Five governance decisions were issued and are applied throughout this cluster's artifacts and `docs/rules/INVENTORY.md`. **These are governance decisions, not research conclusions**, and this document records rather than derives them.

| # | Decision | Effect |
|---|---|---|
| **1** | **`CHAR-004` canonically owns equipment-facing class restrictions** — the class-specific mechanics required to determine authoritative **mundane** equipment legality: weapon-permission predicates; armour/shield legality where relevant to equipment selection; class-specific equipment prohibitions; equipment-specific class pricing adjustments; other class-dependent mundane equipment rules | Established instances: Thief, Dwarf and Halfling weapon restrictions; Halfling armour fit; the Druid **+50%** wooden-weapon pricing adjustment; Magic-User weapon legality; Mystic mundane-equipment restrictions. **No dependency on the whole of `CHAR-009` is created.** `CHAR-009` may describe these as class features but **must not** become a second canonical implementation owner. Magic-item-specific restrictions stay with `TREAS-004` |
| **2** | **`CHAR-005` canonically owns the authoritative character movement-rate mechanic** — ordinary base movement; class/level-specific base movement exceptions; the **Mystic level-dependent `MV`**; encumbrance effects on movement; the authoritative derivation of this card's movement scales | **The whole of `CHAR-009` is not an incoming dependency.** The **`MV` × encumbrance composition remains an unresolved RC ambiguity and is not invented** |
| **3** | **`EXP-003` is narrowed and renamed to `EXP-003 — Dungeon Movement`** | The previous title *"Dungeon Movement, Mapping & Special Terrain"* is **no longer approved**. Mapping stays documented as an activity **already encompassed by ordinary exploration movement**, with **no** separate mechanic, time cost, roll or failure state. **"Special Terrain" is no longer an `EXP-003` responsibility** |
| **4** | **Chapter 10 high-level equipment material is `researched / preserved / NOT V1-WIRED`** | Different cash handling, equipment grants, the owned-versus-carried distinction and the magic-item acquisition procedure are all **preserved as findings** and **not** made executable by `CLUSTER-003`. Terminology follows the existing `NOT V1-WIRED` precedent (`CHAR-003 W3`) |
| **5** | **Condition effects split by responsibility** | For blindness, stunning and starvation, the procedure that **causes or establishes** the condition remains owned elsewhere; the **stated numerical effect on the authoritative movement rate** belongs to `CHAR-005`. `CHAR-005` is **not** responsible for how or why the condition was acquired |

**Source location versus canonical ownership.** Decisions 1 and 2 move *ownership*, not *evidence*. The class-specific text physically resides in **RC Chapter 2**, and every citation to it is preserved in this cluster's evidence packets. A future reader must be able to see both that RC prints the Thief weapon restriction on p. 21 and that `CHAR-004` is the card that implements it.

### 3.0 Independent completeness review — result, and the boundary reopen

The first independent completeness review was performed against the Stage-A package committed at `e26a1e0` and **did not pass**:

```text
RESULT:                      REMEDIATION REQUIRED
PRIMARY-SOURCE COMPLETENESS: FAIL -- unfinished structural inspection
BOUNDARY INTEGRITY:          REOPEN REQUIRED -- CHAR-005 has a newly
                             established unlanded class-specific movement
                             dependency presently associated with CHAR-009
EXP-010 / CHAR-006 / CHAR-008:  remain deferred
```

**A governance reading in the first researcher report is corrected here.** That report concluded the Mystic `MV` finding was not a boundary-reopen condition because `CHAR-009` is not one of the three deferred cards (§5.1). **That was wrong.** The approved boundary rule fires whenever Stage-A work establishes a **mechanically indispensable dependency on any unlanded Rule Card not currently in `CLUSTER-003`** — and the original assignment named *"`CHAR-005` genuinely requiring an unlanded class/race movement rule"* as its worked example.

**The boundary recorded in §4 is therefore provisional and awaits human governance.** `CHAR-009` was **not** added; see §7.6 for the evidence package and the five options the human decision may take.

**Remediation pass 1** (2026-09-13) closed the declared structural inspection. Record: `docs/rules/evidence/CLUSTER-003-remediation-pass-1.md`. It closed six open rows, found **two governing objects the first pass missed**, produced **two new contradictions**, **withdrew one gap**, and corrected two citations — while adding, removing, and renaming **nothing** in the cluster.

**This record is a boundary and evidence-state record, not an authorization.** It creates no Rule Card, approves nothing, and expands no boundary. The cluster boundary recorded in §4 was set by the human project owner in the task that commissioned this research; this document records it, it does not decide it.

### Lifecycle gates, in order

| Gate | Authority | State |
|---|---|---|
| Stage-A evidence collection | `DEC-0009`, `DEC-0010` | **Done** — three packets under `docs/rules/evidence/` |
| Adversarial self-review | protocol §10.1.1 | **Done** — `docs/rules/evidence/CLUSTER-003-completeness-audit.md` |
| **Independent completeness review (round 1)** | protocol §10.1.2, `DEC-0010` item 14 | **PERFORMED — `REMEDIATION REQUIRED`.** See §3.0. |
| **Stage-A remediation pass 1** | this cluster record §3.0 | **Done** — `docs/rules/evidence/CLUSTER-003-remediation-pass-1.md` |
| **Second independent completeness / boundary review** | protocol §10.1.2 | **PERFORMED — `PASS` on remediation, `CONDITIONAL PASS` on completeness.** See §3.0a |
| **Human boundary / ownership governance** | human project owner | **ISSUED AND APPLIED 2026-09-14** — five decisions, §3.1 |
| **Stage-A researcher closure (Nets Table)** | protocol §9.2 | **Done 2026-09-14** — the one conditional item is closed |
| **Final independent `DEC-0010` completeness certification** | protocol §10.1.2, `DEC-0010` item 14 | **NOT PERFORMED.** May not be performed by the original researcher. |
| Human evidence review | protocol §11 | **Not reached** |
| Stage B synthesis | protocol §3 | **Not begun, not eligible** |
| Rule Card approval | `SOURCE_HIERARCHY.md` §9 | Not reached |
| Implementation | `ARCHITECTURE.md` §15, `AGENTS.md` §9 | **Not authorized** |

Each of the three Stage-A packets carries the protocol §11.19 recommendation `MORE PRIMARY RESEARCH REQUIRED`, with the outstanding work named row by row in the completeness audit §8. That is a statement about the completeness perimeter, not about the core procedures, which are established and visually verified.

## 4. Approved Boundary

**Re-approved by the human project owner, 2026-09-14.**

```text
CLUSTER-003 -- Equipped Dungeon Movement

    CHAR-004   Equipment
               (registered INVENTORY.md title: "Starting Equipment &
                Expedition Preparation" -- unchanged; the boundary
                refers to the entry as "Equipment")
    CHAR-005   Encumbrance & Movement Rate
    EXP-003    Dungeon Movement
               (RENAMED 2026-09-14; the previous title
                "Dungeon Movement, Mapping & Special Terrain"
                is NO LONGER APPROVED)
```

### Why these three, and why in this order

The cluster is a **single dependency spine**, each link stated by RC itself rather than inferred:

```text
landed character foundation (CLUSTER-002)
        |
        v
CHAR-004   a character rolls 3d6 x 10 gp and buys gear
           each catalog row carries an Enc (cn) value
           RC Ch. 4 p. 63: "the more encumbrance a character is
           carrying, the slower he moves"
        |
        v
CHAR-005   total cn -> Character Movement Rates and Encumbrance
           Table (RC p. 88) -> normal / encounter / running speed
        |
        v
EXP-003    RC Ch. 7 p. 91: "customarily characters will travel at
           their normal speed during game turns"
        |
        v
landed EXP-002 dungeon-time machinery (CLUSTER-001)
```

`CLUSTER-003` is the first cluster whose value is **compositional across two landed clusters**: it consumes `CLUSTER-002`'s characters at one end and `CLUSTER-001`'s dungeon turn at the other.

## 5. Explicit Exclusions

### 5.1 Deliberately deferred during boundary review — do not absorb

| Card | Title | State |
|---|---|---|
| `CHAR-006` | Retainers & Hirelings | **Deferred.** Not researched, not absorbed. |
| `CHAR-008` | Alignment | **Deferred.** Not researched, not absorbed. |
| **`CHAR-009`** | **Class Special Abilities & Racial Abilities/Limitations — as a whole** | **Deferred, and confirmed out by the 2026-09-14 human decision.** Not added. Two mechanics whose RC source text sits in its chapter are canonically owned elsewhere by Decisions 1 and 2 — see §3.1. |
| `EXP-010` | Party Formation & Marching Order | **Deferred.** Tested only as a possible incoming dependency; `DISPROVED` — see §7.3. |

A boundary-reopen condition exists for these: **if primary-source evidence proves one of them is an indispensable incoming dependency, that is a stop for human governance review, not an expansion.** Stage A **did** trigger it on 2026-09-13 for a class-specific movement rule associated with `CHAR-009`; the human decision of 2026-09-14 **resolved** it without adding a card:

```text
No additional whole Rule Card is required for CLUSTER-003.
```

### 5.2 Deferred governance items — not absorbed

`P1` (Druid transition ownership), `P3` (Chapter 13 Ability Check Rule ID), `CHAR-003 W2` (`MOOT`), `CHAR-003 W3` (`NOT V1-WIRED`). `P3` was reached only as a cross-reference from RC Ch. 13 "Climbing" and was **not opened, not researched, and no Rule ID was proposed**.

### 5.3 Material located and routed to other cards

| Material | Owner | Where recorded |
|---|---|---|
| Opening stuck doors; listening | `EXP-005` | Already assigned; Doors procedure in `CLUSTER-002-completeness-audit.md` §5.4 |
| Light-source radius and duration (torch 30′/6 turns; lantern 30′/24 turns per flask) | `EXP-006` | `EXP-003-evidence.md` §4 |
| Infravision (60′ in the dark; fails in light) | `CHAR-009` / `EXP-006` | `EXP-003-evidence.md` §4 |
| Traps | `EXP-007` | No dungeon-movement interaction located |
| Evasion, pursuit, and dungeon "difficult terrain" as an **evasion** condition (RC Ch. 7 p. 98) | **`ENC-005`** | `EXP-003-evidence.md` §4, §9 Challenge 1 |
| Surprise, encounter distance, reaction | `ENC-002`, `ENC-003` | Routed from the Game Turn Checklist |
| Wandering-monster checks and turn accounting | landed `EXP-001` / `EXP-002` | Game Turn Checklist steps 1 and 4 |
| Overland travel, terrain-by-day, becoming lost, water and aerial travel | wilderness-movement responsibility | Inspected only to bound `EXP-003`; then excluded |
| Monster, mount and vehicle carrying capacity | `MON-*` and an **unassigned transport responsibility** | `CHAR-004-evidence.md` §11 item 5 |
| Weapon damage, ranges, two-handed initiative, net entanglement | `COMBAT-002`/`003`/`006`/`007` | `CHAR-004-evidence.md` §7 |
| Endurance general skill (extends the 30-round running limit) | `CHAR-012` | `CHAR-005-evidence.md` §4 |

### 5.4 Architectural exclusions (standing project constraints)

No speculative orchestration abstraction is introduced or implied by this cluster — no `GameState`, `Party`, `ExplorationEngine`, `TurnManager`, `Command`, `Session`, or `ApplicationService`. The landed clusters are pure functions over explicit inputs, and nothing in this evidence requires otherwise.

### 5.5 Random Encounter Principle

**A random encounter does not automatically mean combat** (`AGENTS.md` §5). RC's Game Turn Checklist routes a positive wandering-monster result to the **Encounter Checklist**, which begins with detection, surprise and reaction. **`CLUSTER-003` encodes no assumption that movement becomes combat**, and no Stage-A conclusion in any of the three packets depends on one.

### 5.6 AD&D

Excluded by default (`AGENTS.md` §4). Not consulted.

## 6. Dependency Analysis

### 6.1 As recorded in `docs/rules/INVENTORY.md` before this research

```text
CHAR-004   depends on CHAR-001..CHAR-003          (all landed)
CHAR-005   depends on CHAR-004
EXP-003    depends on CHAR-005, EXP-002           (EXP-002 landed)
```

### 6.3 Final dependency graph after governance (2026-09-14)

```text
landed character identity / class / level
  (CHAR-001, CHAR-002, CHAR-003, CHAR-007 -- all VERIFIED)
                |
                v
        CHAR-004  Equipment
            owns: money, catalogs, cost, encumbrance values,
                  unlisted-item procedure,
                  AND per-class mundane equipment legality  [Decision 1]
                |
                v
        CHAR-005  Encumbrance & Movement Rate
            owns: standard character movement,
                  Mystic MV exception                        [Decision 2]
                  applicable movement modifiers,
                  condition movement effects                 [Decision 5]
                |
                v
        EXP-003   Dungeon Movement                           [Decision 3]
                |
                v
        EXP-002   Dungeon Time  [LANDED / VERIFIED]
```

**No whole-card dependency `CHAR-004 → CHAR-009` or `CHAR-005 → CHAR-009` exists for `CLUSTER-003`.** Both were recorded as candidates on 2026-09-13 and both are **withdrawn** by Decisions 1 and 2. What remains is a **source-location** relationship, not a card dependency: the governing RC text for several of these mechanics is printed in Chapter 2, and that provenance is preserved in the evidence packets.

### 6.2 What Stage A found

| Edge | Status after Stage A (2026-09-13), with the 2026-09-14 governance outcome |
|---|---|
| `CHAR-004` → landed `CHAR-001`–`CHAR-003` | **Confirmed.** Chapter 1 places "Roll for Money" and "Buy Equipment" as steps 5 and 6, after abilities, class and hit points. |
| `CHAR-005` → `CHAR-004` | **Confirmed, and stated by RC itself** (Ch. 4 p. 63 → Ch. 6 p. 88). |
| `EXP-003` → `CHAR-005` | **Confirmed** (Ch. 7 p. 91 "normal speed"). |
| `EXP-003` → landed `EXP-002` | **Confirmed** (the 10-minute turn; Measurements of Game Time Table). |
| **`CHAR-005` → an unlanded class-abilities responsibility** | **RAISED 2026-09-13, WITHDRAWN 2026-09-14.** The **visually verified** Mystic Special Abilities Table (RC p. 31) gives a class- and level-dependent `MV` of 120′ → 320′, contradicting RC p. 88's "**any character** will have a movement rate of `120' (40')`" (§7.1). **Human Decision 2 assigns the authoritative movement-rate mechanic, including the Mystic `MV`, to `CHAR-005` itself.** No card dependency results |
| **`CHAR-004` → an unlanded class-abilities responsibility** | **CONTESTED 2026-09-13, WITHDRAWN 2026-09-14.** RC states class weapon/armour permissions in Chapter 4 itself *and* routes the buying step to the Chapter 2 class description (Ch. 1 p. 8) (§7.2). **Human Decision 1 assigns mundane equipment legality to `CHAR-004` itself**, and `CHAR-002`'s downstream ownership pointer has been corrected accordingly. No card dependency results |
| `EXP-003` → `EXP-010` | **DISPROVED.** See §7.3. |

## 7. Boundary Findings — Raised for Human Governance, Not Resolved

### 7.1 `CHAR-005` has an incoming dependency `INVENTORY.md` does not record

```text
RC Ch. 6 p. 88   "Any character will have a movement rate of '120' (40')'
                  unless he is weighed down by a lot of gear."

RC Ch. 2 p. 31   Mystic Special Abilities Table, MV column, VISUALLY VERIFIED
                  L1 120'  L2 130'  L3 140'  L4 150'  L5 160'  L6 170'
                  L7 180'  L8 190'  L9 200'  L10 210' L11 220' L12 240'
                  L13 260' L14 280' L15 300' L16 320'
                  legend: "First level mystics move as fast as any other
                  unarmored characters, but higher level mystics learn to
                  move very, very fast indeed."
```

The Mystic is **REQUIRED V1 content** under `DEC-0008`, so this is not an optional-content edge case. RC nowhere states how the `MV` value composes with the encumbrance bands.

**This is raised, not resolved.** It is **not** a §5.1 boundary-reopen condition — `CHAR-009` is not one of the three deferred cards — but it is a genuine unlanded incoming dependency that a human must settle before Stage B.

### 7.2 `CHAR-004`'s ownership of purchase legality is contested by the source itself

RC states class weapon and armour permissions **twice**: in Chapter 4's own Weapons Table notes (`c`, `w`, `2H`, `HH`) and armour prose, and — by Chapter 1's explicit instruction — in the Chapter 2 class entries. This is an audit-class-I duplicate presentation, not a missing rule. The assigned falsification target (that `CHAR-004` needs no unlanded class card) **holds for the money roll, catalogs, costs, encumbrances and the unlisted-item procedure, and does not hold for purchase legality**.

### 7.3 `EXP-010` is NOT an incoming dependency — the reopen condition is not triggered

```text
RC Ch. 1 "Mapping and Calling"
    "Any player can be the mapper or caller."
    "The caller is just a convenience in many campaigns;
     it's not a game rule that players have to use."

whole-source phrase sweep
    "marching order"  -> 1 occurrence, in NPC PARTY GENERATION
    "single file", "front rank", "order of march", "abreast" -> none

Tables Index -> no formation or marching-order table
```

Stated as coverage over the objects inspected, not as proof RC contains nothing. **`EXP-010` remains deferred and unresearched.**

### 7.4 Two of `EXP-003`'s three named sub-responsibilities have no RC mechanic

| Sub-responsibility | Finding |
|---|---|
| Dungeon Movement | **A substantial RC procedure.** Ch. 7 p. 91 turn loop + Game Turn Checklist; Ch. 6 rate, units and 10′ map scale. |
| Mapping | **DM description technique, no mechanic.** No die, no time cost, no failure state — and RC p. 88 states that normal speed *already includes* mapping. Charging time for mapping in Stage B would double-count. |
| Special Terrain | **No located RC dungeon-scale mechanic.** RC states terrain "makes no difference to the combat round or the 10-minute turn"; both terrain tables are **visually verified** as per-day and outdoor. The only text presupposing a dungeon-scale terrain modifier is the Mystic Acrobatics ability, and RC never publishes the rule it negates. `RC DOES NOT SPECIFY`. |

Whether the card's title should change is a governance decision and is **not** made here.

### 7.5a Post-remediation corrections to §7.1–§7.4 (2026-09-13)

| § | Status after remediation pass 1 |
|---|---|
| **7.1** `CHAR-005` dependency | **CONFIRMED and escalated.** The Mystic is now established as the **only** class with a movement exception, on structural evidence: all nine experience tables and all nine boxed blocks opened as page images, all nine Class Details read in full, and RC's own "Understanding the Tables" (p. 13) enumerates the experience-table column set with no movement column. The reading that this was *not* a reopen condition is **withdrawn** — see §3.0. |
| **7.2** `CHAR-004` ownership | **SHARPENED, and the answer is now NO.** `CHAR-004` cannot determine legal starting equipment from Ch. 1 + Ch. 4 + Ch. 13 alone. **Armour permissions are genuinely duplicated; weapon permissions are not.** Thief, Dwarf and Halfling weapon restrictions and the Druid **+50% pricing rule** exist only in Chapter 2. RC's General Index routes `Weapon restrictions` to **nine class pages and not to Chapter 4**. |
| **7.3** `EXP-010` | **CONFIRMED, additionally supported.** The General Index contains no `Marching`, `Formation`, or `Carrying capacity` entry. `EXP-010` remains deferred and un-researched. |
| **7.4** `EXP-003` sub-responsibilities | **Mapping unchanged and stronger** — two further presentations located (RC p. 5, Ch. 17 p. 262), neither with a mechanic. **Special Terrain qualified** — RC Ch. 14 p. 153 prohibits a monster from charging in *"broken, heavy forest, jungle, mountain, swamp"* terrain, with *"20 yards (**20 feet indoors**)"*. That is a real indoor terrain constraint, but on an **action**, owned by `COMBAT-*`/`MON-*`, not a rate or turn-cost rule. The gap stands, narrower. **Also: the 10′ map square is a DM-variable default** (Ch. 17 p. 260), not a constant. |

### 7.5 Four internal source defects, all visually verified, none resolved

| Defect | Disposition |
|---|---|
| Belt pouch: printed `2*` enc + `Capacity 50 cn`, footnote worked example says `55 cn` (`2 + 50 = 52`) | `RETAINED AS GENUINE SOURCE AMBIGUITY` — **survives re-testing**; `55 cn` occurs once in the whole source |
| Suit Armor: `Enc 750 cn` → `90' (30')` by the p. 88 table; item description says "movement rate is `30' (10')`" | `RETAINED AS GENUINE SOURCE AMBIGUITY` — **survives re-testing**; no override language exists in either direction |
| Starvation Table movement column non-monotonic: `No Penalty / ×3/4 / ×1/2 / ×3/4` | `RETAINED AS GENUINE SOURCE AMBIGUITY` — **survives re-testing** |
| "Clothes, plain" carries `***` (the quiver footnote) instead of `**` | Recorded as a typographic defect — **survives re-testing** |
| **NEW (remediation)** — magic-user dagger: Ch. 4 note `w` marks both dagger rows *"at the DM's discretion"*, while Ch. 2 p. 19 makes the dagger the magic-user's one **unconditional** weapon | `RETAINED AS GENUINE SOURCE AMBIGUITY` |
| **NEW (remediation)** — running speed: Ch. 6 p. 88 *"equal to their normal speed in feet per round… or three times their encounter speed"* vs. Ch. 8 p. 103 *"(**3 × normal movement**)"* | `RETAINED AS GENUINE SOURCE AMBIGUITY` — a factor-of-3 discrepancy, both sides visually verified |
| **WITHDRAWN (remediation)** — racial-armour movement reduction, previously `RC DOES NOT SPECIFY` | **NOT A GAP.** The complete sentence is *"**The DM can impose penalties** on a character who wears the armor of a different race"*; the movement reduction is an example of an optional penalty. RC delegates by design. |

Per protocol §10.2.2 case 3, a fully mapped genuine conflict does not block source completeness. **None is resolved, and no side is silently preferred.**

### 7.6 Boundary-reopen evidence package

> Prepared for human governance by remediation pass 1. **No boundary is chosen here.** Full detail: `docs/rules/evidence/CLUSTER-003-remediation-pass-1.md` §9.

| Question | Answer |
|---|---|
| **A.** Indispensable unlanded dependency? | **YES — two, different in kind** |
| **B.** Which cards? | `CHAR-005` (movement) and `CHAR-004` (equipment legality). `EXP-003` exhibits none |
| **C.** Exact mechanic crossing the boundary | `CHAR-005`: a `(class, level) → base movement rate` datum, non-default for **one** class (Mystic `MV`, 120′→320′), plus an **unsupplied** composition rule for `MV` × encumbrance. `CHAR-004`: a per-class **weapon-permission predicate** (Thief, Dwarf, Halfling) plus the Druid **+50% pricing** rule. Armour permissions are duplicated in Chapter 4 and are **not** a dependency |
| **D.** Is the whole external Rule Card required? | **No.** `CHAR-009`'s scope — class and racial abilities across the roster — is far larger than either slice, and nothing else in it is reachable from these two cards |
| **E.** Could a narrower ownership correction solve it? | **Consistent with the evidence, in at least three shapes** — see remediation §9E. Counter-consideration recorded: RC's own boxed material names *"increased movement"* as a Mystic **special ability**, and RC's own index routes `Weapon restrictions` to class pages |
| **F.** Would the current three-card cluster produce incorrect behaviour if implemented unchanged? | **YES, demonstrably, for four of nine required V1 classes.** A 10th-level mystic would be given 120′ where RC says **210′**; a thief could buy a **two-handed sword**; a dwarf a **longbow**; a halfling a **Medium weapon** and non-halfling armour. One wrong number, three permitted-illegal purchases |

~~**The eventual human decision may be A (add an existing whole Rule Card), B (change ownership of a narrow mechanic), C (identify a different existing owner), D (revise a Rule Card boundary), or E (revise the cluster boundary). That decision is not made here.**~~

> **RESOLVED 2026-09-14 — the human project owner selected option B for both dependencies: change ownership of the narrow mechanic.** Mundane equipment legality → `CHAR-004` (Decision 1); the authoritative movement-rate mechanic including Mystic `MV` → `CHAR-005` (Decision 2). **Option A was not taken: no additional whole Rule Card is required for `CLUSTER-003`.** The answers to A–F above are preserved unaltered as the evidence the decision rested on — in particular answer **F**, which remains the record of what would have gone wrong had the cluster been implemented on the pre-decision boundary.

## 8. Unresolved Evidence-Stage Questions

The complete, non-silent inventory is the reconciliation table at `docs/rules/evidence/CLUSTER-003-completeness-audit.md` §8 — twenty-one rows, every one dispositioned. Summarised:

**Unfinished source inspection (blocks completeness):**

1. Ch. 2 class entries as complete entries — weapon/armour permissions.
2. The other eight class tables — any `MV`-style column.
3. Ch. 19 Variant Rules body (only its TOC sub-headings were used).
4. Ch. 17 "Designing Adventures and Dungeons" pp. 259–262.
5. The General Index (p. 302) as a completeness locator — audit class H is only partly discharged.
6. Ch. 10 high-level character creation, re-checked for a wealth/equipment provision.

**Human decisions required (no amount of reading supplies these):**

7. `CHAR-004` scope — do mounts, vehicles, ships and siege equipment belong to it?
8. Do the blindness / stunning / starvation movement multipliers (RC p. 150) belong to `CHAR-005` or to a status-condition responsibility `INVENTORY.md` does not yet contain? **No Rule ID was invented.**
9. `EXP-003`'s title, given §7.4.
10. The two dependency questions in §7.1 and §7.2.

**Genuine source ambiguities (do not block completeness):** the four defects in §7.5, plus `RC DOES NOT SPECIFY` for the racial-armour movement reduction and for the rough-terrain modifier presupposed by Mystic Acrobatics.

### 8.1 Disposition of §8 after remediation and governance (2026-09-14)

| §8 item | Disposition |
|---|---|
| 1–6 — unfinished source inspection | **ALL CLOSED** by remediation pass 1 (2026-09-13). Items 1, 2, 3, 4, 6 closed by direct inspection; item 5, the General Index, closed and **it found two governing objects the earlier passes missed** |
| **Nets Table** *(the one item the second independent review left conditional)* | **CLOSED 2026-09-14 by visual verification.** Agrees with existing evidence; no new mechanic, contradiction or dependency — §3.0a |
| 7 — `CHAR-004` scope: mounts, vehicles, ships, siege | **STILL OPEN — human governance.** Not decided by the 2026-09-14 decisions, which addressed class-restriction ownership, not chapter scope. Water transport and siege remain recorded as *located and deliberately uninspected* |
| 8 — condition movement multipliers | **DECIDED 2026-09-14 (Decision 5)** — split by responsibility; §3.1 |
| 9 — `EXP-003` title | **DECIDED 2026-09-14 (Decision 3)** — renamed to `EXP-003 — Dungeon Movement`; §3.1 |
| 10 — the two dependency questions | **DECIDED 2026-09-14 (Decisions 1 and 2)** — option B, narrow ownership correction; §7.6 |
| Genuine source ambiguities | **ALL PRESERVED, NONE RESOLVED.** The racial-armour item was reclassified during remediation as **DM discretion by design, not a gap**; the remainder stand, with two contradictions added by remediation. §7.5 |

**One item from §8 therefore remains open, and it is a human scope question, not an inspection task:** item 7. It does **not** block `CLUSTER-003` Stage-A primary-source closure, because the water-transport and siege objects are recorded as deliberate exclusions with stated reasons rather than as unexamined gaps.

**`DEC-0011` is not activated.** No alternate-source research has been performed or authorized. A future human authorization will identify which exact gaps and contradictions proceed into that research.

## 9. Relationship to `CLUSTER-001` and `CLUSTER-002`

| Cluster | State | What `CLUSTER-003` takes from it |
|---|---|---|
| `CLUSTER-001` — Dungeon Exploration Time | **`VERIFIED`**, merged and implemented | The 10-minute turn and turn-credit accounting that `EXP-003` spends movement against; the wandering-monster check the Game Turn Checklist invokes |
| `CLUSTER-002` — Character Foundation | **`VERIFIED`**, merged 2026-09-13 (`8d26eb0`) | The character `CHAR-004` equips: abilities, race/class, hit points, ability-score effects |

**Method inheritance.** This cluster is the first researched wholly under `DEC-0010`'s structure-first order from the outset, rather than being remediated into it. The audit's §2 records that **three of eleven visual verifications changed a conclusion OCR alone would have produced**, and that the cluster's single most consequential finding (§7.1) was surfaced by the **Tables Index**, not by any chapter a topic-driven search would have opened. `CLUSTER-002`'s remediation cost is what bought that ordering; it appears to have paid.

## 10. Roadmap Position

`docs/rules/INVENTORY.md` §"Suggested research order" places `CHAR-004`–`CHAR-006` at item 3 and the `EXP-002`–`EXP-010` research at item 4. `CLUSTER-003` takes `CHAR-004` and `CHAR-005` from item 3 — **leaving `CHAR-006` where it is** — and `EXP-003` from item 4. Nothing else moves.

## 11. Expected Simulation Capability After Eventual Implementation

Stated as an expectation about a cluster that is **not authorized for implementation**, so that a later reader can judge whether the boundary was the right size:

```text
An equipped character can be created, given 3d6 x 10 gp of gear whose
encumbrance is known, and moved through a dungeon at a rate the rules
derive rather than assume -- with the party moving at its slowest
member's rate, and each turn of movement debited against the landed
dungeon-turn machinery that already drives wandering-monster checks.
```

That is the smallest end-to-end dungeon-exploration loop the project has been able to describe, and it is the reason these three cards were clustered.

## 12. Implementation Authorization Status

```text
NOT AUTHORIZED
```

No Rule Card exists for any of the three cards. `AGENTS.md` §2 forbids implementing a Rule Card that is not `APPROVED`, and §9's path runs Evidence → Human Review → Stage B → Draft → Approval → Implementation. This cluster is at the **first** of those gates, and has not cleared it.

## 13. Provenance

| Item | Value |
|---|---|
| Governing protocol | `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` (`DEC-0009`) |
| Completeness requirements | `DEC-0010` |
| Alternate-source corpus requirements | `DEC-0011` — **not reopened, and not invoked**; no alternate-source research was performed |
| Primary source | *D&D Rules Cyclopedia* (TSR, 1991), per `SOURCE_HIERARCHY.md` §3 and `DEC-0007` |
| Stage-A packets | `docs/rules/evidence/CHAR-004-evidence.md`, `CHAR-005-evidence.md`, `EXP-003-evidence.md` |
| Self-review artifact | `docs/rules/evidence/CLUSTER-003-completeness-audit.md` |
| Boundary set by | Human project owner, in the task commissioning this research |
| Research performed | 2026-09-13 |

```text
CLUSTER-003:

STAGE A                     COMPLETE -- DEC-0010 completeness PASS
DEC-0011 (BECMI)            COMPLETE -- remediation 1 applied
HUMAN ADJUDICATION          COMPLETE -- 2026-09-24
STAGE B                     COMPLETE -- three Rule Cards drafted
RULE CARDS                  AWAITING_APPROVAL

HUMAN RULE CARD REVIEW:     PENDING
IMPLEMENTATION:             NOT AUTHORIZED
PRE-CODE GATE:              NOT BEGUN
FURTHER LINEAGE RESEARCH:   NOT STARTED / NOT AUTHORIZED
```
