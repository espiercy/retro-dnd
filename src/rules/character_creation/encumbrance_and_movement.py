"""CHAR-005 — Encumbrance & Movement Rate.

See docs/rules/character_creation/encumbrance_and_movement_rate.md (Status:
APPROVED, human-approved 2026-09-24, amended 2026-09-25) for the governing
Rule Card, and docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md §6.3 and §10
(Slice D) for the approved implementation contract this module implements.

**This card is the authoritative owner of the numerical character movement
rate** — normal, encounter and running — and :func:`movement_rate` is its
single entry point. There is deliberately no second way to obtain a rate.

THE ONE DERIVATION
------------------
``movement_rate`` validates its inputs, chooses a **normal speed** by one of
exactly two paths, and derives every rate from it by one shared rule:

    1. validate level        (§1.1, amended — int, not bool, 1..maximum)
    2. validate encumbrance  (int, not bool, >= 0)
    3. Mystic AND enc <= 400  ->  the MV table          (SR-9)
    4. otherwise              ->  the standard band table (§3)
    5. normal -> encounter, running                      (§4, §6.1)

**Steps 3-5 are why there is no separate Mystic subsystem.** The gate
chooses a normal speed and one derivation follows, so `SR-9`, §6.1 and Q4 are
all satisfied by the same three lines. :class:`MovementRate` stores only the
normal speed and derives the other two, which makes an internally
inconsistent rate unrepresentable rather than merely untested.

EXACT RATIONALS, NEVER FLOATS
-----------------------------
Encounter speed is ``normal / 3``, and for a Mystic that is frequently not a
whole number of feet: ``MV 130'`` gives ``43 1/3'`` exactly. The card is
categorical — *"Do NOT round up. Do NOT round down. Do NOT round to nearest
whole foot"* — so every rate is a :class:`fractions.Fraction`. **No float is
used, produced or accepted.** Any later snapping to map or grid units is a
separate spatial concern the card explicitly does not own (§6, case M74).

NOT IMPLEMENTED — §7 CONDITION MODIFIERS, ``NOT V1-WIRED``
----------------------------------------------------------
Blindness, stunning, prone and starvation movement effects are specified by
card §7 and carry `SR-10`, but **every causation owner is Unresearched**, so
no landed or approved card can produce any of those conditions. The
implementation plan §8 dispositions them ``NOT V1-WIRED``, the established
treatment for an approved mechanic whose trigger is unreachable (precedent:
``CHAR-003 W3``).

``movement_rate()`` therefore takes **no condition parameter**, and no
``Condition`` enum, modifier pipeline or hook exists. `SR-10` remains
approved and recorded on the card. Nothing about simultaneous-condition
composition, ordering between modifiers, or ordering against the `SR-9` gate
is invented here; when a causation card lands it will arrive with its own
composition question answered by whoever owns it.

This module does not, and must not, carry:

- item ``Enc`` values, catalogs or legality — CHAR-004's, in equipment.py.
  Only :data:`SUIT_ARMOR_ENCUMBRANCE_CN` crosses, and it is re-exported from
  that catalog rather than restated;
- spending a rate against the dungeon turn — EXP-003's;
- turn or round time accounting — landed EXP-002's;
- causation of any condition — their owning cards';
- resolution of an attack or of damage. :class:`ExhaustionPenalty` **records**
  §9's combat consequences because they follow from a movement choice, and
  applies none of them: that is COMBAT-002/003's;
- a racial-armour penalty, swimming, monster or vehicle encumbrance, terrain,
  or spatial quantisation (§11, cases M72-M76).
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from enum import Enum
from fractions import Fraction
from types import MappingProxyType
from typing import Final

from rules.character_creation.character_class import CharacterClass
from rules.character_creation.equipment import ARMOR as _ARMOR
from rules.character_creation.errors import (
    MovementLevelError,
    MovementNotPermittedError,
)

__all__ = [
    "ENCOUNTER_SPEED_DIVISOR",
    "IMMOBILE_NORMAL_SPEED",
    "MAXIMUM_RUNNING_ROUNDS",
    "MYSTIC_MAXIMUM_LEVEL",
    "MYSTIC_MV",
    "MYSTIC_UNENCUMBERED_MAXIMUM_CN",
    "REQUIRED_REST_TURNS",
    "SUIT_ARMOR_ENCUMBRANCE_CN",
    "ExhaustionPenalty",
    "MovementMode",
    "MovementRate",
    "Setting",
    "combat_movement",
    "is_rested",
    "may_attack_in_the_same_round",
    "movement_rate",
    "party_movement_rate",
    "run_for",
]


def _require_int(value: object, name: str) -> int:
    """Reject a non-``int``, and a ``bool`` masquerading as one.

    ``bool`` is a subtype of ``int``, so mypy strict permits ``True`` where
    an ``int`` is expected and it would read as ``1``. Excluded explicitly,
    following src/rng/rng.py, turn_credit.py and hit_points_and_hit_dice.py
    (implementation plan §12, §14.2).
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"{name} must be an int and must not be a bool, got {value!r}")
    return value


