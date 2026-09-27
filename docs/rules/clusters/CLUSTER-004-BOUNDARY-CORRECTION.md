# CLUSTER-004 — Boundary Correction After Inventory Restoration

```text
STATUS:  ACTIVE BOUNDARY RECORD -- supersedes the recommendation in
         CLUSTER-004-BOUNDARY-PROPOSAL.md (fc9ebe9)

ACTIVE BOUNDARY (human-approved 2026-09-27):

    KEEP      EXP-006   Light & Exploration Resources
              ENC-005   Retreat, Pursuit & Evasion (underworld)

    DEFERRED  EXP-004   Rest / Exhaustion Procedure
              EXP-010   Party Formation & Marching Order

STAGE A:  NOT STARTED, NOT AUTHORIZED
```

> **This document corrects a boundary proposal that was produced against an incomplete
> inventory.** The earlier proposal (`fc9ebe9`) is **deliberately preserved unaltered** —
> its analysis, and the fact that it was made on bad data, are project history. This record
> states what changed and what did not.
>
> Prepared 2026-09-27, immediately after the inventory restoration (`6c5c73a`).

---

## 1. The defect, and why the earlier analysis was incomplete

Commit **`5208798`** (2026-09-24, *"CLUSTER-003 Stage B"*) deleted 46 lines from
`docs/rules/INVENTORY.md` while rewriting three rows. Four deletions were legitimate
replacements; **42 lines were lost outright** — 27 Rule Card rows across four domains, plus
three section headers and their table headers:

```text
EXP-004 .. EXP-010     7 rows   (incl. EXP-004's REVALIDATION_REQUIRED status)
ENC-001 .. ENC-007     7 rows
MON-001 .. MON-004     4 rows
COMBAT-001 .. COMBAT-009   9 rows
```

It was unintended collateral damage from a scripted edit, introduced by this project's
agent. **It went uncaught through `CLUSTER-003`'s Rule Card approval, its Pre-Code Gate,
six implementation slices, an independent transcription review, and the merge to `main`**,
and surfaced only when the `CLUSTER-004` boundary research tried to read the dependency
frontier.

**Why the earlier frontier analysis was incomplete, precisely.** The proposal reconstructed
the missing rows from `INVENTORY_MIGRATION_MAP.md`, `RC_V1_SCOPE_AUDIT.md` and a `git show`
of `7e6f005`. That recovered the *existence* of the rows and their `Dependencies` cells, but
**not their `Downstream Consumers`, `Status` or `Risk / Notes` columns** — which is exactly
where the two findings that changed the boundary were sitting. The analysis was therefore
not merely unverified; it was **structurally unable to see the columns that mattered**.

Restored by `6c5c73a`: 42 insertions, 0 deletions, verbatim from `7e6f005`, with the current
amended `CHAR-004`, `CHAR-005` and `EXP-003` rows preserved and not reverted.

---

## 2. What changed, and what did not

### 2.1 Conclusions that changed — all from columns the defect hid

| # | Earlier conclusion (`fc9ebe9`) | Corrected conclusion | Hidden by the defect? |
|---|---|---|---|
| 1 | Candidate C is four clean cards, *"every card has a seam a landed card explicitly named"* | **Two are clean; two must be deferred.** See §3 and §4 | **Yes** — `EXP-004`'s `Risk / Notes` and `EXP-010`'s `Downstream Consumers` were both in deleted rows |
| 2 | The dungeon-stocking cycle is two-node: `MON-001 <-> EXP-008` | **Three responsibilities form one coupled knot:** `EXP-008 <-> MON-001` **and** `EXP-008 <-> TREAS-001`. See §5 | **Yes** — `EXP-008`'s full dependency cell was deleted |
| 3 | `EXP-005` waits on `CHAR-010` | `EXP-005` waits on `CHAR-010` **and `ENC-002`** — and `ENC-002` itself waits on `CHAR-010`, so it is two hops deep | **Yes** |
| 4 | `ENC-007` waits on `MON-001` and `EXP-001` | Waits on **`MON-001` only**; `EXP-001` is landed | **Yes** |
| 5 | `TREAS-004` waits on `TREAS-003` | Waits on `TREAS-003` **and `CHAR-009`** | **Yes** |
| 6 | 16 unblocked Rule Cards | **16 unblocked Rule Cards** — unchanged, but now computed from the full registry rather than a reconstruction | No |

