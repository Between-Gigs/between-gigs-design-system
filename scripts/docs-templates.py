import os, sys, textwrap
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "components")
T = {
 "WorkspaceHub": (860, """
# WorkspaceHub

Template: the Workspace hub. Every module grouped by category, filtered from the FilterBar, with the selected module in the Inspector.

## Built from

HubFrame (AppShell, TopBar, ModuleBar, Sidebar, PromptBar), PageHeader, FilterBar, Input, Select, SegmentedControl, ModuleCard, Count, Pager, Inspector, StatusBadge, Banner.

## Rules this screen shows

- One section panel per category: `surface`, `radius-xl`, `line`, `space-6` padding, heading-lg title with a Count.
- Selecting a card puts it in the inspector; the card gets the one `selected` outline in the view.
- The primary mint action is absent here on purpose: browsing has no single main action. Each card's Open is secondary.
"""),
 "FunnelStudio": (860, """
# FunnelStudio

Template: Funnel Studio. A campaign's steps left to right on a recessed canvas, traffic sources stacked at the start, the selected step in the inspector.

## Built from

HubFrame, PageHeader with Breadcrumbs, Tag (step-type filters), FunnelStepCard, FlowConnector, Inspector, StatusBadge, Select, Banner, Button.

## Rules this screen shows

- The canvas is `surface-sunken` with `radius-xl`; it scrolls sideways inside its frame, never the page.
- Each step type keeps its category color (`stepTypes`) in the stripe, the dot and the filter label.
- Connectors are labelled with what the person does next ("Claims a card", "Books"). Dashed connectors lead to steps that aren't built.
- Draft campaigns say so in a warning Banner; no counts are shown until there is live traffic.
"""),
 "ReviewQueue": (900, """
# ReviewQueue

Template: profile review for Peter and Patti. Pipeline counts, the submitted queue as a table, and the selected profile with approve and request-changes in the inspector.

## Built from

HubFrame, PageHeader, StageStats, Tabs, Table, Avatar, StatusBadge, Inspector, Field, Textarea, Button, ToastProvider and useToast.

## Rules this screen shows

- "Approve profile" is the `strong` action; "Request changes" is `secondary` and stays disabled until a note is written, because the Gigster needs to know what to fix.
- Both actions confirm with a Toast that offers Undo, instead of a confirmation dialog.
- The Gigster's About me is set in the editorial serif: it's their voice, not interface text.
"""),
 "ProfileBuilder": (900, """
# ProfileBuilder

Template: the Gigster's four-step profile builder (Details, Skills, Availability, Preview), with a live preview of how clients will see the profile.

## Built from

Wordmark, Stepper, Card, Field, Input, Select, Textarea, Button, Avatar, Banner.

## Rules this screen shows

- Onboarding has no app shell: a plain header with the wordmark and "Save and finish later".
- The forward action is `strong` and names the next step ("Continue to Skills"); the last step says "Submit for review".
- The preview updates as people type, so they see their words the way a client will.
"""),
 "SignIn": (760, """
# SignIn

Template: sign-in. A brand panel beside a short form: Google first, then email link.

## Built from

Wordmark, Button, Field, Input.

## Rules this screen shows

- The brand panel sets `data-theme="dark"` on its own element, so it is a dark-theme island: every token inside switches to its dark value, and components read correctly on the forest even when the page is light.
- One decisive action ("Continue securely", `strong`). Google is `secondary` so the two don't compete.
- Auth is provided by Clerk; this template is the visual layer around it.
"""),
 "FoundingLanding": (1000, """
# FoundingLanding

Template: the Founding 20 marketing page hero, with the draft strip, nav, headline, progress, founding cards and stat row.

## Built from

Banner (strip), Wordmark, Button, Progress, Stat, StatRow.

## Rules this screen shows

- Marketing pages are dark-theme islands on `surface-brand`: set `data-theme="dark"` on the page root.
- The headline's second sentence switches to `ink-brand`. One accent per headline.
- Founding cards are artwork: they use primitives (`mint-500`, `lime-300`, `forest-700`, `sage-0`) directly, the one place primitives appear outside tokens. Open slots are dashed and labelled.
- Sample names are marked as illustrative in a caption.
"""),
}
for name, (h, readme) in T.items():
    d = os.path.join(OUT, name); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "preview.html"), "w").write(f"""<!-- @dsCard group="Templates" height={h} width=1440 page -->
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{name}</title>
</head>
<body>
<div id="root" style="height:{h}px"></div>
<script>
ReactDOM.createRoot(document.getElementById("root")).render(React.createElement(window.BetweenGigs.Templates.{name}));
</script>
</body>
</html>
""")
    open(os.path.join(d, "README.md"), "w").write(textwrap.dedent(readme).strip() + "\n")
print(len(T))
