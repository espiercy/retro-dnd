"""Shared rules primitive: exact monetary values in Rules Cyclopedia coin.

This contract is owned by no single Rule Card. CHAR-004 §4 states RC's
conversions and needs exact prices; CHAR-004 §7 needs the Druid's +50%
wooden-weapon surcharge to be representable without loss; TREAS-* and
ADV-003 are expected to need the same values later. Each owns *different
data expressed in* money, so none may own the representation itself.

It follows the shared-primitive precedent of
src/rules/character_creation/character_class.py and
src/rules/exploration/turn_credit.py: a small module owned by neither
consuming card individually, carrying representation and nothing else.
See docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md §5.1/§6.1 and §10
(Slice A) for the approved design this module implements.

**Representation.** One integer, in copper pieces. RC's own conversion
line (Ch. 4 p. 62, restated in CHAR-004 §4) fixes the ratios:

    1 pp = 5 gp = 10 ep = 50 sp = 500 cp

so copper is the smallest unit RC names, and every price the approved
catalogs state is an exact whole number of it. The approved plan selected
this representation to keep the Druid surcharge exact: a 3 gp club is
300 cp, and 300 x 3/2 = 450 cp = 4.5 gp, with no float and no rounding
anywhere (implementation plan §5.1, Pre-Code Gate caution 3).

**No floating point is used, produced, or accepted.** ``Coin`` stores an
``int``; every operation here is integer arithmetic; and
:meth:`Coin.scaled` refuses a ratio that would not land on a whole copper
rather than rounding to one.

This module does not, and must not, carry:

- starting-gold generation, equipment catalogs, prices, purchasing, class
  legality or the Druid pricing *policy* — all CHAR-004's, arriving in
  Slices B and C (implementation plan §5, §10);
- encumbrance, movement or dungeon procedures — CHAR-005's and EXP-003's;
- treasure ownership, exchange or market behaviour — TREAS-*, unresearched;
- denominations RC does not name, or operations no approved rule needs.
  The authorization for this slice is explicit that the primitive stays
  narrow and does not become an economy subsystem.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from enum import Enum
from types import MappingProxyType
from typing import Final


class Denomination(Enum):
    """The five Rules Cyclopedia coin denominations (RC Ch. 4 p. 62).

    This enum carries identity and nothing else; the conversion data lives
    in :data:`IN_COPPER`, following the separation
    ``character_class.py`` establishes for shared primitives.
    """

    PLATINUM = 1
    GOLD = 2
    ELECTRUM = 3
    SILVER = 4
    COPPER = 5


IN_COPPER: Final[Mapping[Denomination, int]] = MappingProxyType(
    {
        Denomination.PLATINUM: 500,
        Denomination.GOLD: 100,
        Denomination.ELECTRUM: 50,
        Denomination.SILVER: 10,
        Denomination.COPPER: 1,
    }
)
"""Each denomination's worth in copper pieces.

Derived from RC's single conversion statement, ``1 pp = 5 gp = 10 ep =
50 sp = 500 cp`` (Ch. 4 p. 62; CHAR-004 §4): platinum anchors the line at
500 cp, and each remaining denomination is 500 divided by its stated
count of that denomination per platinum piece.

