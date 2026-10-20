import * as React from "react";
import {
  Bell, Building2, Clock, Code2, Columns2, Command, FileText, Filter, FolderKanban, Home, Layers, Mail, Megaphone,
  Mic, Monitor, PanelLeft, Palette, Pencil, Plus, Redo2, Sun, Undo2, Users, BookOpen,
} from "lucide-react";
import {
  AppShell, Avatar, Button, CommandPalette, IconButton, Logo, ModuleBar, NavItem, NavSection, Popover, PromptBar, SegmentedControl,
  ShellMenuButton, Sidebar, Switch, ToolbarDivider, TopBar, useCommandShortcut, type Command as PaletteCommand,
} from "../components";

export const categories = [
  { id: "all", label: "All modules", icon: <Layers />, count: 101 },
  { id: "projects", label: "Projects & planning", icon: <FolderKanban />, count: 5 },
  { id: "pages", label: "Pages & experiences", icon: <FileText />, count: 6 },
  { id: "people", label: "People & knowledge", icon: <Users />, count: 12 },
  { id: "design", label: "Design & experience", icon: <Palette />, count: 23 },
  { id: "dev", label: "Developer tools", icon: <Code2 />, count: 12 },
  { id: "marketing", label: "Marketing & growth", icon: <Megaphone />, count: 8 },
  { id: "ops", label: "Company operations", icon: <Building2 />, count: 9 },
];

const modules = [
  { id: "hub", label: "Hub", icon: <Home /> },
  { id: "design-system", label: "Design system", icon: <Palette /> },
  { id: "email", label: "Email previews", icon: <Mail /> },
  { id: "journal", label: "The Journal", icon: <BookOpen /> },
  { id: "review", label: "Profile review", icon: <Users /> },
  { id: "funnel", label: "Funnel Studio", icon: <Filter /> },
];

export interface HubFrameProps {
  /** Module tab to mark active. */
  module: string;
  /** Sidebar category to mark active. */
  category?: string;
  inspector?: React.ReactNode;
  /** Controls the inspector drawer on screens below xl. */
  inspectorOpen?: boolean;
  onInspectorOpenChange?: (open: boolean) => void;
  children: React.ReactNode;
}

/** The signed-in frame shared by every hub template: top bar, module bar, category sidebar and prompt bar. */
export function HubFrame({ module, category = "all", inspector, inspectorOpen, onInspectorOpenChange, children }: HubFrameProps) {
  const [prompt, setPrompt] = React.useState("");
  const [palette, setPalette] = React.useState(false);
  const [theme, setTheme] = React.useState("system");
  const [materials, setMaterials] = React.useState(false);
  const openPalette = React.useCallback(() => setPalette(true), []);
  useCommandShortcut(openPalette);
  const commands: PaletteCommand[] = [
    ...modules.map((m) => ({ id: "m-" + m.id, group: "Modules", label: m.label, icon: m.icon, onRun: () => {} })),
    ...categories.slice(1).map((c) => ({ id: "c-" + c.id, group: "Categories", label: c.label, icon: c.icon, onRun: () => {} })),
    { id: "a-new", group: "Actions", label: "New module", icon: <Plus />, onRun: () => {} },
    { id: "a-theme", group: "Actions", label: "Switch to dark theme", icon: <Sun />, keywords: "appearance", onRun: () => setTheme("dark") },
  ];
  return (
    <>
    <CommandPalette open={palette} onClose={() => setPalette(false)} commands={commands} />
    <AppShell
      inspectorOpen={inspectorOpen}
      onInspectorOpenChange={onInspectorOpenChange}
      topBar={
        <TopBar
          brand={<>
            <ShellMenuButton />
            <Logo layout="mark" height={20} className="ml-1 hidden sm:block" />
            <Button variant="ghost" size="sm">Between Gigs</Button>
            <span className="hidden font-mono text-data-sm text-ink-subtle sm:inline">v3.64</span>
          </>}
          start={<>
            <ToolbarDivider />
            <IconButton size="sm" label="Undo" icon={<Undo2 />} />
            <IconButton size="sm" label="Redo" icon={<Redo2 />} />
            <ToolbarDivider />
            <Button size="sm" variant="ghost" iconStart={<Pencil />}>Sketch</Button>
          </>}
          end={<>
            <span className="hidden items-center gap-1.5 lg:flex">
              <IconButton size="sm" label="Single pane" pressed icon={<Monitor />} />
              <IconButton size="sm" label="Two panes" icon={<Columns2 />} />
              <ToolbarDivider />
            </span>
            <Popover align="end" label="Appearance" title="Appearance" trigger={<IconButton size="sm" label="Appearance" icon={<Sun />} />}>
              <SegmentedControl label="Theme" size="sm" value={theme} onChange={setTheme}
                options={[{ value: "system", label: "System" }, { value: "light", label: "Light" }, { value: "dark", label: "Dark" }]} />
              <Switch checked={materials} onChange={setMaterials} label="Materials" description="Add your personal finish to the shell." />
            </Popover>
            <IconButton size="sm" label="Notifications" icon={<Bell />} />
            <Avatar name="Justin Massion" />
          </>}
        />
      }
      moduleBar={<ModuleBar items={modules} activeId={module} />}
      sidebar={
        <Sidebar
          title="Workspace"
          headerAction={<IconButton size="sm" label="Collapse sidebar" icon={<PanelLeft />} />}
          footer={<>
            <NavItem href="#" label="Version history" icon={<Clock />} />
            <NavItem href="#" label="Team workspace" icon={<Users />} />
          </>}
        >
          <NavSection>
            {categories.map((c) => (
              <NavItem key={c.id} href="#" label={c.label} icon={c.icon} count={c.count} active={c.id === category} />
            ))}
          </NavSection>
        </Sidebar>
      }
      inspector={inspector}
      prompt={
        <PromptBar
          value={prompt}
          onChange={setPrompt}
          onSubmit={() => setPrompt("")}
          start={<>
            <IconButton size="sm" label="Command menu (⌘K)" icon={<Command />} onClick={openPalette} />
            <IconButton size="sm" label="Attach" icon={<Plus />} />
          </>}
          end={<IconButton size="sm" label="Voice" icon={<Mic />} />}
        />
      }
    >
      {children}
    </AppShell>
    </>
  );
}
