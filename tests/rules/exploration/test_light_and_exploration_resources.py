"""EXP-006 — the complete deterministic-case ledger for the approved card.

All four accepted slices are covered here, in one module, so that the
53-case ledger and the guards that discharge it stay in one place:

Slice A — the light-source value/state model: L1-L7, L16, plus the
construction invariants required by the human adjudication of
2026-10-01 §8.

Slice B — depletion and mundane-light contribution: L8-L12, L15, L15a,
L15b, L27, L28, L34.

Slice C — the ignition branch/outcome selector, carrying ``SR-11``:
L17-L26, L19a, L19b.

Slice D — CHAR-004 identity binding and the final architectural guards:
L29-L33, L35-L39.

``CASE_DISCHARGE`` below maps every case ID to the mechanism that
discharges it, and a guard asserts the mapping is exactly the ledger.

Deliberately absent, and guarded as absent rather than merely unwritten:
the seven RC silences the card names, global/world illumination, the
encounter-``Visibility`` product, blindness establishment, rations and
starvation causation. None of these is this card's responsibility.
"""

from __future__ import annotations

import ast
import dataclasses
import inspect
import pathlib
import re
from enum import Enum
from itertools import product
from types import FunctionType, MappingProxyType, ModuleType

import pytest

from rules.character_creation.equipment import Item
from rules.exploration import errors as exploration_errors
from rules.exploration import light_and_exploration_resources as light
from rules.exploration.errors import (
    IgnitionAttemptLimitError,
    IgnitionNotDefinedError,
    LanternRefuelNotDefinedError,
)
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
    deplete,
    ignition_outcome,
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

    # (1) The structural property that actually matters: no API, field or
    #     constant is denominated in hours, so there is nothing to convert
    #     FROM. This is stronger than enumerating arithmetic spellings.
    hour_names = {
        name
        for name in _module_scope_names(light)
        if "hour" in name.lower() or "minute" in name.lower()
    }
    for params in APPROVED_CALLABLES.values():
        hour_names |= {p for p in params if "hour" in p.lower() or "minute" in p.lower()}
    for members in APPROVED_MEMBERS.values():
        hour_names |= {m for m in members if "hour" in m.lower() or "minute" in m.lower()}
    assert hour_names == set(), f"hours/minutes-denominated surface: {hour_names}"

    # (2) And NO scaling arithmetic survives at all, on either operand.
    #     History: the first version inspected only the right operand, so
    #     `6 * hours` and `minutes // 10` passed (review-#1 LOW-7). The
    #     second required an int *Constant*, so `value * TORCH_TURNS`
    #     passed (review-#2 LOW-5). Multiplication and division simply have
    #     no legitimate use in this module — RC states both durations in
    #     turns and depletion is subtraction — so the honest guard forbids
    #     the operators outright rather than guessing their spellings.
    arithmetic = [
        ast.dump(node)
        for node in ast.walk(tree)
        if isinstance(node, ast.BinOp)
        and isinstance(node.op, (ast.Mult, ast.FloorDiv, ast.Div, ast.Mod, ast.Pow))
    ]
    assert arithmetic == [], f"unexpected scaling arithmetic: {arithmetic}"

    augmented = [
        ast.dump(node)
        for node in ast.walk(tree)
        if isinstance(node, ast.AugAssign)
        and isinstance(node.op, (ast.Mult, ast.FloorDiv, ast.Div, ast.Mod, ast.Pow))
    ]
    assert augmented == [], f"unexpected in-place scaling: {augmented}"


def test_this_module_uses_no_reflective_attribute_access() -> None:
    """EXP-006 contains no approved reflective catalog-access path.

    **Claim A, stated narrowly — and deliberately NOT the stronger claim.**
    This does not establish that economic fields are unreachable by every
    conceivable reflection mechanism. Review #2 defeated that stronger
    reading with ``object.__getattribute__(item, "price")``, which is an
    ``ast.Attribute`` call and so was invisible to an ``ast.Name``-only
    predicate. The predicate now covers both call *shapes* — a bare name
    and a dotted attribute — which closes that specific spelling.

    It is still not a static analyzer, and the project does not claim it is
    one: EXP-006 has no approved need for reflective catalog access, this
    guard shows the module uses none of the ordinary mechanisms, and the
    remainder of the boundary is a **reviewed** one (claim C). Building a
    miniature analyzer here was considered and rejected.

    **How open the residue actually is** — recorded 2026-10-03 under
    review-#3 finding ``LOW-6``, which found the previous framing too
    comfortable. Ledger #2 attributed the residual risk to a future agent
    authorizing a new import (the ``dataclasses.astuple`` path). That
    understates it: ``_LIGHT_SOURCE_IDENTITIES[kind].__getstate__()``
    reaches every field of a catalog row with **no import change at all**
    and no name this guard inspects. Approved case ``L42`` is still not
    breached — it forbids *emitting* an economic value, and no public
    callable returns an ``Item`` — but the honest statement is that this
    boundary rests on review, not on this mechanism.
    """
    tree = ast.parse(inspect.getsource(light))
    reflective = {
        "getattr",
        "setattr",
        "delattr",
        "vars",
        "globals",
        "locals",
        "eval",
        "exec",
        "compile",
        "__getattribute__",
        "__getattr__",
        "__dict__",
        "__class__",
        "__reduce__",
        "_asdict",
    }
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)]
    assert calls, "guard anchored on zero Call nodes"

    used: set[str] = set()
    for node in calls:
        if isinstance(node.func, ast.Name) and node.func.id in reflective:
            used.add(node.func.id)
        # object.__getattribute__(x, "price") and x.__getattribute__("price")
        elif isinstance(node.func, ast.Attribute) and node.func.attr in reflective:
            used.add(node.func.attr)
    assert used == set(), f"reflective access could evade the field guard: {used}"

    # Attribute reads of the reflection entry points, not only calls of them.
    reads = {
        node.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Attribute) and node.attr in reflective
    }
    assert reads == set(), f"reflective entry point referenced: {reads}"


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


