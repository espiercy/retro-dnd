# `EXP-006` — Remediation Ledger for Independent Final Implementation Review #2

```text
REVIEW REMEDIATED    docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW_2.md
REVIEW VERDICT       FAIL  -- 2 HIGH, 5 MED, 11 LOW
REVIEWED HEAD        574f1a453464605af2407aafa3a16904cb2f0e16
REMEDIATION DATE     2026-10-03
AUTHORIZED BY        human project owner; remediation only, review #3 NOT in scope
WORKTREE             OD_N_D-cluster-004-exp-006-stage-b
BRANCH               cluster-004-exp-006-stage-b   (unmerged, unpushed)
CERTIFICATION        NONE. The implementer does not and may not certify this.
                     Independent review #3 is required and separately authorized.
```

> **Three artifacts are historical evidence and are preserved unaltered:** final review #1
> (`FAIL`), remediation ledger #1, and final review #2 (`FAIL`). None is rewritten, relabelled or
> softened. This is a **separate** ledger. Where review #2 falsified a closure claim made in
> ledger #1, that falsification is recorded here explicitly (§2) rather than by quietly editing
> the old claim.

---

## 1. Scope discipline — what was *not* reopened

Both independent reviews found the rules logic conformant, clause by clause, across 36 of their own
behavioural and state-space mutations. Accordingly **none** of the following was reopened:

```text
Stage A                              NOT reopened
Rule Card research                   NOT reopened -- no new RC research performed
SR-11                                UNCHANGED -- still exactly one matrix row
The ignition matrix                  UNCHANGED -- 5 resolved rows, 3 absent keys
Depletion arithmetic                 UNCHANGED
Refuel fuel/ignition separation      UNCHANGED
Source durations (6 / 24)            UNCHANGED
Mundane-light semantics              UNCHANGED
The complete-darkness boundary       UNCHANGED -- still unowned, still not filled
The approved Rule Card               NOT MODIFIED (protected; AGENTS.md §12)
```

No merge, no push, no new Stage-A work, and no independent review launched from this task.

The objective was to make **code, tests, governance, documentation and guard claims tell the same
truthful story.** Every change below serves that and nothing else.

---

## 2. Closure claims from ledger #1 that review #2 falsified

Recorded explicitly, as required, instead of being edited away.

| Ledger #1 claimed | Review #2 found | Status now |
|---|---|---|
| **`HIGH-2`:** *"Module docstring now describes the delivered state."* | The docstring said **both** things. Lines 6–7 still read *"This file currently contains **Slice A only**"*, four lines above *"implemented in full"*. The remediation replaced the closing paragraph and never touched the opening one. | **Falsified.** The stale sentence is now deleted outright, and the two further false card quotations review #2 found alongside it are corrected (§3). |
| **`MED-4A`:** *"pinning the exact shape catches them all at once, regardless of spelling, and keeps catching names nobody thought to forbid"* | Six new escapes walked past it: definitions inside `if`/`try`, injection via `globals()`, an inherited mixin member, a forbidden parameter on `LightSource.fresh`, and a module-level `int` counter. | **Falsified.** The guard no longer parses declarations; it reads the imported namespace and the effective class surface (§4–§6). |
| **`MED-4C`:** **15/15 CAUGHT**, reported as closure | The 15 were the eight shapes review #1 had already published, plus controls. Validating a mechanism against the known attack and then reporting it closed *in general* is the project's named defect mode. | **Falsified as a closure claim.** The 15 results were accurate as results; the inference was not. This pass therefore runs **novel** mutations from the same semantic classes (§8). |
| **`MED-4B`:** *"categories recomputed from the actual mechanism"* | Did not hold for `L4`, `L5` (credited a constant for what a behavioural test holds) or `L18` (classed as behavior this module does not produce). | **Falsified for three rows.** The ledger's role is now explicitly traceability, not certification, and every row declares its claim kind (§7). |
| **`LOW-14`:** *"the `ast.Attribute` matcher can no longer be bypassed by reflection"* | `object.__getattribute__(item, "price")` bypassed it; the guard's own forbidden set held a token its `ast.Name` predicate could never match. | **Falsified.** The claim is now stated narrowly and the specific spelling is closed (§9). |
| **`LOW-12`:** *"The '29 of 50' profile line corrected to '26 guards of 53'"* | One of two figures was corrected; *"the 29 guards"* survived four lines later, and the gate's own table still read 50 with `L22` routed. | **Falsified.** The gate no longer publishes a split at all (§10). |

