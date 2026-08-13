# Breakdown format — worked example

This is a reference for judging Task granularity and writing the
proposal shape from `assets/proposal-template.md`. Load this when the
epic's scope is broad enough that it's unclear where a Feature boundary or
a Task boundary should fall.

## Judging Feature boundaries

A Feature is a coherent, user- or system-facing slice of the epic — not an
arbitrary chunk. A good test: could this Feature ship on its own and be
individually described in a release note? If yes, it's sized right. If a
proposed Feature is really "half of one idea," merge it with its sibling.
If a proposed Feature bundles two unrelated capabilities, split it.

## Judging Task boundaries

A Task is the smallest unit that can be independently estimated, reviewed,
and merged — typically one PR. Signs a "Task" is actually oversized (should
be 13 points, i.e. split further):
- It touches more than ~3 distinct areas of the app.
- Its acceptance criteria can't be checked without also checking another
  Task's criteria.
- You can't describe it in one sentence without "and."

Signs a Task is too small to stand alone (should be folded into a sibling):
- Its only acceptance criterion is an implementation detail invisible to
  any test or reviewer working from the ticket alone.

## Worked example

Epic: "Add CSV export to the reports page."

Features:
- **Export trigger & job queueing** — user-facing button, background job
  creation, job status polling.
- **CSV generation** — turning a report's data into a correctly-formatted
  CSV file, given a job.
- **Download delivery** — signed URL generation, expiry, download UI state.

Tasks under "CSV generation" (Feature):
- Task: "Map report schema to CSV columns" — Points: 3 — rationale: "clear
  schema, straightforward mapping, one existing report type to validate
  against."
- Task: "Handle report rows exceeding CSV cell limits" — Points: 5 —
  rationale: "edge case behavior isn't fully defined yet, needs a decision
  on truncation vs. multi-file split."
- Task: "Stream generation for large reports instead of loading fully into
  memory" — Points: 8 — rationale: "touches the job worker's memory model,
  cross-cutting, needs a load test to validate."

Note the rationale in each case names *why* — complexity, unknowns, or
cross-cutting reach — not just a restatement of the points value.
