"""CHAR-004 — Starting Equipment & Expedition Preparation (data and derivations).

See docs/rules/character_creation/starting_equipment_and_expedition_preparation.md
(Status: APPROVED, human-approved 2026-09-24) for the governing Rule Card,
and docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md §6.2 and §10 (Slice B)
for the approved implementation contract this module implements.

**Slice B only.** This module currently owns starting money, the V1 mundane
equipment catalogs, and the derived-encumbrance cases of card §6.2. **Per-class
equipment legality and the Druid +50% wooden-weapon surcharge are card §5 and
§7 and are Slice C**; no symbol here decides either, and a guard test asserts
their absence.

WHAT THIS MODULE SUPPLIES, AND WHAT IT REFUSES TO
--------------------------------------------------
Card §6 is explicit: *"This card supplies the ``Enc (cn)`` of every carried
item. It does not compute movement — that is CHAR-005."* Accordingly this
module exposes no movement rate, no encumbrance band, and no total carried
load: a character's total is CHAR-005's to sum (implementation plan §3), and
approved case E60 is the executable form of that boundary.

CATALOG PROVENANCE
------------------
The approved card does not enumerate the Weapons and Adventuring Gear rows.
It **incorporates the printed tables by reference** — §6.1: *"Read directly
from the Weapons, Ammunition, Armor and Adventuring Gear tables as printed"* —
and its source table records each of those pages as visually verified. The
rows below are transcribed from those pages, re-verified from the page images
during implementation, and every value the card's own E-cases state is
asserted by a test. The Armor rows are taken from card §6.1 itself, which
enumerates them.

PRICE IS A SPECIFICATION, NOT ALWAYS ONE AMOUNT
-----------------------------------------------
Slice B originally withheld two printed rows whose cost could not be a single
``Coin``. The human project owner adjudicated both on 2026-09-26, and card
§4.1 now records the three forms RC prints (:class:`FixedPrice`,
:class:`QuantityPrice`, :class:`OpenEndedPrice`). All three rows are
catalogued, and the currency primitive is untouched: ``Coin`` still holds only
exact, non-negative, integral copper pieces, because a price *specification*
is not the same thing as an amount a character can hand over.

- **Torch** — RC prints ``1/6 gp`` in the Weapons Table and, in Adventuring
  Gear, ``2 sp`` for one torch and ``1 gp`` for six. The ``1/6`` is the
  per-unit expression of the six-for-one rate, not a third price; purchasing
  uses the two whole-coin offers. It is **one commodity**: the same ``Item``
  object appears in ``WEAPONS`` and ``ADVENTURING_GEAR``, so swinging a torch
  cannot give it a second price. The printed ``1/6 gp`` is preserved as
  :attr:`QuantityPrice.printed_unit_notation`, not replaced.
- **Clothes, extravagant** — ``50+ gp`` states a floor and no exact price. A
  caller needing a total must resolve it explicitly through
  :func:`resolve_price`; asking for a concrete cost raises rather than
  silently answering ``50 gp``.

The blowgun's normal load, formerly refused because the approved card and RC
disagreed, is ``5`` darts: the card's ``3`` was a transcription defect,
corrected by the same amendment.

This module does not, and must not, carry:

- per-class legality, weapon predicates or the Druid surcharge — card §5/§7,
  Slice C;
- movement, encumbrance bands or a total carried load — CHAR-005;
- dungeon movement or turn accounting — EXP-003 and landed EXP-002;
- mounts, vehicles, ships or siege equipment (card §B, approved case E58) or
  the Chapter 10 high-level pathway (card §C, ``NOT V1-WIRED``, case E59);
- weapon damage, range, initiative or entanglement effects — COMBAT-*;
- light radius or burn duration — EXP-006. Torch and lantern **cost and
  encumbrance** are this card's; their burn time is not;
- an inventory, equipping, ownership or purchasing-workflow subsystem
  (implementation plan §4.1).
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field, replace
from enum import Enum
from types import MappingProxyType
from typing import Final

from rng import RNG
from rules.character_creation.errors import (
    EncumbranceError,
    UnlistedItemError,
    UnresolvedPriceError,
)
from rules.currency import Coin, Denomination

__all__ = [
    "ADVENTURING_GEAR",
    "AMMUNITION",
    "ARMOR",
    "FILLED_QUIVER_ENCUMBRANCE_CN",
    "NET_COST_PER_SQUARE_FOOT",
    "NET_ENCUMBRANCE_CN_PER_SQUARE_FOOT",
    "PLAIN_CLOTHES_SETS",
    "STANDARD_LOAD_SHOTS",
    "TORCH",
    "WATERSKIN_FILLED_ENCUMBRANCE_CN",
    "WEAPONS",
    "WHIP_COST_PER_FOOT",
    "WHIP_ENCUMBRANCE_CN_PER_FOOT",
    "Ammunition",
    "FixedPrice",
    "Item",
    "ItemCategory",
    "KitEntry",
    "OpenEndedPrice",
    "Price",
    "PurchaseOffer",
    "QuantityPrice",
    "WeaponSize",
    "WeaponTrait",
    "ammunition_encumbrance",
    "catalog_item",
    "clothing_encumbrance",
    "filled_container_encumbrance",
    "free_starting_kit",
    "missile_weapon_encumbrance",
    "net",
    "resolve_price",
    "selection_cost",
    "starting_gold",
    "starting_kit_encumbrance",
    "unlisted_item",
    "whip",
]


def _require_int(value: object, name: str) -> int:
    """Reject a non-``int``, and a ``bool`` masquerading as one.

    ``bool`` is a subtype of ``int``, so mypy strict permits ``True`` where an
    ``int`` is expected and it would read as ``1``. Excluded explicitly at
    every entry boundary, following src/rng/rng.py, turn_credit.py and
    hit_points_and_hit_dice.py (implementation plan §12, §14.2).
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"{name} must be an int and must not be a bool, got {value!r}")
    return value


