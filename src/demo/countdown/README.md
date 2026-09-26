# Countdown

An agent proposes one decrement at a time. The workflow accepts only the
immediately preceding integer, updates a non-negative integer feature, and
returns when it reaches zero.

- Input: `Count(value=10)` by default; any non-negative integer is accepted.
- Output: `Count(value=0)` on success.
- Provider: an installed and authenticated Codex CLI, configured by the workflow's
  `decrementer` profile. Zero input needs no provider call.
- Failure: a malformed or incorrect proposal raises an exception.

Run `verdog sync`, then `verdog run main -- --input.value 1` for one agent invocation.
The repository README contains the complete setup and account-free tests.
