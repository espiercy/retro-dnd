# CLUSTER-003 — Pre-Code Gate Record

> **Gate performed 2026-09-24**, on explicit human authorization following approval of all three `CLUSTER-003` Rule Cards.
>
> **This record is a readiness assessment. It does not authorize implementation.** `ARCHITECTURE.md` §15.2 step 4 — implementation-readiness (re-)approval — is a **human** act and has **not** been given for `CLUSTER-003`.

---

## 0. Outcome

```text
CLUSTER-003 PRE-CODE GATE:            PASS

ARCHITECTURE.md SS15.1 readiness
  criteria 1-5:                       ALL SATISFIED

ARCHITECTURE.md SS15.2 migration gate
  step 1  RC V1 inventory approved    SATISFIED (2026-08-16, global)
  step 2  cluster boundary approved   SATISFIED (2026-09-14)
  step 3  required Rule Cards
          APPROVED under the
          current hierarchy           SATISFIED (2026-09-24)
  step 4  implementation readiness
          (re-)approved               NOT GIVEN -- human act, outstanding

BLOCKING DEFECTS:                     NONE
NON-BLOCKING CAUTIONS:                THREE (SS6)
                                      caution 2 RESOLVED 2026-09-25
                                      by approved CHAR-005 amendment

IMPLEMENTATION:                       NOT AUTHORIZED
IMPLEMENTATION PLAN:                  NOT DRAFTED (SS1.2)
READY FOR IMPLEMENTATION PLANNING:    YES
```

**A `PASS` here does not authorize implementation.** It records that the cluster is dependency-complete and internally coherent enough for the *implementation-planning* phase to begin, if and when the human project owner authorizes it.

## 1. Procedure Used

### 1.1 Which gate this is

The repository defines two distinct gates, and they are not interchangeable:

| Gate | Scope | Status |
|---|---|---|
| **`ARCHITECTURE.md` §16 — Pre-Code Development Gate** | **Project-wide**, eight foundational documents | **`CLEARED` 2026-08-15.** Not re-performed per cluster; nothing in this record touches it |
| **`ARCHITECTURE.md` §15.2 — Rules Baseline Migration Gate** | **Per-cluster**, four steps | The per-cluster gate. Steps 1–3 assessed here; **step 4 is the human's** |
| **`ARCHITECTURE.md` §15.1 — cluster readiness criteria** | **Per-cluster**, five criteria | The substantive readiness test, applied in §2 |

**No new checklist was improvised.** §15.1's five criteria and §15.2's four steps are the repository-defined procedure, and they are what was executed. The additional challenges in §3–§5 are the ones the authorizing instruction named; they sit **inside** criterion 5, not alongside it.

### 1.2 Why no implementation plan was drafted

The authorizing instruction permitted drafting an implementation plan **only if the repository's formal gate procedure explicitly requires one as a gate artifact**. It does not.

`ARCHITECTURE.md` §15.2's status-update entries for `CLUSTER-001` and `CLUSTER-002` each *record* an authoritative implementation plan alongside step 4. That is a record of what those clusters produced, not a stated precondition of the gate. The repository's own history is explicit on the ordering: `CLUSTER-002`'s Pre-Code gate was performed and reported **before** any plan existed, and the plan was drafted later, under a **separate** human authorization.

```text
PRECEDENT (CLUSTER-002):

  Pre-Code gate report   ->  blocker found and resolved
                         ->  SEPARATE human authorization to draft a plan
                         ->  plan drafted, revised x4, human-approved
                         ->  SS15.2 step 4 re-approved
                         ->  implementation authorized
```

**A gate artifact and an authorization to implement are different things**, and an implementation plan is neither — it is the *input* to step 4, produced after the gate passes and on its own authorization. **No plan was drafted.**

## 2. `ARCHITECTURE.md` §15.1 — the five readiness criteria

| # | Criterion | Finding |
|---|---|---|
| **1** | Intended behavioral scope clearly defined | **SATISFIED.** The boundary is human-re-approved (2026-09-14) at three cards, with five recorded ownership decisions and explicit V1 exclusions. The behavioural chain is stated end-to-end in §3 |
| **2** | All historical rules directly required to execute that scope identified | **SATISFIED.** Stage A passed independent `DEC-0010` completeness certification after one remediation; `DEC-0011` BECMI research closed the seven authorized questions after one remediation. Every required RC object is cited on a card |
| **3** | All Rule Cards required by that scope are `APPROVED` | **SATISFIED 2026-09-24.** `CHAR-004`, `CHAR-005`, `EXP-003` — all three human-approved |
| **4** | Any external dependency not implemented in the cluster has a stable approved contract sufficient for integration | **SATISFIED.** See §4 |
| **5** | No unresolved rules ambiguity remains that the implementation agent would need to adjudicate itself | **SATISFIED.** All seven blocking source questions were adjudicated by the human on 2026-09-24 (`SR-6`–`SR-10`, plus two non-rulings). The residual items in §6 do **not** require an implementer to adjudicate — each has either an established in-repo pattern or an unreachable trigger |