class ItemCategory(Enum):
    """Which Chapter 4 table an item comes from, and how it is encumbered.

    The category is not decoration: three of these select a **different**
    encumbrance rule in card §6.2. ``CONTAINER`` carries the footnote ``*``
    rule (container plus contents); ``CLOTHING`` is exactly the set of rows
    printing footnote ``**`` (worn → disregard), which is why "Hat or cap"
    is ``GEAR`` — it prints no marker. ``SHIELD`` is separated from ``ARMOR``
    because the Armor Table gives it an AC modifier rather than an AC, and
    card §7 permits and forbids it independently of body armour.
    """

    WEAPON = 1
    AMMUNITION = 2
    ARMOR = 3
    SHIELD = 4
    GEAR = 5
    CONTAINER = 6
    CLOTHING = 7


class WeaponSize(Enum):
    """A weapon's size class, read from the Weapons Table's Notes column.

    Card §7: *"Weapon size classes (S/M/L) are read from the Weapons Table's
    Notes column, to which the Ch. 2 entries explicitly refer."* Carried here
    as printed catalog data; the class rules that consume it are Slice C.
    """

    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"


class WeaponTrait(Enum):
    """The RC Weapons Table note codes, as printed (RC p. 63).

    Printed catalog data, carried so a later slice can read it. **Slice B
    attaches no behaviour to any of these** — in particular
    :attr:`CLERIC_PERMITTED` and :attr:`MAGIC_USER_DISCRETIONARY` are the
    table's own note text, not a legality decision, which is card §7 and
    Slice C. The size codes ``S``/``M``/``L`` live on :class:`WeaponSize`
    instead, and the code ``n`` has no member because it marks the two rows
    this module builds by dimension (:func:`net`, :func:`whip`) rather than
    catalogues.
    """

    AMMUNITION_INCLUDED = "a"
    CLERIC_PERMITTED = "c"
    MISSILE_ONLY = "m"
    RARELY_THROWN = "r"
    SPECIAL_FEATURES = "s"
    THROWN = "t"
    SET_VS_CHARGE = "v"
    MAGIC_USER_DISCRETIONARY = "w"
    HAND_OR_TWO_HANDED = "HH"
    TWO_HANDED = "2H"


@dataclass(frozen=True, slots=True)
class PurchaseOffer:
    """One printed "this many, for this much" offer.

    RC prints these only for the torch (one for ``2 sp``, six for ``1 gp``).
    The type exists so the pair stays a pair, rather than becoming a unit
    price that has to be divided.
    """

    count: int
    price: Coin

    def __post_init__(self) -> None:
        if _require_int(self.count, "count") <= 0:
            raise ValueError(f"count must be positive, got {self.count!r}")
        if not isinstance(self.price, Coin):
            raise ValueError(f"price must be a Coin, got {self.price!r}")


@dataclass(frozen=True, slots=True)
class FixedPrice:
    """One unit, one exact amount — card §4.1's ``FIXED`` form.

    What almost every catalog row prints, and the only form that existed
    before the 2026-09-26 amendment.
    """

    unit: Coin

    def __post_init__(self) -> None:
        if not isinstance(self.unit, Coin):
            raise ValueError(f"unit must be a Coin, got {self.unit!r}")

    def cost_of(self, count: int = 1) -> Coin:
        """The exact cost of ``count`` units."""
        if _require_int(count, "count") <= 0:
            raise ValueError(f"count must be positive, got {count!r}")
        return self.unit * count


@dataclass(frozen=True, slots=True)
class QuantityPrice:
    """Stated quantities at stated prices — card §4.1's ``QUANTITY`` form.

    RC prices the torch twice, at one and at six, and the Weapons Table
    quotes the same relationship as a per-unit fraction. Only the printed
    offers are honoured: a count RC prints no offer for is **refused**, not
    prorated. Proration is what would reintroduce the fractional copper
    piece the approved currency primitive exists to exclude — one sixth of
    ``1 gp`` is ``16⅔ cp``, and RC names no unit below the copper piece.

    ``printed_unit_notation`` preserves the source datum (``"1/6 gp"``) so
    the amendment's requirement that it not be silently replaced is visible
    in the data rather than only in prose.
    """

    offers: tuple[PurchaseOffer, ...]
    printed_unit_notation: str | None = None

    def __post_init__(self) -> None:
        if not self.offers:
            raise ValueError("offers must not be empty")
        counts = [offer.count for offer in self.offers]
        if len(set(counts)) != len(counts):
            raise ValueError(f"offers must not repeat a count, got {counts!r}")

    def cost_of(self, count: int) -> Coin:
        """The printed price for exactly ``count`` units."""
        if _require_int(count, "count") <= 0:
            raise ValueError(f"count must be positive, got {count!r}")
        for offer in self.offers:
            if offer.count == count:
                return offer.price
        available = ", ".join(str(offer.count) for offer in self.offers)
        raise UnresolvedPriceError(
            f"RC prints no price for {count} of this item; the printed offers "
            f"are for {available}, and this operation will not prorate one of "
            f"them into a price the source does not state"
        )


@dataclass(frozen=True, slots=True)
class OpenEndedPrice:
    """A stated floor and no ceiling — card §4.1's ``OPEN-ENDED`` form.

    RC prints ``50+ gp`` for extravagant clothes: a minimum, and no exact
    price. :meth:`cost_of` therefore **raises**, because answering the
    minimum would silently supply the value RC withheld (approved case E64).
    A caller resolves it explicitly, through :func:`resolve_price`, with an
    amount its own DM or simulation policy chose.

    No default, markup, percentage or upper bound is modelled. RC states a
    floor; a floor is all that is here.
    """

    minimum: Coin

    def __post_init__(self) -> None:
        if not isinstance(self.minimum, Coin):
            raise ValueError(f"minimum must be a Coin, got {self.minimum!r}")

    def cost_of(self, count: int = 1) -> Coin:
        """Always raises: this price has no single amount to give."""
        raise UnresolvedPriceError(
            f"this price is open-ended — RC states a minimum of "
            f"{self.minimum.copper} cp and no exact price — so a concrete "
            f"cost must be resolved explicitly by DM or simulation policy "
            f"rather than defaulted to the minimum (CHAR-004 §4.1.2)"
        )

    def resolve(self, amount: Coin) -> FixedPrice:
        """This price fixed at an explicitly chosen ``amount``.

        The amount must be at least RC's printed floor; below it is refused
        (approved case E65). Nothing bounds it from above, because RC does
        not.
        """
        if not isinstance(amount, Coin):
            raise ValueError(f"amount must be a Coin, got {amount!r}")
        if amount < self.minimum:
            raise UnresolvedPriceError(
                f"{amount.copper} cp is below the {self.minimum.copper} cp "
                f"minimum RC prints for this item"
            )
        return FixedPrice(amount)


