"""CHAR-002 — Race & Class Eligibility.

See docs/rules/character_creation/race_and_class_eligibility.md (Status:
APPROVED, human-approved 2026-09-04) for the governing Rule Card, and
docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §7.5 for the approved
implementation contract this module implements (Slice B).

This module owns creation-time class eligibility and, as the single
CLUSTER-002 owner of both tables, the authoritative statement of each
class's **creation minimums** and **prime requisites**. CHAR-001 §4 will
consume both for the 2-for-1 trade (Slice D); they are defined here once
and nowhere else.

Its input is the six **eligibility scores** — CHAR-001 §1's as-rolled
scores, after any Chapter 13 switch the DM or simulation policy authorized,
and *before* the Chapter 1 trade (card §1, SR-3). This module cannot
observe which of those a caller supplies; supplying adjusted (post-trade)
scores is a calling-contract violation, not something it can detect.

Every requirement is a **raw-score threshold**. An ability score of 13 means
score 13, never adjustment +1 — which is why this card has, and must have,
no CHAR-007 dependency (card §4.1, Open Questions).

Being ineligible is a normal rules result, reported as an
:class:`Eligibility` value. It is not an exception.

It does not, and must not:

- perform the Chapter 13 score switch — that is CHAR-001 §6.2, and it runs
  *before* this card (card §4, §5);
- perform the Chapter 1 2-for-1 prime-requisite adjustment — CHAR-001 §4,
  which runs *after* this card and may neither establish nor destroy the
  eligibility decided here (card §4, §4.1);
- transition a cleric to a druid, or expose any part of that procedure.
  Its ownership is P1 — DEFER FOR HUMAN GOVERNANCE, no Rule ID assigned
  (card §B);
- implement any downstream Mystic mechanic — XP source, armour and
  protective-device prohibition, tithing, oath sanction or alignment
  tendency. The P2 pointers in INVENTORY.md record where those belong;
  they specify nothing and expand nothing here (card §C);
- apply an ability-score adjustment, or import CHAR-007 in any form. Every
  gate is a raw score;
- read the p. 12 Experience Bonuses and Penalties table, or any XP
  material (ADV-001);
- test a prime requisite against any threshold — prime requisites are
  eligibility-inert here and are exported, not consulted (card §3);
- choose a class for the player. It reports which classes are available;
  selection is the caller's;
- own class special abilities, thief skills, Hit Dice, saving throws,
  equipment permissions, spell access, level caps or alignment as a system
  (card §A);
- perform RNG, or import one.
"""

from __future__ import annotations

from collections.abc import Mapping
from enum import Enum, auto
from types import MappingProxyType

from rules.character_creation.ability import Ability, AbilityScores
from rules.character_creation.character_class import CharacterClass

__all__ = [
    "Eligibility",
    "creation_minimums",
    "eligibility",
    "eligible_classes",
    "prime_requisites",
]


class Eligibility(Enum):
    """Whether a class is available to a character at creation.

    A closed three-value result. The two ineligible values are **not**
    interchangeable: RC gates the demihuman and Mystic classes on ability
    thresholds a different score array could satisfy, while the Druid's
    requirement is not an ability threshold at all and no score array can
    ever satisfy it (card §2, approved case E18).
    """

    ELIGIBLE = auto()
    NOT_ELIGIBLE_ABILITY_REQUIREMENT = auto()
    NOT_ELIGIBLE_AT_CREATION = auto()


def _minimums(**requirements: int) -> Mapping[Ability, int]:
    """An immutable creation-minimum table for one class."""
    return MappingProxyType(
        {Ability[name.upper()]: score for name, score in requirements.items()}
    )


_CREATION_MINIMUMS: Mapping[CharacterClass, Mapping[Ability, int]] = MappingProxyType(
    {
        CharacterClass.CLERIC: _minimums(),
        CharacterClass.FIGHTER: _minimums(),
        CharacterClass.MAGIC_USER: _minimums(),
        CharacterClass.THIEF: _minimums(),
        CharacterClass.DWARF: _minimums(constitution=9),
        CharacterClass.ELF: _minimums(intelligence=9),
        CharacterClass.HALFLING: _minimums(dexterity=9, constitution=9),
        CharacterClass.MYSTIC: _minimums(wisdom=13, dexterity=13),
        CharacterClass.DRUID: _minimums(),
    }
)
"""The "Other Requirements" column of the Character Classes and Ability
Requirements Table (RC p. 7), as raw-score thresholds (card §2).

The four human classes are available "regardless of his ability scores" —
RC states it as a universal — so their tables are empty.

The **Druid's** table is empty too, and that emptiness means something
different: the Druid's requirement is Neutral alignment and 9th level as a
cleric, which is not an ability threshold at all. An empty table must never
be read as "eligible": :func:`eligibility` decides Druid before consulting
any minimum."""


