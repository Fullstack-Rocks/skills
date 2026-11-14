// Smoke run, page screenshots and label lists in one pass over the page list in ux.json:
//   node pages.mjs ux.json OUT [NAME ...]
// For each page it saves OUT/NAME.png and OUT/NAME.txt (the labels the action-name test rates) and prints
// the first 300 characters of the page. It ends with ERRORS [...] and exits 1 when any page logged an error.
// A page in ux.json: { "name": "cart", "path": "#cart", "width": 1440, "height": 900, "steps": [...] }
// path is appended to "base". A step is a CSS selector to click (its last match), {"type": "text"} or {"key": "Enter"}.
import fs from 'node:fs';
import path from 'node:path';
import { launch, open, scan, press } from './lib.mjs';

const [config, out, ...only] = process.argv.slice(2);
const opts = JSON.parse(fs.readFileSync(config, 'utf8'));
const pages = opts.pages.filter((p) => !only.length || only.includes(p.name));
fs.mkdirSync(out, { recursive: true });

async function step(page, s) {
  if (typeof s === 'string') await press(page.locator(s).last(), opts);
  else if (s.type) await page.keyboard.type(s.type, { delay: 10 });
  else if (s.key) await page.keyboard.press(s.key);
  await page.waitForTimeout(150);
}

// The labels a user would rate on this page: inside labelScope, outside labelSkip, not covered, each once.
async function labels(page) {
  const all = await scan(page, opts);
  const inScope = await page.evaluate(({ scope, skip, ids }) => ids.filter((i) => {
    const el = document.querySelector(`[data-ux-i="${i}"]`);
    return el.closest(scope) && !(skip && el.closest(skip));
  }), { scope: opts.labelScope || 'body', skip: opts.labelSkip || '', ids: all.map((c) => c.i) });
  const kept = all.filter((c) => inScope.includes(c.i) && !c.covered).map((c) => c.label);
  return [...new Set(kept)];
}

const browser = await launch(opts);
const errors = [];
for (const p of pages) {
  const { page, errors: logged } = await open(browser, opts.base + (p.path || ''), p.width || 1440, p.height || 900, opts);
  try {
    for (const s of p.steps || []) await step(page, s);
    await page.screenshot({ path: path.join(out, `${p.name}.png`) });
    fs.writeFileSync(path.join(out, `${p.name}.txt`), (await labels(page)).map((l, i) => `${i + 1}. ${l}`).join('\n') + '\n');
    const text = await page.evaluate((scope) => document.querySelector(scope)?.innerText || '', opts.labelScope || 'body');
    console.log(p.name, '|', text.replace(/\s+/g, ' ').slice(0, 300));
  } catch (e) {
    logged.push(`step failed: ${e.message.split('\n')[0]}`);
  }
  errors.push(...logged.map((m) => `${p.name}: ${m}`));
  await page.close();
}
await browser.close();
console.log('ERRORS', errors);
process.exit(errors.length ? 1 : 0);
