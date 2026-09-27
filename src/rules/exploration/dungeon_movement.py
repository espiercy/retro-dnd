"""EXP-003 — Dungeon Movement.

See docs/rules/exploration/dungeon_movement.md (Status: APPROVED,
human-approved 2026-09-24) for the governing Rule Card, and
docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md §6.4 and §10 (Slice E) for
the approved implementation contract this module implements.

**This card carries no Simulator Ruling.** Every clause is Rules Cyclopedia
Explicit or a necessary consequence of one, and that is a finding rather
than an omission — it is the simplest of the three CLUSTER-003 cards.

WHAT THIS MODULE DOES
---------------------
One thing: it turns a party's **already-derived** normal speed into the
distance available in one 10-minute exploration turn, and divides that by
the map scale on request. RC Ch. 7 p. 91: *"customarily characters will
travel at their normal speed during game turns."*

**It consumes a rate and computes none.** :func:`turn_movement_allowance`
takes a :class:`~rules.character_creation.encumbrance_and_movement.MovementRate`
and reads ``.normal`` — it never receives encumbrance, class or level, so it
is structurally incapable of re-deriving a rate that CHAR-005 owns (approved
case D29). The type system enforces the ownership boundary; that is
deliberate, and it is why the signature takes a ``MovementRate`` rather than
a bare number.

IT OWNS THE MOVEMENT SPEND, NOT THE LOOP
----------------------------------------
RC's Game Turn Checklist (p. 91) has four steps, and this card owns the
movement declared at step 2 and nothing else:

    1. WANDERING MONSTERS      arrivals from the previous turn's check
                               -> EXP-001 / EXP-002, both LANDED
    2. ACTIONS                 movement, listening, searching, ...
                               -> THIS CARD OWNS ONLY THE MOVEMENT SPEND;
                                  listening, searching and doors are
                                  EXP-005's, traps EXP-007's
    3. RESULTS                 discoveries, area descriptions, encounters
    4. WANDERING-MONSTER CHECK 1d6 every other turn  -> EXP-001, LANDED

:data:`GAME_TURN_CHECKLIST` records those four steps as inert data so the
delegation is legible. **No function here runs them.** There is no
``explore()``, no ``run_turn()``, no engine and no state: this module returns
an allowance and the caller spends it (plan §4.1, §5.6).

**A random encounter is not automatically combat.** Steps 1 and 4 route to
the Encounter Checklist, which begins with detection, surprise and reaction
(ENC-002/ENC-003). Nothing here encodes an assumption that movement becomes
combat (AGENTS.md §5, approved case D23).

WHAT THE RATE ALREADY COVERS
----------------------------
RC Ch. 6 p. 88: *"this rate includes many assumed actions — mapping, peeking
around corners, resting, and so forth."* The consequence is a hard
constraint: **charging additional exploration time for mapping would
double-count a cost the rate already contains.** This module creates no
mapping time cost, no mapping roll, no mapping failure state and no mapping
movement penalty (card §4, cases D12-D17).

Mapping owns no mechanic at all. RC's four presentations were located and
read in full during Stage A and **none** contains a die roll, a time cost or
a failure state; the mapper and caller are player roles, and RC says of the
caller that *"it's not a game rule that players have to use"* (case D16).

TERRAIN DOES NOT APPLY AT THIS SCALE
------------------------------------
RC Ch. 6 p. 88 states it positively: *"Though it makes no difference to the
combat round or the 10-minute turn, the terrain may affect the distance a
party travels in a day."* That is a statement of **non-application**, not an
absence of evidence, so no terrain mechanic is created here (cases
D18-D20). The overland Terrain Effects and Traveling Rates tables are
per-day and outdoor, and do not reach a dungeon turn.

This module does not, and must not, carry:

- the movement rate itself, encumbrance, bands or the party rule — CHAR-005's;
- turn or round accounting — landed EXP-002's. **It imports nothing from
  dungeon_turn_time_accounting**; the integration is demonstrated by a test
  that drives the real ``complete_ordinary_turn()`` alongside an allowance;
- wandering-monster checks — landed EXP-001's;
- surprise, encounter distance, reaction, evasion — ENC-002/003/005;
- listening, searching, doors, traps, light — EXP-005/006/007;
- party formation or marching order — EXP-010, deferred, and **not** an
  incoming dependency (case D32);
- **spatial quantisation.** §3 divides by the map scale and does not round.
  Snapping a fractional allowance to whole squares is a separate execution
  concern this card explicitly does not own (cases D9, D31).
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Final

from rules.character_creation.encumbrance_and_movement import MovementRate

__all__ = [
    "DEFAULT_MAP_SCALE_FEET",
    "GAME_TURN_CHECKLIST",
    "DungeonMovementAllowance",
    "turn_movement_allowance",
]

DEFAULT_MAP_SCALE_FEET: Final = 10
"""The customary dungeon map scale: one graph-paper square is ``10'``.

