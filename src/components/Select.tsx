import * as React from "react";
import { cx } from "./cx";
import { ChevronDown } from "./icons";
import { controlFrame, type ControlSize } from "./Input";

export interface SelectOption {
  value: string;
  label: string;
  disabled?: boolean;
}

export interface SelectProps extends Omit<React.SelectHTMLAttributes<HTMLSelectElement>, "size"> {
  options: SelectOption[];
  /** Shown as a first, unselectable option when there is no value yet ("Choose a service"). */
  placeholder?: string;
  size?: ControlSize;
  invalid?: boolean;
  /** Icon before the value (filter bars use one). */
  start?: React.ReactNode;
}

/** A native select in the system's frame. Native keeps keyboard, mobile pickers and screen readers right for free. */
export const Select = React.forwardRef<HTMLSelectElement, SelectProps>(function Select(
  { options, placeholder, size = "md", invalid, start, className, disabled, value, defaultValue, ...rest },
  ref,
) {
  return (
    <div className={cx(controlFrame(size, invalid, disabled), "relative pr-0", className)}>
      {start}
      <select
        ref={ref}
        disabled={disabled}
        value={value}
        defaultValue={value === undefined ? defaultValue ?? (placeholder ? "" : undefined) : undefined}
        aria-invalid={invalid || undefined}
        className="h-full min-w-0 flex-1 cursor-pointer appearance-none bg-transparent pr-9 outline-none focus-visible:outline-none disabled:cursor-not-allowed"
        {...rest}
      >
        {placeholder && <option value="" disabled>{placeholder}</option>}
        {options.map((o) => (
          <option key={o.value} value={o.value} disabled={o.disabled}>{o.label}</option>
        ))}
      </select>
      <ChevronDown className="pointer-events-none absolute right-3" />
    </div>
  );
});
