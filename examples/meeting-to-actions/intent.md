# Intent: Meeting Notes to Action Items

## Problem

Meeting notes often contain decisions, open questions, and follow-up tasks. A simple workflow can turn notes into clear action items without using private meeting data.

## User

A facilitator who wants to summarize a Skillathon planning meeting.

## Goal

Create action items, decisions, and open questions from mock meeting notes.

## Input

- `mock-data/meeting-notes.md`

## Output

- Action item list
- Decision list
- Open question list
- Items that need human confirmation

## Constraints

- Use mock meeting notes only.
- Do not assign real people without review.
- Do not send messages or calendar invites.

## Human approval points

- Confirm owners and due dates.
- Approve any message sent to participants.

## Success criteria

- Decisions and open questions are separated.
- Action items are short and clear.
- Ambiguous owners or dates are marked for review.

## Next improvement

- Add a due-date suggestion rule.
