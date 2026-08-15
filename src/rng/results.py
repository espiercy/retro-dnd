"""The rich, immutable roll-result value type.

See docs/technical/RNG_CONTRACT.md §5.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class RollResult:
    """The result of one public, rules-visible RNG operation.

    Fields match RNG_CONTRACT.md §5. ``total`` is always derived from
    ``dice`` and ``modifier`` — it is not an independent constructor
    argument, so a RollResult can never represent an internally
    inconsistent total.

    Deliberately excluded (RNG_CONTRACT.md §5): timestamps, the identity of
    the calling rules procedure, campaign/character identifiers, and
    narrative text. Those are rules-procedure or event-layer concerns, not
    RNG concerns.
    """

    expression: str
    dice: tuple[int, ...]
    die_size: int
    modifier: int
    sequence_number: int
    total: int = field(init=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "total", sum(self.dice) + self.modifier)
