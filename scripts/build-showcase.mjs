// Assembles docs/showcase: copies the docs bundle, token data, contrast report and fonts next to the page,
// and writes the component index from docs/components/*/README.md. Run after `npm run docs:bundle` and `npm run tokens`.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const OUT = path.join(ROOT, "docs", "showcase");
const cp = (from, to) => fs.copyFileSync(path.join(ROOT, from), path.join(OUT, to));
fs.mkdirSync(path.join(OUT, "fonts"), { recursive: true });
cp("dist/docs-bundle.js", "bundle.js");
cp("dist/docs-bundle.css", "bundle.css");
cp("tokens/tokens.json", "tokens.json");
cp("tokens/contrast-report.json", "pairs.json");
for (const f of fs.readdirSync(path.join(ROOT, "fonts"))) cp(`fonts/${f}`, `fonts/${f}`);

// tokens.css: the theme as plain CSS variables for the static page (light, dark, and any [data-theme] island).
const t = JSON.parse(fs.readFileSync(path.join(ROOT, "tokens/tokens.json"), "utf8"));
const val = (v, th) => {
  const x = typeof v === "string" ? v : v[th] ?? v.light;
  return x.replace(/\{([^}]+)\}/g, "var(--$1)");
};
const colors = [...t.color.tokens, ...t.shadow.tokens];
const vars = (th) => colors.map((c) => `--${c.name}:${val(c.value, th)};`).join("");
const families = Object.keys(t).filter((k) => t[k] && Array.isArray(t[k].tokens) && !["color", "shadow"].includes(k));
const other = families.flatMap((k) => t[k].tokens.map((s) => `--${s.name.replace(".", "\\.")}:${s.value};`)).join("")
  + Object.entries(t.type.families).map(([k, v]) => `--font-${k}:${v};`).join("");
let css = "/* Between Gigs tokens, generated from tokens/tokens.json */\n";
css += t.type.fonts.map((f) => `@font-face{font-family:'${f.family}';src:url(${f.file}) format('woff2');font-weight:${f.weight};font-style:${f.style};font-display:swap}`).join("\n") + "\n";
css += `:root{${vars("light")}${other}color-scheme:light}\n`;
css += `@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){${vars("dark")}color-scheme:dark}}\n`;
css += `[data-theme="dark"]{${vars("dark")}color-scheme:dark}\n[data-theme="light"]{${vars("light")}color-scheme:light}\n`;
fs.writeFileSync(path.join(OUT, "tokens.css"), css);

// Component index for the showcase's detail views.
const docs = path.join(ROOT, "docs", "components");
const comps = [];
for (const name of fs.readdirSync(docs).sort()) {
  const pv = path.join(docs, name, "preview.html"), rd = path.join(docs, name, "README.md");
  if (!fs.existsSync(pv) || !fs.existsSync(rd)) continue;
  const group = (fs.readFileSync(pv, "utf8").split("\n")[0].match(/group="([^"]+)"/) || [])[1] || "";
  const summary = fs.readFileSync(rd, "utf8").split("\n").find((l) => l.trim() && !l.startsWith("#"));
  comps.push({ name, group, summary });
}
fs.writeFileSync(path.join(OUT, "components.json"), JSON.stringify(comps));
console.log(`Showcase assembled: ${comps.length} components, ${JSON.parse(fs.readFileSync(path.join(OUT, "pairs.json"))).length} contrast pairs.`);
