# FunnelStudio

Template: Funnel Studio. A campaign's steps left to right on a recessed canvas, traffic sources stacked at the start, the selected step in the inspector.

## Built from

HubFrame, PageHeader with Breadcrumbs, Tag (step-type filters), FunnelStepCard, FlowConnector, Inspector, StatusBadge, Select, Banner, Button.

## Rules this screen shows

- The canvas is `surface-sunken` with `radius-xl`; it scrolls sideways inside its frame, never the page.
- Each step type keeps its category color (`stepTypes`) in the stripe, the dot and the filter label.
- Connectors are labelled with what the person does next ("Claims a card", "Books"). Dashed connectors lead to steps that aren't built.
- Draft campaigns say so in a warning Banner; no counts are shown until there is live traffic.
