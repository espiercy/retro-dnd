"""EXP-006 Slices A and B.

Slice A — the light-source value/state model: L1, L2, L3, L4, L5, L6, L7
and L16, plus the construction invariants the human adjudication of
2026-10-01 §8 requires.

Slice B — depletion and mundane-light contribution: L8, L9, L10, L11,
L12, L15, L15a, L15b, L27, L28 and L34.

Ignition (L17-L26) and CHAR-004 catalog integration are Slices C and D
and are deliberately absent.
"""

from __future__ import annotations

import ast
import inspect
import pathlib
import re
from enum import Enum
from itertools import product

import pytest

from rules.exploration import light_and_exploration_resources as light
from rules.exploration.errors import IgnitionAttemptLimitError, IgnitionNotDefinedError
from rules.exploration.light_and_exploration_resources import (
    FRESH_DURATION_TURNS,
    LANTERN_TURNS_PER_FLASK,
    MUNDANE_LIGHT_RADIUS_FEET,
    TORCH_TURNS,
    IgnitionConditions,
    IgnitionOutcome,
    LightSource,
    LightSourceKind,
    MundaneLightContribution,
    catalog_identity,
    deplete,
    ignition_outcome,
    mundane_light_contribution,
    oil_flask_identity,
    refuel_lantern,
    tinderbox_identity,
)

TORCH = LightSourceKind.TORCH
LANTERN = LightSourceKind.LANTERN

# --- Kinds -----------------------------------------------------------------


def test_only_the_two_mundane_kinds_exist() -> None:
    """The enumeration is closed at the two sources RC gives a radius and a
    duration. A ``MAGICAL`` member would be MAGIC-*'s (card §B, case L41)."""
    assert set(LightSourceKind) == {LightSourceKind.TORCH, LightSourceKind.LANTERN}


# --- L1, L2, L3, L4, L5: illumination --------------------------------------


@pytest.mark.parametrize("kind", list(LightSourceKind))
def test_a_lit_source_illuminates_thirty_feet(kind: LightSourceKind) -> None:
    """L1 and L2 — a lit torch and a lit lantern each illuminate 30 feet."""
    assert LightSource.fresh(kind, lit=True).illumination_radius_feet == 30


def test_an_unlit_source_illuminates_nothing() -> None:
    """L3 — an unlit torch illuminates nothing, and reports None rather
    than a radius of zero."""
    assert LightSource.fresh(LightSourceKind.TORCH).illumination_radius_feet is None


def test_torch_and_lantern_radii_do_not_differ() -> None:
    """L4 — guard. RC states one radius for both; a difference must not occur."""
    torch = LightSource.fresh(LightSourceKind.TORCH, lit=True)
    lantern = LightSource.fresh(LightSourceKind.LANTERN, lit=True)
    assert torch.illumination_radius_feet == lantern.illumination_radius_feet


def test_no_illumination_quality_distinction_exists() -> None:
    """L5 — guard. One module-level radius constant serves both kinds, so no
    per-kind quality distinction is representable."""
    assert MUNDANE_LIGHT_RADIUS_FEET == 30
    radius_names = [
        name
        for name in light.__all__
        if "RADIUS" in name or ("LIGHT" in name and "TURNS" not in name)
    ]
    assert radius_names == ["MUNDANE_LIGHT_RADIUS_FEET"]


# --- L6, L7, L16: durations ------------------------------------------------


def test_a_fresh_torch_has_six_turns() -> None:
    """L6."""
    assert LightSource.fresh(LightSourceKind.TORCH).remaining_turns == 6
    assert TORCH_TURNS == 6


def test_a_fresh_lantern_has_twenty_four_turns() -> None:
    """L7 — 24 turns per flask of oil."""
    assert LightSource.fresh(LightSourceKind.LANTERN).remaining_turns == 24
    assert LANTERN_TURNS_PER_FLASK == 24


def test_fresh_durations_are_exposed_so_callers_never_restate_them() -> None:
    """L6/L7 — the mapping is the single source of both figures."""
    assert dict(FRESH_DURATION_TURNS) == {
        LightSourceKind.TORCH: 6,
        LightSourceKind.LANTERN: 24,
    }


def test_fresh_duration_table_is_read_only() -> None:
    """A caller must not be able to redefine how long a torch burns."""
    with pytest.raises(TypeError):
        FRESH_DURATION_TURNS[LightSourceKind.TORCH] = 99  # type: ignore[index]


def test_this_module_performs_no_hour_to_turn_conversion() -> None:
    """L16 — guard. RC states both durations in turns itself, so the module
    holds turn figures directly and converts nothing.

    Asserted over the parsed module rather than its text: a substring search
    for ``60`` or ``* 6`` matches docstring prose and incidental numbers, the
    false-positive mode CLUSTER-003 recorded (implementation plan §13).
    """
    tree = ast.parse(inspect.getsource(light))
    multipliers = {
        node.right.value
        for node in ast.walk(tree)
        if isinstance(node, ast.BinOp)
        and isinstance(node.op, ast.Mult)
        and isinstance(node.right, ast.Constant)
        and isinstance(node.right.value, int)
    }
    assert multipliers == set(), f"unexpected arithmetic on durations: {multipliers}"


# --- Construction invariants (human adjudication 2026-10-01 §7, §8) --------


