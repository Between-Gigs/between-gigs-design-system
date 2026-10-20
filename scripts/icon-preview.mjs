// Renders a custom icon beside Lucide icons at 16/20/24px on light and dark grounds: qa-output/icon-<name>.png.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright-core";
import * as lucide from "lucide-react";
import * as React from "react";
import { renderToStaticMarkup } from "react-dom/server";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const name = process.argv[2];
if (!name) { console.error("usage: node scripts/icon-preview.mjs <kebab-name>"); process.exit(1); }
const custom = fs.readFileSync(path.join(ROOT, "icons", "custom", `${name}.svg`), "utf8").replace(/\swidth="24"\s+height="24"/, "");
const peers = ["Calendar", "Mail", "Wallet", "Layers", "Star"].map((n) => [n, renderToStaticMarkup(React.createElement(lucide[n]))]);
const sizes = [16, 20, 24];
const row = (ground, ink) => `<div style="background:${ground};color:${ink};padding:20px 24px;display:grid;gap:16px">${sizes.map((s) =>
  `<div style="display:flex;align-items:center;gap:${s}px"><span style="font:11px monospace;opacity:.6;width:32px">${s}px</span>
   <span style="width:${s}px;height:${s}px;display:inline-flex;outline:1px dashed rgba(127,127,127,.35)">${custom.replace("<svg", `<svg width="${s}" height="${s}"`)}</span>
   ${peers.map(([, m]) => m.replace(/width="24" height="24"/, `width="${s}" height="${s}"`)).join("")}</div>`).join("")}</div>`;
const html = `<!doctype html><body style="margin:0;font-family:system-ui">
<div style="padding:10px 24px;font:12px monospace;background:#eef2ee">${name} · then ${peers.map(([n]) => n).join(", ")}</div>
${row("#f5f8f4", "#0e1a13")}${row("#071a11", "#eaf4ee")}</body>`;
const b = await chromium.launch({ executablePath: fs.existsSync("/opt/pw-browsers/chromium") ? "/opt/pw-browsers/chromium" : undefined });
const p = await b.newPage({ viewport: { width: 520, height: 400 }, deviceScaleFactor: 2 });
await p.setContent(html);
fs.mkdirSync(path.join(ROOT, "qa-output"), { recursive: true });
const out = path.join(ROOT, "qa-output", `icon-${name}.png`);
await p.screenshot({ path: out, fullPage: true });
await b.close();
console.log(out);
