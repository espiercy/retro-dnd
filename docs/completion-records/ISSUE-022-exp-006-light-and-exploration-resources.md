# ISSUE-022: `EXP-006` Light & Exploration Resources — Implementation

```text
STATUS:  NOT COMPLETE
EXP-006-PHASE: REVIEW-5-REMEDIATED

         Implementation is code complete and all canonical gates pass, but
         DEVELOPMENT_WORKFLOW.md §5.1 forbids representing an issue as
         complete while required verification is outstanding, and human
         acceptance is a separate act that has not occurred.

         EVERY independent final implementation review performed so far
         returned FAIL, and NONE found a rules-conformance defect.  The
         review history is the persisted artifact set in §3, not a count
         stated here -- see the note below.

         LOW-3 and LOW-8 are RESOLVED (applied at a150837).

         This record is the authoritative current status for EXP-006.

BRANCH:  cluster-004-exp-006-stage-b   (unmerged, unpushed)
```

> **Why this record no longer states a review count.** Corrected 2026-10-03 under review-#4 finding
> `B-4`. Every prose count of the review history written into this record has gone stale within a
> day of being written — §11 still said "**Two** independent final implementation reviews" and the
> chronology still listed review #3 as "pending" while the `STATUS` block above said three, so the
> record contradicted itself. The review history is now established by **the artifact set that
> exists on disk** (enumerated in §3 and listed in the chronology below), and
> `test_the_review_artifact_set_is_internally_consistent` checks that every review artifact has a
> paired remediation ledger and that each appears in §3.
>
> *Unsupported conjunct dropped 2026-10-03 under review-#5 `BLOCKING-2`.* This sentence also claimed
> the test checks *"that no live record asserts a contradicting prose count"*. **It does not** — it
> globs the review and ledger files, compares their counts, and checks each filename appears in this
> record; it reads no other live record, and no mechanism anywhere checks prose counts. Review #5
> demonstrated the gap against a contradicting count then live in `ARCHITECTURE.md`, with the suite
> green. Per the standing project rule the **claim is narrowed to the mechanism**, rather than the
> mechanism broadened to preserve the claim.

> **This record is the single authoritative statement of current `EXP-006` status.** Other records
> carry the `EXP-006-PHASE` token and point here; a test
> (`tests/rules/exploration/test_exp_006_record_consistency.py`) asserts they agree, because three
> consecutive reviews found them disagreeing.

> **Rewritten 2026-10-03** under review-#2 finding `MED-5`, which found that the record created to
> discharge review #1's `MED-3` did not itself satisfy `DEVELOPMENT_WORKFLOW.md` §5: it omitted the
> rules-provenance and deviations categories entirely, reported tests as a file list, left out the
> documentation artifacts the same commit changed, did not follow the 1→12 order, and claimed a
> **`policy`** verification gate that does not exist (`LOW-1`). §5 is a protected document and its
> twelve categories are followed below in order, with an explicit statement wherever a category is
> genuinely empty.

## 1. Issue/Task Identifier and Objective

`ISSUE-022`. Implement approved Rule Card `EXP-006` — the mundane light and exploration-resource
mechanics — as a single-card vertical slice: the light-source value model, depletion against
authoritative elapsed turns, the mundane-light contribution, the ignition branch selector, and the
`CHAR-004` identity binding. Delivered as four separately authorized slices, A–D.

**Explicitly not in scope:** the mechanics that *consume* light state, `CLUSTER-004` cross-card
integration, and `ENC-005`.

## 2. Approved Inputs/Specifications

- **Rule Card `EXP-006`**, Status: `APPROVED` (human project owner, 2026-10-01), carrying
  `SR-11` — `docs/rules/exploration/light_and_exploration_resources.md`
- **Stage-A evidence**, `ACCEPTED` 2026-09-29 — `docs/rules/evidence/EXP-006-evidence-remediated.md`
  (passed independent `DEC-0010` completeness review at the fifth attempt; the four prior `FAIL`
  reviews stand unaltered)
