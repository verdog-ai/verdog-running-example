"""The agent returns a count and retains its number of proposals."""

from dataclasses import dataclass

from demo.countdown.subroutines.main.impl import Count


@dataclass(frozen=True, slots=True, kw_only=True)
class State:
    attempts: int = 0


Output = Count
