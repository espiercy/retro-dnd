# `EXP-006` — Pre-Code Gate Assessment

## 0. Outcome

```text
PRE-CODE GATE: PASS

Card:        EXP-006 -- Light & Exploration Resources
Approved:    2026-10-01, human project owner, at b9af227
Assessed:    2026-10-01
Blocking defects:      NONE
Non-blocking cautions: 3
```

**This `PASS` is a readiness finding, not an authorization.** It states that the approved Rule
Card is complete, deterministic, bounded and dependency-safe enough to permit **drafting an
implementation plan**. It does not authorize an implementation plan, production code, production
tests, or `CLUSTER-004` implementation, all of which remain separate human acts under
`ARCHITECTURE.md` §15.2 step 4.

---

## 1. Procedure used

### 1.1 Which gate this is

This is the **per-card readiness assessment** modelled on `docs/technical/CLUSTER-003_PRE_CODE_GATE.md`
and evaluated against `ARCHITECTURE.md` §15.1's five criteria. `ARCHITECTURE.md` §16's
project-wide Pre-Code Development Gate is already `CLEARED` (2026-08-15) and is **neither
re-performed nor weakened** by this document.

### 1.2 Why no implementation plan was drafted

Drafting one is **not a required artifact of this gate** — the `CLUSTER-003` precedent (§1.2 of
that record) establishes that explicitly — and the authorizing direction for this task prohibits
it. None exists and none was begun.

### 1.3 Sources used

The approved Rule Card, the accepted Stage-A evidence packet, current approved governance, and
the landed source tree. **No new RC source research was performed.**

---

## 2. `ARCHITECTURE.md` §15.1 — the five readiness criteria

| # | Criterion | Finding |
|---|---|---|
| 1 | **Intended behavioral scope clearly defined** | **MET.** §A states what the card owns; §B lists fourteen exclusions by name; §6 fixes the entire output surface at three fields |
| 2 | **All historical rules required to execute that scope identified** | **MET.** Stage A passed independent `DEC-0010` completeness review (review 5, after four `FAIL`s). Every executable clause traces to a cited, visually verified RC page |
| 3 | **All Rule Cards required by that scope are `APPROVED`** | **MET.** `EXP-006` `APPROVED` 2026-10-01. Its two *required* dependencies — `EXP-002`, `CHAR-004` — are `APPROVED` **and implemented** (§4) |
| 4 | **External dependencies not implemented in the cluster have a stable approved contract sufficient for integration** | **MET.** The only consumed externals are landed. Every unresearched card is **downstream-only** and is reached, if at all, by the consumer — never called by `EXP-006` (§4) |
| 5 | **No unresolved rules ambiguity the implementation agent would need to adjudicate** | **MET.** Seven silences are named; **each has a deterministic disposition** — refuse, floor, or do-not-produce — so the implementer decides nothing (§5) |

---

## 3. Owned mechanics — confirmed against the approved card

**Executable ownership is limited to exactly these ten**, and the card contains nothing else
executable:

```text
torch mundane illumination state           §2, §6      L1, L3, L27
lantern mundane illumination state         §2, §6      L2, L27
finite source duration                     §3          L6, L7
depletion vs authoritative EXP-002 turns   §4          L8, L10, L11
oil as lantern fuel, as specified          §3, §4      L7, L12
tinderbox ordinary-condition ignition      §5          L17, L18, L19
Fire-Building branch selection             §5          L20, L21, L22
refusal of source-undefined ignition       §5          L23, L24
mundane-light contribution output          §6          L27, L28, L34
source-local exhaustion                    §4          L9, L12, L15a
```

**Confirmed NOT owned.** Each is excluded in §B and carries at least one guard test:

| Not owned | Guard |
|---|---|
| global / environmental darkness | L29, L37a |
| encounter `Visibility` | L30, L31, L32 |
| encounter distance | L33, L36 |
| surprise | L34, L35 |
| blindness determination | L37, L37a |
| blindness consequences | L38, L39 |
| magical illumination | L41 |
| infravision possession | L40 |
| skill-check resolution | L25 |
| dungeon-time advancement | L13, L14 |
| equipment pricing / encumbrance | L42 |
| rations | L43 |
| starvation causation | L44 |
| torch-as-weapon | L45 |
| oil-as-missile / pursuit | L46 |

**Verified mechanically**: `infravision` does not appear anywhere in §1–§5 of the specification.
The pre-remediation card consumed it to classify visibility; the remediation removed that
coupling, and the absence is now a checkable property rather than a claim.

---

## 4. Dependency classification

