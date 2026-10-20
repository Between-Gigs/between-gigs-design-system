# FlowConnector

The arrow between two steps on a flow or funnel canvas, with an optional label for what the person does to move on.

## The consumer provides

- `label`: a short verb phrase ("Claims a card", "Books").
- `variant`: `solid`, or `dashed` for paths to steps that aren't built or are optional.

Place it between two cards in a flex row; it stretches to fill the gap. The label sits above the line and never wraps, so every arrow in a row stays at the same height. Keep labels to two or three words. It is drawn in `line-strong`, so it holds 3:1 on the canvas.
