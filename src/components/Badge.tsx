import * as React from "react";
import { cx } from "./cx";

export type BadgeTone = "success" | "warning" | "danger" | "info" | "neutral" | "brand";

export interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  tone?: BadgeTone;
  /** A leading dot in the tone color. Use when the badge sits in a dense list. */
  dot?: boolean;
  icon?: React.ReactNode;
  size?: "sm" | "md";
}

const tones: Record<BadgeTone, string> = {
  success: "bg-success-soft text-success",
  warning: "bg-warning-soft text-warning",
  danger: "bg-danger-soft text-danger",
  info: "bg-info-soft text-info",
  neutral: "bg-neutral-soft text-ink-muted",
  brand: "bg-surface-selected text-ink-brand",
};

/** A short label for state or type. For the fixed status words use StatusBadge. */
export function Badge({ tone = "neutral", dot, icon, size = "md", className, children, ...rest }: BadgeProps) {
  return (
    <span
      className={cx(
        "inline-flex shrink-0 items-center gap-1.5 rounded-full text-label-sm whitespace-nowrap [&_svg]:size-3.5",
        size === "sm" ? "h-5 px-2" : "h-6 px-2.5",
        tones[tone],
        className,
      )}
      {...rest}
    >
      {dot && <span aria-hidden="true" className="size-1.5 rounded-full bg-current" />}
      {icon}
      {children}
    </span>
  );
}
