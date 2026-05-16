# Validation Checklist

Use this checklist before submitting or sharing the skill artifact.

## Problem and user

- [ ] The problem is clear in one sentence.
- [ ] The target user is named.
- [ ] The task is small enough to test in 30 to 60 minutes.
- [ ] The workflow is for repeated knowledge work, not a one-time answer.

## Inputs

- [ ] Input format is explicit.
- [ ] Mock data exists.
- [ ] No private data is included.
- [ ] No secrets, tokens, passwords, or real API keys are included.

## Outputs

- [ ] Output format is explicit.
- [ ] The output is useful to a non-developer.
- [ ] Draft outputs are clearly marked as drafts when review is needed.
- [ ] The result JSON records status, outputs, warnings, metrics, and next improvements.

## Workflow

- [ ] YAML is runtime-independent.
- [ ] Steps are written in plain language.
- [ ] Each step has input and output.
- [ ] Human approval points are included.
- [ ] External services are not required for the first test.

## Safety

- [ ] The workflow uses mock data only.
- [ ] Destructive actions are not allowed.
- [ ] Publishing, sending messages, or changing systems requires human approval.
- [ ] Professional decisions such as medical, legal, or financial advice are avoided or clearly limited to mock education examples.

## Skillathon readiness

- [ ] `README.md` explains the project in beginner-friendly language.
- [ ] `SKILL.md` explains when and how to use the skill.
- [ ] At least one complete example has `intent.md`, `workflow.yaml`, and `result.json`.
- [ ] Templates are included.
- [ ] Limitations and next improvements are documented.
- [ ] The submission can be explained in three sentences.
