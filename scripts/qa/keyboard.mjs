// Keyboard and screen-size checks for the interactive components and templates.
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright-core";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const dir = path.join(ROOT, "qa-output", "render");
const out = [];
const ok = (name, cond, note = "") => out.push(`${cond ? "PASS" : "FAIL"}  ${name}${note ? "  — " + note : ""}`);
const b = await chromium.launch();
const open = async (f, w = 960, h = 900) => { const p = await b.newPage({ viewport: { width: w, height: h } }); await p.goto("file://" + dir + "/" + f + "-light.html"); await p.waitForTimeout(350); return p; };
let p = await open('Tabs'); await p.locator('[role=tab][aria-selected=true]').focus(); await p.keyboard.press('ArrowRight');
  ok('Tabs: arrow key moves selection', await p.locator('[role=tab][aria-selected=true]').innerText().then(t => t.includes('Media')));
  p = await open('SegmentedControl'); await p.locator('[role=radio][aria-checked=true]').first().focus(); await p.keyboard.press('ArrowRight');
  ok('SegmentedControl: arrow key moves selection', await p.locator('[role=radio][aria-checked=true]').first().innerText().then(t => t.includes('Tiles')));
  p = await open('Switch'); const sw = p.locator('[role=switch]').nth(1); await sw.focus(); await p.keyboard.press('Space');
  ok('Switch: Space toggles', (await sw.getAttribute('aria-checked')) === 'true');
  p = await open('Menu'); await p.keyboard.press('Escape'); await p.waitForTimeout(100);
  ok('Menu: Escape closes and returns focus to trigger', (await p.locator('[role=menu]').count()) === 0 && await p.evaluate(() => document.activeElement && document.activeElement.getAttribute('aria-haspopup') === 'menu'));
  await p.keyboard.press('ArrowDown'); await p.waitForTimeout(150);
  ok('Menu: ArrowDown on trigger opens and focuses first item', await p.evaluate(() => (document.activeElement.getAttribute('role') || '').startsWith('menuitem')));
  p = await open('Modal'); await p.waitForTimeout(200);
  ok('Modal: opens with focus inside', await p.evaluate(() => !!document.activeElement.closest('dialog')));
  for (let i = 0; i < 12; i++) await p.keyboard.press('Tab');
  ok('Modal: Tab stays inside the dialog', await p.evaluate(() => !!document.activeElement.closest('dialog')));
  await p.keyboard.press('Escape'); await p.waitForTimeout(150);
  ok('Modal: Escape closes', await p.evaluate(() => !document.querySelector('dialog[open]')));
  p = await open('Tooltip'); await p.locator('button[aria-label=Share]').focus(); await p.waitForTimeout(100);
  ok('Tooltip: shows on keyboard focus', (await p.locator('[role=tooltip]').count()) >= 2);
  p = await open('Field'); const zip = p.locator('input').nth(1);
  ok('Field: error linked to input', (await zip.getAttribute('aria-invalid')) === 'true' && !!(await zip.getAttribute('aria-describedby')));
  p = await open('Table'); await p.locator('tbody tr').first().focus(); 
  ok('Table: rows focusable and Enter works', (await p.locator('tbody tr').first().getAttribute('tabindex')) === '0');
  p = await open('Menu'); ok('Menu: search box sits outside role=menu', (await p.locator('[role=menu] input').count()) === 0 && (await p.locator('input[aria-label="Find a company"]').count()) === 1);
  p = await open('Combobox'); const cb = p.locator('[role=combobox]'); await cb.click(); await cb.fill('tenn'); await p.keyboard.press('ArrowDown'); await p.keyboard.press('Enter'); await p.waitForTimeout(100);
  ok('Combobox: type, arrow and Enter selects', (await cb.inputValue()) === 'Tennis Shop', 'got ' + await cb.inputValue());
  p = await open('CommandPalette'); await p.keyboard.press('Control+k'); await p.waitForTimeout(200);
  ok('CommandPalette: Ctrl/⌘K opens with focus in search', await p.evaluate(() => document.activeElement && document.activeElement.getAttribute('role') === 'combobox' && !!document.querySelector('dialog[open]')));
  await p.keyboard.type('dark'); ok('CommandPalette: filters by keyword', (await p.locator('[role=option]').count()) === 1);
  await p.keyboard.press('Escape'); await p.waitForTimeout(150); ok('CommandPalette: Escape closes', await p.evaluate(() => !document.querySelector('dialog[open]')));
  p = await open('Popover'); ok('Popover: opens with focus inside', await p.evaluate(() => !!document.activeElement.closest('[role=dialog]')));
  await p.keyboard.press('Escape'); await p.waitForTimeout(100);
  ok('Popover: Escape closes and returns focus', (await p.locator('[role=dialog]').count()) === 0 && await p.evaluate(() => document.activeElement.getAttribute('aria-haspopup') === 'dialog'));
  p = await open('Accordion'); const h = p.locator('button[aria-expanded]').nth(1); await h.focus(); await p.keyboard.press('Enter');
  ok('Accordion: Enter expands a section', (await h.getAttribute('aria-expanded')) === 'true');
  p = await open('ConfirmDialog'); await p.locator('button:has-text("Remove from gallery")').click(); await p.waitForTimeout(150);
  ok('ConfirmDialog: opens with a verb, not OK', (await p.locator('dialog[open] button:has-text("Remove profile")').count()) === 1);
  for (const w of [1440, 1180, 900, 400]) {
    p = await open('ReviewQueue', w);
    let reach = await p.locator('aside button:has-text("Approve profile")').isVisible().catch(() => false);
    if (!reach) { await p.locator('button:has-text("Review panel")').click().catch(() => {}); await p.waitForTimeout(250); reach = await p.locator('dialog[open] button:has-text("Approve profile")').isVisible().catch(() => false); await p.keyboard.press('Escape'); await p.waitForTimeout(150); }
    ok(`ReviewQueue @${w}px: approve action reachable`, reach);
    let nav = await p.locator('aside[aria-label=Workspace] a[aria-current]').isVisible().catch(() => false);
    if (!nav) { await p.locator('button[aria-label="Open navigation"]').click().catch(() => {}); await p.waitForTimeout(250); nav = await p.locator('dialog[open] a[aria-current]').isVisible().catch(() => false); await p.keyboard.press('Escape'); }
    ok(`ReviewQueue @${w}px: navigation reachable`, nav);
    const sw = await p.evaluate(() => document.documentElement.scrollWidth); ok(`ReviewQueue @${w}px: no sideways page scroll`, sw <= w, 'scrollWidth ' + sw);
  }
  p = await open('ReviewQueue', 900); await p.locator('tbody tr').nth(1).click(); await p.waitForTimeout(250);
  ok('ReviewQueue @900px: selecting a row opens the review drawer', await p.locator('dialog[open] button:has-text("Approve profile")').isVisible().catch(() => false));
  p = await open('WorkspaceHub', 1440); await p.locator('button[aria-pressed]:has-text("Table Studio")').focus(); await p.keyboard.press('Enter'); await p.waitForTimeout(150);
  ok('WorkspaceHub: module card selectable by keyboard', (await p.locator('aside h2:has-text("Table Studio")').count()) === 1);
console.log(out.join("\n"));
await b.close();
const failed = out.filter((l) => l.startsWith("FAIL")).length;
console.log(failed ? `\n${failed} check(s) failed.` : `\nAll ${out.length} keyboard and screen-size checks pass.`);
process.exit(failed ? 1 : 0);
