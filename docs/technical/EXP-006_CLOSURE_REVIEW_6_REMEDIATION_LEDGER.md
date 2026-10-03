# `EXP-006` — Remediation Ledger for Closure Review #6

```text
REVIEW REMEDIATED    docs/technical/EXP-006_CLOSURE_REVIEW_6.md
REVIEW VERDICT       FAIL  -- 2 BLOCKING, 5 non-blocking, 3 informational
REVIEWED HEAD        ba4c49e59ef2a85ef4c332474f9756d8c874f3b9
ARTIFACT COMMIT      534e0d842749519c85ee050b24d00c18f27e01ca
REMEDIATION DATE     2026-10-03
AUTHORIZED BY        human project owner, with an ARCHITECTURE DECISION
                     (see SS1). Review #7 NOT launched.
WORKTREE             OD_N_D-cluster-004-exp-006-stage-b
BRANCH               cluster-004-exp-006-stage-b   (unmerged, unpushed)
CERTIFICATION        NONE. Closure review #6 remains a historical FAIL.
```

> **Reviews #1–#5, closure review #6 and remediation ledgers #1–#5 are preserved unaltered.** Where
> a historical ledger made a claim a later review disproved, that ledger is **not** edited — the
> correction is recorded here (§5).

---

## 1. The architecture decision this ledger implements

Closure review #6 did not find a new kind of mistake. It found the **same** mistake for the third
consecutive pass, and named the root cause precisely:

```text
Token presence is not prose coherence.
```

`CLUSTER-004` carried the correct `EXP-006-PHASE: REVIEW-5-REMEDIATED` token **and**, twelve lines
below it, the sentence *"Review #4's remediation is the most recent work"* — simultaneously, with
the suite green, in a block that declared itself *"status, not history"* and *"cannot silently go
stale again"*.

The project had three times attempted the same remedy: **synchronize the duplicated current-status
prose.** Each attempt corrected the instances a review named and seeded a new one —

| Pass | Fixed | Missed |
|---|---|---|
| review-#4 remediation | the plan, the `CLUSTER-004` record | the `ARCHITECTURE.md` twin |
| review-#5 remediation | the `ARCHITECTURE.md` twin | the `CLUSTER-004` twin, `INDEX.md` |

**That strategy is withdrawn by human decision of 2026-10-03.** The replacement is **single
ownership**: volatile current status is owned by exactly one record, and the others reference it
rather than restating it. A fact that exists in one place cannot have a stale twin.

---

## 2. `BLOCKING-6-1` — the cluster record

| | |
|---|---|
| **Defect** | `CLUSTER-004-equipment-resources-and-evasion.md:446` asserted *"Review #4's remediation is the most recent work"*, present-tense and unmarked, twelve lines below the `REVIEW-5-REMEDIATED` token at `:434`, in a block the same pass had edited. The statement was **true** at `e5caf12` and was **made false** by the review-#5 remediation. |
| **Root cause** | **Duplicated ownership of volatile current status.** Two records each independently asserted "which review is newest"; the phase-token mechanism pinned one string and said nothing about the prose around it, so the guard was green while the record contradicted itself. |
| **Correction** | **Not** a change of "Review #4" to "Review #5". The volatile assertion is **removed**, and `§13` is restructured: `§13.1` states that current status is **not owned here** and references `ISSUE-022`; `§13.2` keeps the record's own durable business — the `ENC-005` position and `CLUSTER-004`'s own authorization state — plus explicitly-labelled `HISTORICAL` chronology. The `§3` status block's phase token is likewise replaced by a reference. |
| **Verification** | `test_non_authoritative_records_own_no_volatile_status` (production predicate, all six enrolled records); `test_a_volatile_duplicate_in_the_cluster_record_is_rejected` reproduces the exact defect shape on a fixture. |

---

## 3. `BLOCKING-6-2` — the completion-records index

| | |
|---|---|
| **Defect** | `docs/completion-records/INDEX.md:28` stated *"most recent: review #4 `FAIL`, remediation current"* — in **the very cell the review-#4 remediation had rewritten** to close review-#4 `B-5` ("the index said a completed review was pending"). The review-#5 remediation did not touch `INDEX.md` at all. |
| **Root cause** | The same duplicated ownership, aggravated by a coverage gap: `INDEX.md` was enrolled for stale-wording checks but **deliberately exempt** from the phase token ("the index is a one-line summary"), so the one mechanism that might have caught it did not apply. |
| **Correction** | **Not** a change to review #5 or #6. The volatile claim is removed; the row now says what `EXP-006` is, that slices A–D are accepted, that every review to date returned `FAIL` with none concerning rules logic — all durable — and that **current status is owned by the record itself and not stated in the index**. |
| **Verification** | Same production predicate; `test_a_volatile_duplicate_in_the_index_is_rejected` reproduces the `Review #6 is pending` shape on a fixture. |

