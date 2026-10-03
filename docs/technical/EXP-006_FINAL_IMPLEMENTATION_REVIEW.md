# `EXP-006` — Final Implementation / Integration Review

## 0. Outcome

```text
EXP-006 FINAL IMPLEMENTATION REVIEW:  FAIL

Reviewed at:   026e19096b472a091c381fba99de684ef5885f97
Branch:        cluster-004-exp-006-stage-b
Worktree:      C:\Users\evanp\source\repos\OD_N_D-cluster-004-exp-006-stage-b
Reviewed:      2026-10-01
Reviewer:      independent -- did not write this implementation

Rules conformance (A, B, C-scope, E, F, G, H, L):   CLEAN
Canonical verification (M):                         PASS
Encoding (K):                                       CLEAN
Defects:   2 HIGH, 4 MED, 8 LOW
```

**The rules logic is correct.** Every positive mechanic, the eight-way ignition matrix, the
`SR-11` intersection, the error categories, the ownership boundary and the state-space invariants
were independently re-derived from the approved Rule Card and survived every falsification attempt
made against them, including 21 deliberate mutations of the production code, all 21 of which the
suite caught.

**The `FAIL` is not about the rules logic.** It is about artifacts of record that do not describe
the code that exists:

- `ARCHITECTURE.md` §15.2 — amended **on this branch** — affirmatively states that the `EXP-006`
  card **"carries no Simulator Ruling"**. It carries `SR-11`. A governance document changed by
  this very branch denies the existence of the ruling the branch implements (**HIGH-1**);
- the production module's own docstring states that Slice C (ignition) and Slice D (`CHAR-004`
  identity) **"are not authorized yet and are deliberately absent"** — printed directly above
  ~250 lines of Slice C and Slice D code (**HIGH-2**);
- the `CASE_DISCHARGE` ledger claims six of the Rule Card's `MUST NOT EXIST` / `MUST NOT OCCUR`
  cases are discharged by guards that **demonstrably do not fail** when the forbidden behaviour is
  added and exported (**MED-4**, proven by mutation).

Per the review instruction, **nothing was remediated**. The only file this review wrote is this
document. No production or test file was modified; no commit, merge or push was made.

---

## 1. What was read, and how

Read in full, as source rather than as prior summary:

| Artifact | Lines |
|---|---|
| `src/rules/exploration/light_and_exploration_resources.py` | 607 |
| `src/rules/exploration/errors.py` | 89 |
| `tests/rules/exploration/test_light_and_exploration_resources.py` | 1061 |
| `docs/rules/exploration/light_and_exploration_resources.md` (`APPROVED`, carries `SR-11`) | 733 |
| `docs/technical/EXP-006_IMPLEMENTATION_PLAN.md` (`APPROVED`) | 660 |
| `docs/technical/EXP-006_PRE_CODE_GATE.md` (`PASS` + §8a) | 372 |
| `docs/rules/clusters/CLUSTER-004-equipment-resources-and-evasion.md` §10 | — |
| `docs/rules/INVENTORY.md` `EXP-006` row; `ARCHITECTURE.md` §15.2 diff | — |
| `src/rules/character_creation/equipment.py` (the `CHAR-004` seam, as landed) | — |

**No Rules Cyclopedia research was performed.** This is an implementation review against an
already-approved contract. Where the card is silent, the review records the silence rather than
resolving it (`AGENTS.md` §3).

Active falsification performed (all scratch work in the session scratchpad; the repo was never
written to except for this file):

- `probe.py` — 40+ constructor/API attacks on the state space;
- `mutate.py` — 29 single-point mutations of a **scratch copy** of the production module;
- `mutate2.py` — 12 mutations that additionally **export** a forbidden operation in `__all__`;
- `mutate3.py` — 6 mutations aimed at the AST matchers' anchoring;
- `ledger_and_encoding.py`, `ledger2.py`, `cov.py` — ledger reconciliation, encoding, coverage.

---

## 2. Defects

### HIGH-1 — `ARCHITECTURE.md` §15.2 denies `SR-11`, on this branch

`ARCHITECTURE.md`, in the `CLUSTER-004` status block **added by this branch's diff**, states:

> Step 3 — required Rule Cards: **PARTIAL.** `EXP-006` `APPROVED` 2026-10-01 … **The card carries
> no Simulator Ruling, no `Alternate-Source Compatible Completion` and no `Human-Approved
> Variant`.**

The card carries `SR-11`. The same block also states:

> Step 4 — implementation readiness: **NOT (RE-)APPROVED.** No implementation plan exists for
> `EXP-006` or for `CLUSTER-004`, and none was drafted.

The implementation plan exists and is `APPROVED`; it is added by the same diff.

**Why this is HIGH rather than clerical.** `GAME_CONSTITUTION.md` §5 / `AGENTS.md` §12 make rules
provenance and Simulator Rulings protected authority. An affirmative denial that a card carries a
ruling is strictly worse than an omission: a future agent auditing `SR` allocation from
`ARCHITECTURE.md` would read a denial and could re-allocate `SR-11`, which is precisely the
failure mode the card's own §"ID allocation" paragraph guards against (it records that the only
prior textual occurrences of `SR-11` were `CHAR-005`'s **denials**, and treats denials as
distinguishable from allocations — a third denial now exists, written by this branch).

**Not a Task-C registration failure in the narrow sense.** The cluster record enumerates the four
places of record — cluster record, Rule Card §Simulator Ruling, `INVENTORY.md` `EXP-006` row, plan
§11 — and `SR-11` is correctly and consistently present in **all four** (verified textually;
see §5.C). The defect is the contradicting statement in a fifth governance document that the
branch chose to amend.

### HIGH-2 — the production module's docstring denies the existence of its own shipped code

`src/rules/exploration/light_and_exploration_resources.py`, lines 6–7:

> This file currently contains **Slice A only** — the light-source value/state model.

and lines 30–31:

> Slices A and B are implemented. Ignition (Slice C) and `CHAR-004` catalog lookup (Slice D) are
> not authorized yet and are deliberately absent.

