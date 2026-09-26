from typing import Final
from demo.countdown.subroutines.main.nodes.decrement import Output as Input
from verdog_runtime.declarations import VisitDefinition, FeatureState, FeatureSuccess, NodeContext
from demo.countdown.subroutines.main import Params
from demo.countdown.subroutines.main import StateScope

State = FeatureState[StateScope]
Context = NodeContext[Params]
Result = FeatureSuccess[StateScope]

def visit(input: Input, state: State, context: Context, /) -> Result:
    from .impl import visit_impl
    return visit_impl(input, state, context)

VISIT: Final[VisitDefinition] = VisitDefinition(implementation=visit)
