# Design annotation format — detail and example

Load this when the shape in `assets/annotation-template.md` isn't enough
context on its own — e.g. the ticket's scope is ambiguous, or it's unclear
how granular the impacted-areas or test-coverage lists should be.

## How granular "impacted parts of the app" should be

One bullet per distinct area, at the level a reviewer would want to know
about before opening the diff — usually a file, a module, or a named
service/surface. Not so granular that it's restating the diff line-by-line,
not so coarse that "the backend" is a bullet on its own.

## How to write required test coverage so the review gate can check it

Bad (not checkable): "Add tests for the new behavior."

Good (checkable): "Unit test: `parseReportSchema` rejects a schema with a
duplicate column name" — `sdlc-review-gate` can look at the diff and answer
yes/no on whether that specific test exists.

Write every item so a reviewer with no other context could search the diff
for it and get a definitive answer.

## Worked example

Ticket: "Map report schema to CSV columns" (Task, part of "CSV generation"
Feature).

```
## Technical Design — added by sdlc-technical-design

### Approach

Add a `mapSchemaToColumns(schema): CsvColumn[]` pure function in
`lib/reports/csv.ts` that walks the report's field definitions and produces
an ordered column list, handling the three existing field types (text,
number, date). Called from the existing export job handler.

**Ruled out:** generating columns dynamically at write-time from row data
instead of the schema — rejected because column order would then depend on
which row happens to be processed first, which is non-deterministic under
concurrent writes.

### Impacted parts of the app

- `lib/reports/csv.ts` — new `mapSchemaToColumns` function
- `lib/jobs/exportReportJob.ts` — calls the new function instead of the
  placeholder column list
- `lib/reports/schema.ts` — no changes, but the field-type enum here is a
  hard dependency; a fourth field type added later requires updating both

### Required test coverage

- [ ] **Unit** — `mapSchemaToColumns` produces correct column headers/order
  for a schema with all three current field types
- [ ] **Unit** — `mapSchemaToColumns` throws a descriptive error on an
  unrecognized field type rather than silently dropping the column
- [ ] **Integration** — `exportReportJob` end-to-end on a fixture report
  produces a CSV whose header row matches the report's field order
```