def test_no_fresh_duration_ceiling_is_imposed() -> None:
    """The adjudicated **absence** of a ceiling, now guarded.

    Added 2026-10-03 under review-#3 finding `LOW-1`. The human adjudication
    of 2026-10-01 refused to add ``remaining_turns <= fresh_duration``:
    *"Adding it would be an implementation-level rule we have not
    authorized. If a future mechanic could legitimately alter duration, that
    cap would become accidental policy."* That decision had no regression
    test, so re-adding the cap left the suite green — an adjudicated
    boundary protected only by memory.

    A long-duration source must stay constructible, and must deplete
    normally, unless some *approved* invariant forbids it. None does.
    """
    long_torch = LightSource(kind=TORCH, remaining_turns=600, lit=True)
    assert long_torch.remaining_turns == 600
    assert long_torch.illumination_radius_feet == MUNDANE_LIGHT_RADIUS_FEET

    (after,) = deplete([long_torch], 6)
    assert after.remaining_turns == 594
    assert after.lit is True

    # Likewise for a lantern beyond one flask, and at the exact boundary.
    assert LightSource(kind=LANTERN, remaining_turns=100, lit=True).remaining_turns == 100
    assert LightSource(kind=TORCH, remaining_turns=TORCH_TURNS, lit=True).remaining_turns == 6
    assert mundane_light_contribution([long_torch]).max_mundane_radius_feet == 30


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

    This is the card's literal specification, not an interpretation of it:
    §4 and case `L12` both state 24 remaining and ``lit = False``. (The
    earlier `L12` wording *"contributes illumination again"* was withdrawn
    by the card on 2026-10-01; quoting it as current was review-#2 finding
    `HIGH-2` and is corrected here.) A further flask restores the lantern's
    *fuel*; only a separately authorized ignition operation changes ``lit``.
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


def test_a_torch_passed_to_refuel_lantern_is_an_invalid_argument() -> None:
    """A non-lantern is a **structural** rejection, not a source silence.

    Human adjudication 2026-10-03, on review-#2 finding `LOW-9`.
    ``refuel_lantern`` is specifically a lantern operation, so any other
    source kind is an invalid argument to it. This previously raised
    `LanternRefuelNotDefinedError`, which asserted something false: that
    **RC had failed to define** how to refuel a torch. RC has no such gap
    — the operation simply does not apply to that source kind, and there
    is no silence to report.
    """
    with pytest.raises(ValueError, match="refuel_lantern is a lantern operation"):
        refuel_lantern(LightSource(kind=TORCH, remaining_turns=0, lit=False))


def test_a_torch_refusal_is_not_reported_as_a_source_silence() -> None:
    """The other half of `LOW-9`: the two categories must not be conflated.

    Asserting the **negative** is coherent here because the three domain
    types are concrete siblings of ``Exception`` and are **not** subclasses
    of ``ValueError`` — verified by
    `test_the_domain_errors_are_not_subclasses_of_value_error`. Were they
    subclasses, this assertion would contradict the taxonomy rather than
    protect it.
    """
    with pytest.raises(ValueError) as caught:
        refuel_lantern(LightSource(kind=TORCH, remaining_turns=0, lit=False))
    assert not isinstance(caught.value, LanternRefuelNotDefinedError)


def test_refuelling_a_lantern_that_has_not_reached_zero_is_refused() -> None:
    """A **valid lantern state**, and here the source genuinely is silent.

    The card establishes replacing the flask after exhaustion and
    establishes nothing for a partly-fuelled lantern: **no topping up to
    24, no adding 24, no partial-flask arithmetic.** None is invented; the
    request is refused deterministically, in the rules domain.
    """
    with pytest.raises(
        LanternRefuelNotDefinedError, match="only for a lantern that has reached zero"
    ):
        refuel_lantern(LightSource.fresh(LANTERN, lit=True))


def test_a_partial_refill_refusal_is_not_reported_as_an_invalid_argument() -> None:
    """A partly-fuelled lantern is a legitimate lantern state.

    So the refusal must carry the rules-domain category, never the
    structural one (human adjudication 2026-10-03, `LOW-9`).
    """
    partly_fuelled = LightSource(kind=LANTERN, remaining_turns=7, lit=False)
    with pytest.raises(LanternRefuelNotDefinedError):
        refuel_lantern(partly_fuelled)
    # And it is not a ValueError at all, so a caller filtering structural
    # input errors cannot swallow a source silence.
    with pytest.raises(Exception) as caught:
        refuel_lantern(partly_fuelled)
    assert not isinstance(caught.value, ValueError)


def test_refuelling_a_partly_spent_lantern_is_refused_whether_lit_or_not() -> None:
    """The precondition is about remaining fuel, not about burning."""
    partly_spent_lit = LightSource(kind=LANTERN, remaining_turns=7, lit=True)
    partly_spent_unlit = LightSource(kind=LANTERN, remaining_turns=7, lit=False)
    for source in (partly_spent_lit, partly_spent_unlit):
        with pytest.raises(
            LanternRefuelNotDefinedError, match="only for a lantern that has reached zero"
        ):
            refuel_lantern(source)


def test_refuel_refuses_a_non_light_source() -> None:
    with pytest.raises(ValueError, match="must be a LightSource"):
        refuel_lantern("lantern")  # type: ignore[arg-type]


def test_the_domain_errors_are_not_subclasses_of_value_error() -> None:
    """The taxonomy is real, not nominal.

    Three concrete siblings of ``Exception``. If any were a ``ValueError``
    subclass, the structural/rules-domain split would collapse at the
    catch site: a caller filtering malformed input would silently absorb a
    source silence. This is what makes the ``NOT ValueError`` assertions
    above coherent, and it is checked rather than assumed.
    """
    for error_type in (
        IgnitionNotDefinedError,
        IgnitionAttemptLimitError,
        LanternRefuelNotDefinedError,
    ):
        assert not issubclass(error_type, ValueError), f"{error_type.__name__} is a ValueError"
        assert error_type.__mro__ == (error_type, Exception, BaseException, object)


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
    filter, because filtering is not the caller's job.

    Note the asymmetry this test fixes in place: a VALID unlit source is
    accepted and simply does not contribute, while a MALFORMED member is
    refused outright (MED-5).
    """
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
    state to get out of step.

    Corrected 2026-10-03 under review-#2 finding `LOW-4`. This was written
    as ``assert not hasattr(cls, "__dataclass_fields__") or set(...) ==
    {...}`` — a disjunction that passes if the structure it inspects
    disappears, which is a vacuous pass dressed as a check. The dataclass
    is now asserted to exist first.
    """
    assert dataclasses.is_dataclass(MundaneLightContribution)
    assert set(MundaneLightContribution.__dataclass_fields__) == {"lit_sources"}
    assert isinstance(
        inspect.getattr_static(MundaneLightContribution, "any_mundane_source_lit"), property
    )
    assert isinstance(
        inspect.getattr_static(MundaneLightContribution, "max_mundane_radius_feet"), property
    )


def test_the_aggregate_refuses_a_non_tuple_and_non_source() -> None:
    with pytest.raises(ValueError, match="must be a tuple"):
        MundaneLightContribution(lit_sources=[])  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="must contain LightSource values"):
        MundaneLightContribution(lit_sources=("torch",))  # type: ignore[arg-type]


def test_querying_light_state_needs_no_surprise_or_encounter_state() -> None:
    """L34 — surprise is not an input to this card."""
    signature = inspect.signature(mundane_light_contribution)
    assert list(signature.parameters) == ["sources"]


