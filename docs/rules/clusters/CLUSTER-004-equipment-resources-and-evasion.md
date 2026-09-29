# Cluster 4: Exploration Resources and Evasion — Stage-A Record

## 1. Cluster ID

`CLUSTER-004`

## 2. Boundary

```text
EXP-006   Light & Exploration Resources
ENC-005   Retreat, Pursuit & Evasion (underworld)

DEFERRED, NOT IN THIS CLUSTER
    EXP-004   Rest / Exhaustion Procedure          DEFERRED / SPLIT CANDIDATE
    EXP-010   Party Formation & Marching Order     DEFERRED
```

Human-approved 2026-09-27; see `CLUSTER-004-BOUNDARY-CORRECTION.md` for the boundary and
the deferral rationale, and `CLUSTER-004-BOUNDARY-PROPOSAL.md` for the superseded original
analysis.

## 3. Status

```text
BOUNDARY                    APPROVED  2026-09-27
STAGE A (EVIDENCE)          COMPLETE -- READY FOR HUMAN EVIDENCE REVIEW
    EXP-006                 docs/rules/evidence/EXP-006-evidence.md
    ENC-005                 docs/rules/evidence/ENC-005-evidence.md
INDEPENDENT COMPLETENESS
    REVIEW                  docs/rules/evidence/CLUSTER-004-stage-a-completeness-review.md
HUMAN EVIDENCE REVIEW       NOT GIVEN  -- hard gate, DEC-0009
STAGE B (SYNTHESIS)         NOT STARTED, NOT AUTHORIZED
RULE CARDS                  NONE DRAFTED
IMPLEMENTATION              NOT AUTHORIZED
ALTERNATE-SOURCE RESEARCH   NONE PERFORMED; one candidate question flagged (§7)
```

---

## 4. What Stage A found, in one page

### 4.1 The two cards are very different sizes

| | `EXP-006` | `ENC-005` |
|---|---|---|
| Governing objects | **4 item descriptions** | 1 prose section, **1 checklist, 1 table** |
| Governing tables | **none** | Evasion Table (p. 99) |
| Pages | 69–70 | 98–99 |
| Randomised mechanics | 1 (tinderbox `1d6`) | 3 (evasion `d100`, initiative `1d6`, dropped-goods `1d6`) |
| Printed defects found | 0 | **2** |
| Hard deps on unresearched cards | 0 | **4** |
| Research risk (protocol §9.4) | Low | **High** — a table drives the procedure |

**`EXP-006` turned out smaller than its title; `ENC-005` turned out larger than its
dependency cell.** Both findings are boundary-relevant and neither was visible from the
inventory.

### 4.2 `EXP-006` — the inventory's source attribution is wrong

`INVENTORY.md` gives the source as *"Dungeon Adventures chapter"*. **RC has no such
chapter.** Every governing object is in **Chapter 4: Equipment**, in the Adventuring Gear
*descriptions* — the same pages `CHAR-004` was researched from, split cleanly by the source
itself:

```text
p. 69 TABLE        cost, encumbrance             ->  CHAR-004  [LANDED]
p. 69-70 PROSE     radius, burn time, ignition   ->  EXP-006
```

**No duplication exists between the two.** RC states radius and duration only in the
descriptions, and cost and encumbrance only in the table.

**`EXP-006` has no governing table and no checklist** — confirmed from the Index to Tables
and Checklists (p. 301), read visually in full.

### 4.3 `ENC-005` — not underworld-specific, and not really unblocked

RC gives **one** evasion procedure covering dungeon and wilderness together, and separates
only *naval* evasion into its own table. The card title's `(underworld)` is a project
narrowing, not a source boundary.

And although the inventory lists its dependencies as `EXP-002` and `EXP-003` — both landed —
**the printed checklist depends on four unresearched cards**:

```text
step 1  encounter distance    ENC-001      Unresearched
step 2  surprise states       ENC-002      Unresearched
step 3  morale check          ENC-004      Unresearched  (DEC-0008 REQUIRED)
step 5  1d6 initiative        COMBAT-006   Unresearched
step 5a morale, every 5 rnds  ENC-004      Unresearched
step 5b combat checklist      COMBAT-*     Unresearched
step 5  speed comparison      MON-003      Unresearched
```