def test_an_exhausted_source_cannot_be_lit() -> None:
    """The exhaustion invariant: ``remaining_turns == 0`` with ``lit`` is
    refused at construction, so an exhausted source contributing light is
    unconstructible rather than merely untested."""
    with pytest.raises(ValueError, match="exhausted source is never lit"):
        LightSource(kind=LightSourceKind.TORCH, remaining_turns=0, lit=True)


def test_an_exhausted_source_may_exist_unlit() -> None:
    """The invariant forbids the *combination*, not the exhausted state."""
    spent = LightSource(kind=LightSourceKind.TORCH, remaining_turns=0, lit=False)
    assert spent.illumination_radius_feet is None


def test_an_unlit_source_retains_its_remaining_duration() -> None:
    """L11's precondition — Slice B exercises the depletion half. An unlit
    source is not a source without duration; a 'always lit' model could not
    represent this (implementation plan §6.1)."""
    unlit = LightSource(kind=LightSourceKind.TORCH, remaining_turns=6, lit=False)
    assert unlit.remaining_turns == 6
    assert unlit.illumination_radius_feet is None


def test_negative_remaining_turns_is_refused() -> None:
    with pytest.raises(ValueError, match="must not be negative"):
        LightSource(kind=LightSourceKind.TORCH, remaining_turns=-1, lit=False)


def test_a_bool_is_not_an_acceptable_turn_count() -> None:
    """``bool`` is a subtype of ``int``; ``True`` would otherwise read as 1."""
    with pytest.raises(ValueError, match="must be an int"):
        LightSource(kind=LightSourceKind.TORCH, remaining_turns=True, lit=False)


def test_a_non_int_turn_count_is_refused() -> None:
    with pytest.raises(ValueError, match="must be an int"):
        LightSource(kind=LightSourceKind.TORCH, remaining_turns="6", lit=False)  # type: ignore[arg-type]


def test_a_non_bool_lit_flag_is_refused() -> None:
    with pytest.raises(ValueError, match="lit must be a bool"):
        LightSource(kind=LightSourceKind.TORCH, remaining_turns=6, lit=1)  # type: ignore[arg-type]


def test_an_unsupported_kind_is_refused() -> None:
    with pytest.raises(ValueError, match="must be a LightSourceKind"):
        LightSource(kind="torch", remaining_turns=6, lit=False)  # type: ignore[arg-type]


def test_fresh_refuses_an_unsupported_kind() -> None:
    with pytest.raises(ValueError, match="must be a LightSourceKind"):
        LightSource.fresh("lantern")  # type: ignore[arg-type]


def test_the_value_object_carries_no_extra_state() -> None:
    """Frozen and slotted, like TurnCredit and MovementRate."""
    source = LightSource.fresh(LightSourceKind.TORCH)
    assert not hasattr(source, "__dict__")
    assert LightSource.__slots__ == ("kind", "remaining_turns", "lit")
    with pytest.raises(AttributeError):
        source.lit = True  # type: ignore[misc]


# =========================================================================
# Slice B — depletion
# =========================================================================


def test_one_elapsed_turn_spends_one_turn_of_fuel() -> None:
    """L8 — lit torch, EXP-002 reports 1 elapsed turn, 5 remaining."""
    (spent,) = deplete([LightSource.fresh(TORCH, lit=True)], 1)
    assert spent.remaining_turns == 5
    assert spent.lit is True


def test_a_torch_is_expended_after_its_six_turns() -> None:
    """L9 — 6 elapsed turns: 0 remaining, EXPENDED, contributing nothing."""
    (spent,) = deplete([LightSource.fresh(TORCH, lit=True)], 6)
    assert spent.remaining_turns == 0
    assert spent.lit is False
    assert spent.illumination_radius_feet is None


def test_remaining_turns_floor_at_zero_and_never_go_negative() -> None:
    """L10 — 9 elapsed turns against a 6-turn torch floors at 0."""
    (spent,) = deplete([LightSource.fresh(TORCH, lit=True)], 9)
    assert spent.remaining_turns == 0


def test_an_unlit_source_does_not_deplete() -> None:
    """L11 — an unlit torch is not burning, so it spends no fuel."""
    (spent,) = deplete([LightSource.fresh(TORCH)], 3)
    assert spent.remaining_turns == 6
    assert spent.lit is False


def test_zero_elapsed_turns_changes_nothing() -> None:
    source = LightSource.fresh(LANTERN, lit=True)
    (spent,) = deplete([source], 0)
    assert spent == source


def test_depletion_returns_new_values_and_mutates_nothing() -> None:
    source = LightSource.fresh(TORCH, lit=True)
    deplete([source], 4)
    assert source.remaining_turns == 6, "the input value object was mutated"


def test_depleting_no_sources_is_valid() -> None:
    assert deplete([], 3) == ()


@pytest.mark.parametrize("bad", [True, "1", 1.5, None])
def test_elapsed_turns_domain_is_validated(bad: object) -> None:
    """EXP-006 owns the numeric domain of elapsed_turns, not its provenance."""
    with pytest.raises(ValueError, match="elapsed_turns must be an int"):
        deplete([LightSource.fresh(TORCH, lit=True)], bad)  # type: ignore[arg-type]


