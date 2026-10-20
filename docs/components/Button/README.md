# Button

Triggers an action. Five variants, each with one job, so a person can tell at a glance which button matters.

## Variants

- `primary`: the one mint action per view ("Claim a card", "Save changes", "Search"). Never two on the same screen.
- `strong`: the decisive step inside a flow or review ("Create my profile", "Approve profile"). Forest in light theme, near-white in dark.
- `secondary`: outline. Every other visible action ("Export", "How it works", "Request changes").
- `ghost`: toolbar and low-emphasis actions ("Undo", "Cancel" inside dense panels).
- `danger`: destructive actions. Always confirm inside the page first.

## The consumer provides

- `children`: the label. Sentence case, a verb that says what happens.
- `variant`, `size` (`sm` 32px, `md` 40px, `lg` 48px for marketing and the search bar).
- `iconStart` / `iconEnd`: 16px Lucide icons. Use `ArrowUpRight` on the end only for links that leave the page.
- `loading`: keeps the label, adds a spinner, blocks clicks.

## Don't

- Don't make a primary button to fill space. If you're unsure which one is primary, the screen has too many actions.
- Don't replace the label with "Loading…".
- Don't put two primary or two danger buttons next to each other.
