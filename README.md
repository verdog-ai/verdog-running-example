# Countdown

The runnable example from the [Verdog guide](https://drexlerd.github.io/verdog-website/running-example.html).
An agent proposes the integer before the current count. Python validates each
proposal, and a decreasing integer feature controls the loop until it reaches zero.

## Try it

Requires Python 3.12+, Git, and [uv](https://docs.astral.sh/uv/getting-started/installation/).

```sh
uv tool install verdog-cli
git clone https://github.com/verdog-ai/verdog-running-example.git
cd verdog-running-example
verdog sync
verdog check
verdog run main -- --input.value 0
```

This first run returns `Count(value=0)` without a model account or provider call.
`verdog sync` prepares the editor and workflow environments; there is no manual
venv activation or separate dependency installation.

For the agent loop, install and sign in to the [Codex CLI](https://learn.chatgpt.com/docs/codex/cli#get-started-with-codex-cli), then run:

```sh
verdog run main -- --input.value 1
```

This makes one agent invocation and returns `Count(value=0)`. Run `verdog run` for
the default countdown from 10, or change `--input.value` to another non-negative
integer. Each decrement invokes Codex once and uses the provider's quota
or billing. Invalid replies fail immediately; this example has no repair loop.
The `--` separates Verdog options from the workflow's typed arguments.

Open this directory in VS Code with the **Verdog** extension installed. Choose
**Verdog: Show Canvas** to inspect the graph or **Verdog: Run Workflow** to run the
default countdown. No Verdog sign-in is needed to edit, check, or run this example.

## What to edit

- `project.json`: graph, conditions, effects, and provider configuration; the canvas edits this file.
- `src/demo/countdown/subroutines/main/impl.py`: the `Count` input/output type and its default value.
- `src/demo/countdown/subroutines/main/nodes/decrement/visit/check_counter__decrement/prompt.md.j2`: the agent prompt.
- Each node's `visit/<edge>/impl.py`: its Python behavior.

After graph edits made outside the canvas, run `verdog generate`. After changing
workflow dependencies, run `verdog sync`. Run `verdog check` to validate the result.
Generated `__init__.py` files and `pyproject.toml` are maintained by Verdog.

The graph initializes `counter`, checks whether it is zero, asks the agent for a
proposal, validates `next == current - 1`, and updates `counter`. `verdog analyze`
certifies the graph's decreasing-feature loop. That certificate does not guarantee
that Python code or a provider request returns.

## Test without a model account

```sh
.verdog/environments/main/bin/python -m unittest discover -s tests -v
```

On Windows, use `.verdog/environments/main/Scripts/python.exe` instead. These tests
run the same graph with a deterministic test provider, check session reuse and
countdowns from 0, 3, and 10, and verify that an incorrect proposal is rejected.

Runs are stored under `.verdog/runs/main/` and appear in VS Code's **Runs** view.
They are ignored by Git.
