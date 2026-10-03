# `EXP-006` — Remediation Ledger for Independent Final Implementation Review #1

```text
REVIEW REMEDIATED    docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW.md
REVIEW VERDICT       FAIL  -- 2 HIGH, 4 MED, 8 LOW
REVIEWED HEAD        026e19096b472a091c381fba99de684ef5885f97
REMEDIATION DATE     2026-10-03
AUTHORIZED BY        human project owner, bounded remediation of review findings only
WORKTREE             OD_N_D-cluster-004-exp-006-stage-b
BRANCH               cluster-004-exp-006-stage-b   (unmerged, unpushed)
CERTIFICATION        NONE. The implementer does not and may not certify this.
                     A second independent review is required and is PENDING.
```

> **The `FAIL` review artifact is preserved byte-for-byte.** Nothing in it is relabelled,
> softened or deleted, and `EXP-006 FINAL IMPLEMENTATION REVIEW: FAIL` stands as the historical
> first final-review result. This ledger is a *separate* document recording what was changed in
> response. The review's own apparent mojibake at its line 703 was checked and is **not
> corruption** — the reviewer is quoting the byte sequences it searched for.

---

## 1. Scope discipline

This remediation touched **only** what a finding named. In particular:

- **No approved rules mechanic was altered.** No finding proved the implementation differs from
  the approved card, and none was treated as licence to adjust one. The ignition matrix, the
  depletion arithmetic, the `30`-foot radius, the `6`/`24` durations, `SR-11`'s branch and the
  seven guarded RC silences are **unchanged**.
- **No new `CHAR-004` identity module** was created.
- **No new RC research** was performed and **Stage A was not reopened**.
- **No merge and no push.**
- The approved Rule Card was **not modified** — see §4 for the one finding-adjacent statement in
  it that was deliberately left alone, and why.

---

## 2. The 14 findings

### HIGH

| # | Artifact | Required correction | Verification proving closure |
|---|---|---|---|
| **HIGH-1** | `ARCHITECTURE.md` §15.2 | §15.2 **denied that `SR-11` exists** and called the implementation plan unapproved, while four other artifacts register `SR-11` and plan §1 reads `APPROVED`. A governance record that denies a live Simulator Ruling is worse than one that merely omits it: the card's own ID-allocation reasoning treats a prior *textual denial* as evidence an SR number is free, which is precisely how `SR-11` was selected. | §15.2 now states the card "carries exactly one Simulator Ruling — `SR-11`" and that the plan is `APPROVED`, with a dated correction note explaining the denial-vs-omission distinction. A new §15.2 entry records `EXP-006 IMPLEMENTATION: COMPLETE — pending a passing independent final review`, notes the `FAIL` is preserved, and keeps `CLUSTER-004` implementation `NOT AUTHORIZED`. |
| **HIGH-2** | `src/rules/exploration/light_and_exploration_resources.py`; test module | The **production** docstring stated Slices C and D "are not authorized yet and are deliberately absent" — printed directly above ~250 lines of shipped Slice C/D code. A false *authorization* claim in production source, in a project whose §2 treats cards as executable specifications. The test module repeated it. | Module docstring now describes the delivered state: "The card's responsibilities are implemented in full: the light-source value model, depletion against authoritative elapsed turns, the mundane light contribution, the ignition branch selector (carrying ``SR-11``), and CHAR-004 identity binding." Test docstring rewritten to cover all four slices and to list what is *genuinely* absent (the seven RC silences, world illumination, encounter `Visibility`, blindness, rations, starvation causation). |

### MED

