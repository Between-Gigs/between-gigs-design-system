# SignIn

Template: sign-in. A brand panel beside a short form: Google first, then email link.

## Built from

Wordmark, Button, Field, Input.

## Rules this screen shows

- The brand panel sets `data-theme="dark"` on its own element, so it is a dark-theme island: every token inside switches to its dark value, and components read correctly on the forest even when the page is light.
- One decisive action ("Continue securely", `strong`). Google is `secondary` so the two don't compete.
- Auth is provided by Clerk; this template is the visual layer around it.
