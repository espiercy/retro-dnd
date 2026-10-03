# `EXP-006` — Remediation Ledger for Independent Final Implementation Review #3

```text
REVIEW REMEDIATED    docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW_3.md
REVIEW VERDICT       FAIL  -- 1 HIGH, 4 MED, 8 LOW
REVIEWED HEAD        d66db5f6cccda857ede6a8031340586b4aafc3f2
ARTIFACT COMMIT      c197fa58e462a1bb689c03362a2412a6edb1d227
REMEDIATION DATE     2026-10-03
AUTHORIZED BY        human project owner; remediation only. Review #4 NOT
                     launched. LOW-3 and LOW-8 deliberately NOT actioned.
WORKTREE             OD_N_D-cluster-004-exp-006-stage-b
BRANCH               cluster-004-exp-006-stage-b   (unmerged, unpushed)
CERTIFICATION        NONE. The implementer may not certify its own work.
```

> **All three `FAIL` reviews and both prior ledgers are preserved unaltered.** Review #3 is not
> relabelled, edited or softened. This is a **separate** ledger.

---

## 1. The governing human conclusion, and what it rules out

Three independent final reviews have now found **no `EXP-006` rules-conformance defect**. Review #3
re-derived the contract from the card, executed all eight ignition rows, and ran thirty of its own
mutations; every behavioural control was caught. Accordingly this remediation **did not reopen**:

```text
Stage A                              NOT reopened
RC research                          NOT reopened -- none performed
The approved mechanical contract     UNCHANGED
SR-11                                UNCHANGED -- still one matrix row
Ignition semantics                   UNCHANGED
Depletion semantics                  UNCHANGED
Refuel mechanics                     UNCHANGED
Light-contribution behavior          UNCHANGED
Ownership boundaries                 UNCHANGED
The approved Rule Cards              NOT MODIFIED (protected; AGENTS.md §12)
```

Only factual-record and proof-claim defects were remediated.

---

## 2. HIGH-1 — the claim was narrowed; the guard was **not** widened

**The finding.** A module-level `__getattr__` (PEP 562) serves attributes that are never keys in
`vars()`, so `_module_scope_names()` — which filters dunders — cannot observe it. Review #3
demonstrated unapproved `VisibilityCategory` and `encounter_distance_from_light` reachable with the
suite green, which is exactly the `Visibility` category (`L30`, `L31`) and the light→distance path
(`L36`) the card forbids. Three separate statements asserted the broader claim.

**Human direction applied: NARROW THE CLAIM. DO NOT CHASE `__getattr__`.** No `__getattr__`
denylist, no generic dynamic-attribute detector, no static analyzer was added. Production code uses
no such mechanism — re-confirmed independently, see §4 — and a fourth-generation universal guard is
not authorized.

**What the mechanism now claims, exactly:**

```text
At normal module initialization, EXP-006's concrete bound namespace
matches the approved namespace/state surface.
```

**What it explicitly disclaims**, now stated in the guard section and in each affected test
docstring rather than left implicit — absence of dynamic module attribute hooks; absence of
arbitrary future reflection; absence of every Python mechanism capable of exposing a value.

| Location | Was | Now |
|---|---|---|
| Guard-section header | "bind **exactly** the approved set of module-level names" | "**at normal module initialization** … the approved **concrete** module-level namespace", with the three disclaimers enumerated and the `__getattr__` limit named |
| `_module_scope_names()` docstring | "a name created inside `if`, `try`… is visible here" | adds an explicit **scope limit**: dunders are excluded, so a module-level `__getattr__` is not observed, and callers may claim only the concrete bound namespace |
| `test_the_module_scope_surface_is_exactly_approved` | "Any new module-level name, **however spelled and however created**, fails here" | narrowed to any new **bound** name; quotes the withdrawn claim and names the review-#3 demonstration |
| `test_the_errors_module_scope_surface_is_exactly_approved` | "nothing else" | "nothing else **bound**", same scope limit |
| `test_no_module_level_mutable_state_exists` | asserted an exhaustive either/or dichotomy | dichotomy **withdrawn** (see `MED-3`) |

