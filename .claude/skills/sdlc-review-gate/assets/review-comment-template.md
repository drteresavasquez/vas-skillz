# Review Gate: PR #<N> against #<ticket number>

## Acceptance criteria

- [x] Given <context>, when <action>, then <expected outcome> — addressed
  in `<file>`
- [ ] Given <context>, when <action>, then <expected outcome> — **not
  addressed**, no change found touching this behavior

## Required test coverage

- [x] **Unit** — <item> — found: `<test file / test name>`
- [ ] **Integration** — <item> — **missing**

*(If no technical-design annotation exists on the ticket, say so here
instead of a checklist: "No required-test-coverage list found on this
ticket — sdlc-technical-design hasn't been run on it.")*

## Definition of Done

- [x] AC coverage — Pass — all AC bullets addressed
- [ ] Required test coverage present — Fail — integration test missing
- [x] No unrelated changes — Pass
- [x] No debug/leftover code — Pass
- [x] Error handling matches the design — Pass
- [ ] Docs/comments updated — N/A — no documented behavior changed
- [x] Dependency check — Pass — blocking issue #<N> is closed

## Release-note fragment

> <one paragraph or short bullets, user-facing, describing what changed>

---

**Overall:** <ready to merge / not ready — N item(s) need attention before
this meets the ticket's Definition of Done>

This has not been posted to the PR yet. Confirm before I post it as a PR
comment with `gh pr comment`.
