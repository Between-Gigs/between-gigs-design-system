# QA report

Run with `npm run qa` on version 1.1.0. Every component preview and template is tested in light and dark.

## Results

| Check | Result |
| --- | --- |
| Contrast, 130 text/ground pairs in both themes (`npm run tokens`) | 130 pass |
| axe-core accessibility audit, 57 previews × 2 themes | 0 violations, 0 render errors |
| Keyboard and screen-size tests | 34 of 34 pass |
| Raw colors or arbitrary values in `src/` | none |
| TypeScript strict | passes |

Page-level axe rules (document title, language, main landmark, h1) are skipped for previews because each one is a fragment of a real page; the app provides those.

## Issues found in 1.0 and fixed in 1.1

| Severity | Issue | Status |
| --- | --- | --- |
| High | Inspector hidden below 1280px with no way to open it; "Approve profile" unreachable on laptops | Fixed: inspector drawer |
| High | Sidebar hidden below 1024px with no menu button; phone layout scrolled sideways | Fixed: navigation drawer, responsive top bar |
| Serious | Clickable table rows unreachable by keyboard | Fixed |
| Serious | Search input inside `role="menu"` (company switcher) | Fixed |
| Serious | Dark theme `ink-subtle` on highlighted menu items at 4.45:1 | Fixed: 4.77:1 |
| Moderate | Tabs referenced panels that weren't rendered | Fixed |
| Moderate | Two unnamed complementary landmarks; prompt bar outside any landmark | Fixed |
| Minor | Heading levels skipped in templates | Fixed: `headingLevel` |
| Minor | Module card selection mouse-only; Menu replaced the trigger's onClick | Fixed |

## Known gaps

- **Not yet integrated into the production dashboard.** The components have been tested in isolation and in the templates, not in the client's codebase.
- **Icons:** Lucide is proposed and used in previews; the illustrated category icons are not yet documented.
- **Missing components:** charts, date picker and calendar, file upload, multi-select, rich-text toolbar, split view, Coverflow, funnel canvas (zoom/pan), version compare, video call seats, material and pointer pickers, notifications, comments.
- **Missing templates:** Writing Studio, Campaign Studio, material library, People & profiles, email previews, settings, error pages.
- **No visual regression tests yet;** the axe and keyboard tests catch behavior, not pixel changes.
- **No high-contrast theme or compact density yet.**