Price = FixedPrice | QuantityPrice | OpenEndedPrice
"""The three price-specification forms card §4.1 records.

Deliberately closed. No further form is added until an approved catalog
entry needs one, and none of these authorises a market, bargaining,
merchant or dynamic-pricing mechanic.
"""


@dataclass(frozen=True, slots=True)
class Item:
    """One catalog row: a name, a price and an encumbrance.

    Deliberately flat. There is no item hierarchy, no equipped state, no
    owner and no quantity: an ``Item`` *is* the printed row, and everything
    that varies — how full a container is, whether a garment is worn, how
    many arrows are carried — is an argument to a derivation function, not a
    mutation of the row (implementation plan §4.1, §10 of the authorization).

    ``capacity_cn`` is the container capacity RC prints, and is ``None`` for
    every item that prints none. It is **not** a carrying capacity for a
    character: RC gives none, and encumbrance bands are CHAR-005's.
    """

    name: str
    category: ItemCategory
    price: Price
    encumbrance_cn: int
    size: WeaponSize | None = None
    traits: frozenset[WeaponTrait] = field(default_factory=frozenset)
    capacity_cn: int | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ValueError(f"name must be a non-empty str, got {self.name!r}")
        if not isinstance(self.price, FixedPrice | QuantityPrice | OpenEndedPrice):
            raise ValueError(f"price must be a Price, got {self.price!r}")
        if _require_int(self.encumbrance_cn, "encumbrance_cn") < 0:
            raise ValueError(f"encumbrance_cn must not be negative, got {self.encumbrance_cn!r}")
        if self.capacity_cn is not None and _require_int(self.capacity_cn, "capacity_cn") <= 0:
            raise ValueError(f"capacity_cn must be positive, got {self.capacity_cn!r}")


@dataclass(frozen=True, slots=True)
class Ammunition:
    """One Ammunition Table row (RC p. 63), whose ``Enc`` is an inverse rate.

    The printed column is ``Enc (# of shots per cn)`` — **shots per coin
    weight, not coin weights per shot**. Card §6.2 records the consequence:
    arrows at ``2`` means two arrows weigh one ``cn``. Reading the column as
    a flat ``cn`` value is the single most likely misreading of this table,
    and is why the rate has its own field name and its own type rather than
    reusing :attr:`Item.encumbrance_cn`.

    ``cost`` is the price of one **standard load** as printed, not of one
    shot: the table's Cost column sits beside its Standard Load column.
    """

    name: str
    weapon: str
    standard_load_shots: int
    cost: Coin
    shots_per_cn: int

    def __post_init__(self) -> None:
        if _require_int(self.standard_load_shots, "standard_load_shots") <= 0:
            raise ValueError(
                f"standard_load_shots must be positive, got {self.standard_load_shots!r}"
            )
        if _require_int(self.shots_per_cn, "shots_per_cn") <= 0:
            raise ValueError(f"shots_per_cn must be positive, got {self.shots_per_cn!r}")


# --- Starting money (card §2) ----------------------------------------------


def starting_gold(rng: RNG) -> Coin:
    """A beginning character's one-time starting money: ``3d6 x 10`` gp.

    Card §2, from RC Ch. 1 p. 8 and Ch. 4 p. 62, which state it identically.
    Range ``30``-``180`` gp. One ``3d6`` expression is rolled, so exactly
    three d6 are consumed in roll order and the call takes a single sequence
    number (approved case E4; RNG_CONTRACT.md §6).

    This is the **only** starting-money rule V1 wires. RC Chapter 10's
    high-level pathway — cash equal to 1% of XP, explicitly not used for
    purchasing — is ``NOT V1-WIRED`` (card §C, approved case E59) and has no
    entry point here.
    """
    return Coin.of(rng.roll("3d6").total * 10, Denomination.GOLD)


# --- Catalogs (card §6.1; RC Ch. 4 pp. 62-63, 67, 69) ----------------------


def _gp(amount: int) -> Coin:
    return Coin.of(amount, Denomination.GOLD)


def _sp(amount: int) -> Coin:
    return Coin.of(amount, Denomination.SILVER)


def _weapon(
    name: str,
    cost: Coin,
    encumbrance_cn: int,
    size: WeaponSize,
    *traits: WeaponTrait,
) -> Item:
    return Item(
        name=name,
        category=ItemCategory.WEAPON,
        price=FixedPrice(cost),
        encumbrance_cn=encumbrance_cn,
        size=size,
        traits=frozenset(traits),
    )


_S: Final = WeaponSize.SMALL
_M: Final = WeaponSize.MEDIUM
_L: Final = WeaponSize.LARGE
_A: Final = WeaponTrait.AMMUNITION_INCLUDED
_C: Final = WeaponTrait.CLERIC_PERMITTED
_MI: Final = WeaponTrait.MISSILE_ONLY
_R: Final = WeaponTrait.RARELY_THROWN
_SP: Final = WeaponTrait.SPECIAL_FEATURES
_T: Final = WeaponTrait.THROWN
_V: Final = WeaponTrait.SET_VS_CHARGE
_W: Final = WeaponTrait.MAGIC_USER_DISCRETIONARY
_HH: Final = WeaponTrait.HAND_OR_TWO_HANDED
_2H: Final = WeaponTrait.TWO_HANDED