---

## 4. The ownership model

Recorded once, in `ARCHITECTURE.md` §15.2 — not as a new framework:

```text
ISSUE-022            AUTHORITATIVE for current EXP-006 status
CLUSTER-004 record   cluster chronology / durable cluster context
INDEX.md             navigation
ARCHITECTURE.md      architecture and durable process history
INVENTORY.md         rule-inventory ownership and source attribution
plan / Pre-Code Gate the approved contract and the readiness finding
review artifacts     immutable historical review results
remediation ledgers  immutable historical remediation records
```

Everything but the first line **does not own the current `EXP-006` phase**. Normalized this pass:

| Record | Was | Now |
|---|---|---|
| `ARCHITECTURE.md` | phase token; a relative review-recency phrase; a sentence asserting whether a further review was authorized | an ownership-reference block, the ownership table, and durable architectural facts only |
| `CLUSTER-004` record | phase token ×2; "most recent work"; "NOT YET AUTHORIZED" | `§13.1` reference + `§13.2` durable context and labelled history |
| `INVENTORY.md` | phase token in the `EXP-006` row | reference + durable facts |
| implementation plan | phase token ×2 | reference, in both status blocks |
| Pre-Code Gate | *no reference at all* | a header reference; it owns a 2026-10-01 readiness finding, nothing current |
| `INDEX.md` | "most recent: review #4" | reference + durable facts |
| **`ISSUE-022`** | one of several carriers | **the authority** — declares itself so, carries the phase token, and states the full current position |

---

## 5. `NB-1` — a false claim in ledger #5, and the code behind it

| | |
|---|---|
| **Defect** | Closure review #6 found `test_injecting_review_3_pending_into_a_live_record_is_detected` still re-implemented the match inline (`[c for c in STALE_CURRENT_CLAIMS if c in …]`) rather than calling `_stale_claims_in`, making it tautological in exactly the way review-#5 `NB-3` described — it would keep passing if the production predicate were disarmed, the one regression it exists to prevent. |
| **The false claim** | **Ledger #5 §2 stated** *"Both predicates are now named functions … used by **both** the live-record checks and the regressions"*, and **§5 dispositioned `NB-3` as "Corrected"**. That was **false for this one test**. |
| **Disposition** | **Ledger #5 is preserved unaltered** — it is historical evidence, and a historical false claim stays visible as a historical mistake. The discrepancy is recorded **here** instead. |
| **Correction** | The inline comprehension **is** part of the current mechanism and **did** violate the current intended design, so per the authorization's branch (3) the test is corrected to call `_stale_claims_in`. Its docstring records what the claim was and why it was wrong. |
| **Verification** | Both named regressions now call the production predicate; `test_every_stale_claim_is_detectable_by_the_production_predicate` independently covers all configured claims through the same function. |

---

## 6. `INFO-1` propagation

Closure review #6 `NB-5` found that the human adjudication had been made but not propagated to the
authoritative record. `ISSUE-022` §11 item 8 previously said the finding *"is open and requires human
adjudication"*. It now records:

```text
INFO-1   NO CHANGE
         reviewed; no protected-card correction authorized;
         finding not substantiated as a rules/documentation defect
```

with the accepted rationale in new `ISSUE-022` §12.2 — review #4 did not establish an objective
typo; the seven entries are not seven members of one mapped-RC-silence category (three are
governance items); the card contains a genuine separate six-item list. **The protected approved Rule
Card is not modified**: its blob is byte-identical across every reviewed `HEAD`.

---

## 7. The consistency mechanism, redesigned around ownership

The phase-token design is **withdrawn**, not patched. What replaced it:

```text
STATUS_AUTHORITY            ISSUE-022
NON_AUTHORITATIVE_RECORDS   the six enrolled records
VOLATILE_STATUS_FORMS       a closed, narrow list of current-state shapes
_volatile_status_in(text)   the production predicate
```

