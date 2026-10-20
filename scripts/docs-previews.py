"""Writes components/<Comp>/preview.html and README.md for the design system page."""
import os, sys, textwrap

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "components")

HEAD = """<!-- @dsCard group="{group}" level="{level}" height={height}{extra} -->
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{name}</title>
</head>
<body>
<div id="root"></div>
<script>
const {{ useState }} = React;
const BG = window.BetweenGigs;
const {{ html, Icons: I }} = BG;
{code}
ReactDOM.createRoot(document.getElementById("root")).render(React.createElement(Demo));
</script>
</body>
</html>
"""

C = {}

# Atomic design level of every component: atoms are single controls and marks, molecules combine a few
# atoms into one job, organisms are whole regions of a screen, templates are full pages.
LEVELS = {
  "atom": ["Button", "IconButton", "Switch", "ThemeToggle", "Input", "Textarea", "Select", "Checkbox", "Slider", "Badge",
           "StatusBadge", "Tag", "Count", "Avatar", "Progress", "Skeleton", "Kbd", "Logo", "Tooltip", "FlowConnector",
           "Reveal", "Parallax", "ScrollProgress"],
  "molecule": ["SegmentedControl", "Field", "RadioGroup", "Combobox", "Card", "Stat", "Banner", "Toast", "EmptyState",
               "Tabs", "Breadcrumbs", "Pager", "NavItem", "Menu", "Popover", "Accordion", "AvatarGroup", "Stepper", "PageTransition"],
  "organism": ["Modal", "Drawer", "ConfirmDialog", "Table", "PageHeader", "ModuleCard", "AppShell", "FilterBar", "WorkspaceTile",
               "FunnelStepCard", "ProfileCard", "StageStats", "CommandPalette"],
  "template": ["ComingSoon", "SearchResults", "GigsterProfile", "GigsterOnboarding"],
}
LEVEL = {n: lv for lv, names in LEVELS.items() for n in names}

def comp(name, group, height, code, readme):
    C[name] = (group, height, textwrap.dedent(code).strip(), textwrap.dedent(readme).strip())

# ------------------------------------------------------------------ Actions
comp("Button", "Actions", 200, """
function Demo() {
  const { Button } = BG;
  return html`<div className="grid gap-5 p-6">
    <div className="flex flex-wrap items-center gap-3">
      <${Button} variant="primary" iconEnd=${html`<${I.ArrowUpRight}/>`}>Claim a card<//>
      <${Button} variant="strong">Approve profile<//>
      <${Button} variant="secondary" iconStart=${html`<${I.Download}/>`}>Export<//>
      <${Button} variant="ghost" iconStart=${html`<${I.Undo2}/>`}>Undo<//>
      <${Button} variant="danger" iconStart=${html`<${I.Trash2}/>`}>Remove access<//>
    </div>
    <div className="flex flex-wrap items-center gap-3">
      <${Button} variant="primary" size="lg">Search<//>
      <${Button} variant="primary" size="md" loading>Save changes<//>
      <${Button} variant="secondary" size="sm">How it works<//>
      <${Button} variant="primary" disabled>Submit for review<//>
    </div>
  </div>`;
}
""", """
# Button

Triggers an action. Five variants, each with one job, so a person can tell at a glance which button matters.

## Variants

- `primary`: the one mint action per view ("Claim a card", "Save changes", "Search"). Never two on the same screen.
- `strong`: the decisive step inside a flow or review ("Create my profile", "Approve profile"). Forest in light theme, near-white in dark.
- `secondary`: outline. Every other visible action ("Export", "How it works", "Request changes").
- `ghost`: toolbar and low-emphasis actions ("Undo", "Cancel" inside dense panels).
- `danger`: destructive actions. Always confirm inside the page first.

## The consumer provides

- `children`: the label. Sentence case, a verb that says what happens.
- `variant`, `size` (`sm` 32px, `md` 40px, `lg` 48px for marketing and the search bar).
- `iconStart` / `iconEnd`: 16px Lucide icons. Use `ArrowUpRight` on the end only for links that leave the page.
- `loading`: keeps the label, adds a spinner, blocks clicks.

## Don't

- Don't make a primary button to fill space. If you're unsure which one is primary, the screen has too many actions.
- Don't replace the label with "Loading…".
- Don't put two primary or two danger buttons next to each other.
""")

comp("IconButton", "Actions", 120, """
function Demo() {
  const { IconButton, Tooltip } = BG;
  const [layout, setLayout] = useState("grid");
  return html`<div className="flex flex-wrap items-center gap-2 p-6">
    <${IconButton} label="Search" icon=${html`<${I.Search}/>`} />
    <${IconButton} label="Notifications" icon=${html`<${I.Bell}/>`} />
    <${IconButton} label="More actions" icon=${html`<${I.MoreHorizontal}/>`} variant="secondary" />
    <span className="mx-2 h-6 w-px bg-line"></span>
    <${IconButton} label="Grid layout" size="sm" pressed=${layout === "grid"} onClick=${() => setLayout("grid")} icon=${html`<${I.LayoutGrid}/>`} />
    <${IconButton} label="List layout" size="sm" pressed=${layout === "list"} onClick=${() => setLayout("list")} icon=${html`<${I.List}/>`} />
    <span className="mx-2 h-6 w-px bg-line"></span>
    <${IconButton} label="Add" variant="primary" icon=${html`<${I.Plus}/>`} />
  </div>`;
}
""", """
# IconButton

A square button that shows only an icon, for toolbars and dense headers where the icon is universally understood.

## The consumer provides

- `label` (required): the accessible name, also shown as the native tooltip. Say what it does: "Notifications", not "Bell".
- `icon`: one Lucide icon.
- `variant`: `ghost` (default, toolbars), `secondary` (stands alone), `primary` (a single add action), `strong`.
- `size`: `sm` 32px or `md` 40px.
- `pressed`: for toggles such as layout modes and sketch tools.

## Use when

- The icon is unambiguous (search, close, more, layout). Otherwise use a Button with a label.
- Wrap in Tooltip when the action needs more than one word or has a shortcut.
""")

comp("SegmentedControl", "Actions", 140, """
function Demo() {
  const { SegmentedControl } = BG;
  const [view, setView] = useState("coverflow");
  const [mode, setMode] = useState("dark");
  return html`<div className="flex flex-wrap items-center gap-6 p-6">
    <${SegmentedControl} label="View" value=${view} onChange=${setView} options=${[
      { value: "gallery", label: "Gallery", icon: html`<${I.LayoutGrid}/>` },
      { value: "list", label: "List", icon: html`<${I.List}/>` },
      { value: "coverflow", label: "Coverflow", icon: html`<${I.GalleryHorizontal}/>` },
      { value: "tiles", label: "Tiles", icon: html`<${I.Grid2x2}/>` },
    ]} />
    <${SegmentedControl} label="Preview appearance" size="sm" value=${mode} onChange=${setMode} options=${[
      { value: "default", label: "Default" }, { value: "light", label: "Light" }, { value: "dark", label: "Dark" },
    ]} />
  </div>`;
}
""", """
# SegmentedControl

Switches between views of the same content, such as Gallery / List / Coverflow / Tiles or Default / Light / Dark.

## The consumer provides

- `label`: names the group for screen readers ("View").
- `options`: 2 to 5 items, each with `value`, `label` and an optional icon.
- `value` and `onChange`.
- `size`: `sm` in toolbars, `md` elsewhere.

## Use when

- The choice changes how the same data is shown and takes effect immediately.
- For moving between different content, use Tabs. For a setting saved with a form, use RadioGroup.

Arrow keys move the selection; only the selected option is in the tab order.
""")

comp("Switch", "Actions", 170, """
function Demo() {
  const { Switch } = BG;
  const [a, setA] = useState(true);
  const [b, setB] = useState(false);
  return html`<div className="grid max-w-md gap-5 p-6">
    <${Switch} checked=${a} onChange=${setA} label="Highlight edits" description="Marks text that changed since the approved copy." />
    <${Switch} checked=${b} onChange=${setB} label="Use Hub pointer" description="Off uses your device's default." />
    <div className="flex items-center gap-3 text-label-md text-ink"><${Switch} checked=${true} onChange=${() => {}} aria-label="Typewriter mode" /> Typewriter</div>
  </div>`;
}
""", """
# Switch

Turns a setting on or off immediately, with no save step.

## The consumer provides

- `checked` and `onChange(checked)`.
- `label` and optional `description`. Without a visible label, pass `aria-label`.

## Use when

- The change applies the moment it is flipped (Typewriter, Highlight edits, Use Hub pointer).
- For a yes/no inside a form that is submitted later, use Checkbox.
- Label the setting, not the state: "Highlight edits", not "Highlighting is on".
""")

# ------------------------------------------------------------------ Forms
comp("Field", "Forms", 300, """
function Demo() {
  const { Field, Input, Select } = BG;
  return html`<div className="grid max-w-md gap-5 p-6">
    <${Field} label="Name"><${Input} placeholder="First and last name" /><//>
    <${Field} label="ZIP code" error="Enter a 5-digit ZIP code, like 90026."><${Input} defaultValue="9002" /><//>
    <${Field} label="What do you need help with?" hint="Pick the closest match. You can add details next." optional>
      <${Select} placeholder="Choose a service" options=${[
        { value: "builds", label: "Furniture & creative builds" }, { value: "makeup", label: "Makeup services" },
        { value: "hair", label: "Hair styling" }, { value: "wardrobe", label: "Wardrobe & personal styling" },
      ]} />
    <//>
  </div>`;
}
""", """
# Field

Wraps one form control with its label and its help or error text, and connects them for screen readers.

## The consumer provides

- `label`: short, sentence case, no colon.
- `children`: exactly one Input, Textarea or Select. Field passes it `id`, `invalid` and `aria-describedby`.
- `hint`: what to enter or why it's asked.
- `error`: what went wrong and how to fix it ("Enter a 5-digit ZIP code, like 90026"). Replaces the hint while shown.
- `optional`: marks the field "Optional". Required is the default, so required fields are not marked.

## Do

- Show errors after the person leaves the field or submits, not while they type.
- Stack fields with `gap-5`; group related fields under a heading-sm.
""")

comp("Input", "Forms", 240, """
function Demo() {
  const { Input } = BG;
  return html`<div className="grid max-w-md gap-4 p-6">
    <${Input} aria-label="Find a page" placeholder="Find a page, tool or path…" start=${html`<${I.Search}/>`} />
    <${Input} aria-label="Location" defaultValue="Los Angeles, CA" start=${html`<${I.MapPin}/>`} size="lg" />
    <${Input} aria-label="Hourly rate" defaultValue="45" start=${html`<span className="text-ink-subtle">$</span>`} end=${html`<span className="text-body-sm text-ink-subtle">/hr</span>`} size="sm" />
    <${Input} aria-label="Email" defaultValue="maya@example" invalid />
    <${Input} aria-label="Workspace" defaultValue="Between Gigs" disabled />
  </div>`;
}
""", """
# Input

A single-line text field. The focus ring sits on the whole frame, so icons and units stay inside it.

## The consumer provides

- Standard input props (`value`, `onChange`, `type`, `placeholder`, `name`).
- `size`: `sm` 32px for filter bars and tables, `md` 40px default, `lg` 48px for the marketing search bar.
- `start` / `end`: an icon, a currency sign, a unit or a small clear button.
- `invalid`: set by Field when there is an error; set it yourself only outside a Field.

## Do

- Always give it a label: through Field, or `aria-label` when the context is obvious (a search box with a search icon).
- Placeholders show an example, never the label.
""")

