# WorkspaceTile

A company workspace in the Playset gallery: cover, relationship, name, state and the open link.

## The consumer provides

- `name`, `kind` (Client, Prospect, To organize, Archived), `status` (one line), `href`.
- `color`: a `cat-*` cover color. Derive it from the workspace id so it never changes between visits. `image` replaces it with a picture.
- `pin`: a star IconButton with `pressed`. `secondaryAction`: usually edit.

## Rules

- The cover is a flat category color. No gradients.
- Initials sit on a `surface` plate in `ink`, never directly on the color. That keeps them readable in both themes (dark-theme category colors are light).

## Level

Organism (atomic design). See README.md, Components.