def test_a_malformed_member_is_rejected_not_silently_dropped() -> None:
    """MED-5 — the aggregate refuses what `deplete` refuses.

    Before this correction a caller's type error degraded into
    `any_mundane_source_lit is False`: a plausible-looking answer, and the one
    output the card's Finding B warns hardest against over-reading. Both
    sibling functions now reject the same malformed input.
    """
    for bad in ["torch", {"lit": True}, None, 42]:
        with pytest.raises(ValueError, match="must contain LightSource values"):
            mundane_light_contribution([bad])  # type: ignore[list-item]
        with pytest.raises(ValueError, match="must contain LightSource values"):
            deplete([bad], 1)  # type: ignore[list-item]


def test_a_valid_unlit_source_is_accepted_and_simply_does_not_contribute() -> None:
    """The distinction MED-5 turns on: malformed is refused, unlit is not."""
    contribution = mundane_light_contribution(
        [LightSource.fresh(TORCH), LightSource(kind=TORCH, remaining_turns=0, lit=False)]
    )
    assert contribution.lit_sources == ()
    assert contribution.any_mundane_source_lit is False


def test_a_duck_typed_impostor_is_rejected() -> None:
    """A object that merely *looks* like a lit source must not slip through."""

    class _Impostor:
        lit = True
        remaining_turns = 6

    with pytest.raises(ValueError, match="must contain LightSource values"):
        mundane_light_contribution([_Impostor()])  # type: ignore[list-item]


def test_a_failed_1d6_leaves_its_own_branch_selectable() -> None:
    """L18 — using the case's OWN row (no skill, tinderbox, ORDINARY).

    The prior discharge cited a test looping over (skill, tinderbox, ORDINARY),
    which is L20's row, not L18's (MED-4). The card's L18 is a failed roll on
    the tinderbox branch; this card selects the branch and never rolls, so what
    it guarantees is that the same input re-selects the same branch.
    """
    for _ in range(3):
        assert _ignite(False, True, ORDINARY) is IgnitionOutcome.ROLL_1D6_IGNITE_1_2


# --- L15a / L15b: the multiple-source distinction --------------------------


def test_one_source_expiring_does_not_darken_the_party() -> None:
    """L15a — the decisive case, using the card's literal input.

    **Two lit torches**, one with 2 turns left and one with 6, depleted by 2:
    the first expires, the second still burns, and the aggregate still reports
    mundane illumination. (Previously this used a torch and a lantern while
    its own docstring said "two torches" — LOW-13. Behaviour is
    kind-independent, so the property held either way, but the test now
    exercises what the card actually writes.)
    """
    older = LightSource(kind=TORCH, remaining_turns=2, lit=True)
    newer = LightSource(kind=TORCH, remaining_turns=6, lit=True)

    spent = deplete([older, newer], 2)

    expired, still_burning = spent
    assert expired.remaining_turns == 0 and expired.lit is False
    assert still_burning.remaining_turns == 4 and still_burning.lit is True

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
    """L19b — guard. The selector carries nothing between calls.

    **Claim A (surface), narrowly.** This establishes that the function
    object itself holds no attribute state. The *module*-level half of the
    claim is established by ``test_the_module_scope_surface_is_exactly_approved``
    and ``test_no_module_level_mutable_state_exists``, not here.

    Corrected 2026-10-03 under review-#2 finding `MED-1`. This test
    previously filtered ``vars(light)`` for ``list``/``dict``/``set`` only,
    and a module-level ``_ROUNDS_SEEN = 0`` incremented inside
    ``ignition_outcome`` walked straight past it — an ``int`` is none of
    those three types. Filtering by *value type* was the wrong instrument;
    the approved **name set** is the right one.
    """
    function_state = [k for k in vars(ignition_outcome) if not k.startswith("__")]
    assert function_state == [], f"attribute state on the selector: {function_state}"


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

CATALOG_IDENTITY_FIELDS = frozenset({"name", "category"})

CATALOG_ECONOMIC_FIELDS = frozenset(
    f.name for f in dataclasses.fields(Item)
) - CATALOG_IDENTITY_FIELDS
"""`Item` fields EXP-006 must never read directly.

**Derived from `CHAR-004`'s own dataclass**, not hand-listed — corrected
2026-10-03 under review-#2 finding `LOW-2`. This was an eight-name literal
that happened to be complete; a new `Item` field would have become readable
with the suite green. Deriving it means `CHAR-004` adding a field
automatically extends the guard, which is the rank-1 shape mechanism the
project's guard-design order prescribes over a maintained denylist.
"""


def test_the_economic_field_set_is_derived_and_non_trivial() -> None:
    """Non-vacuity anchor for the guard set itself.

    **Claim A.** If `Item` were ever restructured so that `fields()` returned
    nothing, `CATALOG_ECONOMIC_FIELDS` would silently become empty and the
    read-guard below would pass on an empty forbidden set.
    """
    assert {f.name for f in dataclasses.fields(Item)} >= CATALOG_IDENTITY_FIELDS
    assert "price" in CATALOG_ECONOMIC_FIELDS
    assert "encumbrance_cn" in CATALOG_ECONOMIC_FIELDS
    assert CATALOG_IDENTITY_FIELDS.isdisjoint(CATALOG_ECONOMIC_FIELDS)
    assert len(CATALOG_ECONOMIC_FIELDS) >= 8


def test_each_light_source_binds_to_its_char_004_row() -> None:
    assert light._catalog_identity(TORCH).name == "Torch"
    assert light._catalog_identity(LANTERN).name == "Lantern"


def test_the_torch_uses_char_004s_exported_identity() -> None:
    """Human adjudication: TORCH has an export because it is the one
    commodity in both catalogs; the other three do not and are looked up."""
    from rules.character_creation import equipment

    assert light._catalog_identity(TORCH) is equipment.TORCH


def test_catalog_identity_refuses_an_unsupported_kind() -> None:
    with pytest.raises(ValueError, match="must be a LightSourceKind"):
        light._catalog_identity("torch")  # type: ignore[arg-type]


def test_oil_and_tinderbox_bind_to_their_rows() -> None:
    assert light._oil_flask_identity().name == "Oil"
    assert light._tinderbox_identity().name == "Tinder box"


def test_the_oil_identity_is_the_gear_row_not_the_weapon_row() -> None:
    """`Oil, Burning` is the Weapons row and belongs to COMBAT-* (L46)."""
    assert light._oil_flask_identity().name != "Oil, Burning"


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


