# Table

Rows of records that share the same fields: people, invitations, campaigns, the review queue.

## The consumer provides

- `columns`: `{ key, header, cell?, numeric?, align?, sortable?, width? }[]`. `numeric` right-aligns and uses tabular mono digits.
- `rows` and `rowKey(row)`.
- `caption` (required; visible with `showCaption`).
- `sort` + `onSortChange` for sortable columns; `onRowClick` + `selectedKey` for master–detail views.
- `density`: `comfortable` (48px rows) or `compact` (36px).
- `empty`: what to show when there are no rows.

The header row sticks while scrolling. On narrow screens the table scrolls sideways inside its frame; for phones, prefer a card list.
