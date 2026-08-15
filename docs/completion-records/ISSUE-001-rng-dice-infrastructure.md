# ISSUE-001: RNG and Dice Infrastructure

> **Amended 2026-08-15.** The initial completion record covered the RNG module itself. This amendment adds the differentiated coverage-enforcement layer, the canonical verification script, and the GitHub Actions workflow that were flagged as known limitations in the original record. This document describes the final implemented state as it now stands, per `DEVELOPMENT_WORKFLOW.md` §4 — it is not a diff log of the two passes.

## 1. Issue/Task Identifier and Objective

ISSUE-001. Implement the simulation-owned RNG abstraction and dice-expression support (`ARCHITECTURE.md` §15, Issue 1), per the approved RNG technical contract, together with the automated verification tooling (canonical verification command, differentiated coverage gate, CI workflow) required to enforce `TESTING_STRATEGY.md` and `docs/technical/TOOLCHAIN_AND_CI.md` in practice rather than by manual inspection.

## 2. Approved Inputs/Specifications

- `docs/technical/RNG_CONTRACT.md` — approved technical design.
- `docs/technical/TOOLCHAIN_AND_CI.md` — approved toolchain and verification model.
- `docs/decisions/DEC-0002-rng-contract.md` — RNG architecture approval.
- `docs/decisions/DEC-0003-python-toolchain-and-ci.md` — toolchain approval (Python 3.14, pytest, coverage.py, Ruff, mypy strict, uv, GitHub Actions).
- `ARCHITECTURE.md` §5 (RNG ownership), §15 (Issue 1 scope), §16 (Pre-Code Development Gate — cleared 2026-08-15).
- Not a game rule; no Rule Card required (`ARCHITECTURE.md` §15).

## 3. Files Created, Modified, or Deleted

**Created:**
- `pyproject.toml`, `uv.lock`, `.gitignore`
- `src/rng/__init__.py`, `errors.py`, `results.py`, `expressions.py`, `rng.py`
- `tests/rng/test_results.py`, `test_expressions.py`, `test_seeded_rng.py`, `test_scripted_rng.py`, `test_contract_parity.py`, `test_base_rng.py`
- `scripts/check_coverage.py` — differentiated branch-coverage threshold enforcement
- `scripts/verify.py` — the canonical verification command
- `.github/workflows/ci.yml` — GitHub Actions workflow invoking `scripts/verify.py`
- `docs/completion-records/INDEX.md`, this record

**Modified:**
- `pyproject.toml` — added `scripts` to `[tool.mypy] files`.
- `docs/technical/TOOLCHAIN_AND_CI.md` — §4, §8, §9, §11, §12 updated to record that the canonical verification command, the coverage-enforcement layer, and the CI workflow now exist (were previously "open items").
- `ARCHITECTURE.md` §13 — module layout updated to show `scripts/`, `.github/workflows/`, `pyproject.toml`, `uv.lock`, `.gitignore`, `src/rng/`, and `tests/rng/` as created.

**Deleted:** a temporary throwaway test file (`tests/rng/test_zzz_temp_verify_negative_path.py`), created and removed within this session solely to validate `scripts/verify.py`'s failure-reporting behavior (§8 below) — never part of the committed test suite.

## 4. Behavior Actually Implemented

**RNG module** (unchanged from the initial pass):
- A rich, immutable `RollResult` value (`expression`, `dice`, `die_size`, `modifier`, `total`, `sequence_number`); `total` is always derived from `dice`/`modifier`, never independently settable.
- Two public rules-facing operations — `roll_die(sides)` and `roll(expression)` — both built on one private raw-draw primitive per implementation, so each implementation has exactly one point of contact with actual randomness.
- `SeededRNG`: production implementation wrapping `random.Random(seed)`; deterministic given seed + call sequence.
- `ScriptedRNG`: deterministic test double consuming a pre-supplied queue of raw values; real aggregation logic still runs on top of scripted values; raises `RollSequenceExhaustedError` (never falls back to real randomness) on exhaustion, including mid-expression partial exhaustion.
- Sequence numbers are assigned once per public operation, not per underlying die (the `DEC-0002` refinement).
- Dice-expression grammar implemented exactly: `dS`, `NdS`, `NdS+M`, `NdS-M`, with `InvalidDiceExpressionError` for anything else.
- `roll_die` validates its size argument explicitly (`InvalidDieSizeError` for non-positive, non-int, or bool values).
- A rejected call, either operation, never advances the underlying stream or consumes a sequence number.
- The `RNG` Protocol type is published as the formal rules-facing contract type.

