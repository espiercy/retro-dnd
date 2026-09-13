"""Error types for the CLUSTER-002 character-creation domain.

Mirrors src/rng/errors.py's DiceError hierarchy: one domain base plus
specific subclasses, raised eagerly and never silently coerced, clamped, or
defaulted. See docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §9.1 for
the approved error surface.

This module was populated slice by slice, as each approved rejection path
became executable: Slice A added the base and the ability-score domain
error, Slice C the two CHAR-003 hit-point errors, Slice D the four CHAR-001
trade and switch errors, and Slice E the Chapter 10 point-allocation error.
**The hierarchy is now complete for CLUSTER-002** — Slice F adds no
production code and therefore no error type.
"""

from __future__ import annotations


class CharacterCreationError(Exception):
    """Base class for every CLUSTER-002 character-creation rules rejection.

    Distinct from the plain ``ValueError`` that value objects raise for
    structural violations (a non-int, or a bool masquerading as one) —
    that convention follows src/rules/exploration/turn_credit.py and is
    preserved. This hierarchy is for *domain* and *rules* rejections
    (implementation plan §9.1, "Type versus domain validation").
    """


class AbilityScoreDomainError(CharacterCreationError):
    """An ability score outside a declared domain.

    Two different domains are declared in CLUSTER-002, and this error
    serves both (implementation plan §6.4):

    - ``AbilityScores`` holds creation-produced scores, ``3..18``;
    - ``CHAR-007``'s scalar lookups accept their own, wider or narrower,
      table domains — ``2..18`` for the shared adjustment table, ``3..18``
      for the Intelligence and Charisma supplementary tables.

    The raised message always names which lookup and which domain was
    violated. RC specifies nothing outside these ranges and no value may
    be extrapolated (CHAR-007 §1; approved case A15).
    """


class HitPointLevelError(CharacterCreationError):
    """A hit-point gain was requested for a level that is not a valid level.

    Covers both the structural and the domain case, because the invalid
    value is supplied for the same parameter either way:

    - **structural** — ``level`` is not an ``int``, or is a ``bool``.
      ``bool`` is a subtype of ``int``, so static typing alone permits it
      and ``True`` would otherwise read as level 1; it is excluded
      explicitly, following src/rng/rng.py and turn_credit.py;
    - **domain** — below 1, or above the class maximum CHAR-003 §1
      records. RC stops the standard progression at that maximum, and no
      hit points accrue past it from any source this card owns (approved
      cases H14, H20, H24).

    No separate error class exists for the structural case: one parameter,
    one error.

    The request is rejected rather than clamped or answered with zero:
    silently returning 0 would make an out-of-range level indistinguishable
    from a legitimate zero-gain level, and CHAR-003 has none.
    """


class HitDieNotApplicableError(CharacterCreationError):
    """A rolled hit-point gain was requested for a class with no Hit Die.

    CHAR-003 §1 records the Druid's Hit Die as "does not apply — enters at
    9th as a cleric", without qualification, so **no** Druid rolled level
    has a defined die (approved case H39). A character who will become a
    druid rolls levels 1 through Name level **as a cleric**; that is what
    approved case H40 describes, and the caller requests those levels with
    ``CharacterClass.CLERIC``.

    Distinct from :class:`HitPointLevelError`, and the distinction is not
    cosmetic: Druid level 1 is *inside* the Druid's 1-36 level range, so
    reporting a level-range violation for it would assert something false.
    """


class IllegalTradeError(CharacterCreationError):
    """A CHAR-001 2-for-1 prime-requisite trade violates an ordinary rule.

    Covers the trade rules whose violations no approved case needs to
    distinguish **by type**: R1 (the target must be a prime requisite of
    the chosen class), R3 (Constitution and Charisma may not be
    exchanged), R4 (Dexterity may not be lowered), R5 (only the target is
    raised) and R6/R7 (the donor's floor of 9).

    **Every message names the violated rule**, so a test discriminates
    with ``pytest.raises(IllegalTradeError, match="R3")`` — the idiom
    src/rules/exploration already uses — without one exception type per
    case.

    R10 and R11 deliberately do **not** live here: see
    :class:`ClassMinimumViolationError` and
    :class:`PrimeRequisiteCeilingError`.
    """


class ClassMinimumViolationError(CharacterCreationError):
    """A trade would leave the selected class's creation minimum unmet.

    Rule **R10**, from Simulator Ruling **SR-5**. Kept distinct from
    :class:`IllegalTradeError` because approved case V2 turns on exactly
    that distinction: *"R6's floor of 9 would have permitted it; R10 is
    what forbids it."* A shared type would let a wrong-rule rejection pass
    that test.

    R10 **preserves** eligibility already established by CHAR-002; it
    never lets a trade *establish* it (CHAR-001 §4, CHAR-002 §4.1).
    """


class PrimeRequisiteCeilingError(CharacterCreationError):
    """A trade would raise its target ability above 18.

    Rule **R11**, a Necessary Mechanical Consequence of RC's standing
    range limitation for ability scores (RC p. 6; p. 130 "the range
    limitation of 3 to 18 for ability scores still applies"). **Not
    RC-explicit at p. 7**, which states no target bound, and **not a
    Simulator Ruling** — see CHAR-001 §4.

    Kept distinct because approved case C2 turns on it: *"R1, R6 and R7
    all permit this trade; R11 is the only rule that forbids it."* It is
    also why the rule must be evaluated **before** any result
    ``AbilityScores`` is constructed — the value object's own 3-18 guard
    is defence in depth and must never be what C2 or C4 observes.
    """


class IllegalSwitchError(CharacterCreationError):
    """An authorized Chapter 13 highest-score switch is not performable.

    Rule-card §6.2 and §6.2.1. Three causes, distinguished by message:
    the named source does not hold the maximum score; the named
    destination is not a prime requisite of the requested class; or
    source and destination are the same ability, which is not the
    "swap of two scores" §6.2 specifies.

    Separate from the trade errors: a different operation, a different
    moment in the sequence, and different causes. Nothing here decides
    **whether** a switch is authorized — that is the DM's or the
    simulation policy's, and this error is only reached once a caller has
    decided to perform one.
    """


class PointAllocationError(CharacterCreationError):
    """A Chapter 10 point-allocation total or allocation shape is invalid.

    CHAR-001 §5's Second Method. Four causes, distinguished by message:

    - the **total** is not an ``int``, or is a ``bool``. ``bool`` is a
      subtype of ``int``, so static typing alone permits ``True`` and it
      would otherwise read as 1;
    - the total lies outside RC's ``60..90`` allotment bound (approved
      case H5);
    - the **allocation** does not name exactly the six abilities, one
      score each;
    - the allocated scores do not sum to the total. No approved case
      names this; it is implementation-contract validation, because the
      operation cannot faithfully allocate a total it is not given.

    **This error is never used for an individual ability score outside
    3-18.** That is the standing range limitation and raises
    :class:`AbilityScoreDomainError` — the rejected value there is a
    score, not a total (approved case H4).
    """
