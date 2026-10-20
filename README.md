# Between Gigs Design System

Tokens, a Tailwind CSS v4 theme and 50 React components for the Between Gigs dashboard, marketing site and onboarding, in light and dark.

- **Brand book:** [BRAND.md](BRAND.md) (principles, content, color, type, layout, states, accessibility)
- **Logo:** [LOGO.md](LOGO.md) · **Icons:** [ICONS.md](ICONS.md) (Lucide) · **Materials:** [MATERIALS.md](MATERIALS.md)
- **Component guides:** [docs/components/](docs/components) (one README and live preview each)
- **Showcase:** [between-gigs.github.io/between-gigs-design-system](https://between-gigs.github.io/between-gigs-design-system/), built from [docs/showcase/index.html](docs/showcase/index.html), a static page that runs every component live. `.github/workflows/pages.yml` republishes it on every push to `main`.
- **QA report:** [docs/QA.md](docs/QA.md) · **Changes:** [CHANGELOG.md](CHANGELOG.md)

## What's inside

| Path | What |
| --- | --- |
| `tokens/build-tokens.py` | The single source of every token value. Writes everything below and checks contrast. |
| `tokens/tokens.json` | All tokens: 93 colors (light and dark), 19 type styles, 74 scale values. |
| `tokens/contrast-report.json` | 130 text/ground pairs with their contrast ratios, both themes. |
| `styles/between-gigs.css` | The Tailwind v4 theme the app imports. |
| `src/templates/` | Page templates built from the components (`ComingSoon`). |
| `src/components/` | 50 components, TypeScript, one file each. No runtime dependency besides React. |
| `fonts/`, `logos/` | Sora, Figtree, Newsreader, JetBrains Mono (woff2); approved logo SVGs. |
| `scripts/` | Docs bundle, previews, showcase, raw-value lint, QA (axe and keyboard tests). |

## Use it in the app

```css
/* src/styles/app.css */
@import "tailwindcss";
@import "../../design-system/styles/between-gigs.css";
```

Copy or link `src/components` (for example as `@/ui`) and import from it:

```tsx
import { AppShell, Button, Field, Input, StatusBadge, ToastProvider } from "@/ui";
```

- Set `data-theme="light"` or `"dark"` on `<html>`; with no attribute the OS setting decides. Brand sections set `data-theme="dark"` on their own element.
- Install `lucide-react` for interface icons. Components take icons as props, so the set can change later.
- Mount `<ToastProvider>` once at the root. Call `useCommandShortcut` once to open the CommandPalette with ⌘K / Ctrl+K.
- `fonts/` must be served next to the CSS (the theme references `../fonts/`).

## Rules for code

- Components use semantic utilities (`bg-surface`, `text-ink-muted`, `border-line`). Primitives (`forest-800`, `mint-500`) are for brand artwork only.
- No hex values, `rgb()` literals or arbitrary values like `p-[13px]` in `src/`. `npm run lint:values` fails the build if one appears. If a value is missing, add a token in `tokens/build-tokens.py`.
- Never edit `styles/between-gigs.css` or `tokens/tokens.json` by hand. Run `npm run tokens`.

## Scripts

| Command | What it does |
| --- | --- |
| `npm run tokens` | Rebuild tokens and theme CSS; fails if any contrast pair drops below its minimum. |
| `npm run typecheck` | TypeScript over the components. |
| `npm run lint:values` | Block raw colors and arbitrary values in `src/`. |
| `npm run build` | All of the above, plus the docs bundle, component previews and showcase. |
| `npm run qa` | axe accessibility audit on every component preview in both themes, plus keyboard and screen-size tests. |
| `npm run check` | `build` then `qa`. Run it before every merge. |

QA uses Playwright's Chromium: run `npx playwright install chromium` once if it isn't installed.

## Components

**Actions** Button · IconButton · SegmentedControl · Switch
**Forms** Field · Input · Textarea · Select · Combobox · Checkbox · RadioGroup · Slider
**Display** Badge · StatusBadge · Tag · Count · Avatar · AvatarGroup · Progress · Card · Stat · Accordion · Kbd
**Feedback** Banner · Toast · Tooltip · Skeleton · EmptyState
**Navigation** Tabs · Breadcrumbs · Pager · NavItem · Stepper · CommandPalette
**Overlays** Menu · Popover · Modal · Drawer · ConfirmDialog
**Data** Table
**Layout** AppShell (TopBar, ModuleBar, Sidebar, Inspector, PromptBar) · FilterBar
**Patterns** PageHeader · ModuleCard · WorkspaceTile · FunnelStepCard · FlowConnector · ProfileCard · StageStats
**Brand** Logo
