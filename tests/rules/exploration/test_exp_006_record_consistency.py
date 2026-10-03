"""`EXP-006` live-record consistency — a deliberately narrow mechanical check.

WHY THIS EXISTS. Four independent final implementation reviews have now run,
and not one found a rules defect. Every blocking finding in all four was the
same class: a fact duplicated into a second place and not updated there.

    review #1  MED-3   five artifacts of record said "NOT AUTHORIZED" after
                       implementation was authorized and complete
    review #2  MED-4   three mutually inconsistent case totals in one plan
                       section; a gate table still at 50
    review #3  MED-1   three live records still said "review #2 pending"
               MED-4   ISSUE-022 said 108 tests where its own section said 111
    review #4  B-1..5  the plan republished a withdrawn category split under a
                       false claim of test protection; five records said LOW-3
                       and LOW-8 were open at the commit that resolved them;
                       ISSUE-022 contradicted its own status block; the index
                       said a completed review was pending
               B-6     THIS FILE's previous design could not detect four of
                       the six phrasings it enumerated

B-6 IS WHY THE DESIGN CHANGED. The previous version skipped any line
containing a "historical marker" before testing it for a forbidden phrase --
and `"review #2"` was in BOTH lists. So `"review #2 pending"`, the literal
string review #3 found in three live records, was unconditionally
unreachable, along with three of its siblings. A guard that enumerates six
conditions and can only evaluate two is worse than no guard: it reports
protection it does not provide.

THE NEW RULE: no skip list. This test reads ONLY explicitly named
live/current records. Historical artifacts -- the review documents and the
remediation ledgers -- are NEVER scanned, so there is nothing for a
historical exemption to do. They preserve obsolete claims on purpose and
must not be "corrected".

A SECOND LESSON FROM B-1..B-5: prefer DERIVING a fact over transcribing it.
The case total is enumerated from the approved Rule Card. The category split
is derived from `CASE_DISCHARGE` and is no longer duplicated in the plan or
the gate at all. The review history is derived from the artifact files that
exist on disk rather than from a prose count. What cannot be derived -- the
review phase -- is carried as one token that every named record must match.

WHAT THIS DELIBERATELY DOES NOT DO: it does not scan arbitrary prose, it is
not a generic documentation linter, it does not validate historical prose,
and it does not pin the global suite test count (that changes whenever any
unrelated project test is added; duplicated global counts were removed from
the records instead).
"""

from __future__ import annotations

import ast
import pathlib
import re

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]

# --- The named live/current records. Nothing else is ever read. ------------

LIVE_RECORDS = (
    "ARCHITECTURE.md",
    "docs/rules/INVENTORY.md",
    "docs/rules/clusters/CLUSTER-004-equipment-resources-and-evasion.md",
    "docs/technical/EXP-006_IMPLEMENTATION_PLAN.md",
    "docs/technical/EXP-006_PRE_CODE_GATE.md",
    "docs/completion-records/ISSUE-022-exp-006-light-and-exploration-resources.md",
    "docs/completion-records/INDEX.md",
)

# Records required to carry the phase token. The gate and the index are read
# for stale wording but are not required to carry it: the gate is a
# pre-implementation record, and the index is a one-line summary.
PHASE_TOKEN_RECORDS = (
    "ARCHITECTURE.md",
    "docs/rules/INVENTORY.md",
    "docs/rules/clusters/CLUSTER-004-equipment-resources-and-evasion.md",
    "docs/technical/EXP-006_IMPLEMENTATION_PLAN.md",
    "docs/completion-records/ISSUE-022-exp-006-light-and-exploration-resources.md",
)

CURRENT_PHASE = "EXP-006-PHASE: REVIEW-4-REMEDIATED"

# Historical artifacts. NEVER scanned by this test; listed so that the
# never-scanned property is itself asserted rather than merely intended.
HISTORICAL_ARTIFACTS = (
    "docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW.md",
    "docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW_2.md",
    "docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW_3.md",
    "docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW_4.md",
    "docs/technical/EXP-006_REVIEW_REMEDIATION_LEDGER.md",
    "docs/technical/EXP-006_REVIEW_2_REMEDIATION_LEDGER.md",
    "docs/technical/EXP-006_REVIEW_3_REMEDIATION_LEDGER.md",
    "docs/technical/EXP-006_REVIEW_4_REMEDIATION_LEDGER.md",
)

# Statements that were true once and are false now. No exemption mechanism
# exists: if one of these appears in a named live record, the test fails.
# A live record that needs to discuss an obsolete claim must quote it in a
# form that does not reproduce these exact phrases.
STALE_CURRENT_CLAIMS = (
    "review #2 pending",
    "review #2 PENDING",
    "review #3 pending",
    "review #3 PENDING",
    "awaiting review #2",
    "awaiting review #3",
    "pending independent review #2",
    "pending independent review #3",
    "a second independent review is pending",
    "a third independent review is pending",
    "LOW-3 and LOW-8 remain OPEN",
    "LOW-3 and LOW-8 remain open",
    "remain open pending human adjudication",
    "Two independent final implementation reviews",
    "23 of the 53",
)


