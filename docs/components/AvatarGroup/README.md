# AvatarGroup

Overlapping avatars for a team, contributors or who's in a call, with "+N" for the rest.

## The consumer provides

- `people`: `{ name, src? }[]`, most relevant first. `max` (default 4), `size` (`sm`, `md`).

The whole group is announced once with every name, so screen readers don't read each avatar.
