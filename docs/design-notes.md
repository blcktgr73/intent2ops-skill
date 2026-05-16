# Design Notes

## Why Markdown, YAML, and JSON?

Markdown is easy for people to read and write. It is a good place to describe intent, context, goals, and constraints.

YAML is useful for operational structure. It can describe steps, inputs, outputs, approval rules, and safety limits without requiring one specific runtime.

JSON is useful for results. It records what happened in a structured way that can later be compared, summarized, or inspected by another tool.

## Why runtime-independent YAML?

The workflow should be understandable before it is automated. A beginner should be able to read the YAML and understand what an AI agent or automation system would do.

The same workflow may later be adapted to:

- Codex
- OpenClaw
- GitHub Actions
- n8n
- Airflow
- Cloud Scheduler
- Another agent runtime

The first version should not depend on any one of these.

## Why mock data first?

Mock data makes the workflow safer and easier to test. It avoids private information, secrets, external permissions, and production mistakes.

After the mock workflow is clear, a future version can define how real data would be connected with approval and security rules.

## Small first version

The first workflow should fit in a 30 to 60 minute exercise. Good first examples have:

- one clear input
- one clear output
- one human review point
- no external login
- no secret value
- no destructive action

## Current limitations

- This repository does not execute workflows.
- The YAML is a design format, not a formal standard.
- The examples use mock data only.
- The result JSON files are example records, not generated logs.

## Future extensions

- Add Korean examples.
- Add a JSON schema for result files.
- Add a YAML schema for workflow files.
- Add a validator script only if repeated manual checking becomes painful.
- Add runtime adapters after the human-readable workflow format is stable.
