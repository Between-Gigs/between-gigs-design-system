import * as React from "react";
import { cx } from "./cx";
import { Heading, type HeadingLevel } from "./heading";
import { Card } from "./Card";
import { StatusBadge, type Status } from "./StatusBadge";
import type { CategoryColor } from "./WorkspaceTile";

export type StepType = "traffic" | "page" | "form" | "email" | "marketplace";

/** Each step type has one fixed category color, everywhere it appears. */
export const stepTypes: Record<StepType, { label: string; color: CategoryColor }> = {
  traffic: { label: "Traffic source", color: "cat-3" },
  page: { label: "Web page", color: "cat-1" },
  form: { label: "Claim form", color: "cat-4" },
  email: { label: "Email", color: "cat-6" },
  marketplace: { label: "Marketplace", color: "cat-7" },
};

const dots: Record<CategoryColor, string> = {
  "cat-1": "bg-cat-1", "cat-2": "bg-cat-2", "cat-3": "bg-cat-3", "cat-4": "bg-cat-4",
  "cat-5": "bg-cat-5", "cat-6": "bg-cat-6", "cat-7": "bg-cat-7", "cat-8": "bg-cat-8",
};

export interface FunnelStepCardProps {
  type: StepType;
  /** Position in the funnel, shown as "01". */
  step: number;
  title: string;
  /** What happens at this step, with the arrow notation: "Card number + browse professionals → booking". */
  description?: string;
  status: Status;
  /** Screenshot of the page or email, shown on the always-light embed surface. */
  preview?: string;
  /** Short note in the footer ("Double-click to open draft", "Not built yet"). */
  hint?: string;
  selected?: boolean;
  onOpen?: () => void;
  /** Heading level of the title, so it fits the page outline. Default 3. */
  headingLevel?: HeadingLevel;
  className?: string;
}

/** One step on the Funnel Studio canvas: type, order, status, preview and what the step does. */
export function FunnelStepCard({ type, step, title, description, status, preview, hint, selected, onOpen, headingLevel = 3, className }: FunnelStepCardProps) {
  const t = stepTypes[type];
  return (
    <Card padding="none" stripe={t.color} selected={selected} interactive className={cx("flex w-56 flex-col", className)}>
      <div className="flex items-center justify-between gap-2 px-3 pt-3.5">
        <span className="flex items-center gap-1.5 text-label-sm text-ink-muted">
          <span aria-hidden="true" className={cx("size-2 rounded-full", dots[t.color])} />
          {t.label}
        </span>
        <span className="font-mono text-data-sm text-ink-subtle">{String(step).padStart(2, "0")}</span>
      </div>
      <div className="px-3 pt-2"><StatusBadge status={status} size="sm" /></div>
      <button type="button" onClick={onOpen} onDoubleClick={onOpen} aria-label={`Open ${title}`}
        className="mx-3 mt-3 block aspect-4/3 overflow-hidden rounded-sm border border-line bg-surface-embed">
        {preview
          ? <img src={preview} alt="" className="size-full object-cover object-top" />
          : <span className="flex size-full items-center justify-center text-label-sm text-ink-on-embed opacity-60">No preview yet</span>}
      </button>
      <div className="grid gap-1 p-3">
        <Heading level={headingLevel} className="text-heading-sm text-ink">{title}</Heading>
        {description && <p className="text-body-sm text-ink-muted">{description}</p>}
      </div>
      {hint && <p className="mt-auto border-t border-line px-3 py-2 text-caption text-ink-subtle">{hint}</p>}
    </Card>
  );
}
