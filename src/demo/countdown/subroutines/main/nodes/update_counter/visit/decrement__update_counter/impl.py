"""Accept only the immediately preceding integer."""

from verdog_runtime.declarations import FeatureSuccess

from demo.countdown.subroutines.main.features.counter import FEATURE as COUNTER
from . import Context, Input, Result, State


def visit_impl(input: Input, state: State, context: Context, /) -> Result:
    current = state.get(COUNTER)
    if current is None:
        raise ValueError("counter is uninitialized")
    if input.value != current - 1:
        raise ValueError("the proposed counter must be exactly one lower")
    return FeatureSuccess(state=state.replace(COUNTER, input.value))