_WEAPON_ROWS: Final[tuple[Item, ...]] = (
    _weapon("Axe, Battle", _gp(7), 60, _M, _R, _2H),
    _weapon("Axe, Hand", _gp(4), 30, _S, _T),
    _weapon("Bow, Short", _gp(25), 20, _M, _A, _MI, _2H),
    _weapon("Bow, Long", _gp(40), 30, _L, _A, _MI, _2H),
    _weapon("Crossbow, Lt", _gp(30), 50, _M, _A, _MI, _SP, _2H),
    _weapon("Crossbow, Hvy", _gp(50), 80, _L, _A, _MI, _SP, _2H),
    _weapon("Blackjack", _gp(5), 5, _S, _C, _R, _SP),
    _weapon("Club", _gp(3), 50, _M, _C, _R),
    _weapon("Hammer, Throwing", _gp(4), 25, _M, _C, _T),
    _weapon("Hammer, War", _gp(5), 50, _M, _C, _R),
    _weapon("Mace", _gp(5), 30, _M, _C, _R),
    _weapon("Staff", _gp(5), 40, _M, _C, _R, _W, _2H),
    # "Torch" is withheld: its printed cost of 1/6 gp is not a whole number
    # of copper pieces. See the module docstring.
    _weapon("Dagger, Normal", _gp(3), 10, _S, _T, _W),
    _weapon("Dagger, Silver", _gp(30), 10, _S, _T, _W),
    _weapon("Halberd", _gp(7), 150, _L, _SP, _2H),
    _weapon("Javelin", _gp(1), 20, _M, _T),
    _weapon("Lance", _gp(10), 180, _L, _SP, _V),
    _weapon("Pike", _gp(3), 80, _L, _SP, _V, _2H),
    _weapon("Polearm", _gp(7), 150, _L, _SP, _2H),
    _weapon("Poleaxe", _gp(5), 120, _L, _SP, _2H),
    _weapon("Spear", _gp(3), 30, _L, _T, _V),
    _weapon("Trident", _gp(5), 25, _M, _SP, _T),
    _weapon("Shield, Horned", _gp(15), 20, _S, _SP),
    _weapon("Shield, Knife", _gp(65), 70, _S, _SP),
    _weapon("Shield, Sword", _gp(200), 185, _M, _SP, _V),
    _weapon("Shield, Tusked", _gp(200), 275, _L, _SP, _2H),
    _weapon("Sword, Short", _gp(7), 30, _S, _R),
    _weapon("Sword, Normal", _gp(10), 60, _M, _R),
    # RC prints "Bastard" as a group with two rows, which differ in damage
    # and in note code but share a cost and an encumbrance. Both are kept.
    _weapon("Sword, Bastard, One-Handed", _gp(15), 80, _L, _R, _HH),
    _weapon("Sword, Bastard, Two-Handed", _gp(15), 80, _L, _R, _2H),
    _weapon("Sword, Two-Handed", _gp(15), 100, _L, _2H),
    _weapon("Blowgun, up to 2'", _gp(3), 6, _S, _A, _MI, _SP, _W),
    _weapon("Blowgun, 2' +", _gp(6), 15, _M, _A, _MI, _SP, _W, _2H),
    _weapon("Bola", _gp(5), 5, _M, _SP, _T),
    _weapon("Cestus", _gp(5), 10, _S, _SP),
    _weapon("Holy Water", _gp(25), 1, _S, _C, _SP, _T, _W),
    _weapon("Oil, Burning", _gp(2), 10, _S, _C, _SP, _T, _W),
    # "1/10 gp" — exactly 10 cp, so exactly representable.
    _weapon("Rock, Thrown", Coin.of(10, Denomination.COPPER), 10, _S, _C, _T, _W),
    _weapon("Sling", _gp(2), 20, _S, _C, _MI, _W),
)

TORCH: Final[Item] = Item(
    name="Torch",
    category=ItemCategory.GEAR,
    price=QuantityPrice(
        offers=(
            PurchaseOffer(1, _sp(2)),
            PurchaseOffer(6, _gp(1)),
        ),
        printed_unit_notation="1/6 gp",
    ),
    encumbrance_cn=20,
    size=WeaponSize.SMALL,
    traits=frozenset({WeaponTrait.CLERIC_PERMITTED, WeaponTrait.RARELY_THROWN}),
)
"""The torch — **one commodity**, printed in two RC tables (card §4.1.1).

RC prints it three times: the Weapons Table (p. 62) at ``1/6 gp``, ``Enc 20``,
notes ``c,r,S``; and the Adventuring Gear Table (p. 69) as *"Torch / One torch
/ 2 sp / 20"* and *"Torches / Six torches / 1 gp / 120"*.

This **one object is placed in both** :data:`WEAPONS` and
:data:`ADVENTURING_GEAR`, so a torch cannot acquire a second price by being
used as a weapon (approved case E63). Its weapon size and note codes come
from the Weapons Table; its purchase offers from the gear table.

RC's separate "Torches" bundle row is represented as the **6-count offer**
rather than a second catalog row: its printed ``1 gp`` is that offer, and its
printed ``120 cn`` is exactly ``6 x 20``. Nothing printed is lost, and there
is no second torch commodity for the two to drift apart.
"""

WEAPONS: Final[Mapping[str, Item]] = MappingProxyType(
    {row.name: row for row in (*_WEAPON_ROWS, TORCH)}
)
"""The RC Weapons Table (p. 62), less the two rows RC defines by dimension.

Nets and whips carry the note code ``n`` — their cost and encumbrance are
*"based on size"* — so they are built by :func:`net` and :func:`whip` rather
than catalogued with a fixed cost.

``WEAPONS["Torch"]`` **is the same object as** ``ADVENTURING_GEAR["Torch"]``:
see :data:`TORCH`.
"""

_AMMUNITION_ROWS: Final[tuple[Ammunition, ...]] = (
    Ammunition("Dart", "Blowgun", 5, _gp(1), 5),
    Ammunition("Arrow", "Bow", 20, _gp(5), 2),
    Ammunition("Silver-tipped arrow", "Bow", 1, _gp(5), 2),
    Ammunition("Quarrel", "Crossbow", 30, _gp(10), 3),
    Ammunition("Silver-tipped quarrel", "Crossbow", 1, _gp(5), 3),
    Ammunition("Stone or lead pellet", "Sling", 30, _gp(1), 5),
    Ammunition("Silver pellet", "Sling", 1, _gp(5), 5),
)

AMMUNITION: Final[Mapping[str, Ammunition]] = MappingProxyType(
    {row.name: row for row in _AMMUNITION_ROWS}
)
"""The RC Ammunition Table (p. 63), whose ``Enc`` column is shots per ``cn``."""

