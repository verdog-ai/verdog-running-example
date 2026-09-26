"""Ask the configured agent for one decrement."""

from pathlib import Path

from jinja2 import StrictUndefined, Template
from verdog_runtime.declarations import AgentAccess, Success

from . import Context, Input, Output, Result, State


def visit_impl(input: Input, state: State, context: Context, /) -> Result:
    template = Template(
        Path(__file__).with_name("prompt.md.j2").read_text(encoding="utf-8"),
        undefined=StrictUndefined,
    )
    reply = context.invoke(
        template.render(value=input.value),
        workspace=context.output_dir,
        access=AgentAccess.READ_ONLY,
    )
    return Success(
        output=Output(value=int(reply.strip())),
        state=State(attempts=state.attempts + 1),
    )
