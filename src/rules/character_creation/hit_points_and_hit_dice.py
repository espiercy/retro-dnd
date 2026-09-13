"""CHAR-003 — Hit Points & Hit Dice.

See docs/rules/character_creation/hit_points_and_hit_dice.md (Status:
APPROVED, human-approved 2026-09-04) for the governing Rule Card, and
docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §7.6/§7.6.1 for the
approved implementation contract this module implements (Slice C).

This module owns one authoritative, level-aware operation:
:func:`hit_point_gain`. It decides for itself whether a level is a rolled
Hit Die level, a post-Name fixed-gain level, beyond the class maximum, or a
Druid rolled level with no die at all — none of those decisions is pushed
onto a caller.

THE ROLL-ONCE CALLING CONTRACT
------------------------------
A level's Hit Die is **rolled once**, and **no reroll or retry is
permitted** (card §3: "No reroll is permitted"). This operation is
stateless, so invoking it again for an already-resolved level is a
**caller-contract violation it cannot observe** — it has no level history
and, by design, no character or advancement state with which to acquire
one. Approved case H38 is that contract; it is verified by this module's
contract statement, by the executable tests proving one rolled level
consumes exactly one die with no internal retry, and by the Slice C
completion record's checklist, not by runtime state.

ADVANCEMENT BOUNDARY
--------------------
``_NAME_LEVEL`` and ``_MAXIMUM_LEVEL`` are a **private, card-local
projection** of values card §1 states are "`ADV-002`'s authoritative
property, consumed here because they bound how many fixed gains accrue."

    ADV-002 remains the future authoritative owner of general advancement
    limits. Future ADV-002 work must replace or reconcile this projection.

They exist solely so this card can bound its own hit-point behaviour, and
they establish nothing about advancement outside hit points. No
advancement-cap API is exported.

It does not, and must not:

- own damage, death, 0-hit-point consequences or healing (COMBAT-003,
  COMBAT-005, COMBAT-009);
- own saving throws or their progression (COMBAT-004), deliberately, even
  though they sit adjacent to Hit Dice in every Chapter 2 class entry;
- own experience points, level advancement, level caps or Attack Ranks
  (ADV-001, ADV-002) — and must not expose ``maximum_level()``,
  ``name_level()``, ``class_progression()`` or an advancement table, or
  define a ClassProgression, AdvancementRules or LevelTable type;
- implement the Chapter 19 extended demihuman/Mystic progression variant.
  It is NOT ENABLED for V1 (DEC-0008) and its per-level hit-point figures
  differ from these; they must never be confused (card §8; approved cases
  H41, H42);
- implement the cleric-to-druid transition, or any part of it. Ownership
  is P1 — DEFER FOR HUMAN GOVERNANCE, and no Rule ID is assigned;
- implement any downstream Mystic mechanic — Attack Ranks, combat or
  special abilities;
- define the Constitution adjustment. That magnitude is CHAR-007's, and
  obtaining it from there is the whole basis of this card's dependency
  (card §2);
- accumulate totals, advance several levels at once, or reroll. There is
  deliberately no ``total_hit_points``, ``gain_levels`` or
  ``advance_to_level`` operation: each invocation is exactly one level.
"""

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType

from rng import RNG
from rules.character_creation.ability_score_effects import adjustment
from rules.character_creation.character_class import CharacterClass
from rules.character_creation.errors import (
    HitDieNotApplicableError,
    HitPointLevelError,
)

__all__ = ["hit_point_gain"]


_HIT_DIE: Mapping[CharacterClass, int] = MappingProxyType(
    {
        CharacterClass.CLERIC: 6,
        CharacterClass.FIGHTER: 8,
        CharacterClass.MAGIC_USER: 4,
        CharacterClass.THIEF: 4,
        CharacterClass.DWARF: 8,
        CharacterClass.ELF: 6,
        CharacterClass.HALFLING: 6,
        CharacterClass.MYSTIC: 6,
    }
)
"""Hit Die by class (Character Class and Hit Dice Table, RC p. 8; card §1).

**The Druid has no entry, and that absence is the rule.** Card §1 records
its Hit Die as "does not apply" without qualification, so no Druid rolled
level has a defined die. No d6 is fabricated, the Cleric's die is not
borrowed under ``CharacterClass.DRUID``, and no ``None`` or sentinel is
returned — :func:`hit_point_gain` raises instead (approved case H39)."""


_NAME_LEVEL: Mapping[CharacterClass, int] = MappingProxyType(
    {
        CharacterClass.CLERIC: 9,
        CharacterClass.FIGHTER: 9,
        CharacterClass.MAGIC_USER: 9,
        CharacterClass.THIEF: 9,
        CharacterClass.DWARF: 9,
        CharacterClass.ELF: 9,
        CharacterClass.HALFLING: 8,
        CharacterClass.MYSTIC: 9,
        CharacterClass.DRUID: 9,
    }
)
"""Highest rolled-Hit-Die level per class (card §1). ADV-002 projection."""


