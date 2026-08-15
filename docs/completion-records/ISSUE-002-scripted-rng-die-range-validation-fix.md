# ISSUE-002: ScriptedRNG Die-Value Validation (Post-Merge Defect Fix)

> **Note on numbering.** This is completion-record `ISSUE-002` in `DEVELOPMENT_WORKFLOW.md`'s sequential ledger (the next unused ID). It is **not** `ARCHITECTURE.md` §15's roadmap "Issue 2" (Rule Card infrastructure and the first Rule Card) — that work has not begun. This record documents a narrowly scoped post-merge defect fix to the ISSUE-001 RNG module.

## 1. Issue/Task Identifier and Objective

ISSUE-002 (completion-record ledger). Fix a semantic defect in `ScriptedRNG` identified by human code review after ISSUE-001 was merged: the scripted test double consumed raw values without validating them against the requested die, allowing production-impossible results (e.g., a scripted `9` accepted for a d6). Objective: enforce `1 <= value <= sides` (and a real-integer type, excluding `bool`) at draw time, with explicit failure, no rollback/coercion, and no advancement of the rules-visible sequence number on failure.

## 2. Approved Inputs/Specifications

- Human code-review finding (post-merge), specifying the defect, the required invariant, the failure-semantics constraints, and the required regression-test coverage — this task's own instructions.
- `docs/technical/RNG_CONTRACT.md` — the approved RNG contract this fix must remain consistent with (not redesign).
- `docs/decisions/DEC-0002-rng-contract.md` — approved RNG architecture (single stream, raw-draw/public-operation split, substitutability between production and scripted implementations).
- `docs/completion-records/ISSUE-001-rng-dice-infrastructure.md` — the originating implementation this fix corrects.
- Not a game rule; no Rule Card involved.

## 3. Files Created, Modified, or Deleted

**Created:**
- This completion record.

