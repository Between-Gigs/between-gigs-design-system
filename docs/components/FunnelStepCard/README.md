# FunnelStepCard

One step on the Funnel Studio canvas: what kind of step it is, its order, status, a preview and what happens there.

## The consumer provides

- `type`: `traffic`, `page`, `form`, `email` or `marketplace`. Each has a fixed label, category color and icon (`stepTypes`), shown as the top stripe, a dot and the empty-preview icon.
- `status` shows as a badge in the preview's top-right corner, so the header always has room for the full step type.
- `step` (shown as "03"), `title`, `status`.
- `description`: what the step does, with an arrow to the next step ("Name, email, ZIP → reserved email").
- `preview`: a screenshot. It sits on `surface-embed` so light pages and emails look true in both themes. Without one, a quiet dashed placeholder shows the step type's icon instead of an empty white box.
- `hint`: a short footer note. `selected`: the step shown in the inspector. `onOpen`: opens the draft.
- `fluid`: the card grows to share the row (min 192px). Without it the card is a fixed 224px, for canvases that scroll.

Connector lines between steps belong to the canvas, drawn in `line-strong` with labels in `caption`.
