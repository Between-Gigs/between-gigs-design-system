# FunnelStepCard

One step on the Funnel Studio canvas: what kind of step it is, its order, status, a preview and what happens there.

## The consumer provides

- `type`: `traffic`, `page`, `form`, `email` or `marketplace`. Each has a fixed label and category color (`stepTypes`), shown as the top stripe and a dot.
- `step` (shown as "03"), `title`, `status`.
- `description`: what the step does, with an arrow to the next step ("Name, email, ZIP → reserved email").
- `preview`: a screenshot. It sits on `surface-embed` so light pages and emails look true in both themes.
- `hint`: a short footer note. `selected`: the step shown in the inspector. `onOpen`: opens the draft.

Connector lines between steps belong to the canvas, drawn in `line-strong` with labels in `caption`.
