# Agent Monitoring Output

## Overall status

Three mock agents were checked.

- Success: 1
- Warning: 1
- Failed: 1
- Human review required: yes

## Agent status table

| Agent | Owner | Status | Last run | Duration | Outputs | Notes |
| --- | --- | --- | --- | ---: | ---: | --- |
| `agent-news-digest` | `ops-team@example.com` | success | 2026-05-16 08:30 KST | 42s | 3 | No warnings |
| `agent-review-summarizer` | `product-team@example.com` | warning | 2026-05-16 08:45 KST | 91s | 1 | Input contained 2 empty review rows |
| `agent-meeting-actions` | `education-team@example.com` | failed | 2026-05-16 09:00 KST | 13s | 0 | Meeting notes file was missing |

## Recommended follow-up

1. Review `agent-review-summarizer` input data and decide whether empty review rows should be ignored or fixed at the source.
2. Check the expected meeting notes path for `agent-meeting-actions`.
3. Re-run the failed workflow only after a human confirms the input file is available.
4. Do not send alerts, restart agents, or change schedules without explicit approval.

## Human review needed

- Confirm whether the warning requires a ticket.
- Confirm the owner for the failed meeting-notes workflow.
- Approve any real alert or system action.

## Notes

- This report uses mock agent status data only.
- No agent was restarted.
- No external notification was sent.