def test_negative_elapsed_turns_is_refused() -> None:
    with pytest.raises(ValueError, match="must not be negative"):
        deplete([LightSource.fresh(TORCH, lit=True)], -1)


def test_depletion_refuses_a_non_light_source() -> None:
    with pytest.raises(ValueError, match="must contain LightSource values"):
        deplete(["torch"], 1)  # type: ignore[list-item]


# --- L12: refuelling -------------------------------------------------------


def test_an_expended_lantern_takes_a_fresh_flask() -> None:
    """L12 — 24 remaining, and **unlit**.

    Implementation interpretation, recorded rather than read back into the
    card: L12's own wording is *"contributes illumination again"*, and that
    wording is not rewritten. Under the approved separation of fuel state
    from ignition state (human adjudication 2026-10-01), a further flask
    restores the lantern's *fuel*; it does not light it. The lantern is
    *able* to contribute again, once some separately authorized ignition
    operation changes ``lit``.
    """
    expended = LightSource(kind=LANTERN, remaining_turns=0, lit=False)
    refuelled = refuel_lantern(expended)
    assert refuelled.remaining_turns == 24
    assert refuelled.lit is False


def test_refuelling_alone_cannot_make_the_lantern_contribute_illumination() -> None:
    """The proof of the fuel/ignition separation.

    A refuelled lantern contributes nothing — not through its own radius,
    and not through the aggregate. Only an ignition operation, which Slice B
    does not implement, could change that.
    """
    refuelled = refuel_lantern(LightSource(kind=LANTERN, remaining_turns=0, lit=False))

    assert refuelled.illumination_radius_feet is None

    contribution = mundane_light_contribution([refuelled])
    assert contribution.lit_sources == ()
    assert contribution.any_mundane_source_lit is False
    assert contribution.max_mundane_radius_feet is None


def test_a_refuelled_lantern_still_does_not_deplete_while_unlit() -> None:
    """Fuel and ignition stay independent in both directions: a refuelled
    but unlit lantern keeps its 24 turns (L11's rule, applied to L12)."""
    refuelled = refuel_lantern(LightSource(kind=LANTERN, remaining_turns=0, lit=False))
    (after,) = deplete([refuelled], 5)
    assert after.remaining_turns == 24
    assert after.lit is False


def test_a_torch_cannot_be_refuelled() -> None:
    """RC gives the flask to the lantern; a fresh torch is a new source."""
    with pytest.raises(ValueError, match="only a lantern burns a flask"):
        refuel_lantern(LightSource(kind=TORCH, remaining_turns=0, lit=False))


def test_refuelling_a_lantern_that_has_not_reached_zero_is_refused() -> None:
    """An API precondition derived from the approved scope, not a new rules
    mechanic (human adjudication 2026-10-01).

    The card establishes supplying a further flask only after the current
    one is exhausted. **No arithmetic is assigned to the unsupported
    operation** — no topping up to 24, no adding 24, no partial-flask
    arithmetic. It is rejected deterministically.
    """
    with pytest.raises(ValueError, match="only for a lantern that has reached zero"):
        refuel_lantern(LightSource.fresh(LANTERN, lit=True))


def test_refuelling_a_partly_spent_lantern_is_refused_whether_lit_or_not() -> None:
    """The precondition is about remaining fuel, not about burning."""
    partly_spent_lit = LightSource(kind=LANTERN, remaining_turns=7, lit=True)
    partly_spent_unlit = LightSource(kind=LANTERN, remaining_turns=7, lit=False)
    for source in (partly_spent_lit, partly_spent_unlit):
        with pytest.raises(ValueError, match="only for a lantern that has reached zero"):
            refuel_lantern(source)


def test_refuel_refuses_a_non_light_source() -> None:
    with pytest.raises(ValueError, match="must be a LightSource"):
        refuel_lantern("lantern")  # type: ignore[arg-type]


# =========================================================================
# Slice B — mundane-light contribution
# =========================================================================


def test_no_sources_contribute_nothing() -> None:
    """L28 — and nothing further is asserted."""
    contribution = mundane_light_contribution([])
    assert contribution.lit_sources == ()
    assert contribution.any_mundane_source_lit is False
    assert contribution.max_mundane_radius_feet is None


def test_a_lit_source_contributes_thirty_feet() -> None:
    """L27."""
    contribution = mundane_light_contribution([LightSource.fresh(TORCH, lit=True)])
    assert contribution.any_mundane_source_lit is True
    assert contribution.max_mundane_radius_feet == 30


def test_unlit_sources_are_filtered_out_by_the_aggregate_not_the_caller() -> None:
    """A caller cannot accidentally include a spent torch by forgetting to
    filter, because filtering is not the caller's job."""
    contribution = mundane_light_contribution(
        [
            LightSource.fresh(TORCH),  # unlit
            LightSource(kind=TORCH, remaining_turns=0, lit=False),  # expended
            LightSource.fresh(LANTERN, lit=True),  # lit
        ]
    )
    assert contribution.lit_sources == (LightSource.fresh(LANTERN, lit=True),)
    assert contribution.any_mundane_source_lit is True


def test_the_aggregate_cannot_be_constructed_with_an_unlit_source() -> None:
    """The second barrier: even direct construction refuses a non-lit member.

    Together with Slice A's exhausted-never-lit invariant, this makes an
    exhausted source in the aggregate unreachable by two independent
    routes rather than by trusting the caller.
    """
    with pytest.raises(ValueError, match="only lit sources"):
        MundaneLightContribution(lit_sources=(LightSource.fresh(TORCH),))


