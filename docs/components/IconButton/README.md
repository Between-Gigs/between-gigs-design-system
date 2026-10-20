# IconButton

A square button that shows only an icon, for toolbars and dense headers where the icon is universally understood.

## The consumer provides

- `label` (required): the accessible name, also shown as the native tooltip. Say what it does: "Notifications", not "Bell".
- `icon`: one Lucide icon.
- `variant`: `ghost` (default, toolbars), `secondary` (stands alone), `primary` (a single add action), `strong`.
- `size`: `sm` 32px or `md` 40px.
- `pressed`: for toggles such as layout modes and sketch tools.

## Use when

- The icon is unambiguous (search, close, more, layout). Otherwise use a Button with a label.
- Wrap in Tooltip when the action needs more than one word or has a shortcut.