A seventh, from ledger #1's §3: *"every AST guard expected to inspect nodes asserts that it
actually anchored"* — not true of `test_no_catalog_economic_field_is_ever_accessed` (`LOW-3`). Now
true of every one.

---

## 3. HIGH-2 — production documentation describes reality

| Defect | Correction |
|---|---|
| `light_and_exploration_resources.py:6–7` — *"This file currently contains **Slice A only**"*, above a four-slice module | **Deleted.** Not replaced with a different phase claim: the docstring now states the contract and points at `__all__`, with no project chronology. Implementation-history prose does not belong in a production docstring unless it is needed to understand the API. |
| `refuel_lantern` — *"the card's own wording for that case reads **"contributes illumination again"**"* | **Corrected.** That phrase occurs in the card exactly once, at line 44, where the card **withdraws** it. The docstring now says `L12` specifies 24 remaining and `lit = False` *directly*, and notes the withdrawal as history rather than as current wording. |
| `refuel_lantern` — §4 quoted as *"…which **resets** `remaining_turns` to 24."* | **Corrected to the card's actual text:** *"…which **restores** `remaining_turns` to `24` **and leaves the lantern unlit**."* The paraphrase had changed one verb and dropped the adjudicated clause the quotation exists to establish. |
| `LightSource` docstring — *"Slice A has no domain rejection and therefore introduces no exception type of its own"*, in a commit that introduced one | **Rewritten** without the slice framing: construction is structural, so it raises `ValueError`; the card defines no procedure this constructor could fail to supply. |
| `errors.py:24` — *"**The two** types are not interchangeable"*, in a module holding three | **Corrected to three**, each with its distinguishing condition spelled out. |
| The test module repeated the withdrawn-wording claim | **Corrected**, naming `HIGH-2` as the reason. |

**Rule on quoting the card, applied throughout:** quote it accurately, or paraphrase without
quotation marks. Both failures above were paraphrases presented as quotations.

---

## 4. Guard philosophy — three kinds of claim, never conflated

The suite now distinguishes, and labels, three things:

```text
A. machine-proved SURFACE     the module namespace, effective class surfaces,
                              every public signature
B. machine-proved BEHAVIOR    behavioural and invariant tests
C. a REVIEWED ownership boundary, NOT machine proof
```

Labelling a C claim as an A claim is the defect review #2 found. The guard section states this
explicitly, `CASE_DISCHARGE` prefixes every row with its kind, and
`test_every_approved_case_is_accounted_for` asserts the prefix is one of the five known kinds.

**Answering review #2 with a larger lexical denylist was explicitly rejected.** The surviving
token denylist (`test_no_unauthorized_slice_behaviour_is_exposed`) is now **labelled claim C**,
kept only as a cheap second net, and is no longer cited as the sole mechanism for any case.

---

## 5. HIGH-1(a) and MED-1 — the exact runtime module-surface guard

**Replaced** `_public_top_level_definitions()`, which walked `tree.body` and matched five node
types, with `_module_scope_names(module)`, which reads **`vars(module)`** — the namespace the module
actually binds once imported.

Why this is the right instrument rather than a bigger pattern list: the authoritative surface of a
module is what an importer sees. A name created by `if`, `try`, `for`, `while`, `with`, a
comprehension, or `globals()[...] = ...` is, by import time, simply a key in `vars()`. The three
escapes of that class therefore close together, and so do the ones nobody has thought of.

