"""Between Gigs design tokens. This file is the single source of every token value.

Run `python3 tokens/build-tokens.py` (or `npm run tokens`). It writes:
  tokens/tokens.json        every token, for tools and the design-system page
  styles/between-gigs.css   the Tailwind v4 theme the app imports
  styles/docs-theme.css     the theme used to build the docs bundle
and checks WCAG contrast for every text/ground pair in both themes. It exits non-zero if a pair fails."""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- primitives
PRIMS = [
  # forest: the brand's deep green, logo ink on light
  ("forest-50",  "#eef6f1", "Lightest forest tint. Selected rows and soft brand washes in light theme."),
  ("forest-100", "#d9ecdf", "Light forest tint. Hover on selected items, light-theme brand panels."),
  ("forest-200", "#b3d8c2", "Forest tint for borders on brand washes."),
  ("forest-300", "#82bd9c", "Mid-light forest. Decorative only; not for text on light grounds."),
  ("forest-400", "#4f9a74", "Mid forest. Decorative only."),
  ("forest-500", "#2a7a53", "Forest for icons and marks on light grounds."),
  ("forest-600", "#17633f", "Strong forest. Brand-tinted text on light grounds."),
  ("forest-700", "#114e32", "Deep forest. Pressed state of forest fills."),
  ("forest-800", "#0f3d29", "THE brand forest: logo lettering on light surfaces, strong buttons in light theme."),
  ("forest-900", "#0b2b1d", "Very deep forest. Raised panels in dark theme."),
  ("forest-950", "#071a11", "Near-black forest. The dark theme's page ground."),
  # mint: the call-to-action and signal green
  ("mint-100", "#d4fbe9", "Palest mint. Highlighter wash behind words, light theme."),
  ("mint-200", "#a6f6d2", "Pale mint. Highlighter for marketing headlines (the 'deliver / today' marker)."),
  ("mint-300", "#6ff2b9", "Light mint. Hover on mint fills in dark theme."),
  ("mint-400", "#3debA0".lower(), "Bright mint. Brand accent text on dark grounds; focus ring in dark theme."),
  ("mint-500", "#1fdc8c", "THE brand mint: primary action fill in both themes. Never text on light grounds."),
  ("mint-600", "#12b873", "Pressed mint. Hover on mint fills in light theme."),
  ("mint-700", "#0b8a55", "Mint dark enough for marks and the focus ring on light grounds."),
  ("mint-800", "#086c42", "Mint as text on light grounds (links, active tab labels)."),
  # sage: neutrals biased toward green so greys never look stock
  ("sage-0",   "#ffffff", "Pure white. Card and embedded-canvas fill in light theme."),
  ("sage-50",  "#f5f8f4", "Off-white sage. Light theme page ground."),
  ("sage-100", "#ebf0e9", "Sunken wells, filter bars and input fills in light theme."),
  ("sage-200", "#dae3d8", "Hairlines in light theme."),
  ("sage-300", "#bfccbd", "Disabled borders in light theme."),
  ("sage-400", "#8a9b8b", "Disabled text in light theme. Fails 4.5:1 on purpose: never for readable copy."),
  ("sage-500", "#6c7e6e", "Strong control borders in light theme (3:1 on white)."),
  ("sage-600", "#516253", "Subtle text in light theme."),
  ("sage-700", "#3b4a3e", "Muted text in light theme."),
  ("sage-800", "#233028", "Hairlines in dark theme are built from forest, this is for neutral dark fills."),
  ("sage-900", "#0e1a13", "Near-black ink in light theme."),
  # supporting hues (status and categories pull from these)
  ("amber-100", "#fcefc4", "Draft banner and warning washes, light theme."),
  ("amber-300", "#f5cf63", "Warning marks on dark grounds."),
  ("amber-700", "#8a5a00", "Warning text on light grounds."),
  ("amber-900", "#3a2c08", "Warning wash in dark theme."),
  ("red-100",   "#fde8e5", "Danger wash, light theme."),
  ("red-300",   "#ff9a8c", "Danger text and marks on dark grounds."),
  ("red-700",   "#b3261e", "Danger text and fills on light grounds."),
  ("red-900",   "#3d1410", "Danger wash, dark theme."),
  ("blue-100",  "#e4eefb", "Info wash, light theme."),
  ("blue-300",  "#93bdf5", "Info text and marks on dark grounds."),
  ("blue-700",  "#1f5aa6", "Info text and marks on light grounds."),
  ("blue-900",  "#10233b", "Info wash, dark theme."),
  ("lime-300",  "#d6f25c", "Founding-card lime. Celebration and marketing accents only, never UI state."),
]
P = {n: v for n, v, _ in PRIMS}

