# ISSUE-021: Stage-A Evidence-Integrity Gates and Structural Linter

## 1. Issue/Task Identifier and Objective

Human-assigned research-process remediation, 2026-09-30. `CLUSTER-004` Stage A required
**five** independent completeness reviews (four `FAIL`) before both evidence packets passed.
The independent-review gate worked; the researcher workflow did not.

Objective: diagnose the recurring failure and make the correct research behaviour **harder
to skip and easier to verify** — without making `DEC-0010` longer, and without weakening the
independent-review gate that worked.

A completion record is written although this work touches no `src/` file
(`DEVELOPMENT_WORKFLOW.md` §3.1 requires one for changes under `src/`, and directs erring
toward writing one otherwise): the change adds a **new gate to the canonical verification
path**, which is behaviour a future developer needs the durable record of.

## 2. Approved Inputs/Specifications

- **Rule Card(s): none.** No Rule Card was researched, drafted, implemented or modified.
- **Decision record produced by this work:**
  `docs/decisions/DEC-0012-stage-a-evidence-integrity-gates.md`, `Proposed — awaiting human
  approval`. An agent may not approve a project-wide process decision (`AGENTS.md` §12,
  `DEVELOPMENT_WORKFLOW.md` §9).
- **Governing inputs inspected directly, not from memory:** `DEC-0009`, `DEC-0010`,
  `DEC-0011`, `AGENTS.md`, `DEVELOPMENT_WORKFLOW.md`, `TESTING_STRATEGY.md`,
  `SOURCE_HIERARCHY.md`, `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md`,
  `docs/rules/_template.md`, `docs/rules/RESEARCH_PROCESS_PRECEDENTS.md` (`P-001`, `P-002`),
  `docs/technical/TOOLCHAIN_AND_CI.md`, `docs/rules/INVENTORY.md`, and all five
  `docs/rules/evidence/CLUSTER-004-stage-a-completeness-review*.md` artifacts.
- **Authorization boundary:** governance/protocol documentation, evidence template,
  evidence-linter script, linter tests, canonical-verification integration, and root-cause
  documentation. **Not authorized:** new rules research, Stage-A work on any card, Rule Card
  synthesis, production game-rule implementation, source adjudications, pushing to
  `origin/main`.

## 3. Files Created, Modified, or Deleted

**Created**

- `docs/decisions/DEC-0012-stage-a-evidence-integrity-gates.md` — root-cause analysis, the
  new gates, and the check-to-failure map.
- `docs/rules/evidence/_TEMPLATE.md` — canonical Stage-A evidence-packet template.
- `scripts/lint_evidence.py` — structural linter (research tooling, not simulator code).
- `tests/tooling/test_lint_evidence.py` — 71 tests for the linter.
- `tests/tooling/fixtures/` — `README.md` (stating plainly that none of it is evidence),
  one conforming new packet (`TEST-900-evidence-compliant.md`) and three malformed ones
  (`-absence`, `-coverage`, `-skeletal`).

**Modified**

- `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` — §5.1, §9.2.1, §9.3.1, §9.9, §9.10, §10.1.3,
  §10.4, §10.5, §10.6, §11.1, §11.2 added; §3 and §9.1.1 sequences amended identically; §6
  gains two labels; §17 gains two hard stops; §19 records the amendment.
- `AGENTS.md` — §10 items 11–15 (the binding agent-facing summary of the new gates).
  Protected document; edited under the explicit human direction §12 requires.
- `docs/decisions/DEC-0010-primary-source-completeness-audit.md` — `Superseded By` records
  that item 13's *sequence* is superseded as amended. Its decision text is **not** rewritten.
- `docs/decisions/INDEX.md` — `DEC-0012` row.
- `docs/rules/RESEARCH_PROCESS_PRECEDENTS.md` — `P-001` recorded **ELEVATED**; `P-002`
  recorded partially covered and still not elevated; both prior status blocks preserved with
  dated forward notes.
- `docs/technical/TOOLCHAIN_AND_CI.md` — §8 gate diagram, gate description and example
  reporting shape include the `Evidence` gate.