Both statements are false at `026e190`. The same module defines `IgnitionConditions`,
`IgnitionOutcome`, `_IGNITION_MATRIX`, `ignition_outcome()` (Slice C) and `_CATALOG_NAMES`,
`_LIGHT_SOURCE_IDENTITIES`, `catalog_identity()`, `oil_flask_identity()`,
`tinderbox_identity()` (Slice D). The test module repeats the error at
`tests/rules/exploration/test_light_and_exploration_resources.py` lines 1–12:

> Ignition (L17-L26) and `CHAR-004` catalog integration are Slices C and D and are deliberately
> absent.

— directly above ~360 lines of Slice C and Slice D tests.

**Why HIGH.** Behavioural impact is nil. Audit impact is not: the two statements are
*authorization* claims ("not authorized yet"), made in production code, in a project whose §2
contract is that implementation tracks authorization exactly. A rules auditor reading this module
top-down is told the ignition matrix is not there. `AGENTS.md` §9.1 / `DEVELOPMENT_WORKFLOW.md`
§5.1 forbid representing an issue complete when "known incomplete behavior exists and is not
documented"; this is the mirror image — shipped behaviour documented as absent — and it is the
single most misleading text in the changeset.

### MED-3 — no completion record, and five artifacts of record say "NOT AUTHORIZED"

`docs/completion-records/` ends at `ISSUE-021-stage-a-evidence-linter.md`. There is **no**
`EXP-006` completion record. `AGENTS.md` §9 step 9 requires one "before representing it as
complete", and `DEVELOPMENT_WORKFLOW.md` §5 fixes its twelve mandatory sections.

Separately, every artifact of record on this branch states the implementation is not authorized:

| Artifact | Statement |
|---|---|
| Rule Card §Status | "`CLUSTER-004` historical-rules implementation is **NOT AUTHORIZED** and requires separate explicit human authorization under `ARCHITECTURE.md` §15.2 step 4" |
| `ARCHITECTURE.md` §15.2 | "**`CLUSTER-004` HISTORICAL-RULES IMPLEMENTATION: `NOT AUTHORIZED`.** Steps (2)–(4) are outstanding" |
| `INVENTORY.md` `EXP-006` row | "**Implementation NOT authorized**" |
| Plan §1.2 | "`SLICE C` NOT authorized -- BLOCKED, see §19" / "`SLICE D` NOT authorized" |
| Plan §18 | "IMPLEMENTATION NOT AUTHORIZED", and the plan itself "DRAFT -- awaiting human review" (contradicting §1's `APPROVED`) |

Plan §19 resolves Slice C's two blockers and says "`SLICE C READY`" — **readiness**, which the
Pre-Code Gate §0 is at pains to distinguish from authorization ("This `PASS` is a readiness
finding, not an authorization").

**Reviewer's position, stated carefully.** The task brief states the plan is `APPROVED` and the
slices accepted, and the `SR-11` adjudication plus the Slice C/D commits show the human plainly
directed this work in-session. The defect is therefore **not** that the work was unauthorized — it
is that the authorizing act is recorded nowhere, and that five artifacts affirmatively contradict
it. An independent reviewer cannot certify completion against a record that says the work was not
permitted. This is clerical to fix and is **not** mine to fix.

### MED-4 — `CASE_DISCHARGE` overclaims: six Rule-Card guard cases are not actually guarded

The ledger reconciles arithmetically (§5.I: 53/53, no duplicates, no gaps). **Its claims do not
all hold.** I mutated a scratch copy to add each forbidden behaviour the ledger says is guarded,
*including exporting it in `__all__`*, and re-ran the suite:

| Mutation (forbidden thing added **and exported**) | Card case | Ledger claim | Suite |
|---|---|---|---|
| `class VisibilityCategory(Enum): VERY_GOOD_LIGHT / DIM_LIGHT / NO_LIGHT` | `L30`, `L31` | "no `Visibility` category produced (API shape)" | **SURVIVED** |
| `def encounter_distance_from_light(...) -> int` | `L31`, `L36` | "no light->distance path (no distance operation exists)" | **SURVIVED** |
| `class CompleteDarkness(Enum)` | `L37a` | "complete darkness never established here" | **SURVIVED** |
| `def no_light_state(...) -> 'NO_LIGHT'` | `L29` | "no `NO_LIGHT`/world claim from absence" | **SURVIVED** |
| `def party_is_blinded(...) -> bool` | `L37` | "blindness predicate not asserted" | **SURVIVED** |
| `def ration_spoilage_turns(...)` | `L43` | "no ration name or operation" | **SURVIVED** |
| `LightSource.attack_penalty_when_dark -> -6` | `L39` | "no save/attack/AC values (import graph)" | **SURVIVED** |
| `def deplete(..., party_surprised, has_infravision)` | `L32`, `L35` | "surprise is not a parameter of **any** function" / "no infravision parameter exists" | **SURVIVED** |

**Root cause.** The only guard covering these is
`test_no_unauthorized_slice_behaviour_is_exposed`, which matches a forbidden-token set against
`name.split("_")` over `light.__all__`. Two independent holes:

1. **CamelCase is one token.** `"VisibilityCategory".split("_")` yields a single token
   `visibilitycategory`, which never equals the forbidden `visibility`. The guard's own comment
   explains that whole-token matching exists to avoid the `CLUSTER-003` substring false-positive
   (`FRESH_DURATION_TURNS` contains "ration") — a correct fix that introduces the complementary
   **false-negative** for class names, which is exactly how a `Visibility` or `CompleteDarkness`
   type would be named. The control proves the mechanism: snake_case `visibility_category` **was**
   caught; CamelCase `VisibilityCategory` was not.
2. **Near-miss tokens.** Forbidden holds `rations` but not `ration`; `blind`/`blindness` but not
   `blinded`; `darkness` but not `dark`; and neither `encounter`, `distance` nor `no_light` at all.

Six of twelve export mutations were caught (`visibility_category`, `rations_spoilage`,
`is_complete_darkness`, `torch_as_weapon_damage`, `oil_missile_damage`,
`starvation_onset_days`), so the guard is not inert — it is **narrower than the ledger says it
is**. Additionally, several discharges cite the wrong mechanism:

- `L13`, `L14`, `L38`, `L39` cite "import graph". The import graph cannot establish that no
  counter, clock or `-6` literal exists locally; what actually holds those properties is
  `test_the_value_object_carries_no_extra_state` (pins `LightSource.__slots__`),
  `test_the_derived_figures_cannot_disagree_with_the_sources` (pins the aggregate's one field) and
  `test_the_selector_stores_no_round_state` (no module-level mutable). `L39` has no guard at all.
- `L32`, `L35` claim "no parameter exists" / "surprise is not a parameter of **any** function".
  Only `mundane_light_contribution`'s signature is asserted
  (`test_querying_light_state_needs_no_surprise_or_encounter_state`). `deplete`,
  `refuel_lantern`, `ignition_outcome` and the three identity functions are unchecked. I verified
  by independent signature enumeration that no forbidden parameter is in fact present (§5.D) —
  the property is true, the guard just does not assert it.
- `L18` is discharged as "the branch stays selectable", asserted only by
  `test_a_first_attempt_evaluates_normally_and_records_nothing`, which loops over
  `(skill=True, tinderbox=True, ORDINARY)` — **not** `L18`'s own row
  `(skill=False, tinderbox=True, ORDINARY)`.
- `L16`'s guard is one-sided: it collects `ast.BinOp` `Mult` nodes with an **int constant on the
  right**. `return 6 * hours` (constant on the left) and `return minutes // 10` both **SURVIVED**.

**Current code is clean of all of the above.** This is a false-confidence defect in the audit
trail, not a rules defect — but the Pre-Code Gate's own Caution 2 specifically warned that
name-based guards misfire and directed AST/import-graph assertions. That direction was followed
for the strong guards and not for this one.

### MED-5 — `mundane_light_contribution` silently swallows malformed input; `deplete` rejects it

```python
# light_and_exploration_resources.py:601-607
return MundaneLightContribution(
    lit_sources=tuple(
        source for source in sources
        if isinstance(source, LightSource) and source.lit
    )
)
```

Observed behaviour:

```text
deplete(["torch"], 1)                        -> ValueError: sources must contain LightSource values
mundane_light_contribution(["torch"])        -> MundaneLightContribution(lit_sources=())
mundane_light_contribution([{"lit": True}])  -> MundaneLightContribution(lit_sources=())
mundane_light_contribution([DuckTypedLit()]) -> MundaneLightContribution(lit_sources=())
```

Two consequences:

1. **A type error degrades into `any_mundane_source_lit is False`** — the one output the card's
   Finding B surrounds with the most warnings. A caller that hands over the wrong collection is
   told "this card knows of no lit mundane source" instead of being refused. The card does not
   specify this case, so I do not resolve it; I record that the two sibling functions disagree on
   the same malformed input, and that `deplete`'s choice is the safer one.
2. **The result type's first barrier is unreachable through the public factory.** The class
   docstring advertises two independent barriers; barrier 1 ("`lit_sources` may contain only lit
   sources") is pre-empted by the comprehension's own `isinstance`. It is still reachable by direct
   construction, and `test_the_aggregate_refuses_a_non_tuple_and_non_source` exercises it there —
   so the barrier is tested, just not through the path callers use.

### MED-6 — transitive `rng` and `rules.currency` dependency, and a guard that overclaims

`test_the_complete_production_dependency_surface` docstring:

> Proves in one assertion that there is no production dependency on `TurnCredit`, `EXP-001` time
> machinery, the `CHAR-012` skill resolver, **RNG**, encounter resolution, combat resolution,
> magic resolution, or any world-darkness state — because nothing of the kind is imported at all.

It proves no **direct** import. Importing `EXP-006` in a clean interpreter loads:

```text
rng, rng.errors, rng.expressions, rng.results, rng.rng,
rules.currency,
rules.character_creation.character_class, rules.character_creation.equipment,
rules.character_creation.errors, rules.exploration.errors,
rules.exploration.light_and_exploration_resources
```

`rules.character_creation.equipment` (the `CHAR-004` seam `EXP-006` is *directed* to use) itself
does `from rng import RNG` and `from rules.currency import Coin, Denomination`. So the whole RNG
package and the currency primitive are in `sys.modules` as a consequence of `EXP-006`'s single
legitimate import.

**Behaviourally clean.** No RNG object is constructed, no RNG method is called, no `Coin` is read.
`AGENTS.md` §7's actual requirement — simulation randomness goes through the injectable RNG, and
no uncontrolled global randomness enters rules code — is satisfied; the module draws no random
value at all. Mutations M19/M20 confirm a *direct* `rng` or `turn_credit` import is caught
immediately.

**The defects are the claims.** The guard's docstring asserts a transitive property it does not
test, and `CASE_DISCHARGE["L33"]` reads "guard: no distance dice (**no RNG imported**)" — which is
true only of direct imports. Noted rather than rated higher because the transitive edge is forced
by the plan's own §1.1 adjudication ("Use `catalog_item(...)`"; "No landed `CHAR-004` production
code changes in this slice"), so the implementer had no compliant alternative. The accurate
statement is "no RNG is *consumed*", not "nothing of the kind is imported at all".

### LOW findings

| # | Finding |
|---|---|
| LOW-7 | `L16` guard one-sided — `6 * hours` and `minutes // 10` both survive (see MED-4). |
| LOW-8 | Dead ledger key `"L12a_": "placeholder-never-used"` exists only to be filtered by `not k.endswith("_")`. Harmless (the filter can only drop a key, which then surfaces as `approved - mapped`), but it is cruft in an audit artifact. |
| LOW-9 | Plan §11's adjudication reads "**`IgnitionNotDefinedError` only**" and §16 falsification #10 reads "one error base plus one subclass". The code ships **two** concrete types. `errors.py` records this as a deliberate departure citing the 2026-10-01 adjudication, but the plan was never updated, so plan and code disagree on the error surface. |
| LOW-10 | Plan §14 Slice D specifies a new file `tests/rules/exploration/test_light_guards.py`; the guards were placed in the single existing test module instead. Undocumented plan departure. |
| LOW-11 | Plan internal contradiction: §1/§1.1 `APPROVED` vs §18 "`EXP-006 IMPLEMENTATION PLAN` DRAFT -- awaiting human review". |
| LOW-12 | Pre-Code Gate §6 still tabulates **50** cases ("29 of 50"), and classes `L22` as "Routed dependency" where `CASE_DISCHARGE` classes it "behavior". The 50→51→53 correction is recorded in plan §12 but not in the gate. |
| LOW-13 | `test_one_source_expiring_does_not_darken_the_party` docstring says "Two lit **torches**" but the code uses a torch and a lantern. Card case `L15a` reads "Two lit torches, one reaches `0`" — constructible as `(TORCH, 2, lit)` + `(TORCH, 6, lit)` depleted by `2`, and never exercised. Behaviour is kind-independent so the property holds; the test misdescribes itself and does not use the card's literal input. |
| LOW-14 | `getattr(item, 'price')` evades `test_no_catalog_economic_field_is_ever_accessed` (mutation A5 survived) — an inherent limit of an `ast.Attribute` matcher. Direct reads are caught (A4, A6). Requires deliberate obfuscation; current code does none. |

### Adjudication question, not rated as a defect

**Error category for the refuel refusals.** `refuel_lantern` raises plain `ValueError` for a torch
("only a lantern burns a flask of oil") and for a partly-full lantern ("the approved card states
refuelling only for a lantern that has reached zero"). `errors.py` defines the `ValueError`
convention as *structural* — "a non-`int`, a `bool` masquerading as one, a negative count" — and
reserves domain types for "where the source defines no procedure for what was asked". A
well-formed `LightSource` that happens to be a torch, or to hold 7 turns, is none of the
structural cases; and "the card states no arithmetic for a partial refill" is **literally** a
card silence, i.e. the same semantic as `IgnitionNotDefinedError`, scoped by name to ignition.

So card-silence refusals in ignition get a domain type while a card-silence refusal in refuelling
gets the structural type. The Rule Card says only "**REFUSED**" (`L12a`) and specifies no category;
plan §1.1 forbids introducing a domain type unless a slice requires it. **Per `AGENTS.md` §3 I do
not resolve this** — it is flagged for human adjudication, not scored. The refusals themselves are
deterministic and correct.

---

## 3. What I tried that did NOT find a problem

Recorded so the `FAIL` is not mistaken for a broad indictment. Each of the following was a genuine
attempt to break the implementation and failed to.

**21 of 21 behavioural mutations were caught** (scratch copy; first failing test shown):

```text
CAUGHT  radius 30 -> 31 .................. test_a_lit_source_illuminates_thirty_feet
CAUGHT  torch 6 -> 5 turns ............... test_a_fresh_torch_has_six_turns
CAUGHT  lantern 24 -> 20 ................. test_a_fresh_lantern_has_twenty_four_turns
CAUGHT  per-kind radius (quality split) .. test_a_lit_source_illuminates_thirty_feet[LANTERN]
CAUGHT  drop exhausted-never-lit .......... test_an_exhausted_source_cannot_be_lit
CAUGHT  unlit sources deplete too ......... test_an_unlit_source_does_not_deplete
CAUGHT  depletion goes negative ........... test_remaining_turns_floor_at_zero...
CAUGHT  zero result stays lit ............. test_a_torch_is_expended_after_its_six_turns
CAUGHT  refuel ignites the lantern ........ test_an_expended_lantern_takes_a_fresh_flask
CAUGHT  refuel accepts partly-full ........ test_refuelling_a_lantern_that_has_not_reached_zero...
CAUGHT  SR-11 row -> 1d6 (ruling undone) .. test_every_matrix_combination_resolves_as_approved
CAUGHT  fill an RC silence with a default . test_every_matrix_combination_resolves_as_approved[key5]
CAUGHT  same-round guard moved AFTER matrix test_the_same_round_guard_precedes_branch_resolution
CAUGHT  same-round -> wrong error type .... test_a_second_attempt_this_round_raises...
CAUGHT  drop the bool validation .......... test_a_malformed_attempt_flag_remains_a_structural_error
CAUGHT  aggregate stops filtering unlit ... test_refuelling_alone_cannot_make_the_lantern...
CAUGHT  read CHAR-004 .price .............. test_no_catalog_economic_field_is_ever_accessed
CAUGHT  read CHAR-004 .encumbrance_cn ..... test_no_catalog_economic_field_is_ever_accessed
CAUGHT  Oil -> the "Oil, Burning" row ..... test_oil_and_tinderbox_bind_to_their_rows
CAUGHT  import turn_credit ................ test_the_complete_production_dependency_surface
CAUGHT  import rng directly ............... test_the_complete_production_dependency_surface
CAUGHT  add a MAGICAL LightSourceKind ..... test_only_the_two_mundane_kinds_exist
```

**The `_CATALOG_NAMES` matcher the brief flagged as historically vacuous is genuinely fixed.**
The brief noted that an earlier version anchored on zero nodes because the constant parses as
`AnnAssign`, not `Assign`. The current version matches **both** node types and carries an explicit
non-vacuity assertion (`assert assignments, "guard found no _CATALOG_NAMES definition to anchor
on"`). I attacked it three ways and it held every time:

```text
CAUGHT  rename _CATALOG_NAMES -> _NAMES (anchor deliberately destroyed)
CAUGHT  stray "Lantern" literal at a call site
CAUGHT  stray "Tinder box" literal inside a function
```

I searched the rest of the suite for the same zero-node class. Three other matchers assert an
empty result set (`L16` multipliers, economic fields, forbidden imports) and so pass by finding
nothing — but mutations M17/M19/M20/A4/A6 prove the economic-field and import matchers do bite, and
`test_the_complete_production_dependency_surface` asserts an **exact non-empty set**, which is the
strongest form present. Only `L16`'s matcher is substantively one-sided (LOW-7).

**Circular parametrization: looked for, not found.** `APPROVED_MATRIX` is a hand-written literal
transcription of the card's eight rows, not derived from `_IGNITION_MATRIX`; mutating the
production matrix therefore fails the test (M11, M12). Where a parameter list *is*
implementation-derived — `parametrize("kind", list(LightSourceKind))`, and `product(..., list(
IgnitionConditions))` — a companion test pins the enum's membership
(`test_only_the_two_mundane_kinds_exist`; `assert len(combos) == 8`), so a silently shrinking
parameter list is caught (M21). `FRESH_DURATION_TURNS` is checked against literal `6` and `24`.

**Tests that can pass without inspecting anything: none found.** Every test in the module makes at
least one assertion against a value or an exception. `test_the_derived_figures_cannot_disagree_
with_the_sources` uses an `or` whose left operand would short-circuit if the class stopped being a
dataclass, but the right operand is evaluated today and does pin the field set.

**Substring checks masquerading as proofs:** the suite deliberately uses whole-token matching, and
its comments explain why. The residual weakness is false negatives, reported as MED-4 — not
false positives.

---

## 4. Canonical verification (M)

```powershell
$env:PATH = "C:\Users\evanp\AppData\Roaming\Python\Python314\Scripts;$env:PATH"
uv run python scripts/verify.py
```

```text
1155 passed in 1.64s

Differentiated coverage gate
  src/rules/          20 file(s) -- 100% required, per file   MET
  src/survivability/  0 files -- trivially satisfied
  core (aggregate)    5 file(s) -- 100.00% (>= 95% required)
All differentiated coverage thresholds met.

Stage-A evidence-packet structural linter (DEC-0012): every linted packet carries its
required instruments (0 post-DEC-0012 packets; 12 grandfathered; reference packet PASS)

Tests:     PASS
Coverage:  PASS
Ruff:      PASS
mypy:      PASS      (no issues in 52 source files)
Evidence:  PASS
Overall:   PASS
```

Per-file figures for the changed production files, read out of `coverage.json` directly rather
than trusting the gate's summary:

| File | Statements | Stmt % | Missing | Branches | Partial | Missing branches |
|---|---|---|---|---|---|---|
| `src/rules/exploration/light_and_exploration_resources.py` | 125 | **100.0** | none | 46 | **0** | none |
| `src/rules/exploration/errors.py` | 3 | **100.0** | none | 0 | 0 | none |

Repository policy (100% per file across `src/rules/`, branch coverage enabled) is met with zero
partial branches. The `EXP-006` module contributes 92 tests.

---

## 5. Section-by-section findings

### A. Rule-Card conformance — CLEAN

Verified against the card's §2–§6 and re-derived by probe, not by reading the test names.

| Mechanic | Card | Verified |
|---|---|---|
| Torch radius 30 / lantern radius 30 | §2, L1, L2 | One constant `MUNDANE_LIGHT_RADIUS_FEET = 30` serves both; `illumination_radius_feet` does not branch on `kind` |
| No quality distinction | L4, L5 | Not representable: a per-kind radius mutation (M4) fails immediately |
| Fresh torch 6 turns / lantern 24 | §3, L6, L7 | `FRESH_DURATION_TURNS` read-only `MappingProxyType`; both item-assignment attacks blocked |
| Unlit sources retain duration | L11 | `LightSource(TORCH, 6, lit=False).remaining_turns == 6`; `lit` and `remaining_turns` independent |
| Exhausted cannot be lit | §4, Finding C | `ValueError` at construction **and** via `dataclasses.replace` |
| Exhausted contributes nothing | §4, L9 | `illumination_radius_feet is None`; excluded from the aggregate |
| `elapsed_turns` caller-supplied | §1, §4 | `deplete(sources, elapsed_turns)`; no clock held |
| `bool` rejected / negative rejected / zero valid | plan §1.1 | `True`, `False`, `"1"`, `1.5`, `None`, `-1` all `ValueError`; `0` valid and state-preserving (`spent == source`) |
| Lit deplete, unlit do not | L8, L11 | `6 turns - 1 = 5` lit; unlit torch after 3 turns still `6` |
| Floors at zero | L10 | `9` elapsed vs `6` → `0`, never negative (M7 proves the floor is load-bearing) |
| Zero result unlights | L9 | `lit = remaining > 0`; M8 (`>= 0`) caught |
| No world-darkness transition | L15, L15b | `deplete` returns `tuple[LightSource, ...]` and nothing else — structurally incapable of emitting a world fact |
| Refuel: only exhausted lanterns | §4, L12a | torch refused; 7-turn lantern refused lit **and** unlit; fresh lantern refused |
| Refuel restores 24, LEAVES UNLIT | §4, L12 | `remaining_turns=24, lit=False`, hardcoded; M9 caught |
| Refuelled lantern contributes nothing alone | §4 | `illumination_radius_feet is None`; `any_mundane_source_lit is False` |
| Contribution scoped to owned mundane sources | §6, L27, L28 | `lit_sources` / `any_mundane_source_lit` / `max_mundane_radius_feet`; `None` not `0` when nothing lit |
| No exhausted or unlit source may enter it | L15a, L28 | Two independent barriers (one pre-empted — MED-5) |
| Multi-source behaviour source-local | L15a | One source expiring leaves `any_mundane_source_lit is True` and the other's 30' intact |

The two derived figures are **computed properties, not stored fields**, so they cannot disagree
with `lit_sources`. Confirmed: `MundaneLightContribution.__dataclass_fields__ == {"lit_sources"}`.

One observation, not a defect: `EXP-006` exposes **no operation that transitions `lit` False→True**.
`ignition_outcome` returns an enum and never a `LightSource`, which plan §11 requires ("applying a
successful ignition to a source is **not authorized by this plan** in any slice"). A refuelled
lantern therefore cannot be lit through any `EXP-006` API — exactly what the card's §4 demands
("until separately ignited"), and a frontier item for whichever card gains the ignition-application
responsibility.

### B. Ignition — the 8-way matrix — CLEAN

Enumerated independently over `product([True, False], [True, False], IgnitionConditions)` rather
than from the test's own table:

```text
skill=True  tinderbox=True   ORDINARY -> AUTOMATIC                RC Explicit
skill=True  tinderbox=True   ADVERSE  -> ROUTED_SKILL_CHECK       RC Explicit
skill=True  tinderbox=False  ORDINARY -> ROLL_1D6_IGNITE_1_2      RC Explicit
skill=True  tinderbox=False  ADVERSE  -> ROUTED_SKILL_CHECK       SR-11      <-- exactly once
skill=False tinderbox=True   ORDINARY -> ROLL_1D6_IGNITE_1_2      RC Explicit
skill=False tinderbox=True   ADVERSE  -> IgnitionNotDefinedError  RC silence
skill=False tinderbox=False  ORDINARY -> IgnitionNotDefinedError  RC silence
skill=False tinderbox=False  ADVERSE  -> IgnitionNotDefinedError  RC silence
```

Byte-for-byte identical to the card's §5 table. All eight present; five resolve, three refuse.

- **Exhaustiveness and non-overlap are structural.** `_IGNITION_MATRIX` is a `MappingProxyType`
  keyed on the 3-tuple, so a duplicate key is impossible by construction and evaluation order
  cannot create precedence. `len(_IGNITION_MATRIX) == 5`; the three silences are absent, so there
  is no default branch to fall into (M12, which adds one, is caught).
- **No wildcard remains.** The plan §19.1 defect (`any` / `—` rows overlapping at
  `(True, False, ADVERSE)`) is fully discharged: every row is an explicit literal key.
- **`SR-11` is applied exactly once and changes no other row.** The sibling row proves the ruling
  bites rather than being vacuous: same skill, same absent tinderbox, `ORDINARY` still yields the
  `1d6`. Reverting the `SR-11` row (M11) fails the suite.
- **Same-round rejected FIRST.** The guard precedes the lookup. I confirmed the ordering
  behaviourally at all three RC-silent combinations with the flag set: every one raises
  `IgnitionAttemptLimitError`, never `IgnitionNotDefinedError`. Moving the guard after the matrix
  (M13) is caught.
- **Correct type per category.** `IgnitionAttemptLimitError` for same-round,
  `IgnitionNotDefinedError` for RC silence, and the two are independent (`Exception` siblings;
  neither subclasses the other). Swapping them (M14) is caught.
- **Malformed input stays structural `ValueError`** — and this is load-bearing, not cosmetic.
  Because `hash(True) == hash(1)`, an unvalidated dict lookup would resolve `(1, 1, ORDINARY)` to
  `AUTOMATIC`. The `isinstance(value, bool)` checks run **before** the lookup and block it; M15
  (removing them) is caught. A hash-colliding fake `conditions` object with `__eq__` returning
  `True` is also rejected by the `isinstance` check rather than reaching the matrix.

### C. `SR-11` — registration CLEAN in the four required places; contradicted in a fifth

| Place | Content | Verdict |
|---|---|---|
| Rule Card §Simulator Ruling | Full ruling text, ambiguity, ID allocation, "Scope — deliberately narrow" | Correct |
| Rule Card §5 matrix + §Provenance Classification | Fourth row marked `SR-11`; provenance distinguished from Explicit / Necessary Consequence / Variant / Completion | Correct |
| `CLUSTER-004` §10 | Full entry, owner `EXP-006`, and an explicit "Recorded on:" list of the four places | Correct |
| `INVENTORY.md` `EXP-006` row | "Carries **one Simulator Ruling — `SR-11`** … no Compatible Completion, no Human-Approved Variant" | Correct |
| Plan §11 / §19.1; Pre-Code Gate §8a | Matrix row and the resolution record | Correct |
| **`ARCHITECTURE.md` §15.2** | **"The card carries no Simulator Ruling…"** | **HIGH-1** |

**Used only for its intended intersection.** Verified in code: the `SR-11` comment and the ruling
apply to the single key `(True, False, ADVERSE)`. The other four resolving rows and all three
refusals are `RC Explicit`/`RC silence` and are unchanged. No other row's outcome depends on the
ruling.

### D. Ownership boundary — CLEAN directly; one transitive edge reported

The production import surface is pinned by an exact-set assertion:

```text
__future__, collections.abc, dataclasses, enum, types, typing,
rules.character_creation.equipment,   <- identity only
rules.exploration.errors
```

Nothing is imported for: dungeon-time advancement, `TurnCredit`, `EXP-001` time origin, global
illumination, complete darkness, encounter `Visibility`/distance, surprise, blindness, darkness
combat penalties, infravision, `CHAR-012` skill resolution, RNG, magical light/darkness, rations,
starvation, torch-as-weapon, oil-as-missile. `src/rules/exploration/__init__.py` adds no
re-export, and **no other file in the repository imports this module** (grep over `src`, `tests`,
`scripts`) — matching plan §5's "Nothing imports it in this slice".

Independent of names, I enumerated every public callable's signature and found no parameter whose
underscore-separated tokens intersect `{surprise, infravision, visibility, darkness, blind, rng,
random, price, encumbrance, cost, coin, turn_credit, clock, round_number}`:

```text
deplete(sources, elapsed_turns)
refuel_lantern(source)
mundane_light_contribution(sources)
ignition_outcome(*, has_fire_building, has_tinderbox, conditions, attempt_already_made_this_round)
catalog_identity(kind) / oil_flask_identity() / tinderbox_identity()
LightSource(kind, remaining_turns, lit) / MundaneLightContribution(lit_sources)
```

**Indirect dependencies, as instructed.** Two were found and are reported as MED-6: the
`CHAR-004` seam transitively loads the whole `rng` package and `rules.currency`. No RNG or
currency value is consumed; the defect is the guard docstring's claim that nothing of the kind is
imported at all.

### E. `CHAR-004` seam — CLEAN (identity only)

Production access inspected directly, not inferred:

- `catalog_identity()` returns `_LIGHT_SOURCE_IDENTITIES[kind]` — `TORCH` uses `CHAR-004`'s
  **exported** `equipment.TORCH` (identity asserted with `is`), the lantern uses
  `catalog_item("Lantern")`. `oil_flask_identity()` / `tinderbox_identity()` use `catalog_item`.
- **No economic field is read anywhere.** I re-ran the AST attribute sweep myself over the parsed
  module: no `ast.Attribute` node names `price`, `encumbrance_cn`, `capacity_cn`,
  `dimension_feet`, `size`, `traits`, `material`, `made_for_race`, or legality. Mutations A4
  (`.encumbrance_cn`), M17 (`.price`) and A6 (a price-derived int) are all caught. `getattr`-based
  evasion survives (LOW-14).
- **`"Oil, Burning"` is correctly not mistaken for the exploration Oil.** `oil_flask_identity()`
  returns the Adventuring-Gear row (`name == "Oil"`, `category == ItemCategory.GEAR`). I confirmed
  from the catalog that `"Oil, Burning"` is a genuinely distinct row with
  `category == ItemCategory.WEAPON`, so the two are not aliases, and that swapping the name
  (M18) fails the suite.
- **String coupling is confined to `_CATALOG_NAMES`**, enforced by a properly anchored AST guard
  (A1–A3 all caught). Spellings verified against the landed catalog: `"Lantern"`, `"Oil"`,
  `"Tinder box"` (two words).

Observation (not a defect): `catalog_identity()` hands the caller the whole `CHAR-004` `Item`, so
`.price` and `.encumbrance_cn` are reachable *through* the returned object. Card §C forbids
restating, re-deriving or varying those facts, which this does not do — it returns `CHAR-004`'s own
authoritative row unmodified, which is exactly what plan §1.1 directs. `L42` ("any price, `Coin`
or encumbrance value **emitted**") is therefore discharged in the "not produced here" sense rather
than the "not reachable downstream" sense. Worth stating; not a contract breach.

### F. `EXP-002` seam — CLEAN

- No `turn_credit` / `TurnCredit` import (M19 proves the guard bites), and no
  `dungeon_turn_time_accounting` import.
- No clock, counter, accumulator, round number or origin mechanism. `LightSource.__slots__` is
  pinned to `("kind", "remaining_turns", "lit")`; the aggregate has one field; there is no
  module-level `list`/`dict`/`set` (the three constants are `MappingProxyType`, which is **not** a
  `dict` subclass, so the guard's filter is correct rather than accidentally passing).
- `deplete` merely consumes a validated caller-supplied `int`. `_require_elapsed_turns` owns the
  **numeric domain** and explicitly disclaims provenance.
- **The orchestrator-provenance question remains UNRESOLVED, not silently solved.** No fake
  provenance wrapper was introduced; the docstring states that the module "imports no time
  machinery, holds no counter, and has no way to prove where an integer came from", and routes the
  question to the frontier. This matches plan §1.1, §8.2 and §17 item 2. The same boundary is
  applied consistently to `attempt_already_made_this_round`.

### G. State space — every forbidden state is unreachable; the unapproved cap is absent

```text
BLOCKED  lit=True with remaining_turns=0      direct ctor AND dataclasses.replace
BLOCKED  negative remaining_turns             ValueError
BLOCKED  boolean remaining_turns (True/False)  ValueError -- bool excluded explicitly
BLOCKED  float / str remaining_turns          ValueError
BLOCKED  non-bool lit flag                    ValueError
BLOCKED  unsupported light kind (str)         ValueError, in ctor, fresh() and catalog_identity()
BLOCKED  MundaneLightContribution w/ unlit     ValueError "only lit sources"
BLOCKED  MundaneLightContribution w/ exhausted unconstructible at the source (barrier 2)
BLOCKED  refuelled lantern auto-lighting      lit=False hardcoded; radius None; aggregate False
BLOCKED  FRESH_DURATION_TURNS mutation        mappingproxy, no __setitem__
BLOCKED  attribute assignment                 FrozenInstanceError; no __dict__ (slots)
```

`deplete` cannot *produce* a forbidden state either: `max(0, ...)` makes negatives unreachable and
`lit = remaining > 0` makes lit-at-zero unreachable, both confirmed by mutation (M7, M8).

**The unapproved `remaining_turns <= fresh_duration` cap is NOT imposed** — confirmed positively:
`LightSource(TORCH, 600, lit=True)` and `LightSource(LANTERN, 9999, lit=True)` both construct and
deplete normally. The card authorizes no such cap and the implementation invents none. Residual
note: adding the cap (M29) does **not** fail the suite, so its absence is correct today but
unguarded against a future implementer.

One theoretical bypass, recorded for completeness and **not** counted as a defect:
`object.__setattr__` can force `lit=True, remaining_turns=0` on an existing instance. That is true
of every frozen dataclass in Python and in this repository, is not an API path, and no reasonable
invariant can prevent it.

### H. Error semantics — CLEAN for ignition; one category question for refuelling

| Category | Meaning | Paths verified |
|---|---|---|
| `IgnitionNotDefinedError` | RC supplies no procedure | exactly the three RC silences, with branch-specific messages (the "comparatively dry" qualification when a tinderbox is held; "no procedure is stated" otherwise) |
| `IgnitionAttemptLimitError` | RC supplies a procedure and forbids another attempt this round | exactly the same-round flag, raised before the matrix, at all eight combinations |
| `ValueError` | malformed input | non-`bool` flags, non-enum `conditions`, non-`int`/`bool`/negative turns, non-`LightSource` members, bad kinds |

No path emits the wrong category for ignition. `raise ... from None` suppresses the `KeyError`
context, so the refusal does not leak the lookup mechanism. The refuel-refusal category question
is recorded above as an adjudication item, not scored as a defect.

`deplete(5, 1)` raises `TypeError: 'int' object is not iterable` (a non-iterable `sources`) rather
than `ValueError`. That is idiomatic Python and consistent with the type annotation; noted only.

### I. 53-case reconciliation — arithmetic CLEAN, map accuracy NOT

Reconciled independently, without trusting `CASE_DISCHARGE`:

```text
Rule Card table rows matching ^\| (L\d+[a-z]?) \| :  53
Distinct IDs                                      :  53
Duplicate IDs                                     :  none
L-IDs mentioned in prose but lacking a table row  :  none
CASE_DISCHARGE keys                               :  54  (53 counted + "L12a_" filtered)
approved - mapped                                 :  none
mapped - approved                                 :  none
```

Full ID set confirmed: `L1`–`L47` plus `L12a`, `L15a`, `L15b`, `L19a`, `L19b`, `L37a`.

Per-category counts:

| Category | Count | Cases |
|---|---|---|
| behavior | 19 | L1, L2, L3, L6, L7, L8, L9, L10, L11, L12, L15a, L17, L19a, L20, L21, L22, L27, L28, L34 |
| guard | 26 | L4, L5, L13, L14, L15, L15b, L16, L19b, L25, L29, L30, L31, L32, L33, L35, L36, L37a, L38, L39, L40, L41, L42, L43, L44, L45, L46 |
| invariant | 6 | L12a, L18, L19, L23, L24, L26 |
| routed | 2 | L37, L47 |
| **total** | **53** | |

**No case is missing and no ID is duplicated.** The 19 behaviour cases and 6 invariant cases are
each genuinely established by an executing assertion, which I verified by reading the named tests
rather than their titles — with the single exception of `L18`, whose claimed mechanism is asserted
only for a different matrix row (MED-4).

**Nine discharge claims do not establish what they claim** — `L29`, `L31`, `L32`, `L35`, `L36`,
`L37`, `L37a`, `L39`, `L43` — plus `L13`, `L14`, `L16`, `L18`, `L33` and `L38` citing the wrong or
an insufficient mechanism. Detail and mutation evidence in MED-4 and MED-6. The underlying
properties are all **true of the current code** (verified by import-graph pin, signature
enumeration, AST sweep and the absence of the relevant types); the ledger simply asserts a strength
of guarantee the tests do not provide.

### J. Test-quality audit

Covered in §3 (what held) and MED-4 (what did not). Summary:

| Failure mode hunted | Result |
|---|---|
| Tests that pass without inspecting anything | **None found** |
| AST matchers anchored on zero nodes | **The flagged `_CATALOG_NAMES` matcher is fixed and verified** (A1–A3). Three others assert an empty set by design; all but `L16`'s proved to bite under mutation |
| Substring checks masquerading as proofs | Whole-token matching used deliberately; the residual issue is **false negatives**, not false positives (MED-4) |
| Guards asserting implementation details instead of the architectural property | **Found** — the `__all__` token guard is a naming check standing in for "this responsibility does not exist" (MED-4) |
| Circular parametrization from the implementation | **None substantive** — `APPROVED_MATRIX` is a literal transcription; enum-derived lists are pinned by companion membership assertions |
| Mutation sensitivity | **21/21 behavioural mutations caught**; 8 guard-breadth probes and 6 export probes survived, all reported |

### K. Encoding — CLEAN

All nine changed files: valid UTF-8, **no BOM**, no mojibake (`Ã`, `â€`, `Â§`, `ï¿½`, U+FFFD all
absent), no stray foreign-script characters, consistent line endings within each file (the three
pre-existing markdown files were already CRLF; the six new files are LF-only — no file is mixed).

Non-ASCII characters present are legitimate typography: `§`, em/en dashes, curly quotes, `→`/`↓`/
`↔`, box-drawing characters in ASCII diagrams, `′` (prime, for feet), `×`, `≤`, `−`, `⅓`/`⅔`,
`½`/`¾`, `✓`/`✗`, `⚠`. Both production files and the test file are **pure ASCII**.

### L. Complete-darkness frontier — CLEAN, remains unresolved

| Artifact | Statement |
|---|---|
| Rule Card §8 | "the COMPLETE-DARKNESS world-state predicate itself → **OWNER NOT SETTLED.** No Rule ID in `INVENTORY.md` establishes global or environmental illumination state … **NO OWNER IS INVENTED HERE**" |
| Rule Card §B, Open Question 7 | "`OWNER NOT SETTLED`"; "**No owner is invented here**, and nothing in this card depends on one existing" |
| Plan §15 | "`Owner: UNRESOLVED` / `Rule ID: none currently settled` / `Status: NOT an EXP-006 implementation dependency`" |
| Pre-Code Gate §6 Caution 3 | routed-dependency tests, consumers untestable until the owner exists |

**No Rule ID has been allocated**, and `EXP-006` neither solves nor requires it. Confirmed in code:
the module can neither express nor return a world-illumination fact — `deplete` returns only
sources, the aggregate carries one field and two computed properties, and no name on
`MundaneLightContribution` contains any world-state vocabulary. `any_mundane_source_lit is False`
is reachable but is, structurally, a statement about this card's own sources only. The implementation
is consistent with the frontier remaining open — subject to MED-4: the guard that is *claimed* to
prevent a future `CompleteDarkness` type from appearing does not actually do so.

### M. Canonical verification — PASS

See §4. Tests, coverage (per-file 100% statement and branch, zero partial), Ruff, mypy, Evidence
and policy all pass.

---

## 6. Disposition

The rules implementation is, on the evidence above, **genuinely correct**: conformant to the
approved Rule Card mechanic by mechanic, exact on the eight-way ignition matrix and on `SR-11`'s
single intersection, clean on every ownership boundary I could probe directly or transitively, and
sealed against every forbidden state I could construct. The suite is strong where it matters
most — 21 of 21 behavioural mutations caught, and the specific vacuous-matcher bug the brief
flagged is genuinely fixed and verified.

It nonetheless **fails this review**, for defects that are entirely in the record rather than in
the logic:

| # | Severity | Defect |
|---|---|---|
| 1 | **HIGH** | `ARCHITECTURE.md` §15.2, amended on this branch, states the `EXP-006` card "carries no Simulator Ruling" (it carries `SR-11`) and that no implementation plan exists (it does) |
| 2 | **HIGH** | The production module docstring states Slices C and D "are not authorized yet and are deliberately absent", above ~250 lines of Slice C/D code; the test module repeats it |
| 3 | MED | No `EXP-006` completion record exists, and five artifacts of record state the implementation is `NOT AUTHORIZED` |
| 4 | MED | `CASE_DISCHARGE` overclaims: six Rule-Card `MUST NOT` cases survive mutation; six more cite an insufficient mechanism |
| 5 | MED | `mundane_light_contribution` silently swallows malformed input where `deplete` rejects it, degrading a type error into `any_mundane_source_lit is False` |
| 6 | MED | Transitive `rng` + `rules.currency` load via the `CHAR-004` seam, against a guard docstring claiming no RNG dependency at all |
| 7–14 | LOW | One-sided `L16` guard; ledger cruft; plan/code error-surface disagreement; test-file placement departure; plan `APPROVED`/`DRAFT` contradiction; stale 50-case gate table; `L15a` test docstring/code mismatch; `getattr` evasion of the economic-field guard |

None of these require changing the rules logic. Per the review instruction they are **not**
remediated here, to preserve reviewer independence; the two HIGH items and MED-3 are documentation
and record corrections, and MED-4/MED-5/MED-6 are test-strength and API-consistency items for the
implementer to address or for the human project owner to waive explicitly.

---

EXP-006 FINAL IMPLEMENTATION REVIEW: FAIL
