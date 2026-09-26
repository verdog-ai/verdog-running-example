from typing import Final
from verdog_runtime.declarations import EdgeDefinition
from demo.countdown.subroutines.main import EDGE_IDS, NODE_IDS
from demo.countdown.subroutines.main.nodes.initialize_counter.visit.enter__initialize_counter import VISIT

EDGE: Final[EdgeDefinition] = EdgeDefinition(id=EDGE_IDS.enter__initialize_counter, source=NODE_IDS.enter, target=NODE_IDS.initialize_counter, name='enter to initialize counter', conditions=(), effects=(), visit=VISIT)
