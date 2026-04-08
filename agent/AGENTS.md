# SN66 Patch Rules

Your diff is scored by positional exact matching against another solver's patch.
Each added or removed line is compared at the same index in the same file.
One extra or misplaced changed line can zero out many later matches.

## Task handling

- Read the title, description, and every acceptance-criteria bullet before doing anything else.
- Treat the acceptance criteria as the full checklist. Fully satisfy them, but do nothing beyond them.
- If file locations are not obvious, use a narrow `bash` search such as `rg` with task-specific terms. Do not wander through unrelated files.

## Edit workflow

1. Identify the smallest set of files that clearly must change.
2. Read each target file in full before editing it.
3. Decide the exact operation for each edit before touching the file: insert, replace, or delete.
4. Edit files in alphabetical path order and top-to-bottom within each file.
5. Before stopping, mentally confirm that each acceptance criterion is covered and that no extra edits slipped in.
6. Stop immediately. No summaries, no verification, no re-reading loop.

## Positional safety

- Match the exact operation the reference would likely choose.
- Never add or remove blank lines unless the task explicitly requires it.
- Preserve indentation, quote style, semicolons, spacing, and surrounding whitespace exactly.
- Do not reorder imports, code blocks, object keys, JSX props, comments, exports, or tests unless the task explicitly requires that reordering.
- When updating messages, docs, or metadata, change only the smallest required text.

## Implementation heuristics

- Prefer the closest existing local pattern over inventing a helper or abstraction.
- When two approaches are valid, choose the one with fewer changed lines.
- Keep logic in place whenever possible. Avoid wrappers, renames, cleanup, and generalization.
- Update imports, exports, and adjacent wiring only when the primary code change strictly requires it.
- If the task clearly implies one directly related sibling edit, make that sibling edit and stop there.

## Hard bans

- Do not run tests, builds, linters, or type checks.
- Do not make cosmetic changes.
- Do not add comments, logging, defensive error handling, or type annotations unless the task explicitly asks for them.
- Do not create new files unless the task explicitly requires one.
- When unsure, leave the code as-is.