comp("Textarea", "Forms", 220, """
function Demo() {
  const { Field, Textarea } = BG;
  return html`<div className="grid max-w-lg gap-4 p-6">
    <${Field} label="Question / hypothesis">
      <${Textarea} rows=${3} maxLength=${280} showCount defaultValue="Can the viewer understand what changed without invented results?" />
    <//>
  </div>`;
}
""", """
# Textarea

Multi-line text: project descriptions, review notes, prompts, hypotheses.

## The consumer provides

- Standard textarea props; `rows` sets the starting height (default 4). It resizes vertically.
- `maxLength` with `showCount` to show "used / max" under the field.
- `invalid`: set by Field.

Use inside a Field. For long-form writing with formatting, use the Writing Studio editor, not this.
""")

comp("Select", "Forms", 200, """
function Demo() {
  const { Select } = BG;
  const opts = [{ value: "all", label: "All" }, { value: "working", label: "Working" }, { value: "preview", label: "Preview" }, { value: "not-started", label: "Not started" }];
  return html`<div className="grid max-w-md gap-4 p-6">
    <div className="flex flex-wrap items-center gap-2">
      <span className="text-label-sm text-ink-muted">Status</span>
      <${Select} aria-label="Status" size="sm" defaultValue="all" options=${opts} start=${html`<${I.Filter}/>`} className="w-40" />
    </div>
    <${Select} aria-label="Working version" defaultValue="patti" options=${[{ value: "patti", label: "Patti · approved copy" }, { value: "public", label: "Before Patti · public archive" }]} />
    <${Select} aria-label="Service" placeholder="Choose a service" options=${opts} invalid />
  </div>`;
}
""", """
# Select

Picks one value from a short list. The list is drawn by the design system, not the operating system, so it has the same rounded, raised look as Menu and Combobox in both themes.

## The consumer provides

- `options`: `{ value, label, disabled? }[]`.
- `value` + `onValueChange(value)` to control it, or `defaultValue` to let it manage itself. `onChange` also fires with `{ target: { value } }` for form libraries.
- `placeholder`: shown in the field until something is chosen ("Choose a service"). It is not an option in the list.
- `name` to submit with a form (a hidden input carries the value). `size`, `invalid`, `disabled`, `start` (an icon, as in filter bars).

## Keyboard

Enter, Space or the arrow keys open the list; arrows, Home and End move; Enter or Space picks; Escape closes and returns focus. Typing a letter jumps to the next option that starts with it, open or closed.

## Use when

- Up to about ten options. Longer lists, or options that need search, use Combobox.
- Five or fewer options that all deserve to be seen: use RadioGroup or SegmentedControl.
""")

comp("Checkbox", "Forms", 200, """
function Demo() {
  const { Checkbox } = BG;
  return html`<div className="grid max-w-lg gap-4 p-6">
    <${Checkbox} defaultChecked label="Add me to the Founding Members wall" description="First name, last initial and neighborhood. You can change this later." />
    <${Checkbox} label="I'll leave an honest review after my booking" />
    <${Checkbox} disabled label="Pencil 2 reference (not available for this device)" />
  </div>`;
}
""", """
# Checkbox

A yes/no choice inside a form, or one of several independent choices in a list.

## The consumer provides

- Standard checkbox props (`checked`/`defaultChecked`, `onChange`, `name`).
- `label`: says what checking it means ("Add me to the wall"). `description` for the consequence.

## Use when

- The choice is saved with the form. For a setting that applies immediately, use Switch.
- Never pre-check consent boxes (reviews, marketing, being listed publicly).
""")

comp("RadioGroup", "Forms", 220, """
function Demo() {
  const { RadioGroup } = BG;
  const [v, setV] = useState("area");
  return html`<div className="p-6">
    <${RadioGroup} name="priority" label="Pointer priority" value=${v} onChange=${setV} options=${[
      { value: "area", label: "Area first", description: "Current area, then company default, then your default." },
      { value: "mine", label: "My default everywhere" },
      { value: "company", label: "Company default", description: "Shared company policies are coming soon.", disabled: true },
    ]} />
  </div>`;
}
""", """
# RadioGroup

One choice from two to five options that should all be visible at once.

## The consumer provides

- `name`, a visible `label` (rendered as the fieldset legend), `options`, `value`, `onChange`.
- `orientation`: `vertical` (default) or `horizontal` for short labels.

Put the recommended option first and say so in its label or description. More than five options: use Select.
""")

comp("Slider", "Forms", 180, """
function Demo() {
  const { Slider } = BG;
  const [shine, setShine] = useState(25);
  const [size, setSize] = useState(92);
  return html`<div className="grid max-w-sm gap-6 p-6">
    <${Slider} label="Shine" value=${shine} onChange=${setShine} format=${(v) => v + "%"} />
    <${Slider} label="Pointer size" min=${24} max=${128} value=${size} onChange=${setSize} format=${(v) => v + "px"} />
  </div>`;
}
""", """
# Slider

Picks a value on a continuous range where the exact number matters less than the feel: card size, shine, pointer size, canvas transparency.

## The consumer provides

- `label`, `value`, `onChange(number)`, and `min` / `max` / `step`.
- `format`: shows the current value at the end of the label row ("25%", "92px").

For exact numbers (prices, counts), use an Input with `type="number"`.
""")

# ------------------------------------------------------------------ Display
comp("Badge", "Display", 140, """
function Demo() {
  const { Badge } = BG;
  return html`<div className="grid gap-4 p-6">
    <div className="flex flex-wrap items-center gap-2">
      <${Badge} tone="success">Approved<//><${Badge} tone="warning">Needs review<//><${Badge} tone="danger">Failed<//>
      <${Badge} tone="info">Preview<//><${Badge} tone="neutral">Not started<//><${Badge} tone="brand">Sample person<//>
    </div>
    <div className="flex flex-wrap items-center gap-2">
      <${Badge} tone="warning" size="sm">Draft · not public<//><${Badge} tone="info" icon=${html`<${I.Lock}/>`}>Design locked<//>
      <${Badge} tone="brand" size="sm">Trust · Week 2<//>
    </div>
  </div>`;
}
""", """
# Badge

A short label for a state or a type, in a tone color.

## The consumer provides

- `tone`: `success`, `warning`, `danger`, `info`, `neutral` or `brand` (types and samples, not states).
- `children`: one to three words.
- `icon` (14px) for scanning in dense lists; `size` `sm` or `md`. Badges carry no dot: the tone and the word say it.

## Use when

- For the product's status words (Draft, Needs review, Approved…) use StatusBadge so the color always matches the word.
- Badges are not buttons. For a removable or clickable label use Tag.
""")

comp("StatusBadge", "Display", 150, """
function Demo() {
  const { StatusBadge, statusMeta } = BG;
  return html`<div className="flex flex-wrap items-center gap-2 p-6">
    ${Object.keys(statusMeta).map((s) => html`<${StatusBadge} key=${s} status=${s} />`)}
  </div>`;
}
""", """
# StatusBadge

The product's fixed status vocabulary. Each word always appears in the same color, everywhere.

| status | Word | Tone |
| --- | --- | --- |
| `draft` | Draft | warning |
| `not-started` | Not started | neutral |
| `working` | Working | info |
| `preview` | Preview | info |
| `needs-review` | Needs review | warning |
| `changes-requested` | Changes requested | warning |
| `approved` | Approved | success |
| `published` | Published | success |
| `live` | Live | success |
| `archived` | Archived | neutral |

## The consumer provides

- `status`: one of the keys above. A new status is a design decision: add it to `statusMeta` and the README's status table together.
""")

comp("Tag", "Display", 150, """
function Demo() {
  const { Tag } = BG;
  const [areas, setAreas] = useState(["Silver Lake"]);
  const toggle = (a) => setAreas((xs) => xs.includes(a) ? xs.filter((x) => x !== a) : [...xs, a]);
  return html`<div className="grid gap-4 p-6">
    <div className="flex flex-wrap gap-2"><${Tag}>Alterations<//><${Tag}>Closet styling<//><${Tag}>comparison<//><${Tag}>likeness<//></div>
    <div className="flex flex-wrap gap-2">
      ${["Silver Lake", "Echo Park", "Los Feliz", "All Los Angeles"].map((a) => html`<${Tag} key=${a} selected=${areas.includes(a)} onSelect=${() => toggle(a)}>${a}<//>`)}
    </div>
    <div className="flex flex-wrap gap-2"><${Tag} onRemove=${() => {}}>Event lighting<//><${Tag} onRemove=${() => {}}>Home lighting<//></div>
  </div>`;
}
""", """
# Tag

Keywords on cards ("Alterations", "Closet styling"), filter chips ("Silver Lake") and removable selections.

## The consumer provides

- `children`: one or two words.
- `onSelect` + `selected`: turns it into a toggle chip (filters).
- `onRemove`: adds a remove button named "Remove <tag>".

Tags describe; they never show status. Use Badge or StatusBadge for state.
""")

comp("Count", "Display", 110, """
function Demo() {
  const { Count } = BG;
  return html`<div className="flex flex-wrap items-center gap-6 p-6 text-label-md text-ink">
    <span className="flex items-center gap-2">All modules <${Count} value=${101} /></span>
    <span className="flex items-center gap-2">Pinned <${Count} value=${7} /></span>
    <span className="flex items-center gap-2">Notifications <${Count} value=${3} tone="accent" /></span>
    <span className="flex items-center gap-2">Inbox <${Count} value=${240} max=${99} tone="accent" /></span>
  </div>`;
}
""", """
# Count

A number pill after a label: category totals, tab counts, unread items.

## The consumer provides

- `value`; `max` to cap the display ("99+").
- `tone`: `quiet` for totals, `accent` (mint) only for new or unread items that need attention.
""")

comp("Avatar", "Display", 120, """
function Demo() {
  const { Avatar } = BG;
  return html`<div className="flex flex-wrap items-center gap-4 p-6">
    <${Avatar} name="Maya Chen" size="lg" />
    <${Avatar} name="Peter Lenkov" size="md" />
    <${Avatar} name="Patti" size="sm" />
    <span className="mx-2 h-6 w-px bg-line"></span>
    <${Avatar} name="Hoy Wellness Club" shape="square" size="md" />
    <${Avatar} name="Santa Maria Tennis Club" shape="square" size="lg" />
  </div>`;
}
""", """
# Avatar

A person's photo, or their initials when there is no photo. Square avatars stand for companies and workspaces.

## The consumer provides

- `name` (required): alt text and the source of the initials.
- `src`: photo URL. A broken image falls back to initials.
- `size`: `sm` 24px (lists, seats), `md` 32px (top bar, switcher), `lg` 48px (profile headers).
- `shape`: `circle` for people, `square` for companies.
""")