### 2.2 Conclusions that remain valid

- **The defect finding itself**, and that §15.1's prerequisite was unmet. Correct, and the
  reason this correction exists.
- **`EXP-006` and `ENC-005` are unblocked and clean.** Confirmed against their restored
  rows: dependencies landed, `Medium` risk, no flags, no ownership conflict.
- **`CHAR-009` is the highest-leverage single card.** Strengthened, not weakened — the
  restored rows show it also blocks `TREAS-004` and, through `CHAR-013`, `MAGIC-006`.
- **Candidates A, B and D are unchanged** in shape and in their relative risk.
- **The loop's open edge is real:** a positive wandering-monster check still resolves to
  nothing.
- **`SIM-001` and `SIM-002` remain excluded** from the unblocked Rule Card count. They are
  design tasks whose dependency cells contain prose, not research entries, and they are
  **not** recategorised here.

### 2.3 What was **not** rolled back

**No substantive later work is reverted.** The defect was discovered late; that is a reason
to repair forward, not to rewind.

```text
PRESERVED   CLUSTER-003 -- all three Rule Cards, six slices, merged at c3a3e2d
PRESERVED   CHAR-004, CHAR-005, EXP-003 at their current amended states
PRESERVED   every commit after 5208798
PRESERVED   fc9ebe9, the superseded proposal, unaltered
```

**No dependency contradiction was demonstrated between the restored rows and any landed
work**, and none is asserted. `CLUSTER-003`'s three cards depend only on `CHAR-001`–`CHAR-005`,
`CHAR-007`, `EXP-002` and `EXP-003`, none of which was ever deleted.

---

## 3. `EXP-004` — DEFERRED / SPLIT CANDIDATE

**Removed from the active boundary.**

The restored row shows the apparent card combines two responsibilities that must not be
treated as one executable object:

### A. Running / exertion recovery — **already owned and implemented**

```text
OWNER:  CHAR-005 §9  (approved, implemented, merged)
    30-round running limit          MAXIMUM_RUNNING_ROUNDS
    3-turn rest requirement         REQUIRED_REST_TURNS, is_rested()
    exhaustion consequences         ExhaustionPenalty
```

**This behaviour must not be duplicated in `EXP-004`.**

### B. Wilderness / travel-scale rest — **gated**

Waits on the **Wilderness Adventures reachability boundary**, standing open decision 2 in
`INVENTORY.md`, which is **not resolved by this repair** and is not resolved here.

### Disposition

```text
DEFERRED / SPLIT CANDIDATE

- dungeon/exertion responsibility already owned by CHAR-005 §9
- wilderness/travel-scale rest waits on the Wilderness Adventures
  reachability decision
- these mechanics must not be conflated
```

**`EXP-004` is not to be researched or implemented as a unified card.** Its restored row
already carries `REVALIDATION_REQUIRED` and its own `SPLIT CANDIDATE` flag, and its notes
state the point directly: *"These must not be conflated with each other or with the old
dungeon-rest mechanic."*

---

## 4. `EXP-010` — DEFERRED

**Removed from the active boundary**, although it is technically dependency-unblocked
(`EXP-002`, `EXP-003`, `CHAR-005` are all landed).

Its restored row names its downstream consumers:

```text
ENC-002  Surprise        Unresearched
ENC-003  Reaction        Unresearched
COMBAT-006  Initiative   Unresearched
```

**All three are unresearched**, so marching order would land a contract **no researched
consumer requires**. Building it now would mean designing formation state around
assumptions about future surprise, reaction, initiative and encounter resolution — the
speculative abstraction this project explicitly avoids (`ARCHITECTURE.md` §4.1's lineage;
`AGENTS.md` §2).

