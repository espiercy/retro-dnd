"""EXP-006 — Light & Exploration Resources.

See docs/rules/exploration/light_and_exploration_resources.md (Status:
APPROVED, 2026-10-01) for the governing Rule Card, and
docs/technical/EXP-006_IMPLEMENTATION_PLAN.md (APPROVED, 2026-10-01) for
the implementation contract this module implements. This file currently
contains **Slice A only** — the light-source value/state model.

This module owns the *mundane* light-resource state this project's own
sources contribute: whether a source it owns is lit, that source's
radius, its remaining duration, how that duration is spent against
authoritative elapsed turns, and what those sources together
contribute. It owns nothing about the world.

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

Slices A and B are implemented. Ignition (Slice C) and CHAR-004 catalog
lookup (Slice D) are not authorized yet and are deliberately absent.
"""

from __future__ import annotations

from collections.abc import Iterable
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
    "MundaneLightContribution",
    "deplete",
    "mundane_light_contribution",
    "refuel_lantern",
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


def _require_elapsed_turns(elapsed_turns: int) -> int:
    """Validate the caller-supplied elapsed-turn count's numeric domain.

    EXP-006 owns the **numeric domain** of this value and deliberately
    **not its provenance** (human adjudication 2026-10-01 §3). The count
    represents authoritative elapsed turns produced by EXP-002 and handed
    over by the caller; this module imports no time machinery, holds no
    counter, and has no way to prove where an integer came from. Which
    future orchestrator guarantees that origin is a frontier concern and
    is not solved here.

    No fake provenance wrapper is introduced: a type that cannot actually
    prove origin would assert a guarantee this module does not have.
    """
    if not isinstance(elapsed_turns, int) or isinstance(elapsed_turns, bool):
        raise ValueError(f"elapsed_turns must be an int, got {elapsed_turns!r}")
    if elapsed_turns < 0:
        raise ValueError(f"elapsed_turns must not be negative, got {elapsed_turns!r}")
    return elapsed_turns


def deplete(sources: Iterable[LightSource], elapsed_turns: int) -> tuple[LightSource, ...]:
    """Spend ``elapsed_turns`` against each lit source, source by source.

    For a **lit** source (Rule Card §4)::

        new_remaining = max(0, remaining_turns - elapsed_turns)

    and if that reaches zero the source becomes unlit and **contributes no
    illumination** — the Necessary Mechanical Consequence of RC's finite
    stated durations (approved cases **L8**, **L9**, **L10**).

    For an **unlit** source, elapsed turns change nothing: an unlit torch
    is not burning, so it spends no fuel (approved case **L11**).

    ``elapsed_turns == 0`` is valid and changes no state.

    **The consequence is strictly source-local.** One source reaching zero
    says nothing about any other source, about the party, or about the
    world: no party darkness, no world darkness, no ``NO_LIGHT``, no
    blindness, no encounter ``Visibility``, no burn-out event and no
    partial-turn proration is synthesized here (Rule Card §4, §6, §8;
    approved cases **L15**, **L15a**, **L15b**). :func:`deplete` returns
    sources and nothing else, which is what makes that guarantee
    structural rather than merely documented.

    Returns a new tuple; inputs are never mutated, consistent with the
    frozen value semantics Slice A established.
    """
    spent = _require_elapsed_turns(elapsed_turns)
    depleted: list[LightSource] = []
    for source in sources:
        if not isinstance(source, LightSource):
            raise ValueError(f"sources must contain LightSource values, got {source!r}")
        if not source.lit:
            depleted.append(source)
            continue
        remaining = max(0, source.remaining_turns - spent)
        depleted.append(
            LightSource(kind=source.kind, remaining_turns=remaining, lit=remaining > 0)
        )
    return tuple(depleted)


