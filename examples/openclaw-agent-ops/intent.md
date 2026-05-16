# Intent: OpenClaw Agent Operations Review

## Problem

OpenClaw agents can perform repeated operational work, but the operator needs a clear daily review process for status, security posture, risky permissions, and human approval points.

## User

An operator who manages several OpenClaw agents and wants a safe, repeatable review workflow.

## Goal

Create a daily operations review that classifies agent health, flags security risks, identifies blocked agents, and recommends human-reviewed follow-up actions.

## Input

- `mock-data/openclaw-agent-ops.json`

## Output

- Agent health summary
- Security and permission review
- Blocked or review-required agents
- Recommended follow-up actions
- Human approval checklist
- Machine-friendly result record

## Constraints

- Use mock data only.
- Do not connect to a real OpenClaw environment.
- Do not restart agents.
- Do not rotate secrets.
- Do not publish reports or send alerts automatically.
- Any network access, external write permission, restart permission, or secret marker requires human review.

## Human approval points

- Approve any restart.
- Approve schedule changes.
- Approve external publishing.
- Approve secret rotation or credential cleanup.
- Confirm whether warning agents require tickets.

## Success criteria

- Each agent is classified as healthy, warning, review required, or blocked.
- Security risks are separated from normal status warnings.
- Follow-up actions are written in plain language.
- No real external action is taken.

## Next improvement

- Add severity levels and owner-specific escalation rules after the mock review process is stable.