This is also what landed `EXP-003` already observed: approved case **`D32`** asserts that no
formation input exists, and the card records `EXP-010` as **not** an incoming dependency.

### Disposition

```text
DEFERRED

No researched consumer currently requires the contract.

Revisit EXP-010 when ENC-002, ENC-003, or COMBAT-006 reaches research and
can establish the concrete formation/marching-order inputs it actually
needs.
```

---

## 5. Corrected dependency cycle — a three-member coupled knot

```text
EXP-008  <->  MON-001
EXP-008  <->  TREAS-001
```

```text
EXP-008    Dungeon Stocking                 <- MON-001, MON-002, TREAS-001
MON-001    Monster Determination            <- EXP-001, EXP-008
TREAS-001  Treasure Type Generation         <- EXP-008
```

**Dungeon stocking, monster determination and treasure generation are one coupled research
knot**, not three independently researchable cards. `MON-002` hangs directly off it, and
`ADV-001` (experience awards) sits downstream of both `TREAS-001` and `MON-001`.

**The cycle is recorded, not broken.** When this area becomes active it is to be treated as
a single coupled research cluster covering all three. Specifically, it must **not** be
broken by:

```text
- inventing provisional interfaces
- choosing an arbitrary implementation order
- assigning ownership without source research
- treating any one member as independently research-complete
```

**This is a future-boundary finding only.** No research into it is authorized or begun.

---

## 6. Updated frontier

| | |
|---|---|
| **Total Rule Card rows** | **59** (was 32 while the defect stood) |
| **Referenced IDs with no row** | **0** (was 26) |
| **Unblocked Rule Cards** | **16** — excluding `SIM-001`/`SIM-002`, which are design tasks |
| **Active boundary** | `EXP-006`, `ENC-005` |
| **Deferred from the boundary** | `EXP-004` (§3), `EXP-010` (§4) |

**The 16 unblocked cards:**

```text
CHAR-006  CHAR-008  CHAR-009  CHAR-011  CHAR-012  CHAR-014
COMBAT-001  COMBAT-004  COMBAT-005
ENC-001  ENC-005
EXP-004  EXP-006  EXP-010
MAGIC-001  MAGIC-004
```

`EXP-004` and `EXP-010` appear here because they are dependency-unblocked. They are
nonetheless **deferred from the active boundary** for the reasons in §3 and §4 — dependency
readiness is not the only criterion.

### Open boundary / reachability decisions still unresolved

1. **Wilderness Adventures reachability boundary** — open decision 2. **Gates `EXP-004`'s
   half B.**
2. Whether any newly discovered RC optional system should be enabled — none found.
3. Whether encounter-balancing / individual-initiative configurability get built — bears on
   `ENC-007` and `COMBAT-006`.
4. **`CHAR-013`'s split-candidate status** — bears on `CHAR-009`'s cluster.
5. **`EXP-004`'s exact scope** — open decision 5, now sharpened by §3: half A is already
   owned by `CHAR-005` §9.
6. **Runtime orchestration ownership** — unowned, carried forward from `CLUSTER-003`.
7. **The `EXP-008`/`MON-001`/`TREAS-001` knot** — §5, recorded not resolved.
8. **Starvation has no Rule ID anywhere in the inventory**, and is a causation owner
   `CHAR-005` §7 depends on. Confirmed still true against the restored registry.

---

## 7. What this document does not do

```text
NO Stage A research begun       not authorized; no research stub is required
                                by DEVELOPMENT_WORKFLOW.md, and CLUSTER-003's
                                boundary record stood alone before its Stage A
NO Rule Card drafted
NO implementation
NO restored row edited          cluster membership lives here, not in the registry
NO dependency cycle broken      §5 recorded for a future boundary
NO open decision answered       §6 left open
NO earlier work rolled back     §2.3
```

**Next step: human authorization of Stage-A research for `EXP-006` and `ENC-005`, or a
different boundary.**