The namespace is pinned as a **partition**, because a single public-only set is what let the
counter through:

```text
APPROVED_DEFINITIONS      13  the public contract, == __all__
APPROVED_IMPORTED_NAMES   12  Enum, Final, Item, Iterable, MappingProxyType,
                              annotations, auto, catalog_item, dataclass, and the
                              three error types this module raises
APPROVED_PRIVATE_NAMES     8  _CATALOG_NAMES, _IGNITION_MATRIX,
                              _LIGHT_SOURCE_IDENTITIES, _TORCH_ITEM,
                              _require_elapsed_turns, and the three now-private
                              identity accessors
                          ---
                           33  == the whole non-dunder namespace
```

**A leading underscore is not an exemption.** Any new module-level name fails until a human
classifies it. That is what closes `MED-1`: review #2's `_TURNS_COUNTED = 0` and `_ROUNDS_SEEN = 0`
are new names, and the sibling `errors.py` namespace is pinned the same way.

`test_no_module_level_mutable_state_exists` adds the state half, scoped to the 21 names EXP-006
itself binds (what an imported `Enum` holds is its own module's business). Every one must be an
immutable kind — constant, read-only mapping, frozen dataclass instance, type or function. The
previous version filtered for `list`/`dict`/`set`, which an `int` counter simply is not; filtering
by **value type** was the wrong instrument and the approved **name set** is the right one.

### The no-second-clock claim, stated exactly

```text
EXP-006 defines only the approved module-level state.
```

From that, plus the pinned public API, plus the behavioural tests that fix each constant's value,
the project may conclude there is no implemented EXP-006 round or time counter: an accumulator
needs either a new name (the surface guard refuses it) or an approved constant's name (the value
tests refuse that). **The suite does not claim to recognize every semantic notion of a "clock"**,
and no longer tries to identify one by vocabulary.

---

## 6. HIGH-1(b) and HIGH-1(c) — class surfaces and every public signature

**Inherited members (`MED`-class escape `probe3`).** `test_public_class_members_are_exactly_approved`
now uses **`dir(cls)`**, not `vars(cls)`, so a member arriving through a base class or mixin is
included. A second, independent barrier was added: `test_approved_classes_have_exactly_the_approved_bases`
pins each class's full MRO — `(X, Enum, object)` for the three enums, `(X, object)` for the two
value types — so even a mixin contributing no new public member fails. Both `__slots__` tuples are
pinned in the same test.

**Every public callable (escape `P-1`).** `APPROVED_PARAMETERS` covered seven module-level
functions, so the classmethod `LightSource.fresh` was unpinned and took `party_surprised` and
`has_infravision` — the two literally forbidden inputs — with the suite green. Replaced by
`APPROVED_CALLABLES`, keyed by dotted path and resolved through descriptors:

```text
deplete, refuel_lantern, mundane_light_contribution, ignition_outcome
LightSource.fresh                                  (classmethod)
LightSource.illumination_radius_feet               (property)
LightSource.__init__                               (dataclass constructor)
MundaneLightContribution.any_mundane_source_lit    (property)
MundaneLightContribution.max_mundane_radius_feet   (property)
MundaneLightContribution.__init__                  (dataclass constructor)
                                                   -- 10 callables
```

**No zero-anchor pass is possible.** `test_every_approved_public_callable_signature_is_pinned`
asserts it inspected all 10, and `test_no_public_callable_escapes_the_signature_guard`
independently **discovers** the public callables from the approved surface and asserts the
discovered set equals the pinned set — so adding a public method and forgetting to list it fails,
which is precisely how `fresh` went unpinned.

---

## 7. MED-2 and §9 — the `L42` economic-field disposition

**Human interpretation applied as given:** `L42` prohibits EXP-006 from creating or exposing
EXP-006-owned economic outputs. Consuming or retaining a canonical `CHAR-004` identity does not
transfer ownership of that object's other fields to EXP-006 — but EXP-006 must not expose a public
API whose purpose is to return catalog economics.