def test_no_public_callable_can_emit_a_catalog_row() -> None:
    """`L42` — *"any price, `Coin` or encumbrance value **emitted**"*.

    **Claim A (machine-proved surface), and this is now the primary `L42`
    mechanism.** No public callable of this card returns a `CHAR-004`
    ``Item``, so no economic value is reachable through this card's public
    API — by value or by reference.

    Added 2026-10-03 under review-#2 finding `MED-2`. The previous mechanism
    established that the module never *accessed* an economic field, which is
    a different property from the one the card states. With the three
    identity accessors public, ``catalog_identity(TORCH).price`` did in fact
    reach a `Coin` through this card's API; the human adjudication of
    2026-10-03 made the binding private instead of defending it, which makes
    the card's actual wording provable rather than approximated.
    """
    checked = 0
    for name in sorted(APPROVED_DEFINITIONS):
        obj = getattr(light, name)
        if not isinstance(obj, FunctionType):
            continue
        hints = inspect.signature(obj).return_annotation
        assert "Item" not in str(hints), f"public {name} returns a catalog row: {hints}"
        checked += 1
    assert checked == 4, f"expected 4 public functions, inspected {checked}"

    # And the Item type itself is not re-exported under any public name.
    for name in APPROVED_DEFINITIONS:
        assert getattr(light, name) is not Item, f"{name} re-exports CHAR-004's Item"


