# Banner

A message about a page or section that stays until it is resolved or dismissed.

## The consumer provides

- `tone`: `info`, `success`, `warning`, `danger`. The icon follows the tone.
- `layout`: `inline` (rounded, inside content) or `strip` (full-width band at the top of a page, like "Draft · not public").
- `title` (bold lead), `children` (the detail), `action` (a link or small button), `onDismiss`.

## Use when

- The message is about the state of the page (draft, locked, failed to save).
- For a confirmation that something just happened, use a Toast. For a field error, use Field's `error`.

## Level

Molecule (atomic design). See README.md, Components.