ENCOUNTER_SPEED_DIVISOR: Final = 3
"""Encounter speed is **one third** of normal speed (card §4).

Applied as an exact rational divisor, never as ``0.333...``. Running speed is
the normal *number* per round, which is the same thing as ``3 x`` encounter
speed — the Q4 reading of RC Ch. 8's *"(3 x normal movement)"*, and the
reason cases M16 and M20 both hold without a second rule.
"""


@dataclass(frozen=True, slots=True, order=True)
class MovementRate:
    """A character's three movement rates, all derived from one number.

    **Only the normal speed is stored.** Encounter and running speed are
    derived, so the three can never disagree: case M17 (*"encounter x 3
    equals running, at every band"*) holds by construction rather than by
    test, and no caller can build a rate whose parts contradict each other.

    ``normal`` is feet per **turn**; ``encounter`` and ``running`` are feet
    per **round**. The units differ, and the difference is load-bearing —
    RC Ch. 8 p. 103 forbids normal speed inside the combat sequence
    entirely (see :func:`combat_movement`).

    Ordering is by normal speed, which supplies the comparison §8's
    slowest-member rule needs. It is well defined for every rate this module
    produces, because encounter and running are monotonic in normal.
    """

    normal: Fraction

    def __post_init__(self) -> None:
        if isinstance(self.normal, bool):
            raise ValueError(f"normal must not be a bool, got {self.normal!r}")
        if not isinstance(self.normal, Fraction):
            raise ValueError(
                f"normal must be a Fraction — rates stay exact rationals and a "
                f"float or an int would invite one to be lost — got {self.normal!r}"
            )
        if self.normal < 0:
            raise ValueError(f"normal must not be negative, got {self.normal!r}")

    @property
    def encounter(self) -> Fraction:
        """Encounter speed — one third of normal, feet per **round**, exact.

        Retains fractional thirds: a Mystic at ``MV 130'`` moves ``43 1/3'``
        per round, and that is the authoritative value (cases M42, M47).
        """
        return self.normal / ENCOUNTER_SPEED_DIVISOR

    @property
    def running(self) -> Fraction:
        """Running speed — the normal *number*, feet per **round** (Q4, §6.1).

        Not three times the per-turn number. RC Ch. 8's *"(3 x normal
        movement)"* multiplies the per-round rate, so ``120'`` per turn runs
        at ``120'`` per round, never ``360'`` (case M16). The same
        derivation applies unchanged to an active Mystic ``MV``, which is
        why §6.1 needs no separate Mystic running formula (case M48).
        """
        return self.normal

    @property
    def is_immobile(self) -> bool:
        """Whether this rate permits no movement at all — the ``2,401+`` band."""
        return self.normal == 0


_ENCUMBRANCE_BANDS: Final[tuple[tuple[int, int], ...]] = (
    (400, 120),
    (800, 90),
    (1200, 60),
    (1600, 30),
    (2400, 15),
)
"""RC's Character Movement Rates and Encumbrance Table (Ch. 6 p. 88, §3).

Each entry is ``(inclusive upper bound in cn, normal speed in feet per
turn)``. The unbounded ``2,401+`` band is :data:`IMMOBILE_NORMAL_SPEED`,
held apart because it is the only row with no upper bound and would
otherwise need a sentinel.

Encounter and running speed are **not** stored, because they are derived —
and the printed table agrees at every row, which is exactly why one
derivation is safe:

        0-400 -> 120 (40) 120   |   1,201-1,600 ->  30 (10)  30
      401-800 ->  90 (30)  90   |   1,601-2,400 ->  15  (5)  15
    801-1,200 ->  60 (20)  60   |   2,401+      ->   0  (0)   0
"""