def test_no_catalog_economic_field_is_ever_read_directly() -> None:
    """`L42`, supporting half — nothing in this module reads an economic field.

    **Claim A, stated narrowly.** What this establishes is exactly: *EXP-006
    production code contains no approved reflective catalog-access path and
    does not directly read catalog-economic fields.* It is **not** a claim
    that economic fields are unreachable by every conceivable reflection
    mechanism in Python — review #2 defeated that stronger claim with
    ``object.__getattribute__(item, "price")``, and no AST matcher short of a
    static analyzer closes it. The boundary remains partly a **reviewed**
    one (claim C), and is recorded as such in `CASE_DISCHARGE`.

    The forbidden field set is derived from `CHAR-004`'s own dataclass, so a
    new `Item` field extends this guard automatically.
    """
    tree = ast.parse(inspect.getsource(light))
    attributes = [node for node in ast.walk(tree) if isinstance(node, ast.Attribute)]
    assert attributes, "guard anchored on zero attribute accesses"
    leaked = {node.attr for node in attributes} & CATALOG_ECONOMIC_FIELDS
    assert leaked == set(), f"EXP-006 reads CHAR-004 economic field(s): {leaked}"

    subscripts = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Subscript)
        and isinstance(node.slice, ast.Constant)
        and node.slice.value in CATALOG_ECONOMIC_FIELDS
    ]
    assert subscripts == [], "an economic field is reached by subscript"


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
    """EXP-006's whole **direct** import graph, stated positively.

    Proves there is no **direct** production import of TurnCredit, EXP-001
    time machinery, the CHAR-012 skill resolver, RNG, encounter, combat or
    magic resolution, or any world-darkness state.

    **It does not claim a transitive property, and must not be read as one**
    (MED-6). Importing this module loads `rng` and `rules.currency`
    transitively, because the `CHAR-004` seam this card is *directed* to use
    imports them itself. That is forced by the approved plan §1.1 ("use
    `catalog_item(...)`"; "no landed `CHAR-004` production code changes"),
    and it is behaviourally clean: no RNG object is constructed, no RNG
    method called, no `Coin` read. The accurate guarantee is **"no RNG is
    consumed"**, not "nothing of the kind is reachable".
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


# =========================================================================
# The exact RUNTIME surface guard
# =========================================================================
#
# WHAT THIS SECTION LITERALLY PROVES, and nothing beyond it:
#
#   **At normal module initialization**, EXP-006's two production modules
#   bind exactly the approved **concrete** module-level namespace; its
#   approved classes expose exactly the approved effective member surface,
#   with exactly the approved base classes; and every approved public
#   callable has exactly the approved signature.
#
# WHAT IT DOES NOT PROVE -- stated plainly, because three reviews have now
# each broken a broader reading of it:
#
#   * It does NOT prove that no forbidden *behavior* can ever be written.
#   * It does NOT prove the absence of **dynamic module attribute hooks**.
#     A module-level `__getattr__` (PEP 562) serves names that are never
#     bound in `vars()`, so it is outside what this mechanism observes.
#     Review #3 demonstrated exactly that. **This is deliberately NOT
#     chased**: by human direction of 2026-10-03, the claim is narrowed to
#     what the mechanism observes rather than the guard being widened. No
#     `__getattr__` denylist, no generic dynamic-attribute detector and no
#     static analyzer is added, because production code uses no such
#     mechanism -- independently confirmed -- and a fourth-generation
#     universal guard is not authorized.
#   * It does NOT prove the absence of arbitrary future reflection, nor of
#     every possible Python mechanism capable of exposing a value.
#
# A reviewer still has to read the code. Three distinct kinds of claim are
# kept apart deliberately, and the `CASE_DISCHARGE` ledger labels each case
# with which kind discharges it:
#
#   A. machine-proved surface   -- this section
#   B. machine-proved behavior  -- the behavioral and invariant tests
#   C. reviewed ownership boundary, NOT machine proof -- recorded as such
#
# Labelling a C claim as an A claim is the defect the second independent
# review found, and is forbidden here.
#
# DESIGN HISTORY, so the shape is not casually undone. Review #1
# (2026-10-01) broke a forbidden-token DENYLIST: `VisibilityCategory`
# survived because its name is one token that never equals `visibility`,
# and `ration_spoilage_turns` survived because the set held `rations`.
# That was answered with an AST allowlist over `tree.body`. Review #2
# (2026-10-03) broke *that*, six ways: a definition inside `if True:`,
# inside `try:`, injected through `globals()` from a top-level `for`, an
# inherited member from a private mixin, a forbidden parameter on the
# classmethod `LightSource.fresh`, and a module-level `int` counter that
# a mutable-container filter could not see.
#
# The lesson taken is NOT "add more patterns". It is that the **concrete
# bound namespace** of an imported module is an observable fact worth
# pinning, and the authoritative surface of a class is its **effective**
# surface including inheritance. Both are read from the imported objects,
# so a name created by any executable statement at module scope -- `if`,
# `try`, `for`, `while`, `with`, `match`, a comprehension, or
# `globals()[...] = ...` -- is visible, because by then it is simply a key
# in `vars(light)`.
#
# Review #3 (2026-10-03) then showed the limit of that: a module-level
# `__getattr__` serves attributes that are never keys in `vars()` at all,
# so no namespace comparison can see them. The arms race stops here. The
# mechanism's claim is narrowed to the concrete bound namespace at import
# time, which is true and useful; anything relying on the absence of a
# dynamic hook is a **reviewed** boundary (claim C), not claim A.

# Every module-level name EXP-006 is approved to bind, partitioned by role.
# The partition is the point: a new name must be classified by a human
# before this guard will pass, and "it starts with an underscore" is not a
# way out. `MODULE_SCOPE_IS_CONSTANT` below additionally pins the kind of
# value each may hold, so an unauthorized accumulator cannot hide behind an
# approved name's role.

APPROVED_IMPORTED_NAMES: frozenset[str] = frozenset(
    {
        "Enum",
        "Final",
        "Item",
        "Iterable",
        "MappingProxyType",
        "annotations",
        "auto",
        "catalog_item",
        "dataclass",
        # Raised by this module, defined in rules.exploration.errors.
        "IgnitionAttemptLimitError",
        "IgnitionNotDefinedError",
        "LanternRefuelNotDefinedError",
    }
)

APPROVED_PRIVATE_NAMES: frozenset[str] = frozenset(
    {
        "_CATALOG_NAMES",
        "_IGNITION_MATRIX",
        "_LIGHT_SOURCE_IDENTITIES",
        "_TORCH_ITEM",
        "_require_elapsed_turns",
        # The CHAR-004 identity binding, made private 2026-10-03 under
        # review-#2 finding MED-2. Tests reach these deliberately, to prove
        # the binding restates nothing; no caller needs them.
        "_catalog_identity",
        "_oil_flask_identity",
        "_tinderbox_identity",
    }
)

APPROVED_DEFINITIONS: frozenset[str] = frozenset(
    {
        "FRESH_DURATION_TURNS",
        "LANTERN_TURNS_PER_FLASK",
        "MUNDANE_LIGHT_RADIUS_FEET",
        "TORCH_TURNS",
        "IgnitionConditions",
        "IgnitionOutcome",
        "LightSource",
        "LightSourceKind",
        "MundaneLightContribution",
        "deplete",
        "ignition_outcome",
        "mundane_light_contribution",
        "refuel_lantern",
    }
)

# The approved EFFECTIVE member surface of each approved class, read with
# `dir()` so a member arriving through a base class or mixin is included.
# `APPROVED_BASES` pins the inheritance itself, so a mixin fails twice.

APPROVED_MEMBERS: dict[str, frozenset[str]] = {
    "LightSourceKind": frozenset({"TORCH", "LANTERN"}),
    "IgnitionConditions": frozenset({"ORDINARY", "ADVERSE"}),
    "IgnitionOutcome": frozenset({"AUTOMATIC", "ROLL_1D6_IGNITE_1_2", "ROUTED_SKILL_CHECK"}),
    "LightSource": frozenset(
        {"kind", "remaining_turns", "lit", "fresh", "illumination_radius_feet"}
    ),
    "MundaneLightContribution": frozenset(
        {"lit_sources", "any_mundane_source_lit", "max_mundane_radius_feet"}
    ),
}

APPROVED_BASES: dict[str, tuple[str, ...]] = {
    "LightSourceKind": ("LightSourceKind", "Enum", "object"),
    "IgnitionConditions": ("IgnitionConditions", "Enum", "object"),
    "IgnitionOutcome": ("IgnitionOutcome", "Enum", "object"),
    "LightSource": ("LightSource", "object"),
    "MundaneLightContribution": ("MundaneLightContribution", "object"),
}

# Every approved public callable, keyed by its dotted path. Review #2 added
# `party_surprised` and `has_infravision` to the classmethod
# `LightSource.fresh` and escaped, because only module-level functions were
# pinned. Class members, properties and the generated dataclass constructors
# are therefore all pinned here too.

APPROVED_CALLABLES: dict[str, tuple[str, ...]] = {
    "deplete": ("sources", "elapsed_turns"),
    "refuel_lantern": ("source",),
    "mundane_light_contribution": ("sources",),
    "ignition_outcome": (
        "has_fire_building",
        "has_tinderbox",
        "conditions",
        "attempt_already_made_this_round",
    ),
    "LightSource.fresh": ("kind", "lit"),
    "LightSource.illumination_radius_feet": ("self",),
    "LightSource.__init__": ("self", "kind", "remaining_turns", "lit"),
    "MundaneLightContribution.any_mundane_source_lit": ("self",),
    "MundaneLightContribution.max_mundane_radius_feet": ("self",),
    "MundaneLightContribution.__init__": ("self", "lit_sources"),
}

# The kinds of value a module-level name may hold. Everything EXP-006 binds
# at module scope is a constant, a read-only mapping, a frozen value object,
# a type or a function. A `list`, `dict`, `set` or ordinary mutable object
# fails -- and so does a new scalar, because it would need a name nobody
# approved.
MODULE_SCOPE_IS_CONSTANT = (int, str, frozenset, MappingProxyType, type, FunctionType)


def _is_immutable_module_state(value: object) -> bool:
    """True for the value kinds EXP-006 may bind at module scope.

    A frozen dataclass instance counts: ``_TORCH_ITEM`` is `CHAR-004`'s own
    frozen `Item`, and rebinding its fields raises. An unfrozen dataclass,
    a list, a dict, a set or a plain object does not.
    """
    if isinstance(value, MODULE_SCOPE_IS_CONSTANT):
        return True
    cls = type(value)
    if not dataclasses.is_dataclass(cls):
        return False
    return bool(cls.__dataclass_params__.frozen)  # type: ignore[attr-defined]


def _module_scope_names(module: ModuleType) -> set[str]:
    """Every non-dunder name the module **concretely binds** once imported.

    Read from the live namespace, not parsed from the source, which is why
    a name created inside ``if``, ``try``, ``for``, ``while``, ``with``,
    ``match`` or by ``globals()[...] = ...`` is visible here: by import
    time it is just a key in ``vars()``.

    **Scope limit, stated rather than papered over.** Dunder names are
    excluded, so a module-level ``__getattr__`` (PEP 562) is **not**
    observed — and such a hook serves attributes that are never keys in
    ``vars()`` at all, so no namespace comparison could observe them.
    Callers of this helper may therefore claim only what it sees: the
    concrete bound namespace at normal module initialization.
    """
    return {n for n in vars(module) if not (n.startswith("__") and n.endswith("__"))}


def _signature_of(dotted: str) -> tuple[str, ...]:
    """Parameter names of an approved callable, resolved through descriptors."""
    if "." not in dotted:
        return tuple(inspect.signature(getattr(light, dotted)).parameters)
    cls_name, member = dotted.split(".", 1)
    cls = getattr(light, cls_name)
    raw = inspect.getattr_static(cls, member)
    if isinstance(raw, property):
        assert raw.fget is not None, f"{dotted}: property has no getter to inspect"
        return tuple(inspect.signature(raw.fget).parameters)
    if isinstance(raw, (classmethod, staticmethod)):
        # Resolve through the class so the bound first parameter is dropped,
        # matching how a caller actually invokes it.
        return tuple(inspect.signature(getattr(cls, member)).parameters)
    return tuple(inspect.signature(raw).parameters)


def test_the_module_scope_surface_is_exactly_approved() -> None:
    """At normal module initialization, EXP-006's concrete bound namespace
    matches the approved namespace.

    **Claim A (machine-proved OBSERVED surface). Narrowed 2026-10-03 by
    human direction, under review-#3 finding `HIGH-1`.** This test
    previously claimed that "any new module-level name, however spelled and
    however created, fails here". That was false: a module-level
    ``__getattr__`` (PEP 562) serves attributes that are never keys in
    ``vars()``, and review #3 demonstrated unapproved ``VisibilityCategory``
    and ``encounter_distance_from_light`` reachable with this suite green.

    What is claimed now is exactly what is observed: the **concrete bound**
    namespace at import time. The absence of a dynamic attribute hook is
    **not** claimed here and is **not** chased — production code uses none
    (independently confirmed), and no fourth-generation universal guard is
    authorized.

    Partitioned into public / imported / private deliberately. An
    underscore is *not* an exemption: review #2 escaped the previous guard
    with a module-level ``_TURNS_COUNTED = 0`` accumulator and with a
    private ``_AmbientMixin``, both invisible to a public-only check. Any
    new **bound** module-level name, however spelled and by whatever
    executable statement created, fails here until a human classifies it
    into one of the three sets.
    """
    actual = _module_scope_names(light)
    approved = APPROVED_DEFINITIONS | APPROVED_IMPORTED_NAMES | APPROVED_PRIVATE_NAMES
    assert actual, "guard anchored on an empty namespace"
    assert actual == set(approved), (
        f"unapproved module-level names: {sorted(actual - set(approved))}; "
        f"missing: {sorted(set(approved) - actual)}"
    )


def test_the_errors_module_scope_surface_is_exactly_approved() -> None:
    """The sibling error module's concrete bound namespace, same treatment.

    **Claim A (observed surface), same scope limit as the module above:**
    three concrete types, no base class, nothing else bound — so a fourth
    type or a stray bound name cannot arrive unnoticed. A dynamic attribute
    hook is outside what this observes, and is not claimed against.
    """
    actual = _module_scope_names(exploration_errors)
    assert actual == {
        "annotations",
        "IgnitionNotDefinedError",
        "IgnitionAttemptLimitError",
        "LanternRefuelNotDefinedError",
    }, f"unapproved names in errors.py: {sorted(actual)}"


def test_no_module_level_mutable_state_exists() -> None:
    """Every module-level name EXP-006 binds holds an immutable value.

    **Claim A (machine-proved observed surface), narrowed 2026-10-03 by
    human direction under review-#3 finding `MED-3`.** This is the exact
    claim: of the names EXP-006 concretely binds at module scope, none
    holds mutable state.

    **The previous wording asserted an exhaustive dichotomy** — that an
    accumulator "needs *either* a new name (the surface guard refuses it)
    *or* an approved constant's name (the value tests refuse that)". Review
    #3 falsified it with a third option: a **private class attribute** on an
    approved class (``LightSource._rounds_elapsed``, incremented inside
    ``deplete``) is a working elapsed-turn accumulator that is not a
    module-level name, is filtered out of the public class-surface check,
    and changes neither ``__slots__`` nor the MRO. That claim is withdrawn.

    **No shipped state acts as a clock** — independently re-confirmed
    2026-10-03 across the module namespace, both value types' full class
    dictionaries (slot descriptors, properties and one classmethod only),
    and all four public function objects (no attribute state). The
    *boundary* holds in fact; what is narrowed is the *proof*.

    That no EXP-006-owned clock exists is therefore a **reviewed
    architectural ownership boundary** (claim C), supported by this
    observed-surface check, the import-graph guard and
    `ARCHITECTURE.md` §5 — not a machine-enforced invariant. ``L13`` and
    ``L14`` are classified accordingly in `CASE_DISCHARGE`. This test does
    not claim to recognize every semantic notion of a "clock", and no
    broader detector is authorized.

    Scoped to the names EXP-006 itself **binds** — public and private. The
    twelve imported names are excluded on purpose: what ``Enum`` or
    ``annotations`` holds is its own module's business, and
    ``APPROVED_IMPORTED_NAMES`` is what pins the import set.
    """
    own_names = APPROVED_DEFINITIONS | APPROVED_PRIVATE_NAMES
    checked = 0
    for name in sorted(own_names):
        value = vars(light)[name]
        assert _is_immutable_module_state(value), (
            f"module-level {name} holds a mutable {type(value).__name__} -- "
            f"an unauthorized accumulator or cache?"
        )
        checked += 1
    assert checked == len(own_names) == 21, f"inspected {checked} of EXP-006's own names"
    assert len(_module_scope_names(light)) == 33


def test_all_matches_the_approved_surface() -> None:
    """``__all__`` and the approved public set must not drift apart."""
    assert set(light.__all__) == set(APPROVED_DEFINITIONS)
    assert len(light.__all__) == len(set(light.__all__)), "duplicate in __all__"


def test_public_class_members_are_exactly_approved() -> None:
    """The approved classes expose exactly the approved EFFECTIVE surface.

    **Claim A.** Uses ``dir()``, not ``vars()``. Review #2 added
    ``encounter_range_feet`` and ``ambient_state`` to the aggregate through a
    private mixin; ``vars(cls)`` sees only a class's own ``__dict__`` and
    missed both. ``dir()`` includes inherited members, so it fails.
    """
    checked = 0
    for cls_name, approved in APPROVED_MEMBERS.items():
        cls = getattr(light, cls_name)
        actual = {n for n in dir(cls) if not n.startswith("_")}
        assert actual == set(approved), (
            f"{cls_name}: unapproved members {sorted(actual - set(approved))}; "
            f"missing {sorted(set(approved) - actual)}"
        )
        checked += 1
    assert checked == len(APPROVED_MEMBERS) == 5


def test_approved_classes_have_exactly_the_approved_bases() -> None:
    """No mixin, no intermediate base, and the two value types stay slotted.

    **Claim A.** The second, independent barrier against review #2's
    inheritance escape: even a mixin contributing no *new* public member
    would change the MRO and fail here.
    """
    checked = 0
    for cls_name, approved_mro in APPROVED_BASES.items():
        cls = getattr(light, cls_name)
        assert tuple(c.__name__ for c in cls.__mro__) == approved_mro, (
            f"{cls_name}: MRO {[c.__name__ for c in cls.__mro__]} != {list(approved_mro)}"
        )
        checked += 1
    assert checked == len(APPROVED_BASES) == 5

    # Slots are what make an unapproved instance attribute unassignable.
    assert light.LightSource.__slots__ == ("kind", "remaining_turns", "lit")
    assert light.MundaneLightContribution.__slots__ == ("lit_sources",)


def test_every_approved_public_callable_signature_is_pinned() -> None:
    """Every approved public callable has exactly the approved parameters.

    **Claim A.** Covers module functions, the ``fresh`` classmethod, both
    dataclass constructors and all three properties. Review #2 added
    ``party_surprised`` and ``has_infravision`` to ``LightSource.fresh`` and
    escaped a guard that pinned module-level functions only.
    """
    checked = 0
    for dotted, approved in APPROVED_CALLABLES.items():
        actual = _signature_of(dotted)
        assert actual == approved, f"{dotted}: parameters {actual} != approved {approved}"
        checked += 1
    assert checked == len(APPROVED_CALLABLES) == 10


def test_no_public_callable_escapes_the_signature_guard() -> None:
    """Every public callable in the approved surface IS pinned above.

    **Claim A, and the non-vacuity anchor for the guard above.** Without
    this, adding a new public method and forgetting to list it in
    ``APPROVED_CALLABLES`` would simply not be checked — which is exactly
    how ``LightSource.fresh`` went unpinned through review #2.
    """
    discovered: set[str] = set()
    for name in APPROVED_DEFINITIONS:
        obj = getattr(light, name)
        if isinstance(obj, FunctionType):
            discovered.add(name)
    for cls_name, members in APPROVED_MEMBERS.items():
        cls = getattr(light, cls_name)
        if issubclass(cls, Enum):
            continue  # enum members are data, not callables
        discovered.add(f"{cls_name}.__init__")
        for member in members:
            raw = inspect.getattr_static(cls, member)
            if isinstance(raw, (property, classmethod, staticmethod, FunctionType)):
                discovered.add(f"{cls_name}.{member}")

    assert discovered == set(APPROVED_CALLABLES), (
        f"public callables not pinned: {sorted(discovered - set(APPROVED_CALLABLES))}; "
        f"pinned but no longer present: {sorted(set(APPROVED_CALLABLES) - discovered)}"
    )


# =========================================================================
# CASE_DISCHARGE — traceability, NOT certification
# =========================================================================
#
# This ledger answers exactly one question:
#
#     Where is this approved case discharged?
#
# It does NOT answer:
#
#     Have we formally proved no future implementation could violate it?
#
# Role narrowed 2026-10-03 under review-#2 findings `MED-2`, `LOW-6` and
# `LOW-7`. The ledger had drifted into reading as a certification, and
# several rows cited a guard for a property that guard did not establish —
# `L4` credited "one radius constant" for a property a behavioral test
# actually holds, and `L18` was classed as behavior this module does not
# produce. A row that names the wrong mechanism is worse than no row: it
# tells a later reader the boundary is machine-held when it is not.
#
# Each row is prefixed with the KIND of claim that discharges it:
#
#   surface:   machine-enforced OBSERVED surface   (claim A)
#   behavior:  machine-enforced behavior           (claim B)
#   invariant: machine-enforced refusal            (claim B)
#   reviewed:  a reviewed architectural ownership boundary,
#              NOT machine proof                   (claim C)
#   routed:    not owned by this card at all
#
# Labelling a `reviewed:` claim as `surface:` is the defect review #2
# found. Do not do it.
#
# RECLASSIFIED 2026-10-03 under review-#3 findings `HIGH-1`, `MED-3` and
# `LOW-2`, by human direction. Twelve rows previously read `surface:` on
# the strength of "no such name is bound at module scope". Review #3
# showed a module-level `__getattr__` can serve an unapproved name that is
# never bound — demonstrating exactly the `Visibility` category (`L30`,
# `L31`) and the light→distance path (`L36`) those rows claimed to
# exclude. The observed-namespace check is still true and still useful,
# but it does not establish *absence of the capability*, so those rows are
# now `reviewed:` — the project's real guarantee there is an approved
# architectural ownership boundary plus independent review, which is
# exactly what claim C means. `L13`/`L14`/`L19b` move for the parallel
# reason in `MED-3` (a private class attribute is outside the mechanism),
# and `L46` moves because `LOW-2` showed its cited mechanism addressed a
# different property than the case states.
#
# This is a NARROWING OF CLAIMS, not a weakening of the implementation:
# nothing shipped uses a dynamic hook or holds mutable state, re-confirmed
# independently. No fourth-generation universal guard is authorized, and a
# future reviewer finding another Python construct outside a guard's
# explicitly narrow claim is a limitation, not by itself a defect.

CASE_DISCHARGE: dict[str, str] = {
    # --- machine-proved behavior (claim B) ---------------------------------
    "L1": "behavior: lit torch radius 30",
    "L2": "behavior: lit lantern radius 30",
    "L3": "behavior: unlit illuminates nothing",
    "L4": "behavior: both kinds parametrized to the same 30; radii cannot differ",
    "L5": "behavior: no brighter/dimmer figure is produced for either kind",
    "L6": "behavior: fresh torch 6 turns",
    "L7": "behavior: fresh lantern 24 turns",
    "L8": "behavior: 1 elapsed turn -> 5 remaining",
    "L9": "behavior: 6 elapsed turns -> EXPENDED, contributes nothing",
    "L10": "behavior: floors at 0, never negative",
    "L11": "behavior: unlit sources do not deplete",
    "L12": "behavior: refuel -> 24 turns, still unlit",
    "L15a": "behavior: two torches, one expires, the other still contributes",
    "L17": "behavior: tinderbox 1d6 branch is SELECTED (the roll is the caller's)",
    "L18": "behavior: its own row re-selects; the card's roll is not ours to make",
    "L19a": "behavior: first attempt evaluates and records nothing",
    "L20": "behavior: skill + tinderbox + ordinary -> AUTOMATIC",
    "L21": "behavior: skill, no tinderbox, ordinary -> 1d6",
    "L22": "behavior: adverse -> ROUTED_SKILL_CHECK, incl. the SR-11 row",
    "L27": "behavior: aggregate reports a lit source",
    "L28": "behavior: aggregate empty when none lit, asserting nothing further",
    "L34": "behavior: query succeeds with no surprise state supplied",
    # --- machine-proved refusals (claim B) ---------------------------------
    "L12a": "invariant: LanternRefuelNotDefinedError on a VALID lantern's partial refill",
    "L19": "invariant: IgnitionAttemptLimitError on a second same-round attempt",
    "L23": "invariant: IgnitionNotDefinedError, no skill + tinderbox + adverse",
    "L24": "invariant: IgnitionNotDefinedError, no skill and no tinderbox",
    "L26": "invariant: adverse never defaults to the 1d6",
    # --- machine-enforced OBSERVED surface (claim A) -----------------------
    # Each of these rests on a mechanism a dynamic attribute hook cannot
    # fake: a parsed import graph, a pinned callable signature, a pinned
    # effective class surface, or an AST property of the source itself.
    "L15b": "surface: deplete's parameters pinned; no world-state value returned",
    "L16": "surface: no hour/minute name is bound, and the source has no scaling operator",
    "L25": "surface: import graph has no CHAR-012; the enum member carries no value",
    "L32": "surface: class surfaces pinned via dir(); no classifying member exists",
    "L33": "surface: no DIRECT rng import, so no distance roll can be made here",
    "L35": "surface: EVERY public signature pinned -- no surprise parameter",
    "L38": "surface: signatures and class surfaces pinned; CHAR-005 unimported",
    "L39": "surface: class surfaces pinned via dir(), so inherited members fail",
    "L40": "surface: EVERY public signature pinned, incl. LightSource.fresh",
    "L41": "surface: LightSourceKind members pinned to exactly TORCH/LANTERN",
    "L42": "surface: no approved public callable returns an Item; Item not re-exported",
    # --- reviewed architectural ownership boundaries (claim C) -------------
    # NOT machine proof. The observed-namespace check supports each of
    # these and no unapproved name is bound, but absence of the *capability*
    # is established by the approved architecture, the card's ownership
    # routing and independent review -- not by an executable proof. See the
    # reclassification note above (review #3 `HIGH-1`, `MED-3`, `LOW-2`).
    "L13": "reviewed: no time import and no bound counter; no-counting is reviewed",
    "L14": "reviewed: no bound mutable state, slots/MRO pinned; absence is reviewed",
    "L15": "reviewed: no burn-out/proration name is bound; ownership is reviewed",
    "L19b": "reviewed: selector holds no attribute state; no-round-tracking reviewed",
    "L29": "reviewed: no NO_LIGHT or world-state name is bound; ENC-001 owns it",
    "L30": "reviewed: no Visibility name is bound; ENC-001 owns Visibility",
    "L31": "reviewed: no Visibility category is bound, incl. conditional creation",
    "L36": "reviewed: no distance-returning name is bound; ENC-001 owns distance",
    "L37": "reviewed: nothing asserts blindness; that this is COMPLETE is reviewed",
    "L37a": "reviewed: no CompleteDarkness name is bound; the owner is unresolved",
    "L43": "reviewed: no ration name is bound; ownership deliberately unassigned",
    "L44": "reviewed: no starvation name is bound; causation has no Rule ID",
    "L45": "reviewed: no weapon name is bound; COMBAT-*/CHAR-004 own torch-as-weapon",
    "L46": "reviewed: no missile/pursuit-delay name is bound; RC states no delay mechanic",
    # --- not owned by this card (routed) -----------------------------------
    "L47": "routed: reports any_mundane_source_lit; item/skill not owned here",
}

CLAIM_KINDS = ("surface", "behavior", "invariant", "reviewed", "routed")


def test_every_approved_case_is_accounted_for() -> None:
    """§13 — the complete ledger, reconciled against the finished card.

    Many cases are discharged by **absence** — no such name, member,
    parameter or operation exists — which leaves no case ID in a test name.
    This map is the audit trail for those, so no case goes unaccounted for.

    **No code was written to turn a non-owned assertion into executable
    behavior.**
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

    # Added 2026-10-03 under review-#1 finding MED-4. Two distinct cases
    # sharing one discharge string is how the ledger previously overclaimed:
    # a generic phrase copied across rows reads as coverage without being it.
    # L32 ("infravision folded into a visibility classification") and L40
    # ("infravision possession decided here") both read "no infravision
    # parameter", which named neither case's actual mechanism.
    duplicates = {v for v in CASE_DISCHARGE.values() if list(CASE_DISCHARGE.values()).count(v) > 1}
    assert duplicates == set(), f"two cases share one discharge description: {duplicates}"

    # Every row declares which KIND of claim discharges it, so a reviewed
    # boundary can never be read as machine proof (review-#2 MED-2).
    for case, discharge in CASE_DISCHARGE.items():
        kind = discharge.split(":", 1)[0]
        assert kind in CLAIM_KINDS, f"{case}: unknown claim kind {kind!r}"


