from typing import Final
from demo.countdown.subroutines.main.nodes.decrement import Output as Input
from verdog_runtime.declarations import VisitDefinition, NodeContext, Success
from demo.countdown.subroutines.main import Params
from demo.countdown.subroutines.main.nodes.check_counter import Output, State

Context = NodeContext[Params]
Result = Success[Output, State]

def visit(input: Input, state: State, context: Context, /) -> Result:
    from .impl import visit_impl
    return visit_impl(input, state, context)

VISIT: Final[VisitDefinition] = VisitDefinition(implementation=visit)
