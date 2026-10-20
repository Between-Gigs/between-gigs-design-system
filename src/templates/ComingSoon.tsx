import * as React from "react";
import { ArrowRight, Check, Mail } from "lucide-react";
import { Badge, Button, Input, Logo } from "../components";

export interface ComingSoonProps {
  /** Called with the email when someone joins the list. */
  onJoin?: (email: string) => void;
}

/** Coming soon: the simple teaser page before launch, on the quiet Europium backdrop. Always a dark-theme island. */
export function ComingSoon({ onJoin }: ComingSoonProps) {
  const [email, setEmail] = React.useState("");
  const [error, setError] = React.useState<string>();
  const [joined, setJoined] = React.useState(false);

  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!/^\S+@\S+\.\S+$/.test(email)) { setError("Enter an email address, like you@example.com."); return; }
    setError(undefined);
    setJoined(true);
    onJoin?.(email);
  };

  return (
    <div data-theme="dark" className="backdrop-europium flex min-h-full flex-col text-ink">
      <header className="px-6 py-6 sm:px-12">
        <Logo height={32} />
      </header>

      <main className="flex flex-1 flex-col items-center justify-center gap-6 px-6 py-16 text-center">
        <Badge tone="brand">Coming soon</Badge>
        <h1 className="max-w-3xl font-display text-display-lg text-balance sm:text-display-xl text-ink">
          Hollywood craft, <span className="text-ink-brand">between gigs.</span>
        </h1>
        <p className="max-w-lg text-body-lg text-ink-muted">
          Set builders, costumers and prop makers for the projects in everyday life. Be first to know when we open.
        </p>

        {joined ? (
          <p role="status" className="mt-2 flex items-center gap-2 text-body-md text-ink">
            <Check className="size-5 text-ink-brand" /> You're on the list. We'll email {email} when we open.
          </p>
        ) : (
          <form noValidate onSubmit={submit} className="mt-2 grid w-full max-w-md gap-2 text-left">
            <div className="flex flex-col gap-3 sm:flex-row">
              <Input type="email" size="lg" aria-label="Email" placeholder="you@example.com" start={<Mail />} value={email}
                invalid={Boolean(error)} aria-describedby={error ? "coming-soon-error" : undefined}
                onChange={(e) => setEmail(e.target.value)} className="sm:flex-1" />
              <Button type="submit" variant="primary" size="lg" iconEnd={<ArrowRight />}>Notify me</Button>
            </div>
            {error && <p id="coming-soon-error" className="text-body-sm text-danger">{error}</p>}
          </form>
        )}
      </main>

      <footer className="px-6 py-6 text-center text-caption text-ink-subtle sm:px-12">© 2026 Between Gigs · Los Angeles</footer>
    </div>
  );
}
