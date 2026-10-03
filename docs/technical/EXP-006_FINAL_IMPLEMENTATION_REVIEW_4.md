# `EXP-006` INDEPENDENT FINAL IMPLEMENTATION REVIEW #4

> **Preserved verbatim as received.** Fourth independent final implementation review, performed
> against `HEAD` `a150837` by a reviewer that wrote none of the code, tests, Rule Cards, plan, gate,
> ledgers or records, and that was forbidden to change anything. Historical evidence on the same
> terms as reviews #1–#3: **not** to be rewritten, relabelled or softened.
>
> Recorded in the repository 2026-10-03 because the review was returned as a task result rather
> than written into the tree. Content unaltered; only the transport's HTML entity escaping of `>`
> and `<` has been undone.
>
> **Verdict: `FAIL` — 6 BLOCKING, 7 non-blocking limitations/informational.** **No rules-conformance
> defect, for the fourth consecutive review**, and for the first time **no guard overclaiming**.
> Every blocking finding is a stale cross-reference in a governance record, or the consistency
> mechanism built to prevent exactly that.

## 1. Reviewed HEAD

```text
WORKTREE     C:/Users/evanp/source/repos/OD_N_D-cluster-004-exp-006-stage-b
BRANCH       cluster-004-exp-006-stage-b          (as briefed)
HEAD         a15083790d5c8f81865d391c7c24e736609714cf   (as briefed)
MAIN         c1bdd5c01e998f961b3851c3d95a225b37fa9cc7
ORIGIN/MAIN  c3a3e2d9d961a1df8ec3ccad3823929b0a41cac0
STATUS       clean (no tracked or untracked modifications)
```

