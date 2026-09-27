# CLUSTER-004 — Boundary Research and Candidate Scopes

```text
STATUS:  SUPERSEDED IN PART -- see CLUSTER-004-BOUNDARY-CORRECTION.md
```

> **Forward pointer added 2026-09-27. The body below is unaltered and is kept as the record
> of an analysis made against an incomplete inventory.**
>
> This document was written before the 42 lost `INVENTORY.md` lines were restored
> (`6c5c73a`). It could read the deleted rows' *dependency* cells from git, but **not their
> `Downstream Consumers`, `Status` or `Risk / Notes` columns** — which is where the findings
> that changed the boundary were sitting.
>
> **Its §1 defect finding stands. Its §4 recommendation does not.** The active boundary is
> now `EXP-006` + `ENC-005`, with `EXP-004` and `EXP-010` deferred, and the dungeon-stocking
> cycle is three-member rather than two. See `CLUSTER-004-BOUNDARY-CORRECTION.md` §2 for the
> full list of what changed and what remains valid.

> **This document proposes nothing binding.** No Rule Card is drafted, no cluster is
> selected, and no implementation is authorized. It exists so a human can choose a
> `CLUSTER-004` boundary — or reject all of the candidates below — with the dependency
> frontier visible.
>
> Prepared 2026-09-27, immediately after `CLUSTER-003` was accepted and merged (`c3a3e2d`).

---

## 1. Blocking finding — the inventory is missing 27 rows

**`ARCHITECTURE.md` §15.1's prerequisite is not currently met**, and this must be settled
before any `CLUSTER-004` boundary is approved:

> *"Before any cluster is selected, a complete V1 Rules Inventory and Dependency Map must
> exist and be human-reviewed."*

