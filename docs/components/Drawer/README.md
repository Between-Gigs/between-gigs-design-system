# Drawer

A panel that slides in from the left or right edge and blocks the page until it's closed. The sidebar and inspector become drawers on smaller screens; settings and setup panels use it on every screen.

## The consumer provides

- `open`, `onClose`, `title`, optional `description` and `footer` (Buttons, primary last).
- `side`: `left` for navigation, `right` for details and settings. `size`: `sm` (default), `md`, `lg`.

Built on Modal, so focus stays inside, Escape closes, and focus returns to the button that opened it.

## Level

Organism (atomic design). See README.md, Components.
