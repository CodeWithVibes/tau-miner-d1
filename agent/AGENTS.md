# SN66 Diff Match

Your patch is scored by positional exact matching against another solver's patch.
Changed lines are compared at the same index in the same file.
One extra, missing, or misplaced changed line can zero out many later matches.

## Scoring mindset

- Fully satisfy the task, but nothing beyond it.
- Match the reference solver's likely operation: insert vs replace vs delete.
- Prefer the most conventional local implementation, not the most clever one.
- Every extra changed line is a liability.

## Task handling

1. Read the title, description, and every acceptance-criteria bullet before doing anything else.
2. Build the exact checklist of required layers or files from those criteria.
3. If paths are unclear, run one narrow `rg` search with task-specific terms. Do not wander.
4. Read each target file in full before editing it.

## Coverage discipline

- Treat the acceptance criteria as the full checklist.
- If the task clearly names multiple layers such as schema, views, seeds, controllers, UI, or docs, cover each required layer exactly once.
- Do not stop after the first obvious file if later criteria still require adjacent wiring or reporting changes.
- Do not add speculative sibling changes just because they seem nice.

## Edit workflow

1. Identify the smallest set of files that clearly must change.
2. Decide the exact operation for each edit before touching the file.
3. Edit files in alphabetical path order and top-to-bottom within each file.
4. Keep each edit local and minimal.
5. Before stopping, mentally confirm every acceptance criterion is covered and no extra edits slipped in.
6. Stop immediately. No summaries, no verification, no re-reading loop.

## Positional safety

- Never add or remove blank lines unless the task explicitly requires it.
- Preserve indentation, quote style, semicolons, spacing, and surrounding whitespace exactly.
- Do not reorder imports, object keys, JSX props, comments, exports, or tests unless the task explicitly requires it.
- When updating text, docs, or metadata, change only the smallest required text.
- Avoid broad search-and-replace edits that can shift many later lines.

## Implementation heuristics

- Prefer the closest existing local pattern over inventing a helper or abstraction.
- When two approaches are valid, choose the one with fewer changed lines.
- Keep logic in place whenever possible. Avoid wrappers, renames, cleanup, and generalization.
- Update imports, exports, and adjacent wiring only when the primary code change strictly requires it.
- Add adjacent lifecycle fields, indexes, audit tables, or helper structures only when the task or surrounding local pattern clearly requires them.

## Hard bans

- Do not run tests, builds, linters, or type checks.
- Do not make cosmetic changes.
- Do not add comments, logging, defensive error handling, or type annotations unless the task explicitly asks for them.
- Do not create new files unless the task explicitly requires one.
- When unsure, leave the code as-is.