**The accessors were inspected before any code changed, as directed.** Findings:

- No approved mechanic consumes them. The card's own mechanics (§2–§6) never touch an `Item`;
  `deplete`, `mundane_light_contribution`, `refuel_lantern` and `ignition_outcome` take and return
  light-source values and outcomes only.
- **Plan §9 does not require them to be public.** §9.1 mandates *which* identities to reuse and how
  to reach them; §9.2 directs the three catalog strings into one private mapping; §9.3 requires a
  guard that no economic field is read. Nothing in §9, and nothing in the card's §C, requires a
  public accessor. **There is therefore no plan conflict to report**, and the §9 stop condition
  does not apply.

**Disposition: the identity binding is now private** — `_catalog_identity`, `_oil_flask_identity`,
`_tinderbox_identity`, removed from `__all__`, with the reasoning recorded beside it. This was
preferred over defending the public `Item`-returning API, per the stated preference.

The consequence is that `L42` becomes provable **as the card words it**. The new primary mechanism,
`test_no_public_callable_can_emit_a_catalog_row`, establishes that no public callable returns an
`Item` and that `Item` is not re-exported — so no price, `Coin` or encumbrance value is reachable
through this card's public API, by value or by reference. Previously
`catalog_identity(TORCH).price` did in fact reach a `Coin` through it, while the guard established
only that the module never *accessed* such a field — a different property from the one the card
states.

**No economic field was added to EXP-006.** `CATALOG_ECONOMIC_FIELDS` is now **derived** from
`CHAR-004`'s own dataclass — `fields(Item)` minus `{name, category}` — rather than hand-listed
(`LOW-2`), so a new `Item` field extends the guard automatically, and
`test_the_economic_field_set_is_derived_and_non_trivial` anchors it against becoming empty
(`LOW-3`).

---

## 8. Reflective access — the claim, stated narrowly

The project does **not** claim that an AST check proves economic fields are unreachable by every
conceivable Python reflection mechanism. Review #2 defeated that stronger claim. The guarantee is
now exactly:

```text
EXP-006 production code contains no approved reflective catalog-access path
and does not directly read catalog-economic fields.
```

The predicate was extended from `ast.Name`-only to **both call shapes** — a bare name and a dotted
attribute — which closes `object.__getattribute__(item, "price")`, and the forbidden set grew to
include `globals`, `locals`, `compile`, `__dict__`, `__class__`, `__reduce__` and `_asdict`. It also
now flags an *attribute reference* to a reflection entry point, not only a call of one, and asserts
non-vacuity over `ast.Call` nodes.

**No miniature static analyzer was built.** The remainder of the boundary is a **reviewed** one, is
labelled claim C in the guard docstring, and an independent reviewer must still inspect it.

---

## 9. Stale arithmetic — recomputed, not substituted

**Every live case-count statement was re-derived**, not pattern-replaced. The card's IDs were
re-enumerated independently (53), the category counts recomputed from the current rows, and each
artifact made internally consistent.

| Artifact | Was | Now |
|---|---|---|
| Plan §12 blockquote | *"unit behavior 19, ownership guard 19, internal invariant guard 12, routed dependency 3"* (53) | **Labelled historical and withdrawn.** |
| Plan §12 prose | *"re-derived … they match: **18 / 18 / 11 / 3**"* (50) | **Withdrawn.** It matched neither the table nor the card; a "re-derived and they match" assertion that matched nothing was the defect. |
| Plan §12 table | 18 / 18 / 12 / 3 (51), **omitting `L19a` and `L19b`** | **Replaced** by the computed split, all 53 cases listed by ID. |
| Gate §6 table | 18 / 18 / 11 / 3 (50), `L22` routed | **Withdrawn. The gate no longer publishes a split** — a pre-implementation gate record is the wrong home for a figure that later changed four times. |
| Gate §6 profile | *"26 guards of 53"* on one line, *"the 29 guards"* four lines later | Both replaced by one consistent statement. |

