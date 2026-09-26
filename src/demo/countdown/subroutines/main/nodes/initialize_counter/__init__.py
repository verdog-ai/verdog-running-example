from typing import Final
from verdog_runtime.declarations import Feature, FeatureNodeDefinition
from demo.countdown.subroutines.main import NODE_IDS

NODE: Final[FeatureNodeDefinition] = FeatureNodeDefinition(id=NODE_IDS.initialize_counter, name='Initialize counter', operation=Feature())