IMMOBILE_NORMAL_SPEED: Final = 0
"""The ``2,401+`` band: no movement at all (approved cases M11, M12)."""

SUIT_ARMOR_ENCUMBRANCE_CN: Final[int] = _ARMOR["Suit Armor"].encumbrance_cn
"""Suit Armor's encumbrance: ``750 cn``, and nothing else (**`SR-8`**).

Re-exported from CHAR-004's catalog rather than restated, so there is one
value and it cannot drift. `SR-8` declines the item's own printed
*"movement rate is 30' (10')"* — despite its genuine BECMI ancestry, and
despite BECMI's own precedence rule selecting it — because that precedence
rule does not govern a single-volume compilation, because no source says how
``30' (10')`` composes with other carried weight, and because preserving it
would require inventing a generic equipment-overrides-encumbrance mechanic.

So a character carrying Suit Armor alone totals ``750 cn`` and moves
``90' (30')`` by the ordinary table (case M25), and additional gear keeps
reducing that through the ordinary system (cases M26, M27). **No Suit Armor
symbol exists in this module beyond this integer** (cases M28-M30).
"""

MYSTIC_MV: Final[Mapping[int, int]] = MappingProxyType(
    {
        1: 120,
        2: 130,
        3: 140,
        4: 150,
        5: 160,
        6: 170,
        7: 180,
        8: 190,
        9: 200,
        10: 210,
        11: 220,
        12: 240,
        13: 260,
        14: 280,
        15: 300,
        16: 320,
    }
)
"""The Mystic's level-dependent ``MV``, feet per turn (RC Ch. 2 p. 31, §6).

A **table, not a formula**: the progression steps by 10 feet to 11th level
and by 20 thereafter, so no arithmetic rule reproduces it.

The values are printed inside RC's Chapter 2 class entry, and that
provenance is preserved — but **source location and canonical ownership are
distinct** (card §B). The authoritative numerical rule is this card's;
CHAR-009 may reference Mystic movement and must not re-specify it.
"""

MYSTIC_MAXIMUM_LEVEL: Final = 16
"""The Mystic's maximum level, which bounds the accepted level input.

A **private, card-local projection** of a property that remains `ADV-002`'s,
consumed here only to bound this card's own table — exactly as landed
``hit_points_and_hit_dice.py`` projects the per-class maxima to bound
hit-point accrual, and recorded the same way (card §1.1; plan §6.6).

    ADV-002 remains the future authoritative owner of advancement limits.
    Future ADV-002 work must replace or reconcile this projection.

No advancement API is exported, and nothing here establishes anything about
advancement outside movement.
"""

MYSTIC_UNENCUMBERED_MAXIMUM_CN: Final = 400
"""The `SR-9` gate: enhanced Mystic ``MV`` applies only at or below ``400 cn``.

    total encumbrance <= 400  ->  the MV table      (§6)
    total encumbrance >  400  ->  the standard band (§3)

**A threshold, not a curve and not an exemption.** `SR-9` considered and
rejected both proportional scaling of ``MV`` under encumbrance and Mystic
immunity to encumbrance; a Mystic at ``401 cn`` moves ``90' (30')`` like
anyone else (case M34), and at ``2,401 cn`` is immobile (case M36).

It is the same ``400`` as the first band's upper bound, and deliberately so:
the gate is *"while total encumbrance would leave an ordinary character at
120'"*. It is stated separately rather than read out of the band table,
because it is a ruling about the Mystic and not a property of the table.
"""


def _validate_level(cls: CharacterClass, level: int) -> int:
    """Card §1.1 — level is an explicit, validated, per-class-bounded input."""
    if not isinstance(level, int) or isinstance(level, bool):
        raise MovementLevelError(
            f"level must be an int and must not be a bool, got {level!r}"
        )
    if level < 1:
        raise MovementLevelError(f"level must be at least 1, got {level!r}")
    if cls is CharacterClass.MYSTIC and level > MYSTIC_MAXIMUM_LEVEL:
        raise MovementLevelError(
            f"level must be at most {MYSTIC_MAXIMUM_LEVEL} for a mystic, whose "
            f"MV table CHAR-005 §6 indexes, got {level!r}"
        )
    return level


