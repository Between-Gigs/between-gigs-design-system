# Pager

Steps through a set one item or page at a time: Coverflow, stacked profile cards, long result lists.

## The consumer provides

- `page` (1-based), `pageCount`, `onChange(page)`.
- `itemLabel`: the current item's name, shown after the position ("1 / 5 · Connected work").

The position is announced to screen readers when it changes.

## Level

Molecule (atomic design). See README.md, Components.
