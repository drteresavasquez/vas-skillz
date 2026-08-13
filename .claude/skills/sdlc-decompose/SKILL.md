---
name: sdlc-decompose
description: Breaks a GitHub epic into Features and Tasks (native sub-issues) with acceptance criteria, Points estimates, and dependency links. Use when the user hands you an epic — an issue number or a freeform description of a large body of work — before any tickets for it exist on GitHub, or asks to extend an existing epic with more Features/Tasks.
---

# SDLC Decompose

## When to use this skill

Trigger when the user hands you an epic — a GitHub issue number, a URL, or a
freeform description of a large body of work — and asks for it to be broken
down, planned, or split into tickets. Also applies when the user asks to
re-decompose or extend an existing epic that already has some Features under
it. This runs **before** anything is created on GitHub — it produces a
proposal, not tickets.

## Instructions

1. Read `../../sdlc-spec.md` for the ticket hierarchy, the `Type` field, the
   `Points` field, the acceptance-criteria format, and the dependency
   convention before proceeding — never hardcode these.
2. If given an issue number, fetch the epic with `gh issue view <number>
   --json body,title,labels`. Confirm it carries the `epic` label; if it
   doesn't, flag that to the user before proceeding rather than silently
   assuming it's an Epic. If given a freeform description instead, treat
   that description as the epic's content directly (it doesn't need to
   exist on GitHub yet for you to draft a proposal against it).
3. Propose the Feature-level breakdown: one Feature per coherent slice of
   the epic's scope, each with a working title and a one-line summary of
   what it covers. Each Feature will become a native sub-issue of the Epic.
4. Under each Feature, propose Tasks: the smallest units of work that can be
   independently estimated, reviewed, and merged. Each Task will become a
   native sub-issue of its Feature (a leaf — no further nesting).
5. For every Feature and Task, write:
   - Acceptance criteria in the spec's Given/When/Then checklist format.
   - A `Points` estimate from the spec's Fibonacci scale **plus a one-line
     rationale** for why that size was chosen. Required for every Task —
     `sdlc-velocity` depends on estimates being present and rationale-backed.
   - Dependency links to other tickets in the proposal (or to existing
     tickets), written the spec's two-ways-together way: a `Blocked by #N`
     line under a `## Dependencies` heading in the body, paired with a note
     that the `dependency` label must be applied to that ticket once it
     exists. Only use this for sequencing ("can't start until"), not for
     the Feature/Task parent-child relationship — that's the sub-issue
     link, not a dependency.
6. Assemble the full proposal using `assets/proposal-template.md` as the
   shape: Epic summary, then each Feature with its Tasks nested under it,
   each ticket showing title / summary / AC / Points+rationale /
   dependencies / intended `Type` value. See
   `references/breakdown-format.md` for a worked example if the epic's
   scope or the right level of Task granularity is unclear.
7. Present the proposal in chat for the user to review. Do **not** create
   any issues, sub-issue links, Project field values, or labels on GitHub —
   this skill only produces a proposal.
8. Only after the user explicitly approves, create the real objects, and
   confirm before running any create/link commands:
   - `gh issue create --title <title> --body-file <file> --label epic` for
     the Epic (skip if it already exists).
   - `gh issue create --title <title> --body-file <file>` for each Feature
     and Task, then attach it to its parent via the spec's native sub-issue
     command.
   - Add each ticket to the Project and set its `Type` field
     (Epic/Feature/Task) and `Points` field per the spec.
   - For every dependency in the proposal, apply both the `Blocked by #N`
     body line and the `dependency` label — together, per the spec.
