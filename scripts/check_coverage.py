"""Differentiated branch-coverage enforcement (docs/technical/TOOLCHAIN_AND_CI.md §4, §10).

coverage.py's own `--fail-under` is a single global percentage; it cannot
express the project's *differentiated* thresholds. This script reads
`coverage.json` (produced by `coverage json`) and applies three
independent, AND'ed conditions:

    100% branch coverage, per file, under src/rules/
    100% branch coverage, per file, under src/survivability/
    >=95% branch coverage, in aggregate, across the rest of src/
      (the "simulation core" -- TESTING_STRATEGY.md §8)

Meeting the aggregate does not excuse a rules/survivability file falling
below 100%, and vice versa. A bucket with no matching files yet is
trivially satisfied (reported explicitly, not silently skipped).

This script trusts coverage.py's own accounting of `missing_lines` /
`missing_branches`, which already respects `# pragma: no cover`
exclusions (docs/technical/TOOLCHAIN_AND_CI.md §10) -- it does not
re-implement exclusion handling.

Usage (after `coverage run --branch -m pytest` and `coverage json`):

    uv run python scripts/check_coverage.py

Exits 0 if every applicable threshold is met, 1 otherwise, printing
exactly which file or bucket failed and why.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
COVERAGE_JSON = REPO_ROOT / "coverage.json"

CORE_AGGREGATE_THRESHOLD = 95.0
PER_FILE_100_PERCENT_BUCKETS = ("src/rules/", "src/survivability/")


def _normalize(path: str) -> str:
    return path.replace("\\", "/")


def _bucket_for(path: str) -> str:
    normalized = _normalize(path)
    for prefix in PER_FILE_100_PERCENT_BUCKETS:
        if normalized.startswith(prefix):
            return prefix
    return "core"


def _percent(covered: int, total: int) -> float:
    return 100.0 if total == 0 else (covered / total) * 100.0


def main() -> int:
    if not COVERAGE_JSON.exists():
        print(f"error: {COVERAGE_JSON} not found; run `coverage json` first", file=sys.stderr)
        return 1

    data: dict[str, Any] = json.loads(COVERAGE_JSON.read_text(encoding="utf-8-sig"))

    failures: list[str] = []
    per_bucket_file_count = dict.fromkeys(PER_FILE_100_PERCENT_BUCKETS, 0)

    core_statements = 0
    core_covered_statements = 0
    core_branches = 0
    core_covered_branches = 0
    core_file_count = 0

    for file_path, entry in data["files"].items():
        summary = entry["summary"]
        bucket = _bucket_for(file_path)

        if bucket in PER_FILE_100_PERCENT_BUCKETS:
            per_bucket_file_count[bucket] += 1
            missing_lines = entry.get("missing_lines", [])
            missing_branches = entry.get("missing_branches", [])
            if missing_lines or missing_branches:
                failures.append(
                    f"{file_path}: requires 100% branch coverage (bucket {bucket!r}) "
                    f"-- missing lines {missing_lines}, missing branches {missing_branches}"
                )
        else:
            core_file_count += 1
            core_statements += summary["num_statements"]
            core_covered_statements += summary["covered_lines"]
            core_branches += summary["num_branches"]
            core_covered_branches += summary["covered_branches"]

    core_percent = _percent(
        core_covered_statements + core_covered_branches,
        core_statements + core_branches,
    )

    print("Differentiated coverage gate")
    print("-" * 50)
    for bucket, count in per_bucket_file_count.items():
        if count == 0:
            print(f"{bucket:<24} 0 files -- trivially satisfied")
        else:
            print(f"{bucket:<24} {count} file(s) -- 100% required, per file")
    print(
        f"{'core (aggregate)':<24} {core_file_count} file(s) -- "
        f"{core_percent:.2f}% (>= {CORE_AGGREGATE_THRESHOLD:.0f}% required)"
    )

    if core_percent < CORE_AGGREGATE_THRESHOLD:
        failures.append(
            f"simulation core aggregate branch coverage {core_percent:.2f}% "
            f"is below the required {CORE_AGGREGATE_THRESHOLD:.0f}%"
        )

    if failures:
        print("\nFAILED:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print("\nAll differentiated coverage thresholds met.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
