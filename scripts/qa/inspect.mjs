// Detail inspection: finds the small defects screenshots miss, on every component preview (both themes)
// and on the showcase page, at desktop and phone width:
//   - double focus rings (an element and its frame both outlined) and focus with no visible indicator
//   - native <option> lists with no colors of their own (the OS paints them, often unreadable in dark)
//   - click targets under 24×24px (WCAG 2.5.8)
//   - text clipped by its container
import fs from "node:fs";
import http from "node:http";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright-core";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const RENDER = path.join(ROOT, "qa-output", "render");
const SHOWCASE = path.join(ROOT, "docs", "showcase");

// Serve the showcase locally (it fetches its JSON) with React from node_modules.
const types = { ".js": "text/javascript; charset=utf-8", ".css": "text/css", ".json": "application/json", ".woff2": "font/woff2", ".html": "text/html; charset=utf-8" };
const srv = http.createServer((q, r) => {
  const url = decodeURIComponent(q.url.split("?")[0]);
  if (url === "/__page.html") {
    const html = fs.readFileSync(path.join(SHOWCASE, "index.html"), "utf8")
      .replace(/https:\/\/cdnjs\.cloudflare\.com\/ajax\/libs\/react\/[^"]+/, "/__react.js")
      .replace(/https:\/\/cdnjs\.cloudflare\.com\/ajax\/libs\/react-dom\/[^"]+/, "/__react-dom.js");
    r.writeHead(200, { "content-type": types[".html"] }); r.end(`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>${html}</body></html>`); return;
  }
  const f = url === "/__react.js" ? path.join(ROOT, "node_modules/react/umd/react.production.min.js")
    : url === "/__react-dom.js" ? path.join(ROOT, "node_modules/react-dom/umd/react-dom.production.min.js")
    : path.join(SHOWCASE, url);
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { "content-type": types[path.extname(f)] || "text/plain" }); r.end(d); });
}).listen(0);
const showcaseUrl = `http://localhost:${srv.address().port}/__page.html`;

const staticChecks = () => {
  const out = [];
  const desc = (el) => (el.getAttribute("aria-label") || el.textContent || el.tagName).trim().replace(/\s+/g, " ").slice(0, 40);
  for (const el of document.querySelectorAll("button, a[href], input, select, textarea, [role=switch], [role=tab], [role=radio]")) {
    const r = el.getBoundingClientRect(); if (!r.width || !r.height || getComputedStyle(el).visibility === "hidden") continue;
    if (["checkbox", "radio", "range"].includes(el.type)) continue; // their labels enlarge the target
    if (el.closest("p, li") && el.tagName === "A" && el.closest("p")) continue; // inline links in sentences are exempt
    if (r.width < 24 || r.height < 24) out.push(`small target: ${desc(el)} ${Math.round(r.width)}×${Math.round(r.height)}`);
  }
  for (const el of document.querySelectorAll("body *")) {
    if (el.closest(".sr-only") || ![...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())) continue;
    const cs = getComputedStyle(el);
    if (cs.overflowX === "visible" || cs.overflowX === "auto" || cs.overflowX === "scroll" || cs.textOverflow === "ellipsis") continue;
    if (el.scrollWidth > el.clientWidth + 1) out.push(`clipped text: ${desc(el)}`);
  }
  for (const s of document.querySelectorAll("select")) {
    const o = s.querySelector("option");
    if (o && getComputedStyle(o).backgroundColor === "rgba(0, 0, 0, 0)") out.push(`native options without colors: ${desc(s.closest("div") || s)}`);
  }
  return out;
};
const focusCheck = () => {
  const el = document.activeElement; if (!el || el === document.body) return null;
  if (el.closest("dialog") && !el.closest("dialog[open]")) return null;
  const has = (e) => { const cs = getComputedStyle(e); return cs.outlineStyle !== "none" && parseFloat(cs.outlineWidth) > 0; };
  let anc = false; for (let a = el.parentElement, d = 0; a && d < 3; a = a.parentElement, d++) if (has(a)) { anc = true; break; }
  const r = el.getBoundingClientRect();
  return { key: el.tagName + (el.getAttribute("aria-label") || "") + (el.textContent || "").trim().slice(0, 20) + Math.round(r.top) + Math.round(r.left),
    desc: (el.getAttribute("aria-label") || el.textContent || el.tagName).trim().replace(/\s+/g, " ").slice(0, 40), self: has(el), anc,
    // range inputs with the `range` utility draw focus as a ring on the thumb pseudo-element
    shadow: getComputedStyle(el).boxShadow !== "none" || (el.type === "range" && el.classList.contains("range")) };
};

const browser = await chromium.launch();
async function inspect(url, label, widths) {
  const found = new Set();
  for (const width of widths) {
    const p = await browser.newPage({ viewport: { width, height: 900 } });
    await p.goto(url); await p.waitForTimeout(url.startsWith("http") ? 1200 : 300);
    (await p.evaluate(staticChecks)).forEach((x) => found.add(x));
    const seen = new Set(); let repeats = 0;
    for (let i = 0; i < 300 && repeats < 25; i++) {
      await p.keyboard.press("Tab");
      const r = await p.evaluate(focusCheck);
      if (!r) continue;
      if (seen.has(r.key)) { repeats++; continue; }
      seen.add(r.key);
      if (r.self && r.anc) found.add(`double focus ring: ${r.desc}`);
      if (!r.self && !r.anc && !r.shadow) found.add(`no visible focus: ${r.desc}`);
    }
    await p.close();
  }
  return found.size ? `== ${label}\n${[...found].join("\n")}` : null;
}

const reports = [];
for (const f of fs.readdirSync(RENDER).filter((x) => x.endsWith(".html")).sort()) {
  const wide = fs.readFileSync(path.join(RENDER, f), "utf8").includes('data-wide="1"');
  const r = await inspect("file://" + path.join(RENDER, f), f, wide ? [1440, 400] : [960]);
  if (r) reports.push(r);
}
const sc = await inspect(showcaseUrl, "showcase", [1440, 400]);
if (sc) reports.push(sc);
await browser.close(); srv.close();
console.log(reports.length ? reports.join("\n") + `\n\n${reports.length} page(s) with findings.` : "inspect: no double or missing focus rings, unstyled options, small targets or clipped text.");
process.exit(reports.length ? 1 : 0);