| # | Artifact | Required correction | Verification proving closure |
|---|---|---|---|
| **MED-3** | six artifacts of record | No completion record existed, and artifacts of record still said the implementation was `NOT AUTHORIZED`. | Created `docs/completion-records/ISSUE-022-exp-006-light-and-exploration-resources.md` and indexed it in `docs/completion-records/INDEX.md`, both stating the issue is **not** complete. Corrected plan §1.2 and §18, the `INVENTORY.md` `EXP-006` row, and the `CLUSTER-004` record's §3 status block and §13 next step. Every correction carries a dated note naming the finding and quoting the prior text. |
| **MED-4A** | test module | `CASE_DISCHARGE` claimed coverage its guards did not establish; the reviewer demonstrated **eight** forbidden additions that survived, because the guards were a *denylist* of substrings. | Replaced with an **allowlist**: `APPROVED_DEFINITIONS` (16), `APPROVED_MEMBERS` (5 classes), `APPROVED_PARAMETERS` (7 functions), discharged by four guards — exact public definition surface (AST, over `FunctionDef`/`ClassDef`/`AnnAssign`/`Assign`), `__all__` equality, exact class members (`vars` + `__dataclass_fields__`), exact function parameters (`inspect.signature`). Each carries a **non-vacuity assertion** so it cannot pass by anchoring on nothing (`checked == 5`, `checked == 7`, and a non-empty definition set). |
| **MED-4B** | test module | Discharge descriptions were reclassified honestly rather than broadened. Four rows falsely cited "import graph"; two cited guards that did not exist. | `CASE_DISCHARGE` rewritten wholesale: 53 entries, categories **recomputed from the actual mechanism**. `L13`/`L14`/`L38`/`L39` no longer cite an import graph they are not established by; `L32`/`L35` now cite the all-signatures guard; `L18` reclassified to behavior citing its own row. A new assertion forbids **two cases sharing one discharge string** — the failure mode that let `L32` and `L40` both read "no infravision parameter", naming neither case's mechanism. |
| **MED-4C** | — (verification only) | The repaired guards had to be *proved* against the escapes, not asserted. | A mutation harness on a **scratch copy** (the real worktree is never mutated) reproduces all eight demonstrated escapes plus seven controls: **15/15 CAUGHT**, baseline `PASS`. Covered: `VisibilityCategory`, `encounter_distance_from_light`, `CompleteDarkness`, `no_light_state`, `party_is_blinded`, `ration_spoilage_turns`, `LightSource.attack_penalty_when_dark`, `deplete(..., party_surprised, has_infravision)`, `6 * hours`, `minutes // 10`, an `elapsed_hours` parameter, `getattr(item, 'price')`, a direct `.price` read, the MED-5 silent-filter revert, and the §9 `ValueError` revert. |
| **MED-5** | production module | `mundane_light_contribution` **silently dropped** members that were not `LightSource` — an invalid input produced a plausible answer instead of a rejection. | Rewritten from a filtering comprehension to explicit per-member rejection, raising `ValueError` on a non-`LightSource`. Tests: a malformed member is rejected not dropped; a valid **unlit** source is accepted and simply does not contribute; a duck-typed impostor is rejected. Mutation `M12` reverts the fix and is caught. |
| **MED-6** | test module | A guard docstring claimed the module imports no RNG and no currency "at all"; that holds for **direct** imports only — both are reachable transitively through the `CHAR-004` seam the plan's own §1.1 adjudication mandated. | Docstring now claims **direct** imports only, records that `rng` and `rules.currency` are reachable transitively through the seam, and states the accurate guarantee: **no RNG is consumed**. `CASE_DISCHARGE["L33"]` reworded to "no DIRECT rng import". |

### §9 adjudication (raised by the review, not rated a defect)

| Artifact | Required correction | Verification proving closure |
|---|---|---|
| `src/rules/exploration/errors.py`; production module | `refuel_lantern` raised a plain `ValueError` for a torch and for a partly-full lantern. But `errors.py` defines `ValueError` as **structural** (a non-`int`, a `bool` masquerading as one, a negative count), and "the card states no arithmetic for a partial refill" is literally a **card silence** — the same semantic as `IgnitionNotDefinedError`, which is scoped by name to ignition. Human adjudication: introduce `LanternRefuelNotDefinedError`. | Added `LanternRefuelNotDefinedError` and wired it to **both** the torch case and the partial-refill case. A non-`LightSource` argument remains a structural `ValueError` — the categories are **not** collapsed. `errors.py` now holds three concrete types and **no base class**: exploration has three domain rejections, and a base would be the speculative hierarchy the 2026-10-01 adjudication forbade. Mutation `M13` reverts to `ValueError` and is caught. |

