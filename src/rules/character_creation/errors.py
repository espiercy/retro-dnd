"""Error types for the CLUSTER-002 character-creation domain.

Mirrors src/rng/errors.py's DiceError hierarchy: one domain base plus
specific subclasses, raised eagerly and never silently coerced, clamped, or
defaulted. See docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §9.1 for
the approved error surface.

This module currently defines only the errors Slice A's approved rejection
paths actually require. The plan identifies further subclasses for Slices
B-E (illegal trade, class-minimum violation, prime-requisite ceiling,
illegal switch, hit-point level, hit die not applicable); those are
deliberately **not** pre-stubbed here. Each later slice extends this module
when its own approved rejection paths become executable.
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