No worktree collision. HEAD is `a150837` ("docs(rules): LOW-3/LOW-8 — mark two protected-card
statements historical"), which touched exactly two files: `encumbrance_and_movement_rate.md` (+3)
and `light_and_exploration_resources.md` (+20/−2).

## 2. Independence statement

I wrote none of this code, tests, Rule Cards, plan, gate, ledgers or records. I remediated nothing —
no production file, test, document, gate or configuration in the real worktree was modified;
`git status` was clean at start and end. All mutation testing ran on a scratch copy at
`C:\Users\evanp\AppData\Local\Temp\claude\exp006-rev4`. No Rules Cyclopedia page was fetched and
Stage A was not reopened; the approved Rule Card was my sole rules authority. I re-derived the
53-case set, the ignition matrix, the claim-kind split and every mechanical assertion myself before
reading any prior review or ledger conclusion. All three prior review artifacts and three
remediation ledgers were treated as claims to verify.

## 3. Artifacts reviewed

Approved card `docs/rules/exploration/light_and_exploration_resources.md` (in full, all correction
notes); `src/rules/exploration/light_and_exploration_resources.py`;
`src/rules/exploration/errors.py`; `tests/rules/exploration/test_light_and_exploration_resources.py`
(all 1940 lines); `tests/rules/exploration/test_exp_006_record_consistency.py`;
`docs/technical/EXP-006_IMPLEMENTATION_PLAN.md`; `docs/technical/EXP-006_PRE_CODE_GATE.md` (incl.
§6, §8a); `docs/rules/clusters/CLUSTER-004-equipment-resources-and-evasion.md`;
`docs/rules/INVENTORY.md`; `docs/rules/character_creation/encumbrance_and_movement_rate.md`;
`EXP-006_FINAL_IMPLEMENTATION_REVIEW{,_2,_3}.md`; `EXP-006_REVIEW{,_2,_3}_REMEDIATION_LEDGER.md`;
`docs/completion-records/ISSUE-022-...md` and `INDEX.md`; `ARCHITECTURE.md` §15.1/§15.2;
`DEVELOPMENT_WORKFLOW.md` §5/§5.1; `AGENTS.md`; `GAME_CONSTITUTION.md` §5; `pyproject.toml`;
`scripts/verify.py` output; `git log`/`git blame` for the `LOW-9`, review-#3 and `LOW-3`/`LOW-8`
commits.

## 4. Rules conformance — CLEAN

Re-derived from the card and executed directly against the shipped module. Every item verified:

| Requirement | Card | Observed |
|---|---|---|
| Torch radius | §2 `30'` | `30` |
| Lantern radius | §2 `30'` | `30` (same constant; no per-kind value exists) |
| Torch duration | §3 `6` turns | `6` |
| Lantern duration | §3 `24` turns/flask | `24` |
| Unlit source retains fuel | `L11` | unlit torch → `remaining_turns == 6`, radius `None` |
| Exhausted source cannot be lit | §4/Finding C | `ValueError`: *"an exhausted source is never lit"* — **unconstructible** |
| Exhausted/unlit contributes nothing | `L9`, `L15a` | radius `None`; excluded from `lit_sources` |

Depletion: caller supplies `elapsed_turns` (no time import, no counter); `True` rejected (`bool`
excluded before `int`); `-1` rejected; `1.0` rejected; `0` accepted and state-preserving
(`spent == source`); only lit sources deplete; floors at zero (`9` vs `6` → `0`); reaching zero sets
`lit=False` on **that source only**; `deplete` returns `tuple[LightSource, ...]` and nothing else —
no world-darkness value, no `NO_LIGHT`, no `Visibility`, no burn-out event, no proration. No
fresh-duration ceiling: a 600-turn torch constructs, illuminates, and depletes to `594` normally.

Refuel — contract matches exactly:

- non-lantern → `ValueError` (*"refuel_lantern is a lantern operation"*)
- valid lantern, `remaining_turns > 0` → `LanternRefuelNotDefinedError` (lit **or** unlit)
- exhausted lantern → `remaining_turns = 24`, `lit = False`
- non-`LightSource` → `ValueError`

**No invented partial-refill arithmetic exists.** There is no top-up, no additive `+24`, no
proration anywhere in `refuel_lantern`; the only arithmetic in the whole module is
`max(0, remaining - spent)`, and the suite forbids every multiplication/division/modulo/power
operator at AST level.

Contribution: `lit_sources`, `any_mundane_source_lit`, `max_mundane_radius_feet` (`None`, never
`0`). The two derived figures are computed properties, not fields. Malformed members **reject**
rather than disappear — `"torch"`, `None`, `42`, `{"lit": True}` and a duck-typed impostor all raise
`ValueError`, in both `mundane_light_contribution` and `deplete`. A valid unlit source is accepted
and simply does not contribute. Direct construction with an unlit member is refused.

Ignition — all eight re-derived independently and executed:

```text
skill  tinderbox  conditions   observed                 card
T      T          ORDINARY     AUTOMATIC                RC Explicit      ✓
T      T          ADVERSE      ROUTED_SKILL_CHECK       RC Explicit      ✓
T      F          ORDINARY     ROLL_1D6_IGNITE_1_2      RC Explicit      ✓
T      F          ADVERSE      ROUTED_SKILL_CHECK       SR-11            ✓
F      T          ORDINARY     ROLL_1D6_IGNITE_1_2      RC Explicit      ✓
F      T          ADVERSE      IgnitionNotDefinedError  RC silence       ✓
F      F          ORDINARY     IgnitionNotDefinedError  RC silence       ✓
F      F          ADVERSE      IgnitionNotDefinedError  RC silence       ✓
```

`skill=True, tinderbox=False, ADVERSE → ROUTED_SKILL_CHECK` under `SR-11` confirmed, and the sibling
`ORDINARY` row still gives the `1d6`, so the ruling bites exactly one intersection. Implemented as a
`MappingProxyType` of 5 keys — no overlap is representable, no row-order precedence exists, and the
three silences are refused by **absence** with no default to reach. No RNG import (direct), no RNG
object constructed, no `CHAR-012` execution, no `1d20`, no ability score, no penalty arithmetic. The
same-round guard runs **before** the matrix: `(False, False, ADVERSE, flag=True)` raises
`IgnitionAttemptLimitError`, not a silence.

## 5. Error taxonomy and `LOW-9` — CLEAN, and the distinction is non-vacuous

Four categories behave exactly as documented. The `LOW-9` distinction is **real**: I verified
directly that all three domain types have MRO `(Type, Exception, BaseException, object)` and
`issubclass(T, ValueError) is False` for each. That is what makes the negative assertions
(`not isinstance(caught.value, LanternRefuelNotDefinedError)`,
`not isinstance(caught.value, ValueError)`) meaningful rather than circular, and a caller filtering
`ValueError` provably cannot absorb a source silence. Mutating `LanternRefuelNotDefinedError` to
subclass `ValueError` in scratch was caught by two tests.

## 6. `SR-11` — CLEAN

Registered in all five claimed locations (card §Simulator Ruling ×16, `CLUSTER-004` §10 and §3,
`INVENTORY.md`, plan §11, `ARCHITECTURE.md` §15.2). The earlier §15.2 denial is corrected and the
correction is recorded. Historically unambiguous after `LOW-3`: `CHAR-005` contains exactly two
"there is no `SR-11`" denials (§Status and Amendment History), and **each is immediately followed**
by a 2026-10-03 disambiguation stating it describes only the 2026-09-25 amendment state, that
`SR-11` was later allocated to `EXP-006`, and that no mechanic, provenance classification or
approval status changes. Applies to one matrix row only; flipping it was caught by three tests; no
other row differs from the card.

## 7. Ownership boundaries — CLEAN

The **direct** import graph is pinned and complete: `__future__`, `collections.abc`, `dataclasses`,
`enum`, `types`, `typing`, `rules.character_creation.equipment`, `rules.exploration.errors`. Adding
`rng` was caught by four tests.

`EXP-006` does not own or resolve: dungeon-time advancement or round tracking (no time import, no
counter, no bound mutable state, no attribute state on any function object); complete darkness;
global illumination; encounter `Visibility`; encounter distance; surprise (not a parameter
anywhere); blindness; darkness combat penalties; infravision; `CHAR-012` resolution; RNG execution;
magical light/darkness (enum closed at `TORCH`/`LANTERN`); rations; starvation; torch-as-weapon or
oil-as-missile.

**Direct vs transitive, measured:** importing the module transitively loads `rng`,
`rng.{errors,expressions,results,rng}`, `rules.currency`,
`rules.character_creation.{equipment,errors,character_class}` — all forced by the `CHAR-004` seam
the approved plan §1.1 directs this card to use. No RNG object is constructed, no RNG method called,
no `Coin` read. The suite states the accurate guarantee ("no RNG is **consumed**", not "nothing of
the kind is reachable") and explicitly disclaims the transitive reading. That is correct and
appropriately scoped.

## 8. `CHAR-004` seam — CLEAN

Torch, Lantern, Oil and Tinder box are consumed as canonical identities only. Catalog strings live
in exactly one private `MappingProxyType` (`_CATALOG_NAMES`), AST-verified with no stray literal
elsewhere; the torch uses `CHAR-004`'s own exported `TORCH` (identity, verified by `is`). `"Oil"` is
the Adventuring-Gear row and is **not** `"Oil, Burning"`. The three accessors are private and absent
from `__all__`; no public callable returns an `Item` and `Item` is not re-exported — I confirmed by
mutation that making one accessor public fails six tests. No economic field is read by attribute or
subscript (forbidden set derived from `CHAR-004`'s own `dataclasses.fields(Item)`, with a
non-vacuity anchor); `.price` and a subscript read were each caught. No price, `Coin`, encumbrance or
legality fact is restated; no currency machinery is imported.

## 9. Guard-claim audit — the mechanisms establish their stated claims

I judged each guard against **its own stated claim**, then attacked that claim with 38 novel scratch
mutations. **37 were caught.**

| Guard | Stated claim | Mechanism | Verdict |
|---|---|---|---|
| `test_the_module_scope_surface_is_exactly_approved` | "At normal module initialization, EXP-006's concrete bound namespace matches the approved namespace" | `vars(light)` vs 3-way partitioned allowlist | **Establishes it.** Caught new names via plain assign, `if True:`, `try:`, and `globals()[...] = ...` from a top-level `for`. Explicitly disclaims `__getattr__`; I confirmed no `__getattr__` is bound. Claim is narrower than reality — correct, not a defect. |
| `test_the_errors_module_scope_surface_is_exactly_approved` | three concrete types, nothing else bound | same | **Establishes it.** A 4th error type was caught. |
| `test_no_module_level_mutable_state_exists` | "of the names EXP-006 concretely binds at module scope, none holds mutable state" | value-kind pin + count anchors | **Establishes exactly that.** Caught a `dict` on an approved name and a new `int` accumulator. The withdrawn broader dichotomy is quoted as withdrawn; `L13`/`L14`/`L19b` are reclassified `reviewed:` accordingly. |
| `test_public_class_members_are_exactly_approved` | approved **effective** surface via `dir()`, inherited members included | `dir()` vs allowlist | **Establishes it.** A private-mixin `ambient_state` was caught; so was a new public method. |
| `test_approved_classes_have_exactly_the_approved_bases` | exact MRO, both value types slotted | `__mro__` + `__slots__` | **Establishes it.** Mixin caught independently. |
| `test_every_approved_public_callable_signature_is_pinned` | every approved public callable has exactly the approved parameters | 10 dotted paths through descriptors | **Establishes it.** `party_surprised` on `fresh` and an `elapsed_hours` parameter were both caught. |
| `test_no_public_callable_escapes_the_signature_guard` | the pin is not vacuous | discovery vs pinned set | **Establishes it.** |
| `test_no_public_callable_can_emit_a_catalog_row` | no public callable returns `Item`; `Item` not re-exported | return annotations + identity, `checked == 4` | **Establishes it.** |
| `test_no_catalog_economic_field_is_ever_read_directly` | "no approved reflective path and no direct economic-field read" | AST attribute/subscript, derived field set | **Establishes exactly that**, and says so; discloses the `__getstate__` residue honestly. |
| `test_this_module_uses_no_reflective_attribute_access` | no ordinary reflection mechanism is used, both call shapes | AST name + attribute | **Establishes it.** `getattr(...)` and `object.__getattribute__(...)` both caught. |
| `test_this_module_performs_no_hour_to_turn_conversion` | no hours/minutes-denominated surface + no scaling operator at all | AST `BinOp`/`AugAssign` + name/param scan | **Establishes it.** `spent * 1` caught. |
| `test_the_complete_production_dependency_surface` | the **direct** import graph, positively; explicitly not transitive | AST | **Establishes it.** |
| `test_no_unauthorized_slice_behaviour_is_exposed` | self-labelled claim C, "a cheap second net" | `__all__` token denylist | **Honestly labelled**; not cited as the sole mechanism for any case. |

This area is genuinely clean. I found **no guard claiming more than its mechanism delivers**, with
one minor exception recorded as NB-4 below.

## 10. No-second-clock — CLEAN

The **shipped** implementation owns no mutable round or time state. Verified independently of the
guards: the module namespace binds 33 names, all constants, read-only mappings, a frozen `Item`,
types or functions; `vars(LightSource)` and `vars(MundaneLightContribution)` contain only slot
descriptors, dunders, `__post_init__`, one classmethod and the properties — no counter; all four
public function objects carry no attribute state; `turn_credit` and `dungeon_turn_time_accounting`
are unimported; `attempt_already_made_this_round` is never mutated and nothing is recorded across
calls (three identical calls return identically). `EXP-002` remains the sole time authority. No
defect. I did not require the tests to recognise every theoretical clock representation.

## 11. Independent 53-case reconciliation and split

I enumerated the card's case IDs myself from row anchors: **53 distinct IDs** (5 illumination + 14
duration/depletion + 12 ignition + 10 mundane-light state + 6 routed consequences + 6 seam guards).
No `L`-token appears anywhere in the card outside a table row, so there are no orphan references.
`CASE_DISCHARGE` maps exactly those 53, with no duplicate discharge strings and every row declaring
a valid claim kind.

**My independently derived split, from the shipped ledger:**

```text
behavior   22   L1 L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L15a L17 L18 L19a L20 L21 L22 L27 L28 L34
invariant   5   L12a L19 L23 L24 L26
surface    11   L15b L16 L25 L32 L33 L35 L38 L39 L40 L41 L42
reviewed   14   L13 L14 L15 L19b L29 L30 L31 L36 L37 L37a L43 L44 L45 L46
routed      1   L47
total      53
```

This matches the assertion in `test_the_case_category_counts_are_recomputed_not_carried_over` and
ledger #3's published table. I checked each row's classification against behaviour: the
`behavior`/`invariant` rows are genuinely machine-held (every one I mutated failed loudly); the
`surface` rows each rest on a mechanism a dynamic hook cannot fake (parsed import graph, pinned
signature, pinned effective class surface, or an AST property) — I accepted these; the 14 `reviewed`
rows are honestly labelled as not machine proof and I did not demand proof for them; `L47` is
correctly routed.

**However, the governance artifact that publishes this split does not match it** — see BLOCKING-1.

## 12. Protected-card clarifications — both CLEAN

**`LOW-3`.** `CHAR-005`'s two "there is no `SR-11`" denials each now carry an adjacent 2026-10-03
note stating (a) the denial describes only the 2026-09-25 amendment state, (b) `SR-11` was
subsequently allocated to `EXP-006` on 2026-10-01, (c) it is "**not** a current claim that no
`SR-11` exists", and (d) `SR-8`–`SR-10`, the card's mechanics, provenance and `APPROVED` status are
unaffected. The Amendment History note additionally explains *why* this matters (the `SR` allocation
procedure reads prior textual denials as evidence a number is free). Requirement met.

**`LOW-8`.** The `EXP-006` card's pre-approval sentence is now inside a block headed "**Historical
pre-approval note — retained for chronology, NOT current status.**", quoted rather than rewritten,
followed by an explicit statement that an `EXP-006`-specific Pre-Code Gate (`PASS` 2026-10-01) and
implementation plan (`APPROVED` 2026-10-01) both now exist and that §15.2 step 4 was given for this
card's plan only, with a pointer to `ISSUE-022`. It states "**No mechanic, evidence, provenance
classification, `SR-11`, case ID or approval status is changed by this marking.**" Requirement met;
no contradiction with the gate or plan remains in the card.

## 13. Consistency mechanism — one property is demonstrably unprotected

`test_exp_006_record_consistency.py` claims two properties plus a stale-wording check. I mutated
each in scratch:

| Claimed property | Mutation | Result |
|---|---|---|
| Phase token present in all 5 named live records | removed `CURRENT_PHASE` from `ARCHITECTURE.md` | **CAUGHT** |
| Card case total is 53 | — (recomputed from the card; agrees) | holds |
| Ledger total matches the card | removed a `CASE_DISCHARGE` row | **CAUGHT** (2 tests) |
| Ledger kind split is recomputed | changed `L47`'s kind | **CAUGHT** |
| No live record asserts a superseded phase | injected `"independent review #2 pending"` into `ARCHITECTURE.md` | **NOT CAUGHT — 5 passed** |
| (control) | injected `"a second independent review is pending"` | **CAUGHT** |

The stale-wording guard filters any line containing a `HISTORICAL_MARKERS` entry *before* testing
`SUPERSEDED_PHASE_CLAIMS`. Because `"review #2"` is itself a marker, **four of the six enumerated
claims are unconditionally unreachable** — including `"review #2 pending"`, which is literally the
string review #3's `MED-1` found in three live records. See BLOCKING-6. The rest of the mechanism
works, and I did not require it to validate arbitrary historical prose.

## 14. Live normative-record audit — multiple current contradictions

Historical artifacts (three review documents, three ledgers, explicitly marked historical blocks)
legitimately preserve obsolete statements and I flagged none of them. The following are **live,
unmarked, current** statements that are false at HEAD:

| Record | Statement | Reality at HEAD |
|---|---|---|
| `EXP-006_IMPLEMENTATION_PLAN.md:468-484` | "The **authoritative split**, recomputed 2026-10-03… **computed, not transcribed**… this table cannot drift from the code without a red test": 23/5/23/1/1 | 22/5/11/14/1. 13 of 53 rows misclassified. Suite green. |
| `EXP-006_IMPLEMENTATION_PLAN.md:488` | "`L37` is **the one** case deliberately labelled claim C" | 14 are |
| `EXP-006_PRE_CODE_GATE.md:256-258` | "implementation plan §12 reproduces it **under that assertion's protection**" | It reproduces a different, superseded split, unprotected |
| `EXP-006_PRE_CODE_GATE.md:267` | "**23** of the 53 are discharged by the shape of the public surface" | 11 `surface` |
| `ARCHITECTURE.md:523` | "**Two review-#3 findings remain open** and require human adjudication" | Both adjudicated and applied at HEAD |
| `INVENTORY.md:106` | "its `LOW-3` and `LOW-8` remain **open pending human adjudication**" | Same |
| `CLUSTER-004…md:443-445` (block self-labelled "**Live next step.** This block is **status**, not history") | "Two review-#3 findings remain OPEN and require human adjudication" | Same |
| `ISSUE-022…md:15-17` (the `STATUS:` block) | "review #3 … remediated, except LOW-3 and LOW-8 … **await human adjudication**" | Same |
| `ISSUE-022…md:301-302` | "**Two** independent final implementation reviews have returned `FAIL`; a **third**, separately authorized review … are required" | Three have; contradicts this record's own `STATUS` block |
| `ISSUE-022…md:414` | "Independent final implementation review #3 \| **pending, separately authorized**" | Performed, `FAIL`, remediated |
| `ISSUE-022…md:417,420-421` | "**Both** final-review artifacts"; "**Both** reviews found the rules logic conformant"; "both reviews" | Three |
| `ISSUE-022…md:103-105` | the card "amended **only** by the two … corrections of 2026-10-01 …; **not** touched by either remediation pass" | HEAD amended the card a third time (+20/−2) |
| `completion-records/INDEX.md:28` | "reviews #1 and #2 both `FAIL` …; **review #3 pending, separately authorized**" | Review #3 performed and remediated |

Current review phase (`EXP-006-PHASE: REVIEW-3-REMEDIATED`), implementation completion/acceptance
(`CODE COMPLETE; NOT FINALLY ACCEPTED` / `STATUS: NOT COMPLETE`), `SR-11`, the case total (53), the
error taxonomy, and Rule Card / gate / plan statuses are all consistent and correct. The withdrawn
refuel wording *"contributes illumination again"* appears in seven places and **every one** marks it
as withdrawn or historical — no live record quotes it as current.

`git blame` attributes every stale statement above to `3c7f452e` (review-#2 remediation). The
review-#3 remediation commit `270af44` touched the plan and `ISSUE-022` but left these untouched,
and never touched `INDEX.md` at all.

## 15. `ISSUE-022` against `DEVELOPMENT_WORKFLOW.md` §5

It does **not** falsely claim final completion: `STATUS: NOT COMPLETE`, human acceptance named as a
separate act, §5.1 cited correctly. All twelve §5 categories are present in order, with explicit
"none" where empty. Rules provenance (§5) is correct and complete against `GAME_CONSTITUTION.md`
§5 — exactly one `SR`, no Compatible Completion, no Variant. Deviations (§10) are eight,
substantive and honest. Verification commands and results (§7–§8) match what I ran; coverage (§9)
matches. Behaviour (§4) is an accurate description of the shipped module. The `LOW-9` adjudication
record (§12.1) is accurate and matches observed behaviour.

**But the record fails §5 on two required categories**: §5 item 3 (files created/modified) omits
`EXP-006_FINAL_IMPLEMENTATION_REVIEW_3.md` and `EXP-006_REVIEW_3_REMEDIATION_LEDGER.md`, and asserts
a false absolute about the card's amendment history; §5 item 11 (known limitations) states the wrong
review count and the wrong open-findings set, and the chronology contradicts the record's own
`STATUS` block. See BLOCKING-4.

## 16. State-space falsification — all attempts correctly refused

| Attempt | Result |
|---|---|
| `lit=True, remaining_turns=0` | `ValueError` — unconstructible |
| negative `remaining_turns` | `ValueError` |
| `bool` `remaining_turns` (`True`) | `ValueError` (excluded before `int`) |
| unsupported `LightSourceKind` (`"TORCH"`, `"lantern"` via `fresh`) | `ValueError` |
| malformed contribution member silently ignored | impossible — `ValueError` on `"torch"`, `None`, `42`, `dict`, duck-typed impostor |
| exhausted/unlit member contributing | impossible — filtered by function **and** refused by the aggregate |
| refuelled lantern lit automatically | no — `lit=False`, radius `None`, absent from `lit_sources`; and it does not deplete while unlit |
| invented partial-refill arithmetic | absent — refusal only |
| **unapproved `remaining_turns <= fresh_duration` ceiling** | **ABSENT.** A 600-turn torch constructs, reports radius 30, aggregates, and depletes to 594. Re-adding the ceiling in scratch was caught by `test_no_fresh_duration_ceiling_is_imposed` — the adjudicated absence now has a regression test. |

Additionally caught in scratch: torch radius diverging from lantern, `TORCH_TURNS` 6→5, invariant
removal, unlit sources depleting, `bool` accepted as `elapsed_turns`, `SR-11` row flipped, an RC
silence filled with a default, the same-round guard moved after the matrix, `deplete` emitting a
`'NO_LIGHT'` value, and refuel auto-igniting.

## 17. Documentation truthfulness

The production module's and errors module's docstrings are accurate, including their absolutes. I
verified the surface claim literally ("four constants, five types and four functions, all listed in
`__all__`" — 4/5/4 = 13 = `len(__all__)`), the "one transition deliberately absent" scoping, the
error-taxonomy table, the `"Oil"` vs `"Oil, Burning"` distinction, and the `L42` reasoning. The test
module's narrowing notes, withdrawn-claim quotations and design history are all truthful.

Untrue current absolutes found are confined to the governance records listed in §14: "the
authoritative split", "computed, not transcribed", "cannot drift without a red test", "**the one**
case labelled claim C", "under that assertion's protection", "**Two** independent final reviews",
"**Both** reviews", "amended **only** by the two corrections", "**not** touched by either
remediation pass", "remain **open**", "review #3 **pending**". These are factual, not stylistic.

## 18. Encoding — CLEAN

All 20 live EXP-006 and governance files are valid UTF-8 with no BOM, no mojibake, and no
foreign-script corruption. Notation present is legitimate: `§`, `′`, `−` (U+2212), `⅓`/`⅔`/`⅕`/`½`/
`¾`, `✓`/`✗`, `⚠`, `⇒`, en/em dashes, curly quotes. Only
`EXP-006_FINAL_IMPLEMENTATION_REVIEW.md` contains mojibake sequences (`Â§`, `â€`, and single
`â`/`Â`/`Ã`/`ï`) — each occurring once, consistent with that review deliberately quoting them as
search input, as noted in the brief. Not a defect.

## 19. Canonical verification

`.venv\Scripts\python.exe scripts\verify.py` → exit 0.

```text
Gates that actually exist (five; there is no `policy` gate):
  Tests:     PASS      1180 passed in 1.72s  (suite-wide)
  Coverage:  PASS      src/rules/ 20 files @ 100% required per file; core aggregate 100.00% (>= 95%)
  Ruff:      PASS      no issues
  mypy:      PASS      no issues found in 53 source files
  Evidence:  PASS      1 reference packet (_TEMPLATE.md); 0 Stage-A packets; 12 grandfathered
  Overall:   PASS

Module test counts
  tests/rules/exploration/test_light_and_exploration_resources.py   112 tests
  tests/rules/exploration/test_exp_006_record_consistency.py           5 tests
  EXP-006 total                                                      117 tests

Per-file coverage (independent re-run)
  src/rules/exploration/errors.py                            4 stmts,  0 branch   100% / 100%
  src/rules/exploration/light_and_exploration_resources.py 131 stmts, 52 branch   100% / 100%
```

## 20. BLOCKING findings

**BLOCKING-1 — HIGH — types B and D. Implementation plan §12 publishes the superseded claim-kind
split while asserting it is computed and test-protected.**

`docs/technical/EXP-006_IMPLEMENTATION_PLAN.md:468-484` (approved plan, live section) states: *"**The
authoritative split, recomputed 2026-10-03 from the current 53 cases.** It is **computed, not
transcribed.** The single source is `CASE_DISCHARGE`… and
`test_the_case_category_counts_are_recomputed_not_carried_over` asserts these exact numbers, **so
this table cannot drift from the code without a red test**."* It then tabulates
`behavior 23 / invariant 5 / surface 23 / reviewed 1 / routed 1`.

The shipped ledger and the test assert `behavior 22 / invariant 5 / surface 11 / reviewed 14 /
routed 1`. Measured disagreement: 3 of 5 counts wrong, and **13 of 53 rows misclassified** — `L46`
published as `behavior` (actually `reviewed`), and
`L13 L14 L15 L19b L29 L30 L31 L36 L37a L43 L44 L45` published as `surface` (actually `reviewed`).
§12's prose also asserts *"`L37` is the one case deliberately labelled claim C"*; fourteen are.
§12.1 and §12.2's lists are stale in consequence.

This is exactly the published split review-#3 ledger §3 declares withdrawn: *"The previous
23/5/23/1/1 is **NOT preserved for continuity**"*. `git blame` puts §12's table at `3c7f452e`; the
review-#3 remediation `270af44` edited this plan (25 lines) and did not correct it.

Failure scenario, demonstrated: the table **has** drifted and the whole suite is green (1180
passed). The claim "cannot drift from the code without a red test" names a machine protection that
does not exist — the test asserts the *computed* counts equal the *test's own* literals and never
reads the plan. This is finding type D (claim broader than mechanism) on top of type B (current
normative contradiction). It also contradicts `ISSUE-022` §11 item 5, which correctly says
"**Fourteen** of the 53 cases are now labelled claim C", and the test module's own instruction that
*"Every governance artifact that states a split must agree with this."*

**BLOCKING-2 — MEDIUM — types B and D. Pre-Code Gate §6 asserts a protection for plan §12 that does
not exist, and publishes a stale surface figure.**

`EXP-006_PRE_CODE_GATE.md:256-258`: *"The authoritative split is **computed** from `CASE_DISCHARGE`
and asserted by `test_the_case_category_counts_are_recomputed_not_carried_over`; **implementation
plan §12 reproduces it under that assertion's protection**."* Plan §12 reproduces a different,
superseded split, and no assertion protects it (BLOCKING-1). Separately, `:267` states *"**23** of
the 53 are discharged by the shape of the public surface"*, where the current figure is 11
`surface`. Neither line is marked historical; the surrounding text is presented as the gate's
standing finding.

**BLOCKING-3 — HIGH — types B and C. Five live normative records state that `LOW-3` and `LOW-8`
remain open, when HEAD is the commit that applied both adjudications.**

`ARCHITECTURE.md:523`, `docs/rules/INVENTORY.md:106`,
`CLUSTER-004-equipment-resources-and-evasion.md:443-445`, `EXP-006_IMPLEMENTATION_PLAN.md:59-62`,
and `ISSUE-022…md:15-17` and `:329-334` each assert the two findings "remain OPEN and require human
adjudication". Commit `a150837` (HEAD) applied both: `CHAR-005`'s denials now each carry the required
disambiguation, and the `EXP-006` card's pre-approval sentence is marked historical — verified in §6
and §12 above. `ARCHITECTURE.md`'s wording is additionally wrong in substance ("`CHAR-005` **still
carries** both… denials" as the open defect). The `CLUSTER-004` block is self-labelled "**Live next
step.** This block is **status**, not history", and `ISSUE-022` designates itself "the authoritative
current status", so none of these is a preserved historical statement. Governance/status/
traceability defect: a reader cannot determine from the authoritative records which findings are
actually outstanding before human acceptance.

**BLOCKING-4 — HIGH — types B and C. `ISSUE-022`'s review history is materially wrong and
self-contradictory, and §5 item 3 is incomplete with a false absolute.**

In the record the project designates "the single authoritative statement of current `EXP-006`
status":

- `:301-302` (§11, a required §5 category): *"**Two** independent final implementation reviews have
  returned `FAIL`; a **third**, separately authorized review and then human acceptance are
  required."* Three have. This directly contradicts the same file's `STATUS` block at `:11-14`.
- `:414` (Chronology): *"Independent final implementation review #3 | **pending, separately
  authorized**"*. It was performed (`c197fa5`, `FAIL`, 1 HIGH/4 MED/8 LOW) and remediated
  (`270af44`). The chronology also omits review #3's `FAIL`, ledger #3, and the HEAD `LOW-3`/`LOW-8`
  adjudication.
- `:417`, `:420-421`: *"**Both** final-review artifacts are preserved unaltered"*, *"**Both** reviews
  found the rules logic conformant… across 36 … mutations. Every finding in **both** reviews…"*.
  Three.
- `:108-116` (§5 item 3, required): "Created — review and remediation artifacts" omits
  `EXP-006_FINAL_IMPLEMENTATION_REVIEW_3.md` and `EXP-006_REVIEW_3_REMEDIATION_LEDGER.md`, both of
  which exist.
- `:103-105`: the card *"amended **only** by the two human-authorized bounded corrections of
  2026-10-01 (`5594907`, `e5d92ad`); **not** touched by either remediation pass"*. HEAD `a150837`
  amended that card again on 2026-10-03 (+20/−2).

**BLOCKING-5 — MEDIUM — types B and C. `docs/completion-records/INDEX.md` states review #3 is
pending.**

`:28`: *"independent final reviews #1 and #2 both `FAIL` (14 and 18 findings, all remediated
2026-10-03, none concerning rules logic); **review #3 pending, separately authorized**"*. `INDEX.md`
is mandated by `DEVELOPMENT_WORKFLOW.md` §6 as the scannable implementation history. It was never
touched by `270af44` and is not enrolled in the consistency test's `PHASE_RECORDS`, so the exact
`MED-1` defect class recurred in the one live record the new mechanism does not cover.

**BLOCKING-6 — MEDIUM — types D and E. The consistency mechanism's stale-wording guard cannot detect
four of the six conditions it enumerates, including the one it was built for.**

`tests/rules/exploration/test_exp_006_record_consistency.py:132-149`. The loop skips any line
containing a `HISTORICAL_MARKERS` entry before testing `SUPERSEDED_PHASE_CLAIMS`. `"review #2"`,
`"review-#2"`, `"review #1"`, `"review-#1"`, `"review-#3"`, `"corrected"`, `"previously"`,
`"historical"`, `"superseded"` and `"withdrawn"` are markers. Therefore:

```text
"review #2 pending"              contains marker "review #2"  ->  UNREACHABLE
"review #2 PENDING"              contains marker "review #2"  ->  UNREACHABLE
"awaiting review #2"             contains marker "review #2"  ->  UNREACHABLE
"pending independent review #2"  contains marker "review #2"  ->  UNREACHABLE
"a second independent review is pending"                      ->  reachable
"A SECOND INDEPENDENT FINAL IMPLEMENTATION REVIEW"            ->  reachable
```

Demonstrated on a scratch copy: appending `EXP-006 status: independent review #2 pending.` to
`ARCHITECTURE.md` (a `PHASE_RECORDS` file) leaves all 5 consistency tests passing. The control
mutation `a second independent review is pending` fails the test as designed, so the guard is not
wholly vacuous — but `"review #2 pending"` is the literal string review #3's `MED-1` recorded in
three live records, and it is the one phrasing the mechanism structurally cannot see. The test's
docstring claims it checks *"the specific stale phrasings three reviews have found"*, and the module
docstring presents this as the remediation for a thrice-recurring defect; the repository nowhere
discloses that two-thirds of the list is inert. This is a claim broader than the mechanism
establishes (D) and a mechanism capable of passing while the enumerated condition is present in a
live record (E).

## 21. Non-blocking limitations and informational findings

**NB-1 (limitation, accurately disclosed).** A private class attribute on an approved class —
`LightSource._rounds_elapsed = 0` incremented inside `deplete` — survives the entire suite (112
passed). This is precisely the escape review #3 found and the repository documents verbatim in
`test_no_module_level_mutable_state_exists`'s docstring, with the broader claim explicitly withdrawn
and `L13`/`L14`/`L19b` reclassified `reviewed:`. Nothing shipped holds such state (I verified both
class dictionaries). Per the review standard, a construct outside an explicitly narrow claim is a
limitation, not a defect. **Not blocking.**

**NB-2 (limitation, accurately disclosed).** A module-level `__getattr__` (PEP 562) is outside what
the namespace guards observe. The repository states this in three places and narrows the claim
accordingly. I confirmed no `__getattr__` is bound. **Not blocking.**

**NB-3 (limitation, accurately disclosed).** `_LIGHT_SOURCE_IDENTITIES[kind].__getstate__()` reaches
every catalog field with no import change and no name the AST guard inspects. Disclosed in the guard
docstring and in `ISSUE-022` §11 item 5, with `L42` correctly rested on "no public callable returns
an `Item`" instead. **Not blocking.**

**NB-4 (LOW, informational — imprecise mechanism description).** `CASE_DISCHARGE["L15b"]` reads
*"surface: `deplete`'s signature and **return type** are pinned."* The parameters are pinned; the
**return annotation is not** — changing it to `tuple[object, ...]` or bare `tuple` leaves the suite
green. The property `L15b` actually names (an exhausted source producing no party/world darkness)
*is* machine-held, by `test_exhaustion_produces_no_world_state_at_all` and nine siblings: making
`deplete` emit `'NO_LIGHT'` failed 10 tests. No requirement is falsely certified, and mypy strict
enforces the body against the annotation; only the row's mechanism wording overstates. Flagged
because the ledger preamble itself warns that "a row that names the wrong mechanism is worse than no
row."

**NB-5 (LOW, informational).** The consistency test's stale-total set is hardcoded to
`{"47","50","51"}` and covers only the two `CASE_TOTAL_RECORDS`; it does not check split figures,
per-case classifications, review counts, or the open-findings list. The docstring honestly scopes
this ("arbitrary numerals are not"), so it is not a false claim — but it is the direct reason
BLOCKING-1, -3, -4 and -5 passed undetected.

**NB-6 (LOW, informational).** `PHASE_RECORDS` omits `docs/completion-records/INDEX.md`, which is a
live status record under `DEVELOPMENT_WORKFLOW.md` §6 (see BLOCKING-5).

**NB-7 (informational).** `test_the_complete_production_dependency_surface`'s docstring names `rng`
and `rules.currency` as the transitive loads; the measured set also includes
`rules.character_creation.errors` and `rules.character_creation.character_class`. The docstring is
illustrative rather than an exhaustiveness claim, so this is not an overclaim.

**INFO-1.** The approved card's silence counts are internally loose: §Open Questions opens *"All
**six** are mapped RC silences"* and then enumerates **seven** items; §Approval says *"**Six** RC
silences, plus the unowned … predicate"*; the Submitted-contract line says *"**seven** source
silences"*. `git blame` puts the "All six" line at `82dc9ac` (2026-09-30), pre-approval. This is
inside a protected approved Rule Card, is documentation-only, affects no mechanic, provenance
classification or case ID, and predates implementation. Reported, not corrected; it needs human
direction, not remediation by an implementer.

**INFO-2.** The Stage-A evidence gate is live but has governed zero post-`DEC-0012` packets (12
grandfathered, 1 reference). `verify.py` says so explicitly. Correct and honestly reported.

**INFO-3.** Plan §12.1 and §12.2 enumerate cases by the superseded classification (e.g. `L31`,
`L43`, `L44`, `L45`, `L46` as "provable by API shape"); these are stale in consequence of
BLOCKING-1.

## 22. Final verdict

The rules layer is clean. A fourth independent re-derivation of the approved card — 38 novel
mutations, all eight ignition rows, the full state space, the error taxonomy, the `CHAR-004` seam,
the no-second-clock boundary and the 53-case enumeration — found **no rules-conformance defect, no
invented mechanic, no silently resolved ambiguity, no filled RC silence, and no unapproved
invariant**. 37 of 38 mutations were caught; the single survivor is an escape the repository already
discloses and whose claim it has already withdrawn. The guard layer, which three reviews
successively broke, now states claims that its mechanisms actually establish — I could not find a
guard overclaiming. `LOW-3` and `LOW-8` are correctly and completely applied. Verification is green
on all five real gates with 100% statement and branch coverage per file.

The defect that remains is the one the project has now failed to close four times in a row: the
records that describe this work do not agree with it. Six blocking findings are concrete and
demonstrated — an approved plan section publishing a withdrawn split under a false claim of machine
protection; a gate asserting a protection that does not exist; five live records declaring
adjudicated findings still open; the authoritative completion record contradicting its own status
block and omitting two required artifacts behind a false absolute; the mandated index saying a
completed review is pending; and the very mechanism built to stop this recurrence being structurally
blind to the exact phrasing it enumerates. Each meets the §3 standard (B, C, D or E) with evidence
and a reproduced failure scenario.

`EXP-006 FINAL IMPLEMENTATION REVIEW #4: FAIL`