- **Pre-Code Gate**: `PASS` 2026-10-01, with a bounded revalidation of the ignition portion the
  same day — `docs/technical/EXP-006_PRE_CODE_GATE.md`
- **Implementation plan**: `APPROVED` 2026-10-01 — `docs/technical/EXP-006_IMPLEMENTATION_PLAN.md`
- **Architectural inputs**: `ARCHITECTURE.md` §5 (single simulation-owned RNG stream), §10
  (survivability policies after canonical generation), §15.1, §15.2, §16
- **Decision records**: `DEC-0008` (Mystic and selected optional systems project-REQUIRED),
  `DEC-0009` (Evidence-First two-stage protocol), `DEC-0010` (primary-source completeness audit),
  `DEC-0012` (Stage-A evidence-integrity gates; worktree isolation)
- **Human adjudications during implementation**: `CHAR-004` identity access without modifying
  `CHAR-004`; `EXP-002` elapsed turns as an explicit input rather than an imported `TurnCredit`;
  no fresh-duration ceiling; refuelling does not ignite; the `SR-11` ignition-overlap ruling;
  `attempt_already_made_this_round` as a caller-supplied flag; error-category separation;
  `LanternRefuelNotDefinedError`; and (2026-10-03) making the identity binding private.

## 3. Files Created, Modified, or Deleted

> **Line counts and test counts are deliberately NOT stated here.** Corrected 2026-10-03 under
> review-#3 finding `MED-4`: this subsection carried "(102 lines)", "(529 lines)", "(1418 lines)"
> and "108 tests" while §6 of this same record said 111 — three stale figures and a
> self-contradiction, created precisely because mutable numbers were duplicated across sections.
> They are not re-stated with corrected values, because that would only reset the drift clock. The
> **single authoritative current figures live in §8 and §9**, which report the actual output of the
> canonical verification run, and the deterministic-case total is pinned by a test. Prefer reading
> the files or running `verify.py` over trusting any transcribed count.

**Created — production:**

- `src/rules/exploration/errors.py` — three concrete domain rejections, no base class

**Modified — production:**

- `src/rules/exploration/light_and_exploration_resources.py` — the `EXP-006` module

**Created — tests:**

- `tests/rules/exploration/test_light_and_exploration_resources.py` — the full deterministic-case
  suite, the behavioural and invariant tests, and the structural guard suite

**Modified — governance and documentation:**

- `ARCHITECTURE.md` — §15.2 `EXP-006` entries, `SR-11` registration, implementation status
- `docs/rules/INVENTORY.md` — the `EXP-006` row
- `docs/rules/clusters/CLUSTER-004-equipment-resources-and-evasion.md` — §3 status, §10 `SR-11`
  registry, §13 next step
- `docs/technical/EXP-006_IMPLEMENTATION_PLAN.md` — §1.2, §10.1, §10.2, §11, §12, §14, §16, §18
- `docs/technical/EXP-006_PRE_CODE_GATE.md` — §6
- `docs/rules/exploration/light_and_exploration_resources.md` — the approved card. Amended **only**
  under explicit human authorization, never by a remediation pass acting on its own: the two bounded
  corrections of 2026-10-01 (`5594907`, `e5d92ad`), and the `LOW-8` historical clarification of
  2026-10-03 (`a150837`). *The previous wording claimed the card was "not touched by either
  remediation pass", which became false at `a150837`; corrected under review-#4 `B-4`.*
- `docs/rules/character_creation/encumbrance_and_movement_rate.md` — `CHAR-005`, protected approved
  card, amended once under explicit human authorization for the `LOW-3` historical clarification
  (`a150837`); documentation only
- `docs/completion-records/INDEX.md` — this record's index row

**Created — review and remediation artifacts.** This list is the authoritative review history; it
is paired, and a test checks the pairing (`B-4`):