_ARMOR_ROWS: Final[tuple[Item, ...]] = (
    Item(
        name="Shield",
        category=ItemCategory.SHIELD,
        price=FixedPrice(_gp(10)),
        encumbrance_cn=100,
    ),
    Item(
        name="Leather Armor",
        category=ItemCategory.ARMOR,
        price=FixedPrice(_gp(20)),
        encumbrance_cn=200,
    ),
    Item(
        name="Scale Mail",
        category=ItemCategory.ARMOR,
        price=FixedPrice(_gp(30)),
        encumbrance_cn=300,
    ),
    Item(
        name="Chain Mail",
        category=ItemCategory.ARMOR,
        price=FixedPrice(_gp(40)),
        encumbrance_cn=400,
    ),
    Item(
        name="Banded Mail",
        category=ItemCategory.ARMOR,
        price=FixedPrice(_gp(50)),
        encumbrance_cn=450,
    ),
    Item(
        name="Plate Mail",
        category=ItemCategory.ARMOR,
        price=FixedPrice(_gp(60)),
        encumbrance_cn=500,
    ),
    Item(
        name="Suit Armor",
        category=ItemCategory.ARMOR,
        price=FixedPrice(_gp(250)),
        encumbrance_cn=750,
    ),
)

ARMOR: Final[Mapping[str, Item]] = MappingProxyType({row.name: row for row in _ARMOR_ROWS})
"""The RC Armor Table (p. 67), exactly as card §6.1 enumerates it.

**Suit Armor is 750 cn and nothing else** (``SR-8``, recorded on CHAR-005).
This catalog supplies the integer; it carries no movement rate of its own,
and no row here is special-cased anywhere in this module.

The table's AC column is not transcribed: armour class is COMBAT-*'s, and
card §A does not assign it here. The note codes ``D``/``T``/``S`` are class-
and description-facing and are likewise not carried — card §7 states the
class permissions directly, and reading them is Slice C's.
"""


def _gear(
    name: str,
    category: ItemCategory,
    cost: Coin,
    encumbrance_cn: int,
    capacity_cn: int | None = None,
) -> Item:
    return Item(
        name=name,
        category=category,
        price=FixedPrice(cost),
        encumbrance_cn=encumbrance_cn,
        capacity_cn=capacity_cn,
    )


_CONTAINER: Final = ItemCategory.CONTAINER
_CLOTHING: Final = ItemCategory.CLOTHING
_GEAR: Final = ItemCategory.GEAR

_ADVENTURING_GEAR_ROWS: Final[tuple[Item, ...]] = (
    _gear("Backpack", _CONTAINER, _gp(5), 20, 400),
    _gear("Belt", _CLOTHING, _sp(2), 5),
    _gear("Boots, plain", _CLOTHING, _gp(1), 10),
    _gear("Boots, riding or swash-topped", _CLOTHING, _gp(5), 15),
    _gear("Cloak, short", _CLOTHING, _sp(5), 10),
    _gear("Cloak, long", _CLOTHING, _gp(1), 15),
    _gear("Clothes, plain", _CLOTHING, _sp(5), 20),
    _gear("Clothes, middle-class", _CLOTHING, _gp(5), 20),
    _gear("Clothes, fine", _CLOTHING, _gp(20), 20),
    Item(
        name="Clothes, extravagant",
        category=_CLOTHING,
        # RC prints "50+ gp": a floor, and no exact price (card §4.1.2).
        price=OpenEndedPrice(_gp(50)),
        encumbrance_cn=30,
    ),
    _gear("Garlic", _GEAR, _gp(5), 1),
    _gear("Grappling hook", _GEAR, _gp(25), 80),
    _gear("Hammer", _GEAR, _gp(2), 10),
    _gear("Hat or cap", _GEAR, _sp(2), 3),
    _gear("Holy symbol", _GEAR, _gp(25), 1),
    _gear("Holy water", _GEAR, _gp(25), 1),
    _gear("Iron spike", _GEAR, _sp(1), 5),
    _gear("Iron spikes", _GEAR, _gp(1), 60),
    _gear("Lantern", _GEAR, _gp(10), 30),
    _gear("Mirror", _GEAR, _gp(5), 5),
    _gear("Oil", _GEAR, _gp(2), 10),
    _gear("Pole", _GEAR, _gp(1), 100),
    _gear("Pouch, belt", _CONTAINER, _sp(5), 2, 50),
    _gear("Quiver", _CONTAINER, _gp(1), 5),
    _gear("Rations, iron", _GEAR, _gp(15), 70),
    _gear("Rations, standard", _GEAR, _gp(5), 200),
    _gear("Rope", _GEAR, _gp(1), 50),
    _gear("Sack, small", _CONTAINER, _gp(1), 1, 200),
    _gear("Sack, large", _CONTAINER, _gp(2), 5, 600),
    _gear("Shoes", _CLOTHING, _sp(5), 8),
    _gear("Stakes (3) and mallet", _GEAR, _gp(3), 10),
    _gear("Thieves' tools", _GEAR, _gp(25), 10),
    _gear("Tinder box", _GEAR, _gp(3), 5),
    TORCH,
    _gear("Waterskin/wineskin", _GEAR, _gp(1), 5),
    _gear("Wine", _GEAR, _gp(1), 30),
    _gear("Wolfsbane", _GEAR, _gp(10), 1),
)

ADVENTURING_GEAR: Final[Mapping[str, Item]] = MappingProxyType(
    {row.name: row for row in _ADVENTURING_GEAR_ROWS}
)
"""The RC Adventuring Gear Table (p. 69), less the one withheld row.

``CLOTHING`` is exactly the set of rows printing footnote ``**``. "Clothes,
plain" prints ``***`` — the *quiver* footnote — where every other clothing row
prints ``**``; the approved card treats that as a **typographic defect** and
applies the ``**`` rule, a treatment the human project owner expressly
approved as a defect reading and **not** a Simulator Ruling (card, Open
Questions 1). It is catalogued as ``CLOTHING`` on that basis.

The quiver is a ``CONTAINER`` but carries no ``capacity_cn``: RC prints none
for it, and its filled encumbrance is the stated total at
:data:`FILLED_QUIVER_ENCUMBRANCE_CN` rather than a derivation from contents.

Two rows do not carry a single fixed amount (card §4.1): the torch, whose
price is its printed quantity offers (:data:`TORCH`), and "Clothes,
extravagant", whose ``50+ gp`` is a floor. RC's "Torches" row is the torch's
6-count offer rather than a row of its own.
"""

