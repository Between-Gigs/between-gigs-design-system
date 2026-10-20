// Runs axe-core on every rendered preview and template. Page-level rules that only apply to whole
// documents (title, lang, main landmark, h1) are skipped: each preview is a fragment of a real page.
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright-core";

const require = createRequire(import.meta.url);
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const DIR = path.join(ROOT, "qa-output", "render");
const axe = fs.readFileSync(require.resolve("axe-core/axe.min.js"), "utf8");
const SKIP = ["document-title", "html-has-lang", "landmark-one-main", "page-has-heading-one", "region"];

const browser = await chromium.launch();
const agg = {};
let renderErrors = 0;
for (const f of fs.readdirSync(DIR).filter((x) => x.endsWith(".html"))) {
  const html = fs.readFileSync(path.join(DIR, f), "utf8");
  const wide = html.includes('data-wide="1"');
  const page = await browser.newPage({ viewport: { width: wide ? 1440 : 960, height: 900 } });
  const errs = [];
  page.on("pageerror", (e) => errs.push(e.message));
  await page.goto("file://" + path.join(DIR, f));
  await page.waitForTimeout(300);
  // Audit the settled page: wait for entrance transitions (scroll reveals, page transitions) to finish.
  await page.waitForFunction(() => document.getAnimations().every((a) => a.playState !== "running" || a.effect?.getTiming().iterations === Infinity), null, { timeout: 4000 }).catch(() => {});
  if (errs.length) { renderErrors++; console.log(`RENDER ERROR ${f}: ${errs[0]}`); }
  await page.addScriptTag({ content: axe });
  const res = await page.evaluate(async (skip) => {
    const r = await window.axe.run(document, { resultTypes: ["violations"] });
    return r.violations.filter((v) => !skip.includes(v.id)).map((v) => ({ id: v.id, impact: v.impact, help: v.help, n: v.nodes.length, sample: v.nodes[0].target.join(" ") }));
  }, SKIP);
  for (const v of res) { (agg[v.id] ??= { ...v, pages: [] }).pages.push(f.replace(".html", "")); }
  await page.close();
}
await browser.close();
const ids = Object.keys(agg);
for (const id of ids) console.log(`[${agg[id].impact}] ${id}: ${agg[id].help}\n  on ${agg[id].pages.join(", ")}\n  e.g. ${agg[id].sample}`);
console.log(ids.length || renderErrors ? `\n${ids.length} accessibility rule(s) failing, ${renderErrors} render error(s).` : "axe: no violations, no render errors.");
process.exit(ids.length || renderErrors ? 1 : 0);
