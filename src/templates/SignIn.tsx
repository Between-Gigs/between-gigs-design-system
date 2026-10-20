import * as React from "react";
import { Lock, Mail } from "lucide-react";
import { Button, Field, Input, Logo } from "../components";


/** Sign-in: a brand panel beside the form. The brand panel is a dark-theme island, so components inside it read correctly in either theme. */
export function SignIn() {
  return (
    <div className="grid min-h-full bg-bg lg:grid-cols-2">
      <section data-theme="dark" className="hidden flex-col justify-between bg-surface-brand p-12 text-ink lg:flex">
        <Logo height={36} />
        <div className="grid max-w-md gap-4">
          <h1 className="font-display text-display-lg text-ink text-balance">
            Your craft. <span className="text-ink-brand">More possibilities.</span>
          </h1>
          <p className="text-body-lg text-ink-muted">Hollywood professionals, available for the projects in everyday life.</p>
        </div>
        <p className="text-caption text-ink-subtle">Launching in Los Angeles.</p>
      </section>
      <main className="flex items-center justify-center p-6">
        <div className="grid w-full max-w-sm gap-6">
          <div className="lg:hidden"><Logo height={28} /></div>
          <div className="grid gap-2">
            <span className="inline-flex size-12 items-center justify-center rounded-full bg-surface-selected text-ink-brand"><Lock className="size-5" /></span>
            <h2 className="font-display text-display-sm text-ink">Welcome to Between Gigs</h2>
            <p className="text-body-md text-ink-muted">Sign in to access your profile and continue where you left off.</p>
          </div>
          <Button variant="secondary" size="lg" fullWidth iconStart={<span className="font-display text-label-md">G</span>}>Continue with Google</Button>
          <div className="flex items-center gap-3 text-body-sm text-ink-subtle"><span className="h-px flex-1 bg-line" />or<span className="h-px flex-1 bg-line" /></div>
          <form className="grid gap-4" onSubmit={(e) => e.preventDefault()}>
            <Field label="Email"><Input type="email" size="lg" placeholder="you@example.com" start={<Mail />} /></Field>
            <Button type="submit" variant="strong" size="lg" fullWidth>Continue securely</Button>
          </form>
          <p className="text-caption text-ink-subtle">We'll email you a sign-in link. No password to remember.</p>
        </div>
      </main>
    </div>
  );
}