**Also narrowed, per the same direction:** the project now distinguishes, in the ledger's own
vocabulary, a *machine-enforced invariant*, a *machine-enforced observed surface*, and a *reviewed
architectural ownership boundary* — and no longer presents the third as the first.

---

## 3. The 53 cases, honestly reconciled after narrowing

Every `CASE_DISCHARGE` row affected by `HIGH-1` was re-inspected. A row stayed `surface:` only
where its mechanism is one a dynamic attribute hook **cannot fake** — a parsed import graph, a
pinned callable signature, a pinned effective class surface, or an AST property of the source
itself. Rows resting on "no such name is bound at module scope" moved to `reviewed:`.

```text
MOVED surface -> reviewed   (12)
    L13  L14  L15  L19b  L29  L30  L31  L36  L37a  L43  L44  L45
MOVED behavior -> reviewed  (1)
    L46   -- LOW-2; its cited mechanism addressed a different property
```

**The recomputed split. The previous 23/5/23/1/1 is NOT preserved for continuity:**

| Claim kind | Count | Meaning |
|---|---|---|
| `behavior` | **22** | machine-enforced behavior |
| `invariant` | **5** | machine-enforced refusal |
| `surface` | **11** | machine-enforced **observed** surface |
| `reviewed` | **14** | reviewed architectural ownership boundary, **not** machine proof |
| `routed` | **1** | not owned by this card |
| **total** | **53** | independently enumerated from the card's own tables |

The total is unchanged because the card's case set is unchanged. The split is **computed** by
`test_the_case_category_counts_are_recomputed_not_carried_over`, not transcribed.

**This is a narrowing of claims, not a weakening of the implementation.** Nothing shipped uses a
dynamic hook or holds mutable state. What changed is that fourteen boundaries are now labelled as
what they are: held by approved architecture and independent review rather than by an executable
proof.

---

## 4. MED-3 — which interpretation applies, and why

§7 of the authorization required determining whether `MED-3` identifies *actual shipped mutable
state* (in which case: stop and report a conflict) or an *overbroad claim* (in which case: narrow
it). **Determined independently before any edit**, by inspecting the live objects:

```text
module namespace        33 names: 4 int/mapping constants, 3 read-only mappingproxy,
                        1 frozen Item, 3 enums, 2 frozen slotted dataclasses,
                        5 functions, 12 imported. NO mutable binding.
LightSource             class dict: 3 slot descriptors, 1 property, 1 classmethod.
                        NO class-level state. __slots__ pinned.
MundaneLightContribution class dict: 1 slot descriptor, 2 properties.
                        NO class-level state. __slots__ pinned.
function objects        deplete / refuel_lantern / mundane_light_contribution /
                        ignition_outcome -- attribute dicts all EMPTY.
dynamic hooks           __getattr__, __getattribute__, __setattr__, setattr,
                        globals() -- NONE present in production source.
```

**Interpretation: claim-breadth only. No conflict to report.** The *boundary* holds in fact; the
*proof* did not reach the card's full statement of `L14` ("any second turn counter, clock or
elapsed-time field **owned here**"), because a private class attribute on an approved class is
outside the module-scope check, the public class-surface filter and the slots/MRO pin.

**Correction applied**, same principle as `HIGH-1`: the false either/or dichotomy is withdrawn and
quoted as withdrawn; `L13`, `L14` and `L19b` are reclassified `reviewed:`; the test's claim is
reduced to "every module-level name EXP-006 binds holds an immutable value", with the
no-owned-clock conclusion attributed to the reviewed architectural boundary plus
`ARCHITECTURE.md` §5. **No broader clock detector was invented.**

---

## 5. MED-1 — stale review status, fixed *and* made mechanically impossible

Three live records still said review #2 was pending. All corrected, and the drift closed:

