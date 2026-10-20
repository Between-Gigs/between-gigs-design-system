# Card

The one container for grouped content. Module cards, profile cards, funnel steps and panels all start from it.

## Variants

- `raised` (default): on the page ground, with `shadow-sm`.
- `flat`: inside a panel or another surface; hairline only.
- `sunken`: a recessed well inside a card.

## The consumer provides

- `children`, usually starting with `CardHeader` (`kicker`, `title`, `description`, `aside`).
- `padding`: `sm` 12px, `md` 16px (default), `lg` 24px (panels).
- `stripe`: a `cat-*` color along the top edge to show the item's type (funnel steps). Always with a type label.
- `selected`: the featured or current card. One per view.
- `interactive`: hover feedback. Put the real link or button inside the card; don't make the whole div clickable.

## Don't

- Don't nest raised cards. Inside a card, use `flat` or `sunken`.
- Don't add a colored left border; use `stripe` on top, or a Badge.

## Level

Molecule (atomic design). See README.md, Components.
