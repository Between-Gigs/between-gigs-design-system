# WorkspaceHub

Template: the Workspace hub. Every module grouped by category, filtered from the FilterBar, with the selected module in the Inspector.

## Built from

HubFrame (AppShell, TopBar, ModuleBar, Sidebar, PromptBar), PageHeader, FilterBar, Input, Select, SegmentedControl, ModuleCard, Count, Pager, Inspector, StatusBadge, Banner.

## Rules this screen shows

- One section panel per category: `surface`, `radius-xl`, `line`, `space-6` padding, heading-lg title with a Count.
- Selecting a card puts it in the inspector; the card gets the one `selected` outline in the view.
- The primary mint action is absent here on purpose: browsing has no single main action. Each card's Open is secondary.