### LOW — all eight remediated, none dismissed on severity

| # | Required correction | Verification proving closure |
|---|---|---|
| **LOW-7** | The `L16` hour/turn guard was one-sided: `6 * hours` and `minutes // 10` both survived. | Strengthened to check (1) no hour- or minute-denominated name in any definition, parameter or member, and (2) `Mult`/`FloorDiv`/`Div` with an int constant on **either** operand. Mutations `M9`, `M9b`, `M9c` all caught. |
| **LOW-8** | Dead ledger key `"L12a_": "placeholder-never-used"`, existing only to be filtered by `not k.endswith("_")`. Cruft in an audit artifact. | Key removed. The `endswith("_")` filter is retained because it is what makes the removal provable: a reintroduced placeholder is dropped and then surfaces as `approved - mapped`. |
| **LOW-9** | Plan §11 read "`IgnitionNotDefinedError` **only**" and §16 falsification #10 read "one error base plus one subclass"; the code now ships **three** concrete types. Plan and code disagreed. | Plan §11 now records the final shipped surface — three concrete types, no base, each named with its reason — and quotes the superseded wording so the correction is auditable. §16 row 10 reworded to "three concrete error types with no base, and a pinned public surface". |
| **LOW-10** | Plan §14 specified a new file `tests/rules/exploration/test_light_guards.py`; the guards went into the single existing test module. Undocumented departure. | Plan §14 now records the departure and its reason: one module keeps the 53-case ledger and the guards that discharge it in one place. |
| **LOW-11** | Plan internal contradiction — §1/§1.1 `APPROVED` vs §18 "DRAFT — awaiting human review". | §18 now reads `APPROVED 2026-10-01`, and distinguishes `EXP-006 IMPLEMENTATION: COMPLETE — pending independent review #2` from `CLUSTER-004 IMPLEMENTATION: NOT AUTHORIZED`. |
| **LOW-12** | Pre-Code Gate §6 still tabulated **50** cases ("29 of 50") and classed `L22` as *Routed dependency* where the implementation classes it *behavior*. | §6 heading corrected to 53 with a dated note recording both the 50→51→53 path (`L12a`; `L19a`/`L19b`) and the `L22` reclassification — `L22` is an asserted outcome of the matrix, not a routed call. The "29 of 50" profile line corrected to "26 guards of 53". |
| **LOW-13** | `test_one_source_expiring_does_not_darken_the_party` said "Two lit **torches**" but used a torch and a lantern; the card's literal `L15a` input was never exercised. | Test now uses `(TORCH, 2, lit)` + `(TORCH, 6, lit)` depleted by `2` — the card's literal input — and the stale expected value was corrected `18` → `4`. |
| **LOW-14** | `getattr(item, 'price')` evaded the economic-field guard: an inherent limit of an `ast.Attribute` matcher. | New guard forbids reflective attribute access outright — `getattr`/`setattr`/`delattr`/`vars`/`eval`/`exec`/`__getattribute__` — with a non-vacuity assertion over `ast.Call` nodes, so the `ast.Attribute` matcher can no longer be bypassed by reflection. Mutations `M10` and control `M11` both caught. |

---

## 3. Guard design — the preference order was honoured

Per the standing rule, and explicitly **not** by widening substring matching (the `CLUSTER-003`
failure mode, which recurred repeatedly during this implementation):

