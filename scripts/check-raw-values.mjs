// Fails if component or template code bypasses the tokens: raw hex colors, rgb()/hsl() literals,
// or Tailwind arbitrary values like p-[13px] or bg-[#123456]. Add a token instead.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const dirs = ["src/components"];
// Files allowed to hold raw values, and why.
const allow = new Set(["src/components/Logo.tsx"]); // exact logo paths; inks come from logo-* tokens
const rules = [
  { name: "raw hex color", re: /(?<![\w&])#[0-9a-fA-F]{3,8}\b/g },
  { name: "rgb/hsl literal", re: /\b(?:rgba?|hsla?)\(/g },
  // Variants like has-[:focus-visible]: and property lists like transition-[width] are fine; values are not.
  { name: "Tailwind arbitrary value", re: /\b(?!transition-)[a-z][a-z0-9-]*-\[[^\]]+\](?!:)/g },
];
let failures = 0;
for (const d of dirs) {
  for (const f of fs.readdirSync(path.join(ROOT, d))) {
    const rel = `${d}/${f}`;
    if (!/\.tsx?$/.test(f) || allow.has(rel)) continue;
    const lines = fs.readFileSync(path.join(ROOT, rel), "utf8").split("\n");
    lines.forEach((line, i) => {
      if (line.trim().startsWith("//") || line.trim().startsWith("*") || line.trim().startsWith("/*")) return;
      for (const r of rules) {
        for (const m of line.matchAll(r.re)) {
          failures++;
          console.log(`${rel}:${i + 1}  ${r.name}: ${m[0]}`);
        }
      }
    });
  }
}
if (failures) { console.log(`\n${failures} raw value(s). Use a token, or add one in tokens/build-tokens.py.`); process.exit(1); }
console.log("No raw values in src/. Every color and size comes from a token.");
