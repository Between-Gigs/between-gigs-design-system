# SegmentedControl

Switches between views of the same content, such as Gallery / List / Coverflow / Tiles or Default / Light / Dark.

## The consumer provides

- `label`: names the group for screen readers ("View").
- `options`: 2 to 5 items, each with `value`, `label` and an optional icon.
- `value` and `onChange`.
- `size`: `sm` in toolbars, `md` elsewhere.

## Use when

- The choice changes how the same data is shown and takes effect immediately.
- For moving between different content, use Tabs. For a setting saved with a form, use RadioGroup.

Arrow keys move the selection; only the selected option is in the tab order.

## Level

Molecule (atomic design). See README.md, Components.
