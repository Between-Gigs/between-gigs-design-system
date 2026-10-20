# Progress

Shows how far something has come: a module's build, founding cards claimed, an upload.

## The consumer provides

- `value` and `max` (default 100).
- `label`: what is progressing. `valueText`: the end text ("55% est.", "6 of 20"); defaults to the percentage.
- `size`: `sm` (6px) in cards, `md` (10px) as a page's headline progress.

The fill is `ink-brand`, so it holds 3:1 against its track in both themes. Never show progress you can't measure; use a Skeleton or spinner instead.
