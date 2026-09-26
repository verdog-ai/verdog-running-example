from typing import Final
from verdog_runtime.declarations import NodeDefinition, Agent
from demo.countdown.subroutines.main import NODE_IDS, StateScope, PROFILE_IDS, SESSION_IDS
from .impl import Output as Output, State

NODE: Final[NodeDefinition[State, StateScope]] = NodeDefinition(id=NODE_IDS.decrement, name='Decrement', state_type=State, operation=Agent(profile=PROFILE_IDS.decrementer, session=SESSION_IDS.countdown))
