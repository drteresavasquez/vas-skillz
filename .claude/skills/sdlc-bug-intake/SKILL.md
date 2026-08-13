---
name: sdlc-bug-intake
description: Front door for bugs that don't enter through an epic — gathers repro steps and severity, links impacted tickets/areas via the spec's dependency convention, and proposes a ticket. Use when the user reports or describes a bug and wants it turned into a ticket, as a lighter alternative to sdlc-decompose for work with no parent epic.
---

# SDLC Bug Intake

## When to use this skill

Trigger when the user describes a bug, reports something broken, or asks
for a bug ticket to be filed. This is a lighter, optional variant of
`sdlc-decompose` for work that doesn't start from an epic.

## Instructions

1. Read `../../sdlc-spec.md` for the dependency convention, the `Status`
   field, and the Points/estimate scale before proceeding — never hardcode
   these.
2. Gather from the user (ask if not already given):
   - Repro steps — concrete, numbered, reproducible from a clean state.
   - Severity — see `references/severity-guide.md` for the scale.
   - Links to impacted tickets or areas of the app. Where a related ticket
     already exists and this bug is sequencing-relevant (this bug blocks or
     is blocked by that ticket), use the spec's two-ways-together
     dependency convention (`Blocked by #N` body line + `dependency`
     label). Where there's no existing ticket yet, name the affected area
     in plain text instead — don't invent a dependency link to a ticket
     that doesn't exist.
3. If a fix is obvious enough to estimate, add a `Points` value (spec's
   Fibonacci scale) plus rationale — optional here, unlike in
   `sdlc-decompose`, since triage often precedes estimation for bugs.
4. Draft the ticket body with `assets/bug-template.md`.
5. Show the drafted ticket to the user for review. Do not create it on
   GitHub until the user approves; once approved, create it with:
   ```
   gh issue create --title <title> --body-file <file> --label bug
   ```
   If a dependency was identified in step 2, apply the `Blocked by #N` line
   (already in the body from the template) and the `dependency` label
   together, per the spec — never just one.
6. If the user wants it tracked on the Project board, add it and set its
   `Type` field (per the spec, this is almost always `Task` for a bug
   fix — confirm with the user if the bug is large enough that it should
   actually be its own Epic or Feature instead) and `Status` to `Backlog`
   or `Todo` as the user directs.