_NOT_AVAILABLE_AT_CREATION: frozenset[CharacterClass] = frozenset(
    {CharacterClass.DRUID}
)
"""Classes no score array can ever reach at creation (card §2, §B).

RC: "you can't start a character off as a druid. A druid character must
start off as a cleric... and earn a lot of experience (up to 9th experience
level) as a cleric. Only at that point can he become a druid." Corroborated
by the p. 8 Hit Dice table's "Does not apply" and by the Druid Experience
Table beginning at level 9."""


_PRIME_REQUISITES: Mapping[CharacterClass, frozenset[Ability]] = MappingProxyType(
    {
        CharacterClass.CLERIC: frozenset({Ability.WISDOM}),
        CharacterClass.FIGHTER: frozenset({Ability.STRENGTH}),
        CharacterClass.MAGIC_USER: frozenset({Ability.INTELLIGENCE}),
        CharacterClass.THIEF: frozenset({Ability.DEXTERITY}),
        CharacterClass.DWARF: frozenset({Ability.STRENGTH}),
        CharacterClass.ELF: frozenset({Ability.STRENGTH, Ability.INTELLIGENCE}),
        CharacterClass.HALFLING: frozenset({Ability.STRENGTH, Ability.DEXTERITY}),
        CharacterClass.MYSTIC: frozenset({Ability.STRENGTH, Ability.DEXTERITY}),
        CharacterClass.DRUID: frozenset({Ability.WISDOM}),
    }
)
"""The "Prime Requisite(s)" column of the p. 7 table (card §2).

**Eligibility-inert.** No class is gated on a minimum prime-requisite
value, and this module never tests one against a threshold (card §3). The
table is carried here, and exported, because CHAR-001 §4 needs it as the
trade's raise-target and ADV-001 needs it for the XP modifier.

The distinction is load-bearing: the Dwarf's prime requisite is Strength
while its creation gate is Constitution 9, and the Mystic's are Strength
and Dexterity while its gates are Wisdom 13 and Dexterity 13 — so Wisdom
gates the Mystic without being one of its prime requisites."""


def eligibility(scores: AbilityScores, cls: CharacterClass) -> Eligibility:
    """Whether ``cls`` is available to a character with ``scores``.

    ``scores`` are eligibility scores (see the module docstring): after any
    authorized Chapter 13 switch, before the Chapter 1 trade. This function
    takes no stage, phase or provenance parameter, because the card gives
    it none to consult — the ordering is a calling contract (card §1, §4;
    approved case E21).

    Every threshold is compared against the raw score. No adjustment value
    is read, and no prime requisite is tested (card §3).
    """
    if cls in _NOT_AVAILABLE_AT_CREATION:
        return Eligibility.NOT_ELIGIBLE_AT_CREATION
    minimums = _CREATION_MINIMUMS[cls]
    if all(scores[ability] >= minimum for ability, minimum in minimums.items()):
        return Eligibility.ELIGIBLE
    return Eligibility.NOT_ELIGIBLE_ABILITY_REQUIREMENT


def eligible_classes(scores: AbilityScores) -> frozenset[CharacterClass]:
    """Every class available to a character with ``scores``.

    Derived from :func:`eligibility` rather than from a second copy of the
    thresholds, so there is exactly one implementation path.

    **Never empty**: RC makes the four human classes available whatever the
    scores, so every character has at least four legal classes (card §2,
    approved case E3). **Never contains the Druid** (approved case E19).
    """
    return frozenset(
        cls
        for cls in CharacterClass
        if eligibility(scores, cls) is Eligibility.ELIGIBLE
    )


def prime_requisites(cls: CharacterClass) -> frozenset[Ability]:
    """``cls``'s prime requisite ability or abilities (RC p. 7).

    Exported for CHAR-001 §4's trade target and ADV-001's XP modifier.
    **Not an eligibility gate** — this module never tests one (card §3).
    """
    return _PRIME_REQUISITES[cls]


def creation_minimums(cls: CharacterClass) -> Mapping[Ability, int]:
    """``cls``'s creation-time raw-score thresholds (RC p. 7).

    An immutable view; a caller cannot mutate this module's authoritative
    table. Empty for the four human classes, which RC makes available
    "regardless of his ability scores", and empty for the Druid, whose
    requirement is not an ability threshold at all — see
    :data:`_CREATION_MINIMUMS` and use :func:`eligibility` to decide
    availability.

    Exported for CHAR-001 §4 rule R10 (SR-5), which requires every
    creation minimum of the selected class to survive the trade.
    """
    return _CREATION_MINIMUMS[cls]
