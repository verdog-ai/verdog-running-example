"""Exercise the complete graph without contacting a model provider."""

from dataclasses import replace
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from verdog_runtime.declarations import AgentAccess, WorkflowConfiguration
from verdog_runtime.declarations.agents import AgentReply, AgentRequest
from verdog_runtime.declarations.ids import AgentProfileId, ProviderSessionId
from verdog_runtime.interpreter import Dispatcher

from demo.countdown.subroutines.main.impl import Count
from demo.countdown.workflows.main import definition


class Decrementer:
    session_provider = "test"

    def __init__(self, decrement: int = 1) -> None:
        self.decrement = decrement
        self.values: list[int] = []

    def __call__(self, request: AgentRequest, /) -> AgentReply:
        value = int(request.prompt.split()[-1].rstrip("."))
        self.values.append(value)
        assert request.access == AgentAccess.READ_ONLY
        if len(self.values) > 1:
            assert request.provider_session_id == ProviderSessionId("countdown")
        return AgentReply(
            text=str(value - self.decrement),
            provider_session_id=ProviderSessionId("countdown"),
        )


class CountdownTest(unittest.TestCase):
    def test_countdown(self) -> None:
        for start in (0, 3, 10):
            with self.subTest(start=start), TemporaryDirectory() as output:
                agent = Decrementer()
                workflow = replace(
                    definition(),
                    configuration=WorkflowConfiguration(
                        profile_arguments={AgentProfileId("decrementer"): agent}
                    ),
                )
                result = Dispatcher(project_root=Path(__file__).resolve().parents[1]).run(
                    workflow, Count(value=start), output_dir=Path(output)
                )
                self.assertEqual(result.output, Count(value=0))
                self.assertEqual(agent.values, list(range(start, 0, -1)))

    def test_wrong_proposal_fails(self) -> None:
        with TemporaryDirectory() as output:
            workflow = replace(
                definition(),
                configuration=WorkflowConfiguration(
                    profile_arguments={AgentProfileId("decrementer"): Decrementer(0)}
                ),
            )
            with self.assertRaisesRegex(ValueError, "exactly one lower"):
                Dispatcher(project_root=Path(__file__).resolve().parents[1]).run(
                    workflow, Count(value=3), output_dir=Path(output)
                )

    def test_input_default_and_domain(self) -> None:
        self.assertEqual(Count().value, 10)
        with self.assertRaisesRegex(ValueError, "non-negative"):
            Count(value=-1)


if __name__ == "__main__":
    unittest.main()
