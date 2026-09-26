from dataclasses import dataclass
from demo.countdown.subroutines.main import Output as SubroutineOutput

@dataclass(frozen=True, slots=True, kw_only=True)
class State:
    pass

Output = SubroutineOutput
