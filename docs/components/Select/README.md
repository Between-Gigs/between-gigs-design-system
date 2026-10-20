# Select

Picks one value from a short list. The list is drawn by the design system, not the operating system, so it has the same rounded, raised look as Menu and Combobox in both themes.

## The consumer provides

- `options`: `{ value, label, disabled? }[]`.
- `value` + `onValueChange(value)` to control it, or `defaultValue` to let it manage itself. `onChange` also fires with `{ target: { value } }` for form libraries.
- `placeholder`: shown in the field until something is chosen ("Choose a service"). It is not an option in the list.
- `name` to submit with a form (a hidden input carries the value). `size`, `invalid`, `disabled`, `start` (an icon, as in filter bars).

## Keyboard

Enter, Space or the arrow keys open the list; arrows, Home and End move; Enter or Space picks; Escape closes and returns focus. Typing a letter jumps to the next option that starts with it, open or closed.

## Use when

- Up to about ten options. Longer lists, or options that need search, use Combobox.
- Five or fewer options that all deserve to be seen: use RadioGroup or SegmentedControl.
