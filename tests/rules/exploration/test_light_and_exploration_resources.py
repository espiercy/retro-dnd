"""EXP-006 Slice A — the light-source value/state model.

Covers the approved deterministic cases the implementation plan assigns to
Slice A: L1, L2, L3, L4, L5, L6, L7 and L16, plus the construction
invariants the human adjudication of 2026-10-01 §8 requires.

Depletion (L8-L12, L15*), contribution aggregation (L27-L28, L34),
ignition (L17-L26) and CHAR-004 catalog integration are Slices B, C and D
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
)

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


def test_slice_a_exposes_no_later_slice_behaviour() -> None:
    """Slice A is the value model only: no depletion, aggregation, ignition,
    RNG, catalog lookup, visibility, darkness, blindness, ration or
    starvation surface exists yet (implementation plan §14, §10)."""
    forbidden = {
        "deplete",
        "depletion",
        "contribution",
        "ignite",
        "ignition",
        "rng",
        "random",
        "catalog",
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
