# Select

Picks one value from a list of six or more. It is a native select inside the system's frame, so the keyboard, mobile pickers and screen readers all work without extra code.

## The consumer provides

- `options`: `{ value, label, disabled? }[]`.
- `placeholder`: a first, unselectable option when nothing is chosen yet ("Choose a service").
- `size`, `invalid`, `start` (an icon, as in filter bars), and standard select props.

## Use when

- Five or fewer options that all deserve to be seen: use RadioGroup or SegmentedControl.
- Options with descriptions, avatars or search (company switcher): use Menu with a header Input.