# ---------------------------------------------------------------- semantic (light, dark, usage)
SEM = [
  # grounds
  ("bg",              "{sage-50}",    "{forest-950}", "Page and app-shell ground."),
  ("surface",         "{sage-0}",     "#0e2419",      "Cards, panels, table bodies: the default container on bg."),
  ("surface-raised",  "{sage-0}",     "#143024",      "Menus, popovers, modals, toasts: anything floating above a surface."),
  ("surface-sunken",  "{sage-100}",   "#05130c",      "Wells, filter bars, input fills, code blocks: recessed areas inside a surface."),
  ("surface-hover",   "#0f3d290d",    "#6ff2b912",    "Translucent hover wash laid over any surface (rows, list items, ghost buttons)."),
  ("surface-selected","{forest-50}",  "#163d2a",      "Selected row, active nav item, chosen option."),
  ("surface-brand",   "{forest-800}", "{forest-800}", "Brand band in BOTH themes: marketing heroes, the founding-card wall, sign-in panel. Text on it uses ink-on-brand."),
  ("surface-embed",   "{sage-0}",     "{sage-0}",     "Always-light stage for embedded content (sketch pad, device studio, email and page previews) inside either theme."),
  ("scrim",           "#071a1199",    "#000000b3",    "Backdrop behind modals and drawers."),
  # lines
  ("line",            "{sage-200}",   "#1f3d2d",      "Hairlines: card edges, dividers, table rules. Decorative, so below 3:1 by design."),
  ("line-strong",     "{sage-500}",   "#5b8a70",      "Control borders that must be seen: inputs, selects, outline buttons, checkboxes (3:1 on surface)."),
  ("line-dashed",     "{sage-300}",   "#2f5642",      "Empty-slot outlines (open founding cards, drop zones); always with a label."),
  ("focus",           "{mint-700}",   "{mint-400}",   "Focus ring: 2px solid plus 2px offset, on every interactive element. 3:1 on bg, surface and surface-sunken."),
  # ink
  ("ink",             "{sage-900}",   "#eaf4ee",      "Primary text and icons on bg, surface, surface-raised, surface-sunken and surface-selected."),
  ("ink-muted",       "{sage-700}",   "#a9c2b3",      "Secondary text: descriptions, metadata, table secondary columns. Same grounds as ink."),
  ("ink-subtle",      "{sage-600}",   "#8fab9b",      "Placeholders, captions, timestamps. Same grounds as ink; still 4.5:1."),
  ("ink-disabled",    "{sage-400}",   "#557463",      "Disabled labels only. Intentionally below 4.5:1 (WCAG exempts disabled controls)."),
  ("ink-brand",       "{forest-600}", "{mint-400}",   "Brand-colored text: the second headline line ('Twenty names.'), eyebrows, active nav labels. On bg and surface."),
  ("ink-on-brand",    "#eaf4ee",      "#eaf4ee",      "Text on surface-brand."),
  ("ink-on-embed",    "{sage-900}",   "{sage-900}",   "Text on surface-embed in both themes."),
  ("link",            "{mint-800}",   "#5cf2b2",      "Inline links on bg and surface. Underline at rest; never rely on color alone."),
  # actions
  ("action",          "{mint-500}",   "{mint-500}",   "Primary action fill: one per view ('Claim a card', 'Save changes', 'Search')."),
  ("action-hover",    "{mint-600}",   "{mint-300}",   "Primary action on hover."),
  ("on-action",       "#04180e",      "#04180e",      "Label and icon on action and action-hover."),
  ("action-strong",   "{forest-800}", "#eaf4ee",      "Solid confirm fill for decisive actions inside flows ('Approve profile', 'Create my profile')."),
  ("action-strong-hover","{forest-700}","#c9e6d6",    "action-strong on hover."),
  ("on-action-strong","#ffffff",      "{forest-950}", "Label and icon on action-strong."),
  ("action-danger",   "{red-700}",    "{red-300}",    "Destructive fill (Delete, Remove access)."),
  ("on-action-danger","#ffffff",      "#2a0c09",      "Label on action-danger."),
  # status
  ("success",         "#14794a",      "#5be3a0",      "Success text and icons (Approved, Published, Live). On surface and success-soft. Always paired with an icon or word."),
  ("success-soft",    "#e2f5ea",      "#0f3324",      "Success badge and banner ground."),
  ("warning",         "{amber-700}",  "{amber-300}",  "Warning text and icons (Draft, Needs review, Unsaved). On surface and warning-soft."),
  ("warning-soft",    "{amber-100}",  "{amber-900}",  "Warning badge and banner ground; the 'Draft · not public' strip."),
  ("danger",          "{red-700}",    "{red-300}",    "Error text, invalid field borders and icons. On surface and danger-soft."),
  ("danger-soft",     "{red-100}",    "{red-900}",    "Error banner and badge ground."),
  ("info",            "{blue-700}",   "{blue-300}",   "Info text and icons (Preview, Coming soon). On surface and info-soft."),
  ("info-soft",       "{blue-100}",   "{blue-900}",   "Info badge and banner ground."),
  ("neutral-soft",    "{sage-100}",   "#1a3326",      "Neutral badge ground (Not started, Planned, Archived); text is ink-muted."),
  ("highlight",       "{mint-200}",   "#1fdc8c40",    "Marker highlight behind words in headlines and search hits; text stays ink."),
  # logo inks: exact values from the approved files (on-light / on-dark). Logo only.
  ("logo-mark", "#012b18", "#03ff96", "Logo monogram and the word Gigs. Exact ink of the approved files; never use it outside the Logo."),
  ("logo-ink", "#012b18", "#f5fff8", "The word Between in the logo. Exact ink of the approved files."),
  ("logo-rule", "#799184", "#8daa99", "The thin divider in the wide logo. Exact ink of the approved files."),
  # categories (module types, workspace covers, chart series)
  ("cat-1", "#1e8a57", "#4fe0a0", "Category 1 green: Pages & experiences, chart series 1. Marks only (stripes, dots, bars), 3:1 on surface."),
  ("cat-2", "#0e7f86", "#4fd3cc", "Category 2 teal: Forms, chart series 2."),
  ("cat-3", "#2f69c9", "#86b3f3", "Category 3 blue: Traffic sources, chart series 3."),
  ("cat-4", "#7651c4", "#b9a1f2", "Category 4 violet: Claim / forms flow, chart series 4."),
  ("cat-5", "#bb3f78", "#f28dba", "Category 5 pink: Clients, chart series 5."),
  ("cat-6", "#a8700f", "#f0c14e", "Category 6 amber: Emails, chart series 6."),
  ("cat-7", "#5f7d0e", "#cbe85a", "Category 7 lime: Marketplace, chart series 7."),
  ("cat-8", "#5b6f62", "#a7bcae", "Category 8 sage: Other / uncategorised, chart series 8."),
]

