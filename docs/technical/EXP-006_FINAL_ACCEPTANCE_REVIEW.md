# `EXP-006` FINAL ACCEPTANCE REVIEW

> **Preserved verbatim as received.** Seventh independent review of `EXP-006` and the first to
> return `PASS`. Performed against `HEAD` `e169e6d` by a reviewer that wrote none of the work and
> was forbidden to change anything. Historical evidence on the same terms as reviews #1–#6: **not**
> to be rewritten, relabelled or softened.
>
> Recorded in the repository 2026-10-03 because the review was returned as a task result rather
> than written into the tree. Content unaltered; only the transport's HTML entity escaping of `>`,
> `<` and `&` has been undone.
>
> **Verdict: `PASS` — 0 blocking, 5 non-blocking, 1 process recommendation.** Scope was deliberately
> narrow: whether the current-status normalization eliminated duplicated ownership of volatile
> `EXP-006` status without disturbing the repeatedly validated rules implementation.
>
> **An earlier attempt at this review was terminated by an infrastructure rate limit, not by a
> finding.** It had begun examining a possible phase-token remnant in `INVENTORY.md`; that lead was
> passed to this reviewer as a hint only, and it reached its own conclusion on it (see §6, `NB-A`).

## 1. Reviewed HEAD / worktree (established first and again at end — identical)

| Fact | Value |
|---|---|
| WORKTREE | `C:\Users\evanp\source\repos\OD_N_D-cluster-004-exp-006-stage-b` |
| BRANCH | `cluster-004-exp-006-stage-b` ✔ expected |
| HEAD | `e169e6dfb28e9a59a5cd5e4330ab8ee61a7f2a37` ✔ expected `e169e6d` |
| MAIN | `c1bdd5c01e998f961b3851c3d95a225b37fa9cc7` |
| ORIGIN/MAIN | `c3a3e2d9d961a1df8ec3ccad3823929b0a41cac0` |
| STATUS | clean, `-uall` empty, stash empty, before and after |

No worktree collision. `HEAD` did not move during the review.

## 2. Independence statement

I wrote none of this work and modified nothing. All mutations ran as in-memory fixtures against the
module's production predicates; no file in the repository was written, no commit/stash/reset/clean
was issued. The single commit under review is `e169e6d` "fix(exp-006): single ownership of current
status, not synchronization", touching 9 files: `ARCHITECTURE.md`,
`docs/completion-records/INDEX.md`, `docs/rules/INVENTORY.md`, the `CLUSTER-004` record, the plan,
the Pre-Code Gate, `ISSUE-022`, a new closure-review-#6 ledger, and
`tests/rules/exploration/test_exp_006_record_consistency.py`. **No `src/` change.**

## 3. `ISSUE-022` authority — established

`docs/completion-records/ISSUE-022-exp-006-light-and-exploration-resources.md` declares itself the
sole owner in a header banner (lines 3–14) and exercises that ownership in its `STATUS` block (lines
16–50): `STATUS: NOT COMPLETE`, `EXP-006-PHASE: CLOSURE-REVIEW-6-REMEDIATED`, a `REVIEW STAGE
REACHED` table, `OPEN BLOCKERS NONE known`, `FINAL HUMAN ACCEPTANCE NOT GIVEN`, `MERGED NO`,
`PUSHED NO`, and "Whether a further independent review is authorized is recorded here when it is
decided; no other record states it."

Its traceability claim checks out: the ownership model is at `ARCHITECTURE.md` line 537, and the
nearest preceding heading is line 438 `## 15.2` — so the cited "`ARCHITECTURE.md` §15.2" resolves
correctly. **Criterion A holds.**

## 4. Enrolled-record ownership audit

All six enrolled non-authoritative records: reference `ISSUE-022` ✔, zero `VOLATILE_STATUS_FORMS`
offences ✔, zero `STALE_CURRENT_CLAIMS` ✔.

