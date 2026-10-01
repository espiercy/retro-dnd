"""EXP-006 — Light & Exploration Resources.

See docs/rules/exploration/light_and_exploration_resources.md (Status:
APPROVED, 2026-10-01) for the governing Rule Card, and
docs/technical/EXP-006_IMPLEMENTATION_PLAN.md (APPROVED, 2026-10-01) for
the implementation contract this module implements. This file currently
contains **Slice A only** — the light-source value/state model.

This module owns the *mundane* light-resource state this project's own
sources contribute: whether a source it owns is lit, that source's
radius, and its remaining duration. It owns nothing about the world.

It does not, and must not:

- state or derive global/environmental darkness, encounter Visibility,
  or blindness. Absence of a lit mundane source is an absence of *this
  card's* knowledge, never a fact about the world (Rule Card §6, §8;
  human adjudication 2026-10-01, Finding B);
- advance dungeon time or hold any counter, clock or elapsed-time
  accumulator — EXP-002 is the sole authority (Rule Card §4);
- restate equipment cost, encumbrance, price form or legality —
  CHAR-004 is authoritative (Rule Card §C);
- resolve a CHAR-012 skill check, roll any die, or consume RNG;
- handle magical light or darkness (MAGIC-*), infravision possession
  (CHAR-009), torch-as-weapon or oil-as-missile behaviour (COMBAT-*),
  rations, or starvation causation.

Slice A deliberately contains no depletion, no contribution
aggregation, no ignition, and no CHAR-004 catalog lookup: those are
Slices B, C and D of the approved plan and are not authorized yet.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from types import MappingProxyType
from typing import Final

__all__ = [
    "FRESH_DURATION_TURNS",
    "LANTERN_TURNS_PER_FLASK",
    "MUNDANE_LIGHT_RADIUS_FEET",
    "TORCH_TURNS",
    "LightSource",
    "LightSourceKind",
]


class LightSourceKind(Enum):
    """The mundane light sources EXP-006 owns.

    A **closed** two-value enumeration. RC's Chapter 4 descriptions give
    exactly these two mundane sources a radius and a duration (Rule Card
    §2, §3), and the card's §B excludes magical light entirely — so there
    is deliberately no ``MAGICAL`` member, no ``OTHER``, and no extension
    point (approved case L41).
    """

    TORCH = auto()
    LANTERN = auto()


MUNDANE_LIGHT_RADIUS_FEET: Final = 30
"""The radius, in feet, a lit mundane source illuminates.

**One constant serves both kinds.** RC gives the torch and the lantern an
identical ``30'`` radius and nowhere distinguishes their illumination
quality (Rule Card "Rules Cyclopedia Explicitly Establishes" item 10).
Two constants would permit them to drift; approved cases **L4** and **L5**
exist precisely to forbid a distinction the source does not state.
"""

TORCH_TURNS: Final = 6
"""Turns a fresh torch burns — RC's own turn-denominated figure.

RC p. 70 states *"burns for one hour (six turns)"*. The card takes the
**turn** form directly, in EXP-002's 10-minute turn; no hour-to-turn
conversion is performed anywhere in this module (Rule Card §3; approved
case **L16**).
"""

LANTERN_TURNS_PER_FLASK: Final = 24
"""Turns a lantern burns on one flask of oil.

RC p. 69 states *"burning one flask of oil in four hours (24 turns)"*.
As with the torch, the turn form is taken directly (Rule Card §3).
"""

FRESH_DURATION_TURNS: Final = MappingProxyType(
    {
        LightSourceKind.TORCH: TORCH_TURNS,
        LightSourceKind.LANTERN: LANTERN_TURNS_PER_FLASK,
    }
)
"""Each kind's duration when fresh, keyed by kind.

Read-only. Exposed so a caller never hardcodes ``6`` or ``24`` at a
construction site (approved cases **L6**, **L7**).
"""


@dataclass(frozen=True, slots=True)
class LightSource:
    """One mundane light source and its own state.

    Three fields, and no more: what kind it is, how many whole turns of
    fuel remain to it, and whether it is currently burning.

    **The exhausted-never-lit invariant.** A source with
    ``remaining_turns == 0`` can never be ``lit``; that combination is
    rejected at construction. The approved card's externally observable
    rule is that an exhausted source contributes no illumination (Rule
    Card §4, human adjudication Finding C), and refusing the state is
    the strongest available form of it — the forbidden state is not
    merely untested but *unconstructible*, including by callers this
    module cannot see (implementation plan §6.1).

    **An unlit source retains its duration.** ``lit`` and
    ``remaining_turns`` are independent: an unlit torch still knows it
    has six turns of wood left. Approved case **L11** requires exactly
    this, which is why a "a source is always lit" model was rejected
    (implementation plan §6.1).

    Structural violations raise the plain ``ValueError`` that value
    objects in this package raise — the convention
    src/rules/exploration/turn_credit.py and dungeon_movement.py
    establish. Slice A has no *domain* rejection and therefore
    introduces no exception type of its own (implementation plan §14,
    Slice A; human adjudication 2026-10-01).
    """

    kind: LightSourceKind
    remaining_turns: int
    lit: bool

    def __post_init__(self) -> None:
        if not isinstance(self.kind, LightSourceKind):
            raise ValueError(f"kind must be a LightSourceKind, got {self.kind!r}")
        if not isinstance(self.remaining_turns, int) or isinstance(self.remaining_turns, bool):
            # bool is a subtype of int, so static typing alone permits True
            # and it would otherwise read as 1 — excluded explicitly, as in
            # turn_credit.py and rng.py.
            raise ValueError(f"remaining_turns must be an int, got {self.remaining_turns!r}")
        if self.remaining_turns < 0:
            raise ValueError(f"remaining_turns must not be negative, got {self.remaining_turns!r}")
        if not isinstance(self.lit, bool):
            raise ValueError(f"lit must be a bool, got {self.lit!r}")
        if self.lit and self.remaining_turns == 0:
            raise ValueError(
                "an exhausted source is never lit: "
                f"lit={self.lit!r} with remaining_turns={self.remaining_turns!r}"
            )

    @classmethod
    def fresh(cls, kind: LightSourceKind, *, lit: bool = False) -> LightSource:
        """A source of ``kind`` with its full stated duration.

        The duration comes from :data:`FRESH_DURATION_TURNS`, so no caller
        restates ``6`` or ``24`` (approved cases **L6**, **L7**). Defaults
        to unlit: RC's durations describe how long a source *burns*, and
        a source that has not been lit has not begun burning.
        """
        if not isinstance(kind, LightSourceKind):
            raise ValueError(f"kind must be a LightSourceKind, got {kind!r}")
        return cls(kind=kind, remaining_turns=FRESH_DURATION_TURNS[kind], lit=lit)

    @property
    def illumination_radius_feet(self) -> int | None:
        """This source's own illumination radius, or ``None`` if it is not lit.

        ``None`` rather than ``0`` deliberately: ``0`` reads as "a radius
        of zero", which is a claim about illumination, while ``None``
        reads as "this source contributes no radius" — which is the
        truth (implementation plan §7.1). Approved cases **L1**, **L2**
        (lit, either kind, ``30``) and **L3** (unlit, nothing).

        The value does not depend on ``kind``: see
        :data:`MUNDANE_LIGHT_RADIUS_FEET`.
        """
        return MUNDANE_LIGHT_RADIUS_FEET if self.lit else None