**Verification tooling** (new in this amendment):
- `scripts/check_coverage.py` reads `coverage.json` and applies three independent, AND'ed thresholds: 100% branch coverage per file under `src/rules/`, 100% per file under `src/survivability/`, and ≥95% aggregate across the rest of `src/` (the simulation core). A bucket with no matching files yet is reported as "trivially satisfied," not silently skipped. It trusts `coverage.py`'s own `missing_lines`/`missing_branches` accounting, which already respects `# pragma: no cover` exclusions — it does not re-implement exclusion handling.
- `scripts/verify.py` is the single canonical verification command (`docs/technical/TOOLCHAIN_AND_CI.md` §8): it erases stale coverage data, runs `coverage run --branch -m pytest`, and — only if that run's exit code is `0` — generates `coverage.json` and runs `check_coverage.py`. If the test run failed, Coverage is reported `UNAVAILABLE / FAIL` without computing a percentage. Ruff and mypy run unconditionally and report independently of the Tests outcome. A summary table and an overall PASS/FAIL are printed at the end; the process exit code reflects the overall result.
- `.github/workflows/ci.yml` runs on `ubuntu-latest` (no version matrix), installs Python 3.14 and `uv`, syncs dependencies with `uv sync --locked --group dev` (`--locked` fails the job if `uv.lock` is out of sync with `pyproject.toml`), and its only step of substance is `uv run python scripts/verify.py` — the identical command a developer runs locally, per `docs/technical/TOOLCHAIN_AND_CI.md` §9's "no separate CI-only check list" requirement.

## 5. Rules Provenance

Not applicable — this is simulation infrastructure and developer/CI tooling (`ARCHITECTURE.md` §15: "requires no Rule Card"), not a historical game rule.

## 6. Tests Added or Modified

68 tests across 6 files (unchanged from the initial pass — see file list in §3):

- `test_results.py` — `total` computation under zero/positive/negative modifiers, immutability, dice-order preservation.
- `test_expressions.py` — parameterized exact-mapping tests for every supported notation form and 16 distinct unsupported/malformed notations; non-string and `None` input.
- `test_seeded_rng.py` — deterministic reproduction against an independent reference `random.Random(seed)`; the `DEC-0002` sequence-number refinement; modifier handling; `dS`-shorthand equivalence; error cases and non-perturbation of the stream/sequence counter on rejection.
- `test_scripted_rng.py` — ordered value consumption; real aggregation over scripted values; exhaustion behavior; sequence-number parity with `SeededRNG`.
- `test_contract_parity.py` — both implementations satisfy the identical public contract.
- `test_base_rng.py` — exercises `_BaseRNG._raw_draw`'s `NotImplementedError` safety net directly.

**Not covered by a permanent automated test:** `scripts/verify.py`'s own orchestration logic (subprocess dispatch, PASS/FAIL/UNAVAILABLE aggregation). This was validated once, manually, via a temporary throwaway failing test (§8) rather than a permanent meta-test, since `scripts/` is developer tooling outside `TESTING_STRATEGY.md`'s scope (which governs `src/`), and the orchestration logic itself is a small, direct sequence of subprocess calls and string comparisons. Flagged in §11 as a conscious, documented gap rather than an oversight.

## 7. Exact Verification Commands Executed

Final, canonical form (what both a developer and CI now run):

- `uv run python scripts/verify.py`

Which internally runs, and which were also run individually while building it:

- `python -m coverage erase`
- `python -m coverage run --branch -m pytest`
- `python -m coverage json -q`
- `python scripts/check_coverage.py`
- `python -m ruff check src tests scripts`
- `python -m mypy`

Additionally, for this amendment specifically:

- `python -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))"` — validated the workflow file's YAML syntax and structure (caught and fixed the YAML 1.1 `on:` → boolean-`true` ambiguity by quoting the key as `"on":`; confirmed harmless to GitHub's own parser either way, but fixed for unambiguous correctness).
- A temporary test asserting `False` was added to `tests/rng/`, `scripts/verify.py` was run to confirm `Tests: FAIL`, `Coverage: UNAVAILABLE / FAIL`, `Ruff`/`mypy` still reporting independently, and `Overall: FAIL` with a non-zero exit code — then the temporary test was deleted and `scripts/verify.py` was re-run to confirm a clean return to all-PASS.

## 8. Verification Results