## 3. The Required Chain — verified end to end

```text
created character                 CHAR-001/002/003/007  [LANDED, VERIFIED]
        |                         supplies: class, level (caller-validated),
        |                                   ability scores, hit points
        v
legal personal mundane equipment  CHAR-004 SS5, SS7      [APPROVED]
        |                         per-class permission predicates for all
        |                         nine classes; Druid pricing; unlisted-item
        |                         procedure
        v
carried load / encumbrance        CHAR-004 SS6           [APPROVED]
        |                         Enc (cn) per item, including the four
        |                         DERIVED cases; SR-6 belt pouch = 52 cn
        v
authoritative movement rate       CHAR-005 SS2-SS7        [APPROVED]
        |                         six-band table; normal/encounter/running;
        |                         SR-8 Suit Armor = 750 cn only;
        |                         SR-9 Mystic MV gate; SS6.1 running
        v
dungeon movement                  EXP-003 SS2-SS5        [APPROVED]
        |                         normal speed spent per turn; feet indoors;
        |                         10' default square; Game Turn Checklist
        v
authoritative dungeon time        EXP-002               [LANDED, VERIFIED]
        |                         DungeonTimeAccounting.complete_ordinary_turn()
        |                         -> TurnCredit
        v
existing wandering-check cadence  EXP-001               [LANDED, VERIFIED]
                                  1d6 every other turn, dungeon on a 1
```

**Every link is either an approved card or landed, verified production code. There is no gap in the chain.**

### 3.1 Interface checks against the landed code

| Interface | Landed signature | Consumption | Verdict |
|---|---|---|---|
| `EXP-003` → `EXP-002` | `DungeonTimeAccounting.complete_ordinary_turn() -> TurnCredit` | `EXP-003` §5 runs one Game-Turn-Checklist iteration and §1 declares the turn an input from `EXP-002`; D28 delegates turn credit rather than re-implementing it | **COHERENT.** `TurnCredit` carries `turn_number` + `origin` and explicitly no movement, encounter or presentation data — `EXP-003` neither needs nor supplies any of it |
| `EXP-002` encounter path | `resolve_encounter(encounter_rounds) -> tuple[TurnCredit, ...]` | `EXP-003` §5 step 1/3c **diverts** to the Encounter Checklist rather than resolving it | **COHERENT.** No second time authority is created |
| Level input | `hit_point_gain(rng, cls, level, constitution)` — landed `CHAR-003` takes level as an **explicit caller parameter**, validated against a per-class maximum | `CHAR-005` §6 indexes Mystic `MV` by level | **COHERENT in substance**, imprecise in wording — see §6 caution 2 |

## 4. Criterion 4 — external dependencies

| Dependency | Status | Sufficient for integration? |
|---|---|---|
| `CHAR-002` — class | **`APPROVED` / `IMPLEMENTED` / `VERIFIED`** | **Yes.** Supplies the class that `CHAR-004` §7 and `CHAR-005` §6 key on. Its §A downstream pointer was corrected 2026-09-14 to route mundane equipment legality to `CHAR-004` — **no duplicated authority** |
| `EXP-002` — dungeon turn | **`VERIFIED`**, landed | **Yes.** §3.1 |
| `EXP-001` — wandering check | **`VERIFIED`**, landed | **Yes.** `EXP-003` §5 delegates steps 1 and 4 |
| `CHAR-009` — class abilities | **Unresearched** | **Not required.** Human Decisions 1 and 2 (2026-09-14) assign mundane equipment legality to `CHAR-004` and the authoritative movement rate to `CHAR-005`. **No whole-card dependency exists** — verified in §5 |
| `CHAR-010` — thief skills | **Unresearched** | **Not required.** `CHAR-004` supplies thieves' tools as an item; the *ability* is `CHAR-010`'s and is not exercised by this cluster |
| `TREAS-004` — magic-item use | **Unresearched** | **Not required.** The Mystic protective-device prohibition is routed there and is **not** a mundane-equipment predicate |
| `CHAR-012` — Endurance skill | **Unresearched** | **Not required.** `CHAR-005` §9 names it as the optional extension of the running limit and **specifies nothing**; the base 30-round limit is complete without it |
| `EXP-005`/`EXP-006`/`EXP-007`/`ENC-002`/`ENC-005` | **Unresearched** | **Not required.** `EXP-003` §5 step 2 declares those actions and routes their **resolution** away; no clause of this cluster resolves one |
| `ADV-*` — advancement | **Unresearched** | **Not required** — see §6 caution 2 |
| `COMBAT-*` — condition causation | **Unresearched** | **Not required** — see §6 caution 1 |

