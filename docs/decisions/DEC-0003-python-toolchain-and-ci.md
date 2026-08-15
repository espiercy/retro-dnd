# DEC-0003: Python Toolchain and CI

## Decision ID
DEC-0003

## Title
Python Toolchain and CI Enforcement Model

## Status
Approved

## Date
2026-08-15

## Context

Pre-Code Development Gate item 8 (`ARCHITECTURE.md` §16) required an approved automated verification/CI enforcement model appropriate to the project's implementation toolchain. A draft toolchain and CI design, `docs/technical/TOOLCHAIN_AND_CI.md`, was proposed and reviewed by the project owner, who approved it with specific refinements to the canonical verification behavior and the coverage-exception documentation process. This record captures the now-approved toolchain and CI model at a decision-log level; full technical detail remains in `docs/technical/TOOLCHAIN_AND_CI.md`.

## Decision

The following toolchain and CI model is approved:

```text
Python 3.14 (single pinned minor version)
pytest
coverage.py + project-specific coverage enforcement
Ruff (linting)
mypy (strict mode)
uv + pyproject.toml + committed uv.lock
GitHub (hosting)
GitHub Actions (CI)
```

Key enforcement properties:

- **One canonical local verification operation**, run identically by developers and by CI — Tests → Coverage Gates → Lint → Static Type Checking → PASS/FAIL. CI never maintains a separately defined set of checks.
- **All applicable gates run and report independently** in a single pass (a test failure does not suppress Ruff/mypy results), except that the **Coverage Gate depends on a complete, valid test run** — if tests fail or instrumentation is incomplete, Coverage reports `FAILED / UNAVAILABLE` rather than a misleading computed percentage. Any gate failing, including an unavailable Coverage Gate, fails the overall run.
- **Coverage enforcement is three independent, AND'ed conditions**: 100% branch coverage per file under `src/rules/`, 100% branch coverage per file under `src/survivability/`, and ≥95% branch coverage in aggregate across the simulation core. None of the three substitutes for another.
- **Coverage exceptions** are narrow, explicitly documented, technically justified, and human-approved; documented in the relevant completion record (affected code, uncovered behavior, technical reason, alternate verification if any, and approval), with an optional narrow inline annotation for discoverability. A reusable/project-wide exception policy requires its own decision record; a one-off exception does not.
- **mypy strict mode is the project-wide typing standard** and is not weakened globally for convenience; a specific rule proving impractical is handled as a narrow, documented, per-case exception, mirroring the coverage-exception convention.
- **`uv.lock` is committed to the repository**, alongside `pyproject.toml`, as part of the project's reproducibility model together with the pinned Python version and the deterministic RNG (`DEC-0002`).

## Rationale

A single canonical verification path that both developers and CI invoke identically is the only way to guarantee the two never drift apart (`TESTING_STRATEGY.md` §9–§10). Treating coverage as unavailable rather than computing a number from a broken run prevents a subtle failure mode — a red test suite producing a coincidentally-passing coverage report — that would otherwise let real problems slip past a gate meant to catch them. Pinning one Python version, committing the dependency lock file, and keeping the RNG deterministic (`DEC-0002`) together form one coherent reproducibility story: the project can say precisely what "a run" means at any point in its history. mypy and Ruff were chosen for a pure-Python, low-runtime-surface toolchain; `uv` was chosen to match Ruff's distribution model and collapse environment/dependency management into one tool rather than several.

Major alternatives considered and rejected or deferred:

- **`pytest-cov`** instead of direct `coverage.py` invocation — rejected; it's a thin wrapper primarily valuable under `pytest-xdist`, which this project isn't adopting, and direct invocation gives the project-specific enforcement layer more direct access to structured coverage data.
- **`pyright`** instead of `mypy` — a reasonable alternative, but rejected in favor of `mypy`'s pure-Python distribution, avoiding a second (Node-based) runtime in the verification path.
- **Stdlib `venv` + `pip` + a lock-file mechanism** instead of `uv` — remains a legitimate, more conservative fallback, but rejected in favor of `uv`'s single-tool coverage of environment creation, resolution, and locking, matching Ruff's distribution model.
- **A single global coverage `--fail-under` threshold** — rejected in favor of the three differentiated, independently-enforced thresholds, since a single global number cannot express "100% for rules/survivability, ≥95% overall" without hiding which part failed.
- **Fail-fast verification** (stopping at the first failing gate) — rejected in favor of running all applicable gates and reporting independently, so a developer sees every problem in one pass, except where a gate has a genuine data dependency on another (Coverage on Tests).

## Consequences

- Implementation of Issue 1 onward must create `pyproject.toml`, `uv.lock`, the canonical verification script/mechanism, and (once the GitHub remote is configured) a GitHub Actions workflow invoking that same script — none of which are created by this decision.
- The "project-specific coverage enforcement" layer referenced above does not yet exist as code; its precise shape (script vs. tool) is deferred to implementation (`docs/technical/TOOLCHAIN_AND_CI.md` §12).
- A code formatter, task runner, pre-commit hooks, and CI providers other than GitHub Actions remain explicitly out of scope for now (`docs/technical/TOOLCHAIN_AND_CI.md` §11).
- Full technical detail governing implementation remains `docs/technical/TOOLCHAIN_AND_CI.md`; this record does not replace it.

## Supersedes

None.

## Superseded By

None.