**The authoritative split is computed, not transcribed.** Its single source is `CASE_DISCHARGE`,
and `test_the_case_category_counts_are_recomputed_not_carried_over` asserts these exact numbers, so
the published table cannot drift from the code without a red test:

```text
behavior   23   machine-proved behavior          (claim B)
invariant   5   machine-proved refusal           (claim B)
surface    23   machine-proved surface           (claim A)
reviewed    1   reviewed ownership boundary      (claim C)  -- L37
routed      1   not owned by this card           -- L47
           ---
            53
```

Historical figures remain only where explicitly labelled historical.

---

## 10. `CASE_DISCHARGE` — role changed to traceability

It answers *"where is this case discharged?"* It does **not** answer *"have we formally proved no
future implementation could violate it?"* That is stated at the top of the section.

Every row cites an actual mechanism and declares its kind. Rows corrected because they cited a
guard for a property that guard does not establish:

| Case | Was | Now |
|---|---|---|
| `L4` | *"one radius constant, so the radii cannot differ"* | `behavior:` — the parametrized radius test, which is what actually holds it (`LOW-6`) |
| `L5` | *"public member surface pinned"* | `behavior:` — no brighter/dimmer figure is produced (`LOW-6`) |
| `L13`, `L14`, `L19b` | *"no module-level mutable exists"* | `surface:` — the module-scope **name set**, which an `int` cannot evade (`MED-1`) |
| `L18` | `behavior:` *"its OWN row re-selects"* | `behavior:` — now says the roll is **not ours to make**; the module never rolls (`LOW-7`) |
| `L42` | *"AST attribute walk + reflective access prohibited"* | `surface:` — no public callable returns an `Item`, so nothing is emitted (`MED-2`) |
| `L16` | *"no int mult/floordiv"* | `surface:` — no hour/minute name anywhere, and **no scaling operator at all** (`LOW-5`) |
| `L37` | `routed:` | `reviewed:` — claim C, explicitly not machine proof |

---

## 11. The current error taxonomy, agreed across every normative location

```text
IgnitionNotDefinedError        RC supplies no ignition procedure
LanternRefuelNotDefinedError   RC supplies no partial-refill procedure
IgnitionAttemptLimitError      RC explicitly prohibits another attempt this round
ValueError                     malformed structural input

No base class.
```

**Implemented semantics were not changed** — they already agreed with this. What changed is the
documentation that disagreed with them (`MED-3`):

- Plan **§10.1**'s recommendation of `ExplorationError` plus one subclass, and its *"One base plus
  one subclass"* assertion, are marked superseded and the shipped taxonomy stated in full.
- Plan **§10.2**'s row for `L19` read **`ValueError` — "a caller-protocol violation, not a rules
  gap"**. Corrected to `IgnitionAttemptLimitError`: RC's once-per-round rule is what rejects it, so
  the rejection is a rules rejection.
- Plan **§10.2** gained the missing `L12a` row for `LanternRefuelNotDefinedError`.
- Plan **§11** and **§16** row 10 were corrected in the previous pass and remain correct.
- `errors.py`'s module docstring now enumerates three types, not two (`LOW-8`).

`LOW-9` is **recorded, not actioned**: `LanternRefuelNotDefinedError` covers both a wrong-kind
request and a genuine partial-refill silence, distinguishable only by message. The card specifies
neither case's representation, so splitting the type would be an implementation-level rules
decision this task is not authorized to make. Noted as a limitation for human adjudication.

---

## 12. All eleven LOW findings

