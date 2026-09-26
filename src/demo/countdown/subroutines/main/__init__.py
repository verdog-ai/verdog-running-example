from __future__ import annotations
from dataclasses import dataclass
from functools import cache
from typing import Final, Literal
from verdog_runtime.declarations.ids import EdgeId, GraphId, NodeId, FeatureId, AgentProfileId, AgentSessionId
from verdog_runtime.declarations import GraphDefinition, SubroutineDefinition
from .impl import Input, Output, Params

GRAPH_ID: Final[GraphId] = GraphId('demo.countdown.main')
type StateScope = Literal['demo.countdown.main']

@dataclass(frozen=True, slots=True, kw_only=True)
class NodeIdentifiers:
    check_counter: NodeId
    decrement: NodeId
    enter: NodeId
    exit: NodeId
    failure: NodeId
    initialize_counter: NodeId
    update_counter: NodeId

NODE_IDS: Final[NodeIdentifiers] = NodeIdentifiers(check_counter=NodeId('check_counter'), decrement=NodeId('decrement'), enter=NodeId('enter'), exit=NodeId('exit'), failure=NodeId('failure'), initialize_counter=NodeId('initialize_counter'), update_counter=NodeId('update_counter'))

@dataclass(frozen=True, slots=True, kw_only=True)
class EdgeIdentifiers:
    check_counter__decrement: EdgeId
    check_counter__exit: EdgeId
    decrement__update_counter: EdgeId
    enter__initialize_counter: EdgeId
    initialize_counter__check_counter: EdgeId
    update_counter__check_counter: EdgeId

EDGE_IDS: Final[EdgeIdentifiers] = EdgeIdentifiers(check_counter__decrement=EdgeId('check_counter__decrement'), check_counter__exit=EdgeId('check_counter__exit'), decrement__update_counter=EdgeId('decrement__update_counter'), enter__initialize_counter=EdgeId('enter__initialize_counter'), initialize_counter__check_counter=EdgeId('initialize_counter__check_counter'), update_counter__check_counter=EdgeId('update_counter__check_counter'))

@dataclass(frozen=True, slots=True, kw_only=True)
class FeatureIdentifiers:
    counter: FeatureId

FEATURE_IDS: Final[FeatureIdentifiers] = FeatureIdentifiers(counter=FeatureId('counter'))

@dataclass(frozen=True, slots=True, kw_only=True)
class AgentProfileIdentifiers:
    decrementer: AgentProfileId

PROFILE_IDS: Final[AgentProfileIdentifiers] = AgentProfileIdentifiers(decrementer=AgentProfileId('decrementer'))

@dataclass(frozen=True, slots=True, kw_only=True)
class AgentSessionIdentifiers:
    countdown: AgentSessionId

SESSION_IDS: Final[AgentSessionIdentifiers] = AgentSessionIdentifiers(countdown=AgentSessionId('countdown'))

@cache
def definition() -> SubroutineDefinition[Input, Output, Params, StateScope]:
    from demo.countdown.subroutines.main.nodes import NODES
    from demo.countdown.subroutines.main.features import FEATURES
    from demo.countdown.subroutines.main.profiles import PROFILES, PROFILE_PARAMETERS
    from demo.countdown.subroutines.main.sessions import SESSIONS, SESSION_PARAMETERS
    from demo.countdown.subroutines.main.nodes.enter import PORT as ENTER
    from demo.countdown.subroutines.main.nodes.exit import PORT as EXIT
    from demo.countdown.subroutines.main.nodes.failure import PORT as FAILURE
    from demo.countdown.subroutines.main.edges import EDGES
    return SubroutineDefinition(graph=GraphDefinition[Input, Output, Params, StateScope](id=GRAPH_ID, params_type=Params, enter=ENTER, exit=EXIT, failure=FAILURE, nodes=NODES, edges=EDGES, features=FEATURES, profiles=PROFILES, profile_parameters=PROFILE_PARAMETERS, sessions=SESSIONS, session_parameters=SESSION_PARAMETERS))
