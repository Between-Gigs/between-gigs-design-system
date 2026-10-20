# Popover

A small panel of settings or details anchored to a button, that doesn't block the page: Appearance, Material box, Mouse & gestures, a "With you" call panel.

## The consumer provides

- `trigger`: a Button or IconButton. `label`: the panel's name for screen readers. Optional `title`.
- `children`: the controls. `align` (`start` / `end`), `width` (`sm`, `md`, `lg`).
- `open` / `onOpenChange` to control it; omit them to let it manage itself.

## Use when

- Changes apply as people make them. For a list of actions use Menu. For a task that must be finished or cancelled, use Modal or Drawer.

Focus moves into the panel when it opens; Escape or a click outside closes it.

## Level

Molecule (atomic design). See README.md, Components.
