# Changelog

## 1.1.0 — October 2026

QA fixes and eight new components.

### Fixed
- **Inspector unreachable below 1280px.** The inspector now becomes a right drawer, opened by `ShellInspectorButton` or by selecting a row (`inspectorOpen` / `onInspectorOpenChange` on AppShell). Profile review's "Approve profile" works on laptops, tablets and phones.
- **No navigation below 1024px.** The sidebar becomes a left drawer, opened by `ShellMenuButton` in the top bar. The top bar trims itself on small screens, so phones no longer scroll sideways.
- **Table rows not reachable by keyboard.** Clickable rows are focusable and open with Enter or Space.
- **Menu with a search box broke screen readers.** The header now sits outside the `role="menu"` list. Menu and Popover also keep the trigger's own click handlers.
- **Dark theme: secondary text on highlighted menu items was 4.45:1.** `ink-subtle` (dark) moved from `#8aa596` to `#8fab9b`; it now passes at 4.77:1. The token build checks text on hover states permanently.
- **Tabs pointed screen readers at panels that weren't rendered.** Only the selected tab references its panel.
- **Unnamed landmarks.** Sidebar and Inspector are named; the prompt bar is a named region.
- **Heading levels skipped.** Cards, tiles, StageStats and EmptyState take `headingLevel`; templates use it.
- **Module cards selectable by mouse only.** `ModuleCard` takes `onSelect`, which makes the title a button.

### Added
- Drawer, Popover, Accordion, Combobox, CommandPalette (with `useCommandShortcut`), ConfirmDialog, AvatarGroup, Kbd.
- Modal `placement="left"`.
- The hub frame has a ⌘K command palette and an Appearance popover.
- Repository tooling: `npm run check` (tokens, type-check, raw-value lint, docs build, axe audit, keyboard tests), contrast report, showcase assembly.

## 1.0.0 — October 2026

First release: tokens in light and dark, Tailwind v4 theme, 42 components, 6 templates, brand book, logo and materials rules.