comp("Progress", "Display", 170, """
function Demo() {
  const { Progress } = BG;
  return html`<div className="grid max-w-md gap-6 p-6">
    <${Progress} value=${55} label="Building" valueText="55% est." />
    <${Progress} value=${6} max=${20} label="Founding cards claimed" valueText="6 of 20" size="md" />
    <${Progress} value=${0} label="Planned" valueText="0% est." />
  </div>`;
}
""", """
# Progress

Shows how far something has come: a module's build, founding cards claimed, an upload.

## The consumer provides

- `value` and `max` (default 100).
- `label`: what is progressing. `valueText`: the end text ("55% est.", "6 of 20"); defaults to the percentage.
- `size`: `sm` (6px) in cards, `md` (10px) as a page's headline progress.

The fill is `ink-brand`, so it holds 3:1 against its track in both themes. Never show progress you can't measure; use a Skeleton or spinner instead.
""")

comp("Card", "Display", 300, """
function Demo() {
  const { Card, CardHeader, Badge, Button } = BG;
  return html`<div className="grid gap-4 p-6 md:grid-cols-3">
    <${Card}>
      <${CardHeader} kicker="Web page" title="Founding 20 landing" description="Card wheel, offer, how it works, claim." aside=${html`<${Badge} tone="warning" size="sm">Draft<//>`} />
    <//>
    <${Card} stripe="cat-4" variant="flat">
      <${CardHeader} kicker="Claim form" title="Claim your card" description="Name, email, ZIP, project, wall opt-in." />
    <//>
    <${Card} selected interactive>
      <${CardHeader} title="Group call · screenshare" description="A review needs a decision, not just a comment thread." />
      <div className="mt-4"><${Button} size="sm" variant="secondary" iconEnd=${html`<${I.ArrowUpRight}/>`}>Open study<//></div>
    <//>
  </div>`;
}
""", """
# Card

The one container for grouped content. Module cards, profile cards, funnel steps and panels all start from it.

## Variants

- `raised` (default): on the page ground, with `shadow-sm`.
- `flat`: inside a panel or another surface; hairline only.
- `sunken`: a recessed well inside a card.

## The consumer provides

- `children`, usually starting with `CardHeader` (`kicker`, `title`, `description`, `aside`).
- `padding`: `sm` 12px, `md` 16px (default), `lg` 24px (panels).
- `stripe`: a `cat-*` color along the top edge to show the item's type (funnel steps). Always with a type label.
- `selected`: the featured or current card. One per view.
- `interactive`: hover feedback. Put the real link or button inside the card; don't make the whole div clickable.

## Don't

- Don't nest raised cards. Inside a card, use `flat` or `sunken`.
- Don't add a colored left border; use `stripe` on top, or a Badge.
""")

comp("Stat", "Display", 200, """
function Demo() {
  const { Stat, StatRow } = BG;
  return html`<div className="p-6">
    <${StatRow}>
      <${Stat} value="20" label="numbered founding cards" />
      <${Stat} value="$250" label="gift card toward your first booking" />
      <${Stat} value="$5,000" label="of work for professionals between productions" />
      <${Stat} value="14" label="drafts" delta=${{ value: "3 this week", direction: "up" }} />
    <//>
  </div>`;
}
""", """
# Stat

One headline number with its label. `StatRow` lays several out between hairlines.

## The consumer provides

- `value`: the formatted number ("$5,000", "14"). Set in Sora, tabular.
- `label`: lower-case phrase that completes the number ("numbered founding cards").
- `delta`: optional change, `{ value, direction, invert? }`. `invert` when going up is bad (errors, costs).
- `size`: `lg` for marketing and dashboards, `md` inside panels.

Only use stat rows when the numbers are the point of the page. Never invent figures to fill a row.
""")

# ------------------------------------------------------------------ Feedback
comp("Banner", "Feedback", 260, """
function Demo() {
  const { Banner, Button } = BG;
  return html`<div className="grid gap-4 p-6">
    <${Banner} tone="warning" layout="strip" title="Draft · not public." action=${html`<a className="-my-1 inline-block py-1 text-label-sm text-ink underline" href="#">Open the funnel map</a>`}>Submissions are disabled; sample names are illustrative.<//>
    <${Banner} tone="warning">Draft preview: nothing is saved or sent.<//>
    <${Banner} tone="info" title="Design stays locked">Text edits only. Global design adoption is a separate review.<//>
    <${Banner} tone="danger" title="Couldn't save the system" action=${html`<${Button} size="sm" variant="secondary">Retry<//>`} onDismiss=${() => {}}>Your changes are kept on this device.<//>
  </div>`;
}
""", """
# Banner

A message about a page or section that stays until it is resolved or dismissed.

## The consumer provides

- `tone`: `info`, `success`, `warning`, `danger`. The icon follows the tone.
- `layout`: `inline` (rounded, inside content) or `strip` (full-width band at the top of a page, like "Draft · not public").
- `title` (bold lead), `children` (the detail), `action` (a link or small button), `onDismiss`.

## Use when

- The message is about the state of the page (draft, locked, failed to save).
- For a confirmation that something just happened, use a Toast. For a field error, use Field's `error`.
""")

comp("Toast", "Feedback", 220, """
function Demo() {
  const { Toast, ToastProvider, useToast, Button } = BG;
  function Trigger() {
    const show = useToast();
    return html`<${Button} variant="secondary" onClick=${() => show({ message: "Material change undone.", action: { label: "Redo", onClick: () => {} } })}>Show a toast<//>`;
  }
  return html`<${ToastProvider}><div className="grid max-w-sm gap-3 p-6">
    <${Toast} message="Changes saved" tone="success" />
    <${Toast} message="Material change undone." action=${{ label: "Redo", onClick: () => {} }} onDismiss=${() => {}} />
    <${Toast} message="Couldn't reach the server. Retrying." tone="danger" />
    <div><${Trigger} /></div>
  </div><//>`;
}
""", """
# Toast

A brief confirmation that something just happened, with an optional Undo.

## The consumer provides

- Mount `ToastProvider` once near the app root, then call `useToast()` and `show({ message, tone, action, duration })`.
- `message`: past tense, says what happened ("Changes saved", "Profile approved").
- `action`: one short action, usually Undo or Redo. Toasts with an action stay at least 6 seconds.

## Don't

- Don't use a toast for errors the person must act on; use a Banner.
- Don't stack more than three. The provider keeps the newest three.
""")

comp("Tooltip", "Feedback", 130, """
function Demo() {
  const { Tooltip, IconButton } = BG;
  return html`<div className="flex items-end gap-6 px-6 pt-14 pb-6">
    <${Tooltip} content="Search  ⌘K" defaultOpen><${IconButton} label="Search" icon=${html`<${I.Search}/>`} variant="secondary" /><//>
    <${Tooltip} content="Share & reconnect"><${IconButton} label="Share" icon=${html`<${I.Share2}/>`} /><//>
  </div>`;
}
""", """
# Tooltip

A short label shown on hover and focus, mostly to name icon-only controls or show a shortcut.

## The consumer provides

- `content`: a few words on one line.
- `children`: one focusable element.
- `side`: `top` (default) or `bottom`.

Never put information only in a tooltip. Touch screens can't hover.
""")

comp("Skeleton", "Feedback", 170, """
function Demo() {
  const { Skeleton, Card } = BG;
  return html`<div className="p-6"><${Card} className="grid max-w-xs gap-3">
    <${Skeleton} shape="block" />
    <div className="flex items-center gap-3"><${Skeleton} shape="circle" /><${Skeleton} className="w-1/2" /></div>
    <${Skeleton} /><${Skeleton} className="w-3/4" />
  <//></div>`;
}
""", """
# Skeleton

A placeholder in the shape of content that is still loading. Use for loads over about 300ms.

## The consumer provides

- `shape`: `text` (a line), `block` (an image or card area), `circle` (an avatar).
- `className` for width and height.

Match the real layout so nothing jumps when content arrives. Pulsing stops under reduced motion.
""")

comp("EmptyState", "Feedback", 280, """
function Demo() {
  const { EmptyState, Button } = BG;
  return html`<div className="p-6">
    <${EmptyState} icon=${html`<${I.Layers}/>`} title="No studies yet"
      action=${html`<${Button} variant="primary" iconStart=${html`<${I.Plus}/>`}>New study<//>`}>
      Studies collect visual tests, benchmarks and evidence for one question. Start one, or import from outside.
    <//>
  </div>`;
}
""", """
# EmptyState

Fills a view with nothing to show yet, and says how to start.

## The consumer provides

- `title`: what is empty, plainly ("No studies yet").
- `children`: what will appear here and how to add the first one.
- `action`: usually one primary Button. `icon`: a Lucide icon.

For a filter with no matches, say so and offer "Reset filters" instead of a create action.
""")

# ------------------------------------------------------------------ Navigation
comp("Tabs", "Navigation", 220, """
function Demo() {
  const { Tabs, TabList, Tab, TabPanel } = BG;
  const [t, setT] = useState("studies");
  return html`<div className="p-6"><${Tabs} value=${t} onChange=${setT}>
    <${TabList} label="Experiment workspace">
      <${Tab} value="studies" icon=${html`<${I.Layers}/>`} count=${10}>Studies<//>
      <${Tab} value="media" icon=${html`<${I.Image}/>`}>Media lab<//>
      <${Tab} value="profiles" icon=${html`<${I.Users}/>`} count=${3}>Profiles<//>
      <${Tab} value="campaign" disabled>Campaign Studio<//>
    <//>
    <${TabPanel} value="studies"><p className="text-body-md text-ink-muted">Visual studies, benchmarks and evidence, connected to the places you use them.</p><//>
    <${TabPanel} value="media"><p className="text-body-md text-ink-muted">Generated images and screen recordings.</p><//>
    <${TabPanel} value="profiles"><p className="text-body-md text-ink-muted">Sample people and their profile cards.</p><//>
  <//></div>`;
}
""", """
# Tabs

Switches between sections of one page. This is the only tab style in the product: underline tabs, with optional counts.

## The consumer provides

- `Tabs` with `value` / `onChange`; inside it a `TabList` with a `label`, then `Tab`s and matching `TabPanel`s.
- `Tab`: `value`, label, optional `icon` and `count`, `disabled`.

## Use when

- Sections of the same page or record (Studies / Media lab / Profiles).
- To change how the same data is displayed, use SegmentedControl. To go to another page, use links or NavItem.

Arrow keys, Home and End move between tabs. The list scrolls horizontally instead of wrapping.
""")