- `scripts/verify.py` — `Evidence` gate added, reporting independently.
- `pyproject.toml` — pytest `pythonpath` gains `scripts` so the tool is importable under
  test. Coverage `source` is unchanged (`src` only).
- `DEVELOPMENT_WORKFLOW.md` — §9.4's supersession illustration used `DEC-0012` as an
  invented placeholder ID. A real `DEC-0012` now exists and supersedes nothing, so that
  example asserted something false about real records; corrected in place to this
  repository's own real supersession (`DEC-0004` → `DEC-0005`), which §9.4 permits as a
  clerical fix. **A defect introduced by this work, found by checking references rather
  than assuming them.**

**Deleted** — none.

## 4. Behavior Actually Implemented

`uv run python scripts/verify.py` now runs a fifth gate, `Evidence`, which fails
verification when a Stage-A evidence packet under `docs/rules/evidence/` lacks a required
research instrument or contradicts its own coverage ledgers. Eighteen checks (`E001`–`E018`),
each traceable to a recorded `CLUSTER-004` review finding.

The checks that carry the most weight, because each catches a defect that survived multiple
passes and at least one independent review:

- `E006` — a page carrying an evidence row must appear as `IMAGE-VERIFIED` or
  `ACCESS-BLOCKED`. RC p. 84 carried evidence row `E-43` and appeared on neither coverage
  list across three passes.
- `E008` — an `ACCESS-BLOCKED` page forces `STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED`
  and forbids an `EVIDENCE READY FOR HUMAN REVIEW` recommendation.
- `E009` — a `BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED` closure item forbids an
  `EVIDENCE READY` recommendation.
- `E011` — absence asserted in prose with no Negative Claim Record behind it.
- `E016` — repository-fact rows must exist, and an `UNVERIFIED PROJECT FACT` blocks the gate.

**The gate is live, not inert.** Every real packet is grandfathered, so a linter governing
only real packets would lint zero files and pass vacuously — a green check that inspected
nothing, which is worse than no check because it is read as enforcement. Therefore:

- the **canonical template is linted as a reference packet on every run** (a real committed
  artifact, and the thing every future packet is copied from); its absence is itself a
  finding, since §11.2 requires it;
- the gate **states explicitly** when it has checked only the reference packet, so
  `Evidence: PASS` is never mistaken for *"a real packet was verified"*;
- a **conforming new packet and three malformed ones** are proven by fixtures under
  `tests/tooling/fixtures/` — deliberately **not** in `docs/rules/evidence/`, so a
  fabricated packet can never be mistaken for real research or reached by the directory
  scan;
- the script takes an optional directory argument so **the enforcement path is tested by
  exit code**, as a subprocess, not only in-process.

**What the linter deliberately does not do:** read the primary source, judge whether
research is correct, or judge interpretation, ownership or synthesis. It checks arithmetic,
set membership and string presence. Verbatim source transcriptions inside fenced blocks are
excluded from prose checks, so RC's own wording is never linted as the researcher's.

## 5. Rules Provenance

**Not applicable — research-process tooling and governance only.** No rule was researched,
interpreted, specified or implemented. No provenance classification arises. The `NOT YET
ESTABLISHED` and `REPOSITORY FACT — NOT A SOURCE CLAIM` labels added to the §6 *confidence*
vocabulary are research-evidence classifications, not rules provenance categories, and
`SOURCE_HIERARCHY.md` §10's provenance set is untouched.

## 6. Tests Added or Modified

`tests/tooling/test_lint_evidence.py` — 58 tests. Each check has a passing and a failing
case, the failing case built from the recorded defect wherever it reproduces in miniature:

- **Baseline** — a minimal conforming packet must lint clean, so any finding in a mutated
  copy is attributable to that mutation alone.
- **`test_template_is_a_conforming_packet`** — the canonical template must pass its own
  linter. Otherwise a researcher who follows it starts red and learns to ignore the gate.
- **`test_all_required_sections_are_named_by_the_protocol_template`** — the linter matches
  on section names, so linter and template cannot drift apart silently.
- **Per-check pairs** — including `E006`'s missing-page case asserting p. 84 is named in the
  message, `E008`'s three-way behaviour, `E009`'s `BLOCKED` interaction, `E011`'s
  absence-without-record case, and `E016`'s wrong-owner case.