| Record | Was | Now |
|---|---|---|
| `INVENTORY.md` `EXP-006` row | "a second independent review is pending" | all three reviews, all three `FAIL`, none a rules defect; `LOW-3`/`LOW-8` open; points at `ISSUE-022` as authoritative |
| `CLUSTER-004` §3 status block | "review #2 PENDING" | carries the phase token; slice acceptance only |
| `CLUSTER-004` §13 "Live next step" | "A SECOND INDEPENDENT FINAL IMPLEMENTATION REVIEW" | all three artifacts named; review #4 **not yet authorized**; the two open protected-card findings named |
| plan §18 and §1.2 | "pending independent review #2 PASS" | "CODE COMPLETE; NOT FINALLY ACCEPTED", all three reviews tabulated |
| `ISSUE-022` status block | "Two independent final reviews have returned FAIL" | three, with counts, and designated the authoritative current status |

Current status now reads, consistently, exactly as directed:

```text
Review #1: FAIL, historical
Review #2: FAIL, historical
Review #3: FAIL, historical
Review #3 remediation: current work
implementation: CODE COMPLETE, NOT FINALLY ACCEPTED
```

Historical chronology is preserved; no review artifact was rewritten.

---

## 6. MED-2 — the withdrawn refuel wording, and two sub-defects beside it

`EXP-006_PRE_CODE_GATE.md` §5.F stated, as a **standing** finding, "`L12` confirms it **contributes
again**" — wording the card expressly withdrew on 2026-10-01. Review #2 graded the identical
misquote `HIGH-2` in a test docstring; it survived here because §8a declares §1–§8 standing.

Corrected to the current contract, with the stale sentence quoted and marked withdrawn:

```text
refuel restores remaining_turns = 24
lit = False
no mundane-light contribution until separately ignited
```

**The Rule Card mechanic is unchanged** — only this record's statement of it. Two further
corrections in the same section, both named by review #3:

- §5.C glossed `ROLL_1d6_IGNITE_1_2` as "this card's own roll". **This card rolls nothing** and
  imports no RNG; it selects a branch and the caller rolls. Corrected in place with a note.
- §8a claimed "§1–§8 are preserved unaltered", which is **false** — §6 carries a 2026-10-03
  correction and now so do §5.C and §5.F. Reworded to the accurate claim: no §1–§8 *finding* was
  reversed or re-performed; several *statements* of those findings were corrected.

---

## 7. MED-4 — counts single-sourced instead of re-transcribed

`ISSUE-022` §3 said "102 lines", "529 lines", "1418 lines" and "**108 tests**" while §6 of the same
record said **111**. Per the authorization, the fix is **not** to write corrected numbers into both
places and reset the drift clock:

- §3 **no longer states line or test counts at all**, and says why, naming `MED-4`.
- §6 no longer duplicates a test count; it points at §8.
- §8 and §9 remain the single authoritative figures, because they report the **actual output** of
  the canonical verification run.
- The deterministic-case total is pinned by a test rather than transcribed.

The reviewer's own cited actuals (160 / 648 / 1800) did **not** match this repository; measured
values at the time were 128 / 537 / 1462. **Its figures were not used as authoritative** — the
finding was verified independently, which is what established that §3 contradicted §6.

---

## 8. The bounded document-consistency mechanism

New: `tests/rules/exploration/test_exp_006_record_consistency.py` — **five tests**, deliberately
narrow.

**What it checks:**

- **A — the current review phase.** One token, `EXP-006-PHASE: REVIEW-3-REMEDIATED`, spelled
  identically in four named live records. Advancing the phase means changing the constant and every
  named record **together**, or the test fails.
- **A′ — the specific stale phrasings** three reviews have actually found ("review #2 pending",
  "awaiting review #2", "A SECOND INDEPENDENT FINAL IMPLEMENTATION REVIEW", …) must not appear in a
  live record unless the line is explicitly marked historical.
- **B — the deterministic case total.** Re-enumerated from the card, and the totals the project has
  actually drifted through (47, 50, 51) may not appear unmarked in a live record line that is about
  case counts. The test ledger's length must equal the card's total.

**What it deliberately does not do**, per the stated constraints: no scanning of arbitrary prose; no
generic documentation linter; no parsing of historical review artifacts (they preserve obsolete
claims **on purpose**); no rejection of deliberately historical numbers — a figure on a line marked
*historical*, *superseded*, *withdrawn*, *previously* or *corrected* is evidence, not drift; and
**no pinning of the global suite test count**, because that changes whenever any unrelated project
test is added and would manufacture the brittleness this file exists to remove. Duplicated global
counts were **removed** from the records instead.

