"""Initialize the routing feature from the input count."""

from verdog_runtime.declarations import FeatureSuccess

from demo.countdown.subroutines.main.features.counter import FEATURE as COUNTER
from . import Context, Input, Result, State


def visit_impl(input: Input, state: State, context: Context, /) -> Result:
    return FeatureSuccess(state=state.replace(COUNTER, input.value))
