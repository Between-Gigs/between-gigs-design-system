// Validates custom icons (icons/custom/*.svg) against Lucide's drawing rules. See .claude/skills/create-icon.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const DIR = path.join(path.resolve(path.dirname(fileURLToPath(import.meta.url)), ".."), "icons", "custom");
const files = fs.existsSync(DIR) ? fs.readdirSync(DIR).filter((f) => f.endsWith(".svg")) : [];
const SHAPES = new Set(["path", "rect", "circle", "ellipse", "line", "polyline", "polygon"]);
let bad = 0;
for (const f of files) {
  const svg = fs.readFileSync(path.join(DIR, f), "utf8");
  const errs = [];
  const root = (svg.match(/<svg\b[^>]*>/) || [""])[0];
  const want = { viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", "stroke-width": "2", "stroke-linecap": "round", "stroke-linejoin": "round" };
  for (const [k, v] of Object.entries(want)) if (!new RegExp(`\\s${k}="${v}"`).test(root)) errs.push(`root <svg> needs ${k}="${v}"`);
  const tags = [...svg.matchAll(/<([a-zA-Z]+)\b/g)].map((m) => m[1]).filter((t) => t !== "svg");
  for (const t of tags) if (!SHAPES.has(t)) errs.push(`<${t}> is not allowed (only ${[...SHAPES].join(", ")})`);
  if (tags.length > 6) errs.push(`${tags.length} shapes; keep it to 6 or fewer`);
  if (/\b(style|class|transform|fill)="(?!none")/.test(svg.replace(root, ""))) errs.push("no style, class, transform or fill on shapes");
  if (/#[0-9a-f]{3,8}\b|rgb\(/i.test(svg)) errs.push("no colors; use currentColor");
  const nums = [...svg.replace(root, "").matchAll(/-?\d*\.?\d+/g)].map((m) => m[0]);
  if (nums.some((n) => (n.split(".")[1] || "").length > 2)) errs.push("numbers with more than 2 decimals");
  // Absolute coordinates on simple shapes must stay inside the 2..22 live area (1 px tolerance for stroke caps).
  for (const m of svg.matchAll(/\b(x|y|cx|cy|x1|y1|x2|y2)="(-?[\d.]+)"/g)) { const v = +m[2]; if (v < 1 || v > 23) errs.push(`${m[1]}=${v} is outside the 24px grid's padding`); }
  for (const m of svg.matchAll(/\b(width|height)="([\d.]+)"/g)) if (!/<svg/.test(svg.slice(Math.max(0, m.index - 200), m.index).split(">").pop() ?? "") && +m[2] > 20) errs.push(`${m[1]}=${m[2]} exceeds the 20px live area`);
  if (errs.length) { bad++; console.log(`✗ ${f}\n  - ${[...new Set(errs)].join("\n  - ")}`); } else console.log(`✓ ${f}`);
}
if (!files.length) console.log("No custom icons yet (icons/custom/*.svg).");
process.exit(bad ? 1 : 0);
