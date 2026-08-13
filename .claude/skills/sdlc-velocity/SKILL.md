---
name: sdlc-velocity
description: Reads real cycle-time and Status-field transition history from the GitHub Project, sums completed Points against remaining scope, checks dependency-labeled issues for what's gated, and proposes an updated projected timeline for the Roadmap view. Use when the user asks for a velocity check, timeline update, or "are we on track" read on an epic or project — never rewrites the timeline without confirmation.
---

# SDLC Velocity

## When to use this skill

Trigger when the user asks about progress, timeline, "are we on track", or
wants a velocity/burndown read on an epic, Feature, or project. This reads
actual GitHub history, not estimates alone — it's a check on the estimates
made by `sdlc-decompose`, not a restatement of them.

## Instructions

1. Read `../../sdlc-spec.md` for the `Status` field, the `Points` field,
   and the dependency convention before proceeding — never hardcode these.
2. Identify scope: the epic, Feature, or set of tickets the user wants
   tracked. Fetch all tickets in scope — for an epic, walk its native
   sub-issue tree (Features, then their Task sub-issues) rather than
   filtering by label, since `Type`/hierarchy is the spec's primary signal,
   not labels. Pull each ticket's `Points` field via `gh project item-list
   --format json` (filtered to the Project from the spec's configuration).
3. Pull real status-change history for those tickets: `Status` field
   transition timestamps from the GitHub Project. If the `gh project`
   subcommands don't expose field-change history directly, fall back to
   `gh api graphql` against the Project's item events, or — if the Project
   isn't instrumented for that at all — issue/PR close timestamps as a
   last-resort proxy, and say clearly that you're using the fallback. See
   `references/cycle-time-methodology.md` for how to compute cycle time and
   throughput from whichever data source is actually available.
4. Compute:
   - Actual cycle time per completed ticket (Todo → Done, or whatever
     transition the data supports).
   - Completed Points over the measurement window (throughput).
   - Remaining Points across tickets not yet Done.
   - Which not-yet-Done tickets carry the `dependency` label, and what
     issue each one's `Blocked by #N` line names as the blocker — report
     these as explicitly gated, separate from ordinary remaining work.
   - A projected completion date, using throughput rather than the
     original estimate-based projection alone.
5. Compare this projection against the last one on record — ask the user
   where that lives (a prior comment, a field on the Roadmap view, a note)
   if it isn't already obvious from context.
6. Present the update as a **delta** — old projection vs. new projection,
   what changed and why (e.g. "throughput dropped because 3 tickets sat in
   In Review for 5+ days", or "projection slipped because #45 is blocked by
   #40, which is still In Progress") — using
   `assets/velocity-update-template.md`.
7. Do not write the update anywhere — the Project's Roadmap view, an issue
   comment, a wiki page — until the user confirms they want it recorded,
   and confirm where. This skill proposes; it never silently rewrites the
   projected timeline.
