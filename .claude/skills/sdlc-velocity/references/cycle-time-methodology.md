# Cycle-time and throughput methodology

Load this when computing step 4 of `SKILL.md` — how to turn raw Status
transition data into cycle time, throughput, and a projection.

## Cycle time

For a single ticket: the elapsed time between its `Status` field entering
`Todo` and entering `Done`. Use the *last* time it entered each state if it
bounced back and forth (e.g. sent back from In Review to In Progress) —
cycle time should reflect the real elapsed wall-clock time to actually
finish, including rework, not just the first attempt's duration.

Report cycle time per ticket in whole days. If a ticket's data only
supports a coarser proxy (e.g. issue-close timestamp instead of a true
`Status: Done` transition), say so next to that ticket's number rather than
presenting it as equally precise.

## Throughput

Sum of `Points` for tickets that transitioned to `Done` within the
measurement window (default: the last 2 completed weeks, or whatever window
the user specifies). Report both:
- Points/week (for the projection math below)
- Ticket count/week (a sanity check — a throughput number driven by one
  huge ticket reads differently than one driven by five small ones)

## Projection

```
projected_completion = today + (remaining_points / points_per_week) weeks
```

If throughput is 0 or the measurement window has too few completed tickets
to be meaningful (fewer than ~3), say so explicitly and don't produce a
confident date — a projection built on near-zero data is worse than no
projection.

## Handling gated (dependency-labeled) work

Points behind an unresolved `Blocked by #N` dependency shouldn't be treated
as flowing at the same throughput as unblocked work — they can't start
until the blocker resolves. Call these out as a separate line ("N points
gated behind #40, currently In Progress") rather than folding them into the
undifferentiated remaining-points total, since doing so would understate
how much of the remaining scope is actually available to work on right now.

## Worked example

- Remaining Points: 42 total, of which 13 are gated behind #40 (still In
  Progress).
- Unblocked remaining: 29 points.
- Throughput: 9 points/week over the last 2 weeks (7 tickets completed).
- Projection: 29 / 9 ≈ 3.2 weeks for the unblocked work, **plus** whatever
  time #40 itself takes to unblock the remaining 13 points — report both
  components rather than a single blended number that hides the
  dependency risk.
