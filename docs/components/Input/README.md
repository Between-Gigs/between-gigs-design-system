# Input

A single-line text field. The focus ring sits on the whole frame, so icons and units stay inside it.

## The consumer provides

- Standard input props (`value`, `onChange`, `type`, `placeholder`, `name`).
- `size`: `sm` 32px for filter bars and tables, `md` 40px default, `lg` 48px for the marketing search bar.
- `start` / `end`: an icon, a currency sign, a unit or a small clear button.
- `invalid`: set by Field when there is an error; set it yourself only outside a Field.

## Do

- Always give it a label: through Field, or `aria-label` when the context is obvious (a search box with a search icon).
- Placeholders show an example, never the label.

## Level

Atom (atomic design). See README.md, Components.