_MAXIMUM_LEVEL: Mapping[CharacterClass, int] = MappingProxyType(
    {
        CharacterClass.CLERIC: 36,
        CharacterClass.FIGHTER: 36,
        CharacterClass.MAGIC_USER: 36,
        CharacterClass.THIEF: 36,
        CharacterClass.DWARF: 12,
        CharacterClass.ELF: 10,
        CharacterClass.HALFLING: 8,
        CharacterClass.MYSTIC: 16,
        CharacterClass.DRUID: 36,
    }
)
"""Class maximum level (card §1). ADV-002 projection.

The Elf's **10** and the Druid's **36** are human adjudications of
2026-08-29 and are not reopened. The Halfling's maximum equals its Name
level, so it has no post-Name band at all."""


_FIXED_GAIN: Mapping[CharacterClass, int] = MappingProxyType(
    {
        CharacterClass.CLERIC: 1,
        CharacterClass.FIGHTER: 2,
        CharacterClass.MAGIC_USER: 1,
        CharacterClass.THIEF: 2,
        CharacterClass.DWARF: 3,
        # Elf +2 at 10th is SIMULATOR RULING SR-1, not an RC-explicit value:
        # RC prints both +1 (p. 25 stat block, p. 130 Step 6) and +2 (p. 25
        # Class Details, p. 129), and the human project owner adjudicated.
        # Reversing SR-1 changes this entry AND the 14 other normative
        # locations card §4.1 "Reversal" enumerates -- H25 exists so a
        # partial change fails loudly rather than drifting silently.
        CharacterClass.ELF: 2,
        CharacterClass.MYSTIC: 2,
        CharacterClass.DRUID: 1,
    }
)
"""Fixed hit points per level above Name level (card §4).

**Constitution never applies to any value in this table** (card §4, §5).

**The Halfling has no entry**, because it has no post-Name band: its
maximum level equals its Name level, so the fixed branch is unreachable for
it and a level past 8 is a level-range rejection instead (approved cases
H13, H14)."""


def _rolled_gain(rng: RNG, cls: CharacterClass, constitution: int) -> int:
    """One rolled Hit Die, adjusted, with the per-roll 1-hit-point floor.

    The floor applies **per roll**, never to a running total (card §3;
    approved cases H9-H11). Exactly one die is drawn, and a low result is
    never rerolled.
    """
    if cls not in _HIT_DIE:
        raise HitDieNotApplicableError(
            f"{cls.name} has no Hit Die for rolled levels; RC records it as "
            f"'does not apply'. A character who will become a druid rolls "
            f"levels 1 to Name level as a CLERIC."
        )
    roll = rng.roll_die(_HIT_DIE[cls])
    return max(1, roll.total + adjustment(constitution))


def hit_point_gain(
    rng: RNG, cls: CharacterClass, level: int, constitution: int
) -> int:
    """Hit points gained by ``cls`` on entering ``level``.

    ``level`` is the level being gained or entered, and this operation
    decides which rule governs it:

    ``level < 1``, or above the class maximum
        :class:`HitPointLevelError`. Nothing accrues past the maximum
        (approved cases H14, H20, H24).

    Druid at a rolled level
        :class:`HitDieNotApplicableError` — no Druid Hit Die exists
        (approved case H39).

    ``1 <= level <= Name level``
        ``max(1, one Hit Die + Constitution adjustment)``. The adjustment
        is obtained from CHAR-007 on **every** application, never cached
        or reimplemented, so a changed Constitution governs the next roll
        (card §3).

    above Name level, up to the class maximum
        The approved fixed gain: **no die is drawn and Constitution is not
        consulted at all** (card §4, §5; approved cases H12, H16, H17).

    ``constitution`` is the character's **current** score, passed as a
    scalar because hit points accrue across later levels, not only at
    creation. Its accepted domain is CHAR-007's (2-18), not the narrower
    creation range; a score outside it raises CHAR-007's own
    ``AbilityScoreDomainError``, which is allowed to propagate unchanged.

    There is no adjustment-injection parameter, so a caller cannot supply
    an arbitrary Constitution adjustment — this card cannot produce an
    authoritative value without CHAR-007 (approved case H36).

    One invocation is one level. See the module docstring's roll-once
    calling contract (approved case H38).
    """
    if level < 1 or level > _MAXIMUM_LEVEL[cls]:
        raise HitPointLevelError(
            f"{cls.name} has no level {level}; levels run 1 to "
            f"{_MAXIMUM_LEVEL[cls]}. No hit points accrue beyond the class "
            f"maximum."
        )
    if level <= _NAME_LEVEL[cls]:
        return _rolled_gain(rng, cls, constitution)
    return _FIXED_GAIN[cls]
