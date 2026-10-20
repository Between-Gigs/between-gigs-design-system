# Stat

One headline number with its label. `StatRow` lays several out between hairlines.

## The consumer provides

- `value`: the formatted number ("$5,000", "14"). Set in Sora, tabular.
- `label`: lower-case phrase that completes the number ("numbered founding cards").
- `delta`: optional change, `{ value, direction, invert? }`. `invert` when going up is bad (errors, costs).
- `size`: `lg` for marketing and dashboards, `md` inside panels.

Only use stat rows when the numbers are the point of the page. Never invent figures to fill a row.

## Level

Molecule (atomic design). See README.md, Components.