**It earned its place immediately:** on first run it failed, because `ISSUE-022` did not yet carry
the phase token — the exact omission class that produced `MED-1` three times.

---

## 9. All remediated LOW findings

| # | Actual defect | Correction | Verification |
|---|---|---|---|
| **LOW-1** | The adjudicated **absence** of `remaining_turns <= fresh_duration` had no regression test; re-adding the cap left the suite green. | New `test_no_fresh_duration_ceiling_is_imposed`: a 600-turn torch constructs, illuminates and depletes to 594; a 100-turn lantern constructs; the aggregate still reports 30′. | Test passes; re-adding the cap now fails it. |
| **LOW-2** | `CASE_DISCHARGE["L46"]` cited the oil-row binding for a case about *no missile/pursuit-delay operation existing* — a different property. | Reclassified `reviewed:` with the accurate mechanism ("no missile/pursuit-delay name is bound; RC states no delay mechanic"), alongside its sibling `L45`. | Recomputed split asserted by test. |
| **LOW-4** | The module docstring's "the card's responsibilities are implemented in full" is broader than true at **card** level: nothing anywhere moves a source `lit=False → lit=True`. | Narrowed to "every responsibility the **approved implementation plan** assigns to this module", with the missing transition named explicitly and attributed to plan §11's exclusion. Recorded as `ISSUE-022` §11 item 6. | Docstring and record agree; plan §11 cited. |
| **LOW-5** | `ISSUE-022` §10 omitted the guard-strategy (`G-3`, `G-5`, `G-6`) and API-shape (plan §7/§7.1) departures. | Deviations 6, 7 and 8 added, naming each departure and whether it was pre-authorized, stronger, or a shape change. §10 header corrected five → eight. | §10 now matches plan §13/§7 on inspection. |
| **LOW-6** | Ledger #2's `N-R3` note attributed the residual reflective risk to a *future import*, understating it: `__getstate__()` reaches every catalog field with **no import change at all**. | The reflective-access guard docstring now records this explicitly and states the honest position — the boundary rests on review, not on that mechanism. `L42` is still not breached. | Guard docstring; `ISSUE-022` §11 item 5. |
| **LOW-7** | `CLUSTER-004` §6 Q10 restated *"normal dungeon conditions = Dim light"* — the inference the card's **Finding A withdrew** — in a section headed "Open questions requiring human decision". | Q10's withdrawn clause struck through and marked **SUPERSEDED**, with a note explaining why an uncorrected 2026-09-29 statement reads as live in a record whose §3/§10/§13 have since been updated. Surrounding Stage-A findings untouched. | Note in place; card Finding A cited. |

`LOW-3` and `LOW-8` are **not** actioned — see §10.

---

## 10. `LOW-3` and `LOW-8` — **HUMAN ADJUDICATION REQUIRED**

Both touch **protected approved Rule Cards** (`AGENTS.md` §12). This task was not authorized to
edit them, and the exact substance had not previously been put to the human reviewer. **No edit was
made.**

### `LOW-3` — **HUMAN ADJUDICATION REQUIRED**

```text
FILE      docs/rules/character_creation/encumbrance_and_movement_rate.md
CARD      CHAR-005 -- Encumbrance & Movement Rate, Status: APPROVED 2026-09-24
SECTIONS  the 2026-09-25 amendment note (line 17); Amendment History (line 626)
```

**Current wording, both occurrences:**

> line 17 — "**No Simulator Ruling was made, granted or renumbered; `SR-8`, `SR-9` and `SR-10`
> stand exactly as ratified, and there is no `SR-11`.**"
>
> line 626 — "**No Simulator Ruling was made, granted, or renumbered.** `SR-8`, `SR-9` and `SR-10`
> stand exactly as ratified on 2026-09-24, and **there is no `SR-11`**."