| Record | What it now says | Verdict |
|---|---|---|
| `ARCHITECTURE.md` §15.2 | Blockquote disclaiming ownership + the ownership-model table (`ISSUE-022` AUTHORITATIVE; five records + review artifacts marked "Does NOT own"); then "Durable architectural facts, which this document does own". Authorization sentence rewritten to *"whether a further review is authorized is current status — recorded in `ISSUE-022`, not here."* | Clean |
| `docs/rules/INVENTORY.md` `EXP-006` row | Disclaimer + pointer, then durable facts only (`APPROVED`, `SR-11`, Stage-A accepted, `LOW-3`/`LOW-8` `RESOLVED`, `CLUSTER-004` NOT AUTHORIZED) | Clean except non-blocking NB-A below |
| `CLUSTER-004` record | New §13.1 "Current `EXP-006` status — not owned here"; §13.2 relabels the block with explicit `HISTORICAL` row prefixes; the §4 summary row replaced with "Current status: see ISSUE-022 (§13.1). This record does not own that phase." | Clean |
| `EXP-006_IMPLEMENTATION_PLAN.md` | §1.2 and §18 both replaced with "CURRENT STATUS, INCLUDING THE REVIEW PHASE: see ISSUE-022. This plan does not own that fact." | Clean |
| `EXP-006_PRE_CODE_GATE.md` | New header banner: readiness finding of 2026-10-01 only; "does not own the current review phase, the acceptance state or the open-blocker list, and does not state them." | Clean |
| `docs/completion-records/INDEX.md` | Row rewritten; "most recent: review #4" removed; "Current status … is owned by the record itself; this index does not state it." | Clean |

Phase tokens: the only `EXP-006-PHASE` token in the repository outside immutable historical
artifacts is `ISSUE-022` line 18. `PHASE_TOKEN_RECORDS` and `CURRENT_PHASE` are gone from the test
module (verified programmatically). **Criteria B and C hold.**

Historical chronology is preserved as historical throughout — `CLUSTER-004` §13.2 uses literal
`HISTORICAL` row labels, `ISSUE-022`'s chronology table date-stamps each `FAIL`, and nothing I read
masquerades a dated event as current state.

## 5. Mutations A–E (fixtures, production predicates, repository untouched)

| # | Target | Injection | Expected | Observed |
|---|---|---|---|---|
| A | `CLUSTER-004` | `Review #6 is the latest review.` | FAIL | **FAIL** — 2 patterns fired (`latest (review\|remediation)`, the `review #N … is the …` predicate) ✔ |
| B | `INDEX.md` | `Review #7 is pending.` | FAIL | **FAIL** — 2 patterns fired ✔ |
| C | `ARCHITECTURE.md` | `The most recent remediation is Review #6 remediation.` | FAIL (in scope) | **FAIL** — `most recent (review\|work\|remediation\|independent)` fired ✔ |
| D | all three | `Review #6 returned FAIL on 2026-10-03.` | PASS | **PASS** in `CLUSTER-004`, `INDEX.md` and `ARCHITECTURE.md` ✔ |
| E | `ISSUE-022` | as-is | PASS | **PASS** — not in `NON_AUTHORITATIVE_RECORDS`, and carries a volatile form (`18: EXP-006-PHASE`), which `test_the_authority_may_state_current_status` positively requires ✔ |

Mechanism judgement (§5): the module's claim is narrow and explicit — a closed list of eight
current-state *predicates*, checked line-by-line in six named records, with no skip list and no
exemption mechanism, exempting the authority **by record identity** rather than by marker. It
establishes exactly that. The historical/current split is carried by the patterns themselves, which
is why D passes without a marker bypass — the construct reviews #4 and #5 both blocked on. The three
predicates (`_volatile_status_in`, `_stale_claims_in`, `_split_transcriptions_in`) take no exemption
argument, so the B-6 and BLOCKING-1 defect shapes are structurally unavailable rather than merely
asserted against. **Criterion D holds for the claims the tests make.**

## 6. Actual competing-status search — THE DECIDING QUESTION

**Result: NO.** No enrolled non-authoritative record currently contains prose that functions as an
independent current-status assertion.

