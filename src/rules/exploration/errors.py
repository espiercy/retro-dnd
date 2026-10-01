"""Domain rejections for the exploration rules domain.

Distinct from the plain ``ValueError`` that value objects in this package
raise for *structural* violations — a non-``int``, a ``bool``
masquerading as one, a negative count. That convention is established by
src/rules/exploration/turn_credit.py and dungeon_movement.py and is
preserved; this module is for *rules* rejections, where the source
defines no procedure for what was asked.

**One concrete type, no base class.** The character-creation domain uses
a base plus subclasses because it has ten of them
(src/rules/character_creation/errors.py). Exploration has exactly one
domain rejection today, so a base would be a hierarchy built ahead of
need. The EXP-006 implementation plan's §11 originally sketched an
``ExplorationError`` base as well; the human adjudication of 2026-10-01
directs that a single concrete type be preferred where it suffices, and
that no speculative exploration-wide hierarchy be built. Recorded there
as a deliberate departure from the plan sketch.

``CharacterCreationError`` is deliberately **not** reused: it is scoped
by name to character creation, and its own docstring draws that domain
boundary.
"""

from __future__ import annotations


class IgnitionNotDefinedError(Exception):
    """RC defines no ignition procedure for the combination requested.

    EXP-006 Rule Card §5, CLUSTER-004 Slice C. Raised for the two
    source-undefined paths, distinguished by message:

    - **no `Fire-Building`, with a tinderbox, in adverse conditions.**
      RC's tinderbox rule is expressly qualified to *"normal
      (comparatively dry) circumstances"* (p. 70), and the
      adverse-condition procedure RC does supply belongs to the
      `Fire-Building` skill (p. 83), which this character lacks.
      Applying the `1d6` outside its stated qualification would **extend**
      RC; supplying any other number would **invent** one (approved case
      `L23`);

    - **no `Fire-Building` and no tinderbox**, in any conditions. RC
      states no procedure at all for starting a fire bare-handed without
      the skill (approved cases `L24`).

    The request is **refused rather than defaulted**. A default would be
    a value the source does not have, which `AGENTS.md` §3 prohibits.

    Not raised for a caller-protocol violation — a second ignition
    attempt in the same round raises the plain ``ValueError`` that
    structural violations raise, because the rules are not what reject
    it (approved case `L19`).
    """
