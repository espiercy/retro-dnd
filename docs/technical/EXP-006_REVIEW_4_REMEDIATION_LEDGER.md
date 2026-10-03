# `EXP-006` — Remediation Ledger for Independent Final Implementation Review #4

```text
REVIEW REMEDIATED    docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW_4.md
REVIEW VERDICT       FAIL  -- 6 BLOCKING, 7 non-blocking/informational
REVIEWED HEAD        a15083790d5c8f81865d391c7c24e736609714cf
ARTIFACT COMMIT      afd440e2b2cc5c073641602fb4c1e9e8fbd4ca8a
REMEDIATION DATE     2026-10-03
AUTHORIZED BY        human project owner; documentation-consistency
                     remediation ONLY. Review #5 NOT launched.
WORKTREE             OD_N_D-cluster-004-exp-006-stage-b
BRANCH               cluster-004-exp-006-stage-b   (unmerged, unpushed)
CERTIFICATION        NONE. Review #4 remains a historical FAIL. This ledger
                     does not and cannot claim it passed.
```

> **Reviews #1–#4 and remediation ledgers #1–#3 are preserved unaltered.** Review #4 is not
> relabelled, edited or softened, and its `FAIL` verdict stands as the fourth final-review result.

---

## 1. Rules and guard layers are FROZEN

Review #4 independently established two things no prior review had both established at once:

```text
RULES LAYER:        clean  -- fourth consecutive review, no rules defect
GUARD-CLAIM LAYER:  clean  -- FIRST review to find no guard overclaiming
```

It re-derived the contract from the approved card, executed all eight ignition rows, ran **38 novel
mutations (37 caught)**, walked the full state space, and audited every guard as *claim → mechanism
→ does the mechanism establish the claim*. Accordingly this remediation changed **none** of:

```text
production rules mechanics      UNCHANGED
ignition matrix                 UNCHANGED
SR-11 mechanics                 UNCHANGED
depletion / refuel mechanics    UNCHANGED
error semantics                 UNCHANGED
CHAR-004 seam                   UNCHANGED
state invariants                UNCHANGED
architecture-guard breadth      UNCHANGED
guard claim scope               UNCHANGED
Stage-A evidence / research      NOT reopened
```

**No guard was "improved" while fixing documentation.** The surviving dynamic-Python limitations
remain non-blocking limitations exactly as review #4 classified them (§4 below). `src/` is
byte-identical to the reviewed HEAD.

Every blocking finding was a **duplicated fact that had gone stale in its second location**, or the
consistency mechanism built to prevent that. The remedy throughout is **derive, or delete — do not
re-transcribe.**

---

## 2. The six blocking findings

### `B-1` — the plan republished a withdrawn split under a false protection claim

| | |
|---|---|
| **Source** | `docs/technical/EXP-006_IMPLEMENTATION_PLAN.md` §12 (approved plan, live section) |
| **Defect** | The section tabulated `behavior 23 / invariant 5 / surface 23 / reviewed 1 / routed 1` — the split review-#3's remediation had **explicitly withdrawn** — with **13 of 53 rows misclassified**, beneath the assertion *"It is **computed, not transcribed**… asserts these exact numbers, so this table **cannot drift from the code without a red test**."* No such protection existed: the test compares counts it derives from `CASE_DISCHARGE` against its own literals and **never reads the plan**. The table had drifted and the suite was green — type D (claim broader than mechanism) on top of type B (current normative contradiction). §12.1's "provable by API shape" enumeration was stale for the same reason. |
| **Correction** | The split is **not restated with corrected numbers**; it is **removed**. §12 now says, normatively: the 53 cases are reconciled by `CASE_DISCHARGE`; the current category split is **derived** from `CASE_DISCHARGE` and verified by the suite; **it is not duplicated normatively in this plan**. The case total is likewise not owned there — it is enumerated from the approved card. The claim-kind vocabulary is retained (it is a definition, not a count). The withdrawn figures and the stale §12.1 list are quoted as superseded, with the false protection claim named. |
| **Verification** | `test_no_live_record_duplicates_the_category_split` fails if any claim-kind count is transcribed into the plan or the gate again. `test_the_case_ledger_total_matches_the_card` and `test_the_case_category_counts_are_recomputed_not_carried_over` hold the derived facts. |

