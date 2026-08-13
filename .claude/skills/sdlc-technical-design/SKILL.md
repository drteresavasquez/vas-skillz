---
name: sdlc-technical-design
description: Adds technical design, impacted-app-area analysis, and required test coverage to a ticket as an annotation. Use when a ticket moves from Backlog to Todo, or when the user asks to start design on a specific issue — this is the Todo-entry gate, and it never overwrites the existing ticket body.
---

# SDLC Technical Design

## When to use this skill

Trigger when the user tells you a ticket is moving from Backlog to Todo (by
name, e.g. "move #123 to Todo", or by intent, e.g. "let's design #123 before
we start it"). This is the Todo-entry gate: a ticket shouldn't sit in Todo
without a technical design, an impact analysis, and a test-coverage
requirement attached.

## Instructions

1. Read `../../sdlc-spec.md` for the ticket hierarchy, the `Status` field,
   the acceptance-criteria format, and the Points/estimate scale before
   proceeding — never hardcode these.
2. Fetch the ticket with `gh issue view <number> --json body,title,labels`.
   Read its acceptance criteria and, if it's a Task, fetch its parent
   Feature/Epic for context (the parent is discoverable via GitHub's native
   sub-issue relationship, not a body-text link — check the issue's parent
   via `gh api repos/<OWNER>/<REPO>/issues/<number>` or the issue's sidebar
   data if the CLI surfaces it).
3. Draft three things, using `assets/annotation-template.md` as the shape:
   - **Technical design** — the approach, key decisions, and anything
     explicitly ruled out and why.
   - **Impacted parts of the app** — files, modules, services, or
     user-facing surfaces this ticket will touch.
   - **Required test coverage** — what must be tested (and at what level:
     unit/integration/e2e) for this ticket's acceptance criteria to be
     considered verifiably met. `sdlc-review-gate` checks the eventual PR
     against exactly this list, so be concrete and enumerable, not vague.
   See `references/design-annotation-format.md` if you need the full
   structure or an example.
4. Show the drafted annotation to the user before posting anything.
5. Once approved, **append** it to the ticket — never overwrite the
   existing body. Use `gh issue comment <number> --body-file <file>`
   (preferred — keeps the annotation as its own comment, existing body
   untouched) rather than `gh issue edit`, which replaces the body. If the
   user specifically wants it inline in the body instead of a comment,
   append a new section to the fetched body text and write the *combined*
   result back — never drop or rewrite existing content.
6. If the user confirms the ticket should now move to Todo, set the
   `Status` Project field to `Todo` per the spec (`gh project item-edit`).
   Do not change `Status` unless the user confirms — this skill's job is to
   produce the design annotation; the status move is a separate, explicit
   step.
