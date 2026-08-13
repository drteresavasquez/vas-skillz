# Definition-of-Done checklist

Run every item below against the PR. Each item resolves to Pass / Fail /
N/A — don't leave one unresolved. "Can't tell from the diff alone" is a
Fail with a note explaining what's missing, not a silent skip.

- [ ] **AC coverage** — every acceptance-criteria bullet on the ticket is
  addressed by the diff (cross-check from step 4 of `SKILL.md`).
- [ ] **Required test coverage present** — every item from the
  technical-design annotation has a matching test in the diff (step 5).
- [ ] **No unrelated changes** — the diff doesn't touch files/areas outside
  what the ticket's impacted-areas list (if present) or its own scope
  implies. Flag, don't block — unrelated cleanup may be intentional, but
  the reviewer should see it called out.
- [ ] **No debug/leftover code** — no commented-out blocks, stray
  `console.log`/`print` debugging, or TODO comments referencing this PR's
  own unfinished work.
- [ ] **Error handling matches the design** — if the technical-design
  annotation specified error/edge-case behavior, the diff implements it.
- [ ] **Docs/comments updated** — if the change alters documented behavior
  (README, API docs, inline doc comments), those are updated in the same
  diff, not deferred.
- [ ] **Dependency check** — if the ticket carries a `Blocked by #N` line
  and `dependency` label (per the spec), confirm the blocking issue is
  actually resolved before treating this PR as mergeable.

Report each line with its verdict and a one-line reason. Don't just say
"Pass" — say what you checked to reach that verdict, so the user can
sanity-check the gate itself.