**Why the reviewer considers it defective.** `SR-11` now exists — allocated 2026-10-01 to `EXP-006`.
Both sentences are scoped to *what the 2026-09-25 amendment did*, so a strict reading survives; the
reviewer's concern is consequential rather than literal. These are **the exact two occurrences the
`EXP-006` card cites as its own ID-allocation evidence**, and `ARCHITECTURE.md` §15.2 expressly
warns that "the card's own ID-allocation reasoning treats prior textual denials as the evidence
distinguishing an allocated `SR` from a free one". A future agent allocating `SR-12` would read
these two lines and could reasonably conclude `SR-11` is free.

**Proposed minimal correction.** Append to each, without touching the amendment's own claim:
*"(`SR-11` was subsequently allocated to `EXP-006` on 2026-10-01; this statement concerns only what
the 2026-09-25 `CHAR-005` amendment did.)"*

**Effect of the correction:** **documentation only.** It changes no mechanic, no provenance
classification, no card status, no movement value, band, threshold or deterministic case. `SR-8`,
`SR-9` and `SR-10` are untouched.

### `LOW-8` — **HUMAN ADJUDICATION REQUIRED**

```text
FILE      docs/rules/exploration/light_and_exploration_resources.md
CARD      EXP-006 -- Light & Exploration Resources, Status: APPROVED 2026-10-01
SECTION   §Status, lines 90-91
```

**Current wording:**

> "**Approval of this card would not authorize implementation.** No Pre-Code Gate has been begun
> for `CLUSTER-004`, and no implementation plan exists."

**Why the reviewer considers it defective.** It sits roughly fifty lines after the same §Status
block points at `docs/technical/EXP-006_PRE_CODE_GATE.md`, so the card appears to contradict
itself. Both clauses remain literally true **as scoped to `CLUSTER-004`** — no cluster-wide gate or
plan exists — and the sentence is in the conditional pre-approval voice ("would not authorize"),
which is why the reviewer rated it `LOW`. But it is not labelled historical. (Ledger #1 examined the
neighbouring line-36 statement and found it accurate; it did not reach lines 90–91.)

**Proposed minimal correction.** Mark it as the pre-approval statement it is, e.g. *"Written before
approval; retained as the pre-approval position. An `EXP-006`-specific Pre-Code Gate and
implementation plan now exist (both `PASS`/`APPROVED` 2026-10-01); no `CLUSTER-004`-wide gate or
plan does."*

**Effect of the correction:** **documentation only.** No mechanic, provenance classification or card
status changes. The approved §1–§8 specification and §A–§E boundaries are untouched.

---

## 11. The guard arms race stops here

Recorded as a standing position, per the authorization:

```text
A future reviewer discovering another Python construct that lies outside a
guard's explicitly narrow stated claim is NOT by itself a defect.

A guard whose stated claim is BROADER than its actual proof IS a defect.

No fourth-generation universal architecture guard is authorized.
```

The repository now distinguishes machine-enforced invariant, machine-enforced observed surface, and
reviewed architectural ownership boundary — and the 53-case ledger labels every case with which one
discharges it.

---

## 12. Verification

```text
uv run python scripts/verify.py

Tests:     PASS
Coverage:  PASS      100% statement AND branch, per file, both production modules
Ruff:      PASS
mypy:      PASS      strict
Evidence:  PASS      DEC-0012 structural linter
Overall:   PASS
```

Five gates, which is all `verify.py` defines. Figures are reported in `ISSUE-022` §8/§9 rather than
duplicated here.

**Preservation confirmed:** reviews #1, #2 and #3 and ledgers #1 and #2 are byte-identical; no
approved Rule Card was modified; no new research was performed.

---

## 13. What this ledger does **not** do

```text
IT DOES NOT CERTIFY COMPLETION.           The implementer may not.
IT DOES NOT RELABEL ANY REVIEW OR LEDGER. All preserved unaltered.
IT DID NOT LAUNCH REVIEW #4.              Out of scope.
IT DID NOT EDIT A PROTECTED RULE CARD.    LOW-3 and LOW-8 await adjudication.
IT DOES NOT AUTHORIZE A MERGE OR PUSH.
IT DOES NOT AUTHORIZE CLUSTER-004 IMPLEMENTATION, ENC-005 STAGE B,
   OR ANY NEW STAGE-A CARD.
```
