# Orrisvane House — homepage design

An inhabited house, presented as an editorial sequence: arrival, people, rooms, ordinary days, and the care that makes returning possible. Warm paper, precise serif headlines and natural-light photography give way to a personal letter on estuary green.

`design.jpg` is the complete desktop art-direction reference at **1440 × 4239 px**, generated with the built-in image generation tool and proportionally resampled to the requested width. The image establishes composition and photographic intent; this spec supplies the authoritative live copy, colour tokens, estate-plan labels and responsive behaviour. In particular, the week section's generated eyebrow reads “02”; build it as “03” below. Do not implement the screenshot as a page background or extract its text into image assets.

Build static semantic HTML, CSS and minimal JavaScript with no build step. Google Fonts is the only external request source. Use relative assets from `../../clients/estate/assets/`. The house, founders, treatment record and identity are fictional; no third-party branding appears.

## Grid and spacing

- **Desktop, 1024 px and above:** centred 12-column grid; max content width **1280 px**; outer margins **80 px at 1440 px**; gutters **24 px**. At 1440 px, each column is **84.667 px**. On narrower desktops use 48 px outer padding; above 1440 px the content remains 1280 px wide.
- **Tablet, 768–1023 px:** 8 columns, 24 px gutters and 32 px outer padding. Split sections become equal halves where their copy fits; the conservation sequence moves below its introductory copy.
- **Mobile, below 768 px:** 4 columns, 16 px gutters and 24 px outer padding; all content becomes one reading column. Use 16 px padding below 360 px. No sideways galleries or horizontal page scrolling.
- **Spacing scale:** 8, 16, 24, 32, 48, 64, 80, 96, 128, 176 px. The 1 px rules, 2 px focus stroke and 4 px focus offset are optical/accessibility exceptions, not layout tokens.
- Header: 96 px nominal height, with 24 px vertical padding. Hero: 32 px top and 96 px bottom padding. Story sections: normally 96 px top and bottom; adjacent paper sections may share one 96 px gap. On mobile use 64 px section spacing and 24–32 px between image and text. The image is a compressed overview; allow the HTML page to grow to fit the complete copy and accessible leading.
- Heading-to-body gap: 24 px; eyebrow-to-heading: 16 px; paragraph gap: 16 px; text-to-action: 32 px; image-to-caption: 8 px. Practical ledger rows: 16 px vertical padding. Invitation: 96 px vertical padding; footer: 48 px.
- Body measure: max 58ch; introductory and invitation copy: max 44ch. Align copy left. Do not justify text. All surfaces, images and buttons have square corners, with no drop shadows. Flat backgrounds are CSS colours, without a texture overlay.
- Images have reserved intrinsic dimensions to prevent layout shifts. Use `object-fit: cover` only where the subject survives the crop; preserve the whole map with `contain`. Captions remain outside image frames. The hero loads eagerly; below-fold photos use native lazy loading.
- Use content-driven heights throughout. At 320 CSS px, 200% text zoom, 400% page zoom, and text-spacing overrides (1.5 line height, .12em tracking, .16em word spacing, 2em paragraph spacing), no text or controls may clip or overlap.

## Colour

Use precisely these six palette tokens, with no opacity on text or functional controls.

| Token | Hex | Role |
| --- | --- | --- |
| Salt paper | `#F4F1E9` | Main canvas; invitation/footer text; light button and input surfaces |
| Household ink | `#252C2A` | Main reading text, headings, estate-plan labels and functional outlines |
| Estuary | `#243F3A` | Invitation and footer background; primary actions and light-button text |
| Dried clay | `#8A4B38` | Underlined editorial links; field error text and error boundaries |
| Olive grey | `#60665E` | Secondary text, captions, placeholders and disabled labels, on salt paper only |
| Warm stone | `#DDD5C8` | Estate-plan and conservation surfaces; dark-surface secondary text and hover fill |