### `B-2` — the gate asserted a protection over the plan, and published a stale figure

| | |
|---|---|
| **Source** | `docs/technical/EXP-006_PRE_CODE_GATE.md` §6 |
| **Defect** | *"implementation plan §12 reproduces it **under that assertion's protection**"* — false twice over: no assertion protected the plan, and the plan's split had drifted. Separately, *"**23** of the 53 are discharged by the shape of the public surface"* was a hand-copied figure, stale after review-#3's reclassification. Neither was marked historical, and §8a presents §1–§8 as standing findings. |
| **Correction** | No substitute number. The gate now records that the **case total is reconciled against the approved Rule Card**, that the **current category classification is derived from `CASE_DISCHARGE`**, and — stated explicitly — that **the gate does not own the post-implementation category split** and asserts no protection over any other document. The "23 of the 53" figure is removed with the reason named. The historical Pre-Code `PASS` and the §8a remediation chronology are preserved intact. |
| **Verification** | Same guard as `B-1`; `"23 of the 53"` is additionally in `STALE_CURRENT_CLAIMS`, so its reappearance in a named live record fails. |

### `B-3` — five live records said `LOW-3`/`LOW-8` were open at the commit that resolved them

| | |
|---|---|
| **Source** | `ARCHITECTURE.md:523`; `docs/rules/INVENTORY.md:106`; `CLUSTER-004-…md:443-445` (a block self-labelled *"Live next step… status, not history"*); `EXP-006_IMPLEMENTATION_PLAN.md` §1.2 and §18; `ISSUE-022` `STATUS` block and §11 |
| **Defect** | All five asserted the two protected-card findings "remain OPEN and require human adjudication". `a150837` — the reviewed HEAD itself — applied both. `ARCHITECTURE.md` was additionally wrong in substance ("`CHAR-005` **still carries** both… denials"). A reader could not determine which findings were actually outstanding before acceptance. |
| **Correction** | All five now state `LOW-3`/`LOW-8` **`RESOLVED`**, naming the applying commit `a150837`, what each clarification did, and that neither changed a mechanic, provenance classification, case ID or approval status. Review #3 and ledger #3 are **not** rewritten — the findings were legitimately open at that point, and that record stands. |
| **Verification** | `"LOW-3 and LOW-8 remain OPEN"`, its lowercase form and `"remain open pending human adjudication"` are in `STALE_CURRENT_CLAIMS`, evaluated against all seven named live records with **no exemption mechanism**. |

### `B-4` — `ISSUE-022` contradicted itself about its own review history

| | |
|---|---|
| **Source** | `docs/completion-records/ISSUE-022-...md` §3, §11, chronology |
| **Defect** | §11 (a required `DEVELOPMENT_WORKFLOW.md` §5 category): *"**Two** independent final implementation reviews have returned `FAIL`; a **third** … required"* — contradicting the same file's `STATUS` block. The chronology listed review #3 as *"pending, separately authorized"* after it had run, failed and been remediated, and omitted reviews #3/#4, ledgers #3/#4 and the `LOW-3`/`LOW-8` adjudication. Closing prose said *"**Both** final-review artifacts"* and *"**Both** reviews found…"*. §5 item 3 omitted `EXP-006_FINAL_IMPLEMENTATION_REVIEW_3.md` and `EXP-006_REVIEW_3_REMEDIATION_LEDGER.md`, and asserted the card was *"amended **only** by the two … corrections of 2026-10-01; **not** touched by either remediation pass"* — false once `a150837` amended it. |
| **Correction** | **No prose count replaces the old one.** The review history is now established by **the artifact set that exists on disk**, enumerated and paired in §3; the `STATUS` block says "every independent final review performed so far returned FAIL" and explains why no count is stated. The chronology is extended through review #4 and the `LOW-3`/`LOW-8` adjudication, with "pending" removed. §5 item 3 lists all eight review/ledger artifacts and both amended protected cards with their authorizations. The false "amended only"/"not touched" absolute is replaced with the accurate rule — the card is amended **only under explicit human authorization, never by a remediation pass acting on its own** — and all three amendments are named. §11 item 8 records `INFO-1` as open. The record still states `NOT COMPLETE` and names human acceptance as a separate act. |
| **Verification** | `test_the_review_artifact_set_is_internally_consistent` asserts every review artifact has a paired ledger **and** that every one appears in §3, so §5 item 3 cannot go incomplete silently. `"Two independent final implementation reviews"` is in `STALE_CURRENT_CLAIMS`. |

