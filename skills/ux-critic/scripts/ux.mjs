// The step browser for task testers. Each command replays the session's earlier actions in a fresh headless
// browser, does one new action, saves a screenshot and prints a numbered list of what can be clicked.
//   node ux.mjs DIR start URL WIDTH HEIGHT [ux.json]
//   node ux.mjs DIR look | click N | type TEXT | key KEY | scroll up|down | select N OPTION
// Clicks are stored by label, so labels must not change while a tester is running.
import fs from 'node:fs';
import path from 'node:path';
import { launch, open, scan, press } from './lib.mjs';

const [dir, cmd, ...rest] = process.argv.slice(2);
const file = path.join(dir, 'session.json');

async function find(page, s, { label, nth }) {
  const hit = (await scan(page, s.opts)).find((c) => c.label === label && c.nth === nth);
  if (!hit) throw new Error(`No control "${label}" (#${nth}) any more`);
  return page.locator(`[data-ux-i="${hit.i}"]`);
}

async function act(page, s, a) {
  if (a.kind === 'click') await press(await find(page, s, a), s.opts);
  if (a.kind === 'select') await (await find(page, s, a)).selectOption({ label: a.option });
  if (a.kind === 'type') await page.keyboard.type(a.text, { delay: 10 });
  if (a.kind === 'key') await page.keyboard.press(a.key);
  if (a.kind === 'scroll') {
    // Scroll where the content is: the middle of the window, not the corner over the navigation.
    const { width, height } = page.viewportSize();
    await page.mouse.move(width / 2, height / 2);
    await page.mouse.wheel(0, a.dir === 'up' ? -600 : 600);
  }
  await page.waitForTimeout(200);
}

async function run(s, extra) {
  const browser = await launch(s.opts);
  const { page } = await open(browser, s.url, s.w, s.h, s.opts);
  for (const a of s.actions) await act(page, s, a);
  if (extra) {
    await act(page, s, extra);
    s.actions.push({ ...extra, at: new Date().toISOString() });
  }
  const shot = path.join(dir, `step-${String(s.actions.length).padStart(2, '0')}.png`);
  await page.screenshot({ path: shot });
  s.list = (await scan(page, s.opts)).filter((c) => !c.covered);
  fs.writeFileSync(file, JSON.stringify(s, null, 1));
  await browser.close();
  console.log(`Step ${s.actions.length}. Screenshot: ${shot}`);
  console.log(s.list.map((c, n) => {
    const kind = c.kind === 'control' ? '' : `[${c.kind}] `;
    const options = c.options ? `: ${c.options.join(' | ')}` : '';
    return `#${n + 1} ${kind}${c.label}${options}${c.off ? ' (out of view)' : ''}`;
  }).join('\n'));
}

function picked(s, n) {
  const c = s.list[Number(n) - 1];
  if (!c) throw new Error(`No #${n} in the last list`);
  return { label: c.label, nth: c.nth };
}

async function main() {
  if (cmd === 'start') {
    const [url, w, h, config] = rest;
    const opts = config ? JSON.parse(fs.readFileSync(config, 'utf8')) : {};
    delete opts.pages;
    fs.mkdirSync(dir, { recursive: true });
    return run({ url, w: Number(w), h: Number(h), opts, actions: [], list: [] });
  }
  const s = JSON.parse(fs.readFileSync(file, 'utf8'));
  if (cmd === 'look') return run(s);
  if (cmd === 'click') return run(s, { kind: 'click', ...picked(s, rest[0]) });
  if (cmd === 'select') return run(s, { kind: 'select', ...picked(s, rest[0]), option: rest.slice(1).join(' ') });
  if (cmd === 'type') return run(s, { kind: 'type', text: rest.join(' ') });
  if (cmd === 'key') return run(s, { kind: 'key', key: rest[0] });
  if (cmd === 'scroll') return run(s, { kind: 'scroll', dir: rest[0] });
  throw new Error(`Unknown command ${cmd}`);
}

main().catch((e) => { console.error(String(e.message || e)); process.exit(1); });
