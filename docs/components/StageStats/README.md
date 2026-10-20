# StageStats

Counts per stage of a pipeline, in order: Invited → Signed in → Draft → Submitted → Changes requested → Approved → In gallery.

## The consumer provides

- `title` and `stages`: `{ label, value, attention? }[]` in pipeline order.
- `value: null` shows a dash: the stage exists but nothing is counted yet. Never show 0 for "not measured".
- `attention`: highlights stages waiting on someone (Submitted waits on Peter or Patti).

Use real counts only. In proposals and drafts, show dashes, not invented numbers.
