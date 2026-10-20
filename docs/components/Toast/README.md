# Toast

A brief confirmation that something just happened, with an optional Undo.

## The consumer provides

- Mount `ToastProvider` once near the app root, then call `useToast()` and `show({ message, tone, action, duration })`.
- `message`: past tense, says what happened ("Changes saved", "Profile approved").
- `action`: one short action, usually Undo or Redo. Toasts with an action stay at least 6 seconds.

## Don't

- Don't use a toast for errors the person must act on; use a Banner.
- Don't stack more than three. The provider keeps the newest three.
