"""Builds standalone test pages for every component preview and template, in light and dark,
into qa-output/render/. Needs `npm run docs:bundle` first."""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "qa-output", "render")
t = json.load(open(os.path.join(ROOT, "tokens", "tokens.json")))

def v(x, th):
    if isinstance(x, dict): x = x.get(th, x["light"])
    return re.sub(r"\{([^}]+)\}", lambda m: f"var(--{m.group(1)})", x)

css = ""
for th in ("light", "dark"):
    css += (":root," if th == "light" else "") + f'[data-theme="{th}"]{{' + "".join(f"--{c['name']}:{v(c['value'], th)};" for c in t["color"]["tokens"] + t["shadow"]["tokens"]) + "}"
fams = [k for k in t if isinstance(t[k], dict) and "tokens" in t[k] and k not in ("color", "shadow")]
css += ":root{" + "".join(f"--{s['name'].replace('.', chr(92) + '.')}:{s['value']};" for k in fams for s in t[k]["tokens"])
css += "".join(f"--font-{k}:{val};" for k, val in t["type"]["families"].items()) + "}"
css += "".join(f"@font-face{{font-family:'{f['family']}';src:url(file://{ROOT}/{f['file']});font-weight:{f['weight']};font-style:{f['style']}}}" for f in t["type"]["fonts"])
read = lambda p: open(os.path.join(ROOT, p)).read()
react, rdom = read("node_modules/react/umd/react.production.min.js"), read("node_modules/react-dom/umd/react-dom.production.min.js")
bcss, bjs = read("dist/docs-bundle.css"), read("dist/docs-bundle.js")
import shutil
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT, exist_ok=True)
n = 0
docs = os.path.join(ROOT, "docs", "components")
for name in sorted(os.listdir(docs)):
    p = os.path.join(docs, name, "preview.html")
    if not os.path.exists(p): continue
    first = open(p).read().splitlines()[0]
    wide = 'width=1440' in first
    body = open(p).read().split("<body>")[1].split("</body>")[0]
    for th in ("light", "dark"):
        doc = (f'<!doctype html><html lang="en" data-theme="{th}" data-wide="{int(wide)}"><head><meta charset="utf-8"><title>{name} ({th})</title>'
               f'<style>{css}</style><style>{bcss}</style><script>{react}</script><script>{rdom}</script><script>{bjs}</script></head><body>{body}</body></html>')
        open(os.path.join(OUT, f"{name}-{th}.html"), "w").write(doc); n += 1
print(f"{n} test pages in qa-output/render/")
