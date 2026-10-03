"""EXP-006 — Light & Exploration Resources.

See docs/rules/exploration/light_and_exploration_resources.md (Status:
APPROVED, 2026-10-01) for the governing Rule Card, and
docs/technical/EXP-006_IMPLEMENTATION_PLAN.md (APPROVED, 2026-10-01) for
the implementation contract this module implements.

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

The card's responsibilities are implemented in full: the light-source
value model, depletion against authoritative elapsed turns, the mundane
light contribution, the ignition branch selector (carrying ``SR-11``),
and the CHAR-004 identity binding (private — see ``__all__``).

Public surface: four constants, five types and four functions, all listed
in ``__all__``. That list is the contract; guards in the test module pin
the module namespace, the effective class surfaces and every public
signature against it.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from enum import Enum, auto
from types import MappingProxyType
from typing import Final

from rules.character_creation.equipment import TORCH as _TORCH_ITEM
from rules.character_creation.equipment import Item, catalog_item
from rules.exploration.errors import (
    IgnitionAttemptLimitError,
    IgnitionNotDefinedError,
    LanternRefuelNotDefinedError,
)

__all__ = [
    "FRESH_DURATION_TURNS",
    "LANTERN_TURNS_PER_FLASK",
    "MUNDANE_LIGHT_RADIUS_FEET",
    "TORCH_TURNS",
    "IgnitionConditions",
    "IgnitionOutcome",
    "LightSource",
    "LightSourceKind",
    "MundaneLightContribution",
    "deplete",
    "ignition_outcome",
    "mundane_light_contribution",
    "refuel_lantern",
]
# The three `CHAR-004` identity accessors are deliberately NOT exported.
# Human adjudication 2026-10-03, on review-#2 finding `MED-2`: no approved
# mechanic consumes them, and the implementation plan §9 requires only that
# the binding exist and restate nothing — it never requires a public
# accessor. Exporting them put `Item`-returning functions, and therefore
# `.price` and `.encumbrance_cn` by reference, in `EXP-006`'s public API,
# which is what made approved case `L42` ("any price, `Coin` or encumbrance
# value **emitted**") unprovable. Private, the binding still demonstrably
# restates no catalog data, and no public callable of this card returns a
# catalog row at all.


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

    Constructing a source is a **structural** operation, so every
    violation here raises the plain ``ValueError`` that value objects in
    this package raise — the convention
    src/rules/exploration/turn_credit.py and dungeon_movement.py
    establish. The card defines no procedure this constructor could be
    asked for and fail to supply, so none of this module's three domain
    rejections (rules.exploration.errors) arises from it.
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

    Rule Card §4: *"A lantern reaching zero consumes its flask, and a
    further flask may be supplied, which restores ``remaining_turns`` to
    ``24`` and leaves the lantern unlit."*

    **Refuelling restores fuel. It does not ignite.** That is the card's
    own words, not a reading of them: §4 states the unlit outcome
    literally, and case `L12` states it again. Fuel availability and
    ignition state are independent, and ignition is §5's::

        expended lantern + new flask  ->  remaining_turns = 24
                                      ->  lit = False

    A refuelled lantern therefore contributes **no** illumination until
    some separately authorized ignition operation changes its ``lit``
    state. No tinderbox or ``Fire-Building`` behaviour is invoked or
    implemented here.

    Approved case **L12** specifies the same outcome directly: ``24``
    remaining, ``lit = False``, no illumination contribution until
    separately ignited. An earlier draft of that case said a refuelled
    lantern *contributes illumination again*; the card **withdrew** that
    wording on 2026-10-01 as asserting an ignition it never establishes.
    Nothing in the card states that supplying a flask lights it.

    The card states this operation for a lantern that has **reached
    zero**. Two requests are refused, and they are refused in **different
    categories** — the distinction is the point (human adjudication
    2026-10-03):

    - a **non-lantern** source raises ``ValueError``. This is a lantern
      operation, so any other source kind is simply an **invalid
      argument** to it, handled by the package's structural convention.
      It is emphatically **not** a claim that RC fails to define how to
      refuel a torch: the operation does not apply to that source kind,
      and there is no silence to report;
    - a **valid lantern that is not yet expended** raises
      :class:`~rules.exploration.errors.LanternRefuelNotDefinedError`.
      A partly-fuelled lantern is a legitimate lantern state, and here
      the source genuinely **is** silent: RC establishes replacing the
      flask after exhaustion and establishes no top-up to 24, no adding
      24, and no partial-flask arithmetic. That is a rules-domain
      source-silence rejection, and no arithmetic is invented for it.
    """
    # Structural: not a LightSource at all.
    if not isinstance(source, LightSource):
        raise ValueError(f"source must be a LightSource, got {source!r}")
    # Structural: a LightSource, but not the kind this operation applies to.
    if source.kind is not LightSourceKind.LANTERN:
        raise ValueError(
            f"refuel_lantern is a lantern operation, got {source.kind.name}: "
            "only a lantern burns a flask of oil, and a fresh torch is a new "
            "source rather than a refuelled one"
        )
    # Rules-domain: a valid lantern state, but RC states no procedure for it.
    if source.remaining_turns != 0:
        raise LanternRefuelNotDefinedError(
            "the approved card states refuelling only for a lantern that has reached zero; "
            f"got remaining_turns={source.remaining_turns!r}. No partial-flask arithmetic "
            "is assigned to this request"
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


_CATALOG_NAMES: Final = MappingProxyType(
    {
        "LANTERN": "Lantern",
        "OIL_FLASK": "Oil",
        "TINDERBOX": "Tinder box",
    }
)
"""**The one place** canonical `CHAR-004` catalog names appear in this card.

String coupling is confined here rather than scattered across call sites
(implementation plan §9.2). The spellings are `CHAR-004`'s own and are
case-sensitive: *"Tinder box"* is two words, and ``"Oil"`` is the
Adventuring-Gear row — **not** ``"Oil, Burning"``, which is the Weapons row
and belongs to `COMBAT-*`.

The torch is absent deliberately: `CHAR-004` **exports** it as
:data:`~rules.character_creation.equipment.TORCH`, because it is the one
commodity appearing in both catalogs and needed disambiguating. The
exported identity is used directly, per the human adjudication of
2026-10-01, and `CHAR-004` is **not** modified to add convenience exports
for the other three.
"""

_LIGHT_SOURCE_IDENTITIES: Final = MappingProxyType(
    {
        LightSourceKind.TORCH: _TORCH_ITEM,
        LightSourceKind.LANTERN: catalog_item(_CATALOG_NAMES["LANTERN"]),
    }
)


def _catalog_identity(kind: LightSourceKind) -> Item:
    """The `CHAR-004` catalog row this light source **is**.

    **Identity consumption only, and deliberately not public.** This card
    binds a light-source kind to `CHAR-004`'s row so that it demonstrably
    restates no catalog data of its own. It reads no economic field and
    derives nothing from one: price, encumbrance, price form, capacity,
    size, traits, material and legality are all `CHAR-004`'s (Rule Card
    §C).

    This card is **not** a second equipment catalog: it holds no row, no
    name beyond :data:`_CATALOG_NAMES`, and no value copied from one.
    """
    if not isinstance(kind, LightSourceKind):
        raise ValueError(f"kind must be a LightSourceKind, got {kind!r}")
    return _LIGHT_SOURCE_IDENTITIES[kind]


def _oil_flask_identity() -> Item:
    """The `CHAR-004` row for a flask of lamp oil — the lantern's fuel.

    The Adventuring-Gear ``"Oil"`` row. **Not** ``"Oil, Burning"``: that is
    the Weapons row, and oil thrown as a missile is `COMBAT-*`'s (Rule Card
    §B; approved case `L46`).
    """
    return catalog_item(_CATALOG_NAMES["OIL_FLASK"])


def _tinderbox_identity() -> Item:
    """The `CHAR-004` row for a tinderbox — the ignition implement of §5."""
    return catalog_item(_CATALOG_NAMES["TINDERBOX"])


class IgnitionConditions(Enum):
    """The circumstances an ignition attempt is made in.

    RC names the adverse case by example — *"during high winds or using
    wet wood"* (p. 83) — and gives **no test** for deciding which applies.
    The distinction is therefore DM-supplied, exactly as the Rule Card §1
    records; this card classifies nothing.
    """

    ORDINARY = auto()
    ADVERSE = auto()


class IgnitionOutcome(Enum):
    """Which RC procedure governs an ignition attempt.

    A **branch selection**, not a result: nothing here says the fire was
    lit. :func:`ignition_outcome` tells a caller *which rule applies*, and
    the caller resolves it.
    """

    AUTOMATIC = auto()
    """Ignition succeeds with no roll (RC p. 83, skill + tinderbox,
    ordinary conditions)."""

    ROLL_1D6_IGNITE_1_2 = auto()
    """The caller rolls `1d6` against the project RNG; `1` or `2` ignites.
    **This module rolls nothing and imports no RNG.**"""

    ROUTED_SKILL_CHECK = auto()
    """A `CHAR-012` `Fire-Building` skill check governs. **Emitted, not
    resolved** — the `1d20`, the Intelligence score and the DM-assigned
    penalty are all `CHAR-012`'s, and none appears in this module."""


_IGNITION_MATRIX: Final = MappingProxyType(
    {
        # (has_fire_building, has_tinderbox, conditions): outcome
        (True, True, IgnitionConditions.ORDINARY): IgnitionOutcome.AUTOMATIC,
        (True, True, IgnitionConditions.ADVERSE): IgnitionOutcome.ROUTED_SKILL_CHECK,
        (True, False, IgnitionConditions.ORDINARY): IgnitionOutcome.ROLL_1D6_IGNITE_1_2,
        # SR-11 -- the ruling. RC states the no-tinderbox 1d6 and the
        # adverse-condition skill check as parallel conditionals with no
        # precedence; this intersection satisfies both. The human project
        # owner ruled 2026-10-01 that the adverse branch governs.
        (True, False, IgnitionConditions.ADVERSE): IgnitionOutcome.ROUTED_SKILL_CHECK,
        (False, True, IgnitionConditions.ORDINARY): IgnitionOutcome.ROLL_1D6_IGNITE_1_2,
        # The three RC silences are absent from this table deliberately:
        #   (False, True,  ADVERSE)
        #   (False, False, ORDINARY)
        #   (False, False, ADVERSE)
        # A missing key is refused, so a silence can never be answered by a
        # default -- there is no default to reach.
    }
)
"""The complete ignition matrix as an explicit lookup.

**A mapping, not a chain of conditionals**, so no row can shadow another
and evaluation order cannot create precedence. Five of the eight
combinations resolve; the other three are RC silences and are refused by
their **absence** (Rule Card §5).
"""


def ignition_outcome(
    *,
    has_fire_building: bool,
    has_tinderbox: bool,
    conditions: IgnitionConditions,
    attempt_already_made_this_round: bool,
) -> IgnitionOutcome:
    """Which RC ignition procedure governs this attempt.

    A **stateless branch selector**. It performs no roll, consumes no
    RNG, resolves no skill check, and returns an :class:`IgnitionOutcome`
    — never a :class:`LightSource`. **Selecting a branch is not lighting
    a source**, and applying a successful ignition to a source is not
    authorized by the implementation plan in any slice.

    ``attempt_already_made_this_round`` is **caller-supplied authoritative
    state** (Rule Card §5.1). RC allows *"once per round"*; the rule is
    this card's, knowledge of the round is not. This is the same API
    boundary as ``elapsed_turns`` in :func:`deplete`: the card **enforces**
    a rule from state it is **given**, and does not become the authority
    that **tracks** it. It holds no round counter, no round number and no
    cross-call state, it never mutates the flag, and it returns no
    round-tracking object. Recording that an attempt occurred is the
    caller's, and no orchestrator is created here (approved cases `L19`,
    `L19a`, `L19b`).

    Raises:
        ValueError: a **structural** violation — a non-``bool`` flag, or a
            ``conditions`` that is not an :class:`IgnitionConditions`.
        IgnitionAttemptLimitError: a second attempt this round. A **rules**
            rejection: RC defines the procedure and limits it to once per
            round (approved case `L19`). Raised **before** the matrix is
            consulted.
        IgnitionNotDefinedError: RC defines **no** procedure for this
            combination (approved cases `L23`, `L24`).

    The last two are deliberately distinct: one says the rule does not
    exist, the other says it exists and has already been used.
    """
    for name, value in (
        ("has_fire_building", has_fire_building),
        ("has_tinderbox", has_tinderbox),
        ("attempt_already_made_this_round", attempt_already_made_this_round),
    ):
        # bool is a subtype of int; 1 and 0 would otherwise pass silently.
        if not isinstance(value, bool):
            raise ValueError(f"{name} must be a bool, got {value!r}")
    if not isinstance(conditions, IgnitionConditions):
        raise ValueError(f"conditions must be an IgnitionConditions, got {conditions!r}")

    # The same-round guard precedes branch resolution (Rule Card §5.1), so a
    # second attempt at an RC-silent combination reports the attempt limit
    # rather than the source silence.
    if attempt_already_made_this_round:
        raise IgnitionAttemptLimitError(
            "another ignition attempt is not permitted this round: "
            'RC allows a tinderbox to be tried "once per round" (p. 70)'
        )

    try:
        return _IGNITION_MATRIX[(has_fire_building, has_tinderbox, conditions)]
    except KeyError:
        raise IgnitionNotDefinedError(
            "RC defines no ignition procedure for "
            f"has_fire_building={has_fire_building!r}, has_tinderbox={has_tinderbox!r}, "
            f"conditions={conditions.name}: "
            + (
                "the tinderbox 1d6 is qualified to normal (comparatively dry) circumstances, "
                "and the adverse-condition procedure belongs to the Fire-Building skill"
                if has_tinderbox
                else "no procedure is stated for starting a fire without the skill "
                "and without a tinderbox"
            )
        ) from None


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

    **A malformed member is refused, not filtered.** A collection
    containing something that is not a :class:`LightSource` raises
    ``ValueError``, matching :func:`deplete`'s treatment of the same
    input. Silently dropping it would turn a caller's type error into
    ``any_mundane_source_lit is False`` — a plausible-looking answer, and
    the single output the Rule Card's Finding B surrounds with the most
    warnings against over-reading. That is distinct from a **valid**
    unlit source, which is accepted and simply does not contribute.
    """
    accepted: list[LightSource] = []
    for source in sources:
        if not isinstance(source, LightSource):
            raise ValueError(f"sources must contain LightSource values, got {source!r}")
        if source.lit:
            accepted.append(source)
    return MundaneLightContribution(lit_sources=tuple(accepted))