**This is the cluster's most consequential finding**, and it is the same class of problem
that deferred `EXP-010`: a card whose *listed* dependencies are satisfied but whose
*procedure* is not. See §6 Q2.

---

## 5. Cross-card interactions found

| Interaction | Direction | Disposition |
|---|---|---|
| Oil *"poured out and ignited to delay pursuit"* (p. 69) | `EXP-006` → `ENC-005` | **Recorded from both sides; RC states no mechanic** — no adjustment, no delay value. Nothing invented |
| Chase rounds vs. the 30-round running limit | `ENC-005` → landed `CHAR-005` §9 | **Open — §6 Q4.** RC's evasion section does not say whether chase rounds count |
| *"Evaders rest"* (checklist step 6) | `ENC-005` → `EXP-004` (deferred) | Followed **only to ownership**. `CHAR-005` §9 owns the 3-turn rest. `EXP-004` **not reopened** |
| Running speed, feet per round | `ENC-005` → landed `CHAR-005` | Consumed, not re-derived |
| Burn time in *turns* | `EXP-006` → landed `EXP-002` | Consumed. RC states hours **and** turns itself |
| Torch lit/unlit damage | `EXP-006` → `COMBAT-002`, `CHAR-011` | Routed away. `EXP-006` owns whether it is lit, not what it does |
| Infravision *"does not work in the presence of normal and magical light"* | `EXP-006` ↔ `CHAR-009` | Recorded, **not claimed**. The vision ability is `CHAR-009`'s |

---

## 6. Open questions requiring human decision

**None of these may be answered by an implementation or Stage-B agent.**

| # | Card | Question |
|---|---|---|
| **1** | `ENC-005` | **Is the card underworld-only, or does it own RC's general evasion procedure?** RC does not separate dungeon from wilderness. Narrowing would mean owning part of one indivisible procedure. Interacts with the standing Wilderness reachability decision. **Stage B cannot begin without this** |
| **2** | `ENC-005` | **Can the card be specified before `ENC-001`/`ENC-002`/`ENC-004`/`COMBAT-006`?** Four of six steps reference them. A card could name them as caller-supplied inputs — but that is a contract with four unresearched counterparties, the concern that deferred `EXP-010` |
| **3** | `ENC-005` | **"Difficult terrain" is undefined.** RC gives examples, no criterion. The second-roll escape cannot be executable without a DM-input flag or a terrain mechanic RC does not supply |
| **4** | `ENC-005` | **Do chase rounds count against `CHAR-005` §9's 30-round running limit?** |
| **5** | `ENC-005` | **Scouts adjustment: prose `−10%` vs Evasion Table `−15%`.** `INTERNAL SOURCE CONFLICT REQUIRES REVIEW` |
| **6** | `ENC-005` | **Evasion Checklist step 2 says "go to Step 2"** — a self-loop. Defect reading, or something else? |
| **7** | `EXP-006` | **Tinderbox ignition is stated only for *"normal (comparatively dry) circumstances"*.** No other chance exists. `PRIMARY PROCEDURE NOT YET ESTABLISHED` for non-normal conditions |
| **8** | `EXP-006` | **RC states no consequence for having no light.** May be deliberate DM delegation rather than an omission. **Not resolved** |
| **9** | `EXP-006` | **Do rations belong to this card?** Its title says *"& Exploration Resources"*, and rations carry a real spoilage rule. **No ownership claimed** — answering it inside Stage A would be silent scope expansion |
| **10** | `EXP-006` | **Is a burn-tracking procedure in scope?** RC gives durations but no procedure for decrementing them and no rule for expiry |
| **11** | `ENC-005` | **Which "retreat" does the card own?** RC's `Retreat` is a **Chapter 8 combat maneuver** (p. 104) — within a combat round, forfeits the shield bonus, grants enemies +2. The card's title claims the word. Found late, by the General Index visual pass; see the packet's §14.1 |
| **12** | `ENC-005` | **Does the Fighting Withdrawal → running speed bridge belong here or to `COMBAT-*`?** It is RC's printed transition from a combat round into a chase |
| **13** | `ENC-005` | **Does `CHAR-012`'s Caving skill modify step 6?** *"If he is forced to flee for a long stretch, he must make a skill check to keep from being lost"* |