- **False-positive guards** — a prohibited certification *named in order to warn against it*
  is allowed (`E004`); absence wording inside a verbatim quotation is not a finding
  (`E011`); `MORE PRIMARY RESEARCH REQUIRED` as a §11 recommendation is not a bare hard-stop
  label (`E015`). Two of these were written after the checks produced real false positives
  on the template, and both linter bugs were fixed rather than the template bent around them.
- **`test_grandfather_list_is_exactly_the_pre_dec_0012_packets`** — pins the closed
  exemption list, so adding a packet requires changing a test and is visible in review.
- **`test_repository_evidence_directory_currently_passes`** — the gate must be green on a
  clean tree, or it is noise.
- **Liveness** — `test_repository_run_actually_lints_the_reference_packet` (the gate must
  inspect at least one artifact) and `test_missing_reference_packet_fails_the_gate`.
- **New-packet fixtures** — the conforming fixture must lint clean; the three malformed
  fixtures must fail their designed checks (`E010`/`E011`, `E006`/`E009`, and `E001`/`E002`/
  `E005`/`E017`).
- **Grandfathering cannot expand silently** — a new packet beside exempt ones is still
  linted, and a name *resembling* an exempt packet
  (`EXP-006-evidence-remediated-pass-6.md`) does not inherit the exemption.
- **End-to-end exit codes** — the script is run as a subprocess against prepared
  directories: exit 0 for a conforming one, **exit 1** for a malformed new packet, exit 0 on
  the repository itself. Plus `test_canonical_verification_invokes_the_evidence_gate`,
  which pins the integration point in `verify.py`.
- **Fixtures are not evidence** — `test_fixtures_are_not_in_the_evidence_directory`
  asserts no `TEST-900*` file exists under `docs/rules/evidence/`.

No existing test was modified.

## 7. Exact Verification Commands Executed

`uv` was **not on `PATH` in this session's shell**, so each gate was executed with the
project's own pinned virtualenv interpreter, which is what `uv run` invokes:

- `.\.venv\Scripts\python.exe scripts/verify.py` (the canonical operation, all gates)
- `.\.venv\Scripts\python.exe -m pytest tests/tooling -q`
- `.\.venv\Scripts\python.exe -m ruff check src tests scripts`
- `.\.venv\Scripts\python.exe -m mypy`
- `.\.venv\Scripts\python.exe scripts/lint_evidence.py`

Toolchain confirmed as the pinned versions: Python 3.14.2, pytest 9.1.1, mypy 2.3.1,
ruff 0.16.3, coverage 7.15.4.

## 8. Verification Results

Canonical verification — `.\.venv\Scripts\python.exe scripts/verify.py`:

```text
Tests:     PASS      1063 passed  (992 pre-existing + 71 new)
Coverage:  PASS
Ruff:      PASS
mypy:      PASS      no issues in 49 source files
Evidence:  PASS      reference packet 1, Stage-A packets 0, grandfathered 12
Overall:   PASS
```

The `Evidence` gate's own output:

```text
reference packet linted:  1  (_TEMPLATE.md)
Stage-A packets linted:   0
Stage-A grandfathered:    12
  _TEMPLATE.md (reference)                     PASS

Every linted Stage-A packet carries its required instruments.
No post-DEC-0012 Stage-A packet exists yet, so only the reference
packet was checked. This gate is live but has not yet governed a
real packet -- see DEC-0012 consequence 7 on grandfathering.
```

**An earlier iteration of this work reported `0 packets linted`, which was a real defect:
the gate passed without inspecting anything.** It now lints a real committed artifact on
every run, and says plainly that no post-`DEC-0012` packet exists yet rather than letting a
green check imply one was verified. That a conforming new packet passes, and malformed ones
fail with a non-zero exit code, is proven by fixtures and subprocess tests.

## 9. Coverage Results

```text
src/rules/          18 file(s) -- 100% branch coverage required, per file -- met
src/survivability/   0 files   -- trivially satisfied
core (aggregate)     5 file(s) -- 100.00%  (>= 95% required)
```

