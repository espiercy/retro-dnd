"""Shared character-creation primitives: the six abilities and a creation-score set.

This contract is owned by no single Rule Card — it is the shared vocabulary
of docs/rules/character_creation/ability_score_generation.md (CHAR-001),
race_and_class_eligibility.md (CHAR-002), hit_points_and_hit_dice.md
(CHAR-003) and ability_score_effects.md (CHAR-007), all Status: APPROVED.
See docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §6.1/§6.3/§6.4 and
§7.1 for the approved representation this module implements (Slice A).

It follows the domain-local shared-value precedent established by
src/rules/exploration/turn_credit.py: a small module owned by neither
consuming card individually.

It does not, and must not:

- carry class data of any kind — prime requisites, creation minimums, Hit
  Dice, Name levels, maximum levels, fixed hit-point gains and XP
  modifiers all belong to CHAR-002, CHAR-003, ADV-001 and ADV-002
  (implementation plan §6.2);
- carry ability-score *effects* — the adjustment table and the
  Intelligence/Charisma supplementary tables are CHAR-007's, in
  ability_score_effects.py (implementation plan §7.4);
- decide eligibility, generation, trades, switches or hit points;
- perform RNG, or import one — Slice A consumes no randomness at all
  (implementation plan §8);
- serve as a general "live character" score representation. AbilityScores
  is the CLUSTER-002 *creation-score set* and enforces the creation
  domain 3-18 (implementation plan §6.4, Approach A). CHAR-007's scalar
  adjustment lookup independently accepts 2-18, and that wider domain
  lives on that lookup, not here.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from enum import Enum
from typing import Final

from rules.character_creation.errors import AbilityScoreDomainError


class Ability(Enum):
    """The six abilities, in the Rules Cyclopedia's own declaration order.

    RC p. 6 lists them as Strength, Intelligence, Wisdom, Dexterity,
    Constitution, Charisma, and that order is mechanically load-bearing:
    CHAR-001 §1 generates scores "in the order listed" and its approved
    case G4 asserts assignment follows roll order rather than sorted
    order. Explicit ordinals are used rather than ``enum.auto()`` so the
    order is a stated fact of this module and can never become an
    accident of declaration or of alphabetical sorting.
    """

    STRENGTH = 1
    INTELLIGENCE = 2
    WISDOM = 3
    DEXTERITY = 4
    CONSTITUTION = 5
    CHARISMA = 6


_INDEX: Final[Mapping[Ability, int]] = {
    ability: index for index, ability in enumerate(Ability)
}
"""Position of each ability within a score set, in RC declaration order."""

MINIMUM_CREATION_SCORE: Final = 3
"""Lowest score RC's creation procedures can produce (3d6 all ones, RC p. 6)."""

MAXIMUM_CREATION_SCORE: Final = 18
"""RC's standing range limitation for ability scores (RC p. 6; p. 130
"the range limitation of 3 to 18 for ability scores still applies").
CHAR-001 §4 rule R11 applies the same bound to the prime-requisite trade."""


@dataclass(frozen=True, slots=True)
class AbilityScores:
    """One character's six creation ability scores, as an immutable value.

    Holds exactly six named scores, one per :class:`Ability`, each an
    integer in ``3..18`` — RC's standing range limitation for ability
    scores, which CHAR-001 §1 produces and rule R11 preserves through the
    prime-requisite trade.

    Structural violations (a non-int, or a bool masquerading as one)
    raise ``ValueError``, following
    src/rules/exploration/turn_credit.py. Domain violations (a score
    outside 3-18) raise :class:`AbilityScoreDomainError`
    (implementation plan §9.1).
    """

    strength: int
    intelligence: int
    wisdom: int
    dexterity: int
    constitution: int
    charisma: int

    def __post_init__(self) -> None:
        for ability, score in zip(Ability, self._as_tuple(), strict=True):
            if not isinstance(score, int) or isinstance(score, bool):
                raise ValueError(
                    f"{ability.name} score must be an int, got {score!r}"
                )
            if not MINIMUM_CREATION_SCORE <= score <= MAXIMUM_CREATION_SCORE:
                raise AbilityScoreDomainError(
                    f"{ability.name} score must be within "
                    f"{MINIMUM_CREATION_SCORE}-{MAXIMUM_CREATION_SCORE} "
                    f"(RC's creation range), got {score!r}"
                )

    def _as_tuple(self) -> tuple[int, int, int, int, int, int]:
        """The six scores in RC declaration order."""
        return (
            self.strength,
            self.intelligence,
            self.wisdom,
            self.dexterity,
            self.constitution,
            self.charisma,
        )

    def __getitem__(self, ability: Ability) -> int:
        """The score recorded for ``ability``."""
        return self._as_tuple()[_INDEX[ability]]

    def maximum(self) -> int:
        """The highest of the six scores.

        Consumed by CHAR-001 §6.2's Chapter 13 switch, which authorizes
        moving *the highest rolled score* into a prime requisite. This
        method reports the value only; it selects no source ability and
        breaks no tie (CHAR-001 §6.2.1).
        """
        return max(self._as_tuple())

    def replace(self, changes: Mapping[Ability, int]) -> AbilityScores:
        """A new score set with ``changes`` applied; this one is unchanged.

        The result is validated exactly as any other construction is, so
        a replacement that would leave a score outside 3-18 raises
        :class:`AbilityScoreDomainError`.
        """
        values = list(self._as_tuple())
        for ability, score in changes.items():
            values[_INDEX[ability]] = score
        return AbilityScores(
            values[0], values[1], values[2], values[3], values[4], values[5]
        )