I read each record's `EXP-006` status region in full as a reader would, looking specifically for the
four shapes named in the brief:

- **Residual phase tokens / token-like strings** — none outside `ISSUE-022`. Swept the whole
  repository for `EXP-006-PHASE`, `REVIEW-5-REMEDIATED`, `phase token`, `single token`, `pinned by a
  test`: every hit is either in `ISSUE-022`, in an immutable historical artifact, in past-tense
  normalization prose ("This entry **previously** carried a phase token", "This block
  **previously** carried a phase token"), or in unrelated cards (`DEC-0012`/protocol grandfathering,
  a `CHAR` card's "carried as human decisions").
- **Tables / status blocks whose rows imply a sequence position** — the two structured blocks that
  previously did (`CLUSTER-004` §4 summary, plan §1.2 and §18) now carry a pointer line instead of a
  phase row. `CLUSTER-004` §13.2's text block is prefixed `HISTORICAL` on every status-bearing row.
  The plan's §18 gate table row reads `EXP-006 CURRENT STATUS  see ISSUE-022 -- not owned here`.
  None of them lets a reader read off a sequence position.
- **Sentences that date-stamp "current" state** — the surviving dated sentences are event sentences
  (`Slices A–D accepted 2026-10-01/2026-10-03`, `Pre-Code Gate PASS 2026-10-01`, `applied at
  a150837`), which are durable facts, not volatile status. The one place authorization state was
  asserted (`ARCHITECTURE.md`: "A further independent review is not yet authorized") was **removed,
  not reworded** — its replacement explicitly defers the fact to `ISSUE-022`.
- **Anything a reader would treat as the live answer instead of consulting `ISSUE-022`** — the
  retained universal statement "every independent review to date returned `FAIL`, none concerning
  rules logic" appears in several records, but it names no review number, no pending item and no
  phase; it is precisely the sentence the test's own allowed fixture sanctions
  (`test_historical_chronology_remains_allowed`, line 486).

**Closest candidate, examined and rejected as a blocker** — `docs/rules/INVENTORY.md` line 106,
inside the `EXP-006` row's correction-history parenthetical:

> "The review phase is now carried as a single token pinned by a test, and the review history is
> derived from the artifact set rather than restated here."

This is the phase-token remnant the prior attempt was circling, and I reached my own conclusion on
it. It is present-tense and it escapes `VOLATILE_STATUS_FORMS` (confirmed programmatically). But it
does **not** function as a competing current-status assertion: it conveys no phase value, no review
number, nothing pending, and nothing acceptance-related, so no reader can extract the live answer
from it. It sits three sentences *after* that same cell's explicit "**Current `EXP-006` status —
including the review phase — is owned by `ISSUE-022`; this row does not state it**", so a reader is
already pointed at the owner. And it is not strictly false under the new model: the phase *is* now
carried as a single token in one place (`ISSUE-022` line 18), and a test does require a volatile
status form to be present there. What it overstates is "pinned" —
`test_the_authority_may_state_current_status` proves *presence*, not the token's *value*. That makes
it imprecise legacy wording, not an independent status claim. Recorded as **NB-A** below.

## 7. NB-1 — predicate sharing, current behaviour only

**Clean.** Every current regression routes through a production predicate; there is no inline
re-implementation anywhere in the module:

- `_stale_claims_in` — lines 353, 372, 398, 511
- `_volatile_status_in` — lines 441, 458, 470, 489, 502
- `_split_transcriptions_in` — lines 549, 568, 583, 596, 602

Line 398 is the NB-1 defect itself
(`test_injecting_review_3_pending_into_a_live_record_is_detected`), which previously matched inline;
it now calls `_stale_claims_in`. The repository's claim of shared usage is now true, and the
docstring at lines 382–390 records the correction honestly, including that the review-#5 ledger's
claim "was **false for this test**" and that the historical ledger is preserved unaltered rather
than corrected. I judged current behaviour only and did not fault the earlier ledgers.

## 8. INFO-1

**`NO CHANGE` properly recorded, and not reopened.** `ISSUE-022` records it in three places: the
`STATUS` block (lines 43–44, `INFO-1  NO CHANGE (adjudicated; see §12.2)`), §12.2 (`INFO-1 REVIEWED
/ NO PROTECTED-CARD CORRECTION AUTHORIZED / FINDING NOT SUBSTANTIATED`, human decision 2026-10-03),
and the chronology table (line 526). Item 8 of §11 also corrects the prior "open and requires human
adjudication" wording and notes the mis-cited ledger section.

The protected Rule Card is unchanged on that point and on every other:
`docs/rules/exploration/light_and_exploration_resources.md` is blob
`92fd60598d13494211a4ffea3d170450cf59c0be` at `a150837`, `ba4c49e`, `534e0d8` **and** `e169e6d` —
byte-identical.

## 9. Historical preservation (by hash, not by reading)

All twelve immutable artifacts are byte-identical between `534e0d8` and `e169e6d`:

`EXP-006_FINAL_IMPLEMENTATION_REVIEW.md` `bf16f8b` · `_2` `52dccdc` · `_3` `9ca3d1c` · `_4`
`2c1e15f` · `_5` `ad35140` · `EXP-006_CLOSURE_REVIEW_6.md` `7df8670` ·
`EXP-006_REVIEW_REMEDIATION_LEDGER.md` `4426d59` · `_2_` `1be7d47` · `_3_` `6bfabad` · `_4_`
`3ce8e82` · `_5_` `eb22bd4`.

The commit added one artifact (`EXP-006_CLOSURE_REVIEW_6_REMEDIATION_LEDGER.md`) and rewrote none. I
did not read them for current-status agreement and do not fault them for statements true when
written.

## 10. Frozen rules layer (hash/diff only)

`HEAD:src` tree hash is **`d6aaf58785645f3ec8db895f9791851dd68f2c59` at all three baselines** —
`ba4c49e`, `534e0d8`, `e169e6d`. `git diff 534e0d8..HEAD -- src` is empty. Therefore the `EXP-006`
production mechanics, `SR-11`, the ignition matrix, depletion/refuel and the error taxonomy are
provably untouched by this remediation, as is the approved Rule Card blob (§8). The only `tests/`
change is the consistency module. **Criterion E holds.**

## 11. Case-identity drift

**53, no drift.** Enumerated from the approved Rule Card's own tables: **53**. `CASE_DISCHARGE` in
`test_light_and_exploration_resources.py`: **53** entries. Both are pinned by
`test_the_approved_case_total_is_still_what_the_records_claim` and
`test_the_case_ledger_total_matches_the_card`. No case-by-case review performed.

## 12. Documentation practice

**Recorded durably, for `EXP-006`.** `ARCHITECTURE.md` §15.2 (line 537 onward) carries all four
elements the brief asks for: one authoritative owner (the ownership table naming `ISSUE-022`
AUTHORITATIVE and five records + the review artifacts as "Does NOT own"); reference rather than
synchronize ("A non-authoritative record that needs to mention status **references `ISSUE-022`**; it
does not restate the fact"); historical artifacts stay historical ("Neither is ever rewritten to
tidy current documentation"); and durable facts may be repeated (an explicit "**Durable
architectural facts, which this document does own**" section). It also records *why*, including the
"token presence is not prose coherence" diagnosis and the decision to **describe rather than quote**
superseded volatile phrasings so normalization does not reintroduce them.

What is **not** recorded is the generalization: the practice exists only as an `EXP-006`-scoped
block in `ARCHITECTURE.md` §15.2, plus `ISSUE-022` and the closure-review-#6 ledger. Nothing in
`DEVELOPMENT_WORKFLOW.md` (the durable process standard that governs completion records) and no
decision record states the practice project-wide, so the next card's records inherit no rule. Per
§12 that is a **process follow-up recommendation, not a blocker** — PR-1 below.

## 13. Canonical verification

`.venv\Scripts\python.exe scripts\verify.py` — real gates only:

```text
Tests:     PASS   1197 passed in 1.73s
Coverage:  PASS   src/rules 20 files @ 100% per file; core aggregate 100.00% (>=95%)
Ruff:      PASS
mypy:      PASS   no issues in 53 source files
Evidence:  PASS   1 reference packet, 0 Stage-A packets, 12 grandfathered
Overall:   PASS   (exit 0)
```

Consistency tests: `tests/rules/exploration/test_exp_006_record_consistency.py` — **22 passed, 0
failed, 0 skipped**. **Criterion F holds.**

## 14. Command completion

Two commands run, both completed and returned explicitly. `mutate.py` printed its terminal sentinel
`MUTATE.PY COMPLETED NORMALLY` and exited `0`. `scripts\verify.py` printed its summary block and
exited `0`. No `python -` stdin piping was used; the script was written to
`C:\Users\evanp\AppData\Local\Temp\claude\exp006-final\mutate.py` and invoked by explicit path. No
`&&`, no heredocs, no `2>&1` on a native exe.

## 15. Process cleanup (verified by enumeration, not by exit code)

Enumerated `Win32_Process`: **no `python.exe` process present**. Two `pythonw.exe` processes exist —
PIDs 34608 and 42056, created 08:16:59 and 08:17:01, command lines `idlelib\idle.pyw` and
`idlelib.run` — a pre-existing user IDLE session unrelated to this review (created ~11 hours before
it, under `C:\Python314`, not the project venv). Nothing of mine was stranded and nothing was
killed.

## 16. Repository integrity

Re-verified after all work: `HEAD e169e6d…` unchanged, `BRANCH cluster-004-exp-006-stage-b`,
`git status --porcelain -uall` empty, `git stash list` empty, `HEAD:src` still `d6aaf58`. Scratch
confined to `C:\Users\evanp\AppData\Local\Temp\claude\exp006-final\`. The repository is
byte-identical to the state I received.

## 17. Blocking findings

**None.** Taking the five blocking grounds in order: (1) no actual current competing ownership of
volatile status — §6 found none, and the one escaping sentence conveys no status value; (2) no
current normative factual contradiction — the closest candidate reconciles under the new model and
sits beneath an explicit disclaimer and pointer; (3) no overclaim by the status mechanism relative to
the claims it makes — the A–E mutations confirm it does what it says, exempts by record identity, and
has no exemption mechanism to subvert; (4) no change to settled rules/code — `src` tree hash and Rule
Card blob are byte-identical across all three baselines; (5) canonical verification is `PASS` on
every gate.

The deciding question answers **NO**, which is the required result. The normalization did what it set
out to do: it removed the fact from the duplicating records rather than resynchronizing it, and it
replaced token-matching with ownership — which the A/B/C mutations show is enforced and the D/E
mutations show is not over-enforced.

## 18. Non-blocking findings and recommendations

**NB-A — `docs/rules/INVENTORY.md` line 106: stale-flavoured mechanism sentence in the `EXP-006`
row.** "The review phase is now carried as a single token pinned by a test" describes the withdrawn
synchronization design in the present tense. It is the last present-tense "phase token" reference
outside `ISSUE-022` and the historical artifacts; the parallel sentences in `ARCHITECTURE.md` (line
528) and `CLUSTER-004` (line 434) were both converted to past tense ("previously carried") and this
one was not. Not blocking for the reasons in §6. *Recommendation: reword to past tense, matching the
two sibling records, or drop "pinned by a test" — no test pins the token's value.*

**NB-B — the consistency module's own docstring is a generation behind the code it documents.**
Lines 1–47 were not touched by `e169e6d` (verified against the diff). Two consequences: line 40
states "What cannot be derived — the review phase — is carried as one token that every named record
must match", which is the **inverse** of enforced behaviour (`EXP-006-PHASE` is now a *forbidden*
form in all six non-authoritative records, so a record following the docstring would fail the suite),
and is contradicted 29 lines later by the module's own comment "The phase-token design is
WITHDRAWN"; and lines 3–5 state "Four independent final implementation reviews have now run", where
six reviews now exist. I weighed this against blocking ground (3) and against the project's own
calibration: closure review #6 graded a false claim about the mechanism's own coverage as `NB-1`,
reserving `BLOCKING` for records independently asserting status. It is the same shape, so
**non-blocking** — but it is the highest-priority item here, because this file's own docstring (lines
26–27) names exactly this defect: "A guard that enumerates six conditions and can only evaluate two
is worse than no guard: it reports protection it does not provide." *Recommendation: bring the
docstring to the current generation; it is the one surviving piece of review-#4-era self-description
in the normalized surface.*

**NB-C — `test_the_review_artifact_set_is_internally_consistent` does not cover the closure-review
artifacts.** Its docstring says "Every persisted review artifact must have a paired remediation
ledger", but it globs only `EXP-006_FINAL_IMPLEMENTATION_REVIEW*.md` (5) and
`EXP-006_REVIEW*_REMEDIATION_LEDGER.md` (5) — `EXP-006_CLOSURE_REVIEW_6.md` and
`EXP-006_CLOSURE_REVIEW_6_REMEDIATION_LEDGER.md` match neither pattern, so neither the pairing count
nor the `ISSUE-022` §3 listing check sees them. The never-scanned glob set
(`HISTORICAL_ARTIFACT_GLOBS`) *was* updated to include `EXP-006_CLOSURE_REVIEW_*.md` this pass; the
pairing globs were not. No present defect: `ISSUE-022` §3 lines 173–174 do list both closure
artifacts. A latent gap only. *Recommendation: add the closure patterns to the pairing globs, or
narrow the docstring to "every final-implementation review artifact".*

**NB-D — `ARCHITECTURE.md`'s artifact-set enumeration omits the closure ledger pattern.** The
three-glob block added at §15.2 lists `…FINAL_IMPLEMENTATION_REVIEW*.md`, `…CLOSURE_REVIEW_*.md` and
`…REVIEW*_REMEDIATION_LEDGER.md`; the closure review's own ledger is matched by none of them, so the
block under-enumerates the set it defines as "the review history" by one file. Same root cause as
NB-C.

**NB-E — trivia.** The plan's §1.2 block says "Every independent final review returned FAIL" where
`ARCHITECTURE.md` and `INDEX.md` say "to date"; the universal form becomes false the moment a review
passes. And `ISSUE-022` §11 has two consecutive list items numbered `8.` (renders correctly as 8/9 in
Markdown; source-level only). Neither affects any claim.

**PR-1 — process follow-up (per §12).** The single-ownership practice is recorded durably but only
`EXP-006`-scoped, in `ARCHITECTURE.md` §15.2. Nothing in `DEVELOPMENT_WORKFLOW.md` or a decision
record carries it forward, so `ENC-005` and the next completion record inherit no rule and the
pattern that produced six consecutive `FAIL` reviews can recur under a different ID. Recommend a
human-directed addition to `DEVELOPMENT_WORKFLOW.md` §5 (or a short `DEC-`) stating the four elements
generally: volatile current status has exactly one authoritative owner; other records reference it
rather than synchronizing duplicates; historical artifacts stay historical and are never rewritten to
tidy current documentation; durable facts may be repeated. I am not authorized to draft or apply it
and have not.

## 19. Verdict

All six acceptance criteria hold: **A** `ISSUE-022` is the sole designated and exercising owner; **B**
all six enrolled records reference it and none maintains a review number, pending review, latest
remediation or acceptance phase; **C** historical chronology is explicitly labelled historical and
does not masquerade as current state; **D** the tests truthfully enforce their narrow claims,
confirmed by mutations A–E; **E** `src` tree hash and Rule Card blob are byte-identical across
`ba4c49e`/`534e0d8`/`e169e6d`; **F** canonical verification `PASS` on every gate. The deciding
question in §6 answers **NO**. Five non-blocking items and one process recommendation remain, none of
which establishes competing ownership, a current normative contradiction, mechanism overclaim, an
unauthorized rules change, or a verification failure.

**EXP-006 FINAL ACCEPTANCE REVIEW: PASS**
