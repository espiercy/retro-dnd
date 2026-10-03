# `EXP-006` — Remediation Ledger for Independent Final Review #5

```text
REVIEW REMEDIATED    docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW_5.md
REVIEW VERDICT       FAIL  -- 3 BLOCKING, 6 non-blocking/informational
REVIEWED HEAD        e5caf121ee6642191ffaa65535e6b2daf406f581
ARTIFACT COMMIT      e10ddec6ede2696fe24a947a3fdba45d4b889f1c
REMEDIATION DATE     2026-10-03
AUTHORIZED BY        human project owner; Review #5 blocking-finding
                     remediation ONLY. Review #6 NOT launched.
WORKTREE             OD_N_D-cluster-004-exp-006-stage-b
BRANCH               cluster-004-exp-006-stage-b   (unmerged, unpushed)
CERTIFICATION        NONE. Review #5 remains a historical FAIL. This ledger
                     does not and cannot claim it passed.
```

> **Reviews #1–#5 and remediation ledgers #1–#4 are preserved unaltered.** Review #5 is not
> relabelled, edited or softened.

---

## 1. Rules, production behaviour and guard philosophy are FROZEN

Review #5 again established — and this time **proved by hash** — that the substantive layers are
clean:

```text
rules / mechanics      conformant
state-space            conformant
error taxonomy         conformant
SR-11                  conformant
CHAR-004 seam          conformant
guard claims           appropriately narrow
src/ tree hash         d6aaf58785645f3ec8db895f9791851dd68f2c59
                       BYTE-IDENTICAL across a150837, afd440e, e5caf12
approved Rule Card     byte-identical
```

Accordingly this remediation changed **none** of: production rules mechanics, Stage-A evidence,
Rule Card mechanics, `SR-11`, the ignition matrix, depletion/refuel behaviour, the error taxonomy,
the `CHAR-004` seam, architecture-guard breadth, or the disclosed non-blocking Python limitations.

**The one exception the authorization permits, and the only code touched: the broken consistency-test
logic itself.**

---

## 2. The three blocking findings

### `BLOCKING-1` — the consistency-test bypass is DELETED

| | |
|---|---|
| **Source** | `tests/rules/exploration/test_exp_006_record_consistency.py`, the split-duplication check |
| **Original defect** | The predicate excused any line containing one of `("withdrawn", "superseded", "previously", "B-1", "B-2")`. Three of those are **verbatim members of the `HISTORICAL_MARKERS` tuple the review-#4 ledger claimed was "removed entirely"**; the other two are merely the finding IDs that remediation prose in these documents naturally cites. So the review-#4 remediation did not remove the skip architecture — it **relocated** it into the same module as a function-local tuple. The tripwire meant to forbid exactly this checked three *global* names against `globals()` and structurally could not see a local. Review #5 demonstrated the consequence: the exact withdrawn `23/5/23/1/1` split, re-transcribed into the **approved implementation plan** on a line citing `` `B-1` ``, left the full 123-test suite green. Types **D** and **E**. |
| **Correction** | **The bypass is deleted outright** — no replacement marker list, no cleverer exemption. Per the human direction: *a live record does not become exempt from truthfulness because its line contains a historical-sounding word.* Historical artifacts are already excluded structurally, by scanning only named live records. A current record that must discuss an obsolete claim has to word it so that it does not reproduce the stale assertion as current normative truth. |
| **Verification** | Four regressions, §3 below, A–D, all against the **production predicate** rather than a reimplementation. Proven safe before being applied: review #5 showed, and I independently reproduced on a scratch copy, that deleting the line keeps the real documents green **and** catches the injection. |

### `BLOCKING-1` companion — the false tripwire is REMOVED, not replaced

The assertion `not any(name in globals() for name in ("HISTORICAL_MARKERS", …))` claimed to prove
no skip list existed. It proved nothing: the skip list was function-local. Per the human direction
the remedy is **structural simplification, not a second mechanism to police the first**:

```text
BEFORE   a skip mechanism, plus a test asserting the skip mechanism is absent
AFTER    no skip mechanism -- the predicates take no exemption at all
```

The indirect assertion is **deleted** (it existed only to certify an absence indirectly). The
remaining configuration checks are properties that can genuinely be verified — no claim subsumed by
another, and no historical artifact in the scanned set. The behaviour that matters is proved
**directly**, by §3.

Also corrected here, review-#5 `NB-3`: the regression tests previously re-implemented the match
inline against a fixture they had just written, which made them tautological — they would have kept
passing if the production check were disarmed, the very regression they exist to prevent. Both
predicates are now named functions (`_stale_claims_in`, `_split_transcriptions_in`) used by **both**
the live-record checks and the regressions, so a regression genuinely exercises production code.

### `BLOCKING-2` — `ARCHITECTURE.md` self-contradiction and stale prose counts

