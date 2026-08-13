# SDLC Spec

This is a plain reference, not a skill — it has no frontmatter and Claude
does not load it automatically. Every skill under `.claude/skills/sdlc-*/`
is instructed to read this file first so the ticket hierarchy, custom
Project fields, acceptance-criteria format, dependency convention, status
columns, and estimate scale stay identical across all of them. Edit this
file and every skill that reads it picks up the change — nothing is
hardcoded per-skill.

Everything below is a **starting default**, marked **REVIEW**, so you can
edit freely before any skill starts relying on it.

## GitHub Project configuration

- Project: `Repped-Labs/8` — the GitHub Project (v2) board ("Repped Index",
  https://github.com/orgs/Repped-Labs/projects/8) that holds `Ticket Type`,
  `Status`, and `Points` as custom fields.
- Repo: `Repped-Labs/repped-index` — the repo Issues and PRs live in.
- **Two `Type` signals exist on this repo/org — set both, always together:**
  1. **Native GitHub Issue Type** — a repo/org-level feature independent of
     Projects. `Repped-Labs` already has `Epic`, `Feature`, `Task` (plus
     `Bug`, `Spike`, `Initiative`, `Documentation`) defined as org issue
     types. This is what shows in a Project's built-in **`Type`** column —
     GitHub reserves the literal field name `Type` for it, which is why
     `gh project field-create --name "Type"` fails with "reserved value."
     Set it directly on the issue (not the Project item):
     ```
     gh issue edit <NUMBER> --type Epic   # or Feature / Task
     ```
  2. **Custom Project field `Ticket Type`** — a single-select field on this
     Project (`Epic`/`Feature`/`Task` options) created because the native
     `Type` name was unavailable. Set via the Project item, same as
     `Points`:
     ```
     gh project item-edit --project-id <PROJECT_ID> --id <ITEM_ID> \
       --field-id <TICKET_TYPE_FIELD_ID> --single-select-option-id <OPTION_ID>
     ```
  Both are kept in sync intentionally (not deduplicated) — a ticket with
  only one set is inconsistent and should be fixed to have both.
- Skills read/write Project fields via `gh project item-edit` (and
  `gh api graphql` for anything the `gh project` subcommands don't cover
  yet, e.g. resolving field/option IDs with `gh project field-list`). If
  field or option IDs are needed and not already known, look them up with:
  ```
  gh project field-list <PROJECT_NUMBER> --owner <OWNER>
  ```
  before attempting to set a value — never guess an ID.

## Ticket hierarchy

**REVIEW** — placeholder scheme.

- **Epic** — a GitHub issue labeled `epic`. Represents a large body of work,
  usually spanning multiple Features. Has no parent.
- **Feature** — a GitHub issue that is a **native GitHub sub-issue** of an
  Epic. Contains a coherent slice of the Epic's scope.
- **Task** — a GitHub issue that is a native GitHub sub-issue of a Feature
  (a leaf — it has no sub-issues of its own). Tasks are the unit of
  estimation and the unit that moves through Status columns.

Parent-child relationships are expressed through GitHub's native sub-issue
feature, not body text and not labels. To attach a child issue to a parent:
```
gh api repos/<OWNER>/<REPO>/issues/<PARENT_NUMBER>/sub_issues \
  -f sub_issue_id=<CHILD_ISSUE_ID>
```
(`sub_issue_id` is the issue's numeric database ID, not its issue number —
resolve it with `gh api repos/<OWNER>/<REPO>/issues/<NUMBER> --jq .id` first.)
If your installed `gh` version exposes a native `--add-sub-issue` flag,
prefer that instead — check `gh issue edit --help` before falling back to
the raw API call above.

This hierarchy answers "what contains what." It is a separate concern from
sequencing (see Dependencies below), which answers "what has to finish
before what can start."

## Type field (primary hierarchy signal)

Two `Type` signals — see Project configuration above for the full
distinction — and every ticket gets **both**, set together, never one
without the other:

- **Native GitHub Issue Type** (`gh issue edit <NUMBER> --type Epic`, or
  `Feature` / `Task`) — drives the Project's built-in `Type` column.
- **Custom Project field `Ticket Type`** (`Epic`/`Feature`/`Task` options),
  set via:
  ```
  gh project item-edit --project-id <PROJECT_ID> --id <ITEM_ID> \
    --field-id <TICKET_TYPE_FIELD_ID> --single-select-option-id <OPTION_ID>
  ```

Together these are the **primary** signal skills read to determine whether
an issue is an Epic, Feature, or Task; the `epic` label and sub-issue
linking are supporting/structural signals, not the first thing to check.

## Status field

```
Backlog → Todo → In Progress → In Review → Done
```

A single-select Project field named `Status`. **Not labels.** Skills that
read or propose a status transition must refer to these five names exactly,
and read/write them via the Project field (`gh project item-edit`, or
`gh project item-list --format json` to read current values), never via
issue labels.

## Points field (estimates)

A **number** Project field named `Points`, Fibonacci-scaled:

| Points | Meaning |
|---|---|
| 1 | Trivial — near-zero risk, well under an hour of focused work |
| 2 | Small — straightforward, low risk |
| 3 | Medium — some design/thought required, one clear approach |
| 5 | Large — meaningful complexity or unknowns |
| 8 | Very large — significant complexity, unknowns, or cross-cutting change |
| 13 | Too big — should usually be split into smaller tickets before work starts |

Every Task ticket gets a `Points` value **plus a one-line rationale** for
why that size was chosen. The number lives in the Project field; the
rationale lives in the ticket body/comment (there's nowhere else to put it).
Both are required, not optional: `sdlc-velocity` sums real throughput
against these estimates, so a Task without a rationale-backed estimate
breaks that math silently. Set the field with:
```
gh project item-edit --project-id <PROJECT_ID> --id <ITEM_ID> \
  --field-id <POINTS_FIELD_ID> --number <VALUE>
```

## Acceptance criteria format

**REVIEW** — Gherkin-flavored checklist, placeholder.

Every Feature and Task carries a `## Acceptance Criteria` heading with a
checklist of Given/When/Then bullets:

```
## Acceptance Criteria

- [ ] Given <context>, when <action>, then <expected outcome>
- [ ] Given <context>, when <action>, then <expected outcome>
```

Each bullet should be independently verifiable — a reviewer should be able
to check it against a PR diff without needing the other bullets for
context.

## Dependencies (sequencing, not decomposition)

Dependencies express sequencing — "issue B can't start until issue A is
done" — and are a separate concern from the parent/child hierarchy above.
They are always written **two ways together**, never just one:

1. A line (single blocker) or a bulleted list (two or more blockers) in the
   blocked issue's body, under a `## Dependencies` heading — every blocker
   named there, none omitted:

   Single blocker:
   ```
   ## Dependencies

   Blocked by #123
   ```

   Multiple blockers — always a list, one bullet per blocking issue, never
   several bare `Blocked by #N` lines stacked without list markers:
   ```
   ## Dependencies

   Blocked by:
   - #123
   - #456
   ```
2. The **same issue** also gets the `dependency` label applied — once, no
   matter how many blockers it has:
   ```
   gh issue edit <BLOCKED_ISSUE_NUMBER> --add-label dependency
   ```

Both steps are mandatory and always applied together — the label makes
blocked issues filterable/queryable across the repo (`gh issue list --label
dependency`) without opening every body, and the body line(s) name *which*
issue(s) are the blocker(s). A skill that adds a `Blocked by` line/list
without also applying the `dependency` label (or vice versa) has done the
convention wrong — and a skill that lists a blocked issue's dependencies
without naming every one of its blockers has also done it wrong.

## How skills use this file

Every skill's `SKILL.md` opens its instructions with a step that reads this
file before doing anything else, and refers back to it by name (hierarchy,
Type field, Status field, Points field, AC format, dependency convention)
rather than restating or hardcoding the values inline. If you edit this
file, no skill needs to change to pick up the update.
