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

## Level

Molecule (atomic design). See README.md, Components.