def test_the_case_category_counts_are_recomputed_not_carried_over() -> None:
    """The authoritative 53-case split, computed from the rows themselves.

    Every governance artifact that states a split must agree with this. The
    numbers are deliberately asserted here rather than written into prose
    and copied around: review #2 found three mutually inconsistent totals
    across the implementation plan and the Pre-Code Gate, each one a figure
    that had been transcribed rather than recomputed.
    """
    counts = {kind: 0 for kind in CLAIM_KINDS}
    for discharge in CASE_DISCHARGE.values():
        counts[discharge.split(":", 1)[0]] += 1

    # Recomputed 2026-10-03 under review-#3 HIGH-1/MED-3/LOW-2. The prior
    # split (23/5/23/1/1) is NOT preserved for continuity: twelve rows moved
    # from `surface` to `reviewed` because an observed-namespace check does
    # not establish absence of a capability, and `L46` moved from `behavior`
    # for the LOW-2 reason. The total is unchanged because the card's case
    # set is unchanged.
    assert counts == {
        "behavior": 22,
        "invariant": 5,
        "surface": 11,
        "reviewed": 14,
        "routed": 1,
    }, f"recompute the published split: {counts}"
    assert sum(counts.values()) == 53


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
    # `equipment` is NOT forbidden here: the identity binding consumes
    # CHAR-004 rows legitimately. That no economic value can be emitted is a
    # separate and now stronger guard -- test_no_public_callable_can_emit_a_
    # catalog_row, backed by test_no_catalog_economic_field_is_ever_read_
    # directly. The complete import surface is asserted by
    # test_the_complete_production_dependency_surface.


def test_no_unauthorized_slice_behaviour_is_exposed() -> None:
    """All four slices are now authorized, so this guard protects only the
    card's **permanently excluded** responsibilities (§B, implementation
    plan §4) — the ones no slice may ever add.

    **Claim C — a reviewed boundary, not machine proof.** This is a token
    denylist. Review #1 proved a denylist can be walked past by spelling
    (`VisibilityCategory`, `ration_spoilage_turns`), and it is kept only as
    a cheap second net over obvious regressions. The *surface* claim is made
    by the module-scope, class-surface and signature guards; this test is
    not cited as the sole mechanism for any case.

    ``skill`` is deliberately not forbidden: ``ROUTED_SKILL_CHECK``
    legitimately *names* the owner it routes to, and a name test could not
    establish whether the resolver is imported — the import graph does that.
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