# ---------------------------------------------------------------- type
FAMILIES = {
  "display": "Sora, \"Avenir Next\", \"Segoe UI\", system-ui, sans-serif",
  "sans":    "Figtree, \"Segoe UI\", system-ui, -apple-system, sans-serif",
  "serif":   "Newsreader, Georgia, \"Times New Roman\", serif",
  "mono":    "\"JetBrains Mono\", ui-monospace, \"SF Mono\", Menlo, monospace",
}
FONTS = [
  {"family": "Sora", "file": "fonts/Sora-Variable.woff2", "weight": "400 700", "style": "normal"},
  {"family": "Figtree", "file": "fonts/Figtree-Variable.woff2", "weight": "400 700", "style": "normal"},
  {"family": "Figtree", "file": "fonts/Figtree-Italic-Variable.woff2", "weight": "400 700", "style": "italic"},
  {"family": "Newsreader", "file": "fonts/Newsreader-Variable.woff2", "weight": "400 600", "style": "normal"},
  {"family": "Newsreader", "file": "fonts/Newsreader-Italic-Variable.woff2", "weight": "400 600", "style": "italic"},
  {"family": "JetBrains Mono", "file": "fonts/JetBrainsMono-Variable.woff2", "weight": "400 600", "style": "normal"},
]
# name, size, line, weight, tracking, sample, usage
TYPE = [
  ("Display", "display", [
    ("display-xl", 72, 76, 600, "-0.035em", "Be one of the first twenty.", "Marketing hero only, one per page. Second line may switch to ink-brand."),
    ("display-lg", 56, 60, 600, "-0.03em", "Twenty cards. Twenty names.", "Section openers on marketing pages and empty hub states."),
    ("display-md", 40, 46, 600, "-0.025em", "Make the next version better.", "Studio and module page titles (Writing Studio, Campaign Studio)."),
    ("display-sm", 32, 38, 600, "-0.02em", "Workspace hub", "App page titles inside the shell."),
    ("stat", 44, 48, 600, "-0.02em", "$5,000", "Big numbers in stat rows and KPI tiles. Set tabular-nums."),
  ]),
  ("Heading", "sans", [
    ("heading-lg", 22, 28, 650, "-0.01em", "People & profiles", "Panel and section titles."),
    ("heading-md", 18, 24, 650, "-0.005em", "Claim founding card No. 07", "Card titles, modal titles, drawer titles."),
    ("heading-sm", 15, 20, 650, "0em", "Connected work", "Small card titles, list group headings, inspector sections."),
  ]),
  ("Body", "sans", [
    ("body-lg", 17, 26, 400, "0em", "Hire a Hollywood professional for the projects in your everyday life.", "Marketing lead paragraphs and onboarding copy. Max 65ch."),
    ("body-md", 15, 22, 400, "0em", "Check the profile details and services, then approve or leave a note.", "Default app text: descriptions, form help, table cells."),
    ("body-sm", 13, 18, 400, "0.005em", "Silver Lake · 3 miles away · Available this week", "Metadata, card descriptions, secondary table text."),
    ("caption", 12, 16, 500, "0.01em", "Names shown are illustrative samples for this draft.", "Footnotes, helper text under charts, legal lines."),
  ]),
  ("Label", "sans", [
    ("label-md", 14, 20, 600, "0em", "Save changes", "Buttons, tabs, form labels, nav items."),
    ("label-sm", 12, 16, 600, "0.01em", "Needs review", "Badges, chips, small buttons, count pills."),
    ("eyebrow", 11, 16, 700, "0.16em", "THE FOUNDING MEMBERS WALL", "Uppercase kicker above titles, in ink-brand. Always uppercase via CSS, never typed in caps."),
  ]),
  ("Data", "mono", [
    ("data-md", 13, 18, 450, "0em", "trig_01J9 · 14 drafts · 0 ready", "IDs, counts in dense tables, code-like values."),
    ("data-sm", 11, 16, 500, "0.02em", "v3.64 · 109%", "Version tags, zoom levels, keyboard hints."),
  ]),
  ("Editorial", "serif", [
    ("editorial-lg", 22, 32, 400, "0em", "A good evening starts by turning “come hang out” into something both the host and the performer can picture.", "Article deks and pull quotes in Writing Studio and The Journal."),
    ("editorial-md", 18, 29, 400, "0em", "Every card is numbered, every project real, and every name here chose to be listed.", "Long-form article body. Max 68ch."),
  ]),
]

