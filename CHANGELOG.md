# Changelog

## 1.6.2 — October 2026

### Changed
- **ComingSoon copy** matches the live brand: eyebrow "Extraordinary talent. Everyday solutions.", headline "Coming soon.", line "Los Angeles Call Sheet".
- **ComingSoon has one call to action**, "Get on the call sheet ↗", instead of the email form. It is a link (`ctaHref`, default `#call-sheet`) styled as the primary button, with an optional `onCta`. `onJoin` is removed.

## 1.6.1 — October 2026

### Changed
- **Motion is calmer and more realistic.** Scroll reveals travel 8-16px instead of up to 56px, scale from 0.97 instead of 0.6, blur 6px instead of 16px, and tilt 8 degrees instead of 24, over 520ms with a soft ease-out. `duration-page` is 460ms (was 640ms). The page templates use one gentle fade-up throughout, without pops, tilts or pings.
- New page effect **`shift`**, the quiet default for steps inside a flow: the old step fades out in 140ms with an 8px nudge, the new one fades in over 300ms with a 12px nudge.
- Onboarding steps use `shift`, scroll instantly instead of smoothly, and no longer replay entrance effects. Chip pickers keep a fixed-width +/✓ slot, so picking a chip never reflows the others.

### Fixed
- Step transitions animated the step content across the page whenever Continue was pressed below the card's top (the page scrolled up, and the content travelled about 450px), and cross-faded the whole page between the two scroll positions. During region transitions the rest of the page now switches instantly, and `shift` fades in place.
- The prototype's route fade no longer runs during step and theme transitions.

## 1.6.0 — October 2026

### Added
- **Between Gigs page templates** (`src/templates/gigs/`), rebuilt from the client's review prototypes A, B and C on the system and taken further:
  - **SearchResults**: brand hero with the people floating in, a search bar lifted over its edge, service pills with counts, availability / budget / distance filters, sort, list or grid, save, an empty state, an illustrative neighbourhood map whose pins light up with the card you hover, and How it works. Filters, search and sort re-flow the results with a view transition.
  - **GigsterProfile**: portrait hero over an ambient glow taken from the person's own work, a sticky booking card, section tabs that follow the scroll, What I can help with, services, a bento portfolio with a keyboard lightbox, example reviews, experience, FAQs and similar professionals. Request opens a validated form; nothing is sent.
  - **GigsterOnboarding**: five steps with a stepper and progress, chip pickers for skills, services and areas, "Another market" and private "Other" requests, per-step validation with a summary, a review step with Edit, a live preview card that updates as you type, and a finish moment. Steps slide forward and back.
  - **GigsApp**: all three as one clickable prototype. The header holds still, pages cross-fade, and a portrait flies from its search card into the profile and back. `docs/showcase/app/` serves it on its own with linkable routes (`#/profile/maya`).
- Six fictional people with copy, rates and imagery taken from the PDFs (`docs/showcase/app/img/`, cropped from the review screenshots).
- Showcase section 05 · Templates: live previews of all three pages and "Open the prototype" / "Try it", which run the prototype full screen inside the page.
- `startPageTransition` takes a `target`, for pages that hold more than one `vt-page` region.

### Fixed
- The raw-value lint now checks subfolders (it skipped them before).
- Hand-built controls use `transition` rather than `transition-all`, so the focus outline shows the moment a control is focused.

## 1.5.0 — October 2026

### Added
- **ThemeToggle** (atom) and **useTheme**: the Day/Night switch, now a library component. It sets `data-theme` on `<html>`, remembers the choice, and reveals the new theme as a circle growing from the switch.
- **Motion** (`src/motion/`, MOTION.md): `useViewTransition` / `startPageTransition` with seven page transitions (reveal, slide, push, zoom, flip, wipe, dissolve) on the View Transitions API; shared-element morphs; `Reveal` with eight scroll effects; `ScrollProgress`; `Parallax`. New token `duration-page` (640ms). All of it off under reduced motion.
- **Atomic design levels**: every component is an atom, molecule, organism or template, stated in its README and the README's component list.
- **create-icon skill** (`.claude/skills/create-icon/`): when Lucide has no icon for something, Claude draws one on Lucide's grid, validates it (`npm run icons:check`), previews it beside Lucide icons at 16/20/24px in both themes, and wires it in. First icon made with it: `FoundingCardGlyph`.
- **Glow utilities**: `glow-horizon`, `glow-text`, `glow-hover`, `glow-focus`, for dark launch surfaces.
- **Showcase**: section 03 · Motion with live demos, the library ThemeToggle in the top bar, a scroll-progress bar, tiles and headings that reveal on scroll, a drifting hero mark, and tiles that morph into their detail pages.

### Changed
- **ComingSoon** sits on a curved panel with a mint horizon glow; the button and field glow on hover and focus. Footer `links` and `copyright` are props (no invented contact details).
- "Open full page" opens the template full screen inside the showcase, morphing out of its frame, instead of a separate file that could load blank in the hosted preview.
- Counts on the showcase and README now match the data: 187 tokens (75 scale), 138 contrast pairs, 51 components.

## 1.4.0 — October 2026

### Added
- **Templates are back, starting with `ComingSoon`** (`src/templates/`): a simple teaser page before launch: headline, one line of copy and an email capture with validation and a confirmation. Built only from system components. Exported as `Templates.ComingSoon` in the docs bundle.
- **`backdrop-europium`**: a quiet Europium phosphor field for teaser and launch pages: faint mint grain with a soft glow at the bottom edge. See MATERIALS.md.
- **ICONS.md**: the icon reference. Interface icons are Lucide (`lucide-react`), passed into components as props; sizes, stroke, color and labelling rules, the built-in glyphs, and every icon in use with its meaning. The showcase has a live Icons tile.
- **Showcase section 04 · Templates**: the Coming soon page rendered live in a browser frame, plus a full-screen version at `templates/coming-soon.html`.

### Changed
- Built-in glyphs (chevrons, check, close, status icons) now use a 2px stroke, the same as Lucide.

### Removed
- **Dots in badges.** `Badge` no longer has a `dot` prop and `StatusBadge` no longer draws one: the tone color and the word carry the status. The category dot in the FunnelStepCard header is gone too; the card's top stripe already shows the step type.

## 1.3.0 — October 2026

### Added
- **Rare-earth materials**: `material-neodymium`, `material-europium`, `material-didymium` and `material-holmium`, procedural presets for the material layer with no image files. Europium glows only in dark; Holmium shifts from sand (light) to rose (dark). See MATERIALS.md.
- **Showcase Day/Night switch** in the top bar: a sliding sun and moon with a circular reveal (instant under reduced motion). The choice is remembered per browser.
- **Showcase rare-earth tile**: the four finishes as periodic-table cells at full strength, with a highlight that follows the pointer.

### Changed
- The showcase is now a complete standalone HTML document (doctype, viewport, language), so it renders the same on GitHub Pages as in the hosted preview. The hero stays a dark brand panel in both modes.

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
