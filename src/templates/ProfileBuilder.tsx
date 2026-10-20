import * as React from "react";
import { ArrowLeft, ArrowRight } from "lucide-react";
import { Avatar, Banner, Button, Card, Field, Input, Logo, Select, Stepper, Textarea } from "../components";


const steps = ["Details", "Skills", "Availability", "Preview"];

/** The Gigster's four-step profile builder. Step 1 shown: details, with a live preview of the profile card. */
export function ProfileBuilder() {
  const [step, setStep] = React.useState(0);
  const [name, setName] = React.useState("Maya Chen");
  const [role, setRole] = React.useState("Set carpenter");
  const [dept, setDept] = React.useState("art");
  const [about, setAbout] = React.useState("I turn tricky spaces into practical storage, with a clear plan and a careful finish.");
  const deptLabel = { art: "Art department", wardrobe: "Costume & wardrobe", camera: "Camera", locations: "Locations" }[dept];

  return (
    <div className="min-h-full bg-bg">
      <header className="flex h-16 items-center justify-between border-b border-line bg-surface px-6">
        <Logo height={28} />
        <Button variant="ghost" size="sm">Save and finish later</Button>
      </header>
      <main className="mx-auto grid max-w-5xl gap-8 px-6 py-10">
        <div className="grid gap-2">
          <span className="text-eyebrow text-ink-brand uppercase">Create your Gigster profile</span>
          <h1 className="font-display text-display-sm text-ink">Your profile, in your words.</h1>
          <p className="text-body-lg text-ink-muted">You signed up. Now tell clients what you offer. Peter or Patti reviews every profile before it goes live.</p>
        </div>
        <Stepper steps={steps} current={step} onStepClick={setStep} className="max-w-xl" />
        <div className="grid items-start gap-6 lg:grid-cols-5">
          <Card padding="lg" className="grid gap-5 lg:col-span-3">
            <h2 className="text-heading-lg text-ink">{steps[step]}</h2>
            <Field label="Full name"><Input value={name} onChange={(e) => setName(e.target.value)} /></Field>
            <div className="grid gap-5 sm:grid-cols-2">
              <Field label="What you do on set"><Input value={role} onChange={(e) => setRole(e.target.value)} /></Field>
              <Field label="Department">
                <Select value={dept} onChange={(e) => setDept(e.target.value)} options={[
                  { value: "art", label: "Art department" }, { value: "wardrobe", label: "Costume & wardrobe" },
                  { value: "camera", label: "Camera" }, { value: "locations", label: "Locations" },
                ]} />
              </Field>
            </div>
            <Field label="About me" hint="One or two sentences. Say what you'd do for someone at home, not your full credits.">
              <Textarea rows={3} maxLength={240} showCount value={about} onChange={(e) => setAbout(e.target.value)} />
            </Field>
            <div className="flex justify-between gap-3 border-t border-line pt-5">
              <Button variant="ghost" iconStart={<ArrowLeft />} disabled={step === 0} onClick={() => setStep((s) => s - 1)}>Back</Button>
              <Button variant="strong" iconEnd={<ArrowRight />} onClick={() => setStep((s) => Math.min(s + 1, 3))}>
                {step === 3 ? "Submit for review" : `Continue to ${steps[step + 1]}`}
              </Button>
            </div>
          </Card>
          <aside className="grid gap-3 lg:col-span-2">
            <span className="text-label-sm text-ink-muted">How clients will see you</span>
            <Card className="grid gap-4">
              <div className="flex items-center gap-3">
                <Avatar name={name || "Your name"} size="lg" />
                <div className="grid">
                  <span className="text-eyebrow text-ink-subtle uppercase">Gigster profile</span>
                  <span className="font-display text-heading-lg text-ink">{name || "Your name"}</span>
                  <span className="text-body-sm text-ink-muted">{role} · {deptLabel}</span>
                </div>
              </div>
              <p className="font-serif text-editorial-md text-ink italic">{about || "Your About me appears here."}</p>
            </Card>
            <Banner tone="info">Nothing is public until your profile is approved.</Banner>
          </aside>
        </div>
      </main>
    </div>
  );
}
