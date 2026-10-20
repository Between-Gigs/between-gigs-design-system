import * as React from "react";
import { ArrowUpRight, X } from "lucide-react";
import {
  Banner, Breadcrumbs, Button, FlowConnector, FunnelStepCard, IconButton, Inspector, InspectorSection, PageHeader, ShellInspectorButton,
  Select, StatusBadge, Tag, stepTypes, type Status, type StepType,
} from "../components";
import { HubFrame } from "./HubFrame";

interface Step { id: string; type: StepType; step: number; title: string; description: string; status: Status; hint: string; link?: string }

const sources: Step[] = [
  { id: "s1", type: "traffic", step: 1, title: "As seen in Deadline", description: "Press, social posts and Peter's network → landing page", status: "published", hint: "External traffic" },
  { id: "s2", type: "traffic", step: 2, title: "Paid and social ads", description: "Six concepts → landing page", status: "draft", hint: "External traffic" },
];
const path: Step[] = [
  { id: "p3", type: "page", step: 3, title: "Founding 20 landing", description: "Card wheel, offer, how it works → Claim", status: "draft", hint: "Double-click to open draft", link: "Claims a card" },
  { id: "p4", type: "form", step: 4, title: "Claim your card", description: "Name, email, ZIP, project, wall opt-in → reserved email", status: "draft", hint: "Double-click to open draft", link: "Submits" },
  { id: "p5", type: "email", step: 5, title: "Your card is reserved", description: "Card number + browse professionals → booking", status: "draft", hint: "Double-click to open draft", link: "Books" },
  { id: "p6", type: "marketplace", step: 6, title: "Book a professional", description: "Client books and pays through Between Gigs; $250 applied", status: "not-started", hint: "Not built yet", link: "Job done" },
  { id: "p7", type: "email", step: 7, title: "How did it go?", description: "Honest review + wall preferences → wall", status: "draft", hint: "Double-click to open draft", link: "Reviews" },
];
const all = [...sources, ...path];

/** Funnel Studio: the campaign's steps laid out left to right on a canvas, with the selected step in the inspector. */
export function FunnelStudio() {
  const [selected, setSelected] = React.useState("p3");
  const [types, setTypes] = React.useState<StepType[]>([]);
  const [drawer, setDrawer] = React.useState(false);
  const pick = (id: string) => { setSelected(id); if (window.innerWidth < 1280) setDrawer(true); };
  const sel = all.find((s) => s.id === selected)!;
  const shown = (s: Step) => types.length === 0 || types.includes(s.type);
  const toggle = (t: StepType) => setTypes((xs) => (xs.includes(t) ? xs.filter((x) => x !== t) : [...xs, t]));

  return (
    <HubFrame
      module="funnel"
      category="marketing"
      inspectorOpen={drawer}
      onInspectorOpenChange={setDrawer}
      inspector={
        <Inspector eyebrow="Selected step" title={sel.title} actions={<IconButton size="sm" label="Close inspector" icon={<X />} />}>
          <InspectorSection>
            <div className="flex flex-wrap items-center gap-2">
              <span className="text-label-sm text-ink-muted">{stepTypes[sel.type].label}</span>
              <StatusBadge status={sel.status} size="sm" />
            </div>
            <p className="text-body-sm text-ink-muted">{sel.description}</p>
          </InspectorSection>
          <InspectorSection title="Preview appearance">
            <Select size="sm" aria-label="Preview appearance" defaultValue="default"
              options={[{ value: "default", label: "Defaults · pages dark / email light" }, { value: "light", label: "Everything light" }, { value: "dark", label: "Everything dark" }]} />
          </InspectorSection>
          <InspectorSection>
            <Banner tone="warning" title="Draft campaign">No live traffic or counts yet. Submissions are disabled.</Banner>
            <Button variant="secondary" fullWidth iconEnd={<ArrowUpRight />}>Open draft</Button>
          </InspectorSection>
        </Inspector>
      }
    >
      <div className="grid gap-6">
        <PageHeader
          breadcrumbs={<Breadcrumbs items={[{ label: "Workspace", href: "#" }, { label: "Marketing & growth", href: "#" }, { label: "Funnel Studio" }]} />}
          eyebrow="Campaign 2 · Draft"
          title="The Founding 20"
          description="20 × $250 gift cards for the first clients who book."
          actions={<><ShellInspectorButton label="Selected step" /><Button variant="secondary" iconEnd={<ArrowUpRight />}>Press</Button><Button variant="primary" iconEnd={<ArrowUpRight />}>Walk the funnel</Button></>}
        />
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div className="flex flex-wrap gap-2" role="group" aria-label="Show step types">
            {(Object.keys(stepTypes) as StepType[]).map((t) => (
              <Tag key={t} selected={types.includes(t)} onSelect={() => toggle(t)}>{stepTypes[t].label}</Tag>
            ))}
          </div>
          <p className="text-body-sm text-ink-muted">7 steps · 1 form · 2 emails · 2 traffic sources</p>
        </div>

        <div className="overflow-x-auto rounded-xl border border-line bg-surface-sunken p-6">
          <div className="flex w-max items-stretch gap-0">
            <div className="flex flex-col gap-4">
              {sources.filter(shown).map((s) => (
                <FunnelStepCard key={s.id} {...s} headingLevel={2} selected={s.id === selected} onOpen={() => pick(s.id)} />
              ))}
            </div>
            {path.filter(shown).map((s) => (
              <React.Fragment key={s.id}>
                <FlowConnector label={s.step === 3 ? "Clicks" : path[path.indexOf(s) - 1]?.link} variant={s.status === "not-started" ? "dashed" : "solid"} />
                <FunnelStepCard {...s} headingLevel={2} selected={s.id === selected} onOpen={() => pick(s.id)} />
              </React.Fragment>
            ))}
          </div>
        </div>
      </div>
    </HubFrame>
  );
}