The distinction that decides this gate is **consumed** versus **routed**. A card `EXP-006` calls
must be implementable. A card that calls `EXP-006`, or that a *consumer* later calls, need not be.

### 4.1 Required to implement `EXP-006` — both landed

| Card | Status | What is consumed | Evidence |
|---|---|---|---|
| **`EXP-002`** | `APPROVED`, **implemented** | `elapsed_turns` only | `src/rules/exploration/turn_credit.py` (`TurnCredit`, `TurnCreditOrigin`), `dungeon_turn_time_accounting.py` (`DungeonTimeAccounting`) |
| **`CHAR-004`** | `APPROVED`, **implemented** | item **identity only** — never price or encumbrance | `src/rules/character_creation/equipment.py` carries `"TORCH"`, `Lantern`, `Oil`, `Tinder box` |

### 4.2 Routed / downstream only — **not required to implement `EXP-006`**

| Card | Status | Why not required |
|---|---|---|
| `CHAR-012` | Unresearched | `has_skill: bool` is a **caller-supplied input** (§1). The adverse branch emits a **routed request**; `EXP-006` resolves no check (L25) |
| `CHAR-009` | Unresearched | Infravision is **not an input** to any clause. Appears only as a routing destination in §8 |
| `CHAR-005` | `APPROVED`, implemented | Pure downstream. `EXP-006` applies no multiplier (L38) |
| `ENC-001` | Unresearched | Pure downstream. `EXP-006` produces no category and rolls no die (L31, L33) |
| `COMBAT-*` | Unresearched | Pure downstream (L39, L45, L46) |
| `MAGIC-*` | Unresearched | Excluded entirely (L41) |

**None of the six was reopened or researched for this gate.**

**Finding:** `EXP-006`'s unusual property is that **its unresearched dependencies are all on the
output side**. It consumes two landed cards and nothing else. The post-remediation contract is
what makes this true — the pre-remediation card consumed infravision and surprise, which would
have coupled it to two unresearched cards.

---

## 5. Particular Pre-Code questions

### A. Time dependency — **YES, without a second clock**

`EXP-002` is sole authority. `EXP-006` receives `elapsed_turns` and performs one subtraction
(§4). It holds no counter, no clock and no elapsed-time field; L13 and L14 are guard tests over
exactly that. RC states both durations **in turns itself** (`six turns`, `24 turns`), so no
conversion exists to get wrong (L16).

### B. Equipment dependency — **YES, without reproducing catalog facts**

`EXP-006` consumes identity only; `OilFlask` and `Tinderbox` are annotated
`(identity/cost/enc: CHAR-004)` in §1. No price, price form, `Coin` or encumbrance value appears
anywhere in §1–§8, and L42 guards emission. Legality is not referenced at all.

### C. Skill dependency — **YES, with `CHAR-012` unimplemented**

Branch selection is a pure function of three booleans (`has_skill`, `has_tinderbox`,
`conditions`) producing one of four dispositions:

```text
AUTOMATIC              no roll
ROLL_1d6_IGNITE_1_2    select the 1d6 branch; THE CALLER ROLLS, not this card
ROUTED_SKILL_CHECK     emit a request; CHAR-012 resolves
REFUSE                 explanatory error
```

