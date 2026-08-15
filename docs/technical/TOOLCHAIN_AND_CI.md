# Toolchain and CI — Technical Design

## 1. Purpose

This document specifies the Python toolchain and automated verification/CI model for the Retro D&D Simulator, addressing Pre-Code Development Gate item 8 (`ARCHITECTURE.md` §16). The choices in this document have been approved by the project owner, subject to the refinements incorporated into this revision. The approval is recorded as `docs/decisions/DEC-0003-python-toolchain-and-ci.md`, which summarizes this document and references it rather than duplicating it.

This remains a design document, not an implementation. No dependencies are installed and no configuration files (`pyproject.toml`, `uv.lock`, CI workflow files, coverage/lint/type-checker config) are created here. Those are implementation-assignment artifacts, created only once production implementation is separately authorized (`ARCHITECTURE.md` §16).

Status legend used throughout:
- **[APPROVED]** — decided by the project owner.
- **[DEFERRED]** — intentionally not decided yet; see §11.

## 2. Python/Runtime

**[APPROVED]** Implementation language: Python.

**[APPROVED]** Target a single pinned Python minor version — **Python 3.14** — for the vertical slice, with no multi-version compatibility matrix.

Purpose of pinning one version: deterministic developer/CI behavior, simple tooling support, reproducible environments, and a clear supported-runtime contract. Do not introduce support for multiple Python versions unless later explicitly authorized.

This pin also grounds the RNG contract's reproducibility guarantee (`docs/technical/RNG_CONTRACT.md` §9): determinism is guaranteed within this supported runtime version, not promised indefinitely across future Python versions.

## 3. Test Tooling

**[APPROVED]** `pytest`.

No additional pytest plugins are recommended at this stage — specifically, not `pytest-randomly` (test-order randomization) and not `pytest-xdist` (parallel execution). Both are plausible future additions, but neither is needed for the first vertical slice, and adding either now would be infrastructure ahead of a demonstrated need (`ARCHITECTURE.md` §13). Revisit if suite size or flakiness gives a concrete reason.

## 4. Coverage Tooling and Enforcement

**[APPROVED]** `coverage.py`, invoked directly (`coverage run --branch -m pytest`), plus a **project-specific coverage enforcement layer** on top of it.

`coverage.py` alone provides one global `--fail-under` percentage; it does not natively support the project's *differentiated* per-path thresholds (§10). The project-specific enforcement layer is a small piece of verification logic (exact mechanism is part of the canonical verification workflow, §8, and remains to be built at implementation time) that consumes `coverage.py`'s structured output (`coverage json`) and independently evaluates:

- 100% branch coverage per file under `src/rules/`;
- 100% branch coverage per file under `src/survivability/`;
- ≥95% branch coverage in aggregate across the simulation core.