_CATALOGS: Final[tuple[Mapping[str, Item], ...]] = (WEAPONS, ARMOR, ADVENTURING_GEAR)


def catalog_item(name: str) -> Item:
    """The catalog row with this exact name.

    Card §8, from RC Ch. 13 p. 147: *"Beginning characters are restricted to
    the Chapter 4 catalogs unless the DM allows otherwise."* A name that is
    not catalogued raises :class:`UnlistedItemError` (approved case E56), and
    mounts, vehicles, ships and siege equipment are refused by exactly this
    path because they are deliberately not catalogued (case E58). When the DM
    does allow an unlisted item, it is built by :func:`unlisted_item`, which
    requires its cost and encumbrance.
    """
    for catalog in _CATALOGS:
        found = catalog.get(name)
        if found is not None:
            return found
    raise UnlistedItemError(
        f"{name!r} is not in the Chapter 4 catalogs; a beginning character is "
        f"restricted to them unless the DM allows otherwise, and an allowed "
        f"item must be supplied with its cost and encumbrance (CHAR-004 §8)"
    )


def unlisted_item(
    name: str,
    category: ItemCategory,
    *,
    cost: Coin | None,
    encumbrance_cn: int | None,
) -> Item:
    """An item the DM has allowed from outside the Chapter 4 catalogs.

    Card §8 is explicit that the DM **must** set cost, encumbrance and other
    characteristics, and that **no default is invented**. Omitting either is
    an error rather than a zero or a guess (approved case E57).

    The DM supplies one exact amount, so the result carries a
    :class:`FixedPrice`. RC's other two price forms describe *printed* rows;
    nothing in card §8 asks a DM to invent a bundle or a floor.
    """
    if cost is None or encumbrance_cn is None:
        raise UnlistedItemError(
            f"the DM allowed {name!r} but supplied "
            f"{'no cost' if cost is None else 'no encumbrance'}; CHAR-004 §8 "
            f"requires both to be set and permits no default"
        )
    return Item(
        name=name,
        category=category,
        price=FixedPrice(cost),
        encumbrance_cn=encumbrance_cn,
    )


def resolve_price(item: Item, amount: Coin) -> Item:
    """``item`` with its open-ended price fixed at an explicitly chosen amount.

    The one way an open-ended price becomes a purchasable one (card §4.1.2,
    approved case E65). The amount comes from the caller's DM or simulation
    policy, must be at least RC's printed floor, and is bounded above by
    nothing, because RC bounds it by nothing.

    Refused for an item whose price is already exact: there would be nothing
    to resolve, and quietly overwriting a printed price is not resolution.
    """
    if not isinstance(item, Item):
        raise ValueError(f"item must be an Item, got {item!r}")
    if not isinstance(item.price, OpenEndedPrice):
        raise UnresolvedPriceError(
            f"{item.name!r} has no open-ended price to resolve; RC prints its "
            f"price, and this operation will not overwrite one"
        )
    return replace(item, price=item.price.resolve(amount))


# --- Derived encumbrance (card §6.2) ---------------------------------------

FILLED_QUIVER_ENCUMBRANCE_CN: Final = 10
"""A filled quiver's encumbrance **in total**: ``10 cn``, not ``5 + 10``.

RC's footnote ``***`` (p. 69): a 5-cn quiver plus 10 cn of missiles — 20
arrows or 30 quarrels — *"still equals only a 10-cn encumbrance bundle to
carry around."* Card §6.2 records it as a stated total, and approved case E12
is the executable form. The quiver is therefore the one container the
footnote ``*`` arithmetic does **not** govern.

RC states the empty value and this filled total and nothing between them, so
a partly filled quiver is not derived here.
"""

WATERSKIN_FILLED_ENCUMBRANCE_CN: Final = 30
"""A filled waterskin's encumbrance: ``30 cn`` against ``5 cn`` empty.

RC prints both on the Adventuring Gear row itself (*"One-quart capacity; enc
30 when filled"*); card §6.2 restates them. Both are stated values, so
neither is derived (approved case E25).
"""

NET_COST_PER_SQUARE_FOOT: Final[Coin] = _sp(1)
NET_ENCUMBRANCE_CN_PER_SQUARE_FOOT: Final = 1
WHIP_COST_PER_FOOT: Final[Coin] = _gp(1)
WHIP_ENCUMBRANCE_CN_PER_FOOT: Final = 10

STANDARD_LOAD_SHOTS: Final[Mapping[str, int]] = MappingProxyType(
    {
        "Bow, Short": 20,
        "Bow, Long": 20,
        "Crossbow, Lt": 30,
        "Crossbow, Hvy": 30,
        "Sling": 30,
        "Blowgun, up to 2'": 5,
        "Blowgun, 2' +": 5,
    }
)
"""The normal load already included in a missile weapon's printed ``Enc``.

RC's Weapons Table note ``a`` (p. 63): *"bow: 20 arrows; crossbow: 30
quarrels; sling: 30 stones; blowgun: 5 darts"*, and card §6.2 restates the
rule.

**Keyed by note ``a``'s text, not by the printed marker.** The note names four
weapon families — bow, crossbow, sling, blowgun — but RC's Sling row prints
``c,m,w,S`` and **no** ``a`` marker. The note's text is the rule; the row's
missing marker is a printed-marker omission, and no marker is invented for the
row to compensate. This is why :func:`missile_weapon_encumbrance` gates on
this table rather than on :attr:`WeaponTrait.AMMUNITION_INCLUDED`.

**The blowgun is 5 darts** (approved case E66). Slice B originally refused it,
because the approved card's summary said 3 and RC's two governing objects said
5; the human-approved amendment of 2026-09-26 recorded the card's figure as a
transcription defect and corrected it. The RC figure is also the coherent one:
at RC's rate of 5 darts per ``cn``, a normal load is exactly ``1 cn``.
"""

