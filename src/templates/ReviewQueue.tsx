import * as React from "react";
import { MessageSquare, ShieldCheck } from "lucide-react";
import {
  Avatar, Button, Field, Inspector, InspectorSection, PageHeader, ShellInspectorButton, StageStats, StatusBadge, Tab, TabList, TabPanel, Tabs, Table,
  Textarea, useToast, ToastProvider, type Status,
} from "../components";
import { HubFrame } from "./HubFrame";

interface Profile { id: string; name: string; role: string; department: string; about: string; submitted: string; status: Status }

const profiles: Profile[] = [
  { id: "1", name: "Maya Chen", role: "Set carpenter", department: "Art department", about: "I turn tricky spaces into practical storage, with a clear plan and a careful finish.", submitted: "Oct 18", status: "needs-review" },
  { id: "2", name: "Luis Ortega", role: "Set carpenter", department: "Custom furniture", about: "Thoughtful custom furniture and creative builds, from sketch to finish.", submitted: "Oct 17", status: "needs-review" },
  { id: "3", name: "Renée Duval", role: "Production coordinator", department: "Events", about: "Calm coordination, memorable gatherings and a plan for every moving part.", submitted: "Oct 16", status: "needs-review" },
  { id: "4", name: "Devon Price", role: "Location scout", department: "Locations", about: "Independent films and commercial shoots across Los Angeles.", submitted: "Oct 15", status: "needs-review" },
];

function Queue() {
  const [tab, setTab] = React.useState("submitted");
  const [selected, setSelected] = React.useState("1");
  const [note, setNote] = React.useState("");
  const [drawer, setDrawer] = React.useState(false);
  const show = useToast();
  const p = profiles.find((x) => x.id === selected)!;

  return (
    <HubFrame
      module="review"
      category="people"
      inspectorOpen={drawer}
      onInspectorOpenChange={setDrawer}
      inspector={
        <Inspector eyebrow="Review this profile" title={p.name}>
          <InspectorSection>
            <div className="flex items-center gap-3">
              <Avatar name={p.name} size="lg" />
              <div className="grid">
                <span className="text-eyebrow text-ink-subtle uppercase">Gigster profile</span>
                <span className="text-body-sm text-ink-muted">{p.role} · {p.department}</span>
              </div>
            </div>
            <figure className="grid gap-1">
              <figcaption className="text-label-sm text-ink-muted">About me</figcaption>
              <blockquote className="font-serif text-editorial-md text-ink italic">{p.about}</blockquote>
            </figure>
          </InspectorSection>
          <InspectorSection title="Checks">
            <ul className="grid gap-2 text-body-sm text-ink-muted">
              <li className="flex items-center gap-2"><ShieldCheck className="size-4 text-success" /> Email verified</li>
              <li className="flex items-center gap-2"><ShieldCheck className="size-4 text-success" /> Professionals form respondent</li>
            </ul>
          </InspectorSection>
          <InspectorSection>
            <Field label="Note for the Gigster" hint="Required when you request changes. They'll see it on their profile." optional>
              <Textarea rows={3} value={note} onChange={(e) => setNote(e.target.value)} placeholder="Add two photos of finished builds…" />
            </Field>
            <div className="grid grid-cols-2 gap-2">
              <Button variant="secondary" iconStart={<MessageSquare />} disabled={!note.trim()}
                onClick={() => show({ message: `Changes requested from ${p.name}`, action: { label: "Undo", onClick: () => {} } })}>
                Request changes
              </Button>
              <Button variant="strong" onClick={() => show({ message: `${p.name} approved`, tone: "success", action: { label: "Undo", onClick: () => {} } })}>
                Approve profile
              </Button>
            </div>
          </InspectorSection>
        </Inspector>
      }
    >
      <div className="grid gap-6">
        <PageHeader eyebrow="People & knowledge" title="Profile review" description="Peter and Patti approve every profile before it joins the gallery."
          actions={<ShellInspectorButton label="Review panel" />} />
        <StageStats headingLevel={2} title="This cohort" stages={[
          { label: "Invited", value: 120 }, { label: "Signed in", value: 64 }, { label: "Draft", value: 31 },
          { label: "Submitted", value: 12, attention: true }, { label: "Changes requested", value: 4 }, { label: "Approved", value: 18 }, { label: "In gallery", value: null },
        ]} />
        <Tabs value={tab} onChange={setTab}>
          <TabList label="Review queue">
            <Tab value="submitted" count={12}>Submitted</Tab>
            <Tab value="changes" count={4}>Changes requested</Tab>
            <Tab value="approved" count={18}>Approved</Tab>
          </TabList>
          <TabPanel value={tab} className="pt-4">
        <Table
          caption="Submitted profiles"
          rows={profiles}
          rowKey={(r) => r.id}
          selectedKey={selected}
          onRowClick={(r) => { setSelected(r.id); if (window.innerWidth < 1280) setDrawer(true); }}
          columns={[
            { key: "name", header: "Gigster", cell: (r) => (
              <span className="flex items-center gap-3">
                <Avatar name={r.name} size="sm" />
                <span className="grid"><span className="text-label-md">{r.name}</span><span className="text-body-sm text-ink-muted">{r.role} · {r.department}</span></span>
              </span>
            ) },
            { key: "status", header: "Status", cell: (r) => <StatusBadge status={r.status} size="sm" /> },
            { key: "submitted", header: "Submitted", align: "end" },
          ]}
        />
          </TabPanel>
        </Tabs>
        <p className="text-caption text-ink-subtle">Sample profiles. Names and details are fictional.</p>
      </div>
    </HubFrame>
  );
}

/** Profile review: the queue of submitted Gigster profiles, with approve and request-changes in the inspector. */
export function ReviewQueue() {
  return <ToastProvider><Queue /></ToastProvider>;
}
