# ISSUE-003: CLUSTER-001 Turn-Credit Contract (TurnCredit / TurnCreditOrigin)

## 1. Issue/Task Identifier and Objective

ISSUE-003 (completion-record ledger). Implement Step 1 of
`docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` (`IMPLEMENTATION PLAN
APPROVED`, human-approved 2026-08-18): the shared value contract between
`EXP-002` (producer) and `EXP-001` (consumer) — `TurnCreditOrigin` and
`TurnCredit` — with no mechanical behavior of either Rule Card implemented
yet.

## 2. Approved Inputs/Specifications

- `docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` §5, §6, §8 — the
  approved state/representation this issue implements (`Status:
  IMPLEMENTATION PLAN APPROVED`, human-approved 2026-08-18).
- `docs/rules/exploration/dungeon_turn_time_accounting.md` (`EXP-002`,
  Status: `APPROVED`, human-approved 2026-08-16) and
  `docs/rules/exploration/dungeon_wandering_monster_check.md` (`EXP-001`,
  Status: `APPROVED`, human-approved 2026-08-18) — the two Rule Cards
  whose interface this contract represents; neither card's own mechanical
  specification is implemented by this issue.
- `ARCHITECTURE.md` §15.2 — `CLUSTER-001` historical-rules implementation
  authorized 2026-08-18, scoped to the `EXP-001` + `EXP-002` boundary.
- Human implementation review: reviewed implementation commit
  `87d27d9cce7c236785c7f72e0e81cd7215c1b9ba`, `HUMAN-APPROVED — 2026-08-18`.

## 3. Files Created, Modified, or Deleted

**Created:**
- `src/rules/__init__.py`, `src/rules/exploration/__init__.py` — minimal
  package markers, no exports.
- `src/rules/exploration/turn_credit.py`
- `tests/rules/exploration/test_turn_credit.py`
- This completion record.

**Modified:** none.

**Deleted:** none.

Merged to `main` at `e5b1135d6978bcb25cac86b4ba820ac41e166c0d`.

## 4. Behavior Actually Implemented

- `TurnCreditOrigin`: a plain, closed two-member `enum.Enum` —
  `ORDINARY`, `ENCOUNTER_DERIVED` — with `auto()` values (no
  presentation-oriented strings, no additional or speculative origins).
- `TurnCredit`: an immutable, slotted, frozen dataclass —
  `turn_number: int`, `origin: TurnCreditOrigin` — representing exactly
  one authoritative whole dungeon-turn credit. `turn_number` is validated
  in `__post_init__` to be a positive `int` (`bool` explicitly excluded,
  matching this codebase's existing `src/rng/rng.py` int-vs-bool
  validation convention), raising `ValueError` otherwise.
- The Rule Cards' separate, *sequence-level* requirement — that a
  produced sequence of credits is strictly increasing and gapless — is
  **not** enforced by `TurnCredit` itself; a single, isolated instance
  has no way to observe prior credits. That invariant is a producer
  responsibility, implemented by `EXP-002`'s `DungeonTimeAccounting`
  (`ISSUE-004`, `docs/rules/exploration/dungeon_turn_time_accounting.md`),
  not by this shared value type. This is documented directly in
  `turn_credit.py`'s own docstring, not merely asserted here.
- No RNG, encounter, wandering-monster, presentation, or narrative data
  is carried by either type. No event bus or generalized message type was
  introduced.

## 5. Rules Provenance

Not a historical game rule in its own right — this is the shared
interface contract between two approved Rule Cards (`EXP-001`,
`EXP-002`), specified by the human-approved implementation plan rather
than by either Rule Card's own mechanical specification. No Provenance
Classification under `GAME_CONSTITUTION.md` §5 applies to this issue.

## 6. Tests Added or Modified

15 tests in `tests/rules/exploration/test_turn_credit.py`:

- **Origin representation** — `ORDINARY` and `ENCOUNTER_DERIVED` both
  exist; the origin set is closed to exactly those two values.
- **Construction** — an ordinary credit and an encounter-derived credit
  are each representable, with both fields preserved exactly as
  authoritative mechanical data.
- **Immutability** — mutating either field on an existing `TurnCredit`
  raises `dataclasses.FrozenInstanceError`.
- **Value semantics** (following naturally from the frozen dataclass, not
  separately implemented) — credits with identical fields compare equal;
  credits differing in `turn_number` or `origin` compare unequal.
- **Validation** — the smallest valid `turn_number` (`1`) is accepted;
  `0`, a negative value, a non-`int`, and `True` (a `bool`) are each
  rejected with `ValueError`.

## 7. Exact Verification Commands Executed

- `uv run python scripts/verify.py`

## 8. Verification Results

- **Tests:** all project tests passed on the reviewed branch (99 total at
  the time of this issue: 84 pre-existing `src/rng/` tests + 15 new).
- **Coverage:** PASS — differentiated gate: `src/rules/` 3 files, 100%
  required per file, met; core aggregate 100.00% (≥95% required).
- **Ruff:** clean.
- **mypy --strict:** clean. Two findings surfaced and were fixed during
  development: an `Enum`-literal non-overlapping-comparison finding
  (resolved by removing a test made redundant by the closed-two-value-set
  test, rather than working around the type checker) and an unused
  `type: ignore` comment (removed — `bool <: int` is statically valid, so
  mypy cannot itself catch the invalid-`bool`-`turn_number` case, which is
  exactly why the runtime check exists).
- **Overall: PASS.**

## 9. Coverage Results

`src/rules/exploration/turn_credit.py`: 13/13 statements (100%), 2/2
branches (100%) — both outcomes of `__post_init__`'s single validation
`if` (accept / reject) are exercised. `src/rules/__init__.py` and
`src/rules/exploration/__init__.py` carry no executable statements
(trivially 100%).

## 10. Deviations

None from the approved implementation plan's §5/§6 representation. One
implementation-shape choice made where the plan left the exact
representation open, not a deviation: the two types live in their own
small `turn_credit.py` module rather than inside either Rule Card's
future module, per the plan's own stated recommendation (§6) to avoid
forcing `EXP-001`'s module to import `EXP-002`'s module merely to obtain
the shared type.

## 11. Known Limitations/Unresolved Issues

None known. The sequence-level strictly-increasing/gapless invariant is
intentionally not enforced by this type (§4) — this is a documented
design boundary, not an open defect, and is satisfied by `ISSUE-004`'s
`DungeonTimeAccounting`.

## 12. Architectural Consequences

Establishes `src/rules/` and `src/rules/exploration/` as populated
packages for the first time (`ARCHITECTURE.md` §13's previously-empty
`src/rules/` bucket), mirroring the existing `docs/rules/exploration/`
naming. No boundary or invariant in `ARCHITECTURE.md` changed; the
module layout already anticipated this package.