# ---------------------------------------------------------------- scales
SPACE = [("space-0.5",2,"Hairline gaps: icon to count badge."),("space-1",4,"Icon-to-label gap inside chips."),
  ("space-1.5",6,"Gap between stacked label and helper text."),("space-2",8,"Gap inside buttons and between chips."),
  ("space-3",12,"Inner padding of compact cards and list rows."),("space-4",16,"Default card padding and form-field gap."),
  ("space-5",20,"Panel padding in dense tools."),("space-6",24,"Panel and modal padding; gap between cards."),
  ("space-8",32,"Gap between page sections inside the app."),("space-10",40,"Page top padding under the top bar."),
  ("space-12",48,"Section spacing on marketing pages (small screens)."),("space-16",64,"Section spacing on marketing pages."),
  ("space-24",96,"Hero padding on marketing pages.")]
RADIUS = [("radius-xs",4,"Keyboard hints, tiny tags inside inputs."),("radius-sm",8,"Checkboxes, chips inside dense tables, tooltips."),
  ("radius-md",12,"Buttons, inputs, selects, segmented controls, menu items."),("radius-lg",16,"Cards, popovers, menus, toasts."),
  ("radius-xl",22,"Panels, modals, drawers, the floating prompt bar."),("radius-2xl",32,"Marketing hero cards and the founding cards."),
  ("radius-full","9999px","Pills: badges, count bubbles, avatars, toggles, progress bars.")]