- **Tests:** 68 passed, 0 failed (final run).
- **Coverage:** 100% branch coverage, all files; differentiated gate (`src/rules/`: 0 files, trivially satisfied; `src/survivability/`: 0 files, trivially satisfied; core aggregate: 100.00%, ≥95% required) — **PASS**, now via an automated gate rather than manual inspection of `coverage report`.
- **Ruff:** clean (an import-order violation found during the initial pass was already fixed prior to this amendment; the negative-path drill also incidentally confirmed Ruff's `B011` rule catches `assert False`).
- **mypy --strict:** clean, 13 source files (now including `scripts/`).
- **Negative-path drill:** confirmed `scripts/verify.py` correctly reports `Tests: FAIL`, `Coverage: UNAVAILABLE / FAIL` (no percentage computed from a broken run), and an overall `FAIL` with exit code `1`, matching `docs/technical/TOOLCHAIN_AND_CI.md` §8's specified behavior exactly.
- **GitHub Actions workflow:** verified locally — YAML parses correctly; its verification step invokes the identical command just confirmed working locally. **Not verified via a live run** — no commit has been pushed to the `origin` remote (`https://github.com/espiercy/retro-dnd`), since doing so is an outward-facing action outside this task's local-verification scope. See §11.

## 9. Coverage Results

100% statement and branch coverage across all of `src/rng/`, confirmed both by `coverage report` and by the new automated differentiated gate:

```text
Name                     Stmts   Miss Branch BrPart  Cover
src\rng\__init__.py          5      0      0      0   100%
src\rng\errors.py            5      0      0      0   100%
src\rng\expressions.py      19      0      8      0   100%
src\rng\results.py          12      0      0      0   100%
src\rng\rng.py               39      0      4      0   100%
TOTAL                        80      0     12      0   100%

Differentiated coverage gate
src/rules/               0 files -- trivially satisfied
src/survivability/       0 files -- trivially satisfied
core (aggregate)         5 file(s) -- 100.00% (>= 95% required)
```

**One coverage exclusion exists** (unchanged from the initial pass), per `DEVELOPMENT_WORKFLOW.md` §5 item 10 / `TESTING_STRATEGY.md` §8:

- **Affected code:** the `RNG` Protocol class body (two method stubs) in `src/rng/rng.py`.
- **Uncovered behavior:** the stub bodies (bare `...`) are never executed, since `Protocol` is structural-typing-only and never instantiated.
- **Technical reason:** the standard, well-known pattern for `typing.Protocol` in coverage-instrumented Python projects.
- **Alternate verification:** `mypy --strict` verifies the type contract instead of a runtime test.
- **Approval:** self-evident mechanical case; not escalated for a decision record (`DEVELOPMENT_WORKFLOW.md` §9.2).

## 10. Deviations

None from `RNG_CONTRACT.md`'s mechanical specification (unchanged from the initial pass — see the `bool`-rejection judgment call noted there previously).

None from `docs/technical/TOOLCHAIN_AND_CI.md`'s specified verification behavior. One design choice made where the document left the mechanism open: `scripts/verify.py` runs Ruff and mypy unconditionally (independent of the Tests outcome), and reports a summary table, exactly as specified in `TOOLCHAIN_AND_CI.md` §8 — this is a direct implementation, not a deviation, noted here only because it was among the previously-open implementation choices.

## 11. Known Limitations/Unresolved Issues

- **No live GitHub Actions run has been confirmed.** The workflow is present, YAML-valid, and invokes the exact command already confirmed working locally — but nothing has been pushed to `origin` to trigger a real run on GitHub's infrastructure. Recommend pushing (with explicit go-ahead, since it's an outward-facing action) before treating the CI requirement as fully closed.
- **`scripts/verify.py`'s own orchestration logic has no permanent automated test** (§6) — its correctness was confirmed once, manually, via a temporary throwaway test during this session. A regression in the orchestration script itself (e.g., a future edit that accidentally makes Coverage evaluate even when Tests failed) would not be automatically caught. Acceptable for now given the script's small size and direct logic; worth revisiting if the script grows more complex.
- No RNG-state persistence exists (correctly deferred per `RNG_CONTRACT.md` §13).

## 12. Architectural Consequences

None to the approved module boundaries in `ARCHITECTURE.md` §13 (`src/`, `tests/`, `docs/`) — `scripts/` and `.github/workflows/` are new top-level directories for developer/CI tooling, not simulation modules, and were already anticipated in spirit by `docs/technical/TOOLCHAIN_AND_CI.md`. `ARCHITECTURE.md` §13's module-layout diagram has been updated to show them as created, for accuracy, but no boundary or invariant changed.
