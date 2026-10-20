# ConfirmDialog

Asks before something destructive or hard to undo.

## The consumer provides

- `open`, `onCancel`, `onConfirm`, `busy` while it runs.
- `title`: a question that names the thing ("Remove Maya Chen from the gallery?").
- `description`: what happens and whether it can be undone.
- `confirmLabel`: the action as a verb ("Remove profile"). Never "OK" or "Yes".
- `tone`: `danger` (default) or `default`.

If the action can be undone, skip the dialog and offer Undo in a Toast instead.
