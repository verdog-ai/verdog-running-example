from typing import Final
from verdog_runtime.declarations import EdgeDefinition, NumericalEffectObservation, NumericalFeatureEffect
from demo.countdown.subroutines.main import EDGE_IDS, NODE_IDS, FEATURE_IDS
from demo.countdown.subroutines.main.nodes.check_counter.visit.update_counter__check_counter import VISIT

EDGE: Final[EdgeDefinition] = EdgeDefinition(id=EDGE_IDS.update_counter__check_counter, source=NODE_IDS.update_counter, target=NODE_IDS.check_counter, name='update counter to check counter', conditions=(), effects=(NumericalFeatureEffect(feature_id=FEATURE_IDS.counter, observation=NumericalEffectObservation.DECREASES),), visit=VISIT)
