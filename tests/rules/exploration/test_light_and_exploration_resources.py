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

import pytest

from rules.exploration import light_and_exploration_resources as light
from rules.exploration.light_and_exploration_resources import (
    FRESH_DURATION_TURNS,
    LANTERN_TURNS_PER_FLASK,
    MUNDANE_LIGHT_RADIUS_FEET,
    TORCH_TURNS,
    LightSource,
    LightSourceKind,
    MundaneLightContribution,
    deplete,
    mundane_light_contribution,
    refuel_lantern,
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


def test_no_unauthorized_slice_behaviour_is_exposed() -> None:
    """Slices A and B are authorized; C and D are not.

    ``deplete`` and ``mundane_light_contribution`` are Slice B and are
    expected. What must not appear is ignition (Slice C), CHAR-004 catalog
    integration (Slice D), or any of the card's permanently excluded
    responsibilities (implementation plan §4, §14).
    """
    forbidden = {
        "ignite",
        "ignition",
        "tinderbox",
        "fire",
        "skill",
        "rng",
        "random",
        "roll",
        "catalog",
        "item",
        "visibility",
        "darkness",
        "blind",
        "blindness",
        "surprise",
        "rations",
        "starvation",
        "weapon",
        "missile",
    }
    # Matched on whole underscore-separated tokens, never as substrings:
    # "FRESH_DURATION_TURNS" contains the letters of "ration", and a naive
    # substring check flags it. That is the CLUSTER-003 false-positive mode
    # this suite is written to avoid (implementation plan §13).
    exported = [
        name for name in light.__all__ if forbidden & {part.lower() for part in name.split("_")}
    ]
    assert exported == []
