# StatusBadge

The product's fixed status vocabulary. Each word always appears in the same color, everywhere.

| status | Word | Tone |
| --- | --- | --- |
| `draft` | Draft | warning |
| `not-started` | Not started | neutral |
| `working` | Working | info |
| `preview` | Preview | info |
| `needs-review` | Needs review | warning |
| `changes-requested` | Changes requested | warning |
| `approved` | Approved | success |
| `published` | Published | success |
| `live` | Live | success |
| `archived` | Archived | neutral |

## The consumer provides

- `status`: one of the keys above. A new status is a design decision: add it to `statusMeta` and the README's status table together.

## Level

Atom (atomic design). See README.md, Components.
