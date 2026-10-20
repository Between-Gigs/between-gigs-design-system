# ModuleCard

A module in the Workspace hub: status, version, live preview, the open action and build progress.

## The consumer provides

- `title`, `status` (StatusBadge vocabulary), `version`.
- `preview`: a screenshot URL. It sits on `surface-embed`, so light screenshots look the same in both themes.
- `action`: the open Button (secondary, full width, `ArrowUpRight`). Omit for modules that haven't started.
- `pin`: a pin IconButton. `progress`: `{ value, label }` with the stage word ("Building", "Planned").
- `selected`: the module in focus in Coverflow.

Coverflow's tilt and depth belong to the Coverflow layout, not to the card. The card itself stays flat.