The following is the **exhaustive allowed text/background pairing list**, including interactive states. Ratios were calculated from the hex values using linearised sRGB relative luminance, `L = .2126R + .7152G + .0722B`, and `(Llighter + .05) / (Ldarker + .05)`, rounded to two decimals. All exceed **4.5:1**, including small text; none depends on the large-text exception.

| Text | Background | Contrast | Where used |
| --- | --- | --- | --- |
| Ink `#252C2A` | Paper `#F4F1E9` | **12.64:1** | Headlines, body, navigation, fields, hover text |
| Olive `#60665E` | Paper `#F4F1E9` | **5.23:1** | Paper captions, placeholders, disabled control labels |
| Clay `#8A4B38` | Paper `#F4F1E9` | **5.92:1** | Editorial links and errors |
| Estuary `#243F3A` | Paper `#F4F1E9` | **10.07:1** | Light action labels and active navigation |
| Ink `#252C2A` | Stone `#DDD5C8` | **9.80:1** | Map, conservation copy/captions, hovered fields |
| Clay `#8A4B38` | Stone `#DDD5C8` | **4.59:1** | Atelier link on conservation panel |
| Estuary `#243F3A` | Stone `#DDD5C8` | **7.81:1** | Hovered light actions and copied-email feedback |
| Paper `#F4F1E9` | Estuary `#243F3A` | **10.07:1** | Invitation/footer copy, outline actions and links |
| Stone `#DDD5C8` | Estuary `#243F3A` | **7.81:1** | Dark-surface support copy and hovered links |

On stone use ink for every secondary caption; olive on stone would be only 4.05:1 and is excluded. Keep all text off photographs. Small labels on the plan must use ink on a solid stone field, not over tinted trees or paths. Decorative foliage uses olive, buildings use ink, the pool uses estuary, and all are backed by stone; meaningful plan shapes must retain at least 3:1 contrast. Distinguish the estate boundary with a dashed ink line and a written label, rather than colour alone.

Functional input borders and light-surface focus indicators use ink against paper or stone (**12.64:1 / 9.80:1**). Dark-surface borders and focus indicators use paper against estuary (**10.07:1**). A 1 px stone rule on paper is decorative only. Ledger rows remain understandable through their labels and spacing without their rules.

## Type

Use the Google Fonts families **Newsreader** (400 normal and 400 italic) and **Source Sans 3** (400 and 500 normal). Load with `display=swap`. Fallbacks: `Georgia, serif` and `"Segoe UI", sans-serif`. Use optical sizing for Newsreader; never synthesize heavier weights. Wordmark artwork is a custom, restrained letterspaced serif arrangement of the invented name, not a real brand reference.

| Role | Family / weight | Desktop size / line height | Mobile size / line height | Letter spacing |
| --- | --- | --- | --- | --- |
| H1 | Newsreader 400 | **84 / 88 px** | **48 / 52 px** | -.02em |
| H2 | Newsreader 400 | **48 / 54 px** | **36 / 42 px** | -.02em |
| H3 / editorial lead | Newsreader 400 | **28 / 36 px** | **26 / 34 px** | -.01em |
| Invitation signature | Newsreader 400 italic | **24 / 32 px** | **24 / 32 px** | 0 |
| Body / ledger values | Source Sans 3 400 | **18 / 28.8 px** | **18 / 28.8 px** | 0 |
| Navigation / action / ledger labels | Source Sans 3 500 | **16 / 24 px** | **16 / 24 px** | 0 |
| Caption / support / footer | Source Sans 3 400 | **14 / 22 px** | **14 / 22 px** | 0 |
| Short uppercase eyebrow | Source Sans 3 500 | **12 / 18 px** | **12 / 18 px** | .16em (1.92 px) |

At tablet widths interpolate H1 to 64 px and H2 to 42 px. Set sizes in rem with a 16 px default root, preserving browser font preferences; the px sizes above describe the default rendering. Do not reduce body copy on mobile. No forced headline line breaks below 768 px. At desktop the hero can break after “house” to read “A house / to return to.”; other headlines wrap naturally. Use one H1, H2 for sections 2–8 and H3 only for subordinate labels that genuinely form headings. Eyebrows are paragraphs, not headings. The footer wordmark is not a heading.

