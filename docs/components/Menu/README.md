# Menu

A list of actions or choices opened from a button: Appearance, account, row actions, the company switcher.

## The consumer provides

- `trigger`: a Button or IconButton. Menu adds `aria-haspopup` and `aria-expanded`.
- `items`: a mix of `{ label, onSelect, icon, description, shortcut, checked, danger, disabled }`, `"separator"` and `{ heading }`.
  Setting `checked` on items makes them a pick-one list with a check on the current choice.
- `header`: optional element above the items, such as a search Input.
- `align`: `start` or `end` relative to the trigger.

Keyboard: Down arrow opens and moves, Up arrow, Home, End; Escape or Tab closes and returns focus to the trigger.

## Level

Molecule (atomic design). See README.md, Components.