SHADOW = [
  ("shadow-xs", "0 1px 2px rgba(7,26,17,0.06)", "0 1px 2px rgba(0,0,0,0.45)", "Inputs and resting buttons."),
  ("shadow-sm", "0 1px 2px rgba(7,26,17,0.05), 0 2px 8px rgba(7,26,17,0.06)", "inset 0 1px 0 rgba(234,244,238,0.04), 0 1px 3px rgba(0,0,0,0.5)", "Cards on bg. In dark theme a 4% top highlight separates the card instead of a visible shadow."),
  ("shadow-md", "0 4px 12px rgba(7,26,17,0.08), 0 12px 32px rgba(7,26,17,0.10)", "inset 0 1px 0 rgba(234,244,238,0.06), 0 8px 24px rgba(0,0,0,0.55)", "Menus, popovers, flyouts, toasts."),
  ("shadow-lg", "0 12px 24px rgba(7,26,17,0.10), 0 32px 64px rgba(7,26,17,0.16)", "inset 0 1px 0 rgba(234,244,238,0.07), 0 24px 64px rgba(0,0,0,0.65)", "Modals and drawers (always over scrim)."),
  ("shadow-glow", "0 0 0 1px rgba(18,184,115,0.55), 0 6px 24px rgba(31,220,140,0.22)", "0 0 0 1px rgba(61,235,160,0.55), 0 0 28px rgba(31,220,140,0.28)", "Selected or featured card (current funnel step, chosen study). One per view."),
]
OTHER = {
  "size": [("size-control-sm","32px","Compact controls in toolbars and tables."),("size-control-md","40px","Default buttons, inputs and selects."),
           ("size-control-lg","48px","Marketing CTAs and the search bar."),("size-icon-sm","16px","Icons inside buttons, badges and inputs."),
           ("size-icon-md","20px","Nav and toolbar icons."),("size-icon-lg","24px","Empty-state and feature icons."),
           ("size-avatar-sm","24px","Avatars in lists and seats."),("size-avatar-md","32px","Avatars in the top bar and company switcher."),
           ("size-avatar-lg","48px","Profile headers."),("size-topbar","56px","App top bar height."),
           ("size-sidebar","248px","Expanded sidebar width."),("size-rail","64px","Collapsed sidebar / icon rail width."),
           ("size-inspector","320px","Right inspector and notebook panels."),("size-content","1280px","Max width of app page content."),
           ("size-prose","680px","Max width of long-form text (about 65ch).")],
  "breakpoint": [("bp-sm","640px","Large phones; stack to one column below this."),("bp-md","768px","Tablets; sidebar becomes a drawer below this."),
           ("bp-lg","1024px","Laptops; inspector panel docks at this width."),("bp-xl","1280px","Desktops; full three-column shell."),
           ("bp-2xl","1536px","Wide screens; split view with two panes."),("bp-3xl","1920px","Studio displays; four-slot layouts.")],
  "zIndex": [("z-base","0","Page content."),("z-raised","10","Sticky table headers, selected card lift."),("z-sticky","100","Top bar and module tabs."),
           ("z-rail","200","Sidebar, icon rail, floating prompt bar."),("z-dropdown","1000","Selects, menus, flyouts."),("z-overlay","1100","Scrim."),
           ("z-modal","1200","Modals and drawers."),("z-popover","1300","Popovers opened from inside a modal."),("z-toast","1400","Toasts."),
           ("z-tooltip","1500","Tooltips."),("z-pointer","9000","Custom hub pointer.")],
  "duration": [("duration-instant","80ms","Color and opacity on press."),("duration-fast","140ms","Hover states, toggles, checkbox ticks."),
           ("duration-base","200ms","Menus, popovers, tabs indicator."),("duration-slow","320ms","Modals, drawers, panel resize."),
           ("duration-deliberate","480ms","Coverflow and card-fan moves; marketing reveals.")],
  "easing": [("ease-standard","cubic-bezier(0.2, 0, 0, 1)","Default for anything that moves and stays."),
           ("ease-enter","cubic-bezier(0, 0, 0.2, 1)","Elements arriving (menus, toasts)."),
           ("ease-exit","cubic-bezier(0.4, 0, 1, 1)","Elements leaving."),
           ("ease-spring","cubic-bezier(0.34, 1.56, 0.64, 1)","Small playful moments only: the founding-card fan, a star toggling on.")],
  "opacity": [("opacity-disabled","0.45","Disabled controls when no disabled color token fits (images, cards)."),
           ("opacity-material-subtle","0.08","Material texture strength under dense UI (tables, forms)."),
           ("opacity-material","0.16","Default material texture strength on panels and cards."),
           ("opacity-material-max","0.28","Ceiling for material texture; never higher behind text.")],
  "borderWidth": [("border-hairline","1px","Cards, dividers, inputs."),("border-strong","1.5px","Outline buttons on dark grounds."),
           ("border-focus","2px","Focus ring width (offset 2px)."),("border-selected","2px","Selected card and chosen option outline.")],
}

# ---------------------------------------------------------------- helpers
def resolve(v, theme):
    while v.startswith("{"):
        v = P[v[1:-1]] if v[1:-1] in P else dict((n, (l if theme=="light" else d)) for n,l,d,_ in SEM)[v[1:-1]]
    return v

def rgba(h):
    h = h.lstrip("#")
    r, g, b = (int(h[i:i+2], 16)/255 for i in (0, 2, 4))
    a = int(h[6:8], 16)/255 if len(h) == 8 else 1
    return r, g, b, a

def over(fg, bg):
    r, g, b, a = rgba(fg); R, G, B, _ = rgba(bg)
    return (r*a+R*(1-a), g*a+G*(1-a), b*a+B*(1-a))

def lum(c):
    f = lambda x: x/12.92 if x <= 0.03928 else ((x+0.055)/1.055)**2.4
    return 0.2126*f(c[0])+0.7152*f(c[1])+0.0722*f(c[2])

def ratio(fg, bg):
    l1, l2 = lum(over(fg, bg)), lum(over(bg, "#000000"))
    return (max(l1, l2)+0.05)/(min(l1, l2)+0.05)