## Sections

### 1. Arrival

**Purpose:** establish the place, its scale and the promise of returning, immediately.

**Layout:** header above a 4/8 split; text occupies columns 1–4 and courtyard photo columns 5–12. Keep the photo about 16:9 with its caption below. Text sits on paper, never across the picture. Header content and exact labels appear under Components.

**Exact copy:**

- Eyebrow: “COASTAL ALENTEJO, PORTUGAL”
- H1: “A house to return to.”
- Body: “A private estate in coastal Alentejo. Three suites. Six guests. By invitation.”
- Underlined link: “The house and grounds”, targeting `#house-and-grounds`.
- Photo caption: “The courtyard, before breakfast.”

**Images:** `hero-courtyard.webp`. Alt: “Three shaded courtyard openings face a timber breakfast table, with terracotta paving and an orchard visible beyond.”

**Mobile:** text, link, photo, caption in that DOM order. Full content width; 4:3 crop with the three openings and table still visible. No viewport-height hero.

### 2. The household

**Purpose:** explain who lives and works here, and why the calendar is limited.

**Layout:** founders' photograph columns 1–6; copy columns 8–12, vertically centred. Use a 3:2 landscape portrait of the two people in their actual workshop setting.

**Exact copy:**

- Eyebrow: “01 / THE HOUSEHOLD”
- H2: “A home, before a guest house.”
- Body: “Iria and Tomé Velorne came here in 2018 to make a home and a conservation workshop. They restored the courtyard buildings around three guest suites. In 2022, they began welcoming introduced guests.”
- Second paragraph: “Eighteen residences each year leave time for the work of the house.”
- Portrait caption: “Iria, architect. Tomé, furniture conservator.”
- Buttons/links: none.

**Images:** `household-portrait.webp`. Alt: “Iria and Tomé stand beside a walnut chair in the conservation workshop, with hand tools hanging on the limewashed wall.” Caption belongs to the figure even if visually aligned beneath the adjacent copy.

**Mobile:** eyebrow and headline, portrait with caption, then body. Use grid placement on desktop while retaining this reading order in HTML. Do not crop out either face or the chair.

### 3. The house and grounds

**Purpose:** show shared and private space, and make arrival and access understandable.

**Layout:** `id="house-and-grounds"`. Full-width heading; suite photograph spans columns 1–7, pool columns 8–12, common image-row height about 320 px. Below, a stone panel holds the plan across 7 columns and practical copy across 5, with 32 px internal padding. Labels and practical copy are ink.

**Exact copy:**

- Eyebrow: “02 / THE HOUSE AND GROUNDS”
- H2: “Room to be together. Room to be quiet.”
- Body: “Three suites open onto the courtyard. The library, gardens and 16-metre pool are yours for the week.”
- Arrival paragraph: “A private inland road leads to the 28-hectare estate near Porto Covo. Return road transfers from Lisbon airport are included.”
- Boundary note: “Coastal access is public and lies outside the estate.”
- Access paragraph: “Tell Iria about mobility or access needs before a proposal is prepared.”
- Plan caption: “Schematic estate plan. Not to scale.”
- Visible plan labels: “Estate boundary”, “Arrival road”, “Courtyard”, “Three suites”, “Library”, “Orchard”, “Gardens”, “16 m pool”.
- Text equivalent below the plan: “The inland arrival road leads to the courtyard and three guest suites. The library sits beside the courtyard; the orchard, gardens and 16-metre pool are within the estate boundary. Public coastal access lies beyond the grounds.”
- Buttons/links: none.

