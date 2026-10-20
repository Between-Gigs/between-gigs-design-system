# QA report

Run with `npm run qa` on version 1.2.0. Every component preview is tested in light and dark.

## Results

| Check | Result |
| --- | --- |
| Contrast, 130 text/ground pairs in both themes (`npm run tokens`) | 130 pass |
| axe-core accessibility audit, 51 previews × 2 themes | 0 violations, 0 render errors |
| Keyboard and screen-size tests | 33 of 33 pass |
| Detail inspection (`scripts/qa/inspect.mjs`): double or missing focus rings, unstyled native options, targets under 24px, clipped text — every preview plus the showcase, desktop and phone | 0 findings |
| Contrast of checked and on states (checkbox, radio, switch, slider) | 6.8:1 light, 11.7:1 dark |
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
| Minor | Heading levels skipped inside page layouts | Fixed: `headingLevel` |
| Minor | Module card selection mouse-only; Menu replaced the trigger's onClick | Fixed |

## Issues found in the 1.2 detail inspection, all fixed

| Severity | Issue |
| --- | --- |
| Serious | Double focus ring on inputs and selects wherever a page sets an unlayered focus style (the showcase did) |
| Serious | Native option lists unreadable in dark theme: OS-white background with light text |
| Serious | Checked checkbox, chosen radio and switch-on at 1.6:1 against white in light theme |
| Moderate | Prompt bar drew a second ring around its buttons |
| Moderate | Click targets under 24px: Switch, Tag remove, breadcrumb links, table sort headers, module and workspace links |
| Minor | Slider focus drew a sharp box around the whole track |
| Minor | Loading buttons looked disabled |
| Minor | AvatarGroup overlap hid initials at small size; Menu clipped two-line items |

## Known gaps

- **Not yet integrated into the production dashboard.** The components have been tested in isolation and in the AppShell layout, not in the client's codebase.
- **Icons:** Lucide is proposed and used in previews; the illustrated category icons are not yet documented.
- **Missing components:** charts, date picker and calendar, file upload, multi-select, rich-text toolbar, split view, Coverflow, funnel canvas (zoom/pan), version compare, video call seats, material and pointer pickers, notifications, comments.
- **No screen templates for now.** The 1.1 templates were removed in 1.2 and can be restored from commit `a9b1b5f`.
- **No visual regression tests yet;** the axe and keyboard tests catch behavior, not pixel changes.
- **No high-contrast theme or compact density yet.**
