# `EXP-006` INDEPENDENT FINAL IMPLEMENTATION REVIEW #3

> **Preserved verbatim as received.** Third independent final implementation review, performed
> against `HEAD` `d66db5f` by a reviewer that did not write the implementation, the Rule Card, the
> plan, the gate, the guards, the issue record or either remediation ledger, and that was forbidden
> to change anything. Historical evidence on the same terms as reviews #1 and #2: **not** to be
> rewritten, relabelled or softened.
>
> Recorded in the repository 2026-10-03 because the review was returned as a task result rather
> than written into the tree. Content unaltered; only the transport's HTML entity escaping of `>`
> and `<` has been undone.
>
> **Verdict: `FAIL` — 1 HIGH, 4 MED, 8 LOW.** No rules defect, for the third consecutive review.

## 1. Reviewed HEAD

```text
WORKTREE     C:/Users/evanp/source/repos/OD_N_D-cluster-004-exp-006-stage-b
BRANCH       cluster-004-exp-006-stage-b          (as assigned)
HEAD         d66db5f6cccda857ede6a8031340586b4aafc3f2   (matches d66db5f)
MAIN         c1bdd5c01e998f961b3851c3d95a225b37fa9cc7
ORIGIN/MAIN  c3a3e2d9d961a1df8ec3ccad3823929b0a41cac0
STATUS       clean; no upstream tracking line
```

No worktree collision. HEAD unchanged at the end of the review.

## 2. Independence statement

I did not write this code, the Rule Card, the plan, the gate, the guards, the issue record or either
remediation ledger. **I modified nothing** — no production code, no test, no governance artifact,
not a typo. No commit, merge, push, rebase, stash, reset or clean. No new Rules Cyclopedia research;
no RC page fetched; Stage A not reopened. The approved Rule Card was my only rules authority. Both
remediation ledgers and every author-written summary were treated as assertions and re-verified
independently: the 53-case total, the category split, the coverage figures, the test count, the five
verification gates, the `N-R3` caveat and the published mutation results were all re-derived, not
accepted.

## 3. Artifacts reviewed

Governing: `AGENTS.md`, `CLAUDE.md`, `GAME_CONSTITUTION.md` §5, `SOURCE_HIERARCHY.md`,
`ARCHITECTURE.md` (§5, §10, §15.1, §15.2, §16), `DEVELOPMENT_WORKFLOW.md` §5/§5.1,
`TESTING_STRATEGY.md`.

