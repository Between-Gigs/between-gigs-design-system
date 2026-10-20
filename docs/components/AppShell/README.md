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
