"""CHAR-001 §5 — Chapter 10 above-1st-level ability-score generation.

See docs/rules/character_creation/ability_score_generation.md (Status:
APPROVED) §5 for the governing specification, and
docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §7.8/§7.8.1 for the
approved implementation contract this module implements (Slice E).

RC p. 130, Step 2 offers the DM two alternatives when creating a character
that starts **above 1st level**:

    First Method  — Rolling and Assigning
                    roll 3d6 eight times, keep the six best, and assign
                    them to abilities in any order.

    Second Method — Point Allocation
                    the DM supplies a point total, either 60 + 5d6 or an
                    equal allotment of at least 60 and at most 90, which
                    the player distributes across the six abilities. The
                    3-18 range per ability still applies.

SEPARATION FROM ORDINARY GENERATION
-----------------------------------
**This module exists in order to be unreachable from ordinary 1st-level
creation.** CHAR-001 §1's ``generate_ability_scores`` is the only 1st-level
generation path, and ``ability_score_generation.py`` does not import this
module — an import-graph fact, not a convention, and the mechanism by which
approved case **H6** is preserved.

The separation is deliberately bidirectional: this module does not import
ordinary generation either. The two are sibling pure rule modules with no
coupling in either direction.

*"Not V1-wired" does not mean "not implemented."* H1-H5 are implemented
here; H6 guards the boundary.

It does not, and must not:

- be reachable from, or dispatched by, ordinary 1st-level generation;
- apply the Chapter 1 discard provision (SR-4). That is §6.1's, and
  Chapter 10 specifies its own generation procedures;
- invoke the Chapter 13 switch or the Chapter 1 2-for-1 trade. Any later
  composition belongs to a caller or a future approved flow;
- choose an assignment or an allocation for the player. Both are supplied;
  this module validates and applies them;
- introduce a generation-method mode, flag, builder, session, player
  object or any other orchestration;
- reroll, replace or discard-and-reroll any result.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from rng import RNG
from rules.character_creation.ability import Ability, AbilityScores
from rules.character_creation.errors import (
    AbilityScoreDomainError,
    PointAllocationError,
)

__all__ = [
    "allocate_points",
    "assign_scores",
    "roll_and_keep_six",
    "roll_point_allocation_total",
]


_ABILITY_COUNT = 6
"""The six abilities a character has (CHAR-001 §1)."""

_FIRST_METHOD_ROLLS = 8
"""First Method: "The player rolls 3d6 eight times" (RC p. 130)."""

_GENERATION_EXPRESSION = "3d6"
"""One ability's worth of dice, as in §1."""

_POINT_ALLOCATION_EXPRESSION = "5d6"
"""Second Method: "the player rolls 5d6, adds 60 to the total"."""

_POINT_ALLOCATION_BASE = 60
"""The 60 added to 5d6 in the rolled form of the Second Method."""

MINIMUM_ALLOTMENT = 60
"""RC bounds an equal allotment at "at least 60" (approved case H5)."""

MAXIMUM_ALLOTMENT = 90
"""RC bounds an equal allotment at "no more than 90" (approved case H5).

The rolled form produces only 65-90, because 5d6 runs 5-30. That does
**not** narrow the accepted domain: 60-64 remain valid caller-supplied
totals under the equal-allotment form, and :func:`allocate_points` is
deliberately agnostic about which form produced its total."""

_MINIMUM_SCORE = 3
"""The standing range limitation's floor (CHAR-001 §1; RC p. 130)."""

_MAXIMUM_SCORE = 18
"""The standing range limitation's ceiling. The same limitation CHAR-001
§4 rule R11 applies to the trade; here it bounds an allocated score
(approved case H4)."""


def _assembled(values: Mapping[Ability, int]) -> AbilityScores:
    """An ``AbilityScores`` from a complete per-ability mapping."""
    return AbilityScores(
        values[Ability.STRENGTH],
        values[Ability.INTELLIGENCE],
        values[Ability.WISDOM],
        values[Ability.DEXTERITY],
        values[Ability.CONSTITUTION],
        values[Ability.CHARISMA],
    )


def roll_and_keep_six(rng: RNG) -> tuple[int, ...]:
    """First Method: roll ``3d6`` eight times and keep the six best.

    Consumes exactly **eight** ``3d6`` expressions — 24 d6 draws and eight
    roll sequence numbers (approved case H2). Nothing is rerolled,
    replaced, or discarded and re-rolled.

    Returns the six retained values **in their original roll order**, the
    two lowest having been removed. That order is a *representation only*:
    RC assigns it no mechanical meaning, and **the player chooses which
    ability receives which value** — see :func:`assign_scores`. Roll order
    is used rather than a descending sort precisely so the tuple's shape
    cannot be mistaken for an assignment rule.

    Where equal values straddle the six/two cut, which of them is
    discarded is mechanically irrelevant, because the retained *multiset*
    is identical either way. **No gameplay tie-break is invented**: the
    earlier roll is dropped, as a deterministic representation choice.

    This method does **not** assign the results to abilities.
    """
    rolled = [
        rng.roll(_GENERATION_EXPRESSION).total for _ in range(_FIRST_METHOD_ROLLS)
    ]
    ranked = sorted(enumerate(rolled), key=lambda pair: (pair[1], pair[0]))
    discarded = {index for index, _ in ranked[: _FIRST_METHOD_ROLLS - _ABILITY_COUNT]}
    return tuple(
        value for index, value in enumerate(rolled) if index not in discarded
    )