**Images:** `suite-orchard.webp`, alt “A linen-covered bed and walnut chair face open courtyard doors, with olive trees in the orchard beyond.” `pool-orchard.webp`, alt “The rectangular sixteen-metre pool sits beside the orchard, edged by stone paving and low planting.” `estate-plan.svg`, alt “Schematic plan of the estate; a complete text description follows.” The plan is an icon/technical diagram asset, not an interactive map. It is a fictional orientation drawing, not surveyed access evidence. Do not imply a step-free route, private beach or measured distance to the sea; invite discussion of actual needs.

**Mobile:** heading, suite, pool, plan, caption and text equivalent, practical copy. Photos are 3:2; plan stays entirely visible. Essential map information is also readable as HTML so shrinking the illustration loses nothing.

### 4. A week here

**Purpose:** show possibilities within an unscheduled day.

**Layout:** heading above three static four-column figures, in breakfast/library/orchard order. Use a gentle 16 px vertical offset for the middle figure on desktop, without changing reading order. Beneath, main paragraph spans 8 columns and atelier note spans 4.

**Exact copy:**

- Eyebrow: “03 / A WEEK HERE”
- H2: “A week with room around it.”
- Breakfast caption: “Meals, when you would like them.”
- Library caption: “Books in the west room.”
- Orchard caption: “The orchard, in your own time.”
- Body: “Breakfast waits in the courtyard. Beyond the orchard, Tomé is repairing a walnut writing chair. You are welcome to visit the atelier after coffee. Nothing else needs arranging.”
- Note: “An atelier morning is optional. The work on the bench sets the subject.”
- Buttons/links: none.

**Images:** `breakfast-table.webp`, alt “Breakfast is laid for six on a courtyard table with woven linen, ceramic plates, bread and fruit.” `west-room-library.webp`, alt “A reading chair and bookshelves sit beside the west room's open window, looking toward the orchard.” `orchard-walk.webp`, alt “A guest walks between mature orchard trees on an unpaved path in soft afternoon light.”

**Mobile:** headline, three image/caption figures stacked without offsets, body, note. No carousel or invented timetable.

### 5. The work of care

**Purpose:** substantiate the working conservation practice through one readable treatment sequence.

**Layout:** full-bleed stone band, inner 12-column container. Introductory copy and link occupy columns 1–4. Three sequential figures occupy the remaining 8 columns in equal widths, with captions beneath. A plain fictional-record note follows the figures. Preserve viewable original joint detail in all crops.

**Exact copy:**

- Eyebrow: “04 / THE WORK OF CARE”
- H2: “The old marks stay.”
- Body: “One walnut writing chair, recorded through three stages of care. The original joints remain; the repair supports another season of use.”
- Figure 1 caption: “Condition · 04 March 2026 — Movement at the rear joint.”
- Figure 2 caption: “Intervention · 06 March 2026 — The joint secured; original timber retained.”
- Figure 3 caption: “Finished detail · 11 March 2026 — Old surface marks remain visible.”
- Note: “Illustrative treatment record for this fictional house.”
- Underlined link: “Visit the atelier”, targeting the required editorial page `atelier.html`. Give this homepage section `id="the-atelier"` for the header's in-page navigation. The editorial page must exist before shipping this secondary link; never substitute an empty or self-referential destination.

**Images:** `chair-condition.webp`, alt “The walnut writing chair's rear joint has opened slightly, exposing the original timber and worn surface.” `chair-intervention.webp`, alt “Tomé steadies the same walnut chair joint at the bench while securing its original timber.” `chair-finished-detail.webp`, alt “The secured rear joint of the same walnut chair retains its old scratches and darkened surface marks.” The three images must show the same chair, same joint and consistent grain. Their dates are narrative for this fictional example, not an asserted real conservation record.

**Mobile:** copy and link, then the three figure/caption pairs in condition/intervention/finished order, then note. They remain separate images, not a before/after slider. At tablet widths use the full row below the introduction; on mobile use 3:2 crops with the joint prominent.

### 6. Returning

**Purpose:** explain the return privilege and the guest's control over stored belongings and preferences.

**Layout:** belongings photograph columns 1–6; copy columns 7–12. Paper background, approximately 3:2 image, aligned at the top of the headline block.