CHECKS = [  # fg, grounds, minimum
  ("ink", ["bg","surface","surface-raised","surface-sunken","surface-selected"], 4.5),
  ("ink-muted", ["bg","surface","surface-raised","surface-sunken","surface-selected"], 4.5),
  ("ink-subtle", ["bg","surface","surface-raised","surface-sunken"], 4.5),
  ("ink-brand", ["bg","surface"], 4.5),
  ("link", ["bg","surface"], 4.5),
  ("ink-on-brand", ["surface-brand"], 4.5),
  ("ink-on-embed", ["surface-embed"], 4.5),
  ("on-action", ["action","action-hover"], 4.5),
  ("on-action-strong", ["action-strong","action-strong-hover"], 4.5),
  ("on-action-danger", ["action-danger"], 4.5),
  ("success", ["surface","success-soft"], 4.5), ("warning", ["surface","warning-soft"], 4.5),
  ("danger", ["surface","danger-soft"], 4.5), ("info", ["surface","info-soft"], 4.5),
  ("ink-muted", ["neutral-soft"], 4.5), ("ink", ["highlight"], 4.5),
  ("line-strong", ["surface","surface-sunken","bg"], 3), ("focus", ["bg","surface","surface-sunken","surface-raised"], 3),
  ("logo-mark", ["bg","surface"], 3), ("logo-ink", ["bg","surface"], 4.5),
] + [(f"cat-{i}", ["surface","bg"], 3) for i in range(1, 9)]

REPORT = []

def check():
    bad = []
    for theme in ("light", "dark"):
        S = {n: resolve(l if theme=="light" else d, theme) for n,l,d,_ in SEM}
        for fg, grounds, need in CHECKS:
            for g in grounds:
                bgv = S[g]
                if len(bgv) == 9:  # translucent ground: composite on surface
                    bgv = "#%02x%02x%02x" % tuple(round(x*255) for x in over(bgv, S["surface"]))
                r = ratio(S[fg], bgv)
                flag = "" if r >= need else "  <-- FAIL"
                REPORT.append({"theme": theme, "fg": fg, "bg": g, "fgv": S[fg], "bgv": bgv, "ratio": round(r, 2), "min": need})
                if flag: bad.append((theme, fg, g, round(r,2)))
                print(f"{theme:5} {fg:18} on {g:20} {r:5.2f} (>= {need}){flag}")
        # hover wash on raised surfaces (focused menu and list items)
        hov = "#%02x%02x%02x" % tuple(round(x*255) for x in over(S["surface-hover"], S["surface-raised"]))
        for fg in ("ink", "ink-muted", "ink-subtle"):
            r = ratio(S[fg], hov)
            REPORT.append({"theme": theme, "fg": fg, "bg": "surface-hover on surface-raised", "fgv": S[fg], "bgv": hov, "ratio": round(r, 2), "min": 4.5})
            if r < 4.5: bad.append((theme, fg, "surface-hover on surface-raised", round(r, 2)))
            print(f"{theme:5} {fg:18} on hover/raised        {r:5.2f} (>= 4.5){'  <-- FAIL' if r < 4.5 else ''}")
    return bad

# ---------------------------------------------------------------- tokens.json
def build_tokens():
    color = [{"name": n, "value": v, "usage": u} for n, v, u in PRIMS]
    color += [{"name": n, "value": {"light": l, "dark": d}, "usage": u} for n, l, d, u in SEM]
    groups = []
    for gname, fam, styles in TYPE:
        groups.append({"name": gname, "family": fam, "styles": [
            {"name": n, "fontSize": f"{s}px", "lineHeight": f"{lh}px", "fontWeight": w, "letterSpacing": ls, "sample": smp, "usage": u}
            for n, s, lh, w, ls, smp, u in styles]})
    t = {
      "name": "Between Gigs", "version": 1,
      "color": {"themes": [{"id": "light", "name": "Light"}, {"id": "dark", "name": "Dark"}], "tokens": color},
      "type": {"fonts": FONTS, "families": FAMILIES, "groups": groups},
      "spacing": {"note": "4px base. Tailwind v4 reads --spacing: 4px, so p-4 = 16px and gap-6 = 24px.",
                  "tokens": [{"name": n, "value": f"{v}px", "usage": u} for n, v, u in SPACE]},
      "radius": {"note": "Generous, never sharp. Nested corners: inner radius = outer radius minus the padding between them.",
                 "tokens": [{"name": n, "value": v if isinstance(v, str) else f"{v}px", "usage": u} for n, v, u in RADIUS]},
      "shadow": {"note": "Light theme: soft forest-tinted shadows. Dark theme: depth comes from surface steps plus a faint top highlight.",
                 "tokens": [{"name": n, "value": {"light": l, "dark": d}, "usage": u} for n, l, d, u in SHADOW]},
    }
    for fam, toks in OTHER.items():
        t[fam] = {"tokens": [{"name": n, "value": v, "usage": u} for n, v, u in toks]}
    return t