RC Ch. 6 p. 87 and Ch. 13 p. 148 both give it, and Ch. 17 p. 260 makes it
explicitly **DM-variable** — *"each square normally representing a 10' x 10'
area, or any other scale you prefer"*.

**A default, not a constant** (card Open Questions 2, recorded so a later
reader does not harden it into an invariant). A configured scale changes the
square count and **must not** change the underlying rate in feet (case D11).
"""

GAME_TURN_CHECKLIST: Final[tuple[str, ...]] = (
    "Wandering monsters",
    "Actions",
    "Results",
    "Wandering-monster check",
)
"""RC's four-step Game Turn Checklist (p. 91), recorded as **inert data**.

Here so the delegation in this module's docstring is legible and testable,
not so anything can iterate it: steps 1 and 4 are EXP-001's and EXP-002's,
step 3 is the DM's description obligation, and of step 2 this card owns
**only the movement spend**. **No function in this module runs a step, and
none ever should** — this card returns an allowance and owns no loop.
"""


@dataclass(frozen=True, slots=True)
class DungeonMovementAllowance:
    """The distance a party may cover in one 10-minute exploration turn.

    ``feet`` is the authoritative value, in **feet**, indoors (card §2, §3).
    It is a :class:`~fractions.Fraction` because CHAR-005's rates are — a
    Mystic's ``43 1/3'`` flows through this card unaltered — and because
    nothing here may round (cases D9, D30, D31).

    Carries no turn number, no elapsed time and no position. A turn credit
    is landed EXP-002's and a party's location is nobody's yet.
    """

    feet: Fraction

    def __post_init__(self) -> None:
        if isinstance(self.feet, bool):
            raise ValueError(f"feet must not be a bool, got {self.feet!r}")
        if not isinstance(self.feet, Fraction):
            raise ValueError(
                f"feet must be a Fraction — the allowance stays exact and a "
                f"float or an int would invite a value to be lost — got "
                f"{self.feet!r}"
            )
        if self.feet < 0:
            raise ValueError(f"feet must not be negative, got {self.feet!r}")

    @property
    def is_immobile(self) -> bool:
        """Whether the party cannot advance at all this turn (case D3)."""
        return self.feet == 0

    def squares(self, scale_feet: int = DEFAULT_MAP_SCALE_FEET) -> Fraction:
        """This allowance in map squares, at ``scale_feet`` feet per square.

        Card §3: ``squares_available = distance_available_this_turn /
        map_scale``. At the default scale a party at ``120'`` covers **12
        squares** (case D7).

        **Exact, and never rounded.** ``15'`` at the default scale is ``1.5``
        squares and stays ``1.5`` (case D9); a Mystic's ``43 1/3'`` stays a
        third of a foot off a whole square. Snapping to whole squares is a
        separate execution concern this card does not own (case D31).

        **Changing the scale changes only this answer.** :attr:`feet` is
        untouched by it, because the rate is in feet and the scale is a
        drawing convention (cases D10, D11).
        """
        if isinstance(scale_feet, bool) or not isinstance(scale_feet, int):
            raise ValueError(
                f"scale_feet must be an int and must not be a bool, got {scale_feet!r}"
            )
        if scale_feet <= 0:
            raise ValueError(f"scale_feet must be positive, got {scale_feet!r}")
        return self.feet / scale_feet


def turn_movement_allowance(party_rate: MovementRate) -> DungeonMovementAllowance:
    """The distance available in one exploration turn, from the party's rate.

    RC Ch. 7 p. 91: *"customarily characters will travel at their **normal
    speed** during game turns."* So this reads ``party_rate.normal`` — feet
    per turn — and nothing else.

    **Not encounter speed, and not running speed.** Those belong to the
    combat sequence and to flight, and are CHAR-005's to define (cases D4,
    D5). There is no parameter through which either could be supplied: the
    argument is a whole :class:`MovementRate`, and only its normal speed is
    read.

    **Not a re-derivation.** It receives no encumbrance, no class and no
    level, so it cannot compute a rate even by accident — deriving the party
    rate from its slowest member is CHAR-005 §8's (case D29).

    ``party_rate`` is expected to be the *party* rate already. This function
    cannot verify that, and does not pretend to: a single character's rate is
    a well-formed argument, and whether a group intended to stay together is
    a question CHAR-005 answers before this is called.
    """
    if not isinstance(party_rate, MovementRate):
        raise ValueError(f"party_rate must be a MovementRate, got {party_rate!r}")
    return DungeonMovementAllowance(party_rate.normal)