Package: the approved card `docs/rules/exploration/light_and_exploration_resources.md` (in full,
every bounded-correction note); `docs/technical/EXP-006_IMPLEMENTATION_PLAN.md`;
`docs/technical/EXP-006_PRE_CODE_GATE.md`;
`docs/rules/clusters/CLUSTER-004-equipment-resources-and-evasion.md`; `docs/rules/INVENTORY.md`
(`EXP-006` row, and `CHAR-005`'s for the `SR-11` registry); both final-review artifacts; both
remediation ledgers; `docs/completion-records/ISSUE-022-...md` and `INDEX.md`;
`src/rules/exploration/light_and_exploration_resources.py`; `src/rules/exploration/errors.py`;
`tests/rules/exploration/test_light_and_exploration_resources.py` (all lines);
`docs/rules/character_creation/encumbrance_and_movement_rate.md` (SR-11 denials); `git log` and
`git show d66db5f`.

## 4. Rule Card conformance — CLEAN

Re-derived from the card and verified by direct execution against the live module (read-only):

| Clause | Card | Observed |
|---|---|---|
| Torch radius | 30′ (§2) | `30` |
| Lantern radius | 30′ (§2) | `30`, same single constant `MUNDANE_LIGHT_RADIUS_FEET` |
| Fresh torch | 6 turns (§3) | `6` |
| Fresh lantern | 24 turns/flask (§3) | `24` |
| Unlit source retains fuel | L11 | unlit torch keeps `6` |
| Exhausted source never lit | §4, Finding C | `LightSource(TORCH, 0, lit=True)` → `ValueError` **unconstructible** |
| Exhausted/unlit contributes nothing | L3, L9, L15a | `illumination_radius_feet is None`; excluded from the aggregate |
| Elapsed turns caller-supplied | §1, §4 | `deplete(sources, elapsed_turns: int)`; no time import |
| `bool` rejected | plan §1.1 | `elapsed_turns=True` → `ValueError` |
| Negative rejected | — | `-1` → `ValueError` |
| Zero accepted | §4 | no state change |
| Only lit sources deplete | L11 | unlit untouched |
| Floors at zero | L10 | 9 turns vs 6 → `0` |
| Zero extinguishes **that** source | L9 | `lit=False`, radius `None` |
| No world-darkness transition | L15b, L29, L37a | `deplete` returns `tuple[LightSource,...]` and nothing else |
| No fresh-duration ceiling | human adjudication | `LightSource(TORCH, 600, lit=True)` constructs; depletes to `594` |

Ignition — all eight combinations executed independently, each resolving exactly once:

```text
skill  tinderbox  conditions   observed
 yes      yes      ORDINARY    AUTOMATIC
 yes      yes      ADVERSE     ROUTED_SKILL_CHECK
 yes      no       ORDINARY    ROLL_1D6_IGNITE_1_2
 yes      no       ADVERSE     ROUTED_SKILL_CHECK      <- SR-11, exactly once
 no       yes      ORDINARY    ROLL_1D6_IGNITE_1_2
 no       yes      ADVERSE     IgnitionNotDefinedError
 no       no       ORDINARY    IgnitionNotDefinedError
 no       no       ADVERSE     IgnitionNotDefinedError
```

`_IGNITION_MATRIX` holds exactly 5 entries; the three silences are absent keys, so **no default
exists to reach** — refusal is structural, not a fallback. It is a mapping, so no wildcard overlap
and no evaluation-order precedence is possible. The same-round limit precedes matrix lookup:
`(False, False, ADVERSE, attempt=True)` raises `IgnitionAttemptLimitError`, not the silence.
Malformed API input (`1` for a bool, a string for `conditions`, a non-`LightSource` member) is
structurally rejected throughout.

Contribution is limited to EXP-006-owned mundane facts: `lit_sources`, `any_mundane_source_lit`,
`max_mundane_radius_feet` (`None`, never `0`). A malformed member **rejects** (`ValueError`) rather
than silently disappearing — verified for `"torch"`, `{"lit": True}`, `None`, `42` and a duck-typed
impostor.

## 5. Refuel / error-taxonomy result — CLEAN

```text
refuel_lantern(torch, 0 turns)         -> ValueError("refuel_lantern is a lantern operation…")
refuel_lantern(lantern, 7 turns)       -> LanternRefuelNotDefinedError("…only for a lantern that has reached zero")
refuel_lantern(lantern, 0 turns)       -> LightSource(LANTERN, remaining_turns=24, lit=False)
```

Taxonomy verified in code **and** by mutation, not by reading the tests' structure:

- MROs confirmed empirically: all three domain types are `(T, Exception, BaseException, object)` —
  **not** `ValueError` subclasses. This is what makes the suite's
  `not isinstance(..., ValueError)` / `not isinstance(..., LanternRefuelNotDefinedError)`
  assertions non-vacuous.
- Control M19 (make `LanternRefuelNotDefinedError` a `ValueError` subclass) → **CAUGHT**.
- Control M18 (revert the non-lantern case to the domain error) → **CAUGHT**.
- Control M17 (partial refill tops up to 24 instead of refusing) → **CAUGHT**.
- Control M20 (same-round guard moved after the matrix) → **CAUGHT**.

`L12a` is correctly scoped. `CASE_DISCHARGE["L12a"]` reads "invariant: `LanternRefuelNotDefinedError`
on a **VALID lantern's** partial refill" — the non-lantern case is **not** claimed as a Rule Card
case anywhere: plan §10.2 lists it under "*(not a case)*", `errors.py`'s scope note states the card
specifies none, and ISSUE-022 §10 item 5 records it as a deviation with the adjudication. No case ID
was invented for it.

## 6. SR-11 — CLEAN

Registered in exactly the five locations the records claim, and all five are correct and consistent:
card §Simulator Ruling; `CLUSTER-004` §10; `INVENTORY.md`'s `EXP-006` row; plan §11;
`ARCHITECTURE.md` §15.2. Scope verified mechanically: it affects **only**
`(skill=True, tinderbox=False, ADVERSE)`. The sibling row `(True, False, ORDINARY)` still yields
`ROLL_1D6_IGNITE_1_2`, so the ruling bites without widening. Control M22 (flip the SR-11 row) →
**CAUGHT**. One stale third-party denial remains — see `LOW-3`.

## 7. Ownership boundaries — CLEAN

EXP-006 implements and owns **none** of: dungeon time advancement, round tracking, `TurnCredit`
provenance, complete darkness, global illumination, encounter `Visibility`, encounter distance,
surprise, blindness, darkness combat penalties, infravision possession, `CHAR-012` skill resolution,
RNG execution, magical light/darkness, rations, starvation, or combat use of torch/oil. No
parameter, field, type, return value or operation expresses any of them.

**Direct vs transitive, measured rather than asserted.** Direct imports are exactly `__future__`,
`collections.abc`, `dataclasses`, `enum`, `types`, `typing`, `rules.character_creation.equipment`,
`rules.exploration.errors`. Importing the module transitively loads `rng`, `rng.errors`,
`rng.expressions`, `rng.results`, `rng.rng` and `rules.currency` through the `CHAR-004` seam the
plan *directs* it to use; it does **not** load `turn_credit` or `dungeon_turn_time_accounting`. The
suite states this correctly and narrowly — review #1's `MED-6` overclaim is genuinely corrected, and
no document now says importing EXP-006 proves no RNG/currency module loads. The accurate guarantee,
"no RNG is consumed," holds: no RNG object is constructed and no RNG method called.

`_require_elapsed_turns` owns the numeric domain and explicitly disclaims provenance, with no fake
provenance wrapper — matching the approved plan §1.1.

## 8. CHAR-004 seam — CLEAN

The identity binding is private (`_catalog_identity`, `_oil_flask_identity`,
`_tinderbox_identity`), absent from `__all__`, and reached only by tests. EXP-006 consumes canonical
identities for Torch (`equipment.TORCH`, used by identity), Lantern, Oil and Tinder box, with the
three strings confined to one private `_CATALOG_NAMES` mapping (AST-verified as the single site).
`"Oil"` resolves to the Adventuring-Gear row; control M26 (swap to `"Oil, Burning"`) → **CAUGHT**.

No public API exposes catalog economics. The `L42` reading is sound against the card's wording. The
card forbids *emitting* a price/`Coin`/encumbrance value; it does not make retaining a canonical
`CHAR-004` identity an ownership transfer of that row's unrelated fields. The implementation
satisfies the literal wording by shape: no public callable returns an `Item` (all four return pinned
non-`Item` types), class surfaces and slots are pinned so no field can carry one, and `Item` is not
re-exported. The supporting AST guard derives its forbidden field set from
`dataclasses.fields(Item)`, so a new `CHAR-004` field extends it automatically. Control M25-class
reflection is discussed under `LOW-6`.

## 9. Runtime module surface — **ONE DEMONSTRATED ESCAPE (HIGH-1)**

I attacked the guard with novel shapes, not the author's published mutations.

| Probe | Result |
|---|---|
| M2 public name bound inside a top-level `match` statement | CAUGHT |
| M3 name injected via `deplete.__globals__[...]` (a mechanism outside the reflective set) | CAUGHT |
| M4 private module-level scalar accumulator `_LAST_ELAPSED = 0` | CAUGHT |
| M5 unexpected public callable `encounter_range_feet()` | CAUGHT |
| M6 unexpected public constant `NO_LIGHT_RADIUS_FEET`, omitted from `__all__` | CAUGHT |
| **M1 / M28 module-level `__getattr__` (PEP 562)** | **ESCAPED** |

`_module_scope_names()` filters any name that both starts and ends with `__`, so a module-level
`def __getattr__(name)` is invisible to it — and `__getattr__` is a *dynamic attribute surface*, so
it needs no further names. Demonstrated concretely on the scratch copy with the suite fully green
(111/111):

```text
light.encounter_distance_from_light(True)  -> 40
light.VisibilityCategory                  -> ('VERY_GOOD_LIGHT', 'DIM_LIGHT', 'NO_LIGHT')
'encounter_distance_from_light' in vars(light)   -> False
'encounter_distance_from_light' in light.__all__ -> False
```

This escapes the **stated** claim, not an invented stronger one. The guard section's own header says
"EXP-006's two production modules **bind exactly the approved set of module-level names**";
`test_the_module_scope_surface_is_exactly_approved` says "Any new module-level name, **however
spelled and however created**, fails here"; `test_no_module_level_mutable_state_exists` says
"EXP-006 **defines only** the approved module-level state." All three are false in the presence of a
`__getattr__` hook, and the escape produces exactly the two artefacts the card most emphatically
forbids (a `Visibility` category — `L30`, `L31` — and a light→encounter-distance path — `L36`).

Nothing shipped uses `__getattr__`; this is a guard-breadth defect, not a rules defect.
`errors.py`'s namespace guard has the same hole.

## 10. Class and signature surfaces — CLEAN

| Probe | Result |
|---|---|
| M7 inherited public **data attribute** (`ambient_visibility`) via a base on `LightSource` | CAUGHT (`dir()` + MRO) |
| M8 inherited public **method** (`is_party_in_darkness`) on the aggregate | CAUGHT |
| M9 inherited public **property** (`visibility_category`) on the aggregate | CAUGHT |
| M10 **private-only** mixin (`_round_counter`, no public member) | CAUGHT (MRO pin alone) |
| M12 unauthorized `has_infravision` on **`deplete`** | CAUGHT |
| M13 unauthorized `party_surprised` on **`mundane_light_contribution`** | CAUGHT |
| M14 unauthorized `round_number` on **`ignition_outcome`** | CAUGHT |

All three callables I mutated are different from those previously mutated (`LightSource.fresh`, both
properties, both constructors). `APPROVED_CALLABLES` pins all ten public callables including the
generated constructors and all three properties;
`test_no_public_callable_escapes_the_signature_guard` independently *discovers* the public callable
set and asserts it equals the pinned set, so a new public method cannot go unpinned. Every guard
carries a non-vacuity anchor (`assert actual`, `assert calls`, `assert attributes`,
`assert assignments`, `assert checked == N`, and the derived-field-set anchor). `LOW-4`'s
`test_the_derived_figures_cannot_disagree_with_the_sources` disjunction is genuinely fixed — the
dataclass is asserted to exist before its fields are inspected.

## 11. No-second-clock — narrower than two discharge rows claim (MED-3)

**No shipped mutable state can act as an EXP-006-owned time or round counter.** Module scope holds
four `int`/mapping constants, two read-only `MappingProxyType`s, one frozen `Item`, three enums, two
frozen slotted dataclasses and five functions; both value types are slotted to their pinned fields;
`ignition_outcome` holds no attribute state; no clock, counter or accumulator exists. The claim as
*narrowly stated* ("the module-level state surface, exactly") is true.

But the mechanism does not reach the card's full statement. `L14` forbids "Any second turn counter,
clock or **elapsed-time field owned here** — MUST NOT EXIST". M27 demonstrates one that survives:

```python
class LightSource:
    _rounds_elapsed = 0        # private class attribute on an approved class
...
def deplete(...):
    spent = _require_elapsed_turns(elapsed_turns)
    LightSource._rounds_elapsed = LightSource._rounds_elapsed + spent   # a working accumulator
```

111/111 still pass. It is not a module-level name; `dir()`'s public filter skips it; `__slots__`,
`__dataclass_fields__` and the MRO are unchanged. `CASE_DISCHARGE["L13"]` ("import graph has no time
module; module-scope name set pinned") and `["L14"]` ("module-scope state immutable; slots and MRO
pinned") both cite mechanisms that do not cover it. The guard's own prose also asserts an exhaustive
dichotomy — "an accumulator needs **either** a new name (the surface guard refuses it) **or** an
approved constant's name (the value tests refuse that)" — which M27 falsifies with a third option.
The adjacent disclaimer ("does not claim the test recognizes every semantic notion of a clock")
partly mitigates, which is why this is MED and not HIGH.

## 12. `N-R3` caveat — accurately documented; one framing imprecision (LOW-6)

1. **Accurate.** I replayed it: `dataclasses.astuple(item)` via an aliased import is **not** matched
   by the reflective-access guard (it is neither a reflective `ast.Name` call nor a reflective
   `.attr`), and is caught by the module-scope namespace guard because the import binds a new name —
   exactly as the ledger says. The note's claim is if anything conservative: with the alias
   authorized in `APPROVED_IMPORTED_NAMES`, `test_the_complete_production_dependency_surface` still
   fails it.
2. **No unauthorized path in production.** The shipped module reads only `.name` (on enums),
   `.kind`, `.lit`, `.remaining_turns`, `.lit_sources`, and subscripts its own mappings. No
   `getattr`/`vars`/`eval`/`__getattribute__`/`__dict__`, no economic field by attribute or
   subscript.
3. **The stated machine-checkable claim is truthful**, and the repository does **not** represent the
   narrower guard as a general proof — the test docstrings and `CASE_DISCHARGE` both label the
   residue claim C. The one imprecision: the note attributes the residual risk to a future agent
   authorizing a new import, whereas `_LIGHT_SOURCE_IDENTITIES[kind].__getstate__()` reaches every
   catalog field with **no import change at all** (M25, suite green). That does not breach `L42` as
   worded — nothing public returns an `Item` — so it is a precision note, not a failure.

## 13. Independent 53-case reconciliation — CLEAN

I enumerated case IDs from the approved card myself rather than assuming the figure:

```text
Illumination        L1-L5                                            5
Duration/depletion  L6-L12, L12a, L13, L14, L15, L15a, L15b, L16    14
Ignition            L17-L19, L19a, L19b, L20-L26                    12
Mundane light state L27-L36                                         10
Routed consequences L37, L37a, L38-L41                               6
Seam guards         L42-L47                                          6
                                                      TOTAL         53
```

53 table rows, all unique, no duplicates, and no `L`-token mentioned in the card that is not a table
row. **The expected 53 is re-derived, not assumed.**

My own counts from `CASE_DISCHARGE`, parsed independently of the author's test:

| Claim kind | My count | Published |
|---|---|---|
| `behavior` | 23 | 23 |
| `invariant` | 5 | 5 |
| `surface` | 23 | 23 |
| `reviewed` | 1 | 1 |
| `routed` | 1 | 1 |
| **total** | **53** | **53** |

Zero missing, zero extra, zero duplicate keys, 53 distinct discharge strings, every row declaring
its claim kind. `L37` correctly labelled claim C; `L47` correctly routed.

Mechanism accuracy, audited row by row: one mis-cited row (`L46`, `LOW-2`); two rows whose cited
mechanism is narrower than the case statement (`L13`, `L14`, folded into `MED-3`); ten `surface:`
rows resting on the module-scope name set, whose cited mechanism is weakened by `HIGH-1` (`L13`,
`L15`, `L29`, `L30`, `L31`, `L36`, `L37a`, `L43`, `L44`, `L45`). The remaining 40 rows name a
mechanism that genuinely discharges the case. The ledger's framing as traceability-not-certification
is correct and prominently stated.

## 14. Plan / gate / status truthfulness — **FAILS (MED-1, MED-2)**

Correct and current: `ARCHITECTURE.md` §15.2 (both FAILs recorded, third review required, SR-11
affirmed, the earlier denial corrected with a dated note), `docs/completion-records/INDEX.md`,
ISSUE-022's status block and chronology. No invented verification gate survives anywhere live; no
live "no Simulator Ruling" claim about `EXP-006`; no live "not implemented" claim.

Stale or contradictory, as current normative statements:

- `docs/rules/INVENTORY.md` line 106 — "all 14 findings were remediated 2026-10-03 and **a second
  independent review is pending**".
- `docs/rules/clusters/CLUSTER-004-...md` line 420, under the explicit heading "**Live next step, as
  of 2026-10-03:**" — "`EXP-006` A SECOND INDEPENDENT FINAL IMPLEMENTATION REVIEW. Review #1
  returned FAIL…".
- `docs/technical/EXP-006_IMPLEMENTATION_PLAN.md` §18 line 705 — "`EXP-006` IMPLEMENTATION
  COMPLETE -- pending independent review #2 PASS"; and §1.2 lines 52–55, which name only review #1
  and its 14 findings.
- `docs/technical/EXP-006_PRE_CODE_GATE.md` §5.F line 208 — "`L12` confirms it **contributes
  again**", the card's expressly **withdrawn** wording, inside a section §8a declares to be standing
  ("Every other finding above stands"). §8a's companion claim that "§1–§8 are preserved unaltered"
  is itself false: §6 carries a 2026-10-03 correction. §5.C additionally glosses
  `ROLL_1d6_IGNITE_1_2` as "this card's own roll", which the approved plan §11 and the shipped
  module contradict.

## 15. ISSUE-022 — structurally compliant, materially wrong in §3 (MED-4)

All twelve `DEVELOPMENT_WORKFLOW.md` §5 categories are present, in order, with explicit "none" where
empty. §5.1 is respected: the record states `STATUS: NOT COMPLETE` and does **not** claim completion
before this review and human acceptance; §11 item 1 says so again; the chronology lists review #3 as
pending. Rules provenance (§5) is accurate against `GAME_CONSTITUTION.md` §5 — exactly one Simulator
Ruling, no Compatible Completion, no Human-Approved Variant. §7's commands and §8's five gates are
real and I reproduced them. §9's coverage figures are correct.

§3 is factually wrong and contradicts §6 of the same record: `errors.py` "(102 lines)" is 160; the
module "(529 lines)" is 648; the test module "(1418 lines) — **108 tests**" is 1800 lines and
**111** tests, while §6 says "**111 tests**". §10 (Deviations) is also incomplete — see `LOW-5`.

## 16. State-space falsification — CLEAN

Every forbidden state refused, every permitted state constructible:

```text
lit=True, remaining_turns=0            -> ValueError  "an exhausted source is never lit"
remaining_turns=-1                     -> ValueError  "must not be negative"
remaining_turns=True (bool)            -> ValueError  "must be an int"
kind="TORCH" (unsupported)             -> ValueError  "must be a LightSourceKind"
LightSourceKind members                -> exactly {TORCH, LANTERN}; M-control adding a third CAUGHT
aggregate with a malformed member      -> ValueError  "must contain LightSource values"
aggregate with an unlit/exhausted member -> ValueError "only lit sources"
refuelled lantern becoming lit         -> impossible; control M16 CAUGHT
partial refill with invented arithmetic -> refused;   control M17 CAUGHT
LightSource(TORCH, 600, lit=True)      -> CONSTRUCTS; depletes by 6 to 594
```

The unapproved `remaining_turns <= fresh_duration` invariant is confirmed **absent** — but its
absence is unguarded (`LOW-1`).

## 17. Guard quality and mutation findings

Thirty mutations run on the scratch copy; **24 caught, 6 escaped across 4 distinct classes.** I
evaluated each guard by *claim → mechanism → does the mechanism prove the claim*, not by catch
count.

| Guard | Claim | Mechanism | Verdict |
|---|---|---|---|
| Module-scope namespace pin | "binds exactly the approved module-level names, however created" | allowlist over `vars()`, **dunders filtered** | **Claim broader than proof — HIGH-1** |
| `errors.py` namespace pin | three types and nothing else | same filter | same hole; control M-X7-class CAUGHT otherwise |
| Module-scope immutability | "defines only the approved module-level state" | value-kind check over 21 own names | true as stated; prose dichotomy overreaches — **MED-3** |
| Effective class surface | approved public members only, inheritance included | `dir()` + MRO pin + slots | **sound**; M7–M10 all caught |
| Signature pin + discovery anchor | every public callable pinned | 10 dotted paths + independent discovery | **sound**; M12–M14 caught |
| Import-graph guards | no **direct** time/RNG/skill/encounter/combat/magic import; full direct surface stated positively | parsed import set, exact equality | **sound and honestly scoped** |
| Economic-field guard | module reads no catalog economic field directly | AST, forbidden set **derived** from `Item` | sound for its narrow claim; residue disclaimed |
| Reflective-access guard | no approved reflective catalog path, both call shapes | AST `Name`+`Attribute` | **claim correctly narrowed**; M25 is outside it and disclaimed — `LOW-6` |
| `L16` scaling guard | no hour/minute surface, no scaling operator at all | names + all `Mult/Div/FloorDiv/Mod/Pow` | **sound**; strictly stronger than the plan sketch |
| Token denylist | cheap second net, labelled claim C, cited for no case | `__all__` tokens | **honestly labelled** |

Rules-logic controls M16–M24, M26 and the SR-11/silence controls were all **CAUGHT**, which is the
result that matters most: the behavioural suite genuinely protects the card's mechanics.

## 18. Encoding — CLEAN

All eleven live EXP-006 artifacts (two production modules, the test module, the card, plan, gate,
both ledgers, ISSUE-022, INDEX, cluster record): valid UTF-8, **no BOM**, no mojibake byte
sequences, no accidental foreign-script content. Non-ASCII content is legitimate notation only —
`§`, em/en dashes, `′`, `×`, `⅓`, `↔`, `÷`, `↓`, and `✓`/`✗` in the plan's matrix. Review #1's
deliberate mojibake search strings were excluded from the sweep as instructed.

## 19. Canonical verification — all real gates pass

`.venv\Scripts\python.exe scripts\verify.py` — reproduced by me at this HEAD:

```text
Tests:     PASS      1174 passed (whole suite)
Coverage:  PASS      src/rules/ 20 files @ 100% required per file; core aggregate 100.00% (>= 95%)
Ruff:      PASS
mypy:      PASS      52 source files, no issues
Evidence:  PASS      DEC-0012 structural linter (1 reference packet, 0 Stage-A, 12 grandfathered)
Overall:   PASS
```

Five gates — which is all `verify.py` defines. No sixth gate exists and none is claimed in any live
record.

```text
EXP-006 module tests                              111 collected, 111 passed
src/rules/exploration/errors.py                   4/4   stmts 100%   0/0  branch 100%
src/rules/exploration/light_and_exploration_...   131/131 stmts 100%  52/52 branch 100%
```

## 20. All findings by severity

### HIGH

**HIGH-1 — The module-scope namespace guard's stated claim is false: a PEP-562 `__getattr__`
escapes it and serves arbitrary unapproved public attributes, including the two outputs the card
most forbids.**
`tests/rules/exploration/test_light_and_exploration_resources.py`, `_module_scope_names()`
(≈ line 1350): `return {n for n in vars(module) if not (n.startswith("__") and n.endswith("__"))}`.
*Defect:* the dunder filter makes a module-level `def __getattr__(name)` invisible, and that hook is
itself an unbounded dynamic surface requiring no further module-level names.
*Demonstration (scratch copy, 111/111 green):* with a `__getattr__` added,
`light.encounter_distance_from_light(True) == 40` and
`light.VisibilityCategory == ('VERY_GOOD_LIGHT','DIM_LIGHT','NO_LIGHT')` are reachable public module
attributes while `vars(light)` and `__all__` are untouched.
*Why it is a defect and not a limitation:* three separate places state the broader claim — the guard
section header ("bind **exactly** the approved set of module-level names"),
`test_the_module_scope_surface_is_exactly_approved` ("any new module-level name, **however spelled
and however created**, fails here"), and `test_no_module_level_mutable_state_exists` ("defines
**only** the approved module-level state"). `CASE_DISCHARGE` rests ten rows on this mechanism
(`L13`, `L15`, `L29`, `L30`, `L31`, `L36`, `L37a`, `L43`, `L44`, `L45`), two of which (`L31`, `L36`)
the escape actually violates. `errors.py`'s namespace guard has the same hole. This is the project's
named recurring defect mode — an audit mechanism claiming more than it establishes — recurring
inside the guard written to close it.

### MED

**MED-1 — Three live normative records still say EXP-006 is awaiting review #2.**
`docs/rules/INVENTORY.md:106` ("a second independent review is pending");
`docs/rules/clusters/CLUSTER-004-equipment-resources-and-evasion.md:417–423`, under the heading
"**Live next step, as of 2026-10-03:**" ("A SECOND INDEPENDENT FINAL IMPLEMENTATION REVIEW", citing
only review #1); `docs/technical/EXP-006_IMPLEMENTATION_PLAN.md` §18:705 ("pending independent
review #2 PASS") and §1.2:52–55 (review #1 and its 14 findings only). Review #2 occurred, returned
FAIL with 18 findings, and was remediated; a third review is required. `ARCHITECTURE.md` §15.2,
ISSUE-022 and `INDEX.md` state this correctly, so the record set contradicts itself. ISSUE-022 §3
asserts the cluster record's "§13 next step" and the plan's §18 were modified — they were, and were
left stale. Direct recurrence of review-#1 `MED-3` and review-#2 `MED-4`.

**MED-2 — The Pre-Code Gate asserts the withdrawn `L12` wording as a standing finding.**
`docs/technical/EXP-006_PRE_CODE_GATE.md:208`: "`expended → refuelled` (lantern) | **Yes** — §4, a
further flask resets to `24`; **L12 confirms it contributes again**". The card withdrew *"contributes
illumination again"* on 2026-10-01 under explicit human adjudication as "asserting an ignition this
card never establishes". §8a's preamble declares §1–§8 "preserved unaltered" and "Every other
finding above stands and is not re-performed", so this is presented as current, not as labelled
history. Review #2 graded the identical misquote in a test docstring `HIGH-2`; it survives here. Two
sub-defects in the same section: §8a's "§1–§8 are preserved unaltered" is false (§6 carries a
2026-10-03 correction), and §5.C's "`ROLL_1d6_IGNITE_1_2` — this card's own roll" contradicts the
approved plan §11 and the shipped module, which roll nothing.

**MED-3 — The no-second-clock mechanism is narrower than `L13`/`L14`'s discharge rows and than the
guard's own dichotomy claim.**
Demonstrated: a private class attribute `LightSource._rounds_elapsed = 0`, incremented inside
`deplete()`, is a functioning EXP-006-owned elapsed-turn accumulator and leaves 111/111 green. It is
outside the module-scope guard (not a module-level name), outside the public class-surface guard
(`dir()` filtered on `not startswith("_")`), and changes neither slots nor MRO. Card `L14` forbids
exactly this ("any second turn counter, clock or elapsed-time field **owned here**"), yet
`CASE_DISCHARGE["L14"]` cites "module-scope state immutable; slots and MRO pinned" and `["L13"]`
cites "module-scope name set pinned". `test_no_module_level_mutable_state_exists`'s prose also
claims an exhaustive dichotomy ("either a new name… or an approved constant's name") that this third
option falsifies. **No shipped state acts as a clock** — the boundary is intact in fact; the
traceability claim is not.

**MED-4 — ISSUE-022 §3 is factually wrong and contradicts §6 of the same record.**
`docs/completion-records/ISSUE-022-...md` §3 states `errors.py` "(102 lines)" (actual **160**), the
module "(529 lines)" (actual **648**), and the test module "(1418 lines) — **108 tests**" (actual
**1800** lines, **111** tests). §6 of the same record says "**111 tests**". Verified by
`pytest --collect-only` (111) and line count. The `d66db5f` commit changed all five files and
updated §6 but not §3, so the record created to satisfy `DEVELOPMENT_WORKFLOW.md` §5 again
misreports its own §3 and §6.

### LOW

**LOW-1 — The absence of the unapproved fresh-duration ceiling is unguarded.** Adding
`if self.remaining_turns > FRESH_DURATION_TURNS[self.kind]: raise ValueError(...)` to
`LightSource.__post_init__` leaves 111/111 green. ISSUE-022 §2 records "no fresh-duration ceiling"
among the human adjudications made during implementation, so an adjudicated boundary carries no
regression test. The card states no case for it, so this is a missing guard rather than a
conformance defect.

**LOW-2 — `CASE_DISCHARGE["L46"]` names a mechanism that does not discharge the case.** Card `L46`
is "Oil resolved as a thrown missile, or a pursuit-delay value → **ERROR** — RC states no delay
mechanic; none exists to call". The row reads "behavior: the oil binding resolves the GEAR row, not
`Oil, Burning`" — true, but a different property. The property `L46` states is held by the
module-scope namespace pin, the same `surface:` mechanism cited for its sibling `L45`. The
misclassification is plausibly an artefact of the distinct-discharge-string check.

**LOW-3 — `CHAR-005` still carries both SR-11 denials.**
`docs/rules/character_creation/encumbrance_and_movement_rate.md:17` and `:626` both state "**there
is no `SR-11`**". Both are scoped to what the 2026-09-25 amendment did, so a strict reading is
defensible — but these are the exact two occurrences the EXP-006 card cites as its ID-allocation
evidence, and `ARCHITECTURE.md:519` expressly warns that "the card's own ID-allocation reasoning
treats prior textual denials as the evidence distinguishing an allocated `SR` from a free one". A
future `SR-12` allocation would read them. `CHAR-005` is a protected approved Rule Card, so any
correction requires human direction. (Minor: the card says these are "the only **two** textual
occurrences of `SR-11` in the repository" — correct at HEAD.)

**LOW-4 — "The card's responsibilities are implemented in full" is broader than true at card
level.** `src/rules/exploration/light_and_exploration_resources.py:29`. No operation anywhere in
EXP-006 can move a source from `lit=False` to `lit=True`: `ignition_outcome` returns a branch and
never a `LightSource`, and `refuel_lantern` leaves the lantern unlit. The approved plan §11
deliberately excludes applying ignition ("not authorized by this plan in any slice"), so the
*plan's* scope is complete — but the card's §4 speaks of "a separately authorized **ignition**
operation (§5) [that] changes its `lit` state", and the Pre-Code Gate §5.F lists
`ignition attempted → lit` as an established transition. ISSUE-022 §11 does not record it as a
limitation.

**LOW-5 — ISSUE-022 §10 omits the guard-strategy and API-shape departures from the approved plan.**
Plan §13's `G-3` dice-literal AST check and `G-6` (construction-site reachability) are not shipped —
`G-6`'s fallback was pre-authorized in §13 itself, and `G-3`'s replacement (no scaling operator at
all) is stronger; `G-5` ships as an `__all__`-only token check explicitly labelled claim C rather
than the planned `__all__`-plus-namespace check. Plan §7's `__all__` sketch omits the shipped
`FRESH_DURATION_TURNS` (12 names listed, 13 shipped), and §7.1 models `any_mundane_source_lit` /
`max_mundane_radius_feet` as dataclass **fields** where the shipped class makes them computed
properties. Plan §14 Slice C still names the dropped `ExplorationError`, though §10.1 and §11 carry
correction notes. None of this is recorded in §10's five deviations.

**LOW-6 — The `N-R3` note's framing understates the openness of the reflective-catalog boundary.**
The note is accurate as written and I independently replayed it. But it attributes the residual risk
to a future agent authorizing a new import, whereas
`_LIGHT_SOURCE_IDENTITIES[kind].__getstate__()` reaches every catalog field with **no import change
at all** and leaves 111/111 green. `L42` as worded is not breached (no public callable returns an
`Item`), and the project's claim-C disclaimers do cover it. Reported for precision only.

**LOW-7 — `CLUSTER-004` §6 open question 10 restates the inference the card withdrew.**
`docs/rules/clusters/CLUSTER-004-...md:190`: "RC gives the default (*"normal dungeon conditions"* =
`Dim light`)". The card's Finding A withdrew that equation entirely and lists it among items
"recorded so they are not reintroduced"; card §Undefined 2 states RC "supplies **no rule at all**"
connecting carried light to the p. 93 column. §6 belongs to the 2026-09-29 Stage-A body, but the
record has been selectively updated on 2026-10-03 (§3, §10, §13) without a note here, and §6 is
headed "Open questions requiring human decision" rather than labelled historical.

**LOW-8 — The approved card's §Status retains a pre-approval statement that now reads false.**
`docs/rules/exploration/light_and_exploration_resources.md:90–91`: "No Pre-Code Gate has been begun
for `CLUSTER-004`, and no implementation plan exists" — fifty lines after the same §Status block
points at `EXP-006_PRE_CODE_GATE.md`. Scoped to CLUSTER-004, both clauses survive (no cluster-wide
gate or plan exists), and the sentence is in the conditional pre-approval voice — but it is not
labelled historical. The card is protected; remedy requires human direction. Ledger #1 examined the
card's line-36 statement and found it accurate, but did not reach lines 90–91.

## 21. Verdict

The rules logic is conformant, clause by clause against the approved card, and I could not break it:
every behavioural control mutation was caught, every forbidden state is refused or unconstructible,
the eight ignition rows resolve exactly once with `SR-11` confined to its single intersection, the
error taxonomy is real rather than nominal, the ownership and `CHAR-004` boundaries hold, the
53-case reconciliation and category split are correct when re-derived from scratch, encoding is
clean, and all five canonical gates pass with 100% statement and branch coverage per file on both
production modules. The class-surface, MRO, slots and signature guards are sound and survived every
novel probe I devised. This is a third review that found no rules defect — consistent with the first
two.

What prevents acceptance is the same layer that failed twice before, and it has recurred rather than
closed. `HIGH-1` is a demonstrated escape of a guard's own stated claim, through a mechanism neither
prior review tried, that yields exactly the `Visibility` category and light→distance path the card
forbids, and that ten `CASE_DISCHARGE` rows depend on. `MED-1` leaves three live records still
describing the state as awaiting review #2 while three others describe it correctly. `MED-2` has the
Pre-Code Gate asserting, as a standing finding, the `L12` wording the card expressly withdrew — the
defect review #2 graded HIGH, surviving in a different artifact. `MED-4` has the completion record
contradicting itself about its own test count.

```text
EXP-006 FINAL IMPLEMENTATION REVIEW #3: FAIL
```

**1 HIGH, 4 MED, 8 LOW.** No remediation was performed in this pass; the worktree is unmodified at
`d66db5f6`. `LOW-3` and `LOW-8` touch protected approved Rule Cards and cannot be corrected without
explicit human direction.