def test_an_exhausted_source_can_never_reach_the_aggregate() -> None:
    """The property the two barriers exist to guarantee, stated directly."""
    with pytest.raises(ValueError, match="exhausted source is never lit"):
        # barrier 1: the only source that could carry 0 turns into the
        # aggregate would have to be lit, and that is unconstructible.
        MundaneLightContribution(
            lit_sources=(LightSource(kind=TORCH, remaining_turns=0, lit=True),)
        )


def test_the_derived_figures_cannot_disagree_with_the_sources() -> None:
    """They are computed properties, not stored fields, so there is no
    state to get out of step."""
    assert not hasattr(MundaneLightContribution, "__dataclass_fields__") or set(
        MundaneLightContribution.__dataclass_fields__
    ) == {"lit_sources"}


def test_the_aggregate_refuses_a_non_tuple_and_non_source() -> None:
    with pytest.raises(ValueError, match="must be a tuple"):
        MundaneLightContribution(lit_sources=[])  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="must contain LightSource values"):
        MundaneLightContribution(lit_sources=("torch",))  # type: ignore[arg-type]


def test_querying_light_state_needs_no_surprise_or_encounter_state() -> None:
    """L34 — surprise is not an input to this card."""
    signature = inspect.signature(mundane_light_contribution)
    assert list(signature.parameters) == ["sources"]


# --- L15a / L15b: the multiple-source distinction --------------------------


def test_one_source_expiring_does_not_darken_the_party() -> None:
    """L15a — the decisive case. Two lit torches, one expires after its six
    turns; the other was lit later and still burns. The aggregate still
    reports mundane illumination."""
    older = LightSource(kind=TORCH, remaining_turns=6, lit=True)
    newer = LightSource(kind=LANTERN, remaining_turns=24, lit=True)

    spent = deplete([older, newer], 6)

    expired, still_burning = spent
    assert expired.remaining_turns == 0 and expired.lit is False
    assert still_burning.remaining_turns == 18 and still_burning.lit is True

    contribution = mundane_light_contribution(spent)
    assert contribution.any_mundane_source_lit is True, "one source expiring darkened the party"
    assert contribution.lit_sources == (still_burning,)
    assert contribution.max_mundane_radius_feet == 30


def test_exhaustion_produces_no_world_state_at_all() -> None:
    """L15b — guard. Depletion returns sources and nothing else: there is no
    darkness, NO_LIGHT, blindness or Visibility value for it to produce."""
    result = deplete([LightSource.fresh(TORCH, lit=True)], 6)
    assert isinstance(result, tuple)
    assert all(isinstance(source, LightSource) for source in result)


def test_no_world_state_vocabulary_exists_on_the_aggregate() -> None:
    """L15b / L29 / L31 — guard. The result type exposes no name a consumer
    could read as a claim about the world."""
    forbidden = {
        "darkness",
        "dark",
        "no_light",
        "visibility",
        "blind",
        "blindness",
        "surprise",
        "world",
        "global",
        "illumination",
    }
    names = {
        name for name in dir(MundaneLightContribution) if not name.startswith("_")
    }
    assert not {
        name for name in names if forbidden & {part.lower() for part in name.split("_")}
    }


# =========================================================================
# Slice C — ignition branch / outcome model
# =========================================================================

ORDINARY = IgnitionConditions.ORDINARY
ADVERSE = IgnitionConditions.ADVERSE

# The approved eight-row matrix. ``None`` means RC defines no procedure.
APPROVED_MATRIX: dict[tuple[bool, bool, IgnitionConditions], IgnitionOutcome | None] = {
    (True, True, ORDINARY): IgnitionOutcome.AUTOMATIC,
    (True, True, ADVERSE): IgnitionOutcome.ROUTED_SKILL_CHECK,
    (True, False, ORDINARY): IgnitionOutcome.ROLL_1D6_IGNITE_1_2,
    (True, False, ADVERSE): IgnitionOutcome.ROUTED_SKILL_CHECK,  # SR-11
    (False, True, ORDINARY): IgnitionOutcome.ROLL_1D6_IGNITE_1_2,
    (False, True, ADVERSE): None,
    (False, False, ORDINARY): None,
    (False, False, ADVERSE): None,
}


def _ignite(skill: bool, tinderbox: bool, conditions: IgnitionConditions) -> IgnitionOutcome:
    return ignition_outcome(
        has_fire_building=skill,
        has_tinderbox=tinderbox,
        conditions=conditions,
        attempt_already_made_this_round=False,
    )


@pytest.mark.parametrize(("key", "expected"), list(APPROVED_MATRIX.items()))
def test_every_matrix_combination_resolves_as_approved(
    key: tuple[bool, bool, IgnitionConditions], expected: IgnitionOutcome | None
) -> None:
    """L20, L21, L22, L17, L23, L24 and the SR-11 intersection — all eight."""
    skill, tinderbox, conditions = key
    if expected is None:
        with pytest.raises(IgnitionNotDefinedError):
            _ignite(skill, tinderbox, conditions)
    else:
        assert _ignite(skill, tinderbox, conditions) is expected


