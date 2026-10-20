# Accordion

Sections that expand and collapse in place: Thread setup, FAQs, groups of settings.

## The consumer provides

- `items`: `{ id, title, meta?, content }[]`. `meta` is short text on the right ("3 items").
- `type`: `multiple` (default) or `single` (opening one closes the rest). `defaultOpen`: ids open at first.
- `variant`: `framed` (default) or `flush` inside panels.

Don't hide anything people need on every visit. Each header is a real button with `aria-expanded`.