| # | Correction | Verification proving closure |
|---|---|---|
| **LOW-1** | `ISSUE-022` claimed a **`policy`** verification gate. `verify.py` defines five gates and no such gate. | §8 of the rewritten record reports exactly the five real gates and states explicitly that no `policy` gate exists. No invented gate appears anywhere. |
| **LOW-2** | `CATALOG_ECONOMIC_FIELDS` was a hand-maintained eight-name denylist. | **Derived** from `dataclasses.fields(Item)` minus the two identity fields, so a new `CHAR-004` field extends the guard automatically — the rank-1 shape mechanism over a maintained list. |
| **LOW-3** | The economic-field guard had no non-vacuity anchor, though it was `L42`'s sole mechanism. | Two anchors: `test_the_economic_field_set_is_derived_and_non_trivial` proves the forbidden set is non-empty and contains `price`/`encumbrance_cn`; the guard itself asserts it saw at least one `ast.Attribute` node. |
| **LOW-4** | `test_the_derived_figures_cannot_disagree_with_the_sources` was `assert not hasattr(...) or ...` — a disjunction that passes if the structure disappears. | Rewritten to assert the dataclass exists first, then its fields, then that both derived figures are genuinely `property` objects. |
| **LOW-5** | The `L16` arithmetic guard required an int **Constant**, so `value * TORCH_TURNS` escaped. | Multiplication, division, floor-division, modulo and power are now forbidden **outright**, in both `BinOp` and `AugAssign` form. RC states both durations in turns and depletion is subtraction, so no scaling operator has any legitimate use here — forbidding the operators beats guessing their spellings. |
| **LOW-6** | `CASE_DISCHARGE["L4"]`/`["L5"]` mis-cited their mechanisms. | Both reclassified to `behavior:` citing the parametrized radius test and the no-quality-distinction test — the mechanisms that actually hold them. |
| **LOW-7** | `CASE_DISCHARGE["L18"]` was classed as behavior this module does not produce. | Row now states the module re-selects its own branch and that **the roll is not ours to make**, matching what the test honestly establishes. |
| **LOW-8** | `errors.py` said *"The two types"* in a three-type module. | Docstring enumerates all three with their distinguishing conditions. |
| **LOW-9** | One error type covers a wrong-kind request and a genuine card silence. | **Recorded as a limitation, not actioned** — the card specifies neither representation, so splitting it would be an unauthorized rules decision. Noted in `ISSUE-022` §11 and §11 above for human adjudication. |
| **LOW-10** | `SR-11`'s registry omitted `ARCHITECTURE.md` §15.2, which review-#1's own `HIGH-1` fix added. | Cluster record §10 now lists **five** locations with a dated note; `ISSUE-022` §12 says five and enumerates them. |
| **LOW-11** | `INVENTORY.md` cited *"Ch. 5 pp. 81–86 (`Fire-Building`, **`Blind Shooting`**)"*; the approved card's RC-source table has no such entry — it carries `Lip Reading`, p. 84. | Corrected **against the approved card**, with **no new RC research**: the cell now cites `Fire-Building` p. 83, the skill-check procedure and `Sample Skills Table` pp. 82/86, and `Lip Reading` p. 84, and records what it previously said. |

---

## 13. Self-falsification — known escapes confirmed, then novel variants

Run on a **scratch copy**; the real worktree was never mutated. Baseline `PASS`, then:

### 13.1 Review #2's six published escapes — all now caught

| Mutation | Guard / property expected to catch it | Result |
|---|---|---|
| `LightSource.fresh(..., party_surprised, has_infravision)` | every public callable signature pinned | **CAUGHT** |
| `MundaneLightContribution(_AmbientMixin)` adding `ambient_state`, `encounter_range_feet` | effective class surface via `dir()`; MRO pinned | **CAUGHT** |
| public `VisibilityCategory` inside `if True:`, omitted from `__all__` | module-scope namespace | **CAUGHT** |
| public `encounter_distance_from_light()` inside `try:` | module-scope namespace | **CAUGHT** |
| `no_light_state` injected via `globals()` from a top-level `for` | module-scope namespace; reflective-access guard | **CAUGHT** |
| `object.__getattribute__(item, "price")` | reflective access, both call shapes | **CAUGHT** |

