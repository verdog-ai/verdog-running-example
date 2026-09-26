from typing import Final
from verdog_runtime.declarations import EdgeDefinition, NumericalConditionObservation, NumericalFeatureCondition
from demo.countdown.subroutines.main import EDGE_IDS, NODE_IDS, FEATURE_IDS
from demo.countdown.subroutines.main import Output as GraphOutput
from demo.countdown.subroutines.main.nodes.check_counter import Output as SourceOutput

def check_exit_output(value: SourceOutput, /) -> GraphOutput:
    return value

EDGE: Final[EdgeDefinition] = EdgeDefinition(id=EDGE_IDS.check_counter__exit, source=NODE_IDS.check_counter, target=NODE_IDS.exit, name='check counter to exit', conditions=(NumericalFeatureCondition(feature_id=FEATURE_IDS.counter, observation=NumericalConditionObservation.EQUAL_ZERO),), effects=(), visit=None)