**Modified:**
- `src/rng/errors.py` — added `InvalidScriptedValueError`.
- `src/rng/rng.py` — `ScriptedRNG._raw_draw` now validates the next queued value against the requested die before consuming it; class docstring updated to document the invariant and the failure/queue semantics.
- `src/rng/__init__.py` — exported `InvalidScriptedValueError`.
- `tests/rng/test_scripted_rng.py` — 16 new regression tests; two pre-existing tests fixed (see §7).
- `tests/rng/test_contract_parity.py` — shared `ScriptedRNG` fixture's queue values corrected to all be valid for the d6 rolls exercised against them (see §7).
- `docs/technical/RNG_CONTRACT.md` — §9 and §12 updated to document the validation requirement explicitly (this contract's original text specified queue-exhaustion behavior but did not state this invariant).
- `docs/technical/TOOLCHAIN_AND_CI.md` — §9 and §12 updated: the "live GitHub Actions run not yet confirmed" open item is now recorded as confirmed (see §11 of this record — a current-state accuracy fix unrelated to the code defect, batched into this same branch per the assigning instructions).

**Deleted:** none.

## 4. Behavior Actually Implemented

- `ScriptedRNG._raw_draw(sides)` now peeks (not pops) the front of its queue, validates the value, and only pops it if valid. A value is valid iff it is an `int` (excluding `bool`) and `1 <= value <= sides`.
- An invalid value raises `InvalidScriptedValueError` (new; see §5) — the queue is left unmodified (the invalid value is **not** consumed — see §6) and no sequence number is assigned (the public operation fails before reaching `RollResult` construction).
- For a multi-die `roll(expression)` call, any raw draws that validated successfully *before* hitting an invalid one remain consumed (real randomness "already happened" is not rolled back); only the invalid value stays queued, and the operation as a whole fails with no `RollResult` produced and no sequence-number advancement.
- `SeededRNG` and the public `roll_die`/`roll` contract are unchanged. The dice grammar, the RNG ownership model, and the raw-draw/public-operation sequence-numbering split are all unchanged.

## 5. Rules Provenance

Not applicable — infrastructure defect fix, not a historical game rule.

## 6. Exception/Failure Semantics Adopted

Extended the existing RNG-specific exception taxonomy rather than introducing a new hierarchy: `InvalidScriptedValueError(DiceError)`, a sibling of `InvalidDiceExpressionError`, `InvalidDieSizeError`, and `RollSequenceExhaustedError`. Its docstring explicitly distinguishes it from `RollSequenceExhaustedError` ("the queue is not empty; its next value is simply invalid for this specific request") and states that no production randomness is consulted when it's raised.

**Scripted-queue behavior on an invalid value — decision and rationale (this contract did not already establish it; flagged here as instructed):** the invalid value is **left queued, not consumed**. This was chosen over "consume and fail" because it mirrors the *existing* control-flow shape already used for exhaustion (`_raw_draw` checks `if not self._queue: raise` *before* popping) — extending the same "check before consuming" pattern to value validation is the smallest, least-surprising change consistent with the existing fake-RNG design, and it means a malformed fixture is never silently discarded: retrying the same call surfaces the identical error again rather than skipping past the bad entry or masking it behind a subsequent exhaustion error.

## 7. Regression Tests Added (16 new, in `tests/rng/test_scripted_rng.py`)

- **Valid boundaries:** `test_accepts_values_at_the_valid_boundary` (`1`, `6` for a d6) — 2 cases.
- **Out-of-range:** `test_rejects_out_of_range_values_for_the_requested_die` (`0`, `-1`, `7`, `9` for a d6) — 4 cases.
- **Invalid types:** `test_rejects_bool_true_even_though_bool_is_an_int_subtype`, `test_rejects_bool_false`, `test_rejects_non_integer_numeric_value` (`1.5`), `test_rejects_string_value` (`"4"`), `test_rejects_none_value`.
- **Multi-die:** `test_invalid_constituent_value_fails_multi_die_operation` (a `9` as the 2nd of 3 scripted values for `"3d6"` fails the whole operation).
- **Queue semantics:** `test_invalid_value_is_left_queued_not_consumed` (the same call raises the identical error twice, proving the bad value isn't silently discarded).
- **Sequence-number semantics:** `test_failed_single_die_call_does_not_advance_sequence_number`, `test_failed_multi_die_call_does_not_advance_sequence_number` (both assert the internal `_sequence_number` counter stayed at `0` after a caught failure — a black-box approach can't observe this directly once the queue's invalid front value permanently blocks further calls on that instance, so this reaches into the private counter, following the precedent already set by `tests/rng/test_base_rng.py` for exactly this kind of otherwise-unobservable internal invariant).
- **Partial-consumption semantics:** `test_multi_die_failure_consumes_valid_values_before_the_invalid_one` (asserts the queue directly: the valid `4` before an invalid `9` was popped; the `9` was not).

**Existing tests fixed** (both previously relied on the defective behavior — an "impossible" value used merely as a sentinel, not as the point of the test):
- `test_sequence_numbers_follow_the_same_semantics_as_seeded_rng`: `ScriptedRNG([4, 2, 5, 9])` → `[4, 2, 5, 3]`. The 4th value only needed to be *some* valid d6 result; `9` was incidental.
- `test_rejected_call_does_not_consume_queue_or_sequence_number`: `ScriptedRNG([9])` → `ScriptedRNG([4])`, with the assertion updated from `result.dice == (9,)` to `result.dice == (4,)`. The test's purpose (a rejected `roll_die(0)` call doesn't touch the queue) is unaffected by which valid value is used.
- `tests/rng/test_contract_parity.py`'s shared fixture `ScriptedRNG([1, 2, 3, 4, 5, 6, 7, 8])` → `[1, 2, 3, 4, 5, 6, 1, 2]`. The `7`/`8` values were never actually reached by any current test (max 2 draws consumed), so this wasn't an active failure, but left uncorrected it would have silently reintroduced the defect's exact shape the moment a future test in that file drew a 7th value. Fixed proactively.

All other existing tests (68 from ISSUE-001) continue to pass unmodified — confirmed by the full run below.

## 8. Final Test Count

**84 tests, 84 passed, 0 failed** (68 from ISSUE-001 + 16 new).

## 9. Exact Verification Commands Executed

- `uv run python scripts/verify.py` (the canonical command; run repeatedly while fixing two mypy findings, final run reported below).

## 10. Verification Results

- **Tests:** 84 passed, 0 failed.
- **Coverage:** PASS — differentiated gate: `src/rules/` 0 files (trivially satisfied), `src/survivability/` 0 files (trivially satisfied), core aggregate 100.00% (≥95% required).
- **Ruff:** clean.
- **mypy --strict:** clean on the final run. Two findings surfaced and were fixed during this task: `ScriptedRNG([True])`/`ScriptedRNG([False])` initially carried an unnecessary `# type: ignore[list-item]` — `bool` is a subtype of `int`, so these are statically well-typed (identical situation to `roll_die(True)` in ISSUE-001); the comments were removed and replaced with an explanatory note rather than suppressed.
- **Overall: PASS.**

## 11. Coverage Results

100% statement and branch coverage, all files:

```text
Name                     Stmts   Miss Branch BrPart  Cover
src\rng\__init__.py          5      0      0      0   100%
src\rng\errors.py            6      0      0      0   100%
src\rng\expressions.py      19      0      8      0   100%
src\rng\results.py          12      0      0      0   100%
src\rng\rng.py               43      0      6      0   100%
TOTAL                        85      0     14      0   100%
```

No new coverage exclusions were introduced by this fix. The one pre-existing exclusion (the `RNG` Protocol's stub bodies, documented in ISSUE-001) is unchanged.

**Semantic coverage note** (this defect's own lesson, applied to its fix): the new tests don't merely execute the new validation branch — they establish the actual behavioral invariant this fix exists to guarantee (`ScriptedRNG` can force any production-reachable die result but cannot manufacture a production-impossible one) via the boundary-acceptance tests (§7) paired with the out-of-range/invalid-type rejection tests (§7), rather than relying on line/branch execution alone as evidence of correctness.

## 12. Deviations

None from the assigning instructions' required behavior. One documented design choice where the instructions explicitly asked for one to be made and flagged (§6 above): "leave queued, don't consume" for an invalid scripted value.

## 13. Known Limitations/Unresolved Issues

None specific to this fix. (Carried forward from ISSUE-001, still true: `scripts/verify.py`'s own orchestration logic has no permanent automated test; no RNG-state persistence exists yet, per `RNG_CONTRACT.md` §13 — deferred, not a regression.)

## 14. Architectural Consequences

None. This fix operates entirely within `ScriptedRNG`'s existing internal implementation; the public RNG interface, the ownership model, the sequence-numbering rule, the dice grammar, and every other approved architectural boundary are unchanged.
