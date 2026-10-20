# Modal

A focused task that blocks the page until it's done or dismissed. With `placement="right"` it becomes a drawer.

## The consumer provides

- `open`, `onClose`, `title`, optional `description`.
- `children`: the body; it scrolls when tall.
- `footer`: Buttons, right-aligned, primary last. Usually Cancel (ghost) + one primary or strong action.
- `size`: `sm`, `md` (default), `lg`. `placement`: `center` or `right`.

Built on the native `<dialog>`: focus is trapped, Escape closes, and it renders in the browser's top layer, so no z-index fights. Clicking the scrim closes it; for forms with unsaved input, confirm before closing.

## Level

Organism (atomic design). See README.md, Components.