## 5. Challenges Performed

Each challenge named in the authorizing instruction, with its finding.

| # | Challenge | Finding |
|---|---|---|
| 1 | **Missing dependencies** | **NONE BLOCKING.** §4. Every unresearched neighbour is either routed-away or names-without-specifying |
| 2 | **Ownership leakage / duplicated authority** | **NONE.** `CHAR-004` owns `Enc` values and never computes movement (guard E60). `CHAR-005` owns the rate and never sets item values. `EXP-003` consumes the rate and never re-derives it (D29) or re-implements turn credit (D28). Suit Armor's `750 cn` is stated on `CHAR-004` §6.1 and its *consequence* on `CHAR-005` — value and consequence, not two authorities. `CHAR-002`'s downstream pointer was corrected; `CHAR-009`'s `INVENTORY` row carries an explicit non-ownership boundary |
| 3 | **Contradictions between the three cards** | **NONE FOUND.** Shared constants cross-checked: Suit Armor `750 cn` (both cards agree); coin weight `1 cn ≈ 1/10 lb` (both agree); the six-band table appears once, on `CHAR-005`; container capacities appear once, on `CHAR-004`; `10′` map square appears once, on `EXP-003`. No value is stated twice with different content |
| 4 | **Contradictions with landed Rule Cards** | **NONE FOUND.** `CHAR-002` §A explicitly disclaims equipment legality; `EXP-002`'s `TurnCredit` carries no movement data and `EXP-003` supplies none; `EXP-001`'s cadence is delegated unchanged (D24). `CHAR-007` is not reached — RC has no Strength-based encumbrance adjustment, so no dependency was invented to create one |
| 5 | **Unresolved source questions that actually prevent implementation** | **NONE.** All seven were adjudicated 2026-09-24. The RC's internal inconsistencies remain unresolved *as history* — but every one has a determinate simulator behaviour, which is what implementation requires |
| 6 | **Ambiguous inputs or outputs** | **ONE, non-blocking** — the level input's stated provenance. §6 caution 2 |
| 7 | **Missing deterministic cases** | **ONE AREA, non-blocking** — composition of condition multipliers. §6 caution 1. Otherwise dense: 60 + 76 + 32 = **168 cases**, covering every band boundary (`400/401`, `800/801`, `1200/1201`, `1600/1601`, `2400/2401`), every class-legality branch in both directions, and explicit **guard** cases asserting the *absence* of prohibited mechanics |
| 8 | **Undefined arithmetic, units, boundaries, transitions** | **NONE BLOCKING.** Units are explicit throughout (`cn`; feet per turn; feet per round; feet indoors / yards outdoors). Band boundaries are inclusive and tested on both sides. The `SR-9` transition is a stated threshold at `400/401 cn`, tested at M33/M34. Fractional arithmetic is explicitly rational and explicitly unrounded |
| 9 | **Accidentally invented mechanics** | **NONE FOUND.** Actively guarded: M29 (no generic equipment-override pathway), M37 (no proportional Mystic scaling), M38 (no encumbrance immunity), M46 (no rounding), M75 (no "personal possessions" restriction), M76/D18/D19 (no terrain mechanic), D13–D15 (no mapping roll, failure state or penalty) |
| 10 | **Inappropriate abstractions introduced to accommodate source defects** | **NONE FOUND — and this was the sharpest test.** `SR-8` is the case where an abstraction would have been tempting: preserving Suit Armor's `30' (10')` would have required either a general "specific equipment overrides general encumbrance" framework or proportional scaling. **The ruling refused both and reduced Suit Armor to a plain `750 cn`.** No card contains an override framework, a scaling rule, or a rounding convention |
| 11 | **V1-deferred behaviour accidentally treated as required** | **NONE.** Chapter 10 equipment is `NOT V1-WIRED` and guarded (E59); mounts/vehicles/ships/siege are out of V1 and guarded (E58); spatial quantisation is unowned and guarded (D31); the rough-terrain modifier is unowned and guarded (M76) |
| 12 | **Class-specific behaviour incorrectly generalized** | **NONE.** Mystic `MV` is explicitly Mystic-only (M39). Druid's `+50%` is explicitly class-specific (E52). The Magic-User dagger ruling is explicitly scoped to the dagger and leaves note `w`'s effect on the other eight weapons intact |

### 5.1 The three sensitive boundaries, verified specifically

**Equipment — can implementation represent each required case?**

| Required representation | Where | Verdict |
|---|---|---|
| Item encumbrance | `CHAR-004` §6.1 | **YES** |
| Filled containers | §6.2 + E7–E11 | **YES** — `container + contents`, with capacity a hard limit (E13) |
| Worn-vs-packed clothing | §6.2 + E14–E16 | **YES** — worn contributes `0` |
| Ammunition inverse encumbrance | §6.2 + E23–E24 | **YES** — the `Enc` column is *shots per `cn`*, recorded as a column semantic OCR destroys |
| Nets/whips sized by dimension | §6.2 + E17–E19 | **YES** — `1 cn`/sq ft, `10 cn`/ft |
| Legal class equipment predicates | §7 + E26–E50 | **YES** — all nine classes, both directions |
| Druid equipment pricing | §7 + E51–E52 | **YES** — `+50%`, class-specific |
| Magic-User dagger baseline | `SR-7` + E26/E36/E37 | **YES** — unconditional, and provably independent of the expanded-list flag |
| **Suit Armor as ordinary `750 cn`, no override** | `SR-8` + M25–M30 | **YES** — and M28/M29 assert that no special rate and no override pathway exist |

**Mystic movement — is the contract unambiguous?**

```text
CHAR-005 SS6, as approved:

    if total encumbrance <= 400 cn:   use level-dependent Mystic MV
    else:                             use the standard encumbrance table

    while enhanced MV is active:
        normal     = MV        feet per turn
        encounter  = MV x 1/3  feet per round   EXACT
        running    = MV        feet per round   [SS6.1, approved 2026-09-24]
```

**YES — unambiguous, and all three prohibitions are guarded:** no proportional scaling (M37), no rounding (M46/M47), no encumbrance immunity (M36/M38).

**Dungeon movement — does it consume without inventing?**

| Required | Verdict |
|---|---|
| Consumes the already-derived authoritative rate | **YES** — §1 declares it an input; D29 delegates the party rate to `CHAR-005` §8 |
| Advances the already-landed dungeon-time procedure | **YES** — D28 delegates to `EXP-002`; §5 runs the checklist |
| Charges no extra mapping time | **VERIFIED** — §4 states the double-count prohibition explicitly; D12/D17 |
| Invents no mapping roll | **VERIFIED** — D13–D15 |
| Invents no special terrain | **VERIFIED** — §7; D18–D20 |
| Creates no second movement authority | **VERIFIED** — D4/D5 refuse encounter and running speed as exploration rates; D6 refuses normal speed inside combat |

## 6. Non-Blocking Implementation Cautions

**None of these blocks the gate.** Each is recorded so it is addressed during implementation planning rather than discovered mid-implementation — which is exactly how `CLUSTER-002`'s ability-score ceiling defect reached its Pre-Code gate.

### Caution 1 — condition-driven movement modifiers are specified but currently unreachable

`CHAR-005` §7 specifies movement effects for blindness, stunning, prone and starvation, including **`SR-10`**. Two things are true at once:

1. **No landed or approved card can produce any of those conditions.** Causation was assigned elsewhere by human Decision 5 (2026-09-14), and **every** prospective owner is `Unresearched`. Within the implementable cluster, the conditions cannot arise.
2. **Composition is unstated.** Neither RC nor the cards state how two simultaneous conditions compose (blind *and* starving), nor the order of a condition multiplier relative to the `SR-9` gate.

**Why this does not block.** Criterion 5 asks whether an implementation agent would have to **adjudicate**. Because the conditions are unreachable, no such decision arises inside the cluster's executable scope.

**Smallest recommended handling** — one of, chosen by the human at planning time:

```text
(a)  the implementation plan marks CHAR-005 SS7 SPECIFIED BUT NOT
     V1-WIRED, following the existing CHAR-003 W3 precedent; or
(b)  the human states the composition rule, if SS7 is to be wired.
```

**Option (a) discards nothing** — `SR-10` remains an approved, recorded ruling whose trigger is simply not yet reachable.

### Caution 2 — the level input's stated provenance is imprecise — **RESOLVED 2026-09-25**

> **Closed by human-approved amendment to `CHAR-005`, 2026-09-25.** New §1.1 states level as an **explicit caller input**, structurally and domain validated at the entry boundary and bounded by the applicable per-class maximum (Mystic 16), following the landed `CHAR-003` pattern. The two incorrect dependencies were **removed and none added**. The card remains `APPROVED`; no ruling, value, band, threshold or deterministic case changed. See `CHAR-005` Amendment History.
>
> The original finding is preserved below as written.


`CHAR-005` §1 states the level input as *"from `CHAR-002` / `ADV-*`"*. **`CHAR-002` does not supply level**, and **`ADV-*` is `Unresearched`**.

**Why this does not block.** The repository already has a landed answer requiring no adjudication: `CHAR-003`'s `hit_point_gain(rng, cls, level, constitution)` takes **level as an explicit caller-supplied parameter**, structurally validated at the entry boundary and range-checked against a per-class maximum. `CHAR-005` §6 needs exactly that, and its maximum is already on the card (Mystic 16, M40).

**Smallest recommended handling.** The implementation plan specifies level as an explicit validated caller input following the `CHAR-003` pattern. **This is a wording imprecision in an approved card's input provenance, not a contract defect** — it is recorded here rather than amended unilaterally, because amending an approved card is a governance act requiring the human amendment path (`CHAR-001`'s 2026-09-05 amendment is the precedent).

