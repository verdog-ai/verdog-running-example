from typing import Final
from demo.countdown.workflows.main.profiles import INVOKERS
from verdog_runtime.declarations import WorkflowConfiguration

CONFIGURATION: Final[WorkflowConfiguration] = WorkflowConfiguration(profile_arguments=INVOKERS)
