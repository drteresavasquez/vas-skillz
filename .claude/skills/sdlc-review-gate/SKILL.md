---
name: sdlc-review-gate
description: Checks a PR's diff against its ticket's acceptance criteria and required test coverage, runs a Definition-of-Done checklist, and drafts a release-note fragment. Use when a PR moves to In Review or is proposed as ready to merge — this is the exit gate before Done, the counterpart to sdlc-technical-design's Todo-entry gate.
---

# SDLC Review Gate

## When to use this skill

Trigger when the user asks you to check whether a PR is ready to merge,
review a PR against its ticket, or run the exit gate — including when a
ticket/PR is described as moving into In Review. This is the gate that sits
before merge — the counterpart to `sdlc-technical-design`, which gates
entry into Todo.

## Instructions

1. Read `../../sdlc-spec.md` for the acceptance-criteria format and the
   `Status` field before proceeding — never hardcode these.
2. Fetch the PR diff with `gh pr diff <number>` and the PR's metadata with
   `gh pr view <number> --json title,body,url`.
3. Identify the linked ticket (from the PR body or branch name) and fetch it
   with `gh issue view <ticket_number> --json body,comments`. Pull out:
   - Its acceptance criteria (spec format).
   - The "Required test coverage" list added by `sdlc-technical-design`, if
     present in the ticket's comments or body.
4. Check the diff against each AC item: does the change plausibly satisfy
   it? Flag any AC item the diff doesn't appear to address.
5. Confirm each item in the required test coverage list actually has a
   corresponding test in the diff. Flag any that are missing. If no
   technical-design annotation exists on the ticket at all, say so
   explicitly rather than silently skipping this check — that's a gap in
   the process, not a pass.
6. Run the Definition-of-Done checklist in `references/dod-checklist.md`
   against the PR.
7. Draft a one-paragraph (or short-bullet) release-note fragment
   summarizing the user-facing effect of this change.
8. Assemble the findings using `assets/review-comment-template.md` — AC
   status, test-coverage status, DoD checklist results, release-note
   fragment. Show this to the user first.
9. Only after the user confirms, post it with `gh pr comment <number>
   --body-file <file>`. Do not merge, approve, or request changes on the PR,
   and do not change the ticket's `Status` field — this skill produces a
   review comment and a release-note fragment, not a merge decision or a
   status transition.