- `docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW.md` — independent review #1, `FAIL`
- `docs/technical/EXP-006_REVIEW_REMEDIATION_LEDGER.md` — remediation of review #1
- `docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW_2.md` — independent review #2, `FAIL`
- `docs/technical/EXP-006_REVIEW_2_REMEDIATION_LEDGER.md` — remediation of review #2
- `docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW_3.md` — independent review #3, `FAIL`
- `docs/technical/EXP-006_REVIEW_3_REMEDIATION_LEDGER.md` — remediation of review #3
- `docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW_4.md` — independent review #4, `FAIL`
- `docs/technical/EXP-006_REVIEW_4_REMEDIATION_LEDGER.md` — remediation of review #4
- `docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW_5.md` — independent review #5, `FAIL`
- `docs/technical/EXP-006_REVIEW_5_REMEDIATION_LEDGER.md` — remediation of review #5
- `docs/completion-records/ISSUE-022-exp-006-light-and-exploration-resources.md` — this record

*Reviews #3 and #4 and their ledgers were missing from this list until 2026-10-03 (`B-4`), which is
why `DEVELOPMENT_WORKFLOW.md` §5 item 3 was not satisfied. `test_the_review_artifact_set_is_internally_consistent`
now fails if a review artifact exists without a paired ledger, or if either is absent from this list.*

**Deleted:** none.

## 4. Behavior Actually Implemented

The system can now model a party's mundane light sources through dungeon exploration.

A light source is a torch or a lantern, each carrying its remaining duration in turns and whether
it is currently lit. A fresh torch has 6 turns, a fresh lantern 24 per flask of oil, and a lit
source of either kind illuminates 30 feet — one radius, with no brightness or quality distinction.
An unlit source illuminates nothing but keeps its remaining duration.

Given a number of elapsed turns supplied by `EXP-002`, the system spends that fuel: lit sources
lose that many turns, floor at zero, and a source reaching zero becomes unlit and contributes
nothing further. Unlit sources do not burn. An expended lantern can be given a further flask,
which restores it to 24 turns and **leaves it unlit** — fuel and ignition are independent. Asking
to refuel a lantern that has not reached zero is refused in the **rules domain**: it is a valid
lantern state, and the card states no partial-refill arithmetic. Asking to refuel a **torch** is
refused as an **invalid argument** — `refuel_lantern` is a lantern operation, and the refusal
asserts nothing about RC.

Asked what a collection of sources together contributes, the system reports the lit ones, whether
any mundane source is lit, and the greatest radius among them — `None`, never `0`, when nothing is
lit. It filters unlit sources itself rather than trusting the caller, refuses a malformed member
rather than silently dropping it, and requires no surprise or encounter state to answer.

For ignition, the system selects which RC branch applies from whether the character has the
`Fire-Building` skill, whether a tinderbox is to hand, and whether conditions are ordinary or
adverse. It returns the branch — automatic ignition, a `1d6` that ignites on 1–2, or a routed
`CHAR-012` skill check — and **never rolls**. For the three combinations RC leaves silent it
refuses rather than inventing a default. A second attempt in the same round is refused on RC's
own once-per-round rule, reported distinctly from a silence.

Each light-source kind, the oil flask and the tinderbox are bound to `CHAR-004`'s catalog rows, so
no item name, price or encumbrance is restated here. That binding is private: no public function
of this card returns a catalog row.

**What it deliberately does not do:** produce encounter distance or visibility, establish
blindness or complete darkness, state any global illumination fact, apply movement or combat
effects, resolve a skill check, roll any die, consume any RNG, advance dungeon time, or model
rations or starvation.

## 5. Rules Provenance

Governing card: **`EXP-006`**, `APPROVED` 2026-10-01.