UTILS = """/* 6. Utilities the scales don't cover. */
@utility eyebrow { text-transform: uppercase; }
@utility tabular { font-variant-numeric: tabular-nums; }
@utility z-* { z-index: --value(--z-*); }
@utility duration-* { transition-duration: --value(--duration-*); }

/* Range input: brand-filled track (set --fill: 0-100% inline) and an outlined thumb. */
@utility range {
  &::-webkit-slider-runnable-track { height: 6px; border-radius: 9999px; background: linear-gradient(to right, var(--ink-brand) var(--fill, 50%), var(--line) var(--fill, 50%)); }
  &::-moz-range-track { height: 6px; border-radius: 9999px; background: linear-gradient(to right, var(--ink-brand) var(--fill, 50%), var(--line) var(--fill, 50%)); }
  &::-webkit-slider-thumb { appearance: none; width: 18px; height: 18px; margin-top: -6px; border-radius: 9999px; background: var(--surface-raised); border: 2px solid var(--ink-brand); box-shadow: var(--shadow-xs, none); }
  &::-moz-range-thumb { width: 14px; height: 14px; border-radius: 9999px; background: var(--surface-raised); border: 2px solid var(--ink-brand); }
}

/* 7. Material layer (optional personal finish). See the Materials section. */
@utility material {
  position: relative;
  isolation: isolate;
  &::before {
    content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none; z-index: -1;
    background-image: var(--material-image, none);
    background-size: var(--material-size, 512px);
    opacity: var(--material-opacity, var(--opacity-material));
    mix-blend-mode: var(--material-blend, soft-light);
  }
}
[data-material=off] .material::before, .material[data-material=off]::before { display: none; }
@media (prefers-reduced-transparency: reduce) { .material::before { display: none; } }"""

def build_ds_theme():
    """Theme for the design-system page build: every value points at the page's own tokens.css variables,
    so a token edited on the page reaches the component previews. Emits no variables of its own."""
    L = []; w = L.append
    w("@theme inline reference {")
    w("  --color-*: initial;")
    w("  --color-white: #ffffff; --color-transparent: transparent; --color-current: currentColor;")
    for n, *_ in PRIMS: w(f"  --color-{n}: var(--{n});")
    for n, *_ in SEM: w(f"  --color-{n}: var(--{n});")
    for k in FAMILIES: w(f"  --font-{k}: var(--font-{k});")
    for _, fam, styles in TYPE:
        for n, sz, lh, wt, ls, _, _ in styles:
            w(f"  --text-{n}: {sz/16:g}rem; --text-{n}--line-height: {lh}px; --text-{n}--letter-spacing: {ls}; --text-{n}--font-weight: {wt};")
    w("  --spacing: 4px;")
    w("  --radius-*: initial;")
    for n, *_ in RADIUS: w(f"  --{n}: var(--{n});")
    w("  --breakpoint-*: initial;")
    for n, v, _ in OTHER["breakpoint"]: w(f"  --breakpoint-{n[3:]}: {int(v[:-2])/16:g}rem;")
    w("  --ease-*: initial;")
    for n, *_ in OTHER["easing"]: w(f"  --{n}: var(--{n});")
    w("  --shadow-*: initial;")
    for n, *_ in SHADOW: w(f"  --{n}: var(--{n});")
    for n, *_ in OTHER["zIndex"] + OTHER["duration"]: w(f"  --{n}: var(--{n});")
    w("}")
    w("@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));")
    w("@layer base {")
    w("  body { background: var(--bg); color: var(--ink); font-family: var(--font-sans); font-size: 0.9375rem; line-height: 22px; -webkit-font-smoothing: antialiased; }")
    w("  :focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }")
    w("}")
    w(UTILS)
    return "\n".join(L) + "\n"

# ---------------------------------------------------------------- tailwind v4 css
def css_val(v):  # aliases -> var()
    return re.sub(r"\{([^}]+)\}", lambda m: f"var(--{m.group(1)})", v)

