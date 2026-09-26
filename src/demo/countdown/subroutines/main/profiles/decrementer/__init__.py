from typing import Final
from verdog_runtime.declarations import AgentProfileParameter
from demo.countdown.subroutines.main import PROFILE_IDS
from demo.countdown.workflows.main.profiles.decrementer import INVOKER as WORKFLOW_MAIN__DECREMENTER_INVOKER

PROFILE_PARAMETER: Final[AgentProfileParameter] = AgentProfileParameter(id=PROFILE_IDS.decrementer, name='Decrementer')
RESOLVED_INVOKERS: Final = (WORKFLOW_MAIN__DECREMENTER_INVOKER,)