### `B-5` — the mandated index said a completed review was pending

| | |
|---|---|
| **Source** | `docs/completion-records/INDEX.md:28` |
| **Defect** | *"reviews #1 and #2 both `FAIL` …; **review #3 pending, separately authorized**"*. `INDEX.md` is mandated by `DEVELOPMENT_WORKFLOW.md` §6 as the scannable implementation history. It was never touched by the review-#3 remediation and was **not enrolled** in the consistency test's record set, so the `MED-1` defect class recurred in the one live record the mechanism did not cover. |
| **Correction** | The row now reads: code complete, all five gates pass; **every independent final review so far `FAIL`, each remediated, none concerning rules logic**; most recent review #4 `FAIL` with remediation current; **final human acceptance pending**; and points at `ISSUE-022` as authoritative. Kept to one line — the index is a summary, not a chronology. |
| **Verification** | `INDEX.md` is now in `LIVE_RECORDS`, so `"review #3 pending"` and its siblings fail there. `test_the_configuration_is_non_empty_and_every_named_record_exists` asserts it exists and is configured. |

### `B-6` — the consistency mechanism could not evaluate four of its six conditions

| | |
|---|---|
| **Source** | `tests/rules/exploration/test_exp_006_record_consistency.py` (previous design) |
| **Defect** | The loop skipped any line containing a `HISTORICAL_MARKERS` entry **before** testing `SUPERSEDED_PHASE_CLAIMS` — and `"review #2"` was in **both** lists. So `"review #2 pending"`, `"review #2 PENDING"`, `"awaiting review #2"` and `"pending independent review #2"` were **unconditionally unreachable**; only two of six conditions could ever fire. Review #4 demonstrated the escape: appending `"independent review #2 pending"` to a pinned record left all five tests green. A guard enumerating six conditions while able to evaluate two **reports protection it does not provide** — types D and E. |
| **Correction** | **The skip-list architecture is removed entirely.** The new rule: this test reads **only** explicitly named live/current records, and **never** scans the review artifacts or remediation ledgers — so there is nothing for a historical exemption to do, and none exists. `STALE_CURRENT_CLAIMS` is evaluated unconditionally against every named live record. |
| **Verification** | Five self-checks now prove the configuration is meaningful: every named record is non-empty and exists; `PHASE_TOKEN_RECORDS ⊆ LIVE_RECORDS`; **no skip list may be reintroduced** (asserted by name against `globals()`, as a tripwire); no stale claim may be subsumed by another; and no historical artifact may appear in the scanned set. `test_every_stale_claim_is_actually_evaluated` proves **each** configured claim is detectable, on a `tmp_path` fixture. Two named regressions reproduce review #4's own injection on fixture copies: `test_injecting_review_2_pending_into_a_live_record_is_detected` and `test_injecting_review_3_pending_into_a_live_record_is_detected`. **No historical artifact is altered to do this.** |

---

## 3. Derive rather than transcribe — the structural change

| Fact | Was | Now |
|---|---|---|
| Case total (53) | hand-maintained in the plan and the gate | **enumerated from the approved Rule Card**; `test_the_approved_case_total_is_still_what_the_records_claim` |
| Category split | tabulated in the plan **and** summarised in the gate; both drifted | **derived from `CASE_DISCHARGE`**, duplicated nowhere; a guard fails any re-transcription |
| Review history | prose counts ("two", "three") in five records | **the persisted artifact set on disk**, paired review↔ledger and cross-checked against `ISSUE-022` §3 |
| Review phase | prose in each record | **one token**, `EXP-006-PHASE: REVIEW-4-REMEDIATED`, required in five records |
| Test counts | duplicated in `ISSUE-022` §3 and §6 | removed; §8/§9 report actual verification output only |