def build_tailwind():
    L = []
    w = L.append
    w("/* Between Gigs design tokens for Tailwind CSS v4.")
    w("   Generated from tokens.json. Edit the tokens, not this file.")
    w("   Usage: @import \"tailwindcss\"; @import \"./between-gigs.css\";")
    w("   Theme: set data-theme=\"light\" | \"dark\" on <html>; without it the OS setting decides. */")
    w("")
    w("@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));")
    w("")
    for f in FONTS:
        w("@font-face {")
        w(f"  font-family: \"{f['family']}\";")
        w(f"  src: url(\"../{f['file']}\") format(\"woff2\");")
        w(f"  font-weight: {f['weight']};")
        w(f"  font-style: {f['style']};")
        w("  font-display: swap;")
        w("}")
    w("")
    w("/* 1. Primitives and scales. Tailwind turns these into utilities (bg-forest-800, rounded-lg, shadow-md, ...). */")
    w("@theme {")
    w("  /* Reset Tailwind's default palette so only brand colors exist */")
    w("  --color-*: initial;")
    w("  --color-white: #ffffff;")
    w("  --color-transparent: transparent;")
    w("  --color-current: currentColor;")
    for n, v, _ in PRIMS:
        w(f"  --color-{n}: {v};")
    w("")
    for k, v in FAMILIES.items():
        w(f"  --font-{k}: {v};")
    w("")
    for _, fam, styles in TYPE:
        for n, s, lh, wt, ls, _, _ in styles:
            w(f"  --text-{n}: {s/16:g}rem;")
            w(f"  --text-{n}--line-height: {lh}px;")
            w(f"  --text-{n}--letter-spacing: {ls};")
            w(f"  --text-{n}--font-weight: {wt};")
    w("")
    w("  --spacing: 4px;")
    w("")
    w("  --radius-*: initial;")
    for n, v, _ in RADIUS:
        w(f"  --{n}: {v if isinstance(v, str) else str(v)+'px'};")
    w("")
    w("  --breakpoint-*: initial;")
    for n, v, _ in OTHER["breakpoint"]:
        w(f"  --breakpoint-{n[3:]}: {int(v[:-2])/16:g}rem;")
    w("")
    for n, v, _ in OTHER["zIndex"] + OTHER["duration"]:
        w(f"  --{n}: {v};")
    w("")
    w("  --ease-*: initial;")
    for n, v, _ in OTHER["easing"]:
        w(f"  --{n}: {v};")
    w("")
    w("}")
    w("")
    def sem_block(theme):
        out = []
        for n, l, d, _ in SEM:
            v = l if theme == "light" else d
            v = css_val(v).replace("var(--", "var(--color-") if v.startswith("{") else v
            out.append(f"  --{n}: {v};")
        for n, l, d, _ in SHADOW:
            out.append(f"  --elev-{n[7:]}: {l if theme=='light' else d};")
        return out
    w("/* 2. Semantic tokens per theme. Components use THESE, never primitives. */")
    w(":root {")
    L.extend(sem_block("light"))
    w("  color-scheme: light;")
    w("}")
    w("@media (prefers-color-scheme: dark) {")
    w("  :root:not([data-theme=light]) {")
    L.extend("  " + x for x in sem_block("dark"))
    w("    color-scheme: dark;")
    w("  }")
    w("}")
    w("[data-theme=dark] {")
    L.extend(sem_block("dark"))
    w("  color-scheme: dark;")
    w("}")
    w("")
    w("/* 3. Expose semantic tokens as utilities: bg-surface, text-ink-muted, border-line, ring-focus, ... */")
    w("@theme inline {")
    for n, *_ in SEM:
        w(f"  --color-{n}: var(--{n});")
    w("  --shadow-*: initial;")
    for n, *_ in SHADOW:
        w(f"  --{n}: var(--elev-{n[7:]});")
    w("}")
    w("")
    w("/* 4. Non-color scales as plain variables (sizes, opacities, borders). */")
    w(":root {")
    for fam in ("size", "opacity", "borderWidth"):
        for n, v, _ in OTHER[fam]:
            w(f"  --{n}: {v};")
    w("}")
    w("")
    w("/* 5. Base layer: page ground, default text, focus ring, reduced motion. */")
    w("@layer base {")
    w("  html { background: var(--bg); color: var(--ink); font-family: var(--font-sans); font-size: 100%; -webkit-font-smoothing: antialiased; }")
    w("  body { font-size: var(--text-body-md); line-height: var(--text-body-md--line-height); }")
    w("  :focus-visible { outline: var(--border-focus) solid var(--focus); outline-offset: 2px; }")
    w("  ::selection { background: var(--highlight); color: var(--ink); }")
    w("  @media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 1ms !important; transition-duration: 1ms !important; } }")
    w("}")
    w("")
    w(UTILS)
    return "\n".join(L) + "\n"

bad = check()
json.dump(build_tokens(), open(os.path.join(ROOT, "tokens", "tokens.json"), "w"), indent=2, ensure_ascii=False)
open(os.path.join(ROOT, "styles", "between-gigs.css"), "w").write(build_tailwind())
open(os.path.join(ROOT, "styles", "docs-theme.css"), "w").write(build_ds_theme())
json.dump(REPORT, open(os.path.join(ROOT, "tokens", "contrast-report.json"), "w"), indent=1)
print("\nContrast failures:", bad or "none")
sys.exit(1 if bad else 0)