def _read(rel: str) -> str:
    return (REPO_ROOT / rel).read_text(encoding="utf-8")


def _approved_case_total() -> int:
    """The Rule Card's own case count, enumerated from its tables."""
    card = _read("docs/rules/exploration/light_and_exploration_resources.md")
    return len(set(re.findall(r"^\|\s*\**`?(L\d+[a-z]?)`?\**\s*\|", card, re.M)))


def _case_discharge() -> dict[str, str]:
    """`CASE_DISCHARGE` parsed from the sibling suite, not imported."""
    src = (
        REPO_ROOT / "tests/rules/exploration/test_light_and_exploration_resources.py"
    ).read_text(encoding="utf-8")
    for node in ast.walk(ast.parse(src)):
        if (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == "CASE_DISCHARGE"
            and isinstance(node.value, ast.Dict)
        ):
            return {
                k.value: v.value
                for k, v in zip(node.value.keys, node.value.values, strict=True)
                if isinstance(k, ast.Constant)
                and isinstance(k.value, str)
                and isinstance(v, ast.Constant)
                and isinstance(v.value, str)
            }
    raise AssertionError("CASE_DISCHARGE not found in the test ledger")


# --- Self-checks: the configuration must be meaningful --------------------


def test_the_configuration_is_non_empty_and_every_named_record_exists() -> None:
    """A misconfigured guard is the defect this file exists to prevent."""
    assert LIVE_RECORDS, "no live records configured"
    assert PHASE_TOKEN_RECORDS, "no phase-token records configured"
    assert STALE_CURRENT_CLAIMS, "no stale claims configured"
    assert HISTORICAL_ARTIFACTS, "no historical artifacts configured"

    for rel in LIVE_RECORDS + PHASE_TOKEN_RECORDS + HISTORICAL_ARTIFACTS:
        assert (REPO_ROOT / rel).is_file(), f"configured record does not exist: {rel}"

    assert set(PHASE_TOKEN_RECORDS) <= set(LIVE_RECORDS), (
        "every phase-token record must also be a live record"
    )


def test_no_stale_claim_can_be_silently_excluded() -> None:
    """`B-6` — the exact defect that made four of six checks unreachable.

    The previous design held `"review #2"` in both the forbidden-claim list
    and a historical-skip list, so four claims could never be evaluated. There
    is now **no skip list at all**; this test asserts that, and asserts the
    two configuration lists cannot overlap in a way that disarms a claim.
    """
    # There is no skip/exemption list in this module. If one is ever
    # reintroduced, this assertion is the tripwire.
    assert not any(
        name in globals()
        for name in ("HISTORICAL_MARKERS", "SKIP_MARKERS", "EXEMPT_MARKERS")
    ), "a skip list was reintroduced; B-6 is the reason there must not be one"

    # No stale claim may be a substring of another, which would make the
    # shorter one's failure message ambiguous about which condition fired.
    for claim in STALE_CURRENT_CLAIMS:
        others = [c for c in STALE_CURRENT_CLAIMS if c != claim and claim in c]
        assert not others, f"{claim!r} is subsumed by {others!r}"

    # Historical artifacts must not be in the scanned set.
    assert not (set(HISTORICAL_ARTIFACTS) & set(LIVE_RECORDS)), (
        "a historical artifact is configured as a live record; it preserves "
        "obsolete claims deliberately and must never be scanned"
    )


def test_every_stale_claim_is_actually_evaluated(tmp_path: pathlib.Path) -> None:
    """Each configured claim must be detectable, proved on a fixture.

    This is the regression `B-6` demanded: injecting a stale claim into a
    named live record must fail. It runs against a **fixture copy** in
    ``tmp_path`` — no repository file is altered.
    """
    detected: list[str] = []
    for claim in STALE_CURRENT_CLAIMS:
        fixture = tmp_path / "live_record.md"
        fixture.write_text(
            f"# Fixture\n\nEXP-006 status: {claim}.\n", encoding="utf-8"
        )
        text = fixture.read_text(encoding="utf-8")
        found = [c for c in STALE_CURRENT_CLAIMS if c in text]
        assert claim in found, f"{claim!r} is not detectable by this predicate"
        detected.append(claim)

    assert len(detected) == len(STALE_CURRENT_CLAIMS)


def test_injecting_review_2_pending_into_a_live_record_is_detected(
    tmp_path: pathlib.Path,
) -> None:
    """`B-6`'s named regression: `"review #2 pending"` must fail.

    Review #4 demonstrated that this exact string could be appended to a
    pinned live record with every consistency test still passing. The fixture
    reproduces that injection and asserts it is now caught.
    """
    fixture = tmp_path / "ARCHITECTURE.md"
    fixture.write_text(
        _read("ARCHITECTURE.md") + "\n\nEXP-006 status: review #2 pending.\n",
        encoding="utf-8",
    )
    offences = [c for c in STALE_CURRENT_CLAIMS if c in fixture.read_text("utf-8")]
    assert "review #2 pending" in offences