**Exact copy:**

- Eyebrow: “05 / RETURNING”
- H2: “Your place at the table, next year.”
- Body: “Before your seasonal week is offered elsewhere, you receive a sixty-day first option on its equivalent the following year, with the next year’s price stated.”
- Second paragraph: “Leave a small box of books or belongings with a written inventory, if you wish. You decide which preferences the house keeps, changes or deletes.”
- Buttons/links: none.

**Images:** `returning-books.webp`. Alt: “A small wooden belongings box rests beside well-used books on a library shelf, ready for a returning guest.” Books have unbranded, unreadable spines; no identifiable real publishing marks or personal names.

**Mobile:** eyebrow, headline, image, two paragraphs. The right to return is a first option, not an automatic booking or a guaranteed unchanged price.

### 7. Before an introduction

**Purpose:** provide all practical terms before asking for correspondence.

**Layout:** full-width heading and six-row `dl` ledger on paper. Desktop terms span 3 columns, values 9; fine stone rules and clear 16 px row padding. No accordion: all terms are visible.

**Exact copy:**

- Eyebrow: “06 / BEFORE AN INTRODUCTION”
- H2: “A few things, clearly said.”

| Term | Exact value |
| --- | --- |
| The residence | Seven nights. One party. Three suites. Six guests, including children. |
| The season | Eighteen residences, March–November. Two empty nights between visits. |
| Included | Accommodation, meals, house wines, laundry, housekeeping and return road transfers from Lisbon airport. |
| Quoted separately | Flights, outside excursions and commissioned conservation work. |
| The proposal | One agreed household price, shared in your personal proposal before commitment. |
| An introduction | A referral is welcome. Iria may also invite guests after direct correspondence. A request is neither a booking nor an invitation. |

**Images:** none. **Buttons/links:** none. No prices, availability claims or currency symbols are added.

**Mobile:** each term sits above its value; pairs remain grouped with 8 px between term/value and 24 px between pairs. No table overflow or horizontal scrolling.

### 8. The invitation

**Purpose:** begin a personal conversation with the named host.

**Layout:** estuary background. Left half: small paper-coloured three-opening emblem, eyebrow and heading. Right half: note, signature, paper-filled primary action, selectable email and outlined copy action. On desktop the email and copy button may share a wrapping row; the support line is below. Keep comfortable whitespace around the letter.

**Exact copy:**

- Eyebrow: “07 / THE INVITATION”
- H2: “Tell Iria who will be coming.”
- Note: “Write with your name, preferred season and the number in your party. If someone introduced you to the house, you are welcome to mention them. I will write back so we can begin a conversation.”
- Signature: “Iria Velorne”
- Primary label: “Request an introduction”
- Visible email: “iria@orrisvane.example”
- Secondary button label: “Copy email address”
- Support: “Opens your email app. An introduction request creates neither a booking nor an invitation.”
- Copy success status: “Email address copied.”
- Copy failure status: “Please select and copy iria@orrisvane.example.”

**Images:** `courtyard-emblem.svg`, decorative here, `aria-hidden="true"`. No additional photo or form.

**Action contract:** give this section `id="introduction"`. The main action is an anchor, not a submit button, with `mailto:iria@orrisvane.example?subject=An%20introduction%20to%20Orrisvane%20House&body=Name%3A%20%0APreferred%20season%3A%20%0AParty%20size%3A%20%0AIntroducer%20%28optional%29%3A%20`. The adjacent visible email is a simple mailto link and remains selectable. The `.example` address is a reserved showcase address, not a working destination. Never invent a sent-message confirmation or a reply-time promise.

The copy button uses `navigator.clipboard.writeText` after activation, when available. Announce the success/failure text through a persistent `role="status"` region. On failure leave the visible address selectable. If JavaScript is unavailable, hide the copy button and retain the email; the primary email link still works. Do not turn the homepage into a form or store the suggested details locally.

