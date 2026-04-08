# SN66 Challenger Instructions

Your diff is scored by positional exact matching against another solver's patch.
Every added or removed line is compared at the same index in each file.
One extra, missing, or misplaced changed line can shift the rest of the file and destroy later matches.

## Task format

The task contains:

- a title
- a short description
- acceptance criteria bullets

Treat the acceptance criteria as the authoritative checklist. The strongest patch is the smallest obvious change set that satisfies every criterion and nothing else.

## Workflow

1. Read the title, description, and **all** acceptance criteria.
2. Identify the smallest set of files that clearly must change.
3. Read each target file **in full** before editing it.
4. Decide the exact operation for each change before touching the file: insert, replace, or delete.
5. Edit files in alphabetical path order and top-to-bottom within each file.
6. After the last edit, do one mental coverage check against the acceptance criteria and stop. No summaries, no verification, no extra reads.

## Positional diff discipline

- Match the exact operation the reference would likely choose: replace vs insert vs delete.
- Never add or remove blank lines unless the task clearly requires it.
- Preserve indentation, quote style, semicolons, spacing, and surrounding whitespace exactly.
- Do not reorder imports, code blocks, object keys, JSX props, comments, or tests unless the task explicitly requires that reorder.
- When updating docs or messages, change only the smallest required words or values.

## Implementation heuristics

- Prefer the closest existing local pattern over inventing a new helper or abstraction.
- When two approaches are valid, choose the one with fewer changed lines.
- Keep logic in place whenever possible. Avoid wrappers, renames, cleanup, and generalization.
- Update imports only when the code change strictly requires it.
- If the task clearly implies a directly related sibling file must change, update only that directly impacted sibling file.

## Hard bans

- Do not run tests, builds, linters, or type checks.
- Do not make cosmetic changes.
- Do not add comments, logging, error handling, or type annotations unless the task explicitly asks for them.
- Do not create new files unless the task explicitly requires one.
- When unsure, leave the code as-is.
