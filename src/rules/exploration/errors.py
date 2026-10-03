"""Domain rejections for the exploration rules domain.

Distinct from the plain ``ValueError`` that value objects in this package
raise for *structural* violations — a non-``int``, a ``bool``
masquerading as one, a negative count. That convention is established by
src/rules/exploration/turn_credit.py and dungeon_movement.py and is
preserved; this module is for *rules* rejections, where the source
defines no procedure for what was asked.

**Concrete types, no base class.** The character-creation domain uses a
base plus subclasses because it has ten of them
(src/rules/character_creation/errors.py). Exploration has three domain
rejections, which does not require a hierarchy; the EXP-006
implementation plan's §11 originally sketched an ``ExplorationError``
base, and the human adjudication of 2026-10-01 directs that concrete
types be preferred where they suffice and that no speculative
exploration-wide hierarchy be built. Recorded there as a deliberate
departure from the plan sketch.

``CharacterCreationError`` is deliberately **not** reused: it is scoped
by name to character creation, and its own docstring draws that domain
boundary.

**The three types are not interchangeable**, and the distinctions are the
point:

- :class:`IgnitionNotDefinedError` — RC supplies **no** ignition
  procedure for what was asked;
- :class:`IgnitionAttemptLimitError` — RC supplies the procedure and
  **forbids using it twice** in one round;
- :class:`LanternRefuelNotDefinedError` — a **valid lantern**, but RC
  supplies **no** partial-refill procedure.

A same-round violation must never claim the rule is undefined, and a
refusal for want of a stated procedure must never be reported as a
structural ``ValueError``.

**The converse also holds, and is the point of the 2026-10-03
adjudication:** an invalid *argument* must never be reported as a source
silence. Passing a non-lantern to ``refuel_lantern`` is an invalid
argument to a lantern operation and raises ``ValueError``; it does not
mean RC failed to define how to refuel a torch. The full taxonomy is:

```text
IgnitionNotDefinedError        RC supplies no ignition procedure
LanternRefuelNotDefinedError   valid lantern, but RC supplies no
                               partial-refill procedure
IgnitionAttemptLimitError      RC explicitly forbids another ignition
                               attempt this round
ValueError                     malformed / invalid API input, including a
                               non-lantern supplied to refuel_lantern()
```

These three types are **concrete siblings of ``Exception``**, not
subclasses of ``ValueError``. A caller catching ``ValueError`` therefore
does **not** catch a source silence, which is what keeps the structural
and rules-domain categories genuinely separate rather than nominally so.
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

    **Never raised for a same-round violation.** That is
    :class:`IgnitionAttemptLimitError`, and conflating the two would make
    this error assert something false — that RC defines no procedure,
    when in fact RC defines one and limits how often it may be attempted.
    """


class IgnitionAttemptLimitError(Exception):
    """A second ignition attempt was made in the same round.

    EXP-006 Rule Card §5.1, CLUSTER-004 Slice C. RC p. 70 is explicit:
    *"Someone with a tinderbox may try to use it **once per round**."*

    **This is a rules rejection, not a structural one.** The caller's
    inputs are all well-formed; what the request violates is an
    RC-explicit limit. It therefore carries a domain error rather than
    the plain ``ValueError`` this package raises for a non-``int``, a
    ``bool`` masquerading as one, or a negative count.

    *(Corrected 2026-10-01. Slice C first raised a plain ``ValueError``
    here and this module's own docstring claimed "the rules are not what
    reject it" — which was wrong: RC's once-per-round rule is exactly
    what rejects it. The two categories were never conflated with each
    other, but this one was mis-filed as structural.)*

    Raised **before** the ignition matrix is consulted (Rule Card §5.1),
    so a second attempt at an RC-silent combination reports the attempt
    limit rather than the source silence — the round is already spent
    either way, and the combination is never reached (approved case
    `L19`).

    The flag itself being a non-``bool`` remains a structural violation
    and still raises ``ValueError``: that is a malformed input, not a
    rule being broken.
    """


class LanternRefuelNotDefinedError(Exception):
    """A valid lantern, but RC supplies no partial-refill procedure.

    EXP-006 Rule Card §4, CLUSTER-004 Slice D remediation. The card
    establishes supplying a further flask **only for a lantern that has
    reached zero**. This type covers **exactly one** request:

    - a **valid lantern that is not yet expended**. A partly-fuelled
      lantern is a legitimate lantern state, and RC establishes replacing
      the flask after exhaustion while establishing nothing for this: no
      topping up to 24, no adding 24, no partial-flask arithmetic. None
      is invented.

    **A rules-domain rejection, not a structural one** (human
    adjudication 2026-10-01). The input is a well-formed
    :class:`LightSource` in a legitimate state; what is missing is an RC
    procedure. That makes it a source silence of exactly the kind
    :class:`IgnitionNotDefinedError` covers for ignition, and it is given
    its own concrete type rather than being merged with it — the two
    describe different silences, and a caller that catches one should not
    silently catch the other.

    **Scope narrowed 2026-10-03 by human adjudication** (review-#2
    finding `LOW-9`). This type previously also covered a **non-lantern**
    passed to ``refuel_lantern``, which conflated two different
    categories. That case is now a plain ``ValueError``: ``refuel_lantern``
    is a lantern operation, so another source kind is an **invalid
    argument**, not a gap in RC. Reporting it here implied RC had failed
    to define how to refuel a torch, when in truth the operation does not
    apply to that source kind at all and there is no silence to report.

    *(Corrected 2026-10-01. Slice B first raised a plain ``ValueError``
    here. The independent final review declined to adjudicate the
    category, correctly, because the card specifies none; the human
    project owner then ruled it a rules-domain source-silence rejection.)*

    A malformed argument — something that is not a
    :class:`LightSource` at all — remains a structural ``ValueError``.
    """