Branch coverage (not just statement/line coverage) is enabled (`coverage.py`'s `branch = true`), since all three thresholds above are branch-coverage thresholds. See §10 for the full enforcement model and exception convention.

## 5. Lint Tooling

**[APPROVED]** Ruff, for linting.

**[DEFERRED]** Adopting `ruff format` (or any other formatter). Formatting enforcement is not part of the approved toolchain direction. Ruff's formatter is available at zero additional-dependency cost whenever the project owner wants to decide on it (§11).

## 6. Static Type Checking

**[APPROVED]** `mypy`, run in strict mode (`--strict`) against `src/`.

The project's typing standard is strict mode, project-wide, from the start. Strict mode must not be weakened globally merely to make implementation easier. If a specific strict-mode rule later proves inappropriate for a concrete, technically justified reason, that is handled as a narrow, documented, per-case exception — e.g., a scoped `# type: ignore[specific-error-code]` with a comment explaining why — mirroring the coverage-exception convention (§10), rather than by relaxing the project's mypy configuration broadly.

## 7. Dependency/Environment Management

**[APPROVED]** `uv`, with project metadata and dependencies declared in `pyproject.toml` (PEP 621), and the resulting resolved environment committed as `uv.lock`.

```text
pyproject.toml
    ↓
Project metadata and declared dependencies

uv.lock
    ↓
Exact resolved dependency environment
    ↓
Committed to repository
```

The lock file is part of the project's reproducibility model (alongside the pinned Python version, §2, and the deterministic RNG, `docs/technical/RNG_CONTRACT.md`) and must be committed to the repository, not gitignored — an uncommitted lock file would let dependency drift back in through the one place this project has otherwise designed it out.

Neither `pyproject.toml` nor `uv.lock` is created by this document; both are implementation-assignment artifacts, created only once production implementation is separately authorized (`ARCHITECTURE.md` §16).

## 8. Canonical Local Verification Workflow

There is exactly one command a developer runs locally that performs the same checks, in the same order, that CI enforces (§9). The exact implementation mechanism remains open (§11); the following behavior is specified regardless of that choice:

```text
Canonical Verification
        ↓
Tests            (pytest, run under coverage instrumentation: `coverage run --branch -m pytest`)
        ↓
Coverage Gates   (project-specific enforcement, §4/§10 — evaluated from the run above)
        ↓
Lint             (`ruff check`)
        ↓
Static Type Checking   (`mypy --strict`)
        ↓
PASS / FAIL
```

**All applicable gates run and report independently**, to give the developer as much useful failure information as possible in one pass. A test failure must not, by itself, prevent Ruff or mypy from reporting their own independent findings in the same run — neither depends on the test run succeeding.

**Coverage is the one gate that depends on Tests having produced a complete, valid run.** If tests fail, or test collection/instrumentation is incomplete for any reason, the coverage data from that run is not valid evidence of anything, and the Coverage Gate must report:

```text
FAILED / UNAVAILABLE
```

rather than computing and displaying a percentage from partial or invalid execution — a coverage number computed from an incomplete run is misleading, not merely "a lower score," and must never be presented as if it were a meaningful measurement. The overall verification result is failure whenever any gate — including a `FAILED / UNAVAILABLE` Coverage Gate — did not pass.

Example of the required reporting shape:

```text
Tests:    FAIL
Coverage: UNAVAILABLE / FAIL
Ruff:     PASS
mypy:     FAIL

Overall:  FAIL
```

Further design decisions:

- **The command takes no required arguments** and needs no setup beyond having the environment created (`uv sync`, §7) — clone, create the environment, run the one verification command.
- **A pinned Python version (§2)** is used both locally and in CI, so there is exactly one environment definition to reason about, not a matrix.

## 9. CI Execution Model

**[APPROVED]** GitHub, hosting the repository; **GitHub Actions**, as the CI provider, invoking the same canonical verification operation from §8 as its only job step of substance (plus environment setup via `uv`).

```text
Developer
    ↓
Canonical verification command

GitHub Actions
    ↓
Same canonical verification command
```

CI must not maintain a second, independently defined list of checks that can drift from local verification. No local/CI behavioral difference is currently identified as necessary; if one ever is, it must be expressed as a documented parameter to the one canonical command, not as separate CI-only logic.

A failed mandatory gate fails the CI job — including a `FAILED / UNAVAILABLE` Coverage Gate (§8). There is no "warn only" mode for any gate.

CI runs on the single pinned Python version (§2) — no version matrix.

No GitHub Actions workflow file is created by this document; that is an implementation-assignment artifact.

## 10. Coverage-Exception Handling

Coverage thresholds are evaluated per path, not as one global percentage (§4):

```text
Rules file coverage = 100%
        AND
Survivability file coverage = 100%
        AND
Simulation core aggregate >= 95%
        ↓
Coverage gate passes
```

All three conditions are mandatory and independent. Satisfying the ≥95% aggregate does not excuse a `src/rules/` or `src/survivability/` file falling below 100%; perfect coverage in those modules does not excuse the aggregate falling below 95%.

A coverage exclusion exists to represent a genuinely approved technical exception — **it is not a mechanism for making CI green.** A one-off exception must be narrow, explicitly documented, technically justified, and human-approved. The relevant issue's completion record (`DEVELOPMENT_WORKFLOW.md` §5 item 10) must document:

- affected file/location;
- affected branch or behavior;
- why normal automated coverage is impractical or inappropriate;
- what alternate verification exists, if relevant;
- who/what human approval authorized the exception.

A narrowly placed coverage-exclusion annotation (`coverage.py`'s `# pragma: no cover`, restricted to the specific uncovered line(s) only — never a whole function, class, or file) may then reference the corresponding issue/completion record for discoverability:

```python
if impossible_state:  # pragma: no cover — see ISSUE-004 completion record, approved 2026-xx-xx
    raise AssertionError("unreachable: ...")
```

Do not introduce broad exclusions, and do not exclude an entire historically significant module merely because it is difficult to test. A reusable/project-wide exception policy — as opposed to a single one-off case — requires its own decision record rather than an issue-level waiver (`DEVELOPMENT_WORKFLOW.md` §9.2).

The verification operation does not currently attempt to automatically validate that every `# pragma: no cover` annotation carries a reference comment — a reasonable future enhancement, not a requirement of this design.

## 11. Deferred Tooling Decisions

Not decided by this document, and not needed for the first vertical slice:

- A code formatter (`ruff format` or otherwise).
- The exact mechanism for the canonical verification command (§8) — a small Python script vs. a task runner (`nox`, `invoke`) vs. a `Makefile`. A plain Python script remains the working assumption; revisit only if it proves insufficient.
- The precise implementation shape of the project-specific coverage-enforcement layer (§4/§10) — e.g., a standalone script parsing `coverage json` output vs. a small local tool.
- Test-order randomization (`pytest-randomly`) or parallelization (`pytest-xdist`).
- Pre-commit hooks (e.g., the `pre-commit` framework) — the canonical verification command (§8) is the enforcement point; a pre-commit hook running the same command locally is a plausible convenience layer to add later, not a requirement now.
- Release/packaging/distribution tooling — not relevant before there is a distributable artifact.
- Any dependency beyond pytest, coverage.py, Ruff, and mypy.

## 12. Remaining Open Items

None of the following block treating this document's toolchain direction as approved (`docs/decisions/DEC-0003-python-toolchain-and-ci.md`); they are implementation-phase decisions deferred to Issue 1 or later, listed here for visibility:

1. The exact mechanism for the canonical verification command (§11).
2. Whether to adopt a code formatter (§5, §11).
3. The precise implementation shape of the project-specific coverage-enforcement layer (§4, §11).
