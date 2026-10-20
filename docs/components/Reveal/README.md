# Reveal

Animates content in as it scrolls into view. Eight effects: `fade-up`, `scale-in`, `blur-in`, `slide-left`, `slide-right`, `clip-up`, `tilt-in` and `pop`.

## The consumer provides

- `effect`, and `delay` in ms to stagger a group (`index * 60`).
- `repeat` to play again each time it re-enters the viewport (default once). `threshold` for how much must be visible first (default 0.2).

## Use when

- Section openers, card grids and marketing pages. Not for app chrome, table rows or anything people need the moment the page loads.
- `fade-up` is the default. Keep one or two effects per page.
- The content is always in the DOM and readable by assistive tech. Under reduced motion it simply shows.

## Level

Atom (atomic design). See README.md, Components.