**Mobile:** emblem, eyebrow, heading, note, signature, full-width main action, email, copy button, support. Buttons can grow taller if labels wrap. Allow the email to wrap with `overflow-wrap: anywhere` at extreme zoom.

### 9. Footer

**Purpose:** repeat the house identity, regional location, contact and utility links consistently.

**Layout:** continuation of the estuary background, separated by a 1 px paper rule. Three flexible columns: identity; location/contact; utility links and showcase attribution. All labels are paper; support copy can be stone. Keep contact in this same DOM position on every page.

**Exact copy:**

- Wordmark: “ORRISVANE HOUSE”
- Tagline: “A house to return to.”
- Location: “Near Porto Covo · Alentejo, Portugal”
- Contact: “iria@orrisvane.example”
- Links: “Privacy”, “Accessibility”
- Attribution: “A fictional house by Maison Lumen.”
- No additional headline or primary button.

**Images:** `orrisvane-wordmark.svg`, rendered in paper. Its accessible name is “Orrisvane House”; the linked image goes to `#top`. The same wordmark appears in ink in the masthead.

**Mobile:** identity, location, email, utility links, attribution stacked, with 24 px group gaps. Preserve 44 px standalone link targets. Privacy and Accessibility link to actual `privacy.html` and `accessibility.html` pages in the finished site; those utility pages are required before shipping, with no empty `href` or dead `#` destinations.

## Components

### Navigation

- Desktop header is opaque paper, in normal flow, with the wordmark left and exactly four links right: **“The House” → `#house-and-grounds`; “Life Here” → `#life-here`; “The Atelier” → `#the-atelier`; “Request an Introduction” → `#introduction`**. Add `id="life-here"` to the week section. Once full editorial pages exist, substitute their real relative page URLs. The header invitation link navigates to the email invitation panel; the filled action there opens email.
- Wordmark home link has an accessible name, “Orrisvane House — home”. Put `id="top"` on the page header. Use a semantic `nav` labelled “Main”. The first focusable item is **“Skip to main content”**, linking to `<main id="main">`; show it on paper at the top when focused. Give main a programmatic focus target with `tabindex="-1"` if needed.
- Default nav: ink on paper. Hover: clay text and visible 1 px underline, 4 px below baseline. Keyboard focus: immediate ink ring plus underline; no waiting for animation. Indicate the current actual page with `aria-current="page"` and underline, never by colour alone. Homepage section anchors do not falsely receive page-current state.
- Below 1024 px use a native `details`/`summary` disclosure labelled **“Menu”**, with four vertically stacked links on paper and 44 px minimum rows. It pushes content down; it is not an overlay or focus trap. Its open label remains “Menu”; the expanded state is exposed natively. Enter/Space operates it and Tab follows the links. Keep all navigation usable without JavaScript.
- Navigation links have no disabled state on this homepage. If a future destination is unavailable, render noninteractive olive-on-paper text with no `href`, plus a visible “Unavailable” note; do not leave a clickable disabled-looking link.

### Buttons

- Main invitation action: paper rectangle, estuary text, 1 px paper border; at least 48 px high, 24 px horizontal padding, 16 px Source Sans 3 medium. Default 0 px radius and no shadow. Hover: stone fill and estuary label. Active: same colours with an inset 2 px estuary rule; no scale or movement.
- Copy action: transparent estuary surface, paper text and 1 px paper border; same minimum size. Hover: stone fill, estuary text. Active: same inset rule as the main action. Maintain its label after copying and use the separate live status text.
- Focus for both: 2 px paper outer ring with 4 px estuary separation; the ring is visible on the surrounding dark panel. On any light surface use an ink outer ring with a paper separation. Focus must not be clipped by a parent.
- Disabled native buttons: paper fill, olive text and olive border, full opacity, no hover change; include `disabled` and a nearby textual reason if applicable. This preserves 5.23:1 label contrast. This homepage's email anchor is never disabled. An unavailable action must become plain explanatory text instead of a nonfunctional anchor.

### Links

