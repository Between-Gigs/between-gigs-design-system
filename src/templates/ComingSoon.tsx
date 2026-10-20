import * as React from "react";
import { ArrowUpRight, Check, Mail } from "lucide-react";
import { Button, Input, Logo } from "../components";

export interface ComingSoonLink {
  label: string;
  href: string;
}

export interface ComingSoonProps {
  /** Called with the email when someone joins the list. */
  onJoin?: (email: string) => void;
  /** Footer links (Instagram, Privacy, Terms, contact). Take them from the live site. */
  links?: ComingSoonLink[];
  /** Footer copyright line. Default "© 2026 Between Gigs". */
  copyright?: string;
}

/**
 * Coming soon: the simple teaser page before launch. A curved, glowing panel on the quiet Europium
 * backdrop, with one email capture. Always a dark-theme island.
 */
export function ComingSoon({ onJoin, links = [], copyright = "© 2026 Between Gigs" }: ComingSoonProps) {
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
    <div data-theme="dark" className="flex min-h-full bg-bg p-2 sm:p-3">
      <div className="backdrop-europium relative isolate flex flex-1 flex-col overflow-hidden rounded-xl border border-line text-ink sm:rounded-2xl">
        <span aria-hidden="true" className="glow-horizon" />

        <header className="relative z-raised px-6 py-6 sm:px-10">
          <Logo height={30} />
        </header>

        <main className="relative z-raised flex flex-1 flex-col items-center justify-center gap-6 px-6 pt-10 pb-24 text-center">
          <p className="text-eyebrow text-ink-brand uppercase">Extraordinary talent. Everyday solutions.</p>
          <h1 className="max-w-3xl font-display text-display-lg text-balance text-ink sm:text-display-xl">
            Coming <span className="glow-text text-ink-brand">soon.</span>
          </h1>
          <p className="max-w-lg text-body-lg text-ink-muted">
            Los Angeles Call Sheet
          </p>

          {joined ? (
            <p role="status" className="mt-2 flex items-center gap-2 rounded-full border border-line bg-surface px-4 py-2 text-body-md text-ink">
              <Check className="size-5 text-ink-brand" /> You're on the call sheet. We'll email {email} when we open.
            </p>
          ) : (
            <form noValidate onSubmit={submit} className="mt-2 grid w-full max-w-md gap-2 text-left">
              <div className="flex flex-col gap-3 sm:flex-row">
                <Input type="email" size="lg" aria-label="Email" placeholder="you@example.com" start={<Mail />} value={email}
                  invalid={Boolean(error)} aria-describedby={error ? "coming-soon-error" : undefined}
                  onChange={(e) => setEmail(e.target.value)} className="glow-focus sm:flex-1" />
                <Button type="submit" variant="primary" size="lg" className="group glow-hover"
                  iconEnd={<ArrowUpRight className="transition-transform duration-base group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />}>Get on the call sheet</Button>
              </div>
              {error && <p id="coming-soon-error" className="text-body-sm text-danger">{error}</p>}
            </form>
          )}
        </main>

        <footer className="relative z-raised flex flex-wrap items-center justify-between gap-3 px-6 py-5 text-caption text-ink-subtle sm:px-10">
          <span>{copyright}</span>
          {links.length > 0 && (
            <nav aria-label="Footer" className="flex flex-wrap gap-x-5 gap-y-2">
              {links.map((l) => (
                <a key={l.href} href={l.href} className="inline-flex min-h-6 items-center rounded-xs text-ink-muted underline-offset-4 transition-colors duration-fast hover:text-ink-brand hover:underline">{l.label}</a>
              ))}
            </nav>
          )}
        </footer>
      </div>
    </div>
  );
}