comp("Breadcrumbs", "Navigation", 110, """
function Demo() {
  const { Breadcrumbs } = BG;
  return html`<div className="p-6"><${Breadcrumbs} items=${[
    { label: "Workspace", href: "#", icon: html`<${I.Home}/>` }, { label: "Marketing & growth", href: "#" }, { label: "Campaign Studio" },
  ]} /></div>`;
}
""", """
# Breadcrumbs

Shows where a page sits and links back up: Workspace › Marketing & growth › Campaign Studio.

## The consumer provides

- `items`: from the top level down, each `{ label, href?, icon? }`. The last item is the current page and is not a link.

Use on every page deeper than a top-level module. Keep labels identical to the page titles they point to.
""")

comp("Pager", "Navigation", 110, """
function Demo() {
  const { Pager } = BG;
  const names = ["Connected work", "Table Studio", "Feature reminders", "Project management", "Spec Builder"];
  const [p, setP] = useState(1);
  return html`<div className="flex justify-center p-6"><${Pager} page=${p} pageCount=${names.length} onChange=${setP} itemLabel=${names[p - 1]} /></div>`;
}
""", """
# Pager

Steps through a set one item or page at a time: Coverflow, stacked profile cards, long result lists.

## The consumer provides

- `page` (1-based), `pageCount`, `onChange(page)`.
- `itemLabel`: the current item's name, shown after the position ("1 / 5 · Connected work").

The position is announced to screen readers when it changes.
""")

comp("NavItem", "Navigation", 320, """
function Demo() {
  const { NavItem, NavSection } = BG;
  return html`<div className="flex gap-6 p-6">
    <nav aria-label="Workspace" className="w-62 rounded-lg border border-line bg-surface p-3"><${NavSection} title="Workspace">
      <${NavItem} href="#" label="All modules" icon=${html`<${I.Layers}/>`} count=${101} active />
      <${NavItem} href="#" label="Projects & planning" icon=${html`<${I.FolderKanban}/>`} count=${5} />
      <${NavItem} href="#" label="People & knowledge" icon=${html`<${I.Users}/>`} count=${12} />
      <${NavItem} href="#" label="Design & experience" icon=${html`<${I.Palette}/>`} count=${23} />
      <${NavItem} href="#" label="Developer tools" icon=${html`<${I.Code2}/>`} count=${12} />
    <//></nav>
    <nav aria-label="Workspace rail" className="grid content-start gap-0.5 rounded-lg border border-line bg-surface p-3">
      <${NavItem} href="#" label="All modules" icon=${html`<${I.Layers}/>`} collapsed active />
      <${NavItem} href="#" label="Projects & planning" icon=${html`<${I.FolderKanban}/>`} collapsed />
      <${NavItem} href="#" label="People & knowledge" icon=${html`<${I.Users}/>`} collapsed />
    </nav>
  </div>`;
}
""", """
# NavItem

One row in the sidebar or a section nav, with an icon and an optional count. `NavSection` groups rows under a title.

## The consumer provides

- `label`, `href` (or other anchor props), `icon`, `count`.
- `active`: the current page. Sets `aria-current="page"`.
- `collapsed`: rail mode, icon only; the label becomes the accessible name and tooltip.

Sidebar rows use Lucide icons at 20px. The illustrated category artwork belongs in category headers, not in nav rows.
""")

# ------------------------------------------------------------------ Overlays
comp("Menu", "Overlays", 380, """
function Demo() {
  const { Menu, Button, Input, Avatar } = BG;
  return html`<div className="flex gap-6 p-6">
    <${Menu} defaultOpen
      trigger=${html`<${Button} variant="secondary" iconEnd=${html`<${I.ArrowRight} className="rotate-90"/>`}>Your companies<//>`}
      header=${html`<${Input} size="sm" aria-label="Find a company" placeholder="Find a company…" start=${html`<${I.Search}/>`} />`}
      items=${[
        { heading: "Workspaces" },
        { label: "Between Gigs", description: "Hub linked · Hub v3.64", checked: true, icon: html`<${Avatar} name="Between Gigs" shape="square" size="sm" />` },
        { label: "Sergio's Campus", description: "Profile only · Version unavailable", checked: false, icon: html`<${Avatar} name="Sergio's Campus" shape="square" size="sm" />` },
        { label: "Hoy Wellness Club", description: "Profile only", checked: false, icon: html`<${Avatar} name="Hoy Wellness Club" shape="square" size="sm" />` },
        "separator",
        { label: "Workspace settings", icon: html`<${I.Settings}/>`, shortcut: "⌘," },
        { label: "Leave workspace", icon: html`<${I.LogOut}/>`, danger: true },
      ]} />
  </div>`;
}
""", """
# Menu

A list of actions or choices opened from a button: Appearance, account, row actions, the company switcher.

## The consumer provides

- `trigger`: a Button or IconButton. Menu adds `aria-haspopup` and `aria-expanded`.
- `items`: a mix of `{ label, onSelect, icon, description, shortcut, checked, danger, disabled }`, `"separator"` and `{ heading }`.
  Setting `checked` on items makes them a pick-one list with a check on the current choice.
- `header`: optional element above the items, such as a search Input.
- `align`: `start` or `end` relative to the trigger.

Keyboard: Down arrow opens and moves, Up arrow, Home, End; Escape or Tab closes and returns focus to the trigger.
""")

comp("Modal", "Overlays", 640, """
function Demo() {
  const { Modal, Button, Field, Input, Select, Checkbox, Banner } = BG;
  const [open, setOpen] = useState(true);
  return html`<div className="p-6">
    <${Button} variant="primary" onClick=${() => setOpen(true)}>Claim a card<//>
    <${Modal} open=${open} onClose=${() => setOpen(false)} title="Claim founding card No. 07"
      description="Reserve your card now. Your $250 gift card arrives once your first booking is confirmed."
      footer=${html`<${Button} variant="ghost" onClick=${() => setOpen(false)}>Cancel<//><${Button} variant="primary">Reserve card 07<//>`}>
      <div className="grid gap-4">
        <${Banner} tone="warning">Draft preview: nothing is saved or sent.<//>
        <${Field} label="Name"><${Input} /><//>
        <${Field} label="What do you need help with?"><${Select} placeholder="Choose a service" options=${[{ value: "b", label: "Furniture & creative builds" }, { value: "m", label: "Makeup services" }]} /><//>
        <${Checkbox} label="Add me to the Founding Members wall" />
      </div>
    <//>
  </div>`;
}
""", """
# Modal

A focused task that blocks the page until it's done or dismissed. With `placement="right"` it becomes a drawer.

## The consumer provides

- `open`, `onClose`, `title`, optional `description`.
- `children`: the body; it scrolls when tall.
- `footer`: Buttons, right-aligned, primary last. Usually Cancel (ghost) + one primary or strong action.
- `size`: `sm`, `md` (default), `lg`. `placement`: `center` or `right`.

Built on the native `<dialog>`: focus is trapped, Escape closes, and it renders in the browser's top layer, so no z-index fights. Clicking the scrim closes it; for forms with unsaved input, confirm before closing.
""")

# ------------------------------------------------------------------ Data
comp("Table", "Data", 330, """
function Demo() {
  const { Table, Avatar, StatusBadge } = BG;
  const rows = [
    { id: "1", name: "Maya Chen", role: "Set carpenter · Art department", status: "needs-review", rate: 45 },
    { id: "2", name: "Luis Ortega", role: "Set carpenter · Custom furniture", status: "approved", rate: 55 },
    { id: "3", name: "Renée Duval", role: "Production coordinator · Events", status: "changes-requested", rate: 60 },
    { id: "4", name: "Devon Price", role: "Location scout", status: "draft", rate: 65 },
  ];
  const [sort, setSort] = useState({ key: "rate", direction: "asc" });
  const sorted = [...rows].sort((a, b) => (sort.direction === "asc" ? 1 : -1) * (a[sort.key] > b[sort.key] ? 1 : -1));
  return html`<div className="p-6"><${Table} caption="Profiles in review" rowKey=${(r) => r.id} rows=${sorted} sort=${sort} onSortChange=${setSort}
    onRowClick=${() => {}} selectedKey="1" columns=${[
      { key: "name", header: "Professional", sortable: true, cell: (r) => html`<span className="flex items-center gap-3"><${Avatar} name=${r.name} size="sm" /><span className="grid"><span className="text-label-md">${r.name}</span><span className="text-body-sm text-ink-muted">${r.role}</span></span></span>` },
      { key: "status", header: "Status", cell: (r) => html`<${StatusBadge} status=${r.status} size="sm" />` },
      { key: "rate", header: "From", numeric: true, sortable: true, cell: (r) => "$" + r.rate + "/hr" },
    ]} /></div>`;
}
""", """
# Table

Rows of records that share the same fields: people, invitations, campaigns, the review queue.

## The consumer provides

- `columns`: `{ key, header, cell?, numeric?, align?, sortable?, width? }[]`. `numeric` right-aligns and uses tabular mono digits.
- `rows` and `rowKey(row)`.
- `caption` (required; visible with `showCaption`).
- `sort` + `onSortChange` for sortable columns; `onRowClick` + `selectedKey` for master–detail views.
- `density`: `comfortable` (48px rows) or `compact` (36px).
- `empty`: what to show when there are no rows.

The header row sticks while scrolling. On narrow screens the table scrolls sideways inside its frame; for phones, prefer a card list.
""")

# ------------------------------------------------------------------ Patterns
comp("PageHeader", "Patterns", 230, """
function Demo() {
  const { PageHeader, Breadcrumbs, Button } = BG;
  return html`<div className="p-6"><${PageHeader}
    breadcrumbs=${html`<${Breadcrumbs} items=${[{ label: "Workspace", href: "#" }, { label: "Marketing & growth", href: "#" }, { label: "Campaign Studio" }]} />`}
    eyebrow="Marketing & growth" title="Campaign Studio" meta="1.1"
    description="Turn useful knowledge into a repeatable content practice."
    actions=${html`<${Button} variant="ghost" iconStart=${html`<${I.Undo2}/>`}>Undo<//><${Button} variant="secondary" iconStart=${html`<${I.Download}/>`}>Export<//><${Button} variant="primary" iconStart=${html`<${I.Save}/>`}>Save changes<//>`} /></div>`;
}
""", """
# PageHeader

The top of every app page: where you are, what this is, and what you can do here.

## The consumer provides

- `breadcrumbs`: a Breadcrumbs element (for pages below a module).
- `eyebrow`: the area name, typed in sentence case ("Marketing & growth"); the style uppercases it.
- `title`, optional `meta` (version or count), `description` (one sentence).
- `actions`: page-level Buttons, primary last.
- `size`: `page` (display-sm) for app pages, `studio` (display-md) for studio landing pages.
""")

