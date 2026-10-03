# `EXP-006` INDEPENDENT FINAL REVIEW #5

> **Preserved verbatim as received.** Fifth independent review, performed against `HEAD` `e5caf12`
> by a reviewer that wrote none of the work and was forbidden to change anything. Historical
> evidence on the same terms as reviews #1–#4: **not** to be rewritten, relabelled or softened.
>
> Recorded in the repository 2026-10-03 because the review was returned as a task result rather
> than written into the tree. Content unaltered; only the transport's HTML entity escaping of `>`
> and `<` has been undone.
>
> **Verdict: `FAIL` — 3 BLOCKING, 6 non-blocking/informational.** Deliberately narrower than
> reviews #1–#4: its purpose was to determine whether the review-#4 documentation-consistency
> failure mode had actually been eliminated. It had not. The rules, state-space, error-taxonomy,
> `SR-11`, `CHAR-004`-seam and guard-claim layers were again found conformant, and the production
> tree provably frozen.

## 1. Reviewed HEAD

| | |
|---|---|
| **WORKTREE** | `C:/Users/evanp/source/repos/OD_N_D-cluster-004-exp-006-stage-b` |
| **BRANCH** | `cluster-004-exp-006-stage-b` ✔ expected |
| **HEAD** | `e5caf121ee6642191ffaa65535e6b2daf406f581` ✔ expected |
| **MAIN** | `c1bdd5c01e998f961b3851c3d95a225b37fa9cc7` |
| **ORIGIN/MAIN** | `c3a3e2d9d961a1df8ec3ccad3823929b0a41cac0` |
| **STATUS** | clean (no tracked changes, no untracked files) |

No worktree collision. Other worktrees (`OD_N_D`, `OD_N_D-main-integration`) both sit at `c1bdd5c`
and were not touched.

## 2. Independence statement

I wrote none of this work and fixed nothing. I read `EXP-006_FINAL_IMPLEMENTATION_REVIEW_4.md`
directly for `B-1`…`B-6` and did **not** rely on `EXP-006_REVIEW_4_REMEDIATION_LEDGER.md`'s
description of those findings. Every ledger, commit-message and `ISSUE-022` assertion was treated as
a claim to verify. All mutation work ran on a scratch copy at
`C:\Users\evanp\AppData\Local\Temp\claude\exp006-rev5\copy`; the real worktree was never mutated. No
Rules Cyclopedia research was performed and Stage A was not reopened.

Where I formed a hypothesis and the evidence refuted it, I report that: I predicted the configured
claim `"Two independent final implementation reviews"` could not match the `B-4` defect text because
review #4 rendered it as `**Two**`. Mechanical scan of the `afd440e` blob showed the source text was
unbolded and the claim **does** fire. I discarded that hypothesis.

## 3. Artifacts reviewed

`EXP-006_FINAL_IMPLEMENTATION_REVIEW_4.md`; `EXP-006_REVIEW_4_REMEDIATION_LEDGER.md`;
`EXP-006_IMPLEMENTATION_PLAN.md`; `EXP-006_PRE_CODE_GATE.md`;
`ISSUE-022-exp-006-light-and-exploration-resources.md`; `docs/completion-records/INDEX.md`;
`docs/rules/INVENTORY.md`; `docs/rules/clusters/CLUSTER-004-equipment-resources-and-evasion.md` and
`-BOUNDARY-CORRECTION.md`; `ARCHITECTURE.md` §15.2; the approved Rule Card
`docs/rules/exploration/light_and_exploration_resources.md`;
`tests/rules/exploration/test_exp_006_record_consistency.py` (full source) and
`test_light_and_exploration_resources.py` (`CASE_DISCHARGE`, guard docstrings);
`src/rules/exploration/{light_and_exploration_resources,errors}.py` (via tree hash);
`scripts/verify.py` output; the `afd440e` blobs of all seven live records.

## 4. `B-1`…`B-6` closure table

