# Stepper

Shows where someone is in a multi-step flow, such as the four-step profile builder.

## The consumer provides

- `steps`: short step names. Three to five steps; more means the flow should be split.
- `current`: 0-based index. Earlier steps show a check.
- `onStepClick`: lets people go back to a finished step. Forward jumps aren't offered.

The current step is marked with `aria-current="step"`. Pair it with a forward button that names the next step ("Continue to Skills").
