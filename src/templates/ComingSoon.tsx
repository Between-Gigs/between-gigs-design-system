import * as React from "react";
import { ArrowUpRight } from "lucide-react";
import { Logo, cx } from "../components";
import { buttonSizes, buttonVariants } from "../components/Button";

export interface ComingSoonLink {
  label: string;
  href: string;
}

export interface ComingSoonProps {
  /** Where "Get on the call sheet" goes: the sign-up form or page. Default "#call-sheet". */
  ctaHref?: string;
  /** Called when the button is pressed, for analytics or to open a sign-up dialog. */
  onCta?: (event: React.MouseEvent<HTMLAnchorElement>) => void;
  /** Footer links (Instagram, Privacy, Terms, contact). Take them from the live site. */
  links?: ComingSoonLink[];
  /** Footer copyright line. Default "© 2026 Between Gigs". */
  copyright?: string;
}

/**
 * Coming soon: the simple teaser page before launch. A curved, glowing panel on the quiet Europium
 * backdrop, with one call to action. Always a dark-theme island.
 */
export function ComingSoon({ ctaHref = "#call-sheet", onCta, links = [], copyright = "© 2026 Between Gigs" }: ComingSoonProps) {
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
          <p className="text-body-lg text-ink-muted">Los Angeles Call Sheet</p>
          <a href={ctaHref} onClick={onCta}
            className={cx("group glow-hover mt-4 inline-flex shrink-0 items-center justify-center rounded-lg font-sans whitespace-nowrap transition-colors duration-fast [&_svg]:size-5",
              buttonVariants.primary, buttonSizes.lg, "h-14 px-8 text-heading-sm")}>
            Get on the call sheet
            <ArrowUpRight aria-hidden="true" className="transition-transform duration-base group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
          </a>
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
