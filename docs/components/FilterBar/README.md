# FilterBar

The recessed row of search and filters above a collection (Workspace hub, material library, People & profiles).

## The consumer provides

- `children` in this order: the search Input (give it `className="min-w-48 flex-1"` so it takes the spare width), then filter Selects (each with a `FilterLabel`), then the view SegmentedControl, then sliders.
- `end`: right-aligned extras, usually "Reset filters" (ghost Button), shown only when a filter is active.

All controls inside use `size="sm"`. The bar wraps on narrow screens; it never scrolls sideways.

## Level

Organism (atomic design). See README.md, Components.
