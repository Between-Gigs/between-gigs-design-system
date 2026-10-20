# ThemeToggle

The Day/Night switch: a sliding sun and moon. Left uncontrolled, it switches the whole page with a circular reveal that grows from the switch.

## The consumer provides

- Nothing, for the usual case: it reads and writes `data-theme` on `<html>` and remembers the choice (localStorage key `bg-theme`).
- Or `theme` and `onChange(theme, origin)` to control it, for example to save the choice to the person's account. Call `useTheme().setTheme(theme, origin)` to keep the reveal.
- `size` `sm` or `md`, and `showLabel` (Day / Night text, default on).

## Use when

- One per screen, in the top bar or the account menu. Not inside forms.
- Restore the saved theme before first paint (an inline script that sets `data-theme`), so the page never flashes the wrong theme.
- The reveal uses the View Transitions API and turns off under reduced motion; the switch still works instantly.

## Level

Atom (atomic design). See README.md, Components.