### Caution 3 — currency representation

`CHAR-004` E51 expresses the Druid surcharge as **`4.5 gp`**. RC's own denominations make this exact (`4 gp 5 sp`), but a float `gp` representation would be lossy and would compound across a purchase list.

**Smallest recommended handling.** The implementation plan specifies a **base-unit integer currency** (copper pieces, with RC's stated `1 pp = 5 gp = 10 ep = 50 sp = 500 cp`), so `4.5 gp = 450 cp` exactly. **No rule changes** — this is a representation decision, directly analogous to `CHAR-005`'s approved requirement that fractional movement stay exact rather than becoming a lossy float (M47).

## 7. §15.2 Migration-Gate Step Status

| Step | Requirement | Status |
|---|---|---|
| **1** | RC V1 Rules Inventory approved | **SATISFIED** — 2026-08-16, global; unchanged |
| **2** | Cluster boundary approved/revalidated | **SATISFIED** — `CLUSTER-003` boundary re-approved **2026-09-14**, three cards, with `CHAR-006`/`CHAR-008`/`CHAR-009`/`EXP-010` explicitly out |
| **3** | All Rule Cards required by the cluster approved under the current hierarchy | **SATISFIED** — `CHAR-004`, `CHAR-005`, `EXP-003` all human-approved **2026-09-24** |
| **4** | Implementation readiness (re-)approved | **NOT GIVEN.** A human act. This gate record is an input to it, not a substitute for it |

```text
CLUSTER-003 HISTORICAL-RULES IMPLEMENTATION:  NOT AUTHORIZED
```

## 8. Readiness Statement

```text
CLUSTER-003 IS READY FOR THE IMPLEMENTATION-PLANNING PHASE.

It is NOT authorized for implementation. Authorization requires
ARCHITECTURE.md SS15.2 step 4 -- a separate, explicit human
implementation-readiness re-approval -- which has not been given.
```

The three cautions in §6 are **inputs to planning**, not preconditions of it: each is resolvable inside an implementation plan, by scoping or by an established in-repo pattern, without adjudicating any rules question.

## 9. Provenance

| Item | Value |
|---|---|
| Gate performed | 2026-09-24 |
| Authorized by | Human project owner, following approval of all three Rule Cards |
| Procedure | `ARCHITECTURE.md` §15.1 (five readiness criteria) + §15.2 (four migration-gate steps); §16 is project-wide and already `CLEARED` |
| Cards assessed | `CHAR-004`, `CHAR-005`, `EXP-003` — all `APPROVED` 2026-09-24 |
| Landed dependencies verified | `CHAR-001`, `CHAR-002`, `CHAR-003`, `CHAR-007`, `EXP-001`, `EXP-002` |
| Deterministic cases reviewed | 168 (60 + 76 + 32) |
| Outcome | **PASS**, no blocking defects, three non-blocking cautions |
| Implementation plan | **NOT DRAFTED** — not a required gate artifact (§1.2) |
| Production code | **NONE WRITTEN.** `src/`, `tests/`, `scripts/` byte-identical to `main` |
