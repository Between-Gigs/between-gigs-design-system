---
name: create-icon
description: Draw a new interface icon for the Between Gigs design system when Lucide has nothing that fits (a product concept like "founding card", "gig call sheet", "costume rack"). Produces a Lucide-compatible 24px outline SVG, validates it, previews it beside real Lucide icons in both themes, and wires it into the component library and ICONS.md. Use whenever someone asks for an icon that doesn't exist yet, says "make an icon for…", or a design needs a glyph the set lacks.
---

# Create an icon

The system's icons are [Lucide](https://lucide.dev). A custom icon must be indistinguishable in style from Lucide, so it can sit in a toolbar next to `Search` and `Download` without looking borrowed.

## 0. Check it really doesn't exist

Search Lucide first: `node -e "const l=require('lucide-react');console.log(Object.keys(l).filter(k=>/WORD/i.test(k)).join(' '))"` (replace WORD with a few synonyms), and look at https://lucide.dev/icons. Also check `ICONS.md` → "Icons in use" and the built-in glyphs in `src/components/icons.tsx`. If something fits, use it and stop. Tell the person which one and why.

## 1. Pin down the meaning

Write one line: what the icon means and where it appears ("Founding card: a numbered member card, shown in the Founding 20 nav item and card wall"). One icon, one meaning. Pick a metaphor a person recognises at 16px: a simple object, seen from the front, no scene.

## 2. Draw it on Lucide's grid

Write `icons/custom/<kebab-name>.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect x="3" y="5" width="18" height="14" rx="2" />
  <path d="M7 15h4" />
</svg>
```

Rules (the validator checks the first six):

1. `viewBox="0 0 24 24"`, `fill="none"`, `stroke="currentColor"`, `stroke-width="2"`, round caps and joins, all on the root `<svg>`.
2. Only `path`, `rect`, `circle`, `ellipse`, `line`, `polyline`, `polygon`. No `text`, `style`, `class`, `transform`, gradients, images or colors.
3. Keep every coordinate inside 2–22 (Lucide's 2px padding). Live area is 20×20.
4. At most 6 shapes, numbers with at most 2 decimals. Fewer strokes read better at 16px.
5. Corners: `rx="2"` on rectangles the size of a card or screen, `rx="1"` on small ones. Arcs and curves over sharp angles.
6. Gaps between parallel strokes at least 2px (they merge at 16px otherwise).
7. Optical weight: a closed shape should fill roughly 18×18 (squares) or 20×16 (wide objects); circles about r=9 or r=10. Compare with `Calendar`, `Mail`, `Wallet`.
8. Detail goes inside the outline as short lines or a small circle, never as fills.

## 3. Validate and preview

```sh
node scripts/check-icons.mjs                    # checks every icons/custom/*.svg
node scripts/icon-preview.mjs <kebab-name>       # writes qa-output/icon-<name>.png
```

Open the PNG (Read tool). It shows the icon at 16, 20 and 24px beside `Calendar`, `Mail`, `Wallet`, `Layers` and `Star`, on light and dark grounds. Check: same stroke weight, same visual size, nothing blurry or merged at 16px, reads as the meaning from step 1. Iterate on the SVG until it does. Show the person the PNG.

## 4. Wire it in

1. Add a component to `src/components/icons.tsx`, copying the SVG's children, named `<Pascal>Glyph`:
   ```tsx
   export const FoundingCardGlyph = (props: GlyphProps) => (
     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" aria-hidden="true" {...props}>
       <rect x="3" y="5" width="18" height="14" rx="2" /><path d="M7 15h4" />
     </svg>
   );
   ```
   Match the existing glyphs' signature in that file.
2. Export it from `src/components/index.ts` next to the other glyphs if consumers need it, and add it to `Icons` in `scripts/bundle-entry.ts` so the showcase Icons tile shows it.
3. Add a row to `ICONS.md` → "Built-in glyphs" with the name and its one-line meaning.
4. Run `npm run check`.

## Don'ts

- Don't trace or copy icons from other sets (Material, Phosphor, Heroicons); draw it.
- Don't add a filled variant, a color, or a second stroke width.
- Don't make one icon carry two meanings, or two icons share one.