comp("ModuleCard", "Patterns", 400, """
function Demo() {
  const { ModuleCard, Button, IconButton } = BG;
  const [sel, setSel] = useState("Connected work");
  const open = html`<${Button} size="sm" variant="secondary" fullWidth iconEnd=${html`<${I.ArrowUpRight}/>`}>Open<//>`;
  const pin = html`<${IconButton} label="Pin module" size="sm" icon=${html`<${I.Pin}/>`} />`;
  const card = (title, status, value, label, version) => html`<${ModuleCard} title=${title} status=${status} version=${version} action=${status === "not-started" ? null : open} pin=${pin}
    progress=${{ value, label }} selected=${sel === title} onSelect=${() => setSel(title)} />`;
  return html`<div className="flex flex-wrap gap-4 p-6">
    ${card("Connected work", "preview", 55, "Building", "v3.46")}
    ${card("Feature reminders", "working", 70, "Building")}
    ${card("Spec Builder", "not-started", 0, "Planned")}
  </div>`;
}
""", """
# ModuleCard

A module in the Workspace hub: status, version, live preview, the open action and build progress.

## The consumer provides

- `title`, `status` (StatusBadge vocabulary), `version`.
- `preview`: a screenshot URL. It sits on `surface-embed`, so light screenshots look the same in both themes.
- `action`: the open Button (secondary, full width, `ArrowUpRight`). Omit for modules that haven't started.
- `pin`: a pin IconButton. `progress`: `{ value, label }` with the stage word ("Building", "Planned").
- `selected`: the module in focus in Coverflow.

Coverflow's tilt and depth belong to the Coverflow layout, not to the card. The card itself stays flat.
""")


# ------------------------------------------------------------------ Layout
comp("AppShell", "Layout", 720, """
function Demo() {
  const { AppShell, TopBar, ToolbarDivider, ModuleBar, Sidebar, Inspector, InspectorSection, PromptBar, NavSection, NavItem,
    IconButton, Button, Avatar, PageHeader, FilterBar, Input, Select, SegmentedControl, ModuleCard, Pager, StatusBadge, Banner } = BG;
  const [mod, setMod] = useState("hub");
  const [view, setView] = useState("gallery");
  const [prompt, setPrompt] = useState("");
  const open = html`<${Button} size="sm" variant="secondary" fullWidth iconEnd=${html`<${I.ArrowUpRight}/>`}>Open<//>`;
  return html`<div style=${{ height: "720px" }}><${AppShell}
    topBar=${html`<${TopBar}
      brand=${html`<${BG.ShellMenuButton} /><${Button} variant="ghost" size="sm" iconStart=${html`<${Avatar} name="Between Gigs" shape="square" size="sm" />`}>Between Gigs<//><span className="font-mono text-data-sm text-ink-subtle">v3.64</span>`}
      start=${html`<${ToolbarDivider} /><span className="font-mono text-data-sm text-ink-muted">109%</span><${IconButton} size="sm" label="Undo" icon=${html`<${I.Undo2}/>`} /><${IconButton} size="sm" label="Redo" icon=${html`<${I.Redo2}/>`} /><${ToolbarDivider} /><${Button} size="sm" variant="ghost" iconStart=${html`<${I.Pencil}/>`}>Sketch<//>`}
      end=${html`<${IconButton} size="sm" label="Single pane" pressed icon=${html`<${I.Monitor}/>`} /><${IconButton} size="sm" label="Two panes" icon=${html`<${I.Columns2}/>`} /><${ToolbarDivider} /><${IconButton} size="sm" label="Appearance" icon=${html`<${I.Sun}/>`} /><${IconButton} size="sm" label="Notifications" icon=${html`<${I.Bell}/>`} /><${Avatar} name="Justin Massion" size="md" />`} />`}
    moduleBar=${html`<${ModuleBar} activeId=${mod} onSelect=${setMod} items=${[
      { id: "hub", label: "Hub", icon: html`<${I.Home}/>` }, { id: "ds", label: "Design system", icon: html`<${I.Palette}/>` },
      { id: "email", label: "Email previews", icon: html`<${I.Mail}/>` }, { id: "journal", label: "The Journal", icon: html`<${I.BookOpen}/>` },
      { id: "lib", label: "Component library", icon: html`<${I.Layers}/>` }, { id: "funnel", label: "Funnel Studio", icon: html`<${I.Filter}/>` },
    ]} />`}
    sidebar=${html`<${Sidebar} title="Workspace" headerAction=${html`<${IconButton} size="sm" label="Collapse sidebar" icon=${html`<${I.PanelLeft}/>`} />`}
      footer=${html`<${NavItem} href="#" label="Version history" icon=${html`<${I.Clock}/>`} /><${NavItem} href="#" label="Team workspace" icon=${html`<${I.Users}/>`} />`}>
      <${NavSection}>
        <${NavItem} href="#" label="All modules" icon=${html`<${I.Layers}/>`} count=${101} active />
        <${NavItem} href="#" label="Projects & planning" icon=${html`<${I.FolderKanban}/>`} count=${5} />
        <${NavItem} href="#" label="Pages & experiences" icon=${html`<${I.FileText}/>`} count=${6} />
        <${NavItem} href="#" label="People & knowledge" icon=${html`<${I.Users}/>`} count=${12} />
        <${NavItem} href="#" label="Design & experience" icon=${html`<${I.Palette}/>`} count=${23} />
        <${NavItem} href="#" label="Developer tools" icon=${html`<${I.Code2}/>`} count=${12} />
        <${NavItem} href="#" label="Marketing & growth" icon=${html`<${I.Megaphone}/>`} count=${8} />
        <${NavItem} href="#" label="Company operations" icon=${html`<${I.Building2}/>`} count=${9} />
      <//>
    <//>`}
    inspector=${html`<${Inspector} eyebrow="Selected module" title="Connected work" actions=${html`<${IconButton} size="sm" label="Close inspector" icon=${html`<${I.X}/>`} />`}>
      <${InspectorSection} title="Status"><${StatusBadge} status="preview" /><//>
      <${InspectorSection} title="Working version"><${Select} size="sm" aria-label="Working version" defaultValue="a" options=${[{ value: "a", label: "v3.46 · preview" }, { value: "b", label: "v3.31 · archived" }]} /><//>
      <${InspectorSection}><${Banner} tone="info" title="Design stays locked">Text edits only.<//><//>
    <//>`}
    prompt=${html`<${PromptBar} value=${prompt} onChange=${setPrompt} onSubmit=${() => setPrompt("")}
      start=${html`<${IconButton} size="sm" label="Command menu" icon=${html`<${I.Command}/>`} /><${IconButton} size="sm" label="Attach" icon=${html`<${I.Plus}/>`} />`}
      end=${html`<${IconButton} size="sm" label="Voice" icon=${html`<${I.Mic}/>`} />`} />`}>
    <div className="grid gap-6">
      <${PageHeader} eyebrow="Between Gigs · Builder" title="Workspace hub" description="101 modules · 6 tools" actions=${html`<${BG.ShellInspectorButton} label="Selected module" />`} />
      <${FilterBar} end=${html`<${Button} size="sm" variant="ghost">Reset filters<//>`}>
        <${Input} size="sm" aria-label="Find a page" placeholder="Find a page, tool or path…" start=${html`<${I.Search}/>`} className="min-w-48 flex-1" />
        <${Select} size="sm" aria-label="Status" defaultValue="all" options=${[{ value: "all", label: "All statuses" }, { value: "w", label: "Working" }]} className="w-40" />
        <${SegmentedControl} size="sm" label="View" value=${view} onChange=${setView} options=${[
          { value: "gallery", label: "Gallery", icon: html`<${I.LayoutGrid}/>` }, { value: "list", label: "List", icon: html`<${I.List}/>` },
          { value: "coverflow", label: "Coverflow", icon: html`<${I.GalleryHorizontal}/>` }]} />
      <//>
      <div className="flex flex-wrap gap-4">
        <${ModuleCard} headingLevel=${2} title="Connected work" status="preview" version="v3.46" action=${open} progress=${{ value: 55, label: "Building" }} selected />
        <${ModuleCard} headingLevel=${2} title="Table Studio" status="preview" version="v3.31" action=${open} progress=${{ value: 55, label: "Building" }} />
        <${ModuleCard} headingLevel=${2} title="Spec Builder" status="not-started" progress=${{ value: 0, label: "Planned" }} />
      </div>
      <div className="flex justify-center"><${Pager} page=${1} pageCount=${5} onChange=${() => {}} itemLabel="Connected work" /></div>
    </div>
  <//></div>`;
}
""", """
# AppShell

The frame of every signed-in screen. It places the top bar, the module bar, the sidebar, the page content, the inspector and the floating prompt bar, and handles their scrolling and stacking.

## Parts

- `TopBar`: `brand` (workspace switcher and version), `start` (zoom, undo, page tools), `end` (layout toggles, appearance, notifications, account). Separate groups with `ToolbarDivider`. 56px tall.
- `ModuleBar`: the row of open modules, `items` + `activeId`. Scrolls sideways; never wraps.
- `Sidebar`: `title`, `headerAction` (collapse), NavSections as children, `footer` links. 248px, or a 64px rail with `collapsed`. Below the `lg` breakpoint it becomes a left Drawer: put `ShellMenuButton` first in the TopBar's `brand` to open it.
- `Inspector`: details of the selected item, as `InspectorSection`s. 320px from `xl` up. Below that it becomes a right Drawer: add `ShellInspectorButton` to the page actions, or control it with `inspectorOpen` / `onInspectorOpenChange` so selecting a row opens it. Omit it when nothing is selected.
- `PromptBar`: the floating composer. `start` and `end` take small IconButtons; the mint send button is built in and disabled while empty.

## The consumer provides

- Each part as a slot, and the page as `children`. Content is centered at 1280px max with the page padding already applied.
- The shell takes the height of its parent. Give the parent `h-dvh`.

## Rules

- One top bar, one module bar, one sidebar per screen. Split views put several page panes inside `children`; they don't repeat the shell.
- Materials (the personal finish) apply to the TopBar, Sidebar and PromptBar surfaces only.
""")

comp("FilterBar", "Layout", 140, """
function Demo() {
  const { FilterBar, FilterLabel, Input, Select, SegmentedControl, Button } = BG;
  const [view, setView] = useState("coverflow");
  return html`<div className="p-6"><${FilterBar} end=${html`<${Button} size="sm" variant="ghost">Reset filters<//>`}>
    <${Input} size="sm" aria-label="Find a page" placeholder="Find a page, tool or path…" start=${html`<${I.Search}/>`} className="min-w-48 flex-1" />
    <${FilterLabel} htmlFor="st">Status<//><${Select} id="st" size="sm" defaultValue="all" options=${[{ value: "all", label: "All" }, { value: "w", label: "Working" }]} className="w-32" />
    <${FilterLabel} htmlFor="so">Sort<//><${Select} id="so" size="sm" defaultValue="cat" options=${[{ value: "cat", label: "Category" }, { value: "new", label: "Newest" }]} className="w-36" />
    <${SegmentedControl} size="sm" label="View" value=${view} onChange=${setView} options=${[
      { value: "gallery", label: "Gallery" }, { value: "list", label: "List" }, { value: "coverflow", label: "Coverflow" }, { value: "tiles", label: "Tiles" }]} />
  <//></div>`;
}
""", """
# FilterBar

The recessed row of search and filters above a collection (Workspace hub, material library, People & profiles).

## The consumer provides

- `children` in this order: the search Input (give it `className="min-w-48 flex-1"` so it takes the spare width), then filter Selects (each with a `FilterLabel`), then the view SegmentedControl, then sliders.
- `end`: right-aligned extras, usually "Reset filters" (ghost Button), shown only when a filter is active.

All controls inside use `size="sm"`. The bar wraps on narrow screens; it never scrolls sideways.
""")