- Editorial links: clay on paper or stone, persistently underlined, 1 px underline with 4 px offset. Hover: ink on the same surface and a 2 px underline. Focus: surface-appropriate immediate ring, with underline retained. Light-surface visited links retain clay. Dark-panel/footer links: paper on estuary; hover/visited can use stone on estuary with underline retained. Navigation may reveal its underline only on hover/focus; the invitation link remains underlined at rest.
- Use `arrow-right.svg` only as a decorative inline end mark, 16 × 16 px with `currentColor`, no added accessible name. Do not make arrows independent targets.
- Disabled links follow navigation's noninteractive-text rule. Do not apply opacity or rely only on `pointer-events: none`. Standalone links are at least 44 × 44 px; inline prose links retain their natural text flow and underlines.

### Form fields

The homepage has **no form fields**: the profile specifies direct email. The following field contract is reserved for a later, explicitly commissioned form and must not add a submission flow to this build.

- Salt-paper surface; ink text and 1 px ink border; 48 px minimum height; 16 px inset; 18 px Source Sans 3. Textareas start at 144 px and remain resizable. A permanent visible label sits 8 px above the field; help/error text follows 8 px below. Placeholder is olive on paper and supplements the label.
- Hover: stone fill, ink text and ink border; hide the placeholder while hovered/focused if it would otherwise sit on stone. Focus: paper fill with immediate 2 px ink ring, 4 px offset. Disabled: paper fill, olive text/border, full opacity, native `disabled`, no hover styling, and adjacent reason. Read-only fields remain selectable and focusable, labelled “Read only”.
- Errors: paper fill, clay text/border plus a written “Error:” message, `aria-invalid="true"` and `aria-describedby` connecting help/error text. Never use colour alone. Use real `label`/`for` relationships and appropriate `autocomplete` (`name`, `email`), do not block paste, and label optional introducer details “Introducer (optional)”. Error examples: “Error: Enter your name.” and “Error: Enter a valid email address.” No field data is collected by this homepage.

### Footer

- Same contact order, wordmark and utility links across the site. Hover and focus match dark links above. The wordmark link gets a paper ring around its whole clickable box.
- Disabled footer destinations are noninteractive stone-on-estuary text with “Unavailable”; this is a documented fallback state, not the shipping state. Privacy and Accessibility must work at launch.
- Use `<footer>` and a separately labelled “House information” nav for the two utility links. Do not add social icons, newsletter signup, tracking banners or popups.

## Motion

| Element / trigger | Behaviour | Duration / easing | Reduced motion |
| --- | --- | --- | --- |
| Link hover | Underline thickness/offset and text colour transition; underline remains present on editorial links | 400 ms, `cubic-bezier(.22,1,.36,1)` | Immediate state change |
| Button hover | Paper/stone fill and label colour transition | 400 ms, same easing | Immediate state change |
| Native mobile menu | Standard disclosure open/close; content reflows | Immediate; no animated height | Same |
| Keyboard focus | Visible outline and underline appear | 0 ms | Same |
| Photographs and page content | Still and visible immediately; no scroll-triggered hiding or transforms | None | Same |
| Anchor navigation / scrolling | Native browser jump and native scrolling | None | Same |

Under `prefers-reduced-motion: reduce`, set transitions and animations to `none` and `scroll-behavior: auto`. Keep focus immediate regardless of motion preference. No video, autoplay, image zoom, parallax, scroll interception or loading curtain is needed. The calm comes from layout, not delayed access to content.

## Asset list

Asset team destination: **`examples/maison-lumen/clients/estate/assets/`**. The table describes production assets to make; this handoff creates only `design.jpg` and this spec. Dimensions are export pixel dimensions (SVG entries describe viewBox width × height). Photos are sRGB, without baked text, UI or branding; use honest natural light, walking-height cameras and straight architecture. Obtain permission for represented people and objects in any eventual real production. The technical plan is listed as `icon` to fit the supplied asset-kind vocabulary.

