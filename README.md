# intent2ops-skill

Turn human intent into an operational workflow.

This repository is a Codex Skillathon learning artifact for non-developers. It shows a small, repeatable pattern:

```text
Markdown intent -> YAML workflow -> JSON result
```

The goal is not to build a production automation system. The goal is to make repeated knowledge work clear enough that another person or AI agent can understand, review, and improve it.

## Who this is for

- Non-developers
- Product managers
- Operators
- Educators
- AI beginners
- People who want safer, repeatable AI-agent workflows

## Core idea

- `intent.md` is for people. It explains the goal, context, inputs, constraints, and review rules.
- `workflow.yaml` is for operation. It breaks the intent into runtime-independent steps.
- `result.json` is for reflection. It records what happened, what was produced, and what should improve next.

The YAML is not tied to GitHub Actions. It may later be adapted to Codex, OpenClaw, GitHub Actions, n8n, Airflow, Cloud Scheduler, or another runtime.

## Repository map

```text
intent2ops-skill/
├── README.md
├── SKILL.md
├── examples/
│   ├── news-summary/
│   │   ├── intent.md
│   │   ├── workflow.yaml
│   │   └── result.json
│   ├── agent-monitoring/
│   │   ├── intent.md
│   │   ├── workflow.yaml
│   │   └── result.json
│   └── meeting-to-actions/
│       ├── intent.md
│       ├── workflow.yaml
│       └── result.json
├── templates/
│   ├── intent-template.md
│   ├── workflow-template.yaml
│   └── result-template.json
├── mock-data/
│   ├── articles.json
│   ├── agent-status.json
│   └── meeting-notes.md
└── docs/
    ├── validation-checklist.md
    └── design-notes.md
```

## How to use this artifact

1. Choose one repeated knowledge-work task.
2. Write the human goal in `intent.md`.
3. Convert the goal into clear steps in `workflow.yaml`.
4. Use mock data first. Do not use secrets or private data.
5. Record an example outcome in `result.json`.
6. Check the workflow with `docs/validation-checklist.md`.
7. Improve the intent, workflow, or result format after each run.

## Included examples

- `examples/news-summary`: collect mock articles, summarize them, and draft social posts.
- `examples/agent-monitoring`: review mock agent status and write an operations report.
- `examples/meeting-to-actions`: turn mock meeting notes into action items.

## Safety rules

- Use mock data only.
- Do not include secrets, tokens, passwords, or private user data.
- Do not run destructive actions.
- Ask for human approval before publishing, sending messages, changing systems, or using external services.
- Keep each first version small enough to test in 30 to 60 minutes.

## Skillathon submission summary

This project helps beginners turn a repeated task idea into a reusable AI-agent workflow. It uses Markdown for human intent, YAML for operational steps, and JSON for execution results. The examples use mock data only, so participants can learn the structure safely before connecting real tools.