def test_all_eight_combinations_are_covered_and_none_overlaps() -> None:
    """Exhaustiveness and non-overlap, proved over the product rather than
    row by row: a mapping cannot have two entries for one key, so coverage
    is the only thing left to establish."""
    combos = list(product([True, False], [True, False], list(IgnitionConditions)))
    assert len(combos) == 8
    assert set(APPROVED_MATRIX) == set(combos)

    resolved = 0
    refused = 0
    for skill, tinderbox, conditions in combos:
        try:
            _ignite(skill, tinderbox, conditions)
            resolved += 1
        except IgnitionNotDefinedError:
            refused += 1
    assert resolved == 5
    assert refused == 3


def test_the_sr11_intersection_routes_to_the_skill_check() -> None:
    """SR-11. Both RC conditionals match this input; the ruling settles it.

    The sibling row proves the ruling actually bites: with the SAME skill
    and the SAME absent tinderbox, ORDINARY conditions still give the 1d6.
    """
    assert _ignite(True, False, ADVERSE) is IgnitionOutcome.ROUTED_SKILL_CHECK
    assert _ignite(True, False, ORDINARY) is IgnitionOutcome.ROLL_1D6_IGNITE_1_2


def test_no_skill_adverse_with_tinderbox_is_refused() -> None:
    """L23 — the 1d6 is qualified to ordinary circumstances and is not
    stretched to cover this."""
    with pytest.raises(IgnitionNotDefinedError, match="comparatively dry"):
        _ignite(False, True, ADVERSE)


@pytest.mark.parametrize("conditions", [ORDINARY, ADVERSE])
def test_no_skill_no_tinderbox_is_refused(conditions: IgnitionConditions) -> None:
    """L24 — RC states no procedure at all."""
    with pytest.raises(IgnitionNotDefinedError, match="no procedure is stated"):
        _ignite(False, False, conditions)


def test_a_refusal_is_never_answered_by_a_default() -> None:
    """The three silences are absent from the lookup, so there is no default
    to reach — refusal is structural, not a fallback branch."""
    from rules.exploration.light_and_exploration_resources import _IGNITION_MATRIX

    assert len(_IGNITION_MATRIX) == 5
    assert (False, True, ADVERSE) not in _IGNITION_MATRIX
    assert (False, False, ORDINARY) not in _IGNITION_MATRIX
    assert (False, False, ADVERSE) not in _IGNITION_MATRIX


# --- L19 / L19a / L19b: the same-round guard --------------------------------


def test_a_second_attempt_this_round_raises_the_attempt_limit_error() -> None:
    """L19 — driven by caller-supplied state, not by the card discovering it.

    A **rules** rejection, not a structural one: RC defines the procedure
    and limits it to once per round.
    """
    with pytest.raises(IgnitionAttemptLimitError, match="once per round"):
        ignition_outcome(
            has_fire_building=True,
            has_tinderbox=True,
            conditions=ORDINARY,
            attempt_already_made_this_round=True,
        )


def test_the_two_refusals_are_different_types() -> None:
    """The semantic distinction, asserted directly.

    One says RC supplies no procedure; the other says RC supplies one and
    forbids using it twice. A same-round violation must never claim the rule
    is undefined.
    """
    with pytest.raises(IgnitionNotDefinedError):
        _ignite(False, False, ORDINARY)
    with pytest.raises(IgnitionAttemptLimitError):
        ignition_outcome(
            has_fire_building=True,
            has_tinderbox=True,
            conditions=ORDINARY,
            attempt_already_made_this_round=True,
        )
    assert not issubclass(IgnitionAttemptLimitError, IgnitionNotDefinedError)
    assert not issubclass(IgnitionNotDefinedError, IgnitionAttemptLimitError)


def test_the_same_round_guard_precedes_branch_resolution() -> None:
    """An RC-silent combination with the flag set fails for the ATTEMPT LIMIT,
    not for source silence — proving the guard runs before the matrix.

    This is the case that would expose a conflation: if the two refusals
    shared a type, or if the matrix were consulted first, this would report
    the wrong reason.
    """
    with pytest.raises(IgnitionAttemptLimitError, match="once per round"):
        ignition_outcome(
            has_fire_building=False,
            has_tinderbox=False,
            conditions=ADVERSE,
            attempt_already_made_this_round=True,
        )


def test_a_malformed_attempt_flag_remains_a_structural_error() -> None:
    """The flag being a non-``bool`` is a malformed input, not a rule being
    broken, and stays a plain ``ValueError``."""
    with pytest.raises(ValueError, match="must be a bool") as excinfo:
        ignition_outcome(
            has_fire_building=True,
            has_tinderbox=True,
            conditions=ORDINARY,
            attempt_already_made_this_round=1,  # type: ignore[arg-type]
        )
    assert not isinstance(excinfo.value, IgnitionAttemptLimitError)


def test_a_first_attempt_evaluates_normally_and_records_nothing() -> None:
    """L19a — and the card is stateless: the identical call repeats forever,
    because nothing was recorded."""
    for _ in range(3):
        assert _ignite(True, True, ORDINARY) is IgnitionOutcome.AUTOMATIC