| Classification (`GAME_CONSTITUTION.md` §5) | Extent in this implementation |
|---|---|
| **Rules Cyclopedia Explicit** | The substantial majority: §2 radii; §3 durations; §5's tinderbox `1d6` on 1–2; §5's once-per-round rule; §5's three RC-explicit `Fire-Building` branches and its three RC-silence refusals |
| **Necessary Mathematical/Mechanical Consequence** | Depletion as `max(0, remaining − elapsed)`; an exhausted source ceasing to contribute its own illumination; exhaustion of one source not implying party or world darkness |
| **Simulator Ruling** | **Exactly one — `SR-11`**: the adverse-condition `Fire-Building` branch governs regardless of a tinderbox, resolving an internal RC ambiguity at `skill + no tinderbox + ADVERSE`. Human project owner, 2026-10-01. Registered in **five** locations (§12 below) |
| **Alternate-Source Compatible Completion** | **None.** No alternate-source research was performed or authorized for this card |
| **Human-Approved Variant** | **None.** |

Seven RC silences are **named and guarded rather than filled**, by express approval.

## 6. Tests Added or Modified

All in `tests/rules/exploration/test_light_and_exploration_resources.py`; the current count is
whatever §8's verification run reports, and is not duplicated here (`MED-4`). What the important
ones protect:

| Test | Protects |
|---|---|
| `test_a_lit_source_illuminates_thirty_feet` (parametrized over both kinds) | Both kinds share one radius, so the radii cannot diverge (`L1`, `L2`, `L4`) |
| `test_an_exhausted_source_cannot_be_lit` | The exhausted-never-lit invariant, refused at construction — the forbidden state is unconstructible, not merely untested |
| `test_remaining_turns_floor_at_zero_and_never_go_negative` | Depletion cannot produce negative fuel (`L10`) |
| `test_an_unlit_source_does_not_deplete` | Fuel burns only while lit (`L11`) |
| `test_refuelling_alone_cannot_make_the_lantern_contribute_illumination` | The fuel/ignition separation — the 2026-10-01 adjudication, in both directions (`L12`) |
| `test_refuelling_a_partly_spent_lantern_is_refused_whether_lit_or_not` | A card silence is refused, not interpolated (`L12a`) |
| `test_a_torch_passed_to_refuel_lantern_is_an_invalid_argument` | A non-lantern is a structural rejection; the refusal asserts nothing about RC |
| `test_a_torch_refusal_is_not_reported_as_a_source_silence` | The two refusal categories are not conflated at the catch site |
| `test_a_partial_refill_refusal_is_not_reported_as_an_invalid_argument` | The converse: a valid lantern's silence keeps the rules-domain category |
| `test_the_domain_errors_are_not_subclasses_of_value_error` | The taxonomy is real, not nominal — three concrete siblings of `Exception`, so catching `ValueError` cannot absorb a source silence |
| `test_a_malformed_member_is_rejected_not_silently_dropped` | An invalid input cannot become a plausible-looking `any_mundane_source_lit is False` |
| `test_an_exhausted_source_can_never_reach_the_aggregate` | The two independent barriers that keep spent sources out of the aggregate |
| `test_every_matrix_combination_resolves_as_approved` | All eight ignition combinations against the card's own table |
| `test_all_eight_combinations_are_covered_and_none_overlaps` | Exactly five resolved rows and three absent keys — no silence filled, no overlap |
| `test_the_sr11_intersection_routes_to_the_skill_check` | `SR-11`'s single row, and that it is not widened |
| `test_a_refusal_is_never_answered_by_a_default` | An RC silence refuses rather than falling back to the `1d6` (`L26`) |
| `test_the_two_refusals_are_different_types` | A same-round violation never claims the rule is undefined |
| `test_the_same_round_guard_precedes_branch_resolution` | The documented ordering of the two refusal paths |
| `test_the_module_scope_surface_is_exactly_approved` | EXP-006 binds exactly the approved module-level names, including names created by conditional execution |
| `test_no_module_level_mutable_state_exists` | No unauthorized module-level accumulator — the no-second-clock claim |
| `test_public_class_members_are_exactly_approved` | The **effective** class surface via `dir()`, so an inherited member fails |
| `test_approved_classes_have_exactly_the_approved_bases` | No mixin or intermediate base; both value types stay slotted |
| `test_every_approved_public_callable_signature_is_pinned` | Every public signature, including `LightSource.fresh` and the properties |
| `test_no_public_callable_escapes_the_signature_guard` | That the signature guard is not vacuous — a new public method must be pinned |
| `test_no_public_callable_can_emit_a_catalog_row` | `L42` as the card words it: nothing public returns an `Item`, so no economic value is emitted |
| `test_this_module_imports_no_time_machinery` | `EXP-002` remains the sole time authority, over the import graph |
| `test_the_complete_production_dependency_surface` | The whole direct import graph, stated positively |
| `test_every_approved_case_is_accounted_for` | All 53 approved cases mapped, no duplicates, every row declaring its claim kind |
| `test_the_case_category_counts_are_recomputed_not_carried_over` | The published split is computed, not transcribed |