Unchanged by this work, and necessarily so: `coverage.run.source` remains `["src"]`, and
`scripts/lint_evidence.py` is peripheral tooling, which `TESTING_STRATEGY.md` §8 explicitly
places outside the simulation core (*"not presentation or peripheral tooling"*). The linter
is nonetheless covered behaviourally by 58 tests.

## 10. Deviations

**Two additions beyond the letter of the assigning task**, both flagged for human review
rather than treated as settled:

1. **Two labels added to the §6 confidence vocabulary** — `NOT YET ESTABLISHED` (required by
   the Negative Claim Gate the task specified) and `REPOSITORY FACT — NOT A SOURCE CLAIM`.
   The second was not requested. `CLUSTER-004` review 5 Finding 8 found four cells where a
   project fact had been forced into a source-confidence column, and stated that forcing a
   §6 label would be worse than the plain wording. Without a label, the Repository Fact Gate
   and the vocabulary check would contradict each other.
2. **`P-002` was not elevated**, only partially covered, and its general half now binds for
   primary-source claims through §10.4. Its alternate-source front-matter requirement is a
   `DEC-0011` obligation, and alternate-source research was outside authorization.

**No coverage exception was requested or taken.**

## 11. Known Limitations/Unresolved Issues

1. **`DEC-0012` is `Proposed`, not `Approved`.** The protocol sections are in the repository
   and the linter gate is live, but the governance record binding them is awaiting human
   approval. The Stage-A research freeze it records remains in force until then.
2. **Four `CLUSTER-004` failure classes remain outside mechanical checking**, stated rather
   than glossed: stale self-description, an elision inside a verbatim quotation, a governing
   object nobody enumerated, and any judgement about whether research is *correct*. These
   remain the independent reviewer's and the human owner's work.
3. **The linter cannot verify that a Coverage Manifest was written *before* its conclusions.**
   §9.3.1 prohibits retroactive reconstruction; only commit history or a reviewer can detect
   a violation.
4. **`E011`/`E012` use a narrow literal phrase list.** A paraphrased absence claim
   (*"nothing in the source addresses…"*) will not be caught. Broadening the patterns trades
   false negatives for false positives; the list was kept narrow deliberately and can be
   extended when a real miss is observed.
5. **The efficiency claim is a prediction, not a measurement.** Whether this reduces
   `CLUSTER-005` to one independent review is unknown until a cluster runs under it.
   `DEC-0012`'s rationale states the falsification condition: if the next cluster still needs
   four `FAIL` cycles, the diagnosis was wrong and should be revisited rather than reinforced.
6. **A worktree-coordination collision occurred and was contained.** Two parallel Claude
   tasks shared this worktree; a branch checkout by this task changed the branch under the
   parallel `EXP-006` Stage-B task, so its commit `6ee30b8` landed on
   `stage-a-research-process-remediation`. I moved this branch back to `main`'s tip with
   `git reset --mixed e7651af`, which left `6ee30b8` reachable only from
   `cluster-004-exp-006-stage-b`. **Nothing was lost**, and `6ee30b8` is now a **sibling**
   of this branch (merge-base `e7651af`, neither an ancestor of the other). The parallel
   task has since been given its own worktree at
   `C:/Users/evanp/source/repos/OD_N_D-cluster-004-exp-006-stage-b`. **Integrating
   `6ee30b8` is explicitly not this task's work**, and no CLUSTER-004 Stage-B artifact was
   modified to repair the collision.
7. **Pre-existing working-tree state from a concurrent session was left untouched** — a
   modified `docs/rules/INVENTORY.md` and an untracked
   `docs/rules/exploration/light_and_exploration_resources.md` (the authorized `EXP-006`
   Stage-B card). Neither was staged, committed or edited by this work.

## 12. Architectural Consequences

The canonical verification operation gains a **fifth independently reported gate**. This is
the first gate that verifies **documentation** structure rather than code, and it establishes
the pattern: research-process tooling lives in `scripts/`, is type-checked and linted like
production code, is tested behaviourally, and is excluded from the coverage buckets that
govern `src/rules/` — because it is not rules behaviour and must never be mistaken for it.

`ARCHITECTURE.md` §16's Pre-Code Development Gate and §15.2's migration gate are untouched.
No production simulator module, Rule Card or rules test was created or modified.
