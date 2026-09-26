from typing import Final
from verdog_runtime.declarations import EdgeDefinition
from demo.countdown.subroutines.main import EDGE_IDS, NODE_IDS
from demo.countdown.subroutines.main.nodes.update_counter.visit.decrement__update_counter import VISIT

EDGE: Final[EdgeDefinition] = EdgeDefinition(id=EDGE_IDS.decrement__update_counter, source=NODE_IDS.decrement, target=NODE_IDS.update_counter, name='decrement to update counter', conditions=(), effects=(), visit=VISIT)
