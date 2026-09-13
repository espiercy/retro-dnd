# Cluster 3: Equipped Dungeon Movement

## 1. Cluster ID

`CLUSTER-003`

## 2. Name

Equipped Dungeon Movement

## 3. Status

```text
STAGE A (EVIDENCE)     RESEARCHER SELF-REVIEW COMPLETE
                       AWAITING INDEPENDENT COMPLETENESS REVIEW
STAGE B (SYNTHESIS)    NOT BEGUN, NOT ELIGIBLE
RULE CARDS             NONE DRAFTED
IMPLEMENTATION         NOT AUTHORIZED
```

**This record is a boundary and evidence-state record, not an authorization.** It creates no Rule Card, approves nothing, and expands no boundary. The cluster boundary recorded in §4 was set by the human project owner in the task that commissioned this research; this document records it, it does not decide it.

### Lifecycle gates, in order

| Gate | Authority | State |
|---|---|---|
| Stage-A evidence collection | `DEC-0009`, `DEC-0010` | **Done** — three packets under `docs/rules/evidence/` |
| Adversarial self-review | protocol §10.1.1 | **Done** — `docs/rules/evidence/CLUSTER-003-completeness-audit.md` |
| **Independent completeness review** | protocol §10.1.2, `DEC-0010` item 14 | **NOT PERFORMED.** May not be performed by the original researcher. |
| Human evidence review | protocol §11 | **Not reached** |
| Stage B synthesis | protocol §3 | **Not begun, not eligible** |
| Rule Card approval | `SOURCE_HIERARCHY.md` §9 | Not reached |
| Implementation | `ARCHITECTURE.md` §15, `AGENTS.md` §9 | **Not authorized** |

Each of the three Stage-A packets carries the protocol §11.19 recommendation `MORE PRIMARY RESEARCH REQUIRED`, with the outstanding work named row by row in the completeness audit §8. That is a statement about the completeness perimeter, not about the core procedures, which are established and visually verified.

## 4. Approved Boundary

```text
CLUSTER-003 -- Equipped Dungeon Movement

    CHAR-004   Starting Equipment & Expedition Preparation
    CHAR-005   Encumbrance & Movement Rate
    EXP-003    Dungeon Movement, Mapping & Special Terrain
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
| `EXP-010` | Party Formation & Marching Order | **Deferred.** Tested only as a possible incoming dependency; see §7. |

A boundary-reopen condition exists for these three: **if primary-source evidence proves one of them is an indispensable incoming dependency, that is a stop for human governance review, not an expansion.** Stage A did not trigger it — see §7.

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

### 6.2 What Stage A found

| Edge | Status after Stage A |
|---|---|
| `CHAR-004` → landed `CHAR-001`–`CHAR-003` | **Confirmed.** Chapter 1 places "Roll for Money" and "Buy Equipment" as steps 5 and 6, after abilities, class and hit points. |
| `CHAR-005` → `CHAR-004` | **Confirmed, and stated by RC itself** (Ch. 4 p. 63 → Ch. 6 p. 88). |
| `EXP-003` → `CHAR-005` | **Confirmed** (Ch. 7 p. 91 "normal speed"). |
| `EXP-003` → landed `EXP-002` | **Confirmed** (the 10-minute turn; Measurements of Game Time Table). |
| **`CHAR-005` → an unlanded class-abilities responsibility** | **NEW — not in `INVENTORY.md`.** The **visually verified** Mystic Special Abilities Table (RC p. 31) gives a class- and level-dependent `MV` of 120′ → 320′, contradicting RC p. 88's "**any character** will have a movement rate of `120' (40')`". See §7.1. |
| **`CHAR-004` → an unlanded class-abilities responsibility** | **CONTESTED.** RC states class weapon/armour permissions in Chapter 4 itself *and* routes the buying step to the Chapter 2 class description (Ch. 1 p. 8). `CHAR-002`'s approved boundary assigns permissions to `CHAR-009`/`TREAS-004`. See §7.2. |
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

### 7.5 Four internal source defects, all visually verified, none resolved

| Defect | Disposition |
|---|---|
| Belt pouch: printed `2*` enc + `Capacity 50 cn`, footnote worked example says `55 cn` (`2 + 50 = 52`) | `RETAINED AS GENUINE SOURCE AMBIGUITY` |
| Suit Armor: `Enc 750 cn` → `90' (30')` by the p. 88 table; item description says "movement rate is `30' (10')`" | `RETAINED AS GENUINE SOURCE AMBIGUITY` |
| Starvation Table movement column non-monotonic: `No Penalty / ×3/4 / ×1/2 / ×3/4` | `RETAINED AS GENUINE SOURCE AMBIGUITY` |
| "Clothes, plain" carries `***` (the quiver footnote) instead of `**` | Recorded as a typographic defect |

Per protocol §10.2.2 case 3, a fully mapped genuine conflict does not block source completeness. **None is resolved, and no side is silently preferred.**

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
CLUSTER-003 STAGE-A RESEARCH:
RESEARCHER SELF-REVIEW COMPLETE
AWAITING INDEPENDENT COMPLETENESS REVIEW
```