Plus review #2's two `MED-1` counters (`_TURNS_COUNTED`, `_ROUNDS_SEEN`): both **CAUGHT**.

### 13.2 Novel variants — same semantic classes, different shapes

Devised for this pass, **not replayed** from either review. `31/31 CAUGHT`.

| Mutation | Guard / property expected to catch it | Result |
|---|---|---|
| `N-W1` public `DarknessLevel` inside a top-level `while` | module-scope namespace | **CAUGHT** |
| `N-W2` public `party_light_state()` inside a `with` block | module-scope namespace | **CAUGHT** |
| `N-W3` public names bound by **tuple unpacking** | module-scope namespace | **CAUGHT** |
| `N-W4` public name bound by a **for-loop target** | module-scope namespace | **CAUGHT** |
| `N-W5` public alias created by a **walrus** in an `if` test | module-scope namespace | **CAUGHT** |
| `N-I1` inherited public **method** on `LightSource` | effective class surface; MRO | **CAUGHT** |
| `N-I2` intermediate base contributing **no** new member | MRO pinned | **CAUGHT** |
| `N-I3` inherited public **classmethod** on the aggregate | effective class surface | **CAUGHT** |
| `N-S1` forbidden param on the property `illumination_radius_feet` | all signatures pinned | **CAUGHT** |
| `N-S2` new field, so the dataclass constructor takes `party_surprised` | constructor pinned | **CAUGHT** |
| `N-S3` forbidden param on `max_mundane_radius_feet` | all signatures pinned | **CAUGHT** |
| `N-S4` **renaming** a pinned parameter | all signatures pinned | **CAUGHT** |
| `N-C1` innocuous `_cache = 0` accumulator, no time vocabulary at all | module-scope name set | **CAUGHT** |
| `N-C2` mutable `list` under an approved-**looking** private name | module-scope state immutability | **CAUGHT** |
| `N-C3` approved private name rebound from `mappingproxy` to a plain `dict` | module-scope state immutability | **CAUGHT** |
| `N-C4` **function-attribute** counter `ignition_outcome.calls = 0` | selector holds no attribute state | **CAUGHT** |
| `N-R1` `item.__getattribute__("price")` — instance-method spelling | reflective access, both shapes | **CAUGHT** |
| `N-R2` `vars(item)["price"]` | reflective access | **CAUGHT** |
| `N-R3` `dataclasses.astuple(item)` — **outside the stated claim** | *see note below* | **CAUGHT, incidentally** |
| `N-E1` re-export the identity accessor publicly | no public callable returns an `Item` | **CAUGHT** |
| `N-E2` read `.made_for_race` — a field the old hand-list happened to hold | **derived** economic field set | **CAUGHT** |
| `N-A1` `value * TORCH_TURNS` — constant on the right, not a literal | no scaling operator at all | **CAUGHT** |
| `N-A2` `value % 10` | no scaling operator at all | **CAUGHT** |
| `N-A3` hours-denominated **private** module name `_TORCH_HOURS` | no hour/minute name anywhere | **CAUGHT** |
| `N-X1` CONTROL per-kind radius split (review #2's own `LOW-6` demo) | behavioural radius tests | **CAUGHT** |
| `N-X2` CONTROL `SR-11` row flipped to the `1d6` | matrix behavioural tests | **CAUGHT** |
| `N-X3` CONTROL an RC silence filled with a default | refusal invariants | **CAUGHT** |
| `N-X4` CONTROL refuelling ignites | refuel behavioural tests | **CAUGHT** |
| `N-X5` CONTROL partial refuel reverts to `ValueError` | error-taxonomy tests | **CAUGHT** |
| `N-X6` CONTROL aggregate silently filters invalid members again | aggregate rejection tests | **CAUGHT** |
| `N-X7` CONTROL a fourth error type in `errors.py` | errors module scope pinned | **CAUGHT** |

> **`N-R3` — reported honestly rather than claimed.** `dataclasses.astuple(item)` reaches every
> field of a catalog row and is **not** in the reflective-access forbidden set, so it falls
> **outside** that guard's stated claim. It was nonetheless caught — but by a *different*
> mechanism: `import dataclasses` binds a new module-level name, which the module-scope namespace
> guard refuses. That is a real result and a useful one, but it is **not** evidence that the
> reflective-access guard covers `astuple`, and the claim is not widened to say so. A future agent
> who adds `dataclasses` to `APPROVED_IMPORTED_NAMES` for an unrelated reason would reopen this
> path. The honest position stands: **the reflective-catalog boundary is partly a reviewed one
> (claim C), and an independent reviewer must still inspect it.**

**Total: 39 mutations, 39 caught** — 8 known escapes, 24 novel variants, 7 rules-logic controls.
The purpose was not to prove Python cannot be evaded; it was to test whether the guards' **narrow
stated claims** hold beyond the exact examples they were written against. On this evidence they
do, with the one documented caveat above.

---

## 14. Verification

```text
uv run python scripts/verify.py

Tests:     PASS
Coverage:  PASS      100% statement AND branch, per file, on both production modules
Ruff:      PASS
mypy:      PASS      strict
Evidence:  PASS      DEC-0012 structural linter
Overall:   PASS
```

Five gates, which is all `verify.py` defines. No other gate is claimed.

**Test count: 108** in the `EXP-006` module (was 101 at the reviewed `HEAD`); whole suite green.

**Per-file coverage**, read from `coverage.json`:

```text
src/rules/exploration/errors.py                            4/4   stmts 100%,  0/0  branch 100%
src/rules/exploration/light_and_exploration_resources.py 131/131 stmts 100%, 52/52 branch 100%
```

**Independent case reconciliation**, enumerated from the Rule Card's own tables: 53 in the card,
53 in `CASE_DISCHARGE`, no drift either way, 53 distinct discharge strings, every row declaring its
claim kind, and the published split asserted by a test rather than transcribed.

**Encoding:** all nine changed files are valid UTF-8 with no BOM, no mojibake and no unexpected
script. Two pre-existing characters were flagged by the sweep and inspected — `↔` in the cluster
record's cross-interaction table, `÷` and `↓` in `INVENTORY.md` rows — and confirmed to be
legitimate notation absent from every line this remediation added. `§`, em-dashes, `′`, `×` and
`⅓` are likewise legitimate typography, not defects.

**Stale-figure scan** over the live artifacts for `47`, `50`, `51`, `53`, `18 / 18 / 11 / 3`,
`19 / 19 / 12 / 3` and `29 guards`: six hits, each inspected in context and each correct — they are
the gate's explicitly-withdrawn-figure note, this ledger's own falsification table quoting what was
wrong, and an unrelated `CHAR-004` inventory row. **No figure was replaced without re-deriving
it.**

---

## 15. What this ledger does **not** do

```text
IT DOES NOT CERTIFY COMPLETION.           The implementer may not.
IT DOES NOT RELABEL REVIEW #1 OR #2.      Both FAIL verdicts stand, unaltered.
IT DOES NOT RELABEL LEDGER #1.            Preserved; its falsified claims are
                                          recorded in §2, not edited away.
IT DOES NOT AUTHORIZE A MERGE OR PUSH.
IT DOES NOT AUTHORIZE CLUSTER-004 IMPLEMENTATION, ENC-005 STAGE B,
   OR ANY NEW STAGE-A CARD.
IT DID NOT LAUNCH REVIEW #3.              Out of scope for this task.

NEXT REQUIRED STEP:  a third INDEPENDENT final implementation review,
   separately authorized, inspecting the whole implementation rather than
   these 18 fixes, treating this ledger as a CLAIM rather than as evidence,
   and performing no remediation in its own pass.
```