This eliminates the exact duplicated-fact class all four reviews found. What cannot be derived — the
phase — is a single token with an atomic update rule.

---

## 4. `INFO-1` — **STOPPED. HUMAN ADJUDICATION REQUIRED.**

The authorization permitted a `six` → `seven` correction **only** if the passage contains seven
distinct entries *all genuinely classified there as mapped RC silences*, and required a STOP if any
entry is differently classified or the intended count is ambiguous. **I inspected the passage and
the count is ambiguous, so I stopped and made no edit.**

**The exact passage** — `docs/rules/exploration/light_and_exploration_resources.md` §Open Questions:

> **None block approval.** All six are mapped RC silences **or governance items** carried forward
> from accepted Stage-A evidence.

**The seven entries that follow:**

```text
1. What happens when a light source's duration reaches zero.   RC SILENCE
2. How carried mundane light maps to any Visibility category.  RC SILENCE
3. Adverse-condition ignition without Fire-Building.           RC SILENCE
4. Deliberate extinguishing.                                   RC SILENCE
5. Rations -- ownership open (SS D), by express direction.      GOVERNANCE ITEM
6. Starvation causation has no Rule ID (SS E)                   GOVERNANCE ITEM
   -- "a standing open governance issue".
7. The complete-darkness / environmental-illumination           GOVERNANCE ITEM
   world-state predicate has no owner.
```

**Why this is not a demonstrable typo.** Three reasons, any one of which triggers the STOP:

1. **Not all seven are RC silences.** Items 5–7 are governance/ownership items, which the sentence
   itself accommodates via *"or governance items"*. The authorization's condition — *all seven
   genuinely classified there as mapped RC silences* — is **not** met.
2. **"Six" is a meaningful number elsewhere in this card, for a genuinely different six-item list.**
   §*Rules Cyclopedia Leaves Undefined / Ambiguous* enumerates exactly **six** items — and it is a
   *different set*: it includes *"whether the timetrack method is intended for light durations"* and
   *"water consumption rate"*, and excludes rations, starvation and the complete-darkness predicate.
   So `6` is not simply wrong in this card; changing `six` → `seven` here might be correcting a
   typo, or might be severing an intended cross-reference to that list.
3. **The other two count statements review #4 grouped with this one are actually correct and
   mutually consistent.** §Approval says *"**Six** RC silences, plus the unowned complete-darkness
   world-state predicate (Open Question 7)"* = 6 + 1; the Submitted-contract line says *"**seven**
   source silences named and guarded"*. 6 + 1 = 7. **Both are right.** Review #4 read all three
   statements as one loose count; they are not. **Only the §Open Questions introducer undercounts
   its own list.**

**Candidate minimal corrections, for human choice** — not applied:

- (a) `All six` → `All seven`, if the introducer is simply miscounting its own list; or
- (b) leave the number and reword to avoid a count, e.g. *"None block approval. Each is a mapped RC
  silence or a governance item carried forward from accepted Stage-A evidence."*

Option (b) is the one consistent with this remediation's derive-or-delete principle, and it cannot
be wrong regardless of which list `six` was reaching for.

**Effect of either correction: documentation only.** No mechanic, silence disposition, provenance
classification, case ID or implementation behaviour is affected. **Protected approved Rule Card —
requires explicit human direction.**

---

## 5. The seven non-blocking / informational findings — dispositions

Per the authorization, these are **recorded, not automatically remediated**. No guard was widened.

