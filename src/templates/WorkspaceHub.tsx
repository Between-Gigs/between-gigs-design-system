import * as React from "react";
import { ArrowUpRight, GalleryHorizontal, LayoutGrid, List, Pin, Search } from "lucide-react";
import {
  Banner, Button, Count, FilterBar, FilterLabel, IconButton, Input, Inspector, InspectorSection, ModuleCard, PageHeader,
  Pager, SegmentedControl, Select, ShellInspectorButton, StatusBadge, type Status,
} from "../components";
import { HubFrame } from "./HubFrame";

const projects: Array<{ title: string; status: Status; version?: string; progress: number; stage: string }> = [
  { title: "Connected work", status: "preview", version: "v3.46", progress: 55, stage: "Building" },
  { title: "Table Studio", status: "preview", version: "v3.31", progress: 55, stage: "Building" },
  { title: "Feature reminders", status: "working", progress: 70, stage: "Building" },
  { title: "Project management", status: "working", progress: 70, stage: "Building" },
  { title: "Spec Builder", status: "not-started", progress: 0, stage: "Planned" },
];

/** Workspace hub: every module, filtered and grouped by category, with the selected module in the inspector. */
export function WorkspaceHub() {
  const [view, setView] = React.useState("gallery");
  const [selected, setSelected] = React.useState("Connected work");
  const [page, setPage] = React.useState(1);
  const [drawer, setDrawer] = React.useState(false);
  const pick = (title: string) => { setSelected(title); if (window.innerWidth < 1280) setDrawer(true); };
  const sel = projects.find((p) => p.title === selected)!;
  const open = <Button size="sm" variant="secondary" fullWidth iconEnd={<ArrowUpRight />}>Open</Button>;

  return (
    <HubFrame
      module="hub"
      inspectorOpen={drawer}
      onInspectorOpenChange={setDrawer}
      inspector={
        <Inspector eyebrow="Selected module" title={sel.title}>
          <InspectorSection title="Status"><StatusBadge status={sel.status} /></InspectorSection>
          <InspectorSection title="Working version">
            <Select size="sm" aria-label="Working version" defaultValue="current"
              options={[{ value: "current", label: `${sel.version ?? "v1.0"} · current` }, { value: "archive", label: "Previous · archived" }]} />
          </InspectorSection>
          <InspectorSection title="Build progress">
            <p className="text-body-sm text-ink-muted">{sel.stage} · {sel.progress}% estimated. Estimates update when a milestone is checked off.</p>
          </InspectorSection>
          <InspectorSection><Banner tone="info" title="Design stays locked">Text edits only. Global design changes go through a separate review.</Banner></InspectorSection>
        </Inspector>
      }
    >
      <div className="grid gap-8">
        <PageHeader eyebrow="Between Gigs · Builder" title="Workspace hub" description="101 modules · 6 tools" actions={<ShellInspectorButton label="Selected module" />} />
        <FilterBar end={<Button size="sm" variant="ghost">Reset filters</Button>}>
          <Input size="sm" aria-label="Find a page" placeholder="Find a page, tool or path…" start={<Search />} className="min-w-48 flex-1" />
          <FilterLabel htmlFor="hub-status">Status</FilterLabel>
          <Select id="hub-status" size="sm" defaultValue="all" className="w-36"
            options={[{ value: "all", label: "All" }, { value: "working", label: "Working" }, { value: "preview", label: "Preview" }]} />
          <SegmentedControl size="sm" label="View" value={view} onChange={setView} options={[
            { value: "gallery", label: "Gallery", icon: <LayoutGrid /> },
            { value: "list", label: "List", icon: <List /> },
            { value: "coverflow", label: "Coverflow", icon: <GalleryHorizontal /> },
          ]} />
        </FilterBar>

        <section className="grid gap-4 rounded-xl border border-line bg-surface p-6">
          <header className="flex items-center gap-2">
            <h2 className="text-heading-lg text-ink">Projects & planning</h2>
            <Count value={projects.length} />
          </header>
          <p className="-mt-2 text-body-sm text-ink-muted">Plan work, ownership and the next useful step.</p>
          <div className="flex gap-4 overflow-x-auto pb-2">
            {projects.map((p) => (
              <div key={p.title} className="shrink-0">
                <ModuleCard
                  onSelect={() => pick(p.title)}
                  title={p.title}
                  status={p.status}
                  version={p.version}
                  selected={p.title === selected}
                  action={p.status === "not-started" ? undefined : open}
                  pin={<IconButton size="sm" label={`Pin ${p.title}`} icon={<Pin />} />}
                  progress={{ value: p.progress, label: p.stage }}
                />
              </div>
            ))}
          </div>
          <div className="flex justify-center">
            <Pager page={page} pageCount={5} onChange={setPage} itemLabel="Connected work" />
          </div>
        </section>
      </div>
    </HubFrame>
  );
}
