# Slider

Picks a value on a continuous range where the exact number matters less than the feel: card size, shine, pointer size, canvas transparency.

## The consumer provides

- `label`, `value`, `onChange(number)`, and `min` / `max` / `step`.
- `format`: shows the current value at the end of the label row ("25%", "92px").

For exact numbers (prices, counts), use an Input with `type="number"`.

## Level

Atom (atomic design). See README.md, Components.