def test_the_selector_stores_no_round_state() -> None:
    """L19b — guard. No module-level mutable state, and no attribute on the
    function, could carry an attempt between calls."""
    assert not hasattr(ignition_outcome, "__dict__") or not [
        k for k in vars(ignition_outcome) if not k.startswith("__")
    ]
    module_mutables = [
        name
        for name, value in vars(light).items()
        if not name.startswith("__")
        and isinstance(value, (list, dict, set))
        and not isinstance(value, type)
    ]
    assert module_mutables == [], f"mutable module state could track rounds: {module_mutables}"


@pytest.mark.parametrize(
    "bad_kwargs",
    [
        {"has_fire_building": 1},
        {"has_tinderbox": 0},
        {"attempt_already_made_this_round": 1},
    ],
)
def test_integers_are_not_accepted_as_booleans(bad_kwargs: dict[str, object]) -> None:
    """bool is an int subclass; 1 and 0 must not pass silently."""
    kwargs: dict[str, object] = {
        "has_fire_building": True,
        "has_tinderbox": True,
        "conditions": ORDINARY,
        "attempt_already_made_this_round": False,
    }
    kwargs.update(bad_kwargs)
    with pytest.raises(ValueError, match="must be a bool"):
        ignition_outcome(**kwargs)  # type: ignore[arg-type]


def test_conditions_must_be_the_enum() -> None:
    with pytest.raises(ValueError, match="must be an IgnitionConditions"):
        ignition_outcome(
            has_fire_building=True,
            has_tinderbox=True,
            conditions="ordinary",  # type: ignore[arg-type]
            attempt_already_made_this_round=False,
        )


# --- Slice-C boundaries -----------------------------------------------------


def test_ignition_returns_an_outcome_never_a_light_source() -> None:
    """L25 and the Slice-B boundary: selecting a branch is not lighting a
    source. AUTOMATIC means the procedure succeeds under the rule, not that
    this slice applies it."""
    result = _ignite(True, True, ORDINARY)
    assert isinstance(result, IgnitionOutcome)
    assert not isinstance(result, LightSource)


def test_the_routed_skill_check_is_emitted_not_resolved() -> None:
    """L25 — no 1d20, no ability score, no penalty arithmetic is produced."""
    result = _ignite(True, False, ADVERSE)
    assert result is IgnitionOutcome.ROUTED_SKILL_CHECK
    assert isinstance(result, Enum)  # a bare signal, carrying no computed value


def test_the_1d6_branch_is_selected_not_rolled() -> None:
    """L26 — the outcome names the procedure; the caller rolls it."""
    assert _ignite(False, True, ORDINARY) is IgnitionOutcome.ROLL_1D6_IGNITE_1_2


# =========================================================================
# Slice D — CHAR-004 identity binding + final architectural guards
# =========================================================================

CATALOG_ECONOMIC_FIELDS = frozenset(
    {
        "price",
        "encumbrance_cn",
        "capacity_cn",
        "dimension_feet",
        "size",
        "traits",
        "material",
        "made_for_race",
    }
)
"""`Item` fields EXP-006 must never consume. `name` and `category` are
identity; everything else is CHAR-004's economics or combat data."""


def test_each_light_source_binds_to_its_char_004_row() -> None:
    assert catalog_identity(TORCH).name == "Torch"
    assert catalog_identity(LANTERN).name == "Lantern"


def test_the_torch_uses_char_004s_exported_identity() -> None:
    """Human adjudication: TORCH has an export because it is the one
    commodity in both catalogs; the other three do not and are looked up."""
    from rules.character_creation import equipment

    assert catalog_identity(TORCH) is equipment.TORCH


def test_catalog_identity_refuses_an_unsupported_kind() -> None:
    with pytest.raises(ValueError, match="must be a LightSourceKind"):
        catalog_identity("torch")  # type: ignore[arg-type]


def test_oil_and_tinderbox_bind_to_their_rows() -> None:
    assert oil_flask_identity().name == "Oil"
    assert tinderbox_identity().name == "Tinder box"


def test_the_oil_identity_is_the_gear_row_not_the_weapon_row() -> None:
    """`Oil, Burning` is the Weapons row and belongs to COMBAT-* (L46)."""
    assert oil_flask_identity().name != "Oil, Burning"


def test_catalog_names_live_in_exactly_one_private_location() -> None:
    """String coupling is centralized, not scattered (plan §9.2).

    Parsed, not grepped: a literal in a docstring must not count. Every
    string constant in the module body outside `_CATALOG_NAMES` is checked
    against the canonical names.
    """
    tree = ast.parse(inspect.getsource(light))
    canonical = {"Lantern", "Oil", "Tinder box"}

    def _is_catalog_names(node: ast.AST) -> bool:
        # The constant is annotated (`_CATALOG_NAMES: Final = ...`), so it
        # parses as AnnAssign, not Assign. Both are matched so the guard does
        # not silently pass by finding nothing.
        if isinstance(node, ast.AnnAssign):
            return isinstance(node.target, ast.Name) and node.target.id == "_CATALOG_NAMES"
        if isinstance(node, ast.Assign):
            return any(isinstance(t, ast.Name) and t.id == "_CATALOG_NAMES" for t in node.targets)
        return False

    assignments = {node for node in ast.walk(tree) if _is_catalog_names(node)}
    assert assignments, "guard found no _CATALOG_NAMES definition to anchor on"
    inside = {
        n
        for a in assignments
        for n in ast.walk(a)
        if isinstance(n, ast.Constant) and isinstance(n.value, str)
    }
    stray = [
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and node.value in canonical
        and node not in inside
    ]
    assert stray == [], f"catalog name used outside _CATALOG_NAMES: {stray}"


