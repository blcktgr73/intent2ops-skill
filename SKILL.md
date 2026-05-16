---
name: intent2ops
description: Convert beginner-friendly human intent into a small, safe, runtime-independent agent workflow. Use when a user wants to turn repeated knowledge work into a Codex Skillathon-style artifact with Markdown intent, YAML workflow steps, JSON execution results, mock data, human approval rules, and a validation checklist. Best for non-developers, operators, educators, product managers, and AI beginners who need a reusable workflow design before using real tools or private data.
---

# Intent to Operations

Help the user turn a repeated knowledge-work idea into a small operational workflow.

Use this pattern:

```text
Markdown intent -> YAML workflow -> JSON result
```

## Operating principles

- Start with human intent.
- Keep the first workflow small.
- Use mock data before real data.
- Make each step reviewable by a person.
- Keep YAML runtime-independent.
- Do not include secrets.
- Do not perform destructive actions.
- Ask for approval before external calls, publishing, sending messages, or changing systems.

## Conversation workflow

Guide the user one step at a time.

1. Define the repeated task.
2. Identify the audience and user.
3. Define the input format.
4. Define the desired output format.
5. Create or request mock data.
6. Draft `intent.md`.
7. Draft `workflow.yaml`.
8. Draft `result.json`.
9. Validate the artifact.
10. Suggest one small improvement for the next iteration.

Do not ask for all details at once. Ask short questions, confirm the answer, then move to the next step.

## Required files for a small artifact

Create these files when the user asks for a full starter artifact:

```text
README.md
SKILL.md
templates/intent-template.md
templates/workflow-template.yaml
templates/result-template.json
mock-data/
examples/
docs/validation-checklist.md
docs/design-notes.md
```

## Intent Markdown guidance

An `intent.md` file should answer:

- What repeated task should be improved?
- Who uses the result?
- What input is available?
- What output should be produced?
- What constraints must be respected?
- What requires human approval?
- What does success look like?

Keep intent readable for a beginner.

## Workflow YAML guidance

A `workflow.yaml` file should include:

- `workflow.name`
- `workflow.purpose`
- `workflow.inputs`
- `workflow.steps`
- `workflow.approvals`
- `workflow.outputs`
- `workflow.safety`
- `workflow.metrics`

Each step should include:

- `id`
- `name`
- `action`
- `input`
- `output`
- `requires_approval`

Keep the YAML runtime-independent. Do not assume GitHub Actions, n8n, Airflow, or any one tool.

## Result JSON guidance

A `result.json` file should record:

- status
- started and completed timestamps if known
- inputs used
- steps completed
- outputs created
- approval decisions
- warnings
- metrics
- next improvements

The result is a reflection record, not only a success message.

## Safety rules

Never ask the user to paste secrets or private data into mock data.

Use placeholders for sensitive fields:

```text
example@example.com
REDACTED
MOCK_TOKEN_DO_NOT_USE
```

Before any real-world action, ask for explicit approval:

- sending email
- posting to social media
- creating issues or pull requests
- editing files outside the working artifact
- calling external APIs
- changing production systems

## Validation

Before finishing, check:

- The problem is clear in one sentence.
- Input and output formats are explicit.
- Mock data exists.
- The workflow has human approval points.
- The result JSON records status, outputs, warnings, and next improvements.
- No secrets or private data are present.
- The artifact is useful without running code.

Use `docs/validation-checklist.md` when present.