**It does not parse English for semantic coherence**, and it does not classify sentences as
historical or current. The patterns match current-state **predicates** — *"is the most recent"*,
*"is pending"*, *"not yet authorized"* — so an event sentence is simply not a match:

```text
"Review #5 returned FAIL on 2026-10-03"     historical event  -> ALLOWED
"Review #5 is the most recent review"       current assertion -> REJECTED
```

That is what keeps history legal **without a marker skip list**. There is none, and there must never
be one: review #4 and review #5 both blocked on exactly that construct, and this pass hit the same
pressure again — nine of my own correction notes initially tripped the new predicate by **quoting**
the forbidden phrasings. The fix was to **describe rather than reproduce them**, not to add an
exemption. That discipline is now recorded in the notes themselves.

Also closed here, from closure review #6's informational findings: `HISTORICAL_ARTIFACT_GLOBS`
replaces the literal historical-artifact list, which `INFO-1` found had omitted review #5 and ledger
#5 while claiming to assert the never-scanned property.

**Scope, deliberately:** only `EXP-006` current-status ownership, only for the explicitly named
records. No NLP, no repository-wide prose linting, no generalized historical/current sentence
classifier, no new framework.

---

## 8. Ownership-model regressions — A to F

| § | Property | Test | Result |
|---|---|---|---|
| **A** | the authority exists and is designated | `test_the_status_authority_exists_and_is_designated` | PASS |
| **B** | enrolled records reference the authority | `test_non_authoritative_records_reference_the_authority` | PASS |
| **C** | a volatile duplicate in `CLUSTER-004` is rejected | `test_a_volatile_duplicate_in_the_cluster_record_is_rejected` | PASS (rejects) |
| **D** | a volatile duplicate in `INDEX.md` is rejected | `test_a_volatile_duplicate_in_the_index_is_rejected` | PASS (rejects) |
| **E** | historical chronology remains allowed | `test_historical_chronology_remains_allowed` | PASS (allows) |
| **F** | the authority may state current status | `test_the_authority_may_state_current_status` | PASS |

All six exercise `_volatile_status_in` — the production predicate — not copied test logic. **F**
asserts the exemption is by **record identity** (the authority is not in the enrolled set), so
enrolling the authority by mistake fails, and it additionally asserts the authority *does* exercise
its ownership.

---

## 9. Settled layers — untouched

```text
production EXP-006 mechanics      unchanged
Rule Card mechanics               unchanged (blob byte-identical)
SR-11                             unchanged
ignition matrix                   unchanged
depletion / refuel semantics      unchanged
error taxonomy                    unchanged
CHAR-004 seam                     unchanged
architecture guard claims         unchanged
CASE_DISCHARGE semantics          unchanged -- no category or case touched
Stage-A evidence / RC research    not reopened; none performed
```

The only test file changed is the consistency module, and the only production-adjacent change is
documentation.

---

## 10. Verification

```text
uv run python scripts/verify.py

Tests:     PASS
Coverage:  PASS      100% statement AND branch, per file, both production modules
Ruff:      PASS
mypy:      PASS      strict
Evidence:  PASS      DEC-0012 structural linter
Overall:   PASS
```

Five gates, which is all `verify.py` defines. Counts are reported from the run in `ISSUE-022`
§8/§9.

**Focused truthfulness audit** over the enrolled non-authoritative records, after normalization:

```text
Does any non-authoritative enrolled record still independently claim
  - the latest review number?              NO
  - a pending review number?               NO
  - the most recent remediation?           NO
  - the current EXP-006 phase?             NO
Explicitly historical statements remain,   AS INTENDED
ISSUE-022 alone owns current volatile status.
```

---

## 11. What this ledger does **not** do

```text
IT DOES NOT CLAIM CLOSURE REVIEW #6 PASSED.  It remains a historical FAIL.
IT DOES NOT CERTIFY COMPLETION.              The implementer may not.
IT DID NOT LAUNCH REVIEW #7.                  Out of scope.
IT DID NOT EDIT A PROTECTED CARD.             INFO-1 is NO CHANGE.
IT DID NOT REWRITE A HISTORICAL LEDGER.       Ledger #5's false claim is
                                              preserved and corrected here.
IT DOES NOT AUTHORIZE A MERGE OR PUSH.
IT DOES NOT AUTHORIZE CLUSTER-004 IMPLEMENTATION, ENC-005 STAGE B,
   OR ANY NEW STAGE-A CARD.
```
