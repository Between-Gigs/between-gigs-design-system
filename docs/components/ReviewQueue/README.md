# ReviewQueue

Template: profile review for Peter and Patti. Pipeline counts, the submitted queue as a table, and the selected profile with approve and request-changes in the inspector.

## Built from

HubFrame, PageHeader, StageStats, Tabs, Table, Avatar, StatusBadge, Inspector, Field, Textarea, Button, ToastProvider and useToast.

## Rules this screen shows

- "Approve profile" is the `strong` action; "Request changes" is `secondary` and stays disabled until a note is written, because the Gigster needs to know what to fix.
- Both actions confirm with a Toast that offers Undo, instead of a confirmation dialog.
- The Gigster's About me is set in the editorial serif: it's their voice, not interface text.
