import * as React from "react";

/* Internal glyphs the components draw themselves. Product icons come from Lucide. */
type GlyphProps = React.SVGProps<SVGSVGElement>;
const glyph = (d: React.ReactNode) =>
  function Glyph(props: GlyphProps) {
    return (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={1.75}
        strokeLinecap="round" strokeLinejoin="round" aria-hidden="true" {...props}>{d}</svg>
    );
  };

export const ChevronDown = glyph(<path d="m6 9 6 6 6-6" />);
export const ChevronLeft = glyph(<path d="m15 18-6-6 6-6" />);
export const ChevronRight = glyph(<path d="m9 18 6-6-6-6" />);
export const Check = glyph(<path d="M20 6 9 17l-5-5" />);
export const Close = glyph(<><path d="M18 6 6 18" /><path d="m6 6 12 12" /></>);
export const Info = glyph(<><circle cx="12" cy="12" r="9" /><path d="M12 16v-4" /><path d="M12 8h.01" /></>);
export const Alert = glyph(<><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0Z" /><path d="M12 9v4" /><path d="M12 17h.01" /></>);
export const CheckCircle = glyph(<><circle cx="12" cy="12" r="9" /><path d="m8.5 12 2.5 2.5 4.5-5" /></>);
export const XCircle = glyph(<><circle cx="12" cy="12" r="9" /><path d="m15 9-6 6" /><path d="m9 9 6 6" /></>);

export function Spinner({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" className={"animate-spin " + (className ?? "")}>
      <circle cx="12" cy="12" r="9" stroke="currentColor" strokeOpacity="0.25" strokeWidth="2.5" />
      <path d="M21 12a9 9 0 0 0-9-9" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" />
    </svg>
  );
}
