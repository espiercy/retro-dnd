"""Shared character-creation primitive: the nine character-class identities.

This contract is owned by no single Rule Card. CHAR-001 §4 needs the chosen
class to determine legal trade targets, CHAR-002 §2 enumerates exactly these
nine, and CHAR-003 §1 keys its Hit Die table on them — each owns *different
data about* the same nine classes, so none may own the enum itself. See
docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §6.2/§7.2 (Slice A).

This module carries identity and nothing else.

It does not, and must not, attach:

- prime requisites or creation minimums (CHAR-002, race_and_class_eligibility.py);
- Hit Dice, Name levels, maximum levels or fixed hit-point gains
  (CHAR-003, hit_points_and_hit_dice.py — and maximum levels remain
  ADV-002's authoritative property, projected there only to bound
  hit-point behaviour);
- experience-point modifiers (ADV-001, not implemented);
- class special abilities, equipment restrictions or alignment
  requirements (CHAR-009, CHAR-008, CHAR-011, CHAR-012, none implemented).
"""

from __future__ import annotations

from enum import Enum


class CharacterClass(Enum):
    """The nine Rules Cyclopedia player-character classes (RC p. 7).

    RC groups them as four human classes (cleric, fighter, magic-user,
    thief), three demihuman classes (dwarf, elf, halfling) and two special
    classes (druid, mystic).

    ``DRUID`` is a member because approved cases require a result for it,
    not in anticipation of future work: CHAR-002 §2 must return
    NOT_ELIGIBLE_AT_CREATION for it (cases E18/E19), and CHAR-003 §1 lists
    it with "does not apply" for Hit Dice (case H39).
    """

    CLERIC = 1
    FIGHTER = 2
    MAGIC_USER = 3
    THIEF = 4
    DWARF = 5
    ELF = 6
    HALFLING = 7
    MYSTIC = 8
    DRUID = 9