**Regression tests for the two review cycles** are the guards named above: each replaced a
mechanism an independent reviewer demonstrated could be walked past.

## 7. Exact Verification Commands Executed

- `uv run python scripts/verify.py`
- `.venv\Scripts\python.exe -m pytest tests/rules/exploration/test_light_and_exploration_resources.py -q`
- `.venv\Scripts\python.exe -m pytest -q`
- `.venv\Scripts\python.exe -m coverage run --branch -m pytest`
- `.venv\Scripts\python.exe -m coverage json -q`
- `.venv\Scripts\python.exe scripts/check_coverage.py`
- `.venv\Scripts\python.exe -m ruff check src tests scripts`
- `.venv\Scripts\python.exe -m mypy`
- `.venv\Scripts\python.exe scripts/lint_evidence.py`

## 8. Verification Results

`scripts/verify.py` defines **five** gates. All five pass:

```text
Tests:     PASS
Coverage:  PASS
Ruff:      PASS
mypy:      PASS
Evidence:  PASS
Overall:   PASS
```

There is **no `policy` gate**; an earlier version of this record claimed one, which review #2
recorded as `LOW-1`. No verification result is reported here for a mechanism that does not exist.

## 9. Coverage Results

**100% statement and 100% branch, per file**, on both production modules — the `src/rules/`
differentiated gate requires 100% branch per file.

```text
src/rules/exploration/errors.py                            100% stmts, 100% branch
src/rules/exploration/light_and_exploration_resources.py   100% stmts, 100% branch
```

## 10. Deviations

Eight, all deliberate and recorded; none is a departure from the **approved Rule Card**, whose
mechanics are implemented as specified. Items 6–8 were added 2026-10-03 under review-#3 `LOW-5`,
which found this category incomplete.

1. **Error surface: three concrete types, no base class** — against the plan's §10.1 sketch of
   `ExplorationError` plus one subclass. Human adjudication 2026-10-01 directed that concrete types
   be preferred and no speculative exploration-wide hierarchy be built. Plan §10.1, §10.2 and §11
   corrected 2026-10-03 to match the shipped taxonomy.
2. **Guards placed in the single existing test module**, not the new
   `tests/rules/exploration/test_light_guards.py` the plan's §14 Slice D specified. One module keeps
   the 53-case ledger and the guards that discharge it in one place. Recorded in plan §14.
3. **`_CATALOG_NAMES` is an `AnnAssign`**, not the plain `Assign` an early guard assumed — the
   mismatch made that guard match zero nodes and pass vacuously. Fixed, and every AST guard now
   asserts it anchored on the structure it claims to inspect.
4. **The `CHAR-004` identity binding is private** (`_catalog_identity`, `_oil_flask_identity`,
   `_tinderbox_identity`), where Slice D shipped it public. Human adjudication 2026-10-03 on
   review-#2 finding `MED-2`: no approved mechanic consumes these accessors and the plan's §9
   never required them to be public, while exporting them put `Item`-returning functions — and so
   `.price` and `Coin` by reference — in this card's public API, which made approved case `L42`
   ("any price, `Coin` or encumbrance value **emitted**") unprovable as worded.