def test_no_catalog_economic_field_is_ever_accessed() -> None:
    """Guard G-4 — the CHAR-004 seam, asserted structurally.

    Every attribute access in the parsed module is inspected. A field named
    in prose, a docstring or a comment cannot fail this, because comments and
    docstring text are not `ast.Attribute` nodes — which is exactly why this
    is an AST check and not a text search.
    """
    tree = ast.parse(inspect.getsource(light))
    accessed = {
        node.attr for node in ast.walk(tree) if isinstance(node, ast.Attribute)
    }
    leaked = accessed & CATALOG_ECONOMIC_FIELDS
    assert leaked == set(), f"EXP-006 reads CHAR-004 economic field(s): {leaked}"


def test_no_currency_or_pricing_machinery_is_imported() -> None:
    """L42 — this card emits no price and owns no money type."""
    tree = ast.parse(inspect.getsource(light))
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module is not None:
            imported.add(node.module)
            imported.update(f"{node.module}.{a.name}" for a in node.names)
        elif isinstance(node, ast.Import):
            imported.update(a.name for a in node.names)
    forbidden = {"currency", "coin", "purchase", "starting_gold", "selection_cost"}
    offending = {
        m for m in imported if forbidden & {p.lower() for p in m.replace(".", "_").split("_")}
    }
    assert offending == set(), f"pricing machinery imported: {offending}"


def test_the_complete_production_dependency_surface() -> None:
    """The final guard: EXP-006's whole import graph, stated positively.

    Proves in one assertion that there is no production dependency on
    TurnCredit, EXP-001 time machinery, the CHAR-012 skill resolver, RNG,
    encounter resolution, combat resolution, magic resolution, or any
    world-darkness state — because nothing of the kind is imported at all.
    """
    tree = ast.parse(inspect.getsource(light))
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module is not None:
            imported.add(node.module)
        elif isinstance(node, ast.Import):
            imported.update(a.name for a in node.names)

    assert imported == {
        "__future__",
        "collections.abc",
        "dataclasses",
        "enum",
        "types",
        "typing",
        "rules.character_creation.equipment",  # identity only -- guarded above
        "rules.exploration.errors",
    }


# --- §13 ledger reconciliation ---------------------------------------------

CASE_DISCHARGE: dict[str, str] = {
    # --- implemented behavior -------------------------------------------
    "L1": "behavior: lit torch radius 30",
    "L2": "behavior: lit lantern radius 30",
    "L3": "behavior: unlit illuminates nothing",
    "L6": "behavior: fresh torch 6 turns",
    "L7": "behavior: fresh lantern 24 turns",
    "L8": "behavior: 1 elapsed turn -> 5 remaining",
    "L9": "behavior: 6 elapsed turns -> EXPENDED",
    "L10": "behavior: floors at 0",
    "L11": "behavior: unlit does not deplete",
    "L12": "behavior: refuel -> 24 turns, unlit",
    "L15a": "behavior: one source expires, the other still contributes",
    "L17": "behavior: tinderbox 1d6 branch selected",
    "L20": "behavior: skill + tinderbox + ordinary -> AUTOMATIC",
    "L21": "behavior: skill, no tinderbox, ordinary -> 1d6",
    "L22": "behavior: adverse -> ROUTED_SKILL_CHECK (incl. SR-11 row)",
    "L19a": "behavior: first attempt evaluates, records nothing",
    "L27": "behavior: aggregate reports lit source",
    "L28": "behavior: aggregate empty when none lit",
    "L34": "behavior: query succeeds with no surprise state",
    "L12a_": "placeholder-never-used",
    # --- implemented invariants (refusals) -------------------------------
    "L12a": "invariant: partial refill refused",
    "L19": "invariant: IgnitionAttemptLimitError on second attempt",
    "L23": "invariant: IgnitionNotDefinedError, no-skill adverse",
    "L24": "invariant: IgnitionNotDefinedError, no skill no tinderbox",
    "L18": "invariant: a failed 1d6 may retry -- the roll is the caller's, "
    "so this card only guarantees the branch stays selectable",
    "L26": "invariant: adverse never defaults to the 1d6",
    # --- architectural guards ---------------------------------------------
    "L4": "guard: torch/lantern radii cannot differ (one constant)",
    "L5": "guard: no illumination-quality distinction exists",
    "L13": "guard: import graph -- no time machinery",
    "L14": "guard: import graph -- no second counter/clock",
    "L15": "guard: no burn-out event/proration (absent from the API)",
    "L15b": "guard: exhaustion produces no world state (deplete returns sources)",
    "L16": "guard: no hour->turn arithmetic in the parsed module",
    "L19b": "guard: no round state, no flag mutation",
    "L25": "guard: no skill check resolved here (import graph)",
    "L29": "guard: no NO_LIGHT/world claim from absence",
    "L30": "guard: no DIM_LIGHT from 'normal dungeon conditions' -- no "
    "Visibility type exists to express it",
    "L31": "guard: no Visibility category produced (API shape)",
    "L32": "guard: no infravision parameter exists",
    "L33": "guard: no distance dice (no RNG imported)",
    "L35": "guard: surprise is not a parameter of any function",
    "L36": "guard: no light->distance path (no distance operation exists)",
    "L37a": "guard: complete darkness never established here",
    "L38": "guard: no movement multiplier (import graph)",
    "L39": "guard: no save/attack/AC values (import graph)",
    "L40": "guard: infravision never decided (no parameter)",
    "L41": "guard: no magical light (LightSourceKind closed at two)",
    "L42": "guard: no CHAR-004 economic field accessed (AST)",
    "L43": "guard: no ration name or operation",
    "L44": "guard: no starvation name or operation",
    "L45": "guard: torch-as-weapon -- no weapon operation exists",
    "L46": "guard: oil-as-missile/pursuit -- no such operation exists",
    # --- routed / non-owned ------------------------------------------------
    "L37": "routed: blindness predicate not asserted; illumination facts only",
    "L47": "routed: reports any_mundane_source_lit; item/skill mechanic not owned",
}


