"""CHAR-007 — General Ability Score Mechanical Effects.

See docs/rules/character_creation/ability_score_effects.md (Status:
APPROVED, human-approved 2026-09-04) for the governing Rule Card, and
docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §7.4 for the approved
implementation contract this module implements (Slice A).

This module owns ability-score **values** and nothing else: the one shared
score-to-adjustment table (RC p. 9), the Intelligence and Languages table
(RC p. 10), the Charisma Adjustment table (RC p. 10), and the per-ability
statement of which effect each adjustment applies to (RC p. 10).

The governing principle of the card, quoted: "CHAR-007 may own an
adjustment value without owning the procedure that consumes it." That
partition is enforced structurally here — this module returns only numbers
and small frozen value objects, and it imports no consumer. COMBAT-002,
COMBAT-003, COMBAT-004, COMBAT-006, CHAR-003, CHAR-006, CHAR-008,
CHAR-012, ENC-003 and EXP-005 will import *from* this module; it will
never import *them*.

It does not, and must not:

- resolve combat, attack rolls or damage rolls (COMBAT-002, COMBAT-003);
- resolve saving throws, or know their five categories (COMBAT-004), and
  must not implement the Chapter 19 optional extended save mapping, which
  is COMBAT-004's solely (card §4.3);
- implement the Open Doors procedure — the 1d6 roll, the 5-6 target, the
  natural-6 override, the once-per-round limit or the surprise
  forfeiture. CHAR-007 owns the Strength adjustment *value*; the
  procedure belongs to EXP-005, with a dependency on ENC-002 (card §4.1);
- resolve NPC reactions (ENC-003) or retainer behaviour (CHAR-006) — the
  Charisma table's three columns are values exported to them (card §3.2);
- apply any adjustment to initiative. RC p. 102's Dexterity initiative
  modifier is an *optional* individual-initiative rule, declined for V1
  by DEC-0008; owner COMBAT-006 (card §4.2);
- implement the Chapter 13 generic Ability Check. It is a different
  mechanic entirely — 1d20 against the *raw* score, with this table
  playing no part — and is confirmed outside this card's scope. Whether
  it receives its own Rule ID is deferred for human governance as
  Stage-B proposal P3; no Rule ID is assigned or invented here
  (card §4.4);
- select, name or teach languages, or model alignment tongues (CHAR-008),
  and must not implement the optional General Skills system (CHAR-012);
- perform RNG, or import one. This module consumes no randomness
  (implementation plan §8).
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from enum import Enum, auto
from typing import Final

from rules.character_creation.ability import Ability
from rules.character_creation.errors import AbilityScoreDomainError

__all__ = [
    "CONDITIONAL_EFFECTS",
    "AbilityEffect",
    "CharismaEffects",
    "LanguageCapability",
    "Literacy",
    "adjusted_effects",
    "adjustment",
    "charisma_effects",
    "language_capability",
]


ADJUSTMENT_MINIMUM_SCORE: Final = 2
"""The shared table's lowest band starts at 2, not 3 (RC p. 9).

The card is explicit about why: "the band starts at 2, not 3, even though
3d6 generation cannot produce a 2 — the table accommodates scores reduced
below the generated range by other effects." This is deliberately *wider*
than AbilityScores' creation domain of 3-18, and the difference is real
(implementation plan §6.4, Approach A)."""

ADJUSTMENT_MAXIMUM_SCORE: Final = 18
"""RC's standing range limitation for ability scores (RC p. 6, p. 130)."""

SUPPLEMENTARY_MINIMUM_SCORE: Final = 3
"""The Intelligence and Charisma supplementary tables begin at 3, not 2.

The card records this difference explicitly and instructs that it be
"faithfully reproduced" (card §1). It is RC's, not an implementation
choice."""

SUPPLEMENTARY_MAXIMUM_SCORE: Final = 18
"""Upper bound of both supplementary tables (RC p. 10)."""


class AbilityEffect(Enum):
    """What an ability's adjustment applies to (Abilities and Adjustments
    Table, RC p. 10; card §2).

    A **closed** set: it is exactly RC's core-rules effect list for V1.
    Its closure is mechanically load-bearing, and approved cases depend on
    it — there is deliberately no member for a saving throw other than
    versus spells (case A38), none for initiative (case A44), none for the
    Chapter 13 ability check (case A47), and none for hit-point gains
    above Name level, to which Constitution expressly does not apply
    (case A40).
    """

    MELEE_ATTACK_ROLLS = auto()
    MELEE_AND_THROWN_DAMAGE_ROLLS = auto()
    OPENING_DOORS = auto()
    LANGUAGES = auto()
    GENERAL_SKILLS = auto()
    SAVING_THROWS_VS_SPELLS = auto()
    MISSILE_AND_THROWN_ATTACK_ROLLS = auto()
    ARMOR_CLASS = auto()
    HIT_POINTS_PER_EXPERIENCE_LEVEL = auto()
    NPC_REACTIONS = auto()
    RETAINERS = auto()