5. **A non-lantern passed to `refuel_lantern` raises `ValueError`**, not
   `LanternRefuelNotDefinedError` as Slice B shipped it. **Human adjudication 2026-10-03**,
   resolving review-#2 finding `LOW-9` — see §12.1 below for the full adjudication record. The
   approved card is unaffected: it states no case for a non-lantern, and `L12a` is worded
   *"refuelling a lantern that has not reached zero"*.

6. **Guard-strategy departures from the approved plan §13.** Recorded 2026-10-03 under review-#3
   finding `LOW-5`. Plan `G-3` (a dice-literal AST check) ships as something strictly stronger — no
   scaling operator of any kind in the source. Plan `G-6` (construction-site reachability) is not
   shipped; §13 pre-authorized that fallback. Plan `G-5` ships as an `__all__` token check
   explicitly labelled **claim C** rather than the planned `__all__`-plus-namespace check, because
   the namespace half is covered by the dedicated surface guard.
7. **API-shape departures from the plan's sketches.** Also `LOW-5`. Plan §7's `__all__` sketch
   omitted `FRESH_DURATION_TURNS`, which ships (12 names sketched, 13 exported, minus the three
   later privatised accessors). Plan §7.1 modelled `any_mundane_source_lit` and
   `max_mundane_radius_feet` as dataclass **fields**; they ship as **computed properties**, so the
   derived figures cannot disagree with `lit_sources`. Plan §14 Slice C still names the dropped
   `ExplorationError`, though §10.1 and §11 carry correction notes.