def refuel_lantern(source: LightSource) -> LightSource:
    """Supply a fresh flask of oil to an **expended** lantern.

    Rule Card §4: *"A lantern reaching zero consumes its flask; a further
    flask may be supplied, which resets ``remaining_turns`` to 24."*

    **Refuelling restores fuel. It does not ignite** (human adjudication
    2026-10-01). The approved card establishes that a further flask
    restores the lantern's fuel duration; it establishes **no** automatic
    ignition or relighting. Fuel availability and ignition state are
    independent, and ignition belongs to the later ignition slice::

        expended lantern + new flask  ->  remaining_turns = 24
                                      ->  lit = False

    A refuelled lantern therefore contributes **no** illumination until
    some separately authorized ignition operation changes its ``lit``
    state. No tinderbox or ``Fire-Building`` behaviour is invoked or
    implemented here.

    On approved case **L12**: the card's own wording for that case reads
    *"contributes illumination again"*, and that wording is **not
    rewritten here**. It is read, under the approved separation above, as
    *able* to contribute again once lit — the lantern has fuel once more,
    which is the condition the card's §4 sentence actually establishes.
    Nothing in the card states that supplying a flask lights it.

    The card states this operation for a lantern that has **reached
    zero**, and this function honours that stated precondition rather
    than extending it. Two requests are refused:

    - a **torch**, which has no fuel. RC gives the flask to the lantern;
      a fresh torch is a new source, not a refuelled one;
    - a lantern that is **not yet expended**. The card does not state
      what supplying a flask to a partly-full lantern does, and no
      arithmetic is assigned to that unsupported operation — no topping
      up to 24, no adding 24, no partial-flask arithmetic. This is an
      **API precondition derived from the approved scope**, not a new
      rules mechanic (human adjudication 2026-10-01).
    """
    if not isinstance(source, LightSource):
        raise ValueError(f"source must be a LightSource, got {source!r}")
    if source.kind is not LightSourceKind.LANTERN:
        raise ValueError(f"only a lantern burns a flask of oil, got {source.kind!r}")
    if source.remaining_turns != 0:
        raise ValueError(
            "the approved card states refuelling only for a lantern that has reached zero; "
            f"got remaining_turns={source.remaining_turns!r}"
        )
    return LightSource(
        kind=LightSourceKind.LANTERN,
        remaining_turns=LANTERN_TURNS_PER_FLASK,
        lit=False,
    )


@dataclass(frozen=True, slots=True)
class MundaneLightContribution:
    """What EXP-006's **own** sources contribute. **Not** a statement about
    the world.

    Every name here carries ``mundane`` or ``source``, deliberately: a
    consumer cannot write ``if not contribution.any_mundane_source_lit``
    and mean *"it is dark"* without the identifier itself contradicting
    them. The type is **not** called ``LightState``, ``Illumination``,
    ``Visibility`` or ``WorldLight`` — each of which would invite exactly
    the misreading the Rule Card's Finding B withdrew (Rule Card §6, §7;
    implementation plan §7.1).

    **An exhausted source cannot appear here**, and that is enforced by
    two independent barriers rather than by trusting callers:

    1. ``lit_sources`` may contain only **lit** sources, checked below;
    2. Slice A's own invariant makes ``lit=True`` with
       ``remaining_turns == 0`` **unconstructible**, so a lit source is
       necessarily a non-exhausted one.

    The two derived figures are **computed properties, not stored
    fields**, so they cannot disagree with ``lit_sources`` — there is no
    state to get out of step.
    """

    lit_sources: tuple[LightSource, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.lit_sources, tuple):
            raise ValueError(f"lit_sources must be a tuple, got {self.lit_sources!r}")
        for source in self.lit_sources:
            if not isinstance(source, LightSource):
                raise ValueError(f"lit_sources must contain LightSource values, got {source!r}")
            if not source.lit:
                raise ValueError(f"lit_sources must contain only lit sources, got {source!r}")

    @property
    def any_mundane_source_lit(self) -> bool:
        """Whether **this card's own** sources include a lit one.

        ``False`` means only that EXP-006 knows of no active mundane
        source it owns. It does **not** mean complete darkness,
        ``NO_LIGHT``, any ``Visibility`` category, blindness, or that the
        party or location is dark (Rule Card §6, human adjudication
        Finding B).
        """
        return bool(self.lit_sources)

    @property
    def max_mundane_radius_feet(self) -> int | None:
        """The largest radius this card's own lit sources contribute.

        ``None`` — **not** ``0`` — when nothing is lit. ``0`` reads as "a
        radius of zero", which is a claim about illumination; ``None``
        reads as "this card contributes no radius", which is the truth
        (implementation plan §7.1).

        Both approved kinds share one radius, so no brightness or quality
        distinction is representable (approved cases **L4**, **L5**).
        """
        return MUNDANE_LIGHT_RADIUS_FEET if self.lit_sources else None


def mundane_light_contribution(sources: Iterable[LightSource]) -> MundaneLightContribution:
    """What ``sources`` together contribute, mundane sources only.

    **The filtering is done here, not by the caller.** Unlit sources — and
    therefore, by Slice A's invariant, every exhausted source — are
    excluded. A caller cannot accidentally include a spent torch by
    forgetting to filter, because filtering is not the caller's job and
    the result type would reject it anyway (approved cases **L27**,
    **L28**, **L15a**).

    Takes no surprise state and no encounter circumstance: querying this
    card's own light state requires neither (approved case **L34**).
    """
    return MundaneLightContribution(
        lit_sources=tuple(
            source
            for source in sources
            if isinstance(source, LightSource) and source.lit
        )
    )
