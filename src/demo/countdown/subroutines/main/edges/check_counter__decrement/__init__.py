from typing import Final
from verdog_runtime.declarations import EdgeDefinition, NumericalConditionObservation, NumericalFeatureCondition
from demo.countdown.subroutines.main import EDGE_IDS, NODE_IDS, FEATURE_IDS
from demo.countdown.subroutines.main.nodes.decrement.visit.check_counter__decrement import VISIT

EDGE: Final[EdgeDefinition] = EdgeDefinition(id=EDGE_IDS.check_counter__decrement, source=NODE_IDS.check_counter, target=NODE_IDS.decrement, name='check counter to decrement', conditions=(NumericalFeatureCondition(feature_id=FEATURE_IDS.counter, observation=NumericalConditionObservation.GREATER_ZERO),), effects=(), visit=VISIT)