8. **Claim-scope narrowing, not mechanism widening** (2026-10-03, review-#3 `HIGH-1`/`MED-3`). The
   module-surface guard's claim was narrowed to the **concrete bound namespace at import time**,
   and twelve `CASE_DISCHARGE` rows moved from `surface` to `reviewed`. By explicit human
   direction, no `__getattr__` denylist, dynamic-attribute detector or static analyzer was added,
   and no fourth-generation universal guard is authorized.

**No approved coverage exception was taken** (`TESTING_STRATEGY.md` §8): coverage is 100% per file
without one.

## 11. Known Limitations and Unresolved Issues

1. **The issue is not complete.** Every independent final implementation review performed so far
   returned `FAIL` (the artifact set in §3 is the authoritative history). Each was remediated. A
   further separately authorized independent review, and then human acceptance, are required.
   *Corrected 2026-10-03 under review-#4 `B-4`: this item said "**Two** … reviews have returned
   `FAIL`; a **third** … is required", contradicting this record's own `STATUS` block.*
2. **Seven RC silences are guarded, not filled** — by express approval. They are not defects.
3. **The global complete-darkness world-state predicate is unowned:**

   ```text
   Owner:   unresolved
   Rule ID: none settled
   Not an EXP-006 dependency; binds before ENC-001 / darkness-related COMBAT-*.
   ```

4. **Rations and starvation causation remain deliberately unassigned.** Stage A evidenced real RC
   ration mechanics; ownership was not assigned, and starvation causation still has no Rule ID.
5. **The guard suite's claims are narrow by design, and substantially reviewed rather than proved.**
   **Fourteen** of the 53 cases are now labelled claim C — a reviewed architectural ownership
   boundary, not machine proof — after the 2026-10-03 narrowing. The module-surface guard
   establishes the **concrete bound namespace at import time** and does *not* establish the absence
   of a dynamic attribute hook, arbitrary future reflection, or every Python mechanism capable of
   exposing a value. The reflective-catalog boundary is likewise only partly machine-held: besides
   the recorded `dataclasses.astuple` path, `__getstate__()` reaches every catalog field with no
   import change at all. No static analyzer was built and the project does not claim one. **An
   independent reviewer must still inspect these boundaries by reading the code.**
6. **The card's light cycle is not closed anywhere in the codebase.** No operation moves a source
   from `lit=False` to `lit=True`: `ignition_outcome` returns a branch and never a `LightSource`,
   and `refuel_lantern` leaves the lantern unlit. The approved plan §11 excludes *applying* a
   successful ignition "in any slice", so this module is complete against its plan while the card's
   §4 reference to "a separately authorized ignition operation (§5)" has no implementation yet.
   Recorded 2026-10-03 under review-#3 `LOW-4`; it needs a future authorization, not a fix here.
7. **Review-#3's two protected-card findings are `RESOLVED`** — adjudicated by the human project
   owner and applied at `a150837` as documentation-only historical clarifications. `LOW-3`:
   `CHAR-005`'s two "there is no `SR-11`" denials each now carry a note that they describe only the
   2026-09-25 amendment state and that `SR-11` was subsequently allocated to `EXP-006`. `LOW-8`: the
   `EXP-006` card's pre-approval sentence is quoted under an explicit "Historical pre-approval
   note — retained for chronology, NOT current status" heading. Neither changed a mechanic,
   provenance classification, case ID or approval status; both confirmed applied by review #4.
8. **One review-#4 informational finding is open and requires human adjudication** (`INFO-1`): the
   approved card's §Open Questions opens *"All **six** are mapped RC silences or governance items"*
   above a list of **seven** entries. Inspected 2026-10-03 and **STOPPED rather than corrected**,
   because the count is genuinely ambiguous rather than a demonstrable typo — see the review-#4
   remediation ledger §INFO-1 for the exact passage and the reason. Documentation-only; no mechanic,
   silence disposition, provenance or case ID is affected.
8. **Not merged and not pushed.** `CLUSTER-004` implementation, `ENC-005` Stage B and any new
   Stage-A card all remain unauthorized.

**`LOW-9` is no longer open.** Review #2's ledger recorded it as *"recorded, not actioned"*, which
was accurate when written and is preserved there as the historical statement. It was **adjudicated
by the human project owner on 2026-10-03** and is now implemented — see §12.1.

## 12. Architectural Consequences

Three, each already reflected in `ARCHITECTURE.md` §15.2:

1. **`SR-11` is allocated**, the project's eleventh Simulator Ruling, registered in five locations:
   the Rule Card §Simulator Ruling; `CLUSTER-004` record §10; `INVENTORY.md`'s `EXP-006` row;
   implementation plan §11; and `ARCHITECTURE.md` §15.2. (§15.2 initially **denied** its existence;
   corrected under review-#1 `HIGH-1`, and added to the §10 registry under review-#2 `LOW-10`.)
2. **A new exploration-domain error module** — `src/rules/exploration/errors.py` — establishes that
   domain rejections in this package are concrete types with no base, distinct from the structural
   `ValueError` convention `turn_credit.py` and `dungeon_movement.py` set.
3. **The `EXP-002` seam is an explicit elapsed-turn input**, not an imported `TurnCredit`. This card
   holds no clock and no counter, which keeps `EXP-002` the single dungeon-time authority.

### 12.1 Human adjudication of `LOW-9` — the refuel error taxonomy

**Adjudicated by the human project owner, 2026-10-03**, closing the one finding review #2's
remediation left deliberately unresolved. Recorded here rather than in the review-#2 ledger,
because that ledger's *"recorded, not actioned"* statement is historical evidence and is preserved
unaltered.

**The defect.** `refuel_lantern` raised `LanternRefuelNotDefinedError` for **two** requests that
are not the same semantic category:

```text
A.  refuel_lantern(torch)                      -- a non-lantern source
B.  refuel_lantern(partially_fuelled_lantern)   -- a valid lantern state
```

**The adjudication.** `refuel_lantern` is specifically a lantern operation, so **A** is an invalid
*argument* to that API — a structural/API-domain rejection, handled by the repository's established
`ValueError` convention. Reporting it as a source silence asserted something false: that RC had
failed to define how to refuel a torch. RC has no such gap; the operation does not apply to that
source kind, and there is nothing to report as silent.

**B** is different. A partly-fuelled lantern is a *legitimate lantern state*, and RC establishes
replacement of the flask after exhaustion while establishing no top-up to 24, no adding 24 and no
partial-flask arithmetic. That is a genuine rules-domain source silence and keeps
`LanternRefuelNotDefinedError`.

```text
refuel_lantern(non-lantern)                 -> ValueError
refuel_lantern(lantern, remaining > 0)      -> LanternRefuelNotDefinedError
refuel_lantern(lantern, remaining == 0)     -> 24 turns, lit = False   [unchanged]
```

**No new exception type and no error hierarchy were introduced.** The three domain types remain
concrete siblings of `Exception` — verified, not assumed, by
`test_the_domain_errors_are_not_subclasses_of_value_error`, which is also what makes the
`NOT ValueError` assertions coherent: a caller catching `ValueError` cannot absorb a source
silence.

**No approved rules behavior changed.** The correction concerns only the *category* used to report
an invalid caller request. The refuel mechanics, the card, `L12a`'s wording and the 53-case ledger
are untouched.

---

## Chronology — preserved, not rewritten

| Date | Event | Outcome |
|---|---|---|
| 2026-09-29 | Stage A accepted after **five** independent completeness reviews | 4 × `FAIL`, then `PASS` |
| 2026-10-01 | Rule Card bounded remediation (Findings A–C), then approval | `APPROVED` |
| 2026-10-01 | Pre-Code Gate, then bounded revalidation of the ignition portion | `PASS` |
| 2026-10-01 | Slices A–C, with three bounded corrections and `SR-11` | accepted |
| 2026-10-03 | Slice D | accepted |
| 2026-10-03 | **Independent final implementation review #1** | **`FAIL`** — 2 HIGH, 4 MED, 8 LOW |
| 2026-10-03 | Bounded remediation of all 14 findings | ledger #1 |
| 2026-10-03 | **Independent final implementation review #2** | **`FAIL`** — 2 HIGH, 5 MED, 11 LOW |
| 2026-10-03 | Bounded remediation of all 18 findings | ledger #2 |
| 2026-10-03 | Human adjudication of `LOW-9` — the refuel error taxonomy | implemented (§12.1) |
| 2026-10-03 | **Independent final implementation review #3** | **`FAIL`** — 1 HIGH, 4 MED, 8 LOW |
| 2026-10-03 | Bounded remediation of review #3; guard claims **narrowed**, not widened | ledger #3 |
| 2026-10-03 | Human adjudication of `LOW-3` / `LOW-8` — protected-card historical clarifications | applied at `a150837` |
| 2026-10-03 | **Independent final implementation review #4** | **`FAIL`** — 6 blocking, 7 non-blocking |
| 2026-10-03 | Bounded remediation of review #4 | ledger #4 |
| 2026-10-03 | **Independent final review #5** | **`FAIL`** — 3 blocking, 6 non-blocking |
| 2026-10-03 | Bounded remediation of review #5 — this pass | ledger #5 |
| — | Further independent review | not yet authorized |
| — | Human acceptance and merge | **pending** |

**No past `FAIL` or `PASS` is relabelled.** Every final-review artifact is preserved unaltered, as
are the four Stage-A `FAIL` reviews and the two superseded first-pass evidence packets.

**Every review found the rules logic conformant** — clause by clause against the approved card,
each re-deriving the contract independently and running its own behavioural and state-space
mutations. **No review has found a rules-conformance defect.** Every finding in every review
concerned the self-description layer: docstrings, ledgers, case tables, status records and the
breadth of guard claims. Review #4 additionally found, for the first time, **no guard claiming more
than its mechanism establishes** — the 2026-10-03 narrowing held under independent audit.

*Rows for reviews #3 and #4 and the `LOW-3`/`LOW-8` adjudication were added 2026-10-03 under
review-#4 `B-4`; the table previously ended with review #3 listed as "pending" and asserted "both
reviews" below it.*