def assign_scores(
    kept_scores: Sequence[int], assignment: Sequence[Ability]
) -> AbilityScores:
    """Assign six retained First Method scores to six abilities.

    ``assignment`` names the destination for each value of ``kept_scores``,
    positionally, and must be a **permutation of all six abilities** —
    each exactly once. Every retained score is therefore used exactly once:
    none is duplicated, dropped, altered or rerolled.

    **No assignment is chosen here.** RC leaves the order to the player
    ("assign them to abilities in whatever order he chooses"), and this
    function applies the one it is given.

    Malformed shape — a wrong number of scores or destinations, a missing
    or duplicated ability — raises ``ValueError``, following the
    structural-validation convention of
    src/rules/exploration/turn_credit.py. A retained score outside 3-18
    raises :class:`AbilityScoreDomainError` from the value object, which
    is the correct error either way.
    """
    if len(kept_scores) != _ABILITY_COUNT:
        raise ValueError(
            f"exactly {_ABILITY_COUNT} retained scores are assigned, got "
            f"{len(kept_scores)}"
        )
    if len(assignment) != _ABILITY_COUNT or set(assignment) != set(Ability):
        raise ValueError(
            "the assignment must name each of the six abilities exactly "
            f"once, got {[ability.name for ability in assignment]}"
        )
    return _assembled(dict(zip(assignment, kept_scores, strict=True)))


def roll_point_allocation_total(rng: RNG) -> int:
    """Second Method, rolled form: the point total is ``60 + 5d6``.

    Consumes exactly one ``5d6`` expression — five d6 draws and one roll
    sequence number (approved case H3). The result therefore runs 65-90.

    **This function covers the rolled form only.** The equal-allotment
    form consumes no randomness and needs no function: the DM's chosen
    total is passed straight to :func:`allocate_points`, which cannot
    tell the two apart and does not need to.
    """
    return _POINT_ALLOCATION_BASE + rng.roll(_POINT_ALLOCATION_EXPRESSION).total


def allocate_points(
    total: int, allocation: Mapping[Ability, int]
) -> AbilityScores:
    """Second Method: distribute ``total`` points across the six abilities.

    ``total`` may come from :func:`roll_point_allocation_total` **or** from
    the DM's equal allotment. This function is agnostic about which, and
    has no mode, flag or optional ``rng`` parameter to express the
    difference.

    Validates, in order:

    1. ``total`` is an ``int`` and not a ``bool`` — ``bool`` is a subtype
       of ``int``, so static typing alone would let ``True`` through;
    2. ``60 <= total <= 90``, RC's allotment bound (approved case H5);
    3. ``allocation`` names exactly the six abilities, one score each;
    4. every allocated score lies within **3-18** — the standing range
       limitation, which RC restates for this method explicitly
       ("Of course, the range limitation of 3 to 18 for ability scores
       still applies"). Checked **before** any ``AbilityScores`` is
       constructed, so approved case H4 observes
       :class:`AbilityScoreDomainError` from this rules boundary and never
       the value object's own guard;
    5. the allocated scores sum to ``total``. Nothing is normalized,
       padded or discarded to make them.

    Steps 1-3 and 5 raise :class:`PointAllocationError`; step 4 raises
    :class:`AbilityScoreDomainError`, because the rejected value there is
    a score, not a total.
    """
    if not isinstance(total, int) or isinstance(total, bool):
        raise PointAllocationError(
            f"the point total must be an int and must not be a bool, got "
            f"{total!r}"
        )
    if not MINIMUM_ALLOTMENT <= total <= MAXIMUM_ALLOTMENT:
        raise PointAllocationError(
            f"RC bounds the point allocation at {MINIMUM_ALLOTMENT}-"
            f"{MAXIMUM_ALLOTMENT} points, got {total}"
        )
    if set(allocation) != set(Ability):
        raise PointAllocationError(
            "the allocation must name each of the six abilities exactly "
            f"once, got {sorted(str(key) for key in allocation)}"
        )
    for ability, score in allocation.items():
        if not _MINIMUM_SCORE <= score <= _MAXIMUM_SCORE:
            raise AbilityScoreDomainError(
                f"the range limitation of {_MINIMUM_SCORE} to "
                f"{_MAXIMUM_SCORE} for ability scores still applies; "
                f"{ability.name} was allocated {score}"
            )
    allocated = sum(allocation.values())
    if allocated != total:
        raise PointAllocationError(
            f"the allocation must distribute exactly {total} points, got "
            f"{allocated}"
        )
    return _assembled(allocation)
