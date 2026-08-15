# Retro D&D Simulator — Testing Strategy

## 1. Purpose and Principles

Testing is a development requirement, not a cleanup phase. Tests for a piece of rules behavior are written and run as part of implementing that behavior, not deferred to "later."

This project is simultaneously:

- a software system, which must be tested the way software normally is (correct inputs/outputs, boundaries, regressions), and
- an executable interpretation of a specific historical rules text, which must be tested against that text's actual mechanical content, not merely against "the code does what the code does."

A test suite that only exercises code paths without anchoring them to the approved Rule Card's mechanical content is inadequate, no matter how much of the code it executes.

Coverage and verification requirements in this document are not merely reporting expectations. Once the implementation toolchain is selected, they must be enforced as hard automated CI/build gates (§9), not left to voluntary compliance.

This document establishes requirements and expectations. It does not choose a language, test framework, or coverage tool — those are selected later, and this document's requirements apply regardless of which tooling is chosen.

## 2. Rules Procedure Testing

Every implemented historical rules procedure must have deterministic automated tests.

A Rule Card's documented test cases (`docs/rules/_template.md`, "Deterministic Test Cases") are part of the acceptance criteria for that procedure's implementation, not a separate, optional addition. No approved mechanical clause should exist without at least one automated test demonstrating it.

Where applicable to the procedure, tests must cover:

- every outcome or branch described by the approved Rule Card;
- boundary values;
- minimum and maximum die results;
- modifiers and exceptional cases;
- success and failure paths;
- explicitly prohibited behavior (what the procedure must *not* do);
- interactions with other procedures identified by the Rule Card;
- historical edge cases;
- survivability-policy interactions, where the procedure is one of the limited set permitted to accept a survivability policy (`ARCHITECTURE.md` §10).

## 3. Deterministic Randomness in Tests

Tests involving randomness must not depend on uncontrolled random behavior.

- Use fixed seeds, an injected deterministic RNG, or controlled/fake roll sequences, as appropriate to what is being tested.
- Tests must be reproducible: the same test run against the same code must always produce the same result.
- Do not write probabilistic tests that can occasionally fail merely due to random sampling (e.g., "run this 1000 times and expect roughly the right distribution" as the *sole* verification of a table).
- Where a random table or procedure is being tested, verify the deterministic mapping from possible roll inputs to results directly (e.g., "roll = 3 → result X", "roll = 18 → result Y") rather than relying only on statistical sampling. Statistical/property-based tests may supplement direct mapping tests but must not replace them for historically authoritative tables.

This mirrors the single-RNG-stream, injectable-and-seedable requirement in `ARCHITECTURE.md` §5: if production code cannot have its randomness controlled, it cannot be tested to this standard. The RNG abstraction's testability is a testing-strategy requirement as much as an architecture one.

## 4. Separation of Historical Procedures

Historically distinct procedures normally require independent test suites, matching the independent-callability requirement in `ARCHITECTURE.md` §4 and §9. For example, each of the following should have its own procedure-level tests rather than receiving coverage only indirectly through a large end-to-end test:

- wandering encounter checks;
- monster generation;
- number appearing;
- surprise;
- reaction;
- morale;
- combat;
- treasure generation;
- experience awards.

Integration tests (e.g., a full expedition or a full encounter resolving end-to-end) supplement procedure-level tests. They must not replace them — an integration test proves the pieces fit together; it does not, by itself, prove any individual piece is mechanically correct across its own branches and edge cases.

## 5. Survivability Invariants

The structural isolation described in `ARCHITECTURE.md` §10 must be backed by tests that actively prove it, not merely assumed from type signatures:

- **Reward invariance.** Identical canonical treasure-generation and XP inputs must produce identical reward results regardless of which survivability configuration is active. A test should assert this directly — run the same canonical procedure under at least two different survivability configurations (including "none") and assert the treasure/XP results are identical.
- **Indirect-modification detection.** Tests should also be able to detect indirect reward modification — for example, a survivability policy implemented by rerolling or suppressing canonical encounters in a way that changes which encounters (and therefore which treasure opportunities) occur. A practical approach: run the canonical encounter/treasure generation procedure independently of any survivability policy, record what it produced, then separately verify that enabling a survivability policy does not change that recorded canonical result — only what is *presented* or how *danger* is handled.

## 6. State and Persistence Testing

Once persistent state exists (`ARCHITECTURE.md` §7), tests must demonstrate the campaign consequences that make persistence meaningful, including:

- removed treasure remains removed after save/load;
- dead characters remain dead after save/load;
- discovered/explored state persists;
- altered dungeon state (opened doors, disarmed traps, etc.) survives save/load;
- state restoration is deterministic — loading the same saved state twice produces identical in-memory state.

No persistence tests are required before persistence is implemented; this section establishes the expectation for when that work begins.

## 7. Regression Tests