| | |
|---|---|
| **Original defect** | Three parts. (1) `:529` said *"A **fourth** independent review is **not yet authorized**"* four lines below `:525` recording that review's `FAIL` — both present tense, neither marked historical. The identical sentence had been corrected in the plan and the `CLUSTER-004` record in the previous pass and **missed here**. (2) `:521` retained *"every finding in **all three**"* and *"**All three** remediations are recorded (…)"*, omitting ledger #4 — **inside the very sentence announcing that prose counts had been abandoned because they go stale**. (3) `ISSUE-022` claimed `test_the_review_artifact_set_is_internally_consistent` checks "that no live record asserts a contradicting prose count"; it does not. |
| **Correction** | (1) Reworded to *"A **further** independent review is not yet authorized"* — phrased so it never needs renumbering — with the stale version quoted and attributed. (2) **The prose counts and the partial inline ledger list are removed, not incremented to "four".** The entry now points at the artifact *globs* and states explicitly that the artifact set **is** the review history, naming both prior failures of this exact sentence. "every finding in all three" → "every finding in every review". (3) The unsupported conjunct is **dropped** from `ISSUE-022`, which now describes only what the test does — pairing, plus presence in §3 — with the gap and the demonstration recorded. **The claim was narrowed to the mechanism; the mechanism was not broadened to preserve the claim.** |
| **Verification** | `test_no_live_record_asserts_a_stale_claim` (no exemptions) over all seven named live records; the focused truthfulness pass in §6; and the phase token, now `REVIEW-5-REMEDIATED`, required in all five `PHASE_TOKEN_RECORDS`. |

### `BLOCKING-3` — the dangling test citation

| | |
|---|---|
| **Original defect** | `CLUSTER-004`'s self-declared *"**Live next step.** This block is **status**, not history"* cited `test_live_status_records_agree_on_the_review_phase`: **1 citation, 0 definitions.** The review-#4 remediation renamed the test and left the cross-reference. False traceability in a block asserting it is current status. |
| **Correction** | Repointed to the existing `test_live_records_carry_the_current_phase_token`. **The test was not renamed to suit the document** — the current name is not defective. The stale citation is recorded in place. |
| **Verification** | New `test_every_test_name_cited_in_a_live_record_exists`: harvests `test_*` identifiers from the **named live records only** and resolves them against the test functions actually defined in the two `EXP-006` test modules, with a non-vacuity anchor on the discovered set. **Deliberately narrow — it is not a generic documentation parser** and validates no other citation kind, per the human direction. |

---

## 3. `BLOCKING-1` regressions — the four required cases

All four exercise `_split_transcriptions_in`, the production predicate, on `tmp_path` fixtures. **No
historical repository artifact is used or altered.**

| § | Case | Expected | Test |
|---|---|---|---|
| **A** | the withdrawn split, plainly stated | **FAIL** | `test_a_stale_split_is_caught` |
| **B** | the same split, line contains `withdrawn` | **FAIL** | `test_a_stale_split_containing_withdrawn_is_still_caught` |
| **C** | the same split, line cites `` `B-1` `` | **FAIL** | `test_a_stale_split_citing_b_1_is_still_caught` |
| **D** | the real current plan and gate | **PASS** | `test_the_real_split_owning_records_are_clean` |

The checker no longer cares whether a live stale assertion carries a historical-sounding marker.
Results in §7.

---

## 4. `INFO-1` — human adjudication: **NO CHANGE**

```text
INFO-1   REVIEWED
         NO PROTECTED-CARD CORRECTION AUTHORIZED
         FINDING NOT SUBSTANTIATED AS A RULES/DOCUMENTATION DEFECT
```

**Human decision, 2026-10-03.** Review #5 independently confirmed that the earlier STOP was
justified. The reasons, as adjudicated:

- the nearby seven entries are **not** seven members of one mapped-RC-silence category;
- some are **governance items** (rations ownership; starvation causation having no Rule ID — which
  the card itself calls *"a standing open governance issue"*; the unowned complete-darkness
  predicate);
- the card contains a **genuine separate six-item list** (`## Rules Cyclopedia Leaves Undefined /
  Ambiguous`, a different set — it substitutes the timetrack question and water consumption, and
  excludes rations, starvation and the complete-darkness predicate);
- therefore **review #4 did not establish that `"six"` was an objective typo.**

**The protected approved Rule Card is not edited.** No mechanic, provenance classification, case ID,
silence disposition, approval state or wording changed. `git diff` over `docs/rules/exploration/`
across this remediation is empty.

---

## 5. The six non-blocking / informational findings — dispositions unchanged

Preserved as non-blocking. **None was turned into remediation work**, and no work was restarted on
theoretical Python mechanisms outside explicitly narrow guard claims.