> **Corrected 2026-10-03 (review-#3 `MED-2`).** This line read *"this card's own roll"*, which
> contradicts the approved plan §11 and the shipped module: `EXP-006` **rolls nothing** and imports
> no RNG. It returns the selected branch, and rolling is the caller's.

Only `ROUTED_SKILL_CHECK` touches `CHAR-012`, and it is **emitted, not resolved** — the DM-assigned
penalty is an input to that check, not a value `EXP-006` must produce. **`EXP-006` is implementable
today with `CHAR-012` entirely absent.**

### D. Source exhaustion — **YES, precise enough**

The card states the positive consequence and the three forbidden over-extensions separately:

```text
remaining_turns == 0  ->  THAT SOURCE contributes no illumination   (§4, Necessary Consequence)
                      ->  NOT global darkness                       (L15b, L29, L37a)
                      ->  NOT blindness                             (L37, L37a)
                      ->  NOT encounter Visibility                  (L30, L31)
```

`L15a` is the decisive case: two lit torches, one expires, `any_mundane_source_lit` **remains
`true`**. An implementation that conflated source-exhaustion with party-darkness fails it.

### E. Output contract — **YES, deterministic and ownership-safe — with one caution**

The three fields are fully determined, and §4 fixes the membership rule: an `EXPENDED` source
**leaves `lit_sources`** and stops contributing to `max_mundane_radius_feet`. So:

```text
lit_sources             = sources that are lit AND remaining_turns > 0
any_mundane_source_lit  = lit_sources is non-empty
max_mundane_radius_feet = 30 if lit_sources else None
```

**The inconsistent state the gate asks about cannot arise in the output**: an exhausted source
cannot appear as illumination-producing, because membership is conditioned on
`remaining_turns > 0`.

**Caution 1 (non-blocking)** — the card does not state whether `LightSource.lit` is itself set
`false` at exhaustion, or remains `true` while the source is excluded by the duration condition.
**No output depends on the answer**; both representations yield identical `lit_sources`,
`any_mundane_source_lit` and `max_mundane_radius_feet`. This is an internal modelling choice for
the implementation plan, **not an unresolved rules ambiguity**, and the implementer is not
adjudicating a rule by picking one. Flagged rather than resolved here.

### F. Ignition state transitions — **YES, with one intentional refusal**

| Transition | Established? |
|---|---|
| `unlit → ignition attempted` | **Yes** — §5, all six branches |
| `ignition attempted → lit` | **Yes** — automatic, or on `1–2` of `1d6`, one attempt per round |
| `ignition attempted → still unlit` | **Yes** — L18, retry next round |
| `lit → expended` | **Yes** — §4, at `remaining_turns == 0` |
| `expended → refuelled` (lantern) | **Yes** — §4: a further flask **restores `remaining_turns` to `24` and leaves the lantern unlit**. **No mundane-light contribution until separately ignited** (§5). *Corrected 2026-10-03 — see the note below this table.* |
| `expended → refuelled` (torch) | **Not applicable** — a torch has no fuel; a fresh torch is a new source. *(The implementation treats this as an invalid **argument**, `ValueError`, not a source silence — human adjudication 2026-10-03, review-#2 `LOW-9`.)* |
| `lit → unlit` (deliberate extinguish) | **INTENTIONALLY UNAVAILABLE** — RC is silent (§Undefined 4). The implementation must **refuse deterministically**; no extinguish, relight or refill-timing procedure is invented |

**No transition is silently invented.** The one unavailable transition is unavailable because RC
does not state it, which the authorizing direction accepts provided refusal is deterministic — and
it is.

> **Withdrawn wording corrected 2026-10-03, under review-#3 finding `MED-2`.** The lantern-refuel
> row above read *"a further flask resets to `24`; **L12 confirms it contributes again**"*. The
> phrase *"contributes illumination again"* was **expressly withdrawn from the Rule Card on
> 2026-10-01** by human adjudication, as asserting an ignition the card never establishes. Because
> §8a below declares §1–§8 to be standing findings, this sentence was reading as a **current**
> claim rather than as history — review #2 graded the identical misquote `HIGH-2` where it appeared
> in a test docstring, and it survived here. The current refuel contract is:
>
> ```text
> refuel restores remaining_turns = 24
> lit = False
> no mundane-light contribution until separately ignited
> ```
>
> **The Rule Card mechanic is unchanged by this correction** — only this record's statement of it.
>
> Two further corrections in this same section, also under `MED-2`:
>
> - §5.C's transition table glossed `ROLL_1d6_IGNITE_1_2` as *"this card's own roll"*. **This card
>   rolls nothing**: it selects a branch and returns it, and the roll belongs to the caller
>   (approved plan §11; approved card §5). Corrected in place.
> - §8a's claim that *"§1–§8 are preserved unaltered"* is **false as written** and is corrected
>   there: §6 carries a 2026-10-03 correction, and so now does this section. What §8a means, and
>   now says, is that no §1–§8 *finding* was re-performed or reversed.

---

## 6. Deterministic-case readiness — all 53 translate

> **Count and classification corrected 2026-10-03, twice.** This section first tabulated **50**
> cases and classed `L22` as *Routed dependency*. A first correction (review-#1 `LOW-12`) fixed the
> heading and one profile figure but **left this section's own table at 50 and `L22` still routed**
> — the two things it claimed to have fixed — and pointed at implementation plan §12, which review
> #2 then found to be internally inconsistent as well (`MED-4`). Both are now corrected.
>
> **This section no longer publishes a split.** A gate record written before implementation is the
> wrong place for a figure that later changed four times. The superseded table — *Implementation
> test 18 / Boundary-ownership 18 / Boundary-internal 11 / Routed 3*, totalling 50 — is withdrawn,
> not preserved for continuity.
>
> **Corrected again 2026-10-03 under review-#4 finding `B-2`.** This note previously added that
> *"implementation plan §12 reproduces it under that assertion's protection"*. **No such protection
> existed** — the test compares counts it derives from `CASE_DISCHARGE` against its own literals and
> never reads the plan — and plan §12 had in fact drifted to a withdrawn split. Plan §12 no longer
> publishes a split either. **This gate does not own the post-implementation category split**, and
> asserts no protection over any other document.

**All 53 approved cases translate into executable obligations, and no case requires exceeding
`EXP-006` ownership to test.** That was this gate's actual finding and it held: the shipped suite
discharges all 53. The **case total is reconciled against the approved Rule Card** by
`test_the_approved_case_total_is_still_what_the_records_claim`, and the **current category
classification is derived from `CASE_DISCHARGE`** — neither is owned here.

The profile is **guard-heavy**: a substantial share of the cases are discharged by the shape of the
public surface rather than by an assertion about a value, split between a machine-enforced observed
surface and a reviewed ownership boundary. *The specific figure this paragraph used to quote ("23 of
the 53") is removed under `B-2`: it was a hand-copied number, it had gone stale, and the current
counts are derived from `CASE_DISCHARGE`, not from this record.* The guard-heaviness is a direct
product of the bounded remediation: four cases that previously *asserted* behaviour now *forbid* it.
`L34` inverted outright — from an `ERROR` when a surprise state was missing, to a **success** case,
because surprise is no longer an input.

**Caution 2 (non-blocking)** — those surface cases are mostly **negative/architectural**
assertions ("this module must not import `ENC-001`", "no price value is emitted"). The
`CLUSTER-003` precedent is directly relevant: guard tests written as substring checks over source
text produced false positives, and the project moved to **AST/import-graph assertions**. The
implementation plan should adopt that technique rather than rediscover it.
>
> *Borne out, and then some.* Review #1 broke a token denylist; review #2 broke the AST
> declaration-walk that replaced it, six ways. The shipped guards read the **imported module
> namespace** and the **effective class surface** instead, and state their claims narrowly.

**Caution 3 (non-blocking)** — `L22` and `L37` assert what the card **does not do** while also
describing a routed outcome. They are testable as "returns a routed request / returns no
predicate", but their *consumers* cannot be tested until `CHAR-012` and the complete-darkness
owner exist. They are **routed-dependency tests, not integration tests**, and should be scoped as
such.

---

## 7. Blockers

```text
NONE.
```

No `PRE-CODE BLOCKER — NOT ESTABLISHED BY APPROVED RULE CARD` condition was reached. Every
question in §5 is answered from the approved card alone; nothing required inference or outside
research.

Seven RC silences remain, **by express approval**, each with a deterministic disposition:

| Silence | Disposition | Blocks implementation? |
|---|---|---|
| Behaviour at zero beyond the source ceasing to burn | nothing synthesized | **No** — L15 |
| Carried light → any `Visibility` category | not produced | **No** — `ENC-001` owns it |
| Adverse ignition without `Fire-Building` | **refuse** | **No** — deterministic |
| Deliberate extinguishing | transition unavailable, refuse | **No** |
| Timetrack scope for light durations | not adopted | **No** — §4 uses `EXP-002` |
| Water consumption rate | out of owned scope | **No** |
| Complete-darkness world-state predicate owner | **not settled**, no owner invented | **No** — `EXP-006` never needs it |

The last is the one worth the project owner's eye: it is an **open governance question**, not a
rules gap, and `EXP-006` is deliberately implementable without it being answered.

---

## 8. Readiness statement

```text
PRE-CODE GATE: PASS -- 2026-10-01

EXP-006 is ready for an IMPLEMENTATION PLAN to be drafted.

This is NOT:
    an implementation plan
    authorization to draft one
    authorization to write production code or production tests
    CLUSTER-004 implementation authorization (ARCHITECTURE.md §15.2 step 4)
```

`CLUSTER-004` historical-rules implementation remains **NOT AUTHORIZED**. `ENC-005` Stage B
remains **DEFERRED** and is untouched by this assessment.

## 8a. Bounded remediation — 2026-10-01, ignition portion only

> **The original `PASS` in §0 and every §1–§8 *finding* stand, unreversed and not re-performed.**
> They were made on 2026-10-01 and **missed two defects in the ignition portion**. This section
> records what was missed, the human adjudications that resolve it, and a reassessment of **only**
> that portion.
>
> **Wording corrected 2026-10-03 (review-#3 `MED-2`).** This preamble previously said §1–§8 were
> "preserved unaltered", which review #3 correctly identified as false: §6 carries a 2026-10-03
> case-count correction, §5.C and §5.F carry 2026-10-03 corrections, and each is marked in place.
> The accurate statement is the one above — no §1–§8 *finding* was reversed; several *statements*
> of those findings have been corrected where they had gone stale or misquoted the card.

### 8a.1 What the original gate missed

**Missed defect 1 — an overlapping ignition branch.** §5.C concluded that *"Branch selection is a
pure function of three booleans… producing one of four dispositions"* and declared it
deterministic. **It never tested `(has_skill=True, has_tinderbox=False, conditions=ADVERSE)`.**
That input satisfied two approved branches at once — `1d6` and `ROUTED_SKILL_CHECK` — which are
incompatible. §7's silence table listed *"Adverse ignition without `Fire-Building` → refuse"*,
which is the **lacks-skill** case, not this intersection; the gate mistook one for the other.

**Missed defect 2 — no implementation contract for one-attempt-per-round.** §5.F judged the
ignition transitions implementable without noticing that approved case `L19`
(*"Two ignition attempts in one round → ERROR"*) requires knowing an attempt already happened —
round state the plan correctly forbids `EXP-006` from holding. The gate's §5.A *"no second clock"*
finding and its §5.F transition finding were each true in isolation and **jointly unsatisfiable**,
and the gate did not notice.

**Both were found by a later pre-Slice-C audit, not by this gate.** Recorded as a gate miss rather
than presented as something the gate had resolved.

### 8a.2 The adjudications that resolve them

**`SR-11`** (human project owner, 2026-10-01) — where a character has `Fire-Building` and
conditions are `ADVERSE`, the adverse-condition procedure governs **regardless of a tinderbox**,
so `(skill, no tinderbox, ADVERSE) → ROUTED_SKILL_CHECK`. The accepted evidence establishes both
RC conditionals and **no precedence between them**; the ruling resolves only that intersection.

**Caller-supplied attempt state** (same date) — the future ignition API consumes
`attempt_already_made_this_round: bool`. `EXP-006` **enforces** the one-attempt rule from
authoritative state it is **given** and does not become the authority that **tracks** it — the
same boundary already established for `elapsed_turns`. No round counter, no clock, no mutable
cross-call state, and no orchestrator or action-economy framework is created.

### 8a.3 The resulting matrix — reassessed

```text
skill  tinderbox  conditions   disposition                     provenance
 yes      yes      ORDINARY    AUTOMATIC                       RC Explicit
 yes      yes      ADVERSE     ROUTED_SKILL_CHECK              RC Explicit
 yes      no       ORDINARY    ROLL_1D6_IGNITE_1_2             RC Explicit
 yes      no       ADVERSE     ROUTED_SKILL_CHECK              SR-11
 no       yes      ORDINARY    ROLL_1D6_IGNITE_1_2             RC Explicit
 no       yes      ADVERSE     REFUSE                          RC silence
 no       no       ORDINARY    REFUSE                          RC silence
 no       no       ADVERSE     REFUSE                          RC silence
```

**Eight combinations, eight rows, no wildcard.** Mechanically verified: every
`(skill, tinderbox, conditions)` triple matches **exactly one** row, and
`(True, False, ADVERSE)` appears once and resolves to `ROUTED_SKILL_CHECK`.

### 8a.4 Reassessment of the ignition portion only

| Question | Finding |
|---|---|
| Branch selection deterministic? | **Yes**, now by enumeration rather than by assertion |
| `(True, False, ADVERSE)` resolved? | **Yes** — `ROUTED_SKILL_CHECK`, by `SR-11` |
| Any wildcard/overlap remaining? | **No** |
| `L19` implementable? | **Yes** — from `attempt_already_made_this_round`, a caller input |
| Does `EXP-006` gain round state? | **No** — guard `L19b` |
| Implementer adjudicates anything? | **No** — the one ambiguity is settled by ruling, not by the implementer |

```text
EXP-006 PRE-CODE GATE: REVALIDATED -- 2026-10-01 (ignition portion)

The original PASS stands as recorded, with its two misses documented above
rather than erased.  The ignition portion is deterministic after remediation.
This remains a readiness finding, not an authorization.
```

## 9. Provenance

Assessed against the approved Rule Card at `b9af227`, the accepted Stage-A packet, `ARCHITECTURE.md`
§15.1/§15.2/§16, and the landed source tree. **No new RC research. No production code, production
test, or implementation plan was created.** Three non-blocking cautions are recorded above for the
implementation plan to absorb.