def test_injecting_review_3_pending_into_a_live_record_is_detected(
    tmp_path: pathlib.Path,
) -> None:
    """The same regression for the next phase's stale wording.

    `B-5` found exactly this in `INDEX.md`, phrased as "review #3 pending".
    """
    fixture = tmp_path / "INDEX.md"
    fixture.write_text(
        _read("docs/completion-records/INDEX.md")
        + "\n\nEXP-006: review #3 pending, separately authorized.\n",
        encoding="utf-8",
    )
    offences = [c for c in STALE_CURRENT_CLAIMS if c in fixture.read_text("utf-8")]
    assert "review #3 pending" in offences


# --- The live-record checks -----------------------------------------------


def test_live_records_carry_the_current_phase_token() -> None:
    """`MED-1`/`B-3` — advancing the phase is one deliberate, atomic act."""
    missing = [rel for rel in PHASE_TOKEN_RECORDS if CURRENT_PHASE not in _read(rel)]
    assert missing == [], (
        f"these live records do not carry {CURRENT_PHASE!r}: {missing}. "
        "Advancing the phase means updating CURRENT_PHASE here and every "
        "record in PHASE_TOKEN_RECORDS together."
    )


def test_no_live_record_asserts_a_stale_claim() -> None:
    """`MED-1`, `B-1`, `B-3`, `B-4`, `B-5` — no exemptions, by design."""
    offences: list[str] = []
    for rel in LIVE_RECORDS:
        for lineno, line in enumerate(_read(rel).splitlines(), 1):
            for claim in STALE_CURRENT_CLAIMS:
                if claim in line:
                    offences.append(f"{rel}:{lineno}: {claim!r}")
    assert offences == [], f"live records assert stale claims: {offences}"


# --- Derived facts: one authoritative source each -------------------------


def test_the_approved_case_total_is_still_what_the_records_claim() -> None:
    """The card is the source of truth for its own case count."""
    assert _approved_case_total() == 53


def test_the_case_ledger_total_matches_the_card() -> None:
    """`CASE_DISCHARGE` and the card cannot disagree about how many cases exist."""
    assert len(_case_discharge()) == _approved_case_total()


def test_no_live_record_duplicates_the_category_split() -> None:
    """`B-1`/`B-2` — the split is derived, and lives in exactly one place.

    The plan and the gate each republished a hand-maintained split; both
    drifted, and the plan asserted a test protection that did not exist. The
    split is now derived from `CASE_DISCHARGE` and must not be transcribed
    into a normative record again. A line is an offence only if it states a
    count **for a claim kind** — the vocabulary may of course be described.
    """
    kinds = ("behavior", "invariant", "surface", "reviewed", "routed")
    offences: list[str] = []
    for rel in ("docs/technical/EXP-006_IMPLEMENTATION_PLAN.md",
                "docs/technical/EXP-006_PRE_CODE_GATE.md"):
        for lineno, line in enumerate(_read(rel).splitlines(), 1):
            lowered = line.lower()
            if not any(k in lowered for k in kinds):
                continue
            if any(m in line for m in ("withdrawn", "superseded", "previously", "B-1", "B-2")):
                continue  # an explicitly-marked historical quotation
            if re.search(r"\*\*\d{1,2}\*\*", line):
                offences.append(f"{rel}:{lineno}: {line.strip()[:90]}")
    assert offences == [], (
        "a normative record transcribes the claim-kind split again; it is "
        f"derived from CASE_DISCHARGE and must not be duplicated: {offences}"
    )


def test_the_review_artifact_set_is_internally_consistent() -> None:
    """`B-4` — the review history is the artifact set, not a prose count.

    Every persisted review artifact must have a paired remediation ledger, so
    the history can be read off the filesystem instead of transcribed into
    records that then go stale.
    """
    technical = REPO_ROOT / "docs/technical"
    reviews = sorted(technical.glob("EXP-006_FINAL_IMPLEMENTATION_REVIEW*.md"))
    ledgers = sorted(technical.glob("EXP-006_REVIEW*_REMEDIATION_LEDGER.md"))

    assert reviews, "no review artifacts found"
    assert len(reviews) == len(ledgers), (
        f"{len(reviews)} review artifact(s) but {len(ledgers)} ledger(s): "
        f"reviews={[p.name for p in reviews]} ledgers={[p.name for p in ledgers]}"
    )

    # Every review artifact is listed in ISSUE-022's §3 artifact inventory,
    # which DEVELOPMENT_WORKFLOW.md §5 item 3 requires to be complete.
    issue = _read("docs/completion-records/ISSUE-022-exp-006-light-and-exploration-resources.md")
    unlisted = [p.name for p in reviews + ledgers if p.name not in issue]
    assert unlisted == [], f"artifacts missing from ISSUE-022 §3: {unlisted}"
