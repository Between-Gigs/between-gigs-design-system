# CommandPalette

⌘K: jump to any module, company or action by typing.

## The consumer provides

- `open`, `onClose`, `commands`: `{ id, label, group, onRun, icon?, keywords?, shortcut? }[]`. Groups appear in the order first used.
- Call `useCommandShortcut(open)` once near the app root so ⌘K (Ctrl+K on Windows) opens it.

Arrow keys move, Enter runs, Escape closes. Keep labels the same as the page titles they lead to.

## Level

Organism (atomic design). See README.md, Components.