| # | Finding | Why review #4 classified it non-blocking | Current-record correction warranted? |
|---|---|---|---|
| **NB-1** | A private class attribute (`LightSource._rounds_elapsed`) incremented in `deplete` survives the suite | The repository **already discloses it verbatim** in `test_no_module_level_mutable_state_exists`, has **withdrawn** the broader claim, and reclassified `L13`/`L14`/`L19b` to `reviewed:`. Nothing shipped holds such state (both class dictionaries verified). A construct outside an explicitly narrow claim is a limitation. | **No.** The disclosure is accurate and current. Guard deliberately **not** widened. |
| **NB-2** | A module-level `__getattr__` (PEP 562) is outside what the namespace guards observe | Stated in **three** places with the claim narrowed to the concrete bound namespace at import time. No `__getattr__` is bound. | **No.** Accurate as disclosed. Deliberately not chased. |
| **NB-3** | `_LIGHT_SOURCE_IDENTITIES[kind].__getstate__()` reaches every catalog field with no import change | Disclosed in the guard docstring and `ISSUE-022` §11 item 5; `L42` correctly rests on "no public callable returns an `Item`" instead. | **No.** Already recorded. |
| **NB-4** | `CASE_DISCHARGE["L15b"]` says *"signature and **return type** are pinned"*; the return annotation is not pinned | No requirement is falsely certified — the property `L15b` names is machine-held by ten sibling tests, and mypy strict enforces the body against the annotation. Only the row's **wording** overstates. | **Yes — corrected.** The row now reads *"`deplete`'s signature and return type are pinned"* → *"`deplete`'s parameters are pinned; no world-state value is returned (ten sibling tests)"*. The ledger's own preamble warns that a row naming the wrong mechanism is worse than no row. |
| **NB-5** | The consistency test's stale-total set was hardcoded and narrow; it did not check split figures, classifications, review counts or the open-findings list | The docstring honestly scoped it, so it was not a false claim — but it is the direct reason `B-1`, `B-3`, `B-4` and `B-5` went undetected. | **Yes — addressed by `B-1`…`B-6`.** The claim set now covers stale review phases, the open-findings wording, the obsolete review count and the copied "23 of the 53"; the split is guarded by non-duplication rather than by figure-matching. |
| **NB-6** | `PHASE_RECORDS` omitted `docs/completion-records/INDEX.md`, a live status record under `DEVELOPMENT_WORKFLOW.md` §6 | Informational; it was the mechanism's coverage gap, surfaced as `B-5`. | **Yes — corrected.** `INDEX.md` is now in `LIVE_RECORDS` and its existence is asserted. |
| **NB-7** | `test_the_complete_production_dependency_surface`'s docstring names `rng` and `rules.currency` as the transitive loads; the measured set also includes `rules.character_creation.{errors,character_class}` | The docstring is **illustrative**, not an exhaustiveness claim, so it is not an overclaim. | **No.** Left as written; widening it would invite the opposite error of claiming an exhaustive transitive set. |

**`INFO-2`** (the Stage-A evidence gate has governed zero post-`DEC-0012` packets) is correct and
honestly reported by `verify.py` itself — no action. **`INFO-3`** (plan §12.1/§12.2 enumerations
stale by consequence of `B-1`) is **resolved by `B-1`**: both enumerations are removed rather than
re-listed.

---

## 6. Verification

```text
uv run python scripts/verify.py

Tests:     PASS
Coverage:  PASS      100% statement AND branch, per file, both production modules
Ruff:      PASS
mypy:      PASS      strict
Evidence:  PASS      DEC-0012 structural linter
Overall:   PASS
```

Five gates, which is all `verify.py` defines. Counts and coverage figures are reported in
`ISSUE-022` §8/§9 from the actual run rather than transcribed here.

**Frozen as required:** `src/` is byte-identical to the reviewed HEAD `a150837`; rules mechanics,
guard implementations and guard claim scopes are unchanged; Stage-A evidence was not reopened and no
new research was performed. **Preserved:** reviews #1–#4 and remediation ledgers #1–#3 are
byte-identical.

---

## 7. What this ledger does **not** do

```text
IT DOES NOT CLAIM REVIEW #4 PASSED.  It remains a historical FAIL.
IT DOES NOT CERTIFY COMPLETION.      The implementer may not.
IT DID NOT LAUNCH REVIEW #5.         Out of scope.
IT DID NOT WIDEN ANY GUARD.          Rules and guard layers frozen.
IT DID NOT EDIT A PROTECTED CARD.    INFO-1 is STOPPED for adjudication.
IT DOES NOT AUTHORIZE A MERGE OR PUSH.
IT DOES NOT AUTHORIZE CLUSTER-004 IMPLEMENTATION, ENC-005 STAGE B,
   OR ANY NEW STAGE-A CARD.
```
