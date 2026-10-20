# Field

Wraps one form control with its label and its help or error text, and connects them for screen readers.

## The consumer provides

- `label`: short, sentence case, no colon.
- `children`: exactly one Input, Textarea or Select. Field passes it `id`, `invalid` and `aria-describedby`.
- `hint`: what to enter or why it's asked.
- `error`: what went wrong and how to fix it ("Enter a 5-digit ZIP code, like 90026"). Replaces the hint while shown.
- `optional`: marks the field "Optional". Required is the default, so required fields are not marked.

## Do

- Show errors after the person leaves the field or submits, not while they type.
- Stack fields with `gap-5`; group related fields under a heading-sm.
