# Tabs

Switches between sections of one page. This is the only tab style in the product: underline tabs, with optional counts.

## The consumer provides

- `Tabs` with `value` / `onChange`; inside it a `TabList` with a `label`, then `Tab`s and matching `TabPanel`s.
- `Tab`: `value`, label, optional `icon` and `count`, `disabled`.

## Use when

- Sections of the same page or record (Studies / Media lab / Profiles).
- To change how the same data is displayed, use SegmentedControl. To go to another page, use links or NavItem.

Arrow keys, Home and End move between tabs. The list scrolls horizontally instead of wrapping.