PLAIN_CLOTHES_SETS: Final[tuple[int, ...]] = (2, 3)
"""The sets of plain clothes a new character owns: RC says "two or three".

Card §3 preserves the indeterminacy rather than resolving it, so
:func:`free_starting_kit` requires the caller to choose one of these and
assumes neither. The choice cannot change the kit's encumbrance in any case,
because the clothes are worn (approved case E16).
"""


def filled_container_encumbrance(container: Item, contents_cn: int) -> int:
    """A container's encumbrance carrying ``contents_cn`` of goods.

    RC's Adventuring Gear footnote ``*``: the printed value is the container's
    encumbrance **when empty**, and when goods are placed within it the
    encumbrance includes *"both the item's encumbrance and the encumbrance of
    the goods within it"*. So the answer is the sum, and for a fully loaded
    belt pouch it is ``2 + 50 = 52`` — **Simulator Ruling SR-6**, which
    preserves RC's two independently stated inputs over its inconsistent
    printed total of ``55`` (approved case E6).

    Capacity is a **hard limit**: goods exceeding it are refused rather than
    silently carried (approved case E13).
    """
    if not isinstance(container, Item):
        raise ValueError(f"container must be an Item, got {container!r}")
    if container.category is not ItemCategory.CONTAINER:
        raise EncumbranceError(
            f"{container.name!r} is not a container, so RC's footnote * "
            f"container arithmetic does not apply to it"
        )
    if container.capacity_cn is None:
        raise EncumbranceError(
            f"RC prints no capacity for {container.name!r}, and its filled "
            f"encumbrance is a stated total rather than container-plus-contents "
            f"(footnote ***); see FILLED_QUIVER_ENCUMBRANCE_CN"
        )
    if _require_int(contents_cn, "contents_cn") < 0:
        raise ValueError(f"contents_cn must not be negative, got {contents_cn!r}")
    if contents_cn > container.capacity_cn:
        raise EncumbranceError(
            f"{contents_cn} cn of goods exceeds the {container.capacity_cn} cn "
            f"capacity RC prints for {container.name!r}; capacity is a hard limit"
        )
    return container.encumbrance_cn + contents_cn


def clothing_encumbrance(item: Item, *, worn: bool) -> int:
    """A garment's encumbrance: ``0`` when worn, the printed value when packed.

    RC's Adventuring Gear footnote ``**``: the printed value is the
    encumbrance *"if packed. If the clothes are worn, disregard the
    encumbrance"* (approved cases E14, E15).

    The distinction is expressed here, as an argument, and **never by
    mutating the catalog row** — the printed value stays printed, and a
    garment has no equipped state to carry (authorization §9.4).
    """
    if not isinstance(item, Item):
        raise ValueError(f"item must be an Item, got {item!r}")
    if item.category is not ItemCategory.CLOTHING:
        raise EncumbranceError(
            f"{item.name!r} does not carry RC's footnote **, so the "
            f"worn-versus-packed rule does not apply to it"
        )
    if not isinstance(worn, bool):
        raise ValueError(f"worn must be a bool, got {worn!r}")
    return 0 if worn else item.encumbrance_cn


def ammunition_encumbrance(row: Ammunition, shots: int) -> int:
    """The encumbrance of ``shots`` rounds of this ammunition.

    The Ammunition Table's ``Enc`` column is **shots per cn**, an inverse
    rate, so the answer is ``shots / shots_per_cn`` — 10 arrows at 2 per cn is
    ``5 cn``, and 30 sling stones at 5 per cn is ``6 cn`` (approved cases E23,
    E24).

    **Exact or refused.** RC states the rate in whole coin weights and says
    nothing about a quantity that falls between them, so a count that does not
    divide evenly raises rather than rounding: a rounded answer would be a
    value the source does not have (AGENTS.md §3).
    """
    if not isinstance(row, Ammunition):
        raise ValueError(f"row must be an Ammunition, got {row!r}")
    if _require_int(shots, "shots") < 0:
        raise ValueError(f"shots must not be negative, got {shots!r}")
    encumbrance_cn, remainder = divmod(shots, row.shots_per_cn)
    if remainder:
        raise EncumbranceError(
            f"{shots} x {row.name} is not a whole number of cn at RC's rate of "
            f"{row.shots_per_cn} shots per cn, and RC states no encumbrance for "
            f"a quantity between its rates; this operation will not round"
        )
    return encumbrance_cn


def missile_weapon_encumbrance(weapon: Item, ammunition: Ammunition, shots: int) -> int:
    """A missile weapon's encumbrance carrying ``shots`` rounds rather than its load.

    RC's Weapons Table note ``a``: the printed ``Enc`` **already includes** the
    weapon's normal load, and varying that load varies the encumbrance at the
    ammunition's own rate. So a long bow is ``30 cn`` as printed with its 20
    arrows, ``20 cn`` with none, and a light crossbow is ``40 cn`` without its
    quarrels — the two figures RC works out itself (approved cases E20-E22).

    The blowgun's normal load is **5 darts**, which at RC's rate of 5 darts
    per ``cn`` is exactly ``1 cn``: a short blowgun is ``6 cn`` as printed and
    ``5 cn`` empty (approved case E66).
    """
    if not isinstance(weapon, Item):
        raise ValueError(f"weapon must be an Item, got {weapon!r}")
    standard_load = STANDARD_LOAD_SHOTS.get(weapon.name)
    if standard_load is None:
        raise EncumbranceError(
            f"RC's note a states no normal load for {weapon.name!r}, so its "
            f"printed encumbrance includes nothing to vary"
        )
    return (
        weapon.encumbrance_cn
        - ammunition_encumbrance(ammunition, standard_load)
        + ammunition_encumbrance(ammunition, shots)
    )