| # | Finding | Disposition |
|---|---|---|
| **NB-1** | The stale-claim check is **per line**, so a forbidden phrase wrapped across a line break is unseen; `PRE_CODE_GATE.md` currently contains `"23 of the 53"` split across a break and passes. | **Unchanged — limitation, accurately disclosed.** The occurrence is a legitimate quotation of removed text. Review #5 flagged it because line-wrap sensitivity is the pressure that produced the original skip list; the answer is **not** a skip list, and not a multi-line matcher either. Recorded. |
| **NB-2** | The three `LOW-3`/`LOW-8` entries in `STALE_CURRENT_CLAIMS` match nothing in the pre-remediation tree, because backticks and emphasis broke the substring match in every real instance. | **Unchanged — limitation, disclosed in scope.** The module docstring scopes this to literal phrasings. The resolved state is independently protected by the atomic phase token (review #5 demonstrated P1/P2 catch). **One correction to the record:** ledger #4's claim that the claim set "now covers… the open-findings wording" was not borne out, and is not repeated here. |
| **NB-3** | The regression tests re-implemented the predicate inline and were tautological. | **Corrected** — see §2's `BLOCKING-1` companion. This was the one non-blocking finding containing a real defect in a verification mechanism, so it was fixed alongside `BLOCKING-1`. |
| **NB-4** | `ISSUE-022` §11 has two items numbered `8.`; markdown auto-renumbers so the rendered list is correct. | **Unchanged — informational, raw-source only.** |
| **NB-5** | `ISSUE-022` §11 item 8 cites "the review-#4 remediation ledger **§INFO-1**"; that ledger's section is numbered **§4**, titled `INFO-1`. | **Unchanged — informational; trivially resolvable by a reader.** |
| **INFO-2** | Review #5 credited the previous pass for disclosing that its own new test caught two of its own misses on first run, rather than claiming a clean pass. | **No action — informational.** |

`INFO-1` is adjudicated separately at §4.

---

## 6. Focused current-record truthfulness pass

Inspected **only** the named live/current records affected by this remediation. Historical `FAIL`
artifacts were **not** scanned for obsolete chronology — they preserve it deliberately.

```text
"Review #4 not authorized"          0 occurrences
"Review #5 not occurred"            0
"Review #5 pending"                 0
"all three remediation ledgers"     0
"all four remediation ledgers"      0   (deliberately NOT introduced)
stale phase token REVIEW-4-...      0 in the five PHASE_TOKEN_RECORDS
dangling test citations             0
```

Lists and globs are preferred over duplicated prose counts throughout: no record states how many
reviews or ledgers exist.

---

## 7. Verification

```text
uv run python scripts/verify.py

Tests:     PASS
Coverage:  PASS      100% statement AND branch, per file, both production modules
Ruff:      PASS
mypy:      PASS      strict
Evidence:  PASS      DEC-0012 structural linter
Overall:   PASS
```

Five gates, which is all `verify.py` defines. Counts and coverage are reported from the actual run
in `ISSUE-022` §8/§9 rather than transcribed here.

**`BLOCKING-1` regression results: A FAIL · B FAIL · C FAIL · D PASS** — the stale split is caught
plainly, caught when the line says `withdrawn`, caught when the line cites `B-1`, and the real
records are clean. **The corrected `CLUSTER-004` citation resolves**, asserted mechanically.

**Preservation confirmed:** `src/` byte-identical to the reviewed HEAD; approved Rule Cards
unchanged; `SR-11` unchanged; reviews #1–#5 and ledgers #1–#4 byte-identical; no Stage-A research.

---

## 8. One observation about this remediation's own mechanism

Recorded because it is the class of defect five reviews have found, and because it bit this pass.

`test_the_review_artifact_set_is_internally_consistent` requires every review artifact to have a
paired ledger. That is a good property — but it **couples artifact persistence to ledger existence**,
so the authorization's own instruction to *"persist the review artifact and commit that artifact
alone before remediation"* necessarily produces a **transiently red commit** (`e10ddec`: five
reviews, four ledgers). It went green when ledger #5 landed in this commit.

This is not presented as resolved. It is a genuine tension between two correct rules — commit the
failure record first, and keep the artifact set paired — and whichever way it is settled should be a
human decision rather than an implementer's convenience.

---

## 9. What this ledger does **not** do

```text
IT DOES NOT CLAIM REVIEW #5 PASSED.  It remains a historical FAIL.
IT DOES NOT CERTIFY COMPLETION.      The implementer may not.
IT DID NOT LAUNCH REVIEW #6.         Out of scope.
IT DID NOT WIDEN ANY GUARD.          Rules and guard philosophy frozen.
IT DID NOT EDIT A PROTECTED CARD.    INFO-1 adjudicated as NO CHANGE.
IT DOES NOT AUTHORIZE A MERGE OR PUSH.
IT DOES NOT AUTHORIZE CLUSTER-004 IMPLEMENTATION, ENC-005 STAGE B,
   OR ANY NEW STAGE-A CARD.
```
