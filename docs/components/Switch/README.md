# Switch

Turns a setting on or off immediately, with no save step.

## The consumer provides

- `checked` and `onChange(checked)`.
- `label` and optional `description`. Without a visible label, pass `aria-label`.

## Use when

- The change applies the moment it is flipped (Typewriter, Highlight edits, Use Hub pointer).
- For a yes/no inside a form that is submitted later, use Checkbox.
- Label the setting, not the state: "Highlight edits", not "Highlighting is on".
