from __future__ import annotations
from dataclasses import dataclass
from functools import cache
from typing import Final
from .bindings import CONFIGURATION
from .sessions import SESSIONS
from verdog_runtime.declarations import ParameterType, SubroutineCall, WorkflowConfiguration, WorkflowDefinition
from verdog_runtime.declarations.ids import GraphId, AgentProfileId
from demo.countdown.subroutines.main import GRAPH_ID as ENTRY_GRAPH_ID, Input, Output, Params, StateScope

PARAMS_TYPES: Final[dict[tuple[str, GraphId], ParameterType]] = {('.', ENTRY_GRAPH_ID): Params}

@dataclass(frozen=True, slots=True, kw_only=True)
class RuntimeOptions:
    pass

def configure(options: RuntimeOptions, /) -> WorkflowConfiguration:
    return CONFIGURATION

GRAPH_ID: Final[GraphId] = GraphId('demo.countdown.main')
ENTRY: Final[SubroutineCall] = SubroutineCall(definition_id=ENTRY_GRAPH_ID, definition_module='demo.countdown.subroutines.main', project_path='.', params_types=PARAMS_TYPES, profile_arguments={AgentProfileId('decrementer'): AgentProfileId('decrementer')}, session_arguments={})

@cache
def definition() -> WorkflowDefinition[Input, Output, Params, StateScope]:
    return WorkflowDefinition(id=GRAPH_ID, input_type=Input, entry=ENTRY, sessions=SESSIONS, configuration=CONFIGURATION)
