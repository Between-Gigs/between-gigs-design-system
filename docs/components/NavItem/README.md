# NavItem

One row in the sidebar or a section nav, with an icon and an optional count. `NavSection` groups rows under a title.

## The consumer provides

- `label`, `href` (or other anchor props), `icon`, `count`.
- `active`: the current page. Sets `aria-current="page"`.
- `collapsed`: rail mode, icon only; the label becomes the accessible name and tooltip.

Sidebar rows use Lucide icons at 20px. The illustrated category artwork belongs in category headers, not in nav rows.
