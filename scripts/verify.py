"""The project's single canonical verification operation.

Runs, in this order, and reports every applicable gate's outcome
independently (docs/technical/TOOLCHAIN_AND_CI.md §8):

    Tests -> Coverage Gates -> Lint -> Static Type Checking -> PASS/FAIL

Both local development and CI invoke exactly this script -- there is no
separate CI-only check list (docs/technical/TOOLCHAIN_AND_CI.md §9). Ruff
and mypy run regardless of whether Tests passed. Coverage is the one gate
that depends on a complete, valid test run: if Tests failed, Coverage is
reported UNAVAILABLE / FAIL rather than computing a percentage from a
broken run.

Usage:

    uv run python scripts/verify.py

Exits 0 if every gate passed, 1 otherwise.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CHECK_COVERAGE_SCRIPT = Path(__file__).resolve().parent / "check_coverage.py"
COVERAGE_JSON = REPO_ROOT / "coverage.json"

SRC_AND_TEST_PATHS = ["src", "tests", "scripts"]


def _run(*command: str) -> int:
    """Run a subprocess from the repo root, streaming its output live."""
    print(f"\n$ {' '.join(command)}")
    result = subprocess.run(command, cwd=REPO_ROOT, check=False)
    return result.returncode


def main() -> int:
    results: dict[str, str] = {}

    # Start from a clean slate so a previous run's data can never leak in.
    _run(sys.executable, "-m", "coverage", "erase")
    if COVERAGE_JSON.exists():
        COVERAGE_JSON.unlink()

    tests_exit = _run(sys.executable, "-m", "coverage", "run", "--branch", "-m", "pytest")
    results["Tests"] = "PASS" if tests_exit == 0 else "FAIL"

    # Coverage is only evaluated against a complete, valid test run. A
    # coverage percentage computed from a run where tests failed is not
    # meaningful evidence of anything (docs/technical/TOOLCHAIN_AND_CI.md §8).
    if tests_exit == 0:
        json_exit = _run(sys.executable, "-m", "coverage", "json", "-q")
        if json_exit == 0:
            coverage_exit = _run(sys.executable, str(CHECK_COVERAGE_SCRIPT))
            results["Coverage"] = "PASS" if coverage_exit == 0 else "FAIL"
        else:
            results["Coverage"] = "UNAVAILABLE / FAIL"
    else:
        results["Coverage"] = "UNAVAILABLE / FAIL"

    ruff_exit = _run(sys.executable, "-m", "ruff", "check", *SRC_AND_TEST_PATHS)
    results["Ruff"] = "PASS" if ruff_exit == 0 else "FAIL"

    mypy_exit = _run(sys.executable, "-m", "mypy")
    results["mypy"] = "PASS" if mypy_exit == 0 else "FAIL"

    overall_pass = all(status == "PASS" for status in results.values())

    print("\n" + "=" * 40)
    for name, status in results.items():
        print(f"{name + ':':<10} {status}")
    print(f"{'Overall:':<10} {'PASS' if overall_pass else 'FAIL'}")
    print("=" * 40)

    return 0 if overall_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