def test_every_approved_case_is_accounted_for() -> None:
    """§13 — the complete ledger, reconciled against the finished card.

    Many cases are discharged by **absence** — no such type, parameter or
    operation exists — which is a stronger guarantee than a runtime
    assertion but leaves no case ID in a test name. This map is the audit
    trail for those, so no case is accidentally unaccounted for.

    **No code was written to turn a non-owned assertion into executable
    behavior**; the two routed entries stay routed.
    """
    card = (
        pathlib.Path(__file__).resolve().parents[3]
        / "docs/rules/exploration/light_and_exploration_resources.md"
    ).read_text(encoding="utf-8")
    approved = set(re.findall(r"^\| (L\d+[a-z]?) \|", card, re.M))

    mapped = {k for k in CASE_DISCHARGE if not k.endswith("_")}

    assert approved - mapped == set(), f"approved case not accounted for: {approved - mapped}"
    assert mapped - approved == set(), f"mapped case not in the card: {mapped - approved}"
    assert len(approved) == 53


# --- Architectural guard: no second clock ----------------------------------


def test_this_module_imports_no_time_machinery() -> None:
    """Guard G-1, and the human adjudication of 2026-10-01 §3.

    EXP-002 remains the sole dungeon-time authority. This module must not
    import ``turn_credit`` (whose own docstring scopes it to the
    EXP-002/EXP-001 interface) or ``dungeon_turn_time_accounting``, and must
    hold no counter or clock. Asserted over the parsed import graph, not a
    text search (implementation plan §13).
    """
    tree = ast.parse(inspect.getsource(light))
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module is not None:
            imported.add(node.module)
        elif isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)

    forbidden = {"turn_credit", "dungeon_turn_time_accounting"}
    assert not {m for m in imported if any(f in m for f in forbidden)}


def test_this_module_imports_no_rng_skill_encounter_combat_or_magic_machinery() -> None:
    """Guard G-2/G-3 — Slice C's architectural guarantee.

    Selecting an ignition branch must not pull in the things the branch
    merely *names*: no RNG for the `1d6`, no `CHAR-012` resolver for the
    skill check, and no encounter, combat or magic module. Asserted over
    the resolved import graph, since a text search would match the
    docstrings that legitimately discuss all of them.
    """
    tree = ast.parse(inspect.getsource(light))
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module is not None:
            imported.add(node.module)
        elif isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)

    forbidden_tokens = {
        "rng",
        "random",
        "dice",
        "skill",
        "char_012",
        "ability",
        "encounter",
        "combat",
        "magic",
    }
    offending = {
        module
        for module in imported
        if forbidden_tokens & {part.lower() for part in module.replace(".", "_").split("_")}
    }
    assert offending == set(), f"forbidden dependency: {offending}"
    # `equipment` is NOT forbidden here: Slice D consumes CHAR-004 identities
    # legitimately. That it reads no economic field is a separate, stronger
    # guard -- test_no_catalog_economic_field_is_ever_accessed. The complete
    # import surface is asserted by test_the_complete_production_dependency_surface.


def test_no_unauthorized_slice_behaviour_is_exposed() -> None:
    """All four slices are now authorized, so this guard protects only the
    card's **permanently excluded** responsibilities (§B, implementation
    plan §4) — the ones no slice may ever add.

    ``catalog_identity`` and friends are Slice D and are expected; that they
    consume identity only is proved by the economic-field guard. ``skill`` is
    likewise not forbidden: ``ROUTED_SKILL_CHECK`` legitimately *names* the
    owner it routes to, and a name test could not establish whether the
    resolver is imported — the import graph does that.
    """
    forbidden = {
        "rng",
        "random",
        "visibility",
        "darkness",
        "blind",
        "blindness",
        "surprise",
        "rations",
        "starvation",
        "weapon",
        "missile",
        "price",
        "cost",
        "coin",
        "encumbrance",
    }
    # Matched on whole underscore-separated tokens, never as substrings:
    # "FRESH_DURATION_TURNS" contains the letters of "ration", and a naive
    # substring check flags it. That is the CLUSTER-003 false-positive mode
    # this suite is written to avoid (implementation plan §13).
    exported = [
        name for name in light.__all__ if forbidden & {part.lower() for part in name.split("_")}
    ]
    assert exported == []
