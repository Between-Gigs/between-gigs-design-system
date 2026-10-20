import * as React from "react";
import { ArrowUpRight } from "lucide-react";
import { Banner, Button, Logo, Progress, Stat, StatRow } from "../components";


const cards = [
  { n: 1, name: "Dana R.", area: "Silver Lake", look: "bg-mint-500 text-forest-950" },
  { n: 2, name: "Marcus T.", area: "Culver City", look: "bg-forest-700 text-sage-0" },
  { n: 3, name: "Priya S.", area: "Echo Park", look: "bg-lime-300 text-forest-950" },
  { n: 4, name: "Hannah K.", area: "Pasadena", look: "bg-mint-300 text-forest-950" },
  { n: 5, name: "Jorge M.", area: "Highland Park", look: "bg-sage-0 text-forest-950" },
  { n: 7, name: "Open", area: "Reserved for you", look: "border-2 border-dashed border-mint-400 text-sage-0", open: true },
];

/** Marketing: the Founding 20 landing hero. The whole page is a dark-theme island on the brand forest. */
export function FoundingLanding() {
  return (
    <div data-theme="dark" className="min-h-full bg-surface-brand text-ink">
      <Banner tone="warning" layout="strip" title="Draft · not public.">Submissions are disabled; sample names are illustrative.</Banner>
      <header className="mx-auto flex max-w-6xl items-center justify-between gap-4 px-6 py-5">
        <Logo height={32} />
        <nav className="flex items-center gap-2">
          <a href="#" className="hidden px-3 text-label-md text-ink-muted hover:text-ink sm:inline">How it works</a>
          <a href="#" className="hidden px-3 text-label-md text-ink-muted hover:text-ink sm:inline">FAQ</a>
          <Button variant="primary" size="sm" iconEnd={<ArrowUpRight />}>Claim a card</Button>
          <Button variant="secondary" size="sm">Sign in</Button>
        </nav>
      </header>
      <main className="mx-auto grid max-w-6xl gap-16 px-6 pt-16 pb-24">
        <section className="grid justify-items-center gap-6 text-center">
          <span className="text-eyebrow text-ink-brand uppercase">The Founding 20 · Los Angeles</span>
          <h1 className="max-w-4xl font-display text-display-lg text-ink text-balance md:text-display-xl">
            Be one of the first twenty. <span className="text-ink-brand">Your first $250 is on us.</span>
          </h1>
          <p className="max-w-2xl text-body-lg text-ink-muted">
            Hire a Hollywood professional for the projects in your everyday life. The first 20 clients to book through Between Gigs
            get a $250 gift card and a permanent place on our Founding Members wall.
          </p>
          <div className="flex flex-wrap justify-center gap-3">
            <Button variant="primary" size="lg" iconEnd={<ArrowUpRight />}>Claim a founding card</Button>
            <Button variant="secondary" size="lg">How it works</Button>
          </div>
          <Progress value={6} max={20} label="Founding cards claimed" valueText="14 of 20 left" className="w-full max-w-sm text-left" />
        </section>
        <section aria-label="Founding cards" className="grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-6">
          {cards.map((c) => (
            <article key={c.n} className={`flex aspect-3/4 flex-col justify-between rounded-2xl p-4 ${c.look}`}>
              <span className="text-eyebrow uppercase opacity-80">Founding member</span>
              <span className="font-display text-display-md tabular-nums">{String(c.n).padStart(2, "0")}<span className="text-body-sm opacity-70">/20</span></span>
              <span className="grid text-body-sm">
                <strong className="font-semibold">{c.name}</strong>
                <span className="opacity-80">{c.area}</span>
              </span>
            </article>
          ))}
        </section>
        <StatRow className="bg-line [&>div]:bg-surface-brand">
          <Stat value="20" label="numbered founding cards" />
          <Stat value="$250" label="gift card toward your first booking" />
          <Stat value="$5,000" label="of work for professionals between productions" />
          <Stat value="1" label="honest review, whatever your experience" />
        </StatRow>
        <p className="text-caption text-ink-subtle">Names shown are illustrative samples for this draft.</p>
      </main>
    </div>
  );
}
