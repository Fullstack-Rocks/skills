// Maison Talvrenne — progressive enhancement only. Without this file the
// page still navigates, the disclosures open natively and the request form
// shows inline with its preview disabled. The CSS collapses the menu and
// hides the inline form only once the last line below adds `js-ready`.

// Mobile menu: collapsed behind a button only when this script runs.
const menuToggle = document.querySelector('.menu-toggle');
const navList = document.getElementById('nav-list');

function setMenu(open) {
  menuToggle.setAttribute('aria-expanded', String(open));
  menuToggle.textContent = open ? 'Close menu' : 'Menu';
  navList.classList.toggle('is-open', open);
}

menuToggle.addEventListener('click', () => {
  setMenu(menuToggle.getAttribute('aria-expanded') !== 'true');
});

navList.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && navList.classList.contains('is-open')) {
    setMenu(false);
    menuToggle.focus();
  }
});
menuToggle.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') setMenu(false);
});

// Section links: mark the current section and move focus to its heading.
const headerLinks = [...navList.querySelectorAll('a')];

function markCurrent(hash) {
  for (const link of headerLinks) {
    if (link.hash === hash) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
}

for (const link of document.querySelectorAll('.nav-list a, .footer-nav a')) {
  link.addEventListener('click', (event) => {
    const section = document.querySelector(link.hash);
    const heading = section && section.querySelector('h1, h2');
    if (!heading) return;
    event.preventDefault();
    setMenu(false);
    history.pushState(null, '', link.hash);
    markCurrent(link.hash);
    section.scrollIntoView();
    heading.focus({ preventScroll: true });
  });
}
markCurrent(location.hash);

// Back and Forward return to the section the URL names.
window.addEventListener('popstate', () => {
  const hash = location.hash;
  const target = hash && document.getElementById(decodeURIComponent(hash.slice(1)));
  markCurrent(hash);
  if (!target) {
    window.scrollTo(0, 0);
    return;
  }
  const details = target.closest('details');
  if (details) details.open = true;
  const focusable = target.matches('h1, h2, h3, summary') ? target : target.querySelector('h1, h2');
  (focusable || target).scrollIntoView();
  if (focusable) focusable.focus({ preventScroll: true });
});

// Scrolling marks the header link whose section crosses the middle of the viewport.
const sectionObserver = new IntersectionObserver((entries) => {
  for (const entry of entries) {
    const hash = '#' + entry.target.id;
    if (entry.isIntersecting) markCurrent(hash);
    else if (headerLinks.some((link) => link.hash === hash && link.hasAttribute('aria-current'))) markCurrent('');
  }
}, { rootMargin: '-50% 0px -50% 0px' });
for (const link of headerLinks) sectionObserver.observe(document.querySelector(link.hash));

// Finishing links open the sample dossier and focus its summary.
const dossierSummary = document.getElementById('sample-dossier');

for (const link of document.querySelectorAll('.dossier-link')) {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    dossierSummary.parentElement.open = true;
    const target = document.getElementById(link.dataset.target);
    history.pushState(null, '', '#sample-dossier');
    target.scrollIntoView();
    target.focus({ preventScroll: true });
  });
}

// Appointment request dialog.
const dialog = document.getElementById('request');
const form = dialog.querySelector('.request-form');
const preview = dialog.querySelector('.preview');
const status = dialog.querySelector('.status');
const heading = document.getElementById('request-title');
const previewButton = form.querySelector('[type="submit"]');
let opener = null;

dialog.close();
previewButton.disabled = false;

for (const trigger of document.querySelectorAll('.request-trigger')) {
  trigger.addEventListener('click', () => {
    opener = trigger;
    dialog.showModal();
    heading.focus();
  });
}

for (const button of dialog.querySelectorAll('.close-request')) {
  button.addEventListener('click', () => dialog.close());
}

dialog.addEventListener('close', () => {
  form.reset();
  clearErrors();
  status.textContent = '';
  form.hidden = false;
  preview.hidden = true;
  if (opener) opener.focus();
  opener = null;
});

const checks = [
  {
    controls: [form.elements.name],
    error: document.getElementById('req-name-error'),
    message: 'Enter your name.',
    valid: () => form.elements.name.value.trim() !== '',
  },
  {
    controls: [form.elements.email],
    error: document.getElementById('req-email-error'),
    message: 'Enter a valid email address.',
    valid: () => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.elements.email.value.trim()),
  },
  {
    controls: [...form.querySelectorAll('[name="format"]')],
    error: document.getElementById('req-format-error'),
    message: 'Choose an appointment format.',
    valid: () => form.elements.format.value !== '',
  },
];

function clearErrors() {
  for (const check of checks) {
    check.error.hidden = true;
    check.error.textContent = '';
    for (const control of check.controls) control.removeAttribute('aria-invalid');
  }
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  clearErrors();
  const failed = checks.filter((check) => !check.valid());

  if (failed.length) {
    for (const check of failed) {
      check.error.textContent = check.message;
      check.error.hidden = false;
      for (const control of check.controls) control.setAttribute('aria-invalid', 'true');
    }
    status.textContent = 'Please check the marked fields.';
    failed[0].controls[0].focus();
    return;
  }

  // User content goes in as text, never HTML.
  for (const field of preview.querySelectorAll('[data-preview]')) {
    field.textContent = form.elements[field.dataset.preview].value.trim() || '—';
  }
  form.hidden = true;
  preview.hidden = false;
  status.textContent = 'Preview ready. This demonstration has not sent your request.';
  preview.querySelector('.edit-request').focus();
});

preview.querySelector('.edit-request').addEventListener('click', () => {
  preview.hidden = true;
  form.hidden = false;
  status.textContent = '';
  form.elements.name.focus();
});

document.documentElement.classList.add('js-ready');