def _band_normal_speed(total_encumbrance_cn: int) -> int:
    """Card §3 — the normal speed for a total encumbrance, in feet per turn."""
    for upper_bound, normal in _ENCUMBRANCE_BANDS:
        if total_encumbrance_cn <= upper_bound:
            return normal
    return IMMOBILE_NORMAL_SPEED


def movement_rate(
    cls: CharacterClass,
    level: int,
    total_encumbrance_cn: int,
) -> MovementRate:
    """The authoritative movement rate for a character — the single entry point.

    ``total_encumbrance_cn`` is the sum of the ``Enc (cn)`` of everything
    carried, as CHAR-004 supplies it (§2). This card consumes a total and
    computes no item value: worn clothing already contributes ``0``, a filled
    container already contributes container plus contents, and Suit Armor
    already contributes ``750`` and nothing else.

    ``level`` is an explicit caller input, validated here (§1.1, amended
    2026-09-25). It creates **no dependency on CHAR-002 for level and none
    on unresearched ADV-* rules to obtain it**. For every class but the
    Mystic it changes no result, because no other class indexes a
    level-dependent table in this card.

    **Takes no condition parameter and no setting parameter.** Card §7's
    condition modifiers are ``NOT V1-WIRED`` (see the module docstring), and
    §10's indoor/outdoor distinction changes the *unit* rather than the
    number (see :class:`Setting`).
    """
    if not isinstance(cls, CharacterClass):
        raise ValueError(f"cls must be a CharacterClass, got {cls!r}")
    _validate_level(cls, level)
    if _require_int(total_encumbrance_cn, "total_encumbrance_cn") < 0:
        raise ValueError(
            f"total_encumbrance_cn must not be negative, got {total_encumbrance_cn!r}"
        )

    if (
        cls is CharacterClass.MYSTIC
        and total_encumbrance_cn <= MYSTIC_UNENCUMBERED_MAXIMUM_CN
    ):
        return MovementRate(Fraction(MYSTIC_MV[level]))
    return MovementRate(Fraction(_band_normal_speed(total_encumbrance_cn)))


def party_movement_rate(rates: Iterable[MovementRate]) -> MovementRate:
    """The rate of a party that intends to stay together — its **slowest** member.

    Card §8, from RC p. 88: *"Groups of characters, if they intend to stay
    together, move at the rate of the slowest character."* An immobile member
    makes the party immobile (case M61).

    **Calling this is the intent.** A party not intending to stay together
    has no group rate — each member uses their own (case M62) — so there is
    no ``intending`` flag to pass and no way to ask this function for a rate
    that ignores the slowest member.
    """
    slowest: MovementRate | None = None
    for rate in rates:
        if not isinstance(rate, MovementRate):
            raise ValueError(f"every party member's rate must be a MovementRate, got {rate!r}")
        if slowest is None or rate < slowest:
            slowest = rate
    if slowest is None:
        raise ValueError("a party must have at least one member to have a rate")
    return slowest


class MovementMode(Enum):
    """Which of the three rates a character is moving at (card §4, §5).

    The distinction is not cosmetic: :attr:`NORMAL` is feet per **turn** and
    is forbidden inside the combat sequence, while the other two are feet per
    **round** and differ in whether an attack may follow.
    """

    NORMAL = 1
    ENCOUNTER = 2
    RUNNING = 3


def combat_movement(
    rate: MovementRate,
    mode: MovementMode,
    *,
    already_engaged: bool = False,
) -> Fraction:
    """How far a character moves in one combat round, in feet.

    Card §5, from RC Ch. 8 p. 103:

    - **normal speed is refused outright.** *"A character's normal speed is
      never used during the combat sequence"* — it is a per-turn rate, and
      the combat sequence runs in rounds (case M21);
    - **encounter speed** may be moved in full, and an attack may still
      follow in the same round (case M22);
    - **running speed** may be moved only by a character not already engaged
      (case M24), and no attack may follow (case M23).

    Free actions such as drawing a weapon do not subtract from the movement
    score. The DM may deduct movement for more complicated manoeuvres, and
    standing up after a fall costs an action — neither is quantified by RC,
    and neither is invented here.
    """
    if not isinstance(rate, MovementRate):
        raise ValueError(f"rate must be a MovementRate, got {rate!r}")
    if not isinstance(mode, MovementMode):
        raise ValueError(f"mode must be a MovementMode, got {mode!r}")
    if not isinstance(already_engaged, bool):
        raise ValueError(f"already_engaged must be a bool, got {already_engaged!r}")
    if mode is MovementMode.NORMAL:
        raise MovementNotPermittedError(
            "normal speed is never used during the combat sequence (RC Ch. 8 "
            "p. 103): it is a rate per turn, not per round"
        )
    if mode is MovementMode.RUNNING:
        if already_engaged:
            raise MovementNotPermittedError(
                "a character already engaged in combat may not run (CHAR-005 §5)"
            )
        return rate.running
    return rate.encounter


