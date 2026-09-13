"""Error types for the CLUSTER-002 character-creation domain.

Mirrors src/rng/errors.py's DiceError hierarchy: one domain base plus
specific subclasses, raised eagerly and never silently coerced, clamped, or
defaulted. See docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §9.1 for
the approved error surface.

This module defines only the errors whose approved rejection paths are
already executable. Slice A added the base and the ability-score domain
error; Slice C adds the two CHAR-003 hit-point errors. The plan identifies
five further subclasses for Slices D-E (illegal trade, class-minimum
violation, prime-requisite ceiling, illegal switch, point allocation);
those are deliberately **not** pre-stubbed. Each later slice extends this
module when its own approved rejection paths become executable.
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