---

### 6.1 A late finding that reflects on the research, not only on the cards

**Two governing objects were missed by the first pass and found only by a visual read of
the General Index**, after both packets had been drafted: `ENC-005`'s `Retreat maneuver`
(p. 104) and `Lost` (p. 89). Both are recorded in that packet's §14 as an addendum rather
than folded in silently.

Neither changes a percentage, a step or a die roll in the transcribed procedure — they are
**boundary evidence**. But they were missed, and precedent `P-001` exists in this repository
precisely because a `CLUSTER-003` pass once skipped the General Index. **The instrument
caught something again.** The independent completeness review has been asked to judge the
packets with that in view.

`Lost . 89` also produced a clean negative worth stating on its own: **RC provides no
dungeon getting-lost mechanic.** Its `Becoming Lost` procedure is per-day, wilderness, and
sits in the Game *Day* Checklist. This sharpens Q1.

## 7. Alternate-source research

**None performed. None authorized. One candidate flagged.**

`ENC-005`'s two printed defects (§6 Q5, Q6) are **internal RC conflicts**. The BECMI Expert
set is known to carry an evasion procedure, and a lineage check might disambiguate both —
**but that lookup is outside the current authorization**, and `DEC-0011` gap research is
gap-directed and requires a documented gap plus human authorization.

**Flagged as a candidate `DEC-0011` question** if the human project owner prefers lineage
disambiguation over adjudicating the conflicts as Simulator Rulings. AD&D remains excluded.

---

## 8. Boundaries respected

```text
EXP-004   NOT researched as a unified card. The step-6 rest reference was
          followed only far enough to establish that CHAR-005 §9 owns the
          running/exertion half. No wilderness rest material inspected.

EXP-010   NOT absorbed. ENC-005's procedure needs party SIZE, not marching
          order; no formation, rank or order appears in the section.

EXP-008 / MON-001 / TREAS-001   UNTOUCHED. The wilderness and city encounter
          subtables printed on pp. 97-98 -- the same pages as the evasion
          section -- were excluded by name.

TERRAIN   No generic terrain mechanic created. The Evasion Table's condition
          column adjusts an evasion PERCENTAGE, not a movement rate. The
          unowned rough/broken-terrain modifier was not imported and the
          Mystic Acrobatics material was not consulted.

CHAR-004  NOT reopened. No price, encumbrance, Coin, quantity-pricing or
          legality fact is restated or duplicated.
```

---

## 9. Simulator Rulings

**None proposed.** Protocol §16 and `AGENTS.md` §10.7 place rulings last, after gap-directed
alternate-source research, and no such research has been authorized or performed.

Two of `ENC-005`'s open questions (§6 Q5, Q6) are **ruling candidates** if lineage research
is declined — recorded so, and no further.

---

## 10. Relationship to landed clusters

| Cluster | What `CLUSTER-004` takes from it |
|---|---|
| `CLUSTER-001` — Dungeon Exploration Time | The 10-minute turn `EXP-006`'s burn durations are stated in |
| `CLUSTER-002` — Character Foundation | Nothing directly |
| `CLUSTER-003` — Equipped Dungeon Movement | `CHAR-004`'s catalogued torch/lantern/oil/tinderbox rows; `CHAR-005`'s running speed and its §9 exhaustion contract; `EXP-003`'s scale boundary |

---

## 11. Next step

```text
HUMAN EVIDENCE REVIEW -- a hard gate under DEC-0009 §6.

Stage B may not begin without explicit human authorization, and §6 Q1 and Q2
should be settled as part of that authorization: they determine whether
ENC-005 can be synthesized at all in this cluster, or whether it should join
its four unresearched counterparties in a later encounter cluster.
```