comp("WorkspaceTile", "Patterns", 330, """
function Demo() {
  const { WorkspaceTile, IconButton } = BG;
  const pin = (on) => html`<${IconButton} size="sm" label="Pin workspace" pressed=${on} icon=${html`<${I.Star}/>`} />`;
  const edit = html`<${IconButton} size="sm" label="Edit workspace" icon=${html`<${I.Pencil}/>`} />`;
  return html`<div className="grid gap-4 p-6 sm:grid-cols-3">
    <${WorkspaceTile} name="Hospital Designer" kind="To organize" status="Awaiting hub link" color="cat-2" href="#" pin=${pin(false)} secondaryAction=${edit} />
    <${WorkspaceTile} name="Karol G" kind="Prospect" status="Profile only" color="cat-5" href="#" pin=${pin(true)} secondaryAction=${edit} />
    <${WorkspaceTile} name="Loraine Healing Arts" kind="Client" status="Hub linked · 3 projects" color="cat-3" href="#" pin=${pin(false)} secondaryAction=${edit} />
  </div>`;
}
""", """
# WorkspaceTile

A company workspace in the Playset gallery: cover, relationship, name, state and the open link.

## The consumer provides

- `name`, `kind` (Client, Prospect, To organize, Archived), `status` (one line), `href`.
- `color`: a `cat-*` cover color. Derive it from the workspace id so it never changes between visits. `image` replaces it with a picture.
- `pin`: a star IconButton with `pressed`. `secondaryAction`: usually edit.

## Rules

- The cover is a flat category color. No gradients.
- Initials sit on a `surface` plate in `ink`, never directly on the color. That keeps them readable in both themes (dark-theme category colors are light).
""")

comp("FunnelStepCard", "Patterns", 330, """
function Demo() {
  const { FunnelStepCard, FlowConnector } = BG;
  const [sel, setSel] = useState("p3");
  return html`<div className="overflow-x-auto p-6"><div className="flex items-stretch" style=${{ minWidth: "940px" }}>
    <${FunnelStepCard} fluid type="traffic" step=${1} status="published" title="As seen in Deadline" description="Press and Peter's network bring visitors to the landing page." hint="External traffic" selected=${sel === "p1"} onOpen=${() => setSel("p1")} />
    <${FlowConnector} label="Clicks" />
    <${FunnelStepCard} fluid type="page" step=${2} status="draft" title="Founding 20 landing" description="Card wheel, the offer and how it works, ending in Claim." hint="Double-click to open draft" selected=${sel === "p3"} onOpen=${() => setSel("p3")} />
    <${FlowConnector} label="Claims a card" />
    <${FunnelStepCard} fluid type="email" step=${3} status="draft" title="Your card is reserved" description="Card number and a link to browse professionals." hint="Double-click to open draft" selected=${sel === "p5"} onOpen=${() => setSel("p5")} />
    <${FlowConnector} label="Books" variant="dashed" />
    <${FunnelStepCard} fluid type="marketplace" step=${4} status="not-started" title="Book a professional" description="The client books and the $250 is applied at checkout." hint="Not built yet" selected=${sel === "p6"} onOpen=${() => setSel("p6")} />
  </div></div>`;
}
""", """
# FunnelStepCard

One step on the Funnel Studio canvas: what kind of step it is, its order, status, a preview and what happens there.

## The consumer provides

- `type`: `traffic`, `page`, `form`, `email` or `marketplace`. Each has a fixed label, category color and icon (`stepTypes`), shown as the top stripe and the empty-preview icon.
- `status` shows as a badge in the preview's top-right corner, so the header always has room for the full step type.
- `step` (shown as "03"), `title`, `status`.
- `description`: what the step does, with an arrow to the next step ("Name, email, ZIP → reserved email").
- `preview`: a screenshot. It sits on `surface-embed` so light pages and emails look true in both themes. Without one, a quiet dashed placeholder shows the step type's icon instead of an empty white box.
- `hint`: a short footer note. `selected`: the step shown in the inspector. `onOpen`: opens the draft.
- `fluid`: the card grows to share the row (min 192px). Without it the card is a fixed 224px, for canvases that scroll.

Connector lines between steps belong to the canvas, drawn in `line-strong` with labels in `caption`.
""")

comp("ProfileCard", "Patterns", 470, """
function Demo() {
  const { ProfileCard, Button, IconButton } = BG;
  const view = html`<${Button} variant="secondary" size="sm">View profile<//>`;
  const save = (on) => html`<${IconButton} size="sm" label="Save" pressed=${on} icon=${html`<${I.Star}/>`} />`;
  return html`<div className="grid gap-3 p-6">
    <${ProfileCard} sample name="Maya Chen" specialty="Costume & wardrobe" summary="Thoughtful alterations, wardrobe edits and custom pieces for everyday life."
      tags=${["Alterations", "Closet styling"]} location="Silver Lake · 3 miles away" availability="Available this week" rate=${45} action=${view} save=${save(true)} />
    <${ProfileCard} sample name="Jordan Ellis" specialty="Props & custom builds" summary="Practical builds, furniture fixes and one-of-a-kind details made with care."
      tags=${["Furniture repair", "Custom projects"]} location="Echo Park · 4 miles away" availability="Available next week" rate=${55} action=${view} save=${save(false)} />
  </div>`;
}
""", """
# ProfileCard

A professional in search results: who they are, what they do, where, when, and from how much.

## The consumer provides

- `name`, `specialty` (service area), `summary` (one sentence, their voice), `photo`.
- `tags`: two or three services. `location`: "Neighborhood · N miles away". `availability`: "Available this week".
- `rate`: starting hourly rate in dollars. `action`: the View profile Button. `save`: a star IconButton.
- `sample`: marks a fictional sample profile. Every sample must be marked.

Photos are real portraits of the professional at work. No stock imagery. Without a photo, the initials stand in.
""")

comp("StageStats", "Patterns", 170, """
function Demo() {
  const { StageStats } = BG;
  return html`<div className="grid gap-4 p-6">
    <${StageStats} title="Stage statistics" stages=${[
      { label: "Invited", value: 120 }, { label: "Signed in", value: 64 }, { label: "Draft", value: 31 },
      { label: "Submitted", value: 12, attention: true }, { label: "Changes requested", value: 4 }, { label: "Approved", value: 18 }, { label: "In gallery", value: null },
    ]} />
  </div>`;
}
""", """
# StageStats

Counts per stage of a pipeline, in order: Invited → Signed in → Draft → Submitted → Changes requested → Approved → In gallery.

## The consumer provides

- `title` and `stages`: `{ label, value, attention? }[]` in pipeline order.
- `value: null` shows a dash: the stage exists but nothing is counted yet. Never show 0 for "not measured".
- `attention`: highlights stages waiting on someone (Submitted waits on Peter or Patti).

Use real counts only. In proposals and drafts, show dashes, not invented numbers.
""")


comp("Stepper", "Navigation", 150, """
function Demo() {
  const { Stepper } = BG;
  const [s, setS] = useState(1);
  return html`<div className="max-w-xl p-6"><${Stepper} steps=${["Details", "Skills", "Availability", "Preview"]} current=${s} onStepClick=${setS} /></div>`;
}
""", """
# Stepper

Shows where someone is in a multi-step flow, such as the four-step profile builder.

## The consumer provides

- `steps`: short step names. Three to five steps; more means the flow should be split.
- `current`: 0-based index. Earlier steps show a check.
- `onStepClick`: lets people go back to a finished step. Forward jumps aren't offered.

The current step is marked with `aria-current="step"`. Pair it with a forward button that names the next step ("Continue to Skills").
""")

comp("FlowConnector", "Patterns", 150, """
function Demo() {
  const { FlowConnector, Card } = BG;
  const box = (t) => html`<${Card} padding="sm" className="w-40 shrink-0 text-label-md">${t}<//>`;
  return html`<div className="flex items-stretch p-6">
    ${box("Founding 20 landing")}<${FlowConnector} label="Claims a card" />${box("Claim your card")}<${FlowConnector} label="Books" variant="dashed" />${box("Book a professional")}
  </div>`;
}
""", """
# FlowConnector

The arrow between two steps on a flow or funnel canvas, with an optional label for what the person does to move on.

## The consumer provides

- `label`: a short verb phrase ("Claims a card", "Books").
- `variant`: `solid`, or `dashed` for paths to steps that aren't built or are optional.

Place it between two cards in a flex row; it stretches to fill the gap. The label sits above the line and never wraps, so every arrow in a row stays at the same height. Keep labels to two or three words. It is drawn in `line-strong`, so it holds 3:1 on the canvas.
""")


comp("Logo", "Brand", 300, """
function Demo() {
  const { Logo } = BG;
  return html`<div className="grid gap-px overflow-hidden sm:grid-cols-2">
    <div className="grid content-start gap-6 bg-bg p-8">
      <span className="text-label-sm text-ink-muted">This theme</span>
      <${Logo} height=${56} />
      <div className="flex items-end gap-8"><${Logo} layout="stacked" height=${120} /><${Logo} layout="mark" height=${32} /></div>
    </div>
    <div data-theme="dark" className="grid content-start gap-6 bg-surface-brand p-8">
      <span className="text-label-sm text-ink-muted">On the brand forest</span>
      <${Logo} height=${56} />
      <div className="flex items-end gap-8"><${Logo} layout="stacked" height=${120} /><${Logo} layout="mark" height=${32} /></div>
    </div>
  </div>`;
}
""", """
# Logo

The Between Gigs logo, drawn from the approved files. Its inks follow the theme of the surface it sits on: the on-light file's colors in light theme, the on-dark file's in dark theme and inside dark-theme islands.

## The consumer provides

- `layout`: `wide` (monogram beside the wordmark; headers and nav), `stacked` (wordmark under the monogram; covers, sign-in, square spaces), `mark` (monogram alone; the app's top bar, collapsed rail, favicon).
- `height` in px. Width follows. Minimum: `wide` 24px tall, `mark` 20px tall.

## Rules

- Never recolor, outline, rotate or add effects. The inks are the `logo-mark`, `logo-ink` and `logo-rule` tokens, which hold the files' exact colors.
- Keep clear space of at least half the monogram's height on every side.
- On photos or material textures, put a solid `surface` or `surface-brand` plate behind it.
- The original SVGs are in the Logos asset group for print, slides and partners.
""")


