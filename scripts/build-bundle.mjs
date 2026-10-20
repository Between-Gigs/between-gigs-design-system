import * as esbuild from "esbuild";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

// Builds the docs bundle: every component as one classic script (window.BetweenGigs),
// used by the component previews and the showcase. Apps import from src/ instead.
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const OUT = path.resolve(process.argv[2] ?? path.join(ROOT, "dist", "docs-bundle.js"));
fs.mkdirSync(path.dirname(OUT), { recursive: true });
const shim = {
  name: "globals",
  setup(b) {
    b.onResolve({ filter: /^react(-dom)?(\/.*)?$/ }, (a) => ({ path: a.path, namespace: "g" }));
    b.onLoad({ filter: /.*/, namespace: "g" }, (a) => ({
      contents: a.path.startsWith("react-dom") ? "module.exports = window.ReactDOM" :
        a.path === "react/jsx-runtime" ? "const R = window.React; module.exports = { jsx: (t,p,k)=>R.createElement(t,{...p,key:k}), jsxs: (t,p,k)=>R.createElement(t,{...p,key:k}), Fragment: R.Fragment }" :
        "module.exports = window.React",
      loader: "js",
    }));
  },
};
const r = await esbuild.build({
  entryPoints: [path.join(ROOT, "scripts", "bundle-entry.ts")], bundle: true, format: "iife", globalName: "BetweenGigs", write: false,
  jsx: "transform", jsxFactory: "React.createElement", jsxFragment: "React.Fragment",
  target: "es2019", minify: true, legalComments: "none", plugins: [shim],
  tsconfigRaw: { compilerOptions: { jsx: "react" } }, metafile: true,
});
let js = r.outputFiles[0].text;
const skip = new Set(["cx", "statusMeta", "useToast", "Icons", "html", "buttonVariants", "buttonSizes", "controlFrame", "initials", "CardHeader", "StatRow", "ToastProvider", "TabList", "Tab", "TabPanel", "NavSection", "TopBar", "ToolbarDivider", "ModuleBar", "Sidebar", "Inspector", "InspectorSection", "PromptBar", "FilterLabel", "stepTypes", "useAppShell", "ShellMenuButton", "ShellInspectorButton", "useCommandShortcut", "useTheme", "FoundingCardGlyph"]);
const names = Object.keys(r.metafile.outputs[Object.keys(r.metafile.outputs)[0]].exports ?? {});
const src = fs.readFileSync(path.join(ROOT, "src", "components", "index.ts"), "utf8");
const comps = [...src.matchAll(/export \{ ([^}]+) \}/g)].flatMap((m) => m[1].split(",").map((s) => s.trim()))
  .filter((n) => n && !n.startsWith("type ") && !skip.has(n));
if (/<\/script|<!--/i.test(js)) { js = js.replace(/<\/script/gi, "<\\/script").replace(/<!--/g, "\\x3C!--"); }
const header = `/* @ds-bundle: ${JSON.stringify({ format: 4, namespace: "BetweenGigs", components: comps.map((name) => ({ name })) })} */\n`;
js = js.replace(/^var BetweenGigs=/, "window.BetweenGigs=");
fs.writeFileSync(OUT, header + js);
console.log("bundle", (js.length / 1024).toFixed(1) + "KB", comps.length, "components", /<\/script|<!--/i.test(js) ? "UNSAFE" : "safe");
