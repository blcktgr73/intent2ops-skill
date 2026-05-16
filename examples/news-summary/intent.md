# Intent: News Summary to Social Drafts

## Problem

Collecting articles, summarizing them, and drafting social posts is repetitive. Beginners need a safe example that uses mock articles instead of live web data.

## User

A community manager who wants to prepare weekly AI-learning updates.

## Goal

Create a short digest and draft social posts from mock article data.

## Input

- `mock-data/articles.json`

## Output

- A three-bullet article digest
- Two draft social posts
- A list of items that need human review before publishing

## Constraints

- Use mock data only.
- Do not browse the web.
- Do not publish anything automatically.
- Keep summaries short and beginner friendly.

## Human approval points

- Review all article summaries.
- Review social post tone.
- Approve before publishing anywhere.

## Success criteria

- Each article has a one-sentence summary.
- Draft posts are clearly marked as drafts.
- No external service is called.

## Next improvement

- Add a channel-specific style guide for LinkedIn, X, or a community newsletter.