The table is exposed rather than private because it *is* the approved RC
conversion, and a consuming card asked to show or accept a price in a
named denomination needs it. It carries no price of any item.
"""


@dataclass(frozen=True, slots=True, order=True)
class Coin:
    """An exact quantity of money, stored as whole copper pieces.

    ``copper`` is the only stored field, so two ``Coin`` values are equal
    exactly when they are worth the same, however they were built —
    ``Coin.of(45, Denomination.SILVER) == Coin(450)`` — and ordering is
    plain integer ordering. ``order=True`` supplies the comparisons that
    CHAR-004 §5 step 5 needs ("if cost > money held, the selection is
    invalid") without a hand-written, and therefore fallible, implementation.

    **Non-negative by construction.** RC states no negative price and no
    debt in any approved V1 rule, so a negative amount is rejected rather
    than represented. Chapter 10's passing mention of outstanding debts is
    ``NOT V1-WIRED`` (CHAR-004 §C), and nothing in the approved cluster
    reaches it. A debt mechanic, if one is ever approved, is a rules
    question for its own card, not a representation this primitive should
    pre-build.

    The structural guards and the plain ``ValueError`` follow
    ``turn_credit.TurnCredit``: a shared value object validates its own
    invariants eagerly, and the ``CharacterCreationError`` hierarchy is
    reserved for *domain and rules* rejections owned by a specific card
    (see ``character_creation/errors.py``).
    """

    copper: int

    def __post_init__(self) -> None:
        if not isinstance(self.copper, int) or isinstance(self.copper, bool):
            # bool is a subtype of int, so static typing alone permits
            # Coin(True) and True == 1 would silently read as one copper
            # piece. Excluded explicitly, following src/rng/rng.py,
            # turn_credit.py and hit_points_and_hit_dice.py.
            raise ValueError(f"copper must be an int and must not be a bool, got {self.copper!r}")
        if self.copper < 0:
            raise ValueError(f"copper must not be negative, got {self.copper!r}")

    @classmethod
    def of(cls, amount: int, denomination: Denomination) -> Coin:
        """``amount`` coins of ``denomination``, converted exactly.

        ``amount`` is a whole number of coins of that denomination, which
        is how every approved catalog price and RC's starting-money rule
        express money. A price RC states in a fraction of a denomination —
        the Druid's surcharged club, at 4.5 gp — is not built here; it is
        produced exactly by :meth:`scaled` from the unsurcharged price,
        which is what CHAR-004 §7 specifies.
        """
        if not isinstance(amount, int) or isinstance(amount, bool):
            raise ValueError(f"amount must be an int and must not be a bool, got {amount!r}")
        return cls(amount * IN_COPPER[denomination])

    def __add__(self, other: Coin) -> Coin:
        """Sum of two amounts — a purchase list, or money pooled."""
        return Coin(self.copper + other.copper)

    def __sub__(self, other: Coin) -> Coin:
        """Difference of two amounts, which may not go below zero.

        CHAR-004 §5 makes the caller check affordability *before*
        deducting: a selection costing more than the money held is invalid
        as a whole, and there is no partial purchase. Subtracting past zero
        therefore means the caller skipped that check, and the ``ValueError``
        raised by the constructor says so rather than inventing a debt.
        """
        return Coin(self.copper - other.copper)

    def __mul__(self, count: int) -> Coin:
        """This amount ``count`` times — ``count`` identical items."""
        if not isinstance(count, int) or isinstance(count, bool):
            raise ValueError(f"count must be an int and must not be a bool, got {count!r}")
        return Coin(self.copper * count)

    def scaled(self, numerator: int, denominator: int) -> Coin:
        """This amount times the exact ratio ``numerator / denominator``.

        The operation CHAR-004 §7's Druid surcharge needs: an all-wooden
        weapon costs ``+50%`` over its counterpart, which is ``scaled(3, 2)``.

        **Exact or refused.** If the ratio would not land on a whole copper
        piece, this raises rather than rounding. RC names no unit below the
        copper piece, so a rounded result would be a value the source does
        not have, silently substituted — the class of quiet coercion this
        project's error convention exists to prevent. Every approved
        catalog price is a whole number of silver or gold, hence an even
        number of copper, so ``scaled(3, 2)`` is exact for all of them.
        """
        if not isinstance(numerator, int) or isinstance(numerator, bool):
            raise ValueError(f"numerator must be an int and must not be a bool, got {numerator!r}")
        if not isinstance(denominator, int) or isinstance(denominator, bool):
            raise ValueError(
                f"denominator must be an int and must not be a bool, got {denominator!r}"
            )
        if denominator == 0:
            raise ValueError("denominator must not be zero")
        scaled_copper, remainder = divmod(self.copper * numerator, denominator)
        if remainder:
            raise ValueError(
                f"{self.copper} cp scaled by {numerator}/{denominator} is not a whole "
                f"number of copper pieces; RC names no smaller unit, and this operation "
                f"will not round"
            )
        return Coin(scaled_copper)