| Rank | Mechanism | Used for |
|---|---|---|
| 1 | exact API/definition shape | the four MED-4A allowlist guards; `__all__` equality; `inspect.signature`; `vars` + `__dataclass_fields__` |
| 2 | AST structure | LOW-7's arithmetic check; LOW-14's reflective-access check; the definition enumerator |
| 3 | import graph | the no-second-clock guard; the direct-dependency guard (MED-6 now scopes its claim to *direct*) |
| 4 | behavioural/invariant tests | MED-5's rejection tests; the exhaustion invariant; the matrix |
| 5 | explicit traceability | `CASE_DISCHARGE`, now with a uniqueness assertion |

Text search appears only as a locator. **Every AST guard expected to inspect nodes asserts that
it actually anchored on the expected structure** — the vacuous-guard defect found earlier in this
work (`_CATALOG_NAMES` is an `AnnAssign`, so an `Assign`-only matcher found zero nodes and would
have passed on nothing).

---

## 4. Deliberately **not** changed, with reasons

| Artifact | Statement | Why it stands |
|---|---|---|
| The approved Rule Card §Status | "Approval of this card does not authorize implementation. `CLUSTER-004` historical-rules implementation is **NOT AUTHORIZED** and requires separate explicit human authorization under `ARCHITECTURE.md` §15.2 step 4." | **Still accurate, and not stale.** Card approval did not authorize implementation; the separate explicit per-slice authorizations are exactly what the sentence requires. Cluster-level implementation genuinely remains unauthorized. The card is also a **protected document** (`AGENTS.md` §12) and no finding proved it wrong. |
| `EXP-006_PRE_CODE_GATE.md` §294 | "`CLUSTER-004` historical-rules implementation remains **NOT AUTHORIZED**." | True at the cluster level, which is what it claims. |
| `ARCHITECTURE.md` §15.2 `CLUSTER-004` entry | "`CLUSTER-004` HISTORICAL-RULES IMPLEMENTATION: `NOT AUTHORIZED`." | True. A sibling entry now records the single-card `EXP-006` position without weakening it. |
| `EXP-006_FINAL_IMPLEMENTATION_REVIEW.md` | the whole artifact, including the `FAIL` verdict | Preserved unaltered by instruction. Its line-703 "mojibake" was checked and is quoted search input, not corruption. |
| All `CLUSTER-001`/`002`/`003` and `ENC-005` status text | various `NOT AUTHORIZED` | Out of scope and, as inspected, accurate. |

---

## 5. Verification

```text
uv run python scripts/verify.py

Tests:     PASS
Coverage:  PASS      100% statement AND branch, per file, on both production modules
Ruff:      PASS      52 source files, line-length 100
mypy:      PASS      strict
Evidence:  PASS      DEC-0012 structural linter
Overall:   PASS
```

**Independent case reconciliation** — enumerated from the **Rule Card's own tables**, not read
off `CASE_DISCHARGE`:

```text
case IDs in the card:              53
case IDs in CASE_DISCHARGE:        53
in card but not mapped:            none
mapped but not in the card:        none
discharge strings unique:          53 of 53   (was 52 -- L32/L40 collision, fixed)
split:  26 guard | 20 behavior | 5 invariant | 2 routed
```

**Adversarial mutation re-run:** baseline `PASS`, then **15/15 CAUGHT**.

**Encoding sweep**, 166 tracked text files: no BOM, all valid UTF-8, no mojibake, no unexpected
script. `§`, em-dashes, `′`, `×`, `⅓` and similar are legitimate typography. The only mojibake
token found anywhere is the reviewer's own quoted search input (§2 above).

---

## 6. What this ledger does **not** do

```text
IT DOES NOT CERTIFY COMPLETION.           The implementer may not.
IT DOES NOT RELABEL REVIEW #1.            FAIL stands, unaltered.
IT DOES NOT AUTHORIZE A MERGE OR PUSH.
IT DOES NOT AUTHORIZE CLUSTER-004 IMPLEMENTATION, ENC-005 STAGE B,
   OR ANY NEW STAGE-A CARD.

NEXT REQUIRED STEP:  a second INDEPENDENT final implementation review
   against the remediated HEAD, inspecting the whole implementation and
   not merely these 14 fixes, performing no remediation in its own pass.
```
