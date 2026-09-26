from typing import Final
from verdog_runtime.declarations import PortDefinition
from demo.countdown.subroutines.main import NODE_IDS

PORT: Final[PortDefinition] = PortDefinition(id=NODE_IDS.failure)