def may_attack_in_the_same_round(mode: MovementMode) -> bool:
    """Whether an attack may follow this round's movement (card §5).

    Encounter speed may be moved in full and still permit an attack; running
    may not (cases M22, M23). Normal speed is refused, for the same reason
    :func:`combat_movement` refuses it.
    """
    if not isinstance(mode, MovementMode):
        raise ValueError(f"mode must be a MovementMode, got {mode!r}")
    if mode is MovementMode.NORMAL:
        raise MovementNotPermittedError(
            "normal speed is never used during the combat sequence (RC Ch. 8 p. 103)"
        )
    return mode is MovementMode.ENCOUNTER


MAXIMUM_RUNNING_ROUNDS: Final = 30
"""Running may be sustained at most 30 rounds — five minutes (card §9)."""

REQUIRED_REST_TURNS: Final = 3
"""An exhausted character must rest at least 3 turns — 30 minutes (card §9).

The optional **Endurance** general skill extends the running limit. It is
`CHAR-012`'s, **specifies nothing here**, and the base 30-round limit is
complete without it.
"""


@dataclass(frozen=True, slots=True)
class ExhaustionPenalty:
    """What §9 says befalls an exhausted character — **recorded, not applied**.

    An exhausted character forced to fight without resting suffers these;
    one forced to keep running drops to encounter speed and cannot move
    faster until rested (case M69).

    **This object resolves nothing.** Applying an attack bonus, subtracting
    from a damage roll or enforcing the minimum is COMBAT-002/003's, and
    card §A says so explicitly: this card records them only because they are
    the consequence of a movement choice. There is deliberately no
    ``damage_after_exhaustion()`` here, and no attack roll.
    """

    monster_attack_bonus: int = 2
    damage_penalty: int = 2
    minimum_damage: int = 1


def run_for(rounds: int) -> bool:
    """Run for ``rounds`` rounds; returns whether the character is now exhausted.

    Card §9: the limit is **30 rounds**, and reaching it exhausts the
    character (case M63). Asking to run longer is refused rather than
    silently truncated at 30, because a caller that asked for 31 rounds of
    movement would otherwise be told it got them (case M64).
    """
    if _require_int(rounds, "rounds") < 0:
        raise ValueError(f"rounds must not be negative, got {rounds!r}")
    if rounds > MAXIMUM_RUNNING_ROUNDS:
        raise MovementNotPermittedError(
            f"running may be sustained at most {MAXIMUM_RUNNING_ROUNDS} rounds "
            f"(CHAR-005 §9), and {rounds} were requested"
        )
    return rounds == MAXIMUM_RUNNING_ROUNDS


def is_rested(turns_rested: int) -> bool:
    """Whether ``turns_rested`` turns of rest clear exhaustion (card §9).

    At least 3 turns, so 2 do not (cases M65, M66).
    """
    if _require_int(turns_rested, "turns_rested") < 0:
        raise ValueError(f"turns_rested must not be negative, got {turns_rested!r}")
    return turns_rested >= REQUIRED_REST_TURNS


class Setting(Enum):
    """Where movement is being measured, and therefore in which unit (card §10).

    RC's numbers do not change between the two; only the unit they are read
    in does — *"indoors the table's numbers are FEET; outdoors the same
    numbers are read as YARDS"* (cases M70, M71). Each member's value is the
    unit's name, because that is the entire content of the rule.

    This is why :func:`movement_rate` takes no setting: a rate of 90 is a
    rate of 90 either way.
    """

    INDOORS = "feet"
    OUTDOORS = "yards"

    @property
    def unit(self) -> str:
        """The unit the table's numbers are read in for this setting."""
        return self.value
