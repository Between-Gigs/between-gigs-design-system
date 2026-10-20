# Motion

Motion makes Between Gigs feel like one place you move through, not a stack of screens. It's built on the browser's own **View Transitions API** (page transitions, shared-element morphs, the theme reveal) and an IntersectionObserver for scroll effects. No animation library.

Everything here turns off under `prefers-reduced-motion`: changes happen instantly and content simply shows. Nothing ever depends on an animation finishing.

## Tokens

| Token | Value | Use |
| --- | --- | --- |
| `duration-instant` · `fast` · `base` · `slow` | 80 · 140 · 200 · 320ms | Controls, menus, modals (unchanged). |
| `duration-deliberate` | 480ms | Card fans, marketing reveals. |
| `duration-page` | 640ms | Page transitions, morphs, the theme reveal, scroll reveals. |
| `ease-standard` · `enter` · `exit` · `spring` | | As before; `spring` only for `pop`. |

## Page transitions

```tsx
import { useViewTransition } from "@/motion";

const go = useViewTransition("slide");
<Tab onClick={(e) => go(() => setTab("studio"), e.currentTarget)} />
<main className="vt-page">…</main>
```

Put `vt-page` on the content region. Only it moves; the shell (top bar, sidebar, module tabs) holds still, so it feels like moving between rooms of one house. Pass `"back"` as the third argument on back navigation.

| Effect | Feels like | Use for |
| --- | --- | --- |
| `slide` | Sideways to a neighbour | Tabs, steps, peers. The default. |
| `push` | Drilling in; the old page sinks | List → detail, hub → module. |
| `zoom` | Stepping into something | Opening an item from a grid. |
| `reveal` | A circle of the new page grows from the click | Big moments: publish, launch, switching workspace. |
| `wipe` | The new page draws across | Before/after, version switches. |
| `flip` | The page turns over | Front/back of a card, settings. Once per flow. |
| `dissolve` | Blur and melt | Changing mode (Studio → Preview). Sparingly. |

One effect per kind of move, the same everywhere.

## Shared-element morphs

Give the element you click and the element it becomes the same `view-transition-name` (`morph`) on either side of the change, and the browser animates one into the other. The showcase's tiles grow into their detail pages this way, and the Coming soon frame grows into the full page.

## Theme reveal

`ThemeToggle` (and `useTheme().setTheme(theme, origin)`) switch `data-theme` inside a view transition, so the new theme grows as a circle from the switch.

## Scroll effects

| Component | What it does |
| --- | --- |
| `Reveal` | Content arrives as it scrolls into view: `fade-up`, `scale-in`, `blur-in`, `slide-left`, `slide-right`, `clip-up`, `tilt-in`, `pop`. Stagger with `delay={i * 60}`. |
| `ScrollProgress` | A mint reading-progress bar, for the page or a scrolling panel. |
| `Parallax` | Decorative art drifts at a different speed. Never text or controls. |

Use reveals on marketing pages, section openers and card grids, not on app chrome, tables or anything people need on load. Keep one or two reveal effects per page.
