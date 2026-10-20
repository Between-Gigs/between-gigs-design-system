# Combobox

Pick one value from a long list by typing to filter it: the company switcher, assigning a person, choosing a service from dozens.

## The consumer provides

- `options`: `{ value, label, description?, icon?, disabled? }[]`. Descriptions are searched too.
- `value` (or `null`) and `onChange(value)`. `placeholder`, `emptyText`, `size`, `invalid`.
- A label: wrap it in Field, or pass `aria-label`.

Arrow keys move through matches, Enter picks, Escape closes. For fewer than about ten options, use Select.