CONDITIONAL_EFFECTS: Final[frozenset[AbilityEffect]] = frozenset(
    {AbilityEffect.GENERAL_SKILLS}
)
"""Effects conditional on an optional system being in use (card §2).

RC's per-ability table annotates Intelligence's general-skills effect as an
optional system; every other effect in the table is unconditional. CHAR-007
records which effects are conditional; it does not decide whether the
optional system is enabled — that is CHAR-012's and the project profile's
(DEC-0008). Approved case A41 turns on this distinction."""


class Literacy(Enum):
    """Reading and writing ability by Intelligence band (RC p. 10, card §3.1).

    A closed four-value set, reproducing RC's own bands. The band text is
    represented as an identity, not as prose to be displayed: presentation
    is not this module's concern.
    """

    TROUBLE_SPEAKING_CANNOT_READ_OR_WRITE = auto()
    CANNOT_READ_OR_WRITE_COMMON = auto()
    WRITES_SIMPLE_COMMON_WORDS = auto()
    READS_AND_WRITES_NATIVE_LANGUAGES = auto()


@dataclass(frozen=True, slots=True)
class LanguageCapability:
    """One Intelligence band's language values (RC p. 10, card §3.1).

    ``additional_languages`` counts languages *beyond* the native ones RC
    describes as "usually two" (the Common tongue and an alignment
    tongue). Which specific languages are available, and their selection,
    belong to CHAR-008 — this card supplies counts only.
    """

    literacy: Literacy
    additional_languages: int


@dataclass(frozen=True, slots=True)
class CharismaEffects:
    """One Charisma band's three values (Charisma Adjustment Table, RC p. 10).

    RC's table carries three distinct columns, and the card is explicit
    that Charisma "carries three distinct outputs, not one".

    ``reaction_adjustment`` is supplied as a value only. RC constrains its
    use sharply: it applies only while the character is talking to the
    creature, and it "never adjust[s] any rolls *you* make; they only
    affect rolls made by the Dungeon Master." A player-side application is
    a rules violation. This module neither applies the adjustment nor
    decides when it applies — ENC-003 owns reaction resolution.

    ``maximum_retainers`` and ``retainer_morale`` are carried here because
    they are columns of CHAR-007's own table, and are exported to
    CHAR-006, which owns what they do.
    """

    reaction_adjustment: int
    maximum_retainers: int
    retainer_morale: int


_ADJUSTMENT: Final[Mapping[int, int]] = {
    score: value
    for low, high, value in (
        (2, 3, -3),
        (4, 5, -2),
        (6, 8, -1),
        (9, 12, 0),
        (13, 15, 1),
        (16, 17, 2),
        (18, 18, 3),
    )
    for score in range(low, high + 1)
}
"""Bonuses and Penalties for Ability Scores Table (RC p. 9), verbatim.

Applies identically to all six abilities; there is no per-class or
per-race variation (card §1, approved case A14)."""


_LANGUAGE: Final[Mapping[int, LanguageCapability]] = {
    score: capability
    for low, high, capability in (
        (3, 3, LanguageCapability(Literacy.TROUBLE_SPEAKING_CANNOT_READ_OR_WRITE, 0)),
        (4, 5, LanguageCapability(Literacy.CANNOT_READ_OR_WRITE_COMMON, 0)),
        (6, 8, LanguageCapability(Literacy.WRITES_SIMPLE_COMMON_WORDS, 0)),
        (9, 12, LanguageCapability(Literacy.READS_AND_WRITES_NATIVE_LANGUAGES, 0)),
        (13, 15, LanguageCapability(Literacy.READS_AND_WRITES_NATIVE_LANGUAGES, 1)),
        (16, 17, LanguageCapability(Literacy.READS_AND_WRITES_NATIVE_LANGUAGES, 2)),
        (18, 18, LanguageCapability(Literacy.READS_AND_WRITES_NATIVE_LANGUAGES, 3)),
    )
    for score in range(low, high + 1)
}
"""Intelligence and Languages Table (RC p. 10), verbatim (card §3.1)."""


_CHARISMA: Final[Mapping[int, CharismaEffects]] = {
    score: effects
    for low, high, effects in (
        (3, 3, CharismaEffects(-3, 1, 4)),
        (4, 5, CharismaEffects(-2, 2, 5)),
        (6, 8, CharismaEffects(-1, 3, 6)),
        (9, 12, CharismaEffects(0, 4, 7)),
        (13, 15, CharismaEffects(1, 5, 8)),
        (16, 17, CharismaEffects(2, 6, 9)),
        (18, 18, CharismaEffects(3, 7, 10)),
    )
    for score in range(low, high + 1)
}
"""Charisma Adjustment Table (RC p. 10), verbatim (card §3.2)."""


