from typing import Final
from demo.countdown.subroutines.main.nodes.check_counter import NODE as CHECK_COUNTER_NODE
from demo.countdown.subroutines.main.nodes.decrement import NODE as DECREMENT_NODE
from demo.countdown.subroutines.main.nodes.initialize_counter import NODE as INITIALIZE_COUNTER_NODE
from demo.countdown.subroutines.main.nodes.update_counter import NODE as UPDATE_COUNTER_NODE

NODES: Final = (CHECK_COUNTER_NODE, DECREMENT_NODE, INITIALIZE_COUNTER_NODE, UPDATE_COUNTER_NODE)