comp("Drawer", "Overlays", 160, """
function Demo() {
  const { Drawer, Button, Field, Select, Switch } = BG;
  const [side, setSide] = useState(null);
  const [on, setOn] = useState(true);
  return html`<div className="flex flex-wrap gap-3 p-6">
    <${Button} variant="secondary" onClick=${() => setSide("left")}>Open navigation drawer<//>
    <${Button} variant="secondary" onClick=${() => setSide("right")}>Open settings drawer<//>
    <${Drawer} open=${side !== null} side=${side || "right"} onClose=${() => setSide(null)} title=${side === "left" ? "Workspace" : "Thread setup"} description=${side === "left" ? null : "Personal notes · Workspace"}
      footer=${side === "right" ? html`<${Button} variant="ghost" onClick=${() => setSide(null)}>Cancel<//><${Button} variant="primary" onClick=${() => setSide(null)}>Save setup<//>` : null}>
      <div className="grid gap-4">
        <${Field} label="Save to"><${Select} options=${[{ value: "notes", label: "Personal notes" }, { value: "team", label: "Team workspace" }]} defaultValue="notes" /><//>
        <${Switch} checked=${on} onChange=${setOn} label="Suggest labels" description="Your original wording stays below." />
      </div>
    <//>
  </div>`;
}
""", """
# Drawer

A panel that slides in from the left or right edge and blocks the page until it's closed. The sidebar and inspector become drawers on smaller screens; settings and setup panels use it on every screen.

## The consumer provides

- `open`, `onClose`, `title`, optional `description` and `footer` (Buttons, primary last).
- `side`: `left` for navigation, `right` for details and settings. `size`: `sm` (default), `md`, `lg`.

Built on Modal, so focus stays inside, Escape closes, and focus returns to the button that opened it.
""")

comp("Popover", "Overlays", 330, """
function Demo() {
  const { Popover, IconButton, Button, SegmentedControl, Switch, Slider } = BG;
  const [theme, setTheme] = useState("system");
  const [mat, setMat] = useState(true);
  const [shine, setShine] = useState(25);
  return html`<div className="flex justify-end p-6 pr-10">
    <${Popover} align="end" label="Appearance" title="Appearance" defaultOpen trigger=${html`<${Button} variant="secondary" iconStart=${html`<${I.Sun}/>`}>Appearance<//>`}>
      <${SegmentedControl} label="Theme" size="sm" value=${theme} onChange=${setTheme} options=${[{ value: "system", label: "System" }, { value: "light", label: "Light" }, { value: "dark", label: "Dark" }]} />
      <${Switch} checked=${mat} onChange=${setMat} label="Materials" description="Your personal finish on the shell." />
      <${Slider} label="Shine" value=${shine} onChange=${setShine} format=${(v) => v + "%"} />
    <//>
  </div>`;
}
""", """
# Popover

A small panel of settings or details anchored to a button, that doesn't block the page: Appearance, Material box, Mouse & gestures, a "With you" call panel.

## The consumer provides

- `trigger`: a Button or IconButton. `label`: the panel's name for screen readers. Optional `title`.
- `children`: the controls. `align` (`start` / `end`), `width` (`sm`, `md`, `lg`).
- `open` / `onOpenChange` to control it; omit them to let it manage itself.

## Use when

- Changes apply as people make them. For a list of actions use Menu. For a task that must be finished or cancelled, use Modal or Drawer.

Focus moves into the panel when it opens; Escape or a click outside closes it.
""")

comp("Accordion", "Display", 300, """
function Demo() {
  const { Accordion, Tag } = BG;
  return html`<div className="grid max-w-lg gap-6 p-6">
    <${Accordion} defaultOpen=${["setup"]} items=${[
      { id: "setup", title: "Thread setup", meta: "Personal notes · Workspace", content: html`<p>Drafts save to your personal notes until you share them with the team.</p>` },
      { id: "labels", title: "Suggested labels", meta: "3", content: html`<div className="flex flex-wrap gap-2"><${Tag}>Hub<//><${Tag}>Feature<//><${Tag}>Needs review<//></div>` },
      { id: "history", title: "Writing history", meta: "12 checkpoints", content: html`<p>Every save keeps a checkpoint you can return to.</p>` },
    ]} />
  </div>`;
}
""", """
# Accordion

Sections that expand and collapse in place: Thread setup, FAQs, groups of settings.

## The consumer provides

- `items`: `{ id, title, meta?, content }[]`. `meta` is short text on the right ("3 items").
- `type`: `multiple` (default) or `single` (opening one closes the rest). `defaultOpen`: ids open at first.
- `variant`: `framed` (default) or `flush` inside panels.

Don't hide anything people need on every visit. Each header is a real button with `aria-expanded`.
""")

comp("Combobox", "Forms", 380, """
function Demo() {
  const { Combobox, Field, Avatar } = BG;
  const companies = ["Between Gigs", "Sergio's Campus", "Hoy Wellness Club", "Santa Maria Tennis Club", "Tennis Shop", "Campus Café", "Security Booth"];
  const [v, setV] = useState("Between Gigs");
  return html`<div className="max-w-sm p-6"><${Field} label="Company">
    <${Combobox} value=${v} onChange=${setV} placeholder="Find a company…" options=${companies.map((c, i) => ({
      value: c, label: c, description: i === 0 ? "Hub linked · v3.64" : "Profile only", icon: html`<${Avatar} name=${c} shape="square" size="sm" />`,
    }))} />
  <//></div>`;
}
""", """
# Combobox

Pick one value from a long list by typing to filter it: the company switcher, assigning a person, choosing a service from dozens.

## The consumer provides

- `options`: `{ value, label, description?, icon?, disabled? }[]`. Descriptions are searched too.
- `value` (or `null`) and `onChange(value)`. `placeholder`, `emptyText`, `size`, `invalid`.
- A label: wrap it in Field, or pass `aria-label`.

Arrow keys move through matches, Enter picks, Escape closes. For fewer than about ten options, use Select.
""")

comp("CommandPalette", "Navigation", 120, """
function Demo() {
  const { CommandPalette, useCommandShortcut, Button, Kbd } = BG;
  const [open, setOpen] = useState(false);
  useCommandShortcut(React.useCallback(() => setOpen(true), []));
  const go = () => {};
  return html`<div className="flex flex-wrap items-center gap-3 p-6">
    <${Button} variant="secondary" iconStart=${html`<${I.Search}/>`} onClick=${() => setOpen(true)}>Search everything<//>
    <span className="flex items-center gap-2 text-body-sm text-ink-muted">or press <${Kbd} keys=${["⌘", "K"]} /></span>
    <${CommandPalette} open=${open} onClose=${() => setOpen(false)} commands=${[
      { id: "1", group: "Modules", label: "Funnel Studio", icon: html`<${I.Filter}/>`, onRun: go },
      { id: "2", group: "Modules", label: "Profile review", icon: html`<${I.Users}/>`, onRun: go },
      { id: "3", group: "Modules", label: "Design system", icon: html`<${I.Palette}/>`, onRun: go },
      { id: "4", group: "Companies", label: "Hoy Wellness Club", icon: html`<${I.Building2}/>`, onRun: go },
      { id: "5", group: "Actions", label: "New module", icon: html`<${I.Plus}/>`, shortcut: ["⌘", "N"], onRun: go },
      { id: "6", group: "Actions", label: "Switch to dark theme", icon: html`<${I.Moon}/>`, keywords: "appearance", onRun: go },
    ]} />
  </div>`;
}
""", """
# CommandPalette

⌘K: jump to any module, company or action by typing.

## The consumer provides

- `open`, `onClose`, `commands`: `{ id, label, group, onRun, icon?, keywords?, shortcut? }[]`. Groups appear in the order first used.
- Call `useCommandShortcut(open)` once near the app root so ⌘K (Ctrl+K on Windows) opens it.

Arrow keys move, Enter runs, Escape closes. Keep labels the same as the page titles they lead to.
""")

comp("ConfirmDialog", "Overlays", 120, """
function Demo() {
  const { ConfirmDialog, Button } = BG;
  const [open, setOpen] = useState(false);
  return html`<div className="p-6">
    <${Button} variant="danger" iconStart=${html`<${I.Trash2}/>`} onClick=${() => setOpen(true)}>Remove from gallery<//>
    <${ConfirmDialog} open=${open} onCancel=${() => setOpen(false)} onConfirm=${() => setOpen(false)}
      title="Remove Maya Chen from the gallery?" description="Her profile goes back to draft and clients can no longer book her. She keeps her account and can resubmit."
      confirmLabel="Remove profile" />
  </div>`;
}
""", """
# ConfirmDialog

Asks before something destructive or hard to undo.

## The consumer provides

- `open`, `onCancel`, `onConfirm`, `busy` while it runs.
- `title`: a question that names the thing ("Remove Maya Chen from the gallery?").
- `description`: what happens and whether it can be undone.
- `confirmLabel`: the action as a verb ("Remove profile"). Never "OK" or "Yes".
- `tone`: `danger` (default) or `default`.

If the action can be undone, skip the dialog and offer Undo in a Toast instead.
""")

comp("AvatarGroup", "Display", 110, """
function Demo() {
  const { AvatarGroup } = BG;
  const team = ["Peter Lenkov", "Patti", "Justin Massion", "Maya Chen", "Luis Ortega", "Renée Duval"].map((name) => ({ name }));
  return html`<div className="flex flex-wrap items-center gap-8 p-6">
    <${AvatarGroup} people=${team} max=${4} />
    <${AvatarGroup} people=${team.slice(0, 3)} size="sm" />
  </div>`;
}
""", """
# AvatarGroup

Overlapping avatars for a team, contributors or who's in a call, with "+N" for the rest.

## The consumer provides

- `people`: `{ name, src? }[]`, most relevant first. `max` (default 4), `size` (`sm`, `md`).

The whole group is announced once with every name, so screen readers don't read each avatar.
""")

comp("Kbd", "Display", 100, """
function Demo() {
  const { Kbd } = BG;
  return html`<div className="flex flex-wrap items-center gap-6 p-6 text-body-md text-ink">
    <span className="flex items-center gap-2">Search <${Kbd} keys=${["⌘", "K"]} /></span>
    <span className="flex items-center gap-2">Undo <${Kbd} keys=${["⌘", "Z"]} /></span>
    <span className="flex items-center gap-2">Close <${Kbd} keys=${["Esc"]} /></span>
  </div>`;
}
""", """
# Kbd

A keyboard key or shortcut, shown next to the action it triggers or inside menus and the command palette.

## The consumer provides

- `keys`: each key separately, `["⌘", "K"]`. Use the Mac symbols in the UI and show Ctrl on Windows where it matters.
""")