| File name | Kind | Size in px | Format | What it shows |
| --- | --- | --- | --- | --- |
| `orrisvane-wordmark.svg` | logo | 640 × 80 | SVG | Original restrained serif “ORRISVANE HOUSE”; outlined custom lettering; single colour, ink for header and paper for footer via `currentColor`/inline SVG |
| `courtyard-emblem.svg` | monogram | 160 × 120 | SVG | Original three-opening courtyard elevation, simple single-colour architectural strokes; ink or paper via `currentColor` |
| `arrow-right.svg` | icon | 24 × 24 | SVG | Plain line arrow, no word or brand, 1.5 px stroke, `currentColor`; decorative 16 px inline rendering |
| `estate-plan.svg` | icon | 1600 × 800 | SVG | Schematic 28-hectare inland estate: labelled dashed boundary, arrival road, courtyard, three suites, library, orchard, gardens, 16 m pool; public coastline outside diagram; labels at least 32 px in source, readable text equivalent in HTML |
| `hero-courtyard.webp` | photo | 2400 × 1350 | WebP | Limewashed courtyard, three shaded openings, terracotta paving, timber table and orchard beyond; horizontal 16:9 with central 4:3 mobile-safe composition |
| `household-portrait.webp` | photo | 1800 × 1200 | WebP | Iria and Tomé beside a walnut chair in their working conservation atelier; both faces and chair remain visible |
| `suite-orchard.webp` | photo | 1800 × 1200 | WebP | Linen bed, walnut chair and open doors toward the courtyard/orchard; room-height architectural view |
| `pool-orchard.webp` | photo | 1500 × 1000 | WebP | Rectangular 16 m pool, stone paving and orchard; no sea, beach claim or resort spectacle |
| `breakfast-table.webp` | photo | 1200 × 800 | WebP | A courtyard breakfast laid for six with woven linen, bread, fruit and everyday ceramics |
| `west-room-library.webp` | photo | 1200 × 800 | WebP | Reading chair, bookshelves and open west-room window; book spines without real names or logos |
| `orchard-walk.webp` | photo | 1200 × 800 | WebP | One guest walking among mature orchard trees, unpaved path and natural afternoon light |
| `chair-condition.webp` | photo | 1000 × 1250 | WebP | Rear joint of one aged walnut writing chair before repair; open joint and old marks clearly visible |
| `chair-intervention.webp` | photo | 1000 × 1250 | WebP | Same chair, joint, timber grain and viewpoint; conservator's hands securing original timber at the bench |
| `chair-finished-detail.webp` | photo | 1000 × 1250 | WebP | Same joint after treatment, secured but with original scratches and patina; no cosmetic replacement |
| `returning-books.webp` | photo | 1800 × 1200 | WebP | A modest wooden belongings box and well-used unbranded books on the library shelf |

SVG labels must use Source Sans 3 or outlined glyphs; the map's full text equivalent remains live HTML. Use inline decorative SVGs with `aria-hidden="true"`; a wordmark used as the home link needs the link's accessible name. One-colour SVGs should inherit `currentColor` so both palette variants use the same file. No texture asset is required: tactile detail belongs in the photographs.

Generation provenance: built-in imagegen, first generated as a complete original UI mockup, then edited against that image. Final edit prompt: “Edit this complete full-page Orrisvane House homepage. Preserve the ENTIRE current composition, every photograph, ALL sections, color palette, typography, copy, and footer. Make only these refinements: change the small label above 'A week with room around it.' from '02 / A WEEK HERE' to exactly '03 / A WEEK HERE'; ensure work-of-care label is '04 / THE WORK OF CARE'; keep warm paper and green SOLID flat colors with NO added grain or vignette. Output a higher resolution image exactly 1440 pixels wide and approximately 4240 pixels tall, with crisp legible type. Preserve every section and footer uncropped. No real brands or logos. This is a precise correction of the supplied design, not a redesign.” The tool returned 731 × 2152 px; the saved deliverable is proportionally resampled to 1440 px width. Its unresolved generated label and map typography are specified correctly above for the developer and asset team.
