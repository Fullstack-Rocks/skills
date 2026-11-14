// Shared by ux.mjs and pages.mjs: open a page the way a new user sees it, and list what can be clicked on it.
// Options come from the record folder's ux.json (all optional):
//   hide       CSS of things no user sees, such as a prototype's own bar; hidden in every screenshot
//   rowName    CSS of the name cell inside a clickable row; a click on the row lands there, as a person's would
//   help       CSS of (?) icons; listed as "(?) <their tooltip>"
//   labelScope CSS of the areas whose labels the action-name test rates (pages.mjs); default body
//   labelSkip  CSS of areas left out of the action-name test, such as the main navigation
//   chrome     path to a Chromium binary, when the Playwright one isn't installed
import { chromium } from 'playwright-core';

const CONTROLS = 'button, a, input, textarea, select, [data-action], [role="tab"], [role="link"], [role="button"]';

export const launch = (opts) => chromium.launch({ executablePath: opts.chrome || process.env.UX_CHROME || undefined });

export async function open(browser, url, width, height, opts) {
  const page = await browser.newPage({ viewport: { width, height } });
  const errors = [];
  page.on('pageerror', (e) => errors.push(e.message));
  page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
  await page.goto(url);
  await page.evaluate(() => document.fonts.ready);
  if (opts.hide) await page.addStyleTag({ content: `${opts.hide}{display:none!important}` });
  await page.waitForTimeout(300);
  return { page, errors };
}

// Every visible control in reading order, tagged data-ux-i so it can be clicked by index afterwards.
// A control is known by its label plus which occurrence of that label it is (nth), so a replay finds it again.
export function scan(page, opts) {
  return page.evaluate(({ sel, help, rowName }) => {
    const shown = (el, r) => r.width && r.height && getComputedStyle(el).visibility !== 'hidden' && !(el.matches('[data-action]') && el.parentElement.closest('button, a'));
    // A (?) icon is named by its tooltip, a dropdown by its label's own words, a row by its name cell.
    const tipOf = (el) => el.getAttribute('title') || el.dataset.tip || el.getAttribute('aria-label') || '';
    const labelText = (el) => el.labels?.[0]?.innerText;
    const textOf = (el) => {
      if (help && el.matches(help)) return `(?) ${tipOf(el)}`;
      if (el.tagName === 'SELECT') return el.getAttribute('aria-label') || (labelText(el) || '').replace(el.innerText, '') || el.name;
      const face = (rowName && el.querySelector(rowName)) || el;
      return [el.getAttribute('aria-label'), face.innerText, el.placeholder, labelText(el), tipOf(el)].find(Boolean);
    };
    const labelOf = (el) => {
      const label = (textOf(el) || '').replace(/\s+/g, ' ').trim().slice(0, 70);
      return label === '(?)' ? '' : label;
    };
    const offScreen = (r) => r.bottom < 0 || r.top > innerHeight || r.right < 0 || r.left > innerWidth;
    // Covered by a sheet, drawer or modal: the point at its centre belongs to something else.
    const coveredAt = (el, r) => {
      const hit = document.elementFromPoint(Math.min(Math.max(r.left + r.width / 2, 0), innerWidth - 1), Math.min(Math.max(r.top + r.height / 2, 0), innerHeight - 1));
      return Boolean(hit && !el.contains(hit) && !hit.contains(el));
    };
    const entry = (el, r, label, nth) => {
      const select = el.tagName === 'SELECT';
      const off = offScreen(r);
      return { label, nth, off, covered: !off && coveredAt(el, r),
        kind: select ? 'select' : el.matches('input, textarea') ? 'field' : 'control',
        options: select ? [...el.options].map((o) => o.label.trim()) : undefined };
    };

    const seen = new Map();
    const out = [];
    for (const el of document.querySelectorAll('[data-ux-i]')) el.removeAttribute('data-ux-i');
    for (const el of document.querySelectorAll(sel)) {
      const r = el.getBoundingClientRect();
      const label = shown(el, r) && labelOf(el);
      if (!label) continue;
      const nth = seen.get(label) ?? 0;
      seen.set(label, nth + 1);
      el.setAttribute('data-ux-i', out.length);
      out.push({ ...entry(el, r, label, nth), i: out.length });
    }
    return out;
  }, { sel: [CONTROLS, opts.help].filter(Boolean).join(', '), help: opts.help, rowName: opts.rowName });
}

// Click an element the way a person would: on its row's name cell when it is a row.
export async function press(locator, opts) {
  const name = opts.rowName ? locator.locator(`:scope ${opts.rowName}`).first() : null;
  await (name && (await name.count()) ? name : locator).click({ timeout: 4000 });
}