# ------------------------------------------------------------------ Theme + Motion
comp("ThemeToggle", "Actions", 150, """
function Demo() {
  const { ThemeToggle } = BG;
  const [t, setT] = useState("dark");
  return html`<div className="flex flex-wrap items-center gap-6 p-6">
    <${ThemeToggle} />
    <${ThemeToggle} size="sm" />
    <${ThemeToggle} showLabel=${false} theme=${t} onChange=${setT} />
    <span className="text-body-sm text-ink-muted">The first two switch this whole page.</span>
  </div>`;
}
""", """
# ThemeToggle

The Day/Night switch: a sliding sun and moon. Left uncontrolled, it switches the whole page with a circular reveal that grows from the switch.

## The consumer provides

- Nothing, for the usual case: it reads and writes `data-theme` on `<html>` and remembers the choice (localStorage key `bg-theme`).
- Or `theme` and `onChange(theme, origin)` to control it, for example to save the choice to the person's account. Call `useTheme().setTheme(theme, origin)` to keep the reveal.
- `size` `sm` or `md`, and `showLabel` (Day / Night text, default on).

## Use when

- One per screen, in the top bar or the account menu. Not inside forms.
- Restore the saved theme before first paint (an inline script that sets `data-theme`), so the page never flashes the wrong theme.
- The reveal uses the View Transitions API and turns off under reduced motion; the switch still works instantly.
""")

comp("PageTransition", "Motion", 420, """
function Demo() {
  const { useViewTransition, pageEffects, Button, Card } = BG;
  const [fx, setFx] = useState("slide");
  const [page, setPage] = useState(0);
  const go = useViewTransition(fx);
  const pages = [["Workspace hub", "Your projects, drafts and the founding wall."], ["Funnel Studio", "Campaign 2: four steps, two drafts."], ["Profile review", "Twelve profiles waiting for approval."]];
  const nav = (i, e) => go(() => setPage(i), e.currentTarget, i < page ? "back" : "forward");
  return html`<div className="grid gap-4 p-6">
    <div className="flex flex-wrap gap-2" role="group" aria-label="Effect">
      ${pageEffects.map((f) => html`<${Button} key=${f} size="sm" variant=${f === fx ? "strong" : "secondary"} aria-pressed=${f === fx} onClick=${() => setFx(f)}>${f}<//>`)}
    </div>
    <div className="flex gap-2" role="tablist" aria-label="Pages">
      ${pages.map((p, i) => html`<${Button} key=${i} size="sm" variant="ghost" role="tab" aria-selected=${i === page} onClick=${(e) => nav(i, e)}>${p[0]}<//>`)}
    </div>
    <div className="vt-page overflow-hidden rounded-xl border border-line bg-surface p-8">
      <p className="text-label-sm text-ink-subtle">Page ${page + 1} of 3</p>
      <h3 className="mt-2 font-display text-display-sm text-ink">${pages[page][0]}</h3>
      <p className="mt-2 text-body-md text-ink-muted">${pages[page][1]}</p>
    </div>
  </div>`;
}
""", """
# PageTransition

Animated moves between pages and views, on the browser's View Transitions API: the old page animates out while the new one animates in. Seven effects: `reveal`, `slide`, `push`, `zoom`, `flip`, `wipe` and `dissolve`.

## The consumer provides

- A content region with the `vt-page` class. Only that region moves; the shell (top bar, sidebar) holds still.
- The change itself, wrapped: `const go = useViewTransition("slide"); go(() => navigate("/studio"), event.currentTarget)`. Or call `startPageTransition(update, { effect, origin, direction })` directly.
- `direction: "back"` for back navigation, so slide and flip run the other way. `origin` is where `reveal` grows from (the clicked element or the pointer event).

## Use when

- `slide` for moving sideways between peers (tabs, steps). `push` for drilling into a detail. `zoom` for opening something from a grid. `reveal` and `wipe` for big moments (publish, launch). `flip` and `dissolve` sparingly, once per flow.
- One effect per kind of move, the same everywhere in the product.
- Under reduced motion, or in browsers without the API, the change happens instantly. Nothing depends on the animation finishing.
""")

comp("Reveal", "Motion", 360, """
function Demo() {
  const { Reveal, revealEffects, Button } = BG;
  const [k, setK] = useState(0);
  return html`<div className="grid gap-4 p-6">
    <div><${Button} size="sm" variant="secondary" onClick=${() => setK(k + 1)}>Replay<//></div>
    <div key=${k} className="grid grid-cols-2 gap-3 sm:grid-cols-4">
      ${revealEffects.map((fx, i) => html`<${Reveal} key=${fx} effect=${fx} delay=${i * 70} className="grid h-24 place-items-center rounded-lg border border-line bg-surface font-mono text-data-sm text-ink-muted">${fx}<//>`)}
    </div>
  </div>`;
}
""", """
# Reveal

Animates content in as it scrolls into view. Eight effects: `fade-up`, `scale-in`, `blur-in`, `slide-left`, `slide-right`, `clip-up`, `tilt-in` and `pop`.

## The consumer provides

- `effect`, and `delay` in ms to stagger a group (`index * 60`).
- `repeat` to play again each time it re-enters the viewport (default once). `threshold` for how much must be visible first (default 0.2).

## Use when

- Section openers, card grids and marketing pages. Not for app chrome, table rows or anything people need the moment the page loads.
- `fade-up` is the default. Keep one or two effects per page.
- The content is always in the DOM and readable by assistive tech. Under reduced motion it simply shows.
""")

comp("ScrollProgress", "Motion", 200, """
function Demo() {
  const { ScrollProgress } = BG;
  const box = React.useRef(null);
  return html`<div className="grid gap-2 p-6">
    <${ScrollProgress} target=${box} placement="inline" aria-label="Reading progress" />
    <div ref=${box} tabIndex="0" aria-label="Article" className="h-32 overflow-auto rounded-lg border border-line bg-surface p-4 text-body-md text-ink-muted">
      ${Array.from({ length: 8 }, (_, i) => html`<p key=${i} className="mb-3">Paragraph ${i + 1}. Scroll this panel and the mint bar above fills.</p>`)}
    </div>
  </div>`;
}
""", """
# ScrollProgress

A thin mint bar that fills as you scroll: reading progress on long pages, guides and the Journal.

## The consumer provides

- Nothing for the page: `<ScrollProgress />` pins to the top of the viewport.
- `target` (a ref) and `placement="inline"` to follow a scrolling panel instead.

## Use when

- Long reading pages only. Not on dashboards or short pages.
""")

comp("Parallax", "Motion", 260, """
function Demo() {
  const { Parallax, Logo } = BG;
  return html`<div className="relative h-52 overflow-hidden rounded-xl bg-surface-brand p-6" data-theme="dark">
    <${Parallax} speed=${-0.3} className="pointer-events-none absolute -right-8 -bottom-10 opacity-20"><${Logo} layout="mark" height=${180} /><//>
    <p className="relative max-w-xs font-display text-heading-lg text-ink">Scroll the page: the mark drifts behind the text.</p>
  </div>`;
}
""", """
# Parallax

Moves decorative art at a different speed from the scroll, for depth: hero marks, covers, background shapes.

## The consumer provides

- `speed`: 0.2 is gentle, negative moves the other way. Keep it under 0.5.

## Use when

- Decorative layers only, behind content. Never on text people read or controls people use.
- Turns off under reduced motion.
""")

comp("ComingSoon", "Templates", 640, """
function Demo() {
  return html`<div className="h-full"><${BG.Templates.ComingSoon} links=${[{ label: "Instagram", href: "#instagram" }, { label: "Privacy", href: "#privacy" }, { label: "Terms", href: "#terms" }]} /></div>`;
}
""", """
# ComingSoon

The teaser page before launch: logo, a Coming soon badge, the headline, one line of copy and an email signup. It sits on a curved panel over the quiet Europium backdrop, lit by a mint horizon glow; the button and field glow on hover and focus.

## The consumer provides

- `onJoin(email)`: save the email. The page validates the address and shows the confirmation itself.
- `links` for the footer (social, Privacy, Terms, contact) and `copyright`. Take both from the live site; the template invents none.

## Use when

- A product or city that isn't open yet. Keep it this simple: no countdown, no feature list.
- It is a dark-theme island in either theme. The backdrop is `backdrop-europium` (see MATERIALS.md).
""")

comp("SearchResults", "Templates", 900, """
function Demo() {
  return html`<${BG.Templates.SearchResults} imageBase="../../showcase/app/img/" />`;
}
""", """
# SearchResults

Find a Gigster: a brand hero with the people in it, a search bar lifted over its edge, service pills, filters, sort, list or grid, and a rail with an illustrative neighbourhood map and how it works.

## The consumer provides

- `onOpenProfile(id)` and `onNavigate(page)`, to route to a profile or another page.
- `imageBase`: the folder the sample photos are served from.

## Use when

- The public "Find a professional" page. Filters and sort re-flow the results with a view transition: each card glides to its new place.
- Hovering a card lights up its pin on the map, and the other way round.
- All sample people, photos and rates are fictional. Keep the "Fictional sample" notes until real profiles exist.
""")

comp("GigsterProfile", "Templates", 900, """
function Demo() {
  return html`<${BG.Templates.GigsterProfile} personId="jordan" imageBase="../../showcase/app/img/" />`;
}
""", """
# GigsterProfile

A Gigster's public profile: portrait hero over an ambient glow from their own work, a sticky booking card, section tabs that follow the scroll, services, a bento portfolio with a lightbox, example reviews, experience, FAQs and similar professionals.

## The consumer provides

- `personId`, `onBack`, `onOpenProfile(id)`, `onNavigate(page)`, `imageBase`.

## Use when

- The page a client lands on from search. The portrait carries a view-transition name, so it flies from the search card into the hero.
- Request, Check availability and Tell us about your project open a short request form; in this concept nothing is sent.
- Disclosures stay visible: fictional profile, sample availability, credits not verified, insurance not verified.
""")

comp("GigsterOnboarding", "Templates", 900, """
function Demo() {
  return html`<${BG.Templates.GigsterOnboarding} imageBase="../../showcase/app/img/" />`;
}
""", """
# GigsterOnboarding

Five steps from "about you" to a profile ready for review, with a live preview of how clients will see you beside the form.

## The consumer provides

- `onNavigate(page)` and `imageBase`. Wire the final submit to your review queue.

## Use when

- Professionals joining Between Gigs. Steps: About you, Skills, Where & when, Your story, Review.
- Curated lists are chip pickers, not dropdowns: every option visible, one tap to pick or drop. "Something else" goes to private review.
- Continue validates the step and lists what needs fixing; Back and the stepper slide the other way. Review jumps back to any step with Edit.
""")

def main():
    for name, (group, height, code, readme) in C.items():
        d = os.path.join(OUT, name)
        os.makedirs(d, exist_ok=True)
        assert name in LEVEL, f"{name} has no atomic level in LEVELS"
        open(os.path.join(d, "preview.html"), "w").write(HEAD.format(group=group, level=LEVEL[name], height=height, extra=(" width=1440" if name == "AppShell" else ""), name=name, code=code))
        open(os.path.join(d, "README.md"), "w").write(readme + f"\n\n## Level\n\n{LEVEL[name].capitalize()} (atomic design). See README.md, Components.\n")
    print(len(C), "components")

main()