Every confirmed defect in historically significant behavior must receive a regression test, added before or alongside its fix whenever practical. A rules-implementation bug is not considered fully repaired unless a test exists that would fail if the bug were reintroduced.

Regression tests should be traceable to their origin (e.g., referencing the completion record or issue that fixed the defect — see `DEVELOPMENT_WORKFLOW.md`).

## 8. Coverage Expectations

Coverage percentage is a supporting metric, not a substitute for behavioral correctness. A module can report 100% code coverage and still be inadequately tested if its tests never establish that the historical rule was implemented correctly. The stronger requirement is semantic coverage: **every approved mechanical requirement must have automated verification demonstrating its intended behavior.** For historical Rule Cards, every approved mechanical clause must be represented by one or more meaningful automated tests.

Numeric thresholds are necessary but not sufficient, and — once the toolchain is selected — are enforced automated gates (§9), not aspirational targets:

- **100% branch coverage** for historically authoritative rules procedures, except where a specific exception is narrow, explicitly documented, technically justified, and human-approved.
- **100% branch coverage** for survivability transformations, subject to the same exception process. This is particularly important because survivability code is permitted to modify only narrowly authorized aspects of canonical game results (`ARCHITECTURE.md` §10).
- **At least 95% branch coverage** across the simulation core overall. The exact definition of "simulation core" is documented once the language/toolchain and module structure exist, but it includes at minimum the authoritative simulation/rules/state behavior — not presentation or peripheral tooling.

Coverage exclusions must be narrow and explicit (e.g., an annotated single line with a stated, technically justified reason), never a blanket exclusion of a file or module, and must never be used to hide rules behavior that is merely difficult to test.

A one-off approved coverage exception is documented in the relevant issue's completion record — affected code, uncovered branch/behavior, technical reason, and human approval (`DEVELOPMENT_WORKFLOW.md` §5 item 10) — together with a narrow inline annotation at the affected code when useful for discoverability. It does not, by itself, warrant a standalone decision record. A decision record is created only when an exception establishes or changes a reusable, project-wide testing policy rather than a single one-off case (`DEVELOPMENT_WORKFLOW.md` §9.2).

## 9. CI / Build Enforcement

Before production implementation is authorized, the selected toolchain must support automated execution of the applicable:

- unit tests;
- integration tests;
- regression tests;
- branch-coverage thresholds (§8);
- linting;
- static analysis;
- type checking, where applicable;
- other agreed verification gates.

A failed mandatory gate must make the build/verification process fail. An implementation issue must not be described as complete when any required gate fails (`DEVELOPMENT_WORKFLOW.md` §5.1).

Coverage results must never be presented as a meaningful pass when the underlying test run was incomplete or invalid. If tests fail, or test collection/instrumentation is otherwise incomplete, the Coverage gate must report as failed/unavailable rather than computing and displaying a percentage from partial execution — a coverage number derived from a broken run is misleading, not merely a lower score. See `docs/technical/TOOLCHAIN_AND_CI.md` §8 for the concrete reporting model.

This is one of the foundational items required before the Pre-Code Development Gate clears (`ARCHITECTURE.md` §16): the CI/build enforcement model appropriate to the selected toolchain must be approved, and operative, before production implementation of Issue 1 onward begins — not added retroactively once code already exists.

## 10. Verification Before Completion

Automated gates and completion records serve different purposes and are not interchangeable:

```text
Automated CI / Build Gates
        ↓
Objective enforcement
        ↓
Completion Record
        ↓
Durable report of what was verified and the results
```

- The automated gates (§9) are the objective enforcement mechanism: they run the tests, check coverage thresholds, and fail the build when a mandatory gate is not met. This is what actually prevents non-conforming work from being merged.
- The completion record (`DEVELOPMENT_WORKFLOW.md` §5, items 7–9) is the durable, human-readable report of what was run and what the results were. It documents that the gates passed; it does not itself substitute for them, and reporting alone — without the gates actually having run and passed — is not sufficient.

No implementation task is complete until the applicable unit, integration, and regression tests, static analysis/type checking, linting, and coverage checks have been run successfully, and the exact commands and results are recorded in that issue's completion record. An issue whose required verification has not been run, or whose required gates have failed, must not be represented as complete (`DEVELOPMENT_WORKFLOW.md` §5.1).

## 11. Tooling

No test framework, coverage tool, linter, or type checker is selected by this document. This document defines requirements that any selected tooling must be capable of satisfying (deterministic seeding, branch-coverage reporting, narrow exclusion annotations, CI-enforceable thresholds that fail the build on violation). Tooling selection is a separate decision, made later.

## 12. Status

This document is a proposed and approved testing standard (`docs/decisions/DEC-0001-project-foundation-baseline.md`), submitted as one of the foundational items in the Pre-Code Development Gate (`ARCHITECTURE.md` §16).
