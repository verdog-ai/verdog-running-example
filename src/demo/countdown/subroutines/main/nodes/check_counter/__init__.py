from typing import Final
from verdog_runtime.declarations import NodeDefinition, Python
from demo.countdown.subroutines.main import NODE_IDS, StateScope
from .impl import Output as Output, State

NODE: Final[NodeDefinition[State, StateScope]] = NodeDefinition(id=NODE_IDS.check_counter, name='Check counter', state_type=State, operation=Python())