| | Original defect (read from review #4 directly) | Current repository state | Closed |
|---|---|---|---|
| **B-1** | Plan §12 republished the **withdrawn** `23/5/23/1/1` split (13 of 53 rows misclassified) under *"computed, not transcribed… cannot drift from the code without a red test"*; §12.1's "API shape" list stale | §12 heading is now "**Where the split lives — deliberately NOT here**"; the table is **deleted, not renumbered**; the false protection claim is named; §12.1's enumeration removed. My independent scan of plan+gate for any `\d{1,3}` beside a kind word found numeric splits **only** inside explicitly marked withdrawn block-quotes (plan `:460-461`, `:477-478`; gate `:250-251`, `:257`, `:275`) | **YES** |
| **B-2** | Gate §6 asserted plan §12 was protected by the count assertion; `:267` published "**23** of the 53" | Both removed. Gate now states it "**does not own the post-implementation category split**, and asserts no protection over any other document". The "23 of the 53" figure survives only as a quoted-as-removed fragment | **YES** |
| **B-3** | Five live records said `LOW-3`/`LOW-8` "remain OPEN" at the commit that resolved them | All five now state `RESOLVED`, naming `a150837`. Semantic regex sweep (emphasis- and wrap-insensitive) over the 7 live records: **0 occurrences** of all three `B-3` defect patterns, down from 3 at `afd440e`. No `LOW-3`/`LOW-8`-open claim remains anywhere current | **YES** |
| **B-4** | `ISSUE-022` said "**Two**" reviews against its own `STATUS` block; listed review #3 "pending"; "**Both**" artifacts; §5 item 3 omitted reviews #3/#4 + ledgers #3/#4; false "amended **only** by the two corrections… **not** touched by either remediation pass" | All corrected. §5 item 3 now lists 4 reviews + 4 ledgers, paired, plus `CHAR-005`; the "amended only" absolute replaced with the accurate rule naming all three authorized amendments; chronology extended through ledger #4; §11 item 1 rewritten with the correction noted | **YES** |
| **B-5** | `INDEX.md:28` said "review #3 pending, separately authorized" | Corrected to "most recent: review #4 `FAIL`, remediation current. **Final human acceptance pending.**" and `INDEX.md` is now **enrolled** in `LIVE_RECORDS` (closing `NB-6`) | **YES** |
| **B-6** | The stale-wording guard skipped any line containing a `HISTORICAL_MARKERS` entry before testing `SUPERSEDED_PHASE_CLAIMS`; `"review #2"` was in **both** lists, making 4 of 6 claims unreachable | **The specific instance is closed** — the `HISTORICAL_MARKERS` global is gone, historical artifacts are never scanned, and I demonstrated all five named-record injections now fail (C1–C5). **But the architecture it identified is present again in the same module and demonstrably cancels an intended check** — see BLOCKING-1 | **Specific defect YES; the architecture the remediation claims to have eliminated, NO** |

## 5. Derived case reconciliation and split

Enumerated independently from the approved Rule Card's table-row anchors and from `CASE_DISCHARGE`
via AST — not read from any planning or gate document, and not taken from the test's own literals:

```text
card table-row L-tokens      53 rows, 53 distinct, 0 duplicate anchors
L-tokens anywhere in card    53  (0 referenced but not a row anchor — no orphans)
CASE_DISCHARGE entries       53  (0 card-only, 0 ledger-only, 0 duplicate discharge strings)

DERIVED SPLIT (from CASE_DISCHARGE prefixes)
  behavior    22   L1 L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L15a L17 L18 L19a L20 L21 L22 L27 L28 L34
  invariant    5   L12a L19 L23 L24 L26
  surface     11   L15b L16 L25 L32 L33 L35 L38 L39 L40 L41 L42
  reviewed    14   L13 L14 L15 L19b L29 L30 L31 L36 L37 L37a L43 L44 L45 L46
  routed       1   L47
  total       53     (0 unrecognised kinds)
```

Identical to review #4's independent derivation. **No current normative planning or gate document
republishes a hand-maintained category split as authoritative** — the §5 requirement is met in
substance: both documents now *refer to* `CASE_DISCHARGE` as the single source rather than
duplicating mutable numbers, and the only surviving numeric splits are inside explicitly marked
withdrawn quotations. The remediation chose **removal over renumbering**, which is the correct
remedy.

The *guard* that is supposed to keep it that way is a different matter — BLOCKING-1.

## 6. Current review/status records

Swept repo-wide for `review #N pending`, `awaiting review`, `LOW-3`/`LOW-8` open, and claims that
review #4 has not occurred, then triaged historical from current.

**Clean:** no current record says `review #2 pending`, `review #3 pending`, `LOW-3 open` or
`LOW-8 open`. All five `PHASE_TOKEN_RECORDS` carry `EXP-006-PHASE: REVIEW-4-REMEDIATED`. Historical
artifacts legitimately retain `REVIEW-3-REMEDIATED` (review #4, ledger #3) — not flagged.
`docs/rules/evidence/EXP-006-evidence-remediated.md:16`'s "pending fifth independent review" refers
to the Stage-A `DEC-0010` completeness-review series, a different sequence, and is historical — not
flagged.

**Not clean:** `ARCHITECTURE.md:529` states review #4 has not been authorized, four lines below the
paragraph recording its `FAIL` — BLOCKING-2.

## 7. `ISSUE-022`

Chronology is current through the review-#4 remediation (rows added for review #3, the
`LOW-3`/`LOW-8` adjudication, review #4 and ledger #4; terminal rows are "Further independent
review — not yet authorized" and "Human acceptance and merge — **pending**"). No obsolete review
count: the prose count is replaced by the **persisted artifact set**, enumerated review↔ledger
paired in §5 item 3, with the omission self-documented. No "review #3 pending". No false "only
amended by…" statement — replaced with the accurate rule and all three authorized amendments named.
`STATUS: NOT COMPLETE`; human acceptance named as a separate act; final completion **not** claimed
prematurely. Artifact enumeration (my preference over prose counts) is complete: 4 reviews + 4
ledgers on disk, all 8 listed.

One overclaim inside it feeds BLOCKING-2: the new block asserts
`test_the_review_artifact_set_is_internally_consistent` checks "that every review artifact has a
paired remediation ledger **and that no live record asserts a contradicting prose count**." The test
does the first; it does **nothing** resembling the second.

One cosmetic defect: §11 contains **two items numbered `8.`** (the new `INFO-1` item and the
pre-existing "Not merged and not pushed"). Markdown auto-renumbers on render, so the rendered list
reads 1–9 correctly. Informational only.

## 8. INDEX / inventory / cluster / architecture phase agreement

All four agree on the current phase, and **no record lags behind the review-#4 remediation**:

| Record | Phase statement |
|---|---|
| `ARCHITECTURE.md` | `EXP-006-PHASE: REVIEW-4-REMEDIATED`; review #4 `FAIL` recorded; `LOW-3`/`LOW-8` `RESOLVED` |
| `docs/rules/INVENTORY.md` | `EXP-006-PHASE: REVIEW-4-REMEDIATED`; `LOW-3`/`LOW-8` `RESOLVED`; not complete pending human acceptance |
| `CLUSTER-004-…evasion.md` | `EXP-006-PHASE: REVIEW-4-REMEDIATED` (twice: summary block + live status block); "A **further** independent review is NOT YET AUTHORIZED" — correctly generalised from "A FOURTH" |
| `docs/completion-records/INDEX.md` | "most recent: review #4 `FAIL`, remediation current. **Final human acceptance pending.**" |

`CLUSTER-004-BOUNDARY-CORRECTION.md` carries no `EXP-006` implementation or review status —
correctly not enrolled. But `ARCHITECTURE.md` contradicts itself *within* its own `EXP-006` block
(BLOCKING-2), and the `CLUSTER-004` live block cites a test that no longer exists (BLOCKING-3).

## 9. Consistency-test audit — claim → mechanism → does it check that claim

### A. Named live records — CLEAN

`LIVE_RECORDS` has 7 entries, `PHASE_TOKEN_RECORDS` 5 (a documented subset, asserted as a subset);
`HISTORICAL_ARTIFACTS` 8. All 20 configured paths exist. The configuration-non-emptiness self-check
is real. **`docs/completion-records/INDEX.md` — review #4's `NB-6` omission — is now enrolled**, and
I confirmed its enrolment is live by injection (C3). I swept every `.md` file mentioning `EXP-006`
outside the enrolled set: the remainder are the approved card (read separately for the case total),
Stage-A evidence packets, other clusters' records, boundary proposals, and unrelated completion
records. **No obvious current `EXP-006` status record is accidentally omitted.**

### B. Historical records — the specific defect is closed, the architecture is not

Historical artifacts are never parsed as current-state records; the never-scanned property is itself
asserted (`HISTORICAL_ARTIFACTS ∩ LIVE_RECORDS = ∅`), and C6 confirms a forbidden phrase appended to
review #4 does **not** fail the suite. No skip exceptions are needed for historical prose. That part
is a genuine improvement.

**But a skip-list architecture capable of cancelling an intended current check is present**, at
`test_exp_006_record_consistency.py:307-308`:

```python
if any(m in line for m in ("withdrawn", "superseded", "previously", "B-1", "B-2")):
    continue  # an explicitly-marked historical quotation
```

Three of those five markers — `"withdrawn"`, `"superseded"`, `"previously"` — are **verbatim entries
from the `HISTORICAL_MARKERS` tuple the ledger says was removed entirely** (confirmed against the
`afd440e` blob, lines 85-97). The tripwire that is supposed to prevent exactly this checks three
*global names* against `globals()` and cannot see a function-local tuple. See BLOCKING-1.

### C. Forbidden stale claims — mechanically demonstrated, CAUGHT

Every mutation below ran against the scratch copy; `expect` was set before running.

| | Mutation | Expect | Result |
|---|---|---|---|
| C1 | `"review #2 pending"` → `ARCHITECTURE.md` | FAIL | **FAIL (caught)** — 1 failed, 10 passed |
| C2 | `"review #3 pending"` → `ARCHITECTURE.md` | FAIL | **FAIL (caught)** |
| C3 | `"review #2 pending"` → `INDEX.md` (newly enrolled) | FAIL | **FAIL (caught)** |
| C4 | `"review #3 pending"` → `ISSUE-022` | FAIL | **FAIL (caught)** |
| C5 | `"review #3 pending"` → `PRE_CODE_GATE` (live, non-phase) | FAIL | **FAIL (caught)** |
| C6 | `"review #2 pending"` → review #4 (historical) | PASS | **PASS (green)** — correctly not scanned |
| P1 | remove the phase token from `ARCHITECTURE.md` | FAIL | **FAIL (caught)** |
| P2 | stale token `REVIEW-3-REMEDIATED` in `ARCHITECTURE.md` | FAIL | **FAIL (caught)** |

Review #4's `B-6` escape is genuinely closed. I additionally validated the claim set
**retrospectively** by running the current predicate against the `afd440e` (pre-remediation) copies
of all seven live records: **4 of 15 configured claims fire**, at four distinct records —
`review #3 pending` (`INDEX.md:28`, = `B-5`), `a second independent review is pending`
(`INVENTORY.md:106`), `Two independent final implementation reviews` (`ISSUE-022:301`, = `B-4`),
`23 of the 53` (`PRE_CODE_GATE:267`, = `B-2`). Against current HEAD: 0 of 15. That is real
retrospective validation, and better than I expected.

### D. `LOW-3` / `LOW-8` — the literal string is held; the historical wording is not

| | Mutation | Result |
|---|---|---|
| D1 | literal configured `"LOW-3 and LOW-8 remain open"` → `INVENTORY.md` | **FAIL (caught)** |
| D2 | the **actual** `B-3` wording, `INVENTORY` form: `` its `LOW-3` and `LOW-8` remain **open pending human adjudication** `` | **PASS (green)** |
| D3 | the **actual** `B-3` wording, `ARCHITECTURE` form: `**Two review-#3 findings remain open** and require human adjudication` | **PASS (green)** |
| D4 | the **actual** `B-3` wording, `CLUSTER-004` form: `Two review-#3 findings remain OPEN and require human adjudication` | **PASS (green)** |

The three `LOW-3`/`LOW-8` entries in `STALE_CURRENT_CLAIMS` fire on **nothing** in the
pre-remediation tree, although the defect was present in three records there — backticks and
markdown emphasis break the substring match in every real instance. The module docstring does
disclose that this is a literal-phrase check and "not a generic documentation linter", so under its
stated scope this is a **limitation, not an escape**; `LOW-3`/`LOW-8`'s resolved state is
independently protected by the atomic phase token (P1/P2 caught). Reported as NB-2, not blocking.
Ledger line 200's claim that the claim set "now covers… the open-findings wording" is nonetheless
not borne out.

### E. Case-total and split drift — total protected, non-duplication NOT protected

| | Mutation | Result |
|---|---|---|
| E1 | delete a `CASE_DISCHARGE` row | **FAIL (caught)** — card/ledger total mismatch |
| E5 | flip `L47` `routed` → `behavior` | **FAIL (caught)** by the sibling module |
| E5b | flip `L16` `surface` → `reviewed` (split moves, total constant) | **FAIL (caught)** |
| E6 | delete case row `L28` from the **approved Rule Card** | **FAIL (caught)** — 3 tests |
| E2 | bolded split re-transcribed into the plan, no marker | **FAIL (caught)** |
| **E3** | **unbolded** split table re-transcribed into the plan | **PASS (green)** |
| **E4** | bolded split into the plan, line cites `` `B-1` `` | **PASS (green)** |
| **E4b** | bolded split into the plan, line says `previously` | **PASS (green)** |
| **E4c** | bolded split into the **gate**, line cites `` `B-2` `` | **PASS (green)** |
| **E4d** | **the exact withdrawn `23/5/23/1/1` split** into the plan, line cites `` `B-1` `` | **PASS (green)** |
| **E7** | three-digit bolded counts (`**011**`, `**014**`) | **PASS (green)** |

Case **total** and per-case **classification** are genuinely machine-held, including against the
approved card. **Non-duplication is not.** E4d is the literal `B-1` defect — the withdrawn split,
with wrong numbers, in the approved plan — and the full 123-test EXP-006 set stays green.

**I then tested whether the hole buys anything.** Removing the marker-skip line from the scratch
copy:

```text
baseline, skip list present                        -> green (11 passed)
skip list REMOVED, documents unchanged             -> green (11 passed)
skip list REMOVED + E4d withdrawn-split injection  -> RED (1 failed)
   AssertionError: a normative record transcribes the claim-kind split again …
   ['…EXP-006_IMPLEMENTATION_PLAN.md:737: Per `B-1` the split is behavior **23** …']
restored                                           -> green
```

The skip list is **gratuitous**: no real document needs it, its removal closes the escape, and its
presence is the sole reason the exact `B-1` defect form passes.

## 10. `INFO-1` — the STOP assessment

I inspected the passage directly. **The STOP was justified, is correctly reasoned, and is properly
recorded.**

- **Entry count.** `§Open Questions` (card `:699-717`) opens *"**None block approval.** All six are
  mapped RC silences **or governance items** carried forward from accepted Stage-A evidence."* above
  **seven** distinct numbered entries. The introducer undercounts its own list by one. Confirmed.
- **Classification.** Not all seven are RC silences: items 1–4 are source silences; item 5 (rations
  ownership), item 6 (starvation causation has no Rule ID — the card itself calls it *"a standing
  open governance issue"*) and item 7 (the unowned complete-darkness predicate) are
  governance/ownership items. The sentence's own disjunction accommodates both, so the *kind* claim
  is sound for all seven; only the *number* is wrong.
- **Does `six` plausibly reach a different list?** **Yes, and I verified it.**
  `## Rules Cyclopedia Leaves Undefined / Ambiguous` (card `:159-196`) enumerates **exactly six**
  items, and it is a genuinely **different set**: it shares items 1–4 but substitutes *"whether the
  timetrack method is intended for light durations"* and *"water consumption rate"*, and excludes
  rations, starvation and the complete-darkness predicate. The ledger's load-bearing reason 2 is
  factually accurate — I checked it against the card rather than accepting it.
- **Are the other count statements consistent?** **Yes.** §Approval: *"**Six** RC silences, plus the
  unowned complete-darkness world-state predicate (Open Question 7)"*; Submitted contract:
  *"**seven** source silences"*. 6 + 1 = 7. Both correct and mutually consistent. Review #4 grouped
  all three statements as one loose count; the remediation's narrowing of `INFO-1` to the
  `§Open Questions` introducer alone is correct, and I confirm it independently.
- **Is leaving it unedited defensible?** Yes. The card is a **protected approved Rule Card**
  (`AGENTS.md` §12); a blind `six → seven` edit could sever an intended cross-reference to the
  six-item `§Leaves Undefined` list and create a new inconsistency with §Approval's "Six RC
  silences, plus… (Open Question 7)" framing. Which framing is canonical is a human decision. The
  ledger §4 records the exact passage, all seven entries with dispositions, three independent STOP
  triggers, and two candidate minimal corrections — including the derive-or-delete-consistent option
  (b) that is correct under either reading.

**No mechanic, case ID, mapped-silence disposition, provenance or approval state changed.** Verified
mechanically: `git diff a150837 e5caf12 -- docs/rules/exploration/` is **empty**. **No repository
artifact claims `INFO-1` was resolved** — `ISSUE-022` §11 records it as open and requiring human
adjudication, the ledger as `STOPPED`. Nothing to find here.

## 11. Non-blocking limitations / overclaim check — CLEAN

No broader proof is claimed than the mechanisms establish, for the known dynamic/reflection
constructs. `src/` is **byte-identical** to both earlier reviewed HEADs (tree
`d6aaf58785645f3ec8db895f9791851dd68f2c59` at `a150837`, `afd440e` and `e5caf12`), and the guard
suite changed by **exactly one string** — the `NB-4` correction, which **narrows** a claim
(`"deplete's signature and return type are pinned"` → `"deplete's parameters pinned; no world-state
value returned"`). So the guard-claim layer is the one review #4 audited and found, for the first
time, free of overclaim.

The three disclosed limitations remain disclosed verbatim: module-level `__getattr__` (PEP 562) in
three places; the private class attribute (`LightSource._rounds_elapsed`) in the
`test_no_module_level_mutable_state_exists` docstring with the broader claim explicitly withdrawn and
`L13`/`L14`/`L19b` reclassified `reviewed:`; `_LIGHT_SOURCE_IDENTITIES[kind].__getstate__()` in the
guard docstring and `ISSUE-022` §11 item 5, with `L42` correctly rested on "no public callable
returns an `Item`". The ledger §5 records `NB-1`/`NB-2`/`NB-3`/`NB-7` as recorded-not-remediated and
widens nothing. **I did not restart the Python-guard arms race and found no reason to.**

## 12. Rules smoke check — CLEAN, and provably frozen

Not a fifth rules review. The `src` **tree hash is identical** across `a150837`, `afd440e` and
`e5caf12`, so the `SR-11` branch, the ignition matrix, depletion/refuel behaviour and the error
taxonomy cannot have changed in production code. The approved Rule Card is byte-identical to
`afd440e` and `a150837` (`docs/rules/exploration/` diff empty), so the mechanics and the 53-case
identity set are unchanged — independently re-derived above as 53 IDs / 53 rows / no orphans / exact
`CASE_DISCHARGE` correspondence, split `22/5/11/14/1`. The only change under `docs/rules/` is to two
status records (`INVENTORY.md`, the `CLUSTER-004` record). Full suite green. No discrepancy
appeared, so no rules-research exercise was warranted.

## 13. Operational verification — three separate checks

- **`command completed`** — **PASS.** Every Python invocation used a written scratch `.py` file
  executed as `.venv\Scripts\python.exe <script>.py`; no `python -` stdin piping was used anywhere.
  Explicit exit codes captured: `verify.py` → 0; `audit_claims.py` → 0; `mutate.py` pass 1 → 1 (a
  deliberate `AssertionError` in my own harness on a wrong card-row pattern, after 17 scenarios had
  completed and printed; corrected in `mutate2.py`); `mutate2.py` → 0; `mutate3.py` → 0;
  `reconcile.py` → 0.
- **`process cleanup completed`** — **PASS, verified by enumeration, not by a kill returning
  cleanly.** `Get-Process` lists exactly two Python processes: PIDs 34608 and 42056, both
  `C:\Python314\pythonw.exe`, started 08:16:59 and 08:17:01. Both **pre-date the commit under
  review** (`e5caf12`, 10:58:24) and therefore pre-date this session; neither is the venv
  interpreter. A path-filtered query for venv processes returns **NONE — no venv python remains**. I
  started no background process and killed nothing.
- **`repository unchanged`** — **PASS.** `git status --porcelain` empty (tracked and untracked); HEAD
  still `e5caf12`; branch still `cluster-004-exp-006-stage-b`; `HEAD:src` still `d6aaf58…`; reflog
  head unchanged at `e5caf12` with no new entries; `git stash list` empty. No commit, merge, push,
  rebase, stash, reset or clean. All mutations ran in `…\Temp\claude\exp006-rev5\copy`.

## 14. Canonical verification

`.venv\Scripts\python.exe scripts\verify.py` → **exit 0**.

```text
Gates that actually exist — FIVE (there is no policy gate)
  Tests:     PASS    1186 passed in 1.75s   (suite-wide)
  Coverage:  PASS    src/rules/ 20 files @ 100% required per file;
                     core aggregate 5 files @ 100.00% (>= 95%)
  Ruff:      PASS    no issues
  mypy:      PASS    no issues found in 53 source files
  Evidence:  PASS    1 reference packet (_TEMPLATE.md); 0 Stage-A packets; 12 grandfathered
  Overall:   PASS

Test counts (independently collected)
  test_light_and_exploration_resources.py    112 tests
  test_exp_006_record_consistency.py          11 tests   (was 5 at afd440e)
  EXP-006 total                              123 tests
  suite-wide                                1186 tests

Per-file coverage (independent coverage run, EXP-006 tests only)
  src/rules/exploration/errors.py                            4 stmts, 0 miss,  0 branch, 0 partial  -> 100% / 100%
  src/rules/exploration/light_and_exploration_resources.py 131 stmts, 0 miss, 52 branch, 0 partial  -> 100% / 100%
```

The Evidence gate's self-report that it has governed zero post-`DEC-0012` packets is accurate and
honestly stated.

## 15. BLOCKING findings

### BLOCKING-1 — HIGH — types **D** and **E**. The skip-list architecture was not removed; it was relocated into the same module, and it demonstrably cancels an intended current check.

**The claims.** `test_exp_006_record_consistency.py` module docstring: *"**THE NEW RULE: no skip
list.**"* `test_no_stale_claim_can_be_silently_excluded` docstring: *"There is now **no skip list at
all**; this test asserts that"*, with the inline comment *"There is no skip/exemption list in this
module. If one is ever reintroduced, this assertion is the tripwire."* Ledger §B-6 `:111`: *"**The
skip-list architecture is removed entirely.** … so there is nothing for a historical exemption to
do, **and none exists**."* Ledger §B-1 `:67`: *"`test_no_live_record_duplicates_the_category_split`
**fails if any claim-kind count is transcribed into the plan or the gate again**."* Ledger §3 `:121`:
*"derived from `CASE_DISCHARGE`, duplicated nowhere; **a guard fails any re-transcription**."*

**The mechanism.** `test_exp_006_record_consistency.py:303-310`. A line is an offence only if it (a)
contains a kind word, (b) contains **none** of
`("withdrawn", "superseded", "previously", "B-1", "B-2")`, and (c) matches `\*\*\d{1,2}\*\*`.
Condition (b) is a marker-keyed line skip — structurally the `B-6` defect — and three of its five
markers (`"withdrawn"`, `"superseded"`, `"previously"`) are **verbatim members of the
`HISTORICAL_MARKERS` tuple** the ledger says was removed entirely (`afd440e` blob lines 85-97).
`"B-1"` and `"B-2"` are not historical markers at all; they are the finding IDs that remediation
prose in these two documents naturally cites. The tripwire that is supposed to forbid this checks
the names `HISTORICAL_MARKERS` / `SKIP_MARKERS` / `EXEMPT_MARKERS` against `globals()` and
structurally cannot see a function-local tuple — so it did not fire.

**Demonstrated failure scenario (scratch copy, full 123-test EXP-006 set green in every case):**

```text
E4d  plan += "Per `B-1` the split is behavior **23** / invariant **5** /
              surface **23** / reviewed **1** / routed **1**."   -> 123 passed
```

That is the **literal `B-1` defect**: the withdrawn `23/5/23/1/1` split, 13 of 53 rows
misclassified, re-transcribed into the approved implementation plan, with the suite green. Also
green: E4 (correct split, cites `` `B-1` ``), E4b (`previously`), E4c (gate, cites `` `B-2` ``), E3
(unbolded table — invisible regardless of markers), E7 (three-digit bold).

**And the hole is unnecessary.** With the skip line deleted in scratch, the suite is **still green
against the unmodified real documents**, and the E4d injection is **caught**. The skip list protects
nothing and is the sole cause of the escape.

**Why this meets the standard.** Type **D**: four separate repository claims — two of them
categorical ("none exists", "fails any re-transcription") — exceed what the mechanism establishes,
and the asserting tripwire cannot detect the construct it names. Type **E**:
`test_no_live_record_duplicates_the_category_split` explicitly claims *"the split is derived, and
lives in exactly one place… must not be transcribed into a normative record again"*, and it passes
while a normative record transcribes the full split. This is not dynamic-Python exotica outside a
narrow stated claim — it is a plain markdown line in the most natural authoring style for these
documents, and it reproduces the exact defect the mechanism was built for. **This is the review-#4
documentation-consistency failure mode, recurring one commit later in the same file.**

### BLOCKING-2 — HIGH — types **B**, **C** and **D**. `ARCHITECTURE.md`'s `EXP-006` block contradicts itself about review #4 and retains stale prose counts, inside the sentence that declares prose counts abandoned — and `ISSUE-022` claims a test checks exactly this.

Three defects in one live, unmarked section of `ARCHITECTURE.md` (enrolled in both `LIVE_RECORDS`
and `PHASE_TOKEN_RECORDS`):

1. **`:529`** — *"**A fourth independent review is not yet authorized**, and acceptance is a human
   act."* **`:525`**, added by this very remediation, states *"**A fourth independent review
   (2026-10-03) returned `FAIL`**"*. Four lines apart, both present tense, neither marked
   historical. The remediation corrected this identical sentence in the plan (deleted) and in the
   `CLUSTER-004` record (*"A **FOURTH**"* → *"A **further**"*) — proving the author recognised it
   needed changing — and missed the `ARCHITECTURE.md` twin. Type **B**; it is also the §6 condition
   "a current record implies review #4 has not occurred".
2. **`:521`** — the same paragraph that states *"it is deliberately not restated here as a count,
   because every prose count of it has gone stale (review-#4 `B-4`)"* then retains, in that very
   sentence, *"every finding in **all three** concerned the self-description layer"* and *"**All
   three** remediations are recorded (`EXP-006_REVIEW_REMEDIATION_LEDGER.md`, `..._REVIEW_2_...`,
   `..._REVIEW_3_...`)"*. Four reviews and four remediations exist; **ledger #4 is omitted from the
   enumeration**. This is `B-4`'s exact defect class — obsolete review count plus incomplete
   artifact enumeration — newly introduced by a partial edit. It was *true* at `afd440e` ("Three
   independent final implementation reviews have now been performed"), so this is a new defect, not
   a `B-4` non-closure. Types **B** and **C**.
3. **The overclaim that ties them together.** `ISSUE-022`'s new block asserts: *"The review history
   is now established by the artifact set that exists on disk… and
   `test_the_review_artifact_set_is_internally_consistent` checks that every review artifact has a
   paired remediation ledger **and that no live record asserts a contradicting prose count**."* The
   test does the first conjunct only — it globs reviews and ledgers, compares their counts, and
   checks each filename appears in `ISSUE-022`. It never reads any other live record, and no
   mechanism anywhere checks prose counts. **Demonstrated:** `ARCHITECTURE.md:521` asserts a
   contradicting prose count right now, and the suite is green (1186 passed). Type **D**, and type
   **E** against the second conjunct.

### BLOCKING-3 — LOW-MEDIUM — type **C**. A self-declared live status block cites a verification mechanism that does not exist.

`docs/rules/clusters/CLUSTER-004-equipment-resources-and-evasion.md:425-427`: *"**Live next step.**
This block is **status**, not history, and the review phase it carries is pinned by
`test_live_status_records_agree_on_the_review_phase` so it cannot silently go stale again."* **No
such test exists.** The remediation renamed it to `test_live_records_carry_the_current_phase_token`
and did not update this cross-reference — it is the only dangling test-name reference in the
repository (I cross-checked every cited consistency-test name against the defined set; all others
resolve). False traceability in a block that explicitly declares itself current status.
**Mitigation:** the substantive protection does exist under the new name and I demonstrated it fires
(P1/P2), so the risk is a reader or auditor who cannot follow the citation, not an absent guard.
This is the weakest of the three and I would not fail the review on it alone.

## 16. Non-blocking and informational findings

- **NB-1 (limitation, accurately disclosed).** The stale-claim check is **per line**, so a forbidden
  phrase that wraps across a line break is not seen. `PRE_CODE_GATE.md:275-276` currently contains
  the configured phrase `"23 of the 53"` split across a line break; it passes. Here that is harmless
  — the text explicitly quotes it as removed under `B-2` — but it means the guard's current green
  state partly depends on line wrapping, and reflowing that paragraph would turn it red for a
  legitimate historical quotation. Flagged because that is the pressure that produced `B-6`'s skip
  list in the first place.
- **NB-2 (limitation, disclosed in scope; one ledger claim not borne out).** The three
  `LOW-3`/`LOW-8` entries in `STALE_CURRENT_CLAIMS` match nothing in the pre-remediation tree,
  although the defect was present in three records there (D2/D3/D4 all pass). The module docstring's
  *"it does not scan arbitrary prose, it is not a generic documentation linter"* fairly scopes this
  to literal phrasings, so it is a limitation rather than an escape, and the phase token
  independently protects the resolved state. But ledger line 200's claim that the claim set "now
  covers… the open-findings wording" is not supported by any form that wording actually took.
- **NB-3 (informational).** `test_every_stale_claim_is_actually_evaluated` re-implements the
  predicate inline against a fixture it just wrote (`claim in f"…{claim}."`) rather than invoking
  the production check, so it is tautological. With no skip list in that test it currently proves
  nothing false — but it would keep passing if a skip list were added to
  `test_no_live_record_asserts_a_stale_claim`, which is precisely the regression it is meant to
  prevent. Same pattern in both named `B-6` regression tests.
- **NB-4 (informational).** `ISSUE-022` §11 has two items numbered `8.`. Markdown auto-renumbers, so
  the rendered list is correct 1–9; raw-source only.
- **NB-5 (informational).** `ISSUE-022` §11 item 8 cites "the review-#4 remediation ledger
  **§INFO-1**"; the ledger's section is numbered **§4**, titled `INFO-1`. Resolvable, trivially.
- **INFO-1 (informational, correctly open).** The approved card's `§Open Questions` introducer
  undercounts its own seven-entry list as "six". Correctly `STOPPED` for human adjudication, with
  the exact passage, all seven dispositions, three STOP triggers and two candidate corrections
  recorded in ledger §4 and the open item carried in `ISSUE-022` §11. **No repository artifact
  claims it was resolved.** See §10 — the STOP was justified and the ledger's reasoning survives
  independent verification.
- **INFO-2 (informational).** Good-faith disclosures I verified and credit: the remediation's commit
  message states *"on first run [the redesigned test] caught two records I had updated in prose but
  not in token, and a historical quotation that reproduced a forbidden phrase verbatim"* — the
  mechanism earned its place, and the author said so rather than claiming a clean first pass.

## 17. Final verdict

The rules layer is clean and **provably frozen**: the `src` tree hash is byte-identical across
`a150837`, `afd440e` and `e5caf12`; the approved Rule Card is byte-identical; the guard suite changed
by exactly one string, which narrows a claim. The 53-case identity set, the derived split
`22/5/11/14/1`, the `SR-11` branch, the ignition matrix, depletion/refuel behaviour and the error
taxonomy are untouched. Verification is green on all five real gates with 100% statement and branch
coverage on both production files. `B-1` through `B-5` are factually and completely closed — I
verified each against the repository rather than against the ledger, and the retrospective scan shows
four of the fifteen configured claims would have fired on four distinct pre-remediation records. The
`INFO-1` STOP was justified, correctly narrowed, and properly recorded; the ledger's load-bearing
claim about a different six-item section in the card is accurate. `ISSUE-022` is materially repaired
and does not claim premature completion. Replacing published numbers with derived ones, and choosing
removal over renumbering, is the right structural remedy and it worked.

Review #5 existed to determine whether the review-#4 documentation-consistency failure mode has
actually been eliminated. **It has not.** The defect moved rather than closing. `B-6`'s specific
escape is dead, but the architecture `B-6` identified — a marker-keyed line skip that cancels an
intended current check — is back in the same module, reusing three of the same markers, behind a
tripwire that structurally cannot see it, under four repository claims including two categorical ones
("none exists", "fails any re-transcription"). I re-transcribed the exact withdrawn `23/5/23/1/1`
split into the approved implementation plan and the whole suite stayed green; deleting the gratuitous
skip line both keeps the real documents green and catches that injection. Alongside it,
`ARCHITECTURE.md` now contradicts itself about whether review #4 happened and retains a
four-reviews-ago count inside the sentence announcing that prose counts were abandoned, while
`ISSUE-022` names a test as checking precisely that condition — a test that does nothing of the kind.

These are the same defect class, reached by the same route: an audit artifact claiming more than its
mechanism establishes, and a fact updated in one place but not its twin. Each finding is concrete,
current, and demonstrated with a reproduced failure scenario meeting the §3 standard (B, C, D or E).

**`EXP-006 INDEPENDENT FINAL REVIEW #5: FAIL`**

Nothing in the rules, mechanics, state space, `SR-11` scoping, ownership boundaries or guard-claim
layer requires further work. The three blocking findings are confined to the self-description layer
and are narrowly fixable: delete one gratuitous skip line (proven safe and proven to close the
escape), correct two sentences in `ARCHITECTURE.md`, drop one unsupported conjunct in `ISSUE-022`,
and repoint one test name in the `CLUSTER-004` record. I made no edits; I am not authorized to, and
`ARCHITECTURE.md` plus the protected records require a human-assigned task either way. No new Rules
Cyclopedia research is implicated, and `INFO-1` still awaits the human adjudication the remediation
correctly stopped for.
