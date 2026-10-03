# `EXP-006` INDEPENDENT FINAL IMPLEMENTATION REVIEW #2

> **Preserved verbatim as received.** This is the second independent final implementation review,
> performed against the remediated `HEAD` `574f1a4` by a reviewer that did not write the
> implementation and was forbidden to change anything. It is historical evidence under the same
> terms as `EXP-006_FINAL_IMPLEMENTATION_REVIEW.md` (review #1): **not** to be rewritten,
> relabelled or softened. The reviewer's verdict stands as the second final-review result.
>
> Recorded in the repository 2026-10-03 because the review was returned as a task result rather
> than written into the tree. Content is unaltered; only the HTML entity escaping of `>` and `<`
> introduced by the transport has been undone.

## 0. Worktree establishment (reported before any other work)

```text
WORKTREE      C:\Users\evanp\source\repos\OD_N_D-cluster-004-exp-006-stage-b
BRANCH        cluster-004-exp-006-stage-b                    [as required]
HEAD          574f1a453464605af2407aafa3a16904cb2f0e16       [as required]
MAIN          c1bdd5c01e998f961b3851c3d95a225b37fa9cc7
ORIGIN/MAIN   c3a3e2d9d961a1df8ec3ccad3823929b0a41cac0
STATUS        clean (verified again at end of review; unchanged)
```

No worktree collision. No file in the repository was created, modified or deleted by this review;
all mutation work ran in `C:\Users\evanp\AppData\Local\Temp\claude\exp006-review2-scratch`. No RC
research was performed and Stage A was not reopened.

---

## 1. Rule-Card conformance — clean

I walked every mechanical clause of the approved card against the code.

| Card clause | Code | Verdict |
|---|---|---|
| §2 torch 30′, lantern 30′, **one** radius, no quality distinction | `MUNDANE_LIGHT_RADIUS_FEET: Final = 30`, single constant, `illumination_radius_feet` does not branch on `kind` | conforms; one constant serves both kinds as the card requires |
| §3 torch 6 turns, lantern 24 per flask, no hour→turn conversion | `TORCH_TURNS = 6`, `LANTERN_TURNS_PER_FLASK = 24`, `FRESH_DURATION_TURNS` mappingproxy | conforms |
| §4 `max(0, remaining − n)` for **lit** sources only | `deplete` skips unlit, floors at 0, sets `lit = remaining > 0` | conforms (L8–L11) |
| §4 `EXPENDED` ⇒ that source contributes nothing, **source-local** | `deplete` returns only `tuple[LightSource, ...]` | conforms; scoping is structural |
| §4 refuel ⇒ 24 turns **and `lit = False`** (the corrected `L12`) | `refuel_lantern` returns `lit=False` | **conforms** — refuelling does not ignite |
| §4 partial refuel unassigned ⇒ refused | `LanternRefuelNotDefinedError`, no arithmetic | conforms (L12a) |
| §5 eight-way matrix, 5 resolved / 3 refused by absent key | `_IGNITION_MATRIX` has exactly 5 keys; `KeyError → IgnitionNotDefinedError ... from None` | conforms |
| §5 `SR-11` at `(skill, no tinderbox, ADVERSE)` only | one row, correctly commented; no other row altered | conforms, **not widened** |
| §5.1 once-per-round from caller-supplied flag, never mutated, no round counter | keyword-only `bool`, guard precedes the matrix, no cross-call state in shipped code | conforms |
| §6 exactly `lit_sources` / `any_mundane_source_lit` / `max_mundane_radius_feet`; `None` not `0` | identical names; both derived figures are properties, not fields | conforms |
| §7, §8 no `Visibility`, no distance, no blindness predicate, surprise not an input | nothing of the kind in the runtime surface (independently enumerated) | conforms |

**No silent rules decision found.** The one point the card leaves open — whether a same-round
violation or an RC-silence refusal reports first — is resolved in code *with* a stated rationale, a
dedicated test (`test_the_same_round_guard_precedes_branch_resolution`) and a note in `errors.py`.
Both paths refuse and neither produces a game outcome, so this is API presentation, not a rules
decision, and it is documented rather than silent.

I ran seven rules-logic control mutations of my own (radius→40, SR-11 row flipped to the `1d6`, an
RC silence filled with a default, refuelling ignites, per-kind radius split, exhausted-never-lit
invariant removed, unlit sources deplete, same-round guard moved after the matrix). **All eight
were caught.** The rules logic is correct and is genuinely pinned.

## 2. `SR-11` review — clean

Matrix implements the card's eight-way table exactly. The three RC silences
`(False,True,ADVERSE)`, `(False,False,ORDINARY)`, `(False,False,ADVERSE)` are absent keys, not
filled values; `len(_IGNITION_MATRIX) == 5` is asserted. `SR-11` is confined to its single row.
Registration is consistent in the Rule Card §Simulator Ruling, cluster record §10, `INVENTORY.md`'s
`EXP-006` row and plan §11 — the ruling text is substantively identical in card and cluster. One
gap, see LOW-10.

## 3. Ownership review — clean

I enumerated the module's **runtime** public surface rather than trusting the suite:

```text
owned public names (16) == APPROVED_DEFINITIONS exactly
LightSource members (dir)            : fresh, illumination_radius_feet, kind, lit, remaining_turns
MundaneLightContribution members (dir): any_mundane_source_lit, lit_sources, max_mundane_radius_feet
LightSource.fresh signature          : (kind, *, lit=False)
```

No encounter distance, no `Visibility`, no blindness establishment, no global illumination or
complete-darkness predicate, no attack/defence effect, no skill resolution, no magical light, no
movement multiplier, no infravision input, no ration or starvation surface. Surprise appears in no
signature. **Clean as shipped** — but see HIGH-1 for how little of this the guards actually hold in
place.

## 4. `CHAR-004` seam — clean, with one maintenance weakness

`catalog_identity`/`oil_flask_identity`/`tinderbox_identity` consume `CHAR-004`'s own `Item`
objects; `_CATALOG_NAMES` holds three strings and no economic value; no catalog row, price or
encumbrance is duplicated. `git diff main...HEAD` touches **no** file under
`src/rules/character_creation/`, `src/rules/currency.py` or `src/rng/`. I verified `Item` has
exactly ten fields and that `CATALOG_ECONOMIC_FIELDS` covers all eight non-identity ones —
complete today. See LOW-2 and MED-2.

## 5. `EXP-002` seam — clean as shipped

No `turn_credit` import, no `dungeon_turn_time_accounting`, no hour/minute conversion, no clock.
`elapsed_turns` is a parameter, validated for numeric domain only, with the provenance limitation
honestly documented in `_require_elapsed_turns`. The exact import surface is pinned to eight
modules. See MED-1 for the guard gap.

## 6. State-space review — clean, and the strongest part of the work

The exhausted-never-lit combination is rejected at construction, so the forbidden state is
**unconstructible**, not merely untested. The aggregate cannot contain an exhausted source by two
independent barriers. Refuelling leaves the lantern `UNLIT`, matching the corrected `L12`. All four
of my state-space mutations were caught.

## 7. Error-semantics review — coherent

Three concrete types, no base class. The structural/domain boundary is applied consistently:
`ValueError` for a non-`int`, a `bool` masquerading as one, a negative count, a non-enum
`kind`/`conditions`, a non-`LightSource` member; domain errors for RC silences and the RC-explicit
once-per-round limit. `IgnitionAttemptLimitError` is correctly *not* a subclass of
`IgnitionNotDefinedError` and that non-relationship is asserted. See LOW-8 and LOW-9.

## 8. Deterministic-case reconciliation

I enumerated the case IDs **from the card's own tables** myself: Illumination 5, Duration/depletion
14, Ignition 12, Mundane light state 10, Routed consequences 6, Seam guards 6 = **53**.
`CASE_DISCHARGE` holds 53, maps exactly, no gaps, no duplicate strings; split is 20 behavior / 5
invariant / 26 guard / 2 routed, matching the ledger's claim. The MED-4 arithmetic is honest this
time.

The *mechanisms*, however, do not all hold — see HIGH-1, MED-1, MED-2, LOW-5, LOW-6, LOW-7. MED-4
has recurred, in a different place and in a weaker form.

## 9. Architecture-review of the tests — see HIGH-1

## 10. Encoding and integrity — clean

All 13 changed files: valid UTF-8, no BOM, no foreign script. Non-ASCII in the three code files is
`§`, `—`, `…` only. The only mojibake anywhere is two tokens on **line 703** of the review-#1
artifact, which I confirmed are that reviewer's quoted search input — the ledger's claim here is
accurate. Four markdown files carry CRLF; that is pre-existing repo-wide checkout state, not a
defect.

## 11. Governance-record accuracy

Protected documents: the approved Rule Card was **not** modified by the remediation commit, and
review #1 is preserved byte-for-byte. The live artifacts consistently say *implementation complete,
issue **not** complete, review #2 pending*; nothing claims certification and nothing claims review
#2 passed. No stale "`EXP-006` implementation not authorized" claim survives; the remaining
`NOT AUTHORIZED` statements are cluster-level and accurate. `ARCHITECTURE.md` §15.2's
characterisation of review #1 ("no finding concerned rules logic, verified by mutation testing") is
accurate — review #1 ran 21 behavioural mutations, all caught. See MED-3, MED-4, MED-5, LOW-1,
LOW-10, LOW-11.

## 12. Canonical verification — all gates PASS, verbatim

```text
1164 passed in 2.07s
Differentiated coverage gate
  src/rules/               20 file(s) -- 100% required, per file
  src/survivability/       0 files -- trivially satisfied
  core (aggregate)         5 file(s) -- 100.00% (>= 95% required)
All differentiated coverage thresholds met.
All checks passed!
Success: no issues found in 52 source files
========================================
Tests:     PASS
Coverage:  PASS
Ruff:      PASS
mypy:      PASS
Evidence:  PASS
Overall:   PASS
========================================
```

Independently confirmed from `coverage.json`, per file:

```text
src\rules\exploration\errors.py                         131→  4/4 stmts 100%,  0 branches 100%
src\rules\exploration\light_and_exploration_resources.py  131/131 stmts 100%, 52/52 branches 100%
```

100% statement **and** branch on both production modules. `verify.py` defines exactly five gates:
Tests, Coverage, Ruff, mypy, Evidence.

## 13. Complete-darkness frontier — correctly recorded, not filled

Recorded in four places (card §8 + Open Question 7, plan §15, Pre-Code Gate §7, completion record
§6), every one of which states the owner is unresolved and **no Rule ID is invented**. The
implementation decides nothing: no complete-darkness predicate, no `NO_LIGHT`, no world-state type
or member exists. Clean.

---

# Findings

## HIGH-1 — the public-surface allowlist does not pin the public surface; six demonstrated escapes falsify the ledger's proven-closure claim for review #1's largest finding

**File:** `tests/rules/exploration/test_light_and_exploration_resources.py`
(`_public_top_level_definitions`, `test_the_public_definition_surface_is_exactly_the_approved_set`,
`test_public_class_members_are_exactly_approved`,
`test_public_function_parameters_are_exactly_approved`,
`test_this_module_uses_no_reflective_attribute_access`, `test_the_selector_stores_no_round_state`);
claims in `docs/technical/EXP-006_REVIEW_REMEDIATION_LEDGER.md` §2 (MED-4A, MED-4C), §3 and §5.

The ledger states that pinning the exact shape *"catches them all at once, regardless of spelling,
and keeps catching names nobody thought to forbid"*, and records **15/15 CAUGHT**. I reproduced all
eight of review #1's escapes (all now caught — that part is true), then devised new ones. **Six
escaped.** Each was applied to a scratch copy and the full 101-test module re-run:

```text
P-1   LightSource.fresh(kind, *, lit=False, party_surprised=False,
                         has_infravision=False)                       101 passed  ESCAPED
probe3 MundaneLightContribution(_AmbientMixin) gaining inherited
       ambient_state and encounter_range_feet properties              101 passed  ESCAPED
N-1   `if True:` block defining public VisibilityCategory
       (VERY_GOOD_LIGHT / DIM_LIGHT / NO_LIGHT), absent from __all__   101 passed  ESCAPED
N-2   `try:` block defining public encounter_distance_from_light()     101 passed  ESCAPED
N-20  top-level `for` loop injecting no_light_state via globals()      101 passed  ESCAPED
N-3   object.__getattribute__(item, "price")                           101 passed  ESCAPED
```

Root causes, each a distinct mechanism defect:

1. `_public_top_level_definitions()` iterates **`tree.body`** and matches only
   `FunctionDef`/`AsyncFunctionDef`/`ClassDef`/`AnnAssign`/`Assign`. Any public definition nested in
   a top-level compound statement is invisible. Because `test_all_matches_the_approved_surface`
   compares `__all__` to the same allowlist, simply omitting the new name from `__all__` completes
   the bypass. The authoritative *shape* of a module's public surface is its runtime namespace,
   which is what an importer sees; the guard inspects the declaration form instead. Review #1's
   root-cause note asked for a shape check and the remediation delivered a declaration check.
2. `test_public_class_members_are_exactly_approved` uses `vars(cls)`, which sees only a class's own
   `__dict__`. An inherited member is invisible. `_AmbientMixin` is underscore-private, so the
   definition allowlist skips it too, and `test_no_world_state_vocabulary_exists_on_the_aggregate`
   (a token denylist) does not contain `ambient`, `encounter` or `range`. Nothing asserts that
   `MundaneLightContribution` has no base class or that it is slotted.
3. `APPROVED_PARAMETERS` covers the seven module-level functions only. `LightSource.fresh` is a
   public classmethod and is unpinned, so `party_surprised` and `has_infravision` — the two
   literally forbidden inputs named by review #1's own MED-4 row and by card cases `L32`, `L35`,
   `L40` — can be added to a public constructor with the suite green.
4. `test_this_module_uses_no_reflective_attribute_access` requires `isinstance(node.func, ast.Name)`.
   `object.__getattribute__(item, "price")` parses as an `ast.Attribute` call, so it escapes — and
   `"__getattribute__"` in the guard's own forbidden set is a token that predicate **can never
   match**. (`item.__dict__["price"]` was caught only incidentally, by a runtime `AttributeError`
   because `Item` is slotted — not by any guard. `globals` is also absent from the set.)

**Failure scenario.** A later agent adds `encounter_range_feet` to `MundaneLightContribution` via a
mixin, or `has_infravision` to `LightSource.fresh`. `scripts/verify.py` reports `Overall: PASS` with
100% coverage. The card's `L31`, `L32`, `L35`, `L36`, `L40` say these MUST NOT EXIST;
`CASE_DISCHARGE` says each is discharged by the allowlist / "EVERY public signature pinned"; the
ledger says the mechanism was proved. All three are wrong, and the `ENC-001` ownership boundary that
the card's Finding B was written to protect is crossed without a single red test.

**This is not a rules defect** — I confirmed the shipped surface is clean. It is a false-confidence
defect, and it is severe because the remediation's own proof was built by re-running the eight shapes
review #1 had already published, which is the project's named defect mode: the mechanism was
validated against the known attack, then represented as closed in general. `APPROVED_DEFINITIONS`,
`APPROVED_MEMBERS` and `APPROVED_PARAMETERS` are the right instruments; they need to be compared
against `vars(light)` (minus imports), `dir(cls)`, and every public callable including class members.

Plan §16 falsification rows 4 and 10 ("Not expressible in the API", "a pinned public surface") carry
the same overstatement.

## HIGH-2 — production source still misdescribes its own contents and misquotes the approved Rule Card; review #1's HIGH-2 defect survives verbatim in the docstring the ledger says it fixed

**Files:** `src/rules/exploration/light_and_exploration_resources.py` lines 6–7, 290–294, 272–274;
`tests/rules/exploration/test_light_and_exploration_resources.py` lines 341–347.

Three separate false statements, in shipped production source:

**(a) The module docstring contradicts itself, and the stale half is HIGH-2's own defect.** At HEAD,
lines 6–7 read:

> `the implementation contract this module implements. This file currently` / `contains **Slice A
> only** — the light-source value/state model.`

while lines 30–33 read *"The card's responsibilities are implemented in full: … the ignition branch
selector (carrying ``SR-11``), and CHAR-004 identity binding."* Both sentences are in the same
docstring, above a 629-line module containing all four slices. The `40f7266→574f1a4` diff shows the
remediation replaced only the *closing* paragraph and never touched lines 6–7. The ledger's HIGH-2
closure claim — *"Module docstring now describes the delivered state"* — is therefore false: the
docstring says both things, and the first thing a reader sees is the wrong one. Review #1 quoted a
different sentence from the same docstring and also missed this one.

**(b) The code asserts a withdrawn clause is the approved card's current wording.**
`refuel_lantern`'s docstring, lines 290–294:

> *"On approved case **L12**: the card's own wording for that case reads *"contributes illumination
> again"*, and that wording is **not rewritten here**."*

The card's current `L12` (line 575) reads *"`24` remaining; **`lit = False`** — **no illumination
contribution until separately ignited** (§5). Refuelling restores fuel, not ignition."* The phrase
*"contributes illumination again"* occurs in the card exactly once, at line 44, inside the §Status
note that **withdraws** it. The test module repeats the same false claim at lines 341–347. The effect
inverts the authority relationship `AGENTS.md` §2 establishes: the code presents the adjudicated
requirement as the implementer's own reinterpretation of superseded wording, when the card now
specifies it literally.

**Failure scenario.** A future agent reads `refuel_lantern`, believes the approved card still says a
refuelled lantern *"contributes illumination again"*, treats `lit=False` as the implementer's gloss
rather than the card's text, and "re-corrects" refuelling to ignite — reversing the 2026-10-01 human
adjudication while citing the card.

**(c) A fabricated direct quotation of a protected approved document.** Lines 272–274 present, in
quotation marks and attributed to Rule Card §4:

> *"A lantern reaching zero consumes its flask; a further flask may be supplied, which resets
> `remaining_turns` to `24`."*

The card §4 (line 325) actually reads *"A lantern reaching zero consumes its flask, and a further
flask may be supplied, which **restores `remaining_turns` to `24` and leaves the lantern unlit**."*
The quotation changes `restores` to `resets` and **drops the adjudicated "and leaves the lantern
unlit" clause** — the exact clause the quoted passage exists to establish.

Supporting instances of the same slice-era staleness, left in source edited by this commit:
`LightSource`'s docstring lines 150–152 (*"Slice A has no domain rejection and therefore introduces
no exception type of its own"*, in a commit that introduced one for this very package), and
`errors.py` line 24 (*"**The two types are not interchangeable**"* in a module whose line 12 says it
holds three).

---

## MED-1 — the no-second-clock / no-round-state guards miss an integer module-level counter; `L13`, `L14`, `L19b` discharge rows overclaim

**File:** `tests/rules/exploration/test_light_and_exploration_resources.py`
(`test_the_selector_stores_no_round_state`), `CASE_DISCHARGE["L13"|"L14"|"L19b"]`.

`test_the_selector_stores_no_round_state` filters `vars(light)` for
`isinstance(value, (list, dict, set))`; an `int` is invisible, and `_public_top_level_definitions`
skips underscore names. Demonstrated:

```text
N-5b  _TURNS_COUNTED = 0 at module level; `global _TURNS_COUNTED;
      _TURNS_COUNTED += spent` inside deplete(), after validation   101 passed  ESCAPED
N-6   _ROUNDS_SEEN = 0 at module level; incremented inside
      ignition_outcome()                                            101 passed  ESCAPED
```

Card `L13` says *"This card advancing or counting turns itself — MUST NOT OCCUR"*; `L14` *"Any
second turn counter, clock or elapsed-time field owned here — MUST NOT EXIST"*; `L19b` *"This card
tracking rounds … MUST NOT OCCUR"*. `CASE_DISCHARGE` cites "no module-level mutable exists" and
"`__slots__` and the aggregate's single field are pinned" — mechanisms that cover class fields and
three container types, not module-level scalars. A cross-call accumulator of authoritative elapsed
turns inside `EXP-006` is exactly the duplicate time authority `ARCHITECTURE.md` §5 and card §4
forbid, and it passes.

(My first variant, N-5, was caught — but only incidentally, because placing the increment *before*
`_require_elapsed_turns` turned a `ValueError` test into a `TypeError`. Moving it one line later
escapes. `L19b`'s further claim "flag never mutated" is discharged by Python's immutable `bool`, not
by any assertion in the suite.)

## MED-2 — `L42`'s mechanism is bypassable and does not establish the case as the card words it

**Files:** `tests/.../test_light_and_exploration_resources.py`
(`test_this_module_uses_no_reflective_attribute_access`,
`test_no_catalog_economic_field_is_ever_accessed`), `CASE_DISCHARGE["L42"]`.

Two distinct problems.

**(a) Bypassable.** N-3 above: `object.__getattribute__(_LIGHT_SOURCE_IDENTITIES[kind], "price")`
reads an economic field with 101/101 passing, because the guard's predicate requires `ast.Name`. The
ledger's LOW-14 closure claim — *"so the `ast.Attribute` matcher can no longer be bypassed by
reflection"* — is falsified, and the guard's forbidden set contains a token (`__getattribute__`) its
own predicate cannot reach.

**(b) Wrong property.** Card `L42` is worded *"Any price, `Coin` or encumbrance value **emitted** —
MUST NOT EXIST"*. The cited mechanism establishes that the module never **accesses** such a field.
Those are different properties, and the implementation sits on the other side of the line as
literally written: `catalog_identity(TORCH).price` returns a `QuantityPrice` containing `Coin`,
because the module returns `CHAR-004`'s whole `Item`. I regard the **behaviour** as authorized —
plan §9.1/§9.3 (APPROVED) explicitly mandate `catalog_item(...)` and nominate the AST read-guard as
the mechanism, and returning `CHAR-004`'s own object is the correct single-source-of-truth choice.
The defect is the discharge claim: nothing in the suite establishes non-emission, and nothing records
that emission-by-reference is the adjudicated reading of `L42`.

## MED-3 — plan §10.2 still prescribes `ValueError` for `L19`, contradicting the shipped code and the §9 adjudication; §10.1 still recommends the dropped base class

**File:** `docs/technical/EXP-006_IMPLEMENTATION_PLAN.md` §10.1, §10.2.

§10.2's per-case mapping table still reads:

> `| L19 | second ignition attempt in one round | ValueError — a caller-protocol violation, not a
> rules gap |`

The shipped code raises `IgnitionAttemptLimitError`, and `errors.py` records that the `ValueError`
treatment *"was wrong: RC's once-per-round rule is exactly what rejects it."* §10.2 also has no row
for `L12a`/`LanternRefuelNotDefinedError`. §10.1 still recommends `class ExplorationError(Exception)`
plus one subclass and asserts *"One base plus one subclass — no hierarchy is built ahead of need"*,
which §11 later contradicts. LOW-9's remediation corrected §11 and §16 row 10 and left the plan's
normative per-case mapping stating the superseded representation — the same plan/code disagreement,
in the section an implementer would actually consult.

## MED-4 — the deterministic-case classification is mutually inconsistent across all three governance artifacts, and `LOW-12`'s correction points at an artifact that is itself wrong

**Files:** `docs/technical/EXP-006_IMPLEMENTATION_PLAN.md` §12;
`docs/technical/EXP-006_PRE_CODE_GATE.md` §6.

Pre-Code Gate §6's dated `LOW-12` note says the count and the `L22` classification are corrected and
that *"the authoritative split is in the implementation plan §12 and the test ledger."* Checking that
pointer:

- **Plan §12 contains three mutually inconsistent totals.** Heading: *"all 53"*. Blockquote:
  *"Running totals: unit behavior 19, ownership guard 19, internal invariant guard 12, routed
  dependency 3"* (= 53). Next line: *"Counts re-derived from the approved card for this plan, **not
  assumed from the gate**; they match: **18 / 18 / 11 / 3**"* (= 50). The table itself: 18 / 18 / 12
  / 3 (= **51**), and I verified by enumeration that **`L19a` and `L19b` appear in no row of it** —
  the two cases the blockquote says were added. A "re-derived … they match" assertion that matches
  neither the table above it nor the card is precisely the MED-4 defect class.
- **Gate §6's own table was not corrected** — it still reads 18 / 18 / 11 / 3 = 50 and still lists
  `L22` under *Routed dependency*, the two things the note says are fixed.
- **The superseded figure survives inside the corrected section.** Line 235 now reads *"26 guards of
  53, as finally recomputed"*; line 239, four lines later, still reads *"the 29 guards are mostly
  negative/architectural assertions."* The ledger's LOW-12 entry claims *"The '29 of 50' profile line
  corrected to '26 guards of 53'"* — one of the two numbers was corrected.
- Gate §6 and plan §12 also disagree on where `L30` and `L36` sit.

A consistent 53-case classification exists in exactly one place: `CASE_DISCHARGE` in the test module.
Every governance artifact that points at another one is pointing at a stale table.

## MED-5 — the completion record created to close `MED-3` does not satisfy `DEVELOPMENT_WORKFLOW.md` §5

**File:** `docs/completion-records/ISSUE-022-exp-006-light-and-exploration-resources.md`.

§5 of a protected document requires twelve numbered categories **"in order"**, and states that a
category with no entries must say so explicitly *"rather than omitting it — an omitted category is
ambiguous; an explicit 'none' is not."* Measured against it:

| §5 item | ISSUE-022 |
|---|---|
| 3. Files created/modified/deleted, **grouped** | §1 lists three code files, ungrouped, and **omits the eight documentation artifacts the same commit changed** (`ARCHITECTURE.md`, `INVENTORY.md`, cluster record, plan, gate, `INDEX.md`, the ledger, this record) |
| 4. Behavior actually implemented | a three-row table column, not a description of what the system now does |
| 5. **Rules provenance** | **absent** — no provenance classification stated |
| 6. **Tests added/modified**, "what behavior each important test protects, not merely a file list" | **a file list** |
| 10. **Deviations** — *state "None." when true* | **category absent entirely**, although plan §11 and §14 record three (three error types vs the plan sketch, test-file location, `_CATALOG_NAMES` shape) |
| order | 1→12 order not followed |

The artifact created specifically to discharge `MED-3` does not meet the protected standard that
governs that artifact. Also: §1's line counts are `~640` / `~125` / `~1200` against actual 629 / 123
/ **1341**.

---

## LOW findings

- **LOW-1** — `ISSUE-022` §5 claims *"tests, coverage, Ruff, mypy strict, Evidence, **policy**: all
  PASS."* `scripts/verify.py` defines exactly five gates and no `policy` gate. A verification result
  is claimed for a mechanism that does not exist.
- **LOW-2** — `CATALOG_ECONOMIC_FIELDS` is a hand-maintained eight-name denylist. It happens to cover
  all eight non-identity `Item` fields today, but nothing keeps it in sync: a new `CHAR-004` `Item`
  field would be readable with the suite green.
  `frozenset(f.name for f in dataclasses.fields(Item)) - {"name", "category"}` is the rank-1 shape
  mechanism the project's own preference order prescribes.
- **LOW-3** — `test_no_catalog_economic_field_is_ever_accessed` has **no non-vacuity anchor**, unlike
  the sibling guard added for LOW-14 (which asserts `calls`). It is the sole mechanism for `L42`'s
  core property, and if its AST walk ever matched zero `ast.Attribute` nodes it would pass on
  nothing. The ledger's §3 claim that *"every AST guard expected to inspect nodes asserts that it
  actually anchored"* is not true of this one.
- **LOW-4** — `test_the_derived_figures_cannot_disagree_with_the_sources` is written as
  `assert not hasattr(..., "__dataclass_fields__") or set(...) == {...}` — a disjunction that passes
  if the structure it inspects disappears. It is cited as a mechanism for `L14`.
- **LOW-5** — the `L16` arithmetic guard's docstring claims *"no int multiplication or
  floor-division survives on EITHER operand"*; it matches int **Constants** only. `value *
  TORCH_TURNS` escapes it (my N-7 was caught only by an incidental validation path, not by the
  arithmetic check).
- **LOW-6** — `CASE_DISCHARGE["L4"]` ("one radius constant, so the radii cannot differ") and `["L5"]`
  ("public member surface pinned") both mis-cite. I demonstrated (N-13) that a per-kind radius split
  is writable with one constant and no new member; what catches it is the parametrized behavioural
  radius test — which review #1's own line 335 already recorded. MED-4B's *"categories recomputed
  from the actual mechanism"* does not hold for these two rows.
- **LOW-7** — `CASE_DISCHARGE["L18"]` is classed `behavior:`, but the card's `L18` content (*roll
  `3`; fails; may retry next round*) is not this module's to produce — the module never rolls. The
  cited mechanism establishes only that the same input re-selects the same branch. The test docstring
  says this honestly; the ledger row's category does not.
- **LOW-8** — `src/rules/exploration/errors.py` line 24: *"**The two types are not
  interchangeable**"*, in a module whose line 12 states it holds three domain rejections.
- **LOW-9** — `LanternRefuelNotDefinedError` covers a wrong-kind request (a torch, arguably a
  category mismatch) and a genuine RC silence (a partly-full lantern) under one type, distinguishable
  only by message substring. The card specifies neither, so this is not a conformance defect, but a
  caller cannot programmatically tell "you passed the wrong kind of source" from "RC states no
  procedure".
- **LOW-10** — `SR-11`'s registration registry was not updated by `HIGH-1`'s own fix. Cluster record
  §10's *"Recorded on:"* list and `ISSUE-022` §2's *"registered in **four** places"* both omit
  `ARCHITECTURE.md` §15.2, which `HIGH-1` added — and `ISSUE-022` then describes that fifth location
  two lines later.
- **LOW-11** — `INVENTORY.md`'s `EXP-006` source cell cites *"Ch. 5 pp. 81–86 (`Fire-Building`,
  **`Blind Shooting`**)"*. The approved card's RC-source table carries no `Blind Shooting` entry (it
  carries `Lip Reading`, p. 84). Two project artifacts disagree about which RC objects bear on this
  card. Reported as a repository inconsistency only; **I performed no RC research** and this is
  pre-existing (it predates `574f1a4`).

## Observations, not findings

- `L17`'s *"ignites on `1` or `2`"* exists only inside the identifier `ROLL_1D6_IGNITE_1_2`; no
  consumer can read the threshold as data. This follows from card §5 assigning the roll to the
  caller, so I do not treat it as a defect.
- The exhausted-never-lit **construction** invariant refuses an input combination the card never
  contemplates. It is stronger than the card, cannot produce a forbidden outcome, and is explicitly
  authorized by plan §6.1 and the gate — correct, and the best engineering in this module.
- The approved card was modified twice after approval (`5594907`, `e5d92ad`); both are recorded
  in-card as human adjudications. I cannot independently verify that authorization and did not reopen
  it; the remediation commit left the card untouched, which is what was in scope.

---

# Verdict

The rules logic is correct, conforms clause by clause to the approved card, carries `SR-11` exactly
where the ruling places it, refuses the three RC silences by absent keys, invents no owner for the
complete-darkness frontier, and survived fifteen rules-logic and state-space mutations. All five
canonical gates pass with 100% statement and branch coverage per file. Nothing claims the issue is
complete or certified. Those are real results and the remediation genuinely closed much of review #1.

But the two centrepiece closure claims do not hold. `HIGH-2`'s own defect — production source denying
what it contains — is still in the module docstring, four lines above the sentence that was rewritten
to fix it, and the code additionally asserts a withdrawn card clause as the card's current wording and
misquotes §4 with the adjudicated clause removed. `MED-4A`'s allowlist, proved against only the eight
shapes review #1 had published, is walked past by six new mutations, two of them realistic and two of
them adding literally forbidden surface (`party_surprised`/`has_infravision` on a public constructor;
an `encounter_range_feet` derivation on the aggregate). `MED-4` itself recurs in the governance
artifacts: the one instrument the Pre-Code Gate names as authoritative for the 53-case split contains
three contradictory totals and omits two cases. The ledger is, on these points, an audit artifact that
claims more than its mechanisms establish — the project's stated recurring defect mode, reproduced in
the document written to close it.

`EXP-006 FINAL IMPLEMENTATION REVIEW #2: FAIL`

```text
HIGH  2   HIGH-1 public-surface guard escapes + falsified MED-4A/4C closure claim
          HIGH-2 production source misdescribes its contents and misquotes the card
MED   5   MED-1 int module counter escapes the no-second-clock/no-round-state guards
          MED-2 L42 mechanism bypassable, and does not establish "emitted"
          MED-3 plan §10.2 still prescribes ValueError for L19; §10.1 base class
          MED-4 53/51/50 case-count inconsistency across plan §12 and gate §6
          MED-5 ISSUE-022 does not satisfy DEVELOPMENT_WORKFLOW §5
LOW  11   LOW-1 .. LOW-11 as itemised above
```

No remediation was performed in this pass. The repository is byte-identical to `574f1a4`;
`git status` is clean and `HEAD` is unchanged.
