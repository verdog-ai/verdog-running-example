"""Input and output for the Countdown workflow."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True, kw_only=True)
class Count:
    """A non-negative countdown value; defaults support one-click execution."""

    value: int = 10

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("the countdown value must be non-negative")


@dataclass(frozen=True, slots=True, kw_only=True)
class Params:
    pass


Input = Count
Output = Count
