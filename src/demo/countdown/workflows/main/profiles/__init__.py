from typing import Final
from verdog_runtime.declarations import AgentInvoker
from verdog_runtime.declarations.ids import AgentProfileId
from demo.countdown.workflows.main.profiles.decrementer import INVOKER as DECREMENTER_INVOKER

INVOKERS: Final[dict[AgentProfileId, AgentInvoker]] = {AgentProfileId('decrementer'): DECREMENTER_INVOKER}