Commit **`5208798`** (2026-09-24, *"CLUSTER-003 Stage B — adjudications and three Rule
Cards"*) deleted **46 lines** from `docs/rules/INVENTORY.md`: three whole domain sections
and seven exploration rows. Its commit message describes only the three rewritten rows and
does not mention the deletion. **It was unintended collateral damage from a scripted edit
to the `CHAR-004`, `CHAR-005` and `EXP-003` rows, and it was introduced by this project's
agent — me — and not caught in any subsequent review.**

**Rows lost (27):**

```text
EXP-004  Rest / Exhaustion Procedure                    [was REVALIDATION_REQUIRED]
EXP-005  Searching, Listening, Doors & Secret Features
EXP-006  Light & Exploration Resources
EXP-007  Traps -- trigger mechanic
EXP-008  Dungeon Stocking
EXP-009  (retired -- see SIM-001)
EXP-010  Party Formation & Marching Order

ENC-001  Encounter Distance          ENC-005  Retreat, Pursuit & Evasion
ENC-002  Surprise                    ENC-006  Non-Combat Resolution / Parley
ENC-003  Reaction                    ENC-007  Encounter Balancing
ENC-004  Monster Morale

MON-001  Monster Determination & Level/Encounter Matrix
MON-002  Number Appearing
MON-003  General Monster Statistics (catalog closure)
MON-004  Monster Special Abilities & Immunities (catalog closure)

COMBAT-001  Combat System (unified Attack Roll vs. AC)
COMBAT-002  Attack Resolution, Armor Class & To-Hit
COMBAT-003  Damage & Death
COMBAT-004  Saving Throws
COMBAT-005  Healing & Natural Recovery
COMBAT-006  Combat Sequence, Initiative & Timing
COMBAT-007  Weapon Mastery Combat Effects
COMBAT-008  Nonlethal Combat                 [Ch. 19 variant, REQUIRED]
COMBAT-009  Mortally Wounded                 [Ch. 19 variant, REQUIRED]
```

**Twenty-six of those IDs are still cited as dependencies elsewhere in the same document**,
in `RC_V1_SCOPE_AUDIT.md`, in `INVENTORY_MIGRATION_MAP.md` (which retains all of them), and
in landed Rule Cards — `EXP-003` §5 routes wandering monsters to `ENC-002`/`ENC-003`;
`CHAR-004` §A defers light to `EXP-006` and traps to `EXP-007`. The registry points at
entries it no longer contains.

**Nothing was lost permanently.** The rows are intact at `7e6f005` and recoverable exactly.

**Recommended before boundary selection, as its own reviewed change:**

```bash
git show 7e6f005:docs/rules/INVENTORY.md
```

restore the three domain sections and the seven `EXP` rows from that version, preserving the
`CHAR-004`/`CHAR-005`/`EXP-003` rows as they now stand. **I have not done this** — the task
was boundary research, `INVENTORY.md` is an approved artifact, and a 46-line restoration to
it should be authorized rather than folded into a research pass.

The dependency data below is read from `7e6f005` and is therefore sound, but a boundary
approved against a registry that does not contain its own cards would not satisfy §15.1.

---

## 2. What is landed

Nine Rule Cards, three clusters, all merged to `main`.

| Cluster | Cards | State |
|---|---|---|
| `CLUSTER-001` Dungeon Exploration Time | `EXP-001`, `EXP-002` | `VERIFIED` |
| `CLUSTER-002` Character Foundation | `CHAR-001`, `CHAR-002`, `CHAR-003`, `CHAR-007` | `VERIFIED` |
| `CLUSTER-003` Equipped Dungeon Movement | `CHAR-004`, `CHAR-005`, `EXP-003` | Accepted 2026-09-27 |

**Capability today.** A party can be created, equipped from the Chapter 4 catalogs within
its starting money and class legality, have its carried encumbrance derived, move through a
dungeon at a rate the rules derive, and have each turn debited against the landed turn
machinery that fires wandering-monster checks.

**Where it stops.** When a wandering-monster check comes up positive, **nothing happens.**
`EXP-001` produces the event; `EXP-003` §5 names the Encounter Checklist as its
destination; no card in that chain exists. That is the loop's most conspicuous open edge.

---

## 3. The dependency frontier

### 3.1 Unblocked now — every incoming dependency landed

```text
EXP-004   Rest / Exhaustion Procedure        <- EXP-002          [REVALIDATION_REQUIRED]
EXP-006   Light & Exploration Resources      <- EXP-002
EXP-010   Party Formation & Marching Order   <- EXP-002, EXP-003, CHAR-005
ENC-001   Encounter Distance                 <- (none)
ENC-005   Retreat, Pursuit & Evasion         <- EXP-002, EXP-003
COMBAT-001 Combat System                     <- (none; "gates everything below")
COMBAT-004 Saving Throws                     <- CHAR-003, CHAR-007
COMBAT-005 Healing & Natural Recovery        <- (none)
CHAR-006  Retainers & Hirelings              <- CHAR-004
CHAR-008  Alignment & Languages              <- (none)
CHAR-009  Class Special Abilities            <- CHAR-002
CHAR-011  Weapon Mastery                     <- CHAR-002, CHAR-004
CHAR-012  General Skills                     <- CHAR-001, CHAR-007
CHAR-014  Aging                              <- CHAR-001
MAGIC-001 Spell Preparation & Memorization   <- CHAR-002
MAGIC-004 Cleric Turn Undead                 <- CHAR-002
```

### 3.2 Blocked, and by what

```text
CHAR-010  Thief Skills            <- CHAR-009
CHAR-013  High-Level Branches     <- CHAR-009, CHAR-008
EXP-005   Doors / Listening       <- CHAR-010
EXP-007   Traps                   <- CHAR-010
ENC-002   Surprise                <- CHAR-010
ENC-003   Reaction                <- MON-001, CHAR-008
ENC-004   Monster Morale          <- ENC-003, the combat domain
ENC-006   Parley                  <- ENC-003
COMBAT-002/003/006                <- COMBAT-001
TREAS-001 Treasure Type           <- EXP-008
ADV-001   Experience Awards       <- TREAS-001, COMBAT-003, MON-001
ADV-002   Level Advancement       <- ADV-001
ADV-003   Resupply                <- TREAS-004
```

**`CHAR-009` is the highest-leverage single card on the board.** It alone blocks
`CHAR-010`, which blocks `EXP-005`, `EXP-007` and `ENC-002`, and it partly blocks
`CHAR-013`.

### 3.3 A dependency cycle, flagged not resolved

```text
MON-001  Monster Determination  <- EXP-001, EXP-008
EXP-008  Dungeon Stocking       <- MON-001, MON-002, TREAS-001
```

**`MON-001` and `EXP-008` each list the other as an incoming dependency.** Any cluster
containing either must either contain both, or the cycle must be broken by a governance
decision about which owns what. This is recorded here because it will bite whichever
cluster first reaches monsters or treasure, and **it is not resolved by this document.**

---

## 4. Candidate cluster scopes

Four candidates. Each is stated with what it would deliver, what it would need, and what
makes it risky. **None is recommended as the only possibility**, and they are not mutually
exclusive in the long run — only as the *next* cluster.

### Candidate A — Dungeon Encounter Onset

```text
ENC-001  Encounter Distance        MON-001  Monster Determination
ENC-003  Reaction                  MON-002  Number Appearing
ENC-005  Retreat, Pursuit, Evasion CHAR-008 Alignment & Languages
ENC-006  Non-Combat Resolution / Parley
```

**Delivers.** The loop's missing link: a positive wandering-monster check produces an actual
encounter — something appears, at a distance, in a number, with a reaction — and the party
may parley, evade or flee. **It deliberately stops at the decision to fight.**

**Why that stopping point is principled rather than arbitrary.** `AGENTS.md` §5 is explicit
that *"a random encounter is not automatically combat"*, and `EXP-003` §5 already encodes
it. A cluster that implements detection → distance → reaction → evade/parley and *cannot*
resolve a fight is the strongest possible executable statement of that rule.

**Needs.** `CHAR-008` (reaction's incoming dependency). **Hits the `MON-001`/`EXP-008`
cycle** (§3.3). `ENC-002` Surprise is **excluded** — it depends on `CHAR-010`, which is two
cards away.

**Risk.** Medium-high. Six or seven cards, an unresolved dependency cycle, and an encounter
without surprise is a visibly partial mechanic.

### Candidate B — Combat Foundation

```text
COMBAT-001 Combat System        COMBAT-004 Saving Throws
COMBAT-002 Attack Resolution    COMBAT-006 Combat Sequence & Initiative
COMBAT-003 Damage & Death       COMBAT-008/009 (Ch. 19, REQUIRED)
```

**Delivers.** The other half of "make it a game". `COMBAT-001` and `COMBAT-004` are
unblocked now, and `COMBAT-001` gates the rest of its own domain.

**A clean seam already exists.** `CLUSTER-003` deliberately did not transcribe weapon damage
dice, ranges, or armour class — `equipment.py` records that armour class is `COMBAT-*`'s and
the Armor Table's AC column is untranscribed. `CHAR-005` §5 already implements and guards
the combat-sequence movement boundary (`M21`–`M24`). This cluster would extend named,
documented seams rather than cut new ones.

**Needs.** Something to fight. `MON-003` (monster statistics) is catalog-closure and the
research order puts it near-last, so a combat cluster must either define its boundary
against an abstract opponent or pull monster statistics forward.

**Risk.** High. The inventory's own flag 6 calls `COMBAT-003` *"a confirmed, foundational,
material change"* from the prior baseline, and two required Chapter 19 variants attach to
it. This is the project's largest and highest-risk domain.

### Candidate C — Dungeon Exploration Completion

```text
EXP-004  Rest / Exhaustion Procedure     [REVALIDATION_REQUIRED]
EXP-006  Light & Exploration Resources
EXP-010  Party Formation & Marching Order
ENC-005  Retreat, Pursuit & Evasion
```

**Delivers.** Everything the dungeon-exploration half of the loop still lacks that does not
require an encounter to resolve: whether the party can see, how long it can push on, what
order it walks in, and how it disengages.

**All four are unblocked today**, and every one of them has a **named seam left by landed
code**:

| Card | The seam `CLUSTER-003` left for it |
|---|---|
| `EXP-004` | `CHAR-005` §9 implements the 30-round running limit and 3-turn rest. `EXP-004` is `REVALIDATION_REQUIRED` and its old mandatory-hourly-rest state machine is flagged as probably not surviving as RC canon |
| `EXP-006` | `CHAR-004` §A: *"Light-source radius and burn duration → `EXP-006`. This card owns torch and lantern cost and encumbrance only"* |
| `EXP-010` | `EXP-003` case `D32` asserts no formation input exists, and the card records `EXP-010` as **not** an incoming dependency |
| `ENC-005` | `EXP-003` §B routes dungeon *"difficult terrain"* as an evasion condition to `ENC-005` |

**Risk.** Low-medium, and the lowest of the four. Four cards, none blocked, no cycle, no
catalog closure. `EXP-004`'s `REVALIDATION_REQUIRED` status makes it a direct test of
whether `CHAR-005` §9's exhaustion contract survives contact with its own owner — which is
exactly the integration feedback §15.1 says clusters exist to produce.

**Weakness.** It delivers no new *loop* capability. A party that can see, rest and march in
order still cannot resolve the encounter the dungeon throws at it.

### Candidate D — Class Abilities Enabler

```text
CHAR-009  Class Special Abilities & Racial Abilities/Limitations
CHAR-010  Thief Skills
```

**Delivers.** Little on its own — but it unblocks `EXP-005`, `EXP-007`, `ENC-002` and part
of `CHAR-013`, which is more downstream unblocking than any other two cards on the board.

**It also tests three boundaries `CLUSTER-003` asserted.** `CHAR-009`'s inventory row
carries an explicit non-ownership boundary added by the 2026-09-14 governance decision:
mundane equipment legality is `CHAR-004`'s and the authoritative movement rate including
Mystic `MV` is `CHAR-005`'s. Landing `CHAR-009` would be the first real test of whether
those boundaries hold when the card that *describes* those abilities is written.

**Risk.** Medium. `CHAR-009` is broad — nine classes plus racial abilities — and the
inventory rates it medium-high. `CHAR-010` carries the Chapter 13 DM-facing resolution
question.

### Summary

| | Cards | Blocked deps | Loop capability added | Risk |
|---|---|---|---|---|
| **A** Encounter Onset | 6–7 | `CHAR-008` in-scope; `MON`/`EXP-008` cycle | **High** — closes the open edge | Medium-high |
| **B** Combat Foundation | 5–7 | monster statistics | **High** | High |
| **C** Exploration Completion | 4 | none | Low | **Low-medium** |
| **D** Class Abilities | 2 | none | Very low, high unblocking | Medium |

---

## 5. Carried-forward unresolved items

Recorded so none is mistaken for an omission, and so a `CLUSTER-004` boundary can state
which it does and does not touch.

### 5.1 From `CLUSTER-003`

| Item | State | Which candidate would reach it |
|---|---|---|
| **Runtime orchestration ownership** — who calls the create → equip → move → turn chain | **Unowned.** Plan §4.1 forbade an orchestrator inside the cluster | None. Needs its own governance decision |
| **`CHAR-004` §7: a thief with a large net** — RC p. 65 makes a net's handedness size-dependent; §7's prohibition is stated over the printed `2H` marker, which no net row carries | Undecided, recorded in `ISSUE-017` §11 | B (weapon handedness) |
| **`CHAR-004` §7: a dual-role item used as a weapon** — the torch is catalogued as `GEAR`, so §7 does not reach it | Undecided, recorded in `ISSUE-017` §11 | B, or `EXP-006` under C |
| **`CHAR-005` §7 condition modifiers** — 11 approved cases `M49`–`M59`, carrying **`SR-10`** | `NOT V1-WIRED`. Every causation owner is Unresearched | **B** (blindness, stunning, prone → `COMBAT-*`); starvation has **no Rule ID assigned at all** |
| **Chapter 10 high-level equipment pathway** | `NOT V1-WIRED`, preserved on `CHAR-004` §C | None currently |
| **Mounts, vehicles, ships, siege equipment** | Out of V1 by human decision. **No transport responsibility exists in the inventory** | None — assigning one is a governance question |
| **Spatial / grid quantisation** of a fractional allowance | Unowned | `SIM-001`, or a presentation layer |
| **Rough / broken-terrain modifier** presupposed by Mystic Acrobatics | **Unowned by express approval** | Would resurface in `CHAR-009` under D |

### 5.2 Standing open decisions from `INVENTORY.md`

Items 1–5 of *"Major Human Decisions Required"* remain open (6–10 were settled at
`CLUSTER-003` Stage-A closure):

1. Whether any newly discovered RC optional system should be enabled — none found in the
   Chapter 13/15/19 review.
2. **Wilderness Adventures reachability boundary** — still open. Bears on `EXP-004` if its
   wilderness-travel-rest half is in scope, which is Candidate C's main scoping question.
3. Whether encounter-balancing or individual-initiative configurability get built — bears
   on `ENC-007` (A) and `COMBAT-006` (B).
4. **`CHAR-013`'s split-candidate status** — Paladin/Knight/Avenger vs. Druid/Mystic. Bears
   on D, since `CHAR-013` depends on `CHAR-009`.
5. **`EXP-004`'s exact scope once researched** — whether RC-native running-exhaustion and
   wilderness-travel-rest stay one card or split. **This is Candidate C's central question**
   and interacts directly with landed `CHAR-005` §9.

### 5.3 Binding adjudications that constrain future work

- **Class level caps (2026-08-29):** Elf **10**, Druid **36**. Binding on `ADV-002`; RC
  Ch. 1 p. 12 is treated as erroneous summary text. Now also projected in landed
  `encumbrance_and_movement.MAXIMUM_LEVEL`, with a test asserting it matches `CHAR-003`'s
  projection.
- **Five RC-optional systems are required V1 content** (`DEC-0008`): Morale, Weapon Mastery,
  General Skills, Druid, Mystic. Morale is `ENC-004` and lands inside Candidate A's
  neighbourhood but is blocked by the combat domain.
- **Three Chapter 19 variants are required:** ability-based saving throws (`COMBAT-004`),
  Nonlethal Combat (`COMBAT-008`), Mortally Wounded (`COMBAT-009`) — all Candidate B.

---

## 6. Recommendation

**Not a decision — a ranked reading of the evidence, for the human project owner to accept,
reorder or reject.**

1. **Restore the 27 inventory rows first, as its own reviewed change.** §15.1's prerequisite
   is not met until then, and every candidate below is scoped against rows the registry does
   not currently contain.

2. **Then `CLUSTER-004` = Candidate C, possibly narrowed to `EXP-004` + `EXP-006`.** It is
   the only candidate with no blocked dependency and no cycle; every card has a seam a
   landed card explicitly named; and `EXP-004`'s `REVALIDATION_REQUIRED` status makes it a
   genuine test of `CHAR-005` §9 rather than new ground. It is small enough that its Stage-A
   research can absorb the `EXP-004` scope question (open decision 5) without the cluster
   stalling.

3. **`CLUSTER-005` = Candidate D**, to unblock `EXP-005`/`EXP-007`/`ENC-002` and test the
   `CHAR-009` non-ownership boundary while `CLUSTER-003` is still fresh.

4. **Then A, then B.** A needs `CHAR-008` and the `MON-001`/`EXP-008` cycle resolved; B is
   the largest and highest-risk domain and benefits from having `ENC-*` and `CHAR-009`
   settled first.

**The contrary case, stated fairly:** Candidate A closes the loop's only *visible* gap, and
a simulator that rolls a wandering-monster check and then does nothing is a strange thing to
keep building around. If the goal is playable capability soonest rather than lowest risk,
**A is the defensible choice** — and its `CHAR-008` dependency and the `MON`/`EXP-008` cycle
become the first things to settle rather than reasons to wait.

---

## 7. What this document does not do

```text
NO Rule Card drafted            AGENTS.md §9 -- research precedes drafting
NO cluster selected             ARCHITECTURE.md §15.1 -- a human selects
NO implementation               nothing here authorizes code
NO inventory repair performed   recommended in §1, deliberately not done
NO dependency cycle resolved    §3.3 flagged for governance
NO open decision answered       §5.2 left open
```

**Next step: human review of §1 and a choice among §4's candidates, or rejection of all of
them.**
