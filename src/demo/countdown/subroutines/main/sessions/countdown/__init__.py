from typing import Final
from verdog_runtime.declarations import AgentSessionDefinition
from demo.countdown.subroutines.main import SESSION_IDS

SESSION: Final[AgentSessionDefinition] = AgentSessionDefinition(id=SESSION_IDS.countdown, name='Countdown', persistent=True)
