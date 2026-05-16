# Intent: Agent Operation Monitoring Report

## Problem

When several AI agents run repeated tasks, operators need a simple status report that highlights failures, warnings, and next actions.

## User

An operations lead who reviews mock AI-agent runs each morning.

## Goal

Create a short monitoring report from mock agent status data.

## Input

- `mock-data/agent-status.json`

## Output

- Overall status summary
- Failed or warning agents
- Recommended human follow-up actions
- Metrics for completed, warning, and failed agents

## Constraints

- Use mock data only.
- Do not restart agents.
- Do not send alerts automatically.
- Do not change any real system.

## Human approval points

- Confirm whether a warning needs follow-up.
- Approve any real alert or system action.

## Success criteria

- Failed agents are easy to see.
- Warnings are not treated as full failures.
- Next actions are written in plain language.

## Next improvement

- Add severity levels and owner-specific notification rules.