_ADJUSTED_EFFECTS: Final[Mapping[Ability, frozenset[AbilityEffect]]] = {
    Ability.STRENGTH: frozenset(
        {
            AbilityEffect.MELEE_ATTACK_ROLLS,
            AbilityEffect.MELEE_AND_THROWN_DAMAGE_ROLLS,
            AbilityEffect.OPENING_DOORS,
        }
    ),
    Ability.INTELLIGENCE: frozenset(
        {AbilityEffect.LANGUAGES, AbilityEffect.GENERAL_SKILLS}
    ),
    Ability.WISDOM: frozenset({AbilityEffect.SAVING_THROWS_VS_SPELLS}),
    Ability.DEXTERITY: frozenset(
        {AbilityEffect.MISSILE_AND_THROWN_ATTACK_ROLLS, AbilityEffect.ARMOR_CLASS}
    ),
    Ability.CONSTITUTION: frozenset(
        {AbilityEffect.HIT_POINTS_PER_EXPERIENCE_LEVEL}
    ),
    Ability.CHARISMA: frozenset(
        {AbilityEffect.NPC_REACTIONS, AbilityEffect.RETAINERS}
    ),
}
"""Abilities and Adjustments Table (RC p. 10), verbatim (card §2).

Strength covers melee *and thrown* damage but only melee attack rolls;
thrown and missile *attack* rolls are Dexterity's (approved cases A33-A36).
Wisdom is the only ability with a core saving-throw effect, and it is
narrow: RC frames it as "a bonus to one of his saving throws", versus
spells (card §2, §4.3; approved cases A37, A38, A45)."""


def adjustment(score: int) -> int:
    """The shared ability-score adjustment for ``score`` (RC p. 9).

    One table, applied identically to all six abilities — this function
    deliberately takes no ability parameter, because there is no
    per-ability, per-class or per-race variation to express (card §1;
    approved case A14).

    Accepts ``2..18``. RC specifies nothing outside that range and no
    value may be extrapolated; a score of 1 or 19 is a rejected input, not
    a ruling about what the game does to such a score (approved case A15).
    """
    if score not in _ADJUSTMENT:
        raise AbilityScoreDomainError(
            f"the shared adjustment table is defined for scores "
            f"{ADJUSTMENT_MINIMUM_SCORE}-{ADJUSTMENT_MAXIMUM_SCORE}; got "
            f"{score!r}. RC specifies no value outside that range and none "
            f"may be extrapolated."
        )
    return _ADJUSTMENT[score]


def language_capability(intelligence: int) -> LanguageCapability:
    """Literacy and additional-language count for ``intelligence`` (RC p. 10).

    Accepts ``3..18``. RC's supplementary table begins at 3, one higher
    than the shared adjustment table's 2, and that difference is RC's own
    (card §1).

    The result is **not** derived from :func:`adjustment`: the two tables
    are independent and diverge — at Intelligence 3 the adjustment is
    ``-3`` while the additional-language count is ``0`` (approved cases
    A16, A24).
    """
    if intelligence not in _LANGUAGE:
        raise AbilityScoreDomainError(
            f"the Intelligence and Languages table is defined for scores "
            f"{SUPPLEMENTARY_MINIMUM_SCORE}-{SUPPLEMENTARY_MAXIMUM_SCORE}; "
            f"got {intelligence!r}. RC specifies no value outside that "
            f"range and none may be extrapolated."
        )
    return _LANGUAGE[intelligence]


def charisma_effects(charisma: int) -> CharismaEffects:
    """Reaction adjustment, maximum retainers and retainer morale (RC p. 10).

    Accepts ``3..18``, matching RC's own supplementary table (card §1).

    Values only. This function takes no situational context — no "is the
    character talking to the creature" input and no roll to modify —
    because CHAR-007 neither applies the reaction adjustment nor decides
    when it applies. RC restricts it to DM-made rolls, and only while the
    character is talking to the creature; ENC-003 owns that procedure and
    CHAR-006 owns retainer behaviour (card §3.2; approved cases A31, A32,
    A48).
    """
    if charisma not in _CHARISMA:
        raise AbilityScoreDomainError(
            f"the Charisma Adjustment table is defined for scores "
            f"{SUPPLEMENTARY_MINIMUM_SCORE}-{SUPPLEMENTARY_MAXIMUM_SCORE}; "
            f"got {charisma!r}. RC specifies no value outside that range "
            f"and none may be extrapolated."
        )
    return _CHARISMA[charisma]


def adjusted_effects(ability: Ability) -> frozenset[AbilityEffect]:
    """What ``ability``'s adjustment applies to (RC p. 10, card §2).

    Reports the assignment only. Every named effect's *procedure* belongs
    to another card — see this module's docstring for the full partition.
    """
    return _ADJUSTED_EFFECTS[ability]