def net(side_feet: int) -> Item:
    """A square net ``side_feet`` on a side, priced and encumbered by its size.

    RC's Weapons Table note ``n``: *"Nets cost 1 sp per square foot of surface
    area and have an encumbrance of 1 cn per square foot. A Medium net (6' x
    6') would cost 36 sp (3.6 gp) and have an encumbrance of 36 cn"* (approved
    cases E17, E18).

    Square, because every size RC's Nets Table prints is square — 2'x2'
    through 25'x25' — and its own footnote adds *"or equivalent in square
    feet"*. A non-square net is not modelled, and the Nets Table's mapping
    from victim size to net size is not this slice's.
    """
    if _require_int(side_feet, "side_feet") <= 0:
        raise ValueError(f"side_feet must be positive, got {side_feet!r}")
    square_feet = side_feet * side_feet
    return Item(
        name=f"Net, {side_feet}' x {side_feet}'",
        category=ItemCategory.WEAPON,
        price=FixedPrice(NET_COST_PER_SQUARE_FOOT * square_feet),
        encumbrance_cn=NET_ENCUMBRANCE_CN_PER_SQUARE_FOOT * square_feet,
        traits=frozenset({WeaponTrait.SPECIAL_FEATURES, WeaponTrait.THROWN, _W}),
    )


def whip(length_feet: int) -> Item:
    """A whip ``length_feet`` long, priced and encumbered by its length.

    RC's Weapons Table prints the whip's cost as ``1/ft`` gp and its
    encumbrance as ``10/ft`` cn, so a 10-foot whip costs ``10 gp`` and weighs
    ``100 cn`` (approved case E19).
    """
    if _require_int(length_feet, "length_feet") <= 0:
        raise ValueError(f"length_feet must be positive, got {length_feet!r}")
    return Item(
        name=f"Whip, {length_feet} ft",
        category=ItemCategory.WEAPON,
        price=FixedPrice(WHIP_COST_PER_FOOT * length_feet),
        encumbrance_cn=WHIP_ENCUMBRANCE_CN_PER_FOOT * length_feet,
        size=WeaponSize.MEDIUM,
        traits=frozenset({WeaponTrait.SPECIAL_FEATURES, _W}),
    )


# --- The free starting kit (card §3) ---------------------------------------


@dataclass(frozen=True, slots=True)
class KitEntry:
    """One line of the free starting kit: an item, how many, and whether worn.

    ``worn`` is carried because card §3 states the consequence directly —
    the clothes and shoes are worn, so footnote ``**`` applies and their
    encumbrance is disregarded — not because equipment generally has an
    equipped state. Nothing outside the kit uses this type.
    """

    item: Item
    count: int
    worn: bool

    def __post_init__(self) -> None:
        if not isinstance(self.item, Item):
            raise ValueError(f"item must be an Item, got {self.item!r}")
        if _require_int(self.count, "count") <= 0:
            raise ValueError(f"count must be positive, got {self.count!r}")
        if not isinstance(self.worn, bool):
            raise ValueError(f"worn must be a bool, got {self.worn!r}")

    @property
    def encumbrance_cn(self) -> int:
        """This line's encumbrance, applying footnote ``**`` when it is clothing."""
        if self.item.category is ItemCategory.CLOTHING:
            return self.count * clothing_encumbrance(self.item, worn=self.worn)
        return self.count * self.item.encumbrance_cn


def free_starting_kit(plain_clothes_sets: int) -> tuple[KitEntry, ...]:
    """What a newly created character owns without purchase (card §3).

    RC Ch. 4 p. 62, the most specific of its three statements: *"two or three
    sets of plain clothes, a pair of shoes, a belt, and a belt-pouch."*

    ``plain_clothes_sets`` must be one of :data:`PLAIN_CLOTHES_SETS`, and has
    no default: RC states a range rather than a number, and picking one would
    be deciding something RC left open. It cannot change the kit's
    encumbrance, because the clothes are worn either way (approved case E16).

    The clothes, shoes and belt are **worn**; the belt-pouch is carried, and
    is issued empty — ``2 cn``, and ``52 cn`` once filled (``SR-6``).
    """
    if _require_int(plain_clothes_sets, "plain_clothes_sets") not in PLAIN_CLOTHES_SETS:
        raise ValueError(
            f"plain_clothes_sets must be one of {PLAIN_CLOTHES_SETS} — RC says "
            f'"two or three sets of plain clothes" — got {plain_clothes_sets!r}'
        )
    return (
        KitEntry(ADVENTURING_GEAR["Clothes, plain"], plain_clothes_sets, worn=True),
        KitEntry(ADVENTURING_GEAR["Shoes"], 1, worn=True),
        KitEntry(ADVENTURING_GEAR["Belt"], 1, worn=True),
        KitEntry(ADVENTURING_GEAR["Pouch, belt"], 1, worn=False),
    )


def starting_kit_encumbrance(kit: Iterable[KitEntry]) -> int:
    """The free starting kit's own encumbrance — ``2 cn`` as issued (case E16).

    Deliberately scoped to the kit. This is **not** a character's total
    carried encumbrance: summing everything a character carries, and reading
    a band from the total, is CHAR-005's (implementation plan §3), and no
    operation here accepts a character or a full inventory.
    """
    return sum(entry.encumbrance_cn for entry in kit)


# --- Purchase arithmetic (card §5 steps 5 and 6) ---------------------------


def selection_cost(items: Iterable[Item]) -> Coin:
    """The total printed cost of a selection of items.

    Card §5 step 5: *"Sum cost. If cost > money held, the selection is
    invalid; remove items until it is not."* The comparison and the deduction
    are the shared currency primitive's — ``total <= money_held`` and
    ``money_held - total`` — which is what ``Coin``'s ordering and its refusal
    to go below zero exist for (approved cases E53-E55). There is no partial
    purchase, so nothing here removes an item on the caller's behalf.

    **Printed cost only.** The Druid's +50% wooden-weapon surcharge is card
    §7 and Slice C; this function applies no class-dependent price.

    Each item contributes the cost of **one** unit. An item whose price
    states no single amount — extravagant clothes, whose ``50+ gp`` has no
    exact value until DM or simulation policy sets one — raises rather than
    contributing its floor; resolve it first with :func:`resolve_price`
    (approved case E64).
    """
    total = Coin(0)
    for item in items:
        if not isinstance(item, Item):
            raise ValueError(f"every selected item must be an Item, got {item!r}")
        total = total + item.price.cost_of(1)
    return total
