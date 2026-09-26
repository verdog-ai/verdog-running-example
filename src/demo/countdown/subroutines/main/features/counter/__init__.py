from typing import Final
from verdog_runtime.declarations import FeatureDefinition, FeatureKind
from demo.countdown.subroutines.main import FEATURE_IDS, StateScope

FEATURE: Final[FeatureDefinition[int, StateScope]] = FeatureDefinition(id=FEATURE_IDS.counter, label='Counter', description='The current non-negative countdown value', kind=FeatureKind.INTEGER)
