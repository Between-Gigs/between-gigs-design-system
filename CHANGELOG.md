# Changelog

## 1.2.0 — October 2026

### Removed
- The six screen templates (Workspace hub, Funnel Studio, Profile review, Profile builder, Sign in, Founding 20), for now. The components they used all remain. They are in the history at commit `a9b1b5f` (`src/templates/`) if they come back.
- The showcase's Templates section and template detail view.

### Fixed (detail inspection)
- **Select's list box was the operating system's** (square corners, gray placeholder row, system border) and couldn't match the theme. Select now draws its own list, the same rounded, raised surface as Menu and Combobox, with full keyboard support (arrows, Home/End, Enter/Space, Escape, type-to-jump) and a hidden input for forms. New `onValueChange`; `onChange` still fires with `{ target: { value } }`.
- **Dropdowns clipped inside cards, scrolling panels and dialogs.** Select, Combobox, Menu and Popover now open in the browser's top layer (`useAnchoredLayer` in `layer.ts`), pinned to their anchor, and flip above it when there's no room below.
- **Double focus ring on inputs and selects** in pages that set their own unlayered focus style: the frame now lights only for its own field, and the showcase's page styles moved into the base layer so component styles win.
- **Unreadable native option lists** in dark theme: Select options now take `surface-raised` and `ink`.
- **Prompt bar showed two rings** when a button inside it had focus.
- **Checked checkbox, chosen radio and switch-on were 1.6:1 in light theme.** They now use `ink-brand` (6.8:1 light), checked by the token build.
- **Slider focus** is a ring around the thumb instead of a box around the track.
- **Loading buttons looked disabled.** They keep their color, show the spinner and ignore clicks.
- **Click targets under 24px** (WCAG 2.5.8): Switch is now 44×24, Tag remove 24×24, and breadcrumb, table-sort, module-title and workspace links have 24px hit areas without moving the layout.
- **Funnel row looked broken**: white preview boxes, arrows at different heights, step types cut off and the last card clipped. FunnelStepCard now shows a quiet placeholder (step-type glyph, "No preview yet") when there's no screenshot, prints the full step type, and puts the status badge in a footer row so badges line up. New `fluid` prop lets cards share a row. FlowConnector labels sit above the line and never wrap, so every arrow stays on one centerline.
- **Showcase handover row**: removed the leftover "Next / Roadmap" tile, and the "In the box" list now fills its tile instead of leaving an empty band under it. The page declares UTF-8 so separators render when opened as a file.
- New `scripts/qa/inspect.mjs` runs in `npm run qa`: flags double or missing focus rings, unstyled native options, small targets and clipped text on every preview and the showcase.

### Changed
- Small-screen QA now runs on the AppShell preview: the inspector and navigation drawers are checked at 1440, 1180, 900 and 400px. The ModuleCard preview checks keyboard selection.

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
