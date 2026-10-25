# Veyravel — homepage design

**Design idea: the journey and the fitting table.** A graphite showroom opens onto the car in the Jura; chalk workshop chapters then show the luggage, personal fitting and serviceable parts that make its touring proposition tangible. Newsreader carries the invitation, while Manrope carries the practical detail.

Read with `design.jpg`, a complete **1440 × 4366 px** desktop concept image. The image is an art-direction reference, not a production page asset: build all copy as selectable HTML, using the exact copy and font metrics below. Content determines the implemented page height; never compress text or fix section heights to reproduce the overview's height. This specification resolves the raster mockup's approximations of type and spacing.

Sources: `../../BRIEF.md`, `profile.md`, `../../research/design-guidelines.md` and `../../research/accessibility.md`. The house, people and vehicle are fictional. Development targets and proposed ownership commitments must retain their qualifications.

## Grid and spacing

- Desktop, **1024 px and above**: twelve equal columns; **24 px** gutters; content width `min(100% - 160px, 1280px)`. At 1440 px this gives **80 px outer margins**, 1280 px content and **84.67 px columns**. On narrower desktop screens, interpolate outer margins from 32 px at 1024 to 80 px at 1440. Above 1440, centre the 1280 px content.
- Tablet, **768–1023 px**: eight columns, 24 px gutters, 32 px outer margins. Two-column stories use 4 + 4 columns; captions and ledgers remain with their associated content.
- Mobile, **320–767 px**: four columns, 16 px gutters, 24 px outer margins; primary content spans all four. At 320 px the content width is 272 px. All stories become a single reading column.
- Use the spacing scale **8, 16, 24, 32, 48, 64, 96, 128, 176 px**. Border widths of 1 px, focus-ring widths of 2 px, and 4 px ring offsets are optical exceptions rather than spacing tokens.
- Desktop story sections: 96 px top/bottom padding, increasing to 128 px around the invitation. Mobile: 64 px top/bottom. Eyebrow to headline: 16 px; headline to body: 24 px; body to action or ledger: 32 px; image to caption: 8 px; stacked story elements: 32 px. Materials images have a 24 px gap.
- Header: 96 px minimum height, normal document flow, solid graphite. Mobile header has 24 px vertical padding and grows to fit its content. Never overlay the photograph or conceal focused content behind sticky chrome.
- Arrival image is the sole full-bleed plate: 1440 × 480 px display at the reference width, `aspect-ratio: 3 / 1`. Other image ratios are listed below. No fixed text-box heights; `min-width: 0` on grid children; use `overflow-wrap: anywhere` for contact strings.
- Square edges throughout: 0 px border radius. Flat surfaces, no card shadows. Use 1 px rules only where they clarify a ledger or component boundary. Never fade functional rules with opacity.
- Reading measure: body max 55 characters, introductory copy max 62 characters; section headings max 20–26 characters per line. Maintain document order when stacking; do not use CSS ordering to create a different reading sequence.

## Colour

Use precisely these five solid tokens. Photographic material colours are not UI tokens. Do not sample a photograph for a text background, apply opacity to text, or place copy on photography.

| Token | Hex | Role |
| --- | --- | --- |
| Graphite | `#171B1D` | Showroom sections, navigation and footer; all primary text on chalk; light-theme button ink and borders |
| Chalk | `#F1EEE7` | Workshop sections; all primary text on graphite; dark-theme button ink or fill |
| Mineral silver | `#AFB8B9` | Secondary text, captions, ledgers and functional rules on graphite only |
| Fired clay | `#80543F` | Underlined links, eyebrows, field borders/errors and focus rings on chalk only |
| Pale brass | `#D7B98E` | Focus rings and hovered links on graphite only; below 5% of page area |

**Exhaustive permitted text/background combinations, including hover, focus, error and disabled states:**

| Text | Background | Contrast | Used for | WCAG 2.2 AA normal text |
| --- | --- | --- | --- | --- |
| Chalk `#F1EEE7` | Graphite `#171B1D` | **14.97:1** | Dark-section headings/body, nav, default dark links, outline-button labels | Pass |
| Mineral silver `#AFB8B9` | Graphite `#171B1D` | **8.57:1** | Dark captions/helpers, secondary navigation, disabled text | Pass |
| Pale brass `#D7B98E` | Graphite `#171B1D` | **9.27:1** | Dark links on hover | Pass |
| Graphite `#171B1D` | Chalk `#F1EEE7` | **14.97:1** | Light headings/body, labels, filled dark-theme buttons, outline light-theme buttons | Pass |
| Fired clay `#80543F` | Chalk `#F1EEE7` | **5.56:1** | Light links/eyebrows/errors/helpers and disabled text | Pass |

Ratios calculated from the exact sRGB values using WCAG relative luminance and `(Llighter + 0.05) / (Ldarker + 0.05)`, rounded to two decimals. All pairs exceed 4.5:1 even for the smallest specified type; body copy always uses the 14.97:1 primary pairing. Reverse primary colours for button hover fills; this introduces no additional pair.

Functional non-text contrast: silver rules on graphite **8.57:1**; graphite borders/diagram on chalk **14.97:1**; clay borders/focus on chalk **5.56:1**; brass focus on graphite **9.27:1**. Diagram strokes have a 1 px minimum rendered width. Use a 2 px outer focus ring, separated from the component by a 4 px gap in the local section background: brass on graphite, clay on chalk. The gap keeps the ring distinct from either button fill. In forced-colours mode use the system `Highlight` outline.

Never use silver or brass as text on chalk, or clay as text on graphite. Selection uses chalk on graphite within light sections and graphite on chalk within dark sections. Do not introduce unlisted hover colours or semitransparent fills.

## Type

Google Fonts: **Newsreader 400**, normal, for editorial headings and large specification values; **Manrope 400/500**, normal, for everything functional. Load only these weights with `display=swap`; Newsreader uses optical sizing. Fallbacks: `Georgia, serif` and `Arial, sans-serif`, respectively. Keep the root at the user's browser default; the px below are design values at a 16 px root and must be implemented in rem. No weight below 400 or synthetic bold.

| Role | Family / weight | Desktop size / line-height | Mobile size / line-height | Letter spacing |
| --- | --- | --- | --- | --- |
| H1 | Newsreader 400 | 80 / 84 px | 40 / 44 px | -0.02em |
| H2 | Newsreader 400 | 48 / 52.8 px | 32 / 38.4 px | -0.02em |
| H3 / appointment office | Manrope 500 | 20 / 28 px | 20 / 28 px | 0 |
| Large figures | Newsreader 400 | 48 / 52.8 px | 32 / 38.4 px | -0.02em |
| Body and lead | Manrope 400 | 18 / 28.8 px | 18 / 28.8 px | 0 |
| Navigation, buttons, field labels | Manrope 500 | 16 / 24 px | 16 / 24 px | 0 |
| Captions, helpers, legal, ledger labels | Manrope 400 | 16 / 25.6 px | 16 / 25.6 px | 0 |
| Eyebrows / chapter labels | Manrope 500 | 14 / 21 px | 14 / 21 px | +0.14em |

Use fluid heading sizes between mobile and desktop, capped at the endpoints. At 320 px permit normal word wrapping; the H1 can reduce to 36 / 40 px if needed without shrinking body copy. Uppercase only the eyebrows and wordmark, not buttons. Use tabular lining numerals for every measurement. No forced `<br>` in body text; desktop art-directed headline wraps are optional and must disappear on mobile. The mockup's fitted logotype is supplied as artwork, not a third web font.

## Sections

The eight numbered stories below are the complete main-content order. The unnumbered arrival is followed by editorial chapter labels 01–07; these labels do not replace semantic headings. `main#main` contains one H1 and seven H2s. Set `lang="en"` and page title **“Veyravel 01 — Made for the distance between places.”**

### 1. Arrival — `#arrival`

**Purpose:** introduce the house and its single car, with a plain account of what is offered and one invitation.

**Layout:** graphite. Above the photograph, H1 spans columns 1–7; description/action spans columns 9–12. Both sit on the solid background. The house wordmark appears in the navigation. After the text row, leave 48 px then show the full-width 3:1 profile plate.

**Exact copy:**

- Eyebrow: **THE VEYRAVEL 01**
- H1: **Made for the distance between places.**
- Description: **An electric grand tourer. Two seats. Up to 180 commissions a year.**
- Button: **Request a private appointment**
- Helper beneath button: **Demonstration email draft**

**Image:** `hero-profile.webp`. Original graphite two-seat fastback, full side profile, both wheels visible, on wet tarmac beside pale limestone in overcast Jura daylight. No badges, text or familiar manufacturer styling. Alt: **“Graphite Veyravel 01 in side profile beside a limestone wall, with wet Jura roads and cliffs beyond.”**

**Mobile:** headline, description, action, helper, then image. Use the separate 4:3 `hero-profile-mobile.webp` crop to keep the complete car visible; do not crop the wheels. The action may wrap to two lines and must grow vertically.

### 2. The touring proposition — `#touring`

**Purpose:** show the utility of the two-person touring package through an actual loaded compartment.

**Layout:** chalk. Loaded-car photograph columns 1–7, 4:3 ratio. Text/ledger columns 8–12. Use a semantic `dl` with three individually ruled rows; values and labels stay in the same row until space requires a wrap.

**Exact copy:**

- Eyebrow: **01 / THE JOURNEY**
- H2: **Two seats. A week’s luggage. Your own measure.**
- Body: **Two fitted cases and two weekend bags sit behind the seats. The 01 is shaped for the journeys you make together, with room for what you take.**
- Ledger: **4.78 m — Length**; **1.89 m — Width, excluding mirrors**; **360 L — Luggage capacity**.
- Buttons: none.

**Image:** `touring-luggage.webp`. Camera at the open rear hatch, both seats beyond the luggage; exactly two fitted cases and two soft weekend bags, plausible compartment depth. Alt: **“Open rear hatch showing two fitted cases and two weekend bags arranged behind the 01’s two seats.”**

**Mobile:** text and ledger first, image below. Match this reading order in the HTML and position the image left on desktop using named grid areas. No horizontal specification table.

### 3. Fit — `#fit`

**Purpose:** make the fitting process personal and specific.

**Layout:** graphite. Text columns 1–5; column 6 empty; portrait columns 7–12. Use a 4:5 portrait in the implementation, with attention on the maker's face, hands, wool seat and adjustment mechanism. The overview shows a tighter crop of this scene.

**Exact copy:**

- Eyebrow: **02 / PERSONAL FIT**
- H2: **Your first appointment begins in the seat.**
- Body: **We adjust its support, place your luggage behind you and take the 01 onto the roads above the atelier. The fitting record grows from the way you intend to travel.**
- Detail: **Seat support · Steering reach · Pedal position**
- Caption: **At the fitting atelier**
- Buttons: none.

**Image:** `fitting-portrait.webp`. A fictional maker kneels beside the open driver door adjusting seat support. Show tactile wool upholstery, reach-adjustable steering and physical controls. Alt: **“A maker adjusts the wool driver’s seat support beside the open door, with steering wheel and physical controls visible.”**

**Mobile:** text, detail, portrait and caption; 4:5 portrait retained. Never place text over the portrait.

### 4. Materials and assembly — `#materials`

**Purpose:** connect named materials to the parts they become and show how assembly permits replacement.

**Layout:** chalk. Heading/body across columns 1–9, followed by a 32 px gap and two figures: samples columns 1–6; assembly columns 7–12. Both frames 16:9 with square edges. This is a static pair, not a carousel.

**Exact copy:**

- Eyebrow: **03 / MATERIALS & ASSEMBLY**
- H2: **Wool. Leather. Aluminium.**
- Body: **At the worktable, samples sit beside the components they become. Contact surfaces and trim can be replaced individually.**
- Left caption: **Wool and leather, before fitting.**
- Right caption: **Satin aluminium. Accessible fasteners.**
- Buttons: none.

**Images:** `materials-worktable.webp`, rough graphite wool, warm brown leather contact material, cut satin aluminium with visible edges on a limestone worktable. Alt: **“Graphite wool, brown leather and satin aluminium samples laid together on a stone worktable, their unfinished edges visible.”** `assembly-controls.webp`, hands fastening a replaceable satin aluminium climate-control panel, physical knobs and screw heads visible. Alt: **“A maker fastens a satin aluminium climate-control panel, showing physical knobs, component edges and accessible screw heads.”**

**Mobile:** heading/body, samples/caption, assembly/caption; 32 px between figures. Keep each caption attached to its image.

### 5. Engineering evidence — `#engineering`

**Purpose:** distinguish development ambition from evidence that a buyer could inspect.

**Layout:** graphite, typographic ledger, no photograph. Heading/body occupy columns 1–9. Below, three equal stat groups each span four columns. Use visible silver rules and a `dl`, not cards or animated counters. Conditions and evidence controls span all twelve columns.

**Exact copy:**

- Eyebrow: **04 / DEVELOPMENT PROGRAMME**
- H2: **Figures, with their conditions.**
- Body: **The programme follows loaded motorway journeys, broken secondary roads and repeated charging stops. The figures below are development targets, not verified results.**
- Figure/label pairs: **520 km — Target combined WLTP range**; **27 min — Target DC charge, 10–80%**; **450 kW — Target combined output**.
- Conditions: **Charging target requires a conditioned battery and a suitable charger. Homologation and independent route results are not yet available.**
- Disclosure labels, styled as underlined text controls: **Read the proposed test method**; **View evidence status**.

Use two native `details` disclosures, collapsed initially. Their `summary` elements are the two controls visible in the image; add a decorative disclosure marker without changing their accessible names. Expanded text is exact:

- **Read the proposed test method:** “Record ambient temperature, speed, luggage load, consumption, charging time and cabin noise on motorway and rough secondary-road routes. Repeat in winter conditions and publish the complete charging curve with battery temperature and charger conditions. Independent witnessing and final methodology remain to be arranged.”
- **View evidence status:** “Development targets only. No homologated range, independently witnessed route report or verified charging result is available in this demonstration. Figures will be replaced or qualified when documented results are available.”

**Images:** none. Do not fabricate a certification seal, test graph or downloadable report.

**Mobile:** stack all three stats, each with its label immediately adjacent in document order; horizontal separators replace vertical ones. Stack disclosure controls; expanded text flows in the page.

### 6. Continued ownership — `#ownership`

**Purpose:** make service access visible and describe the scope and status of the support agreement.

**Layout:** chalk. Technical figure columns 1–7, 4:3 frame; copy columns 8–12. The diagram is a fine-line graphite isometric chassis study with battery access panel separated below and replaceable interior parts above. Technical labels are live HTML outside the SVG.

**Exact copy:**

- Eyebrow: **05 / CONTINUED OWNERSHIP**
- H2: **Made to remain in use.**
- Body paragraph 1: **Replaceable upholstery. Accessible battery modules. Core driving functions without a cloud account.**
- Body paragraph 2: **The proposed ownership agreement provides parts and diagnostic support for 15 years after the final 01 is built. Written terms and the supporting service evidence must be reviewed before commissioning.**
- Caption: **Service access study — illustrative, not a repair instruction.**
- Text equivalent, visible below the caption: **The study separates the lower battery access panel from the chassis and shows removable seat trim and accessible fasteners. Battery work is for qualified technicians.**
- Buttons: none.

**Image:** `service-access.svg`. Alt: **“Exploded service-access study of the 01 chassis, battery access panel and removable interior components; explanation follows.”** Keep the SVG itself free of baked-in small text; no claimed dimensions or repair sequence.

**Mobile:** heading/body, diagram, caption and text equivalent. Use this same DOM reading order on desktop with grid placement. Diagram remains full column width and secondary text must not become tiny to fit it.

### 7. The house — `#house`

**Purpose:** identify the founders, place and working practice behind the car.

**Layout:** graphite. Wide atelier photograph columns 1–7, 16:9; text columns 9–12. Alignment is deliberately offset from the previous chapter, with column 8 empty.

**Exact copy:**

- Eyebrow: **06 / THE HOUSE**
- H2: **One atelier. A shared worktable.**
- Body: **Iria Veyravel, a vibration engineer, and Lucan Esmeret, a coachbuilder, founded the house in 2017. Near Saint-Claude in the French Jura, fitting, assembly and the appointment salon share one roof.**
- Buttons: none.

**Image:** `founders-atelier.webp`. Two fictional founders at a material-covered worktable in the same limestone/steel workshop; the graphite coupe visible behind them. Alt: **“Iria Veyravel and Lucan Esmeret at the material worktable inside their Jura atelier, with the graphite 01 behind them.”**

**Mobile:** heading/body then image. Match this reading order in the DOM. Do not invent awards, production history or founder signatures.

### 8. Private appointment — `#appointment`

**Purpose:** explain the visit and let a reader prepare an inquiry without suggesting a booking or deposit has been accepted.

**Layout:** chalk. Road photograph columns 1–6 at 16:9; invitation columns 7–12. Under body, action/helper and direct contact sit side by side in the right half, separated by a 1 px graphite rule. The final invitation has 128 px desktop vertical padding.

**Exact copy:**

- Eyebrow: **07 / PRIVATE APPOINTMENT**
- H2: **Begin with the journey you make.**
- Body: **Allow three hours for a personal fitting and an extended drive on the roads above the atelier. Bring your companion, your luggage and the route you know by heart.**
- Button: **Request a private appointment**
- Helper: **Opens a demonstration email draft. No appointment is booked.**
- Contact heading: **Appointment office**
- Location: **Saint-Claude, French Jura**
- Email: **appointments@veyravel.example**
- Contact helper: **Demonstration address — not monitored.**

**Image:** `jura-road.webp`. Empty wet secondary road, stone parapet, overcast limestone gorge; no car needed. Alt: **“A wet secondary road curves beside a stone parapet beneath pale limestone cliffs in the French Jura.”**

**Mobile:** invitation, action/helper, contact block, road image. Replace the vertical contact divider with a horizontal rule. Email wraps; keep 44 px action targets and 18 px body copy at 320 px.

**Action contract for all three appointment CTAs:** use an actual link to `mailto:appointments@veyravel.example?subject=Demonstration%20private%20appointment%20request&body=This%20is%20a%20demonstration%20draft.%20No%20appointment%20is%20booked.%0A%0AMy%20usual%20journey%3A%0AMy%20preferred%20visit%20dates%3A`. It opens the visitor's email application if configured; the site sends nothing. Preserve the exact visible label **“Request a private appointment”** in header, arrival and closing. Associate each helper using `aria-describedby`. The direct email link opens the same labelled demonstration draft. Keep the address selectable so it can be copied if no mail app is configured. A real monitored inbox and agreed service terms are production launch inputs; do not invent contact details.

## Components

### Navigation

Desktop: wordmark left, **The 01**, **Making**, **Ownership**, **The House** centred, appointment CTA right with **Demonstration email draft** below it. Map these links to `#touring`, `#fit`, `#ownership`, `#house` for this one-page showcase; do not create dead links to unbuilt pages. Wordmark links to `#arrival`, accessible name **“Veyravel home”**. First focusable link: **“Skip to main content”**, pointing to `#main`; hidden off-screen until focused, then displayed on an opaque chalk plate with graphite text and clay ring.

Default nav text chalk/graphite; hover keeps the same ink and adds a 1 px underline; focus adds the standard brass ring plus underline. Current location may use `aria-current="location"` and a permanent underline. All nav targets at least 44 × 44 px. No disabled nav items on the homepage; if a destination is unavailable, render silver noninteractive text with **“Unavailable”** and no `href`, without opacity.

Below 1024 px, put the wordmark above a full-width appointment link and an inline native `details` menu with summary **“Menu”**. It opens a vertical list in the document flow. No modal, focus trap or off-canvas overlay. Summary gets the same hover/focus treatment and announces its expanded state natively. At 320 px the appointment label wraps within its padded target.

### Buttons

Appointment links use button styling, not `button` semantics. Min-height 48 px, min-width 44 px, 16 px horizontal and 8 px vertical padding; allow multiline labels. Border 1 px, corners 0 px.

| Surface | Default | Hover / pointer active | Keyboard focus | Disabled, if ever needed |
| --- | --- | --- | --- | --- |
| Graphite | Chalk label and border, graphite fill | Graphite label, chalk fill/border | Default or hover state plus brass outer ring with graphite gap | Silver label and dashed silver border on graphite; no opacity |
| Chalk | Graphite label and border, chalk fill | Chalk label, graphite fill/border | Default or hover state plus clay outer ring with chalk gap | Clay label and dashed clay border on chalk; no opacity |

No disabled appointment CTA in this design: the demonstration draft is available. For a future actual disabled action use native `disabled` on a `button`, with visible explanation **“Unavailable”**. Do not apply a fake disabled appearance to a working link. Focus indication appears immediately, never after the hover transition.

### Links and disclosures

Body links are underlined from rest: chalk on graphite, clay on chalk. Hover increases underline thickness from 1 to 2 px; dark link ink may become brass, light link ink becomes graphite. Focus adds the local ring while preserving the underline. Disabled references are noninteractive plain text: silver on graphite, clay on chalk, plus **“Unavailable”**. Do not use colour alone to indicate disabled/current state. Give standalone links 44 px minimum height; inline prose links may retain their natural line box.

The evidence controls use native `details`/`summary` keyboard behaviour: Enter or Space toggles, focus stays on the summary, content remains inline, and no dialog opens. Use a CSS plus/minus marker hidden from assistive technology. They share link colours and focus states; native disclosure content works without JavaScript.

### Form fields

**No form fields appear on this homepage.** The authorised static action is the demonstration email draft; do not add a fake submission flow. Reserve the following tokens for a later appointment page so the component handoff covers inputs without adding a section to this design:

- Chalk background; graphite input text and persistent visible label; clay 1 px border. Minimum 48 px input height, 16 px inner padding, 18 / 28.8 px Manrope 400. Labels 16 / 24 px Manrope 500, 8 px above; helper 16 / 25.6 px graphite, 8 px below.
- Hover: graphite border; no colour change to text. Focus: 2 px clay ring, 4 px chalk gap, no lost border. Disabled: clay label/value and dashed clay border on chalk, native `disabled`, visible **“Unavailable”** helper; never fade the entire control.
- Error: clay border and text plus the explicit message **“Enter a valid email address.”** Set `aria-invalid="true"` and connect the message with `aria-describedby`; error state retains the focus ring. Required state must include visible **“(required)”** text.
- If implemented later: real labels and `type="email"`, `autocomplete="email"`; name uses `autocomplete="name"`. Permit paste and browser autofill; no placeholder-only labels, account requirement, CAPTCHA or custom date picker. Production submission needs a real endpoint and an accurate success state.

### Footer

Graphite, 64 px desktop / 48 px mobile padding. Logo left, same four navigation links in the same order, then **Privacy**, **Accessibility**, then **Fictional house. Demonstration website.** Silver legal text; chalk links. Contact information stays directly above it in the appointment section, in the same DOM position on future pages. Mobile stacks these groups with 24 px gaps and uses two columns only when each 44 px link target fits comfortably.

Privacy and Accessibility are native inline `details` summaries styled like the footer links; their expanded text appears below the footer row. This keeps both destinations useful in the static showcase without unbuilt pages. Exact text:

- **Privacy:** “This demonstration has no inquiry form, analytics or tracking cookies. Appointment links open your email application; the website does not send the draft. Fonts are requested from Google Fonts.”
- **Accessibility:** “This demonstration is designed for keyboard use, visible focus, reduced motion and reflow at 320 CSS pixels. To report an access issue, use the appointment office contact above; its address is a demonstration placeholder and is not monitored.”

Footer hover/focus/disabled states follow the dark link rules above. Logo alt is **“Veyravel”**; decorative image-internal duplicate lettering, if any, must not generate a second accessible name. No newsletter, tracking banner, social icons or deposit flow is needed.

## Motion

| Element | Behaviour | Duration / easing | Reduced-motion fallback |
| --- | --- | --- | --- |
| Story photographs | Optional one-time opacity reveal from 0.85 to 1 when entering the viewport; text stays visible | 600 ms, `cubic-bezier(0.22, 1, 0.36, 1)` | Fully opaque, immediately visible |
| Link underline | Extend underline or change thickness on hover | 400 ms, same curve | Immediate underline change |
| Button fill and label | Swap both approved colours together immediately; a decorative underline may extend | Colour swap 0 ms; underline 400 ms, same curve | Immediate state change |
| Focus rings | Appear as soon as focus arrives | 0 ms | Same visible ring |
| Menus and disclosures | Native inline opening/closing; no height animation | 0 ms | Same native behaviour |

Content is visible by default, including without JavaScript. Any reveal enhancement must be isolated to photographs; never hide an entire section, heading or interactive control while waiting for an observer. No translation, parallax, autoplay, zoom, counters, smooth-scroll interception, custom cursor or automatic carousel. Native document scrolling remains intact.

Do not tween text or fill colours: interpolating between an inverted button's two states would create low-contrast intermediate frames. Only underline geometry and photo opacity animate; all text/background combinations remain the audited solid pairs at every moment.

Under `prefers-reduced-motion: reduce`, disable all animation and transitions and use `scroll-behavior: auto`. Respond if the preference changes during the session. Hover styles must also work without hover-capable input; they convey no essential information that is absent from the default state.

Before acceptance, check keyboard order, visible rings, inline disclosures with JavaScript disabled, 200% text zoom, 320 px reflow, and text-spacing overrides (1.5 line height, 0.12em letter spacing, 0.16em word spacing, paragraph spacing 2em). Text must grow without clipping and the diagram must never force horizontal scrolling. These are implementation acceptance checks, not claims that a raster image establishes WCAG conformance.

## Asset list

The asset team will create the following files in **`clients/car/assets/`**. Sizes are export sizes, not fixed layout dimensions; photos are approximately 2× the largest intended display size. All photos must depict the same original coupe, fictional people and consistent workshop. No real brand names, logos, registration marks or manufacturer-specific control designs. All textual UI, captions, measurements and diagram explanations remain HTML.

| File name | Kind | Size in px | Format | What it shows |
| --- | --- | --- | --- | --- |
| `veyravel-wordmark.svg` | logo | 360 × 48 viewBox | SVG | Original widely spaced VEYRAVEL wordmark; chalk on transparent, with a graphite colour variant implemented through `currentColor` inline use; no inherited real-world insignia |
| `hero-profile.webp` | photo | 2880 × 960 | WebP | Graphite two-seat coupe in complete side profile, wet tarmac, pale limestone wall and Jura cliffs; full-bleed 3:1 desktop plate |
| `hero-profile-mobile.webp` | photo | 1200 × 900 | WebP | Art-directed 4:3 view of the same location and complete car; both wheels and roof line retained |
| `touring-luggage.webp` | photo | 1600 × 1200 | WebP | Open rear hatch, exactly two fitted cases and two weekend bags, both seats visible beyond |
| `fitting-portrait.webp` | photo | 1200 × 1500 | WebP | Maker's face and hands adjusting the wool driver's seat; steering reach and physical controls visible |
| `materials-worktable.webp` | photo | 1280 × 720 | WebP | Wool, leather and satin aluminium samples with tactile cut edges on the atelier worktable |
| `assembly-controls.webp` | photo | 1280 × 720 | WebP | Hands assembling a satin aluminium climate-control unit, exposed fasteners and physical knobs |
| `service-access.svg` | icon (technical diagram) | 1600 × 1200 viewBox | SVG | Graphite fine-line isometric chassis, separated lower battery access panel, removable interior parts; transparent background, no raster text or repair instructions |
| `founders-atelier.webp` | photo | 1600 × 900 | WebP | Iria and Lucan at their worktable, limestone/steel workshop and same graphite coupe behind |
| `jura-road.webp` | photo | 1440 × 810 | WebP | Wet quiet secondary road with stone parapet beneath limestone cliffs; no text, road branding or vehicle required |

No separate monogram or texture is required: the wordmark is sufficient and the material photography supplies texture. Navigation, disclosure markers and underlines are native text/CSS; do not commission redundant icon files. The technical drawing uses non-scaling strokes so it stays legible at mobile width. Use `width`/`height` attributes, meaningful alt text as specified, `srcset` when smaller derivatives are available, eager loading for the hero and lazy loading for later photos. Hero should target at most 450 KB, mobile hero 200 KB and each other photo 250 KB, preserving visible material grain. Treat these as export targets, not reasons to blur critical details.

Implementation delivery remains static HTML, CSS and minimal JavaScript, without a build step or framework. Reference assets relatively from the future site as `../../clients/car/assets/<file>`. Google Fonts is the only external resource request; email opens are explicit user actions. Never use `design.jpg` as the website's background or a single image-of-text page.

### Image production record

Generated with the built-in image generation tool in `ui-mockup` mode; no CLI/API fallback. The selected complete image was saved to `design.jpg` and normalised to the requested 1440 px delivery width. Its original generated raster was 720 × 2183 px; the delivered 1440 × 4366 px file is a 2× resample, not newly resolved detail. The font choices, exact readable copy and accessibility states in this specification govern the production build. The full generation prompt follows for reproducibility.

<details>
<summary>Final image-generation prompt</summary>

```text
Use case: ui-mockup.
Create ONE exquisitely art-directed, full-page desktop homepage design image for the FICTIONAL electric grand tourer house VEYRAVEL. Entire scroll from navigation through all EIGHT sections to footer, top to bottom, a single flat screenshot, no perspective mockup, no browser frame. Target canvas 1440px wide by 5760px high; make the canvas tall enough for every section and readable text. This is a desktop website, NOT a mobile website. Maintain the 1440px desktop composition and realistic 18px body text. No cropping off footer, no numbered presentation slides, no extra logos, no real brands or real car designs. Original two-seat graphite electric coupe with elegant long fastback, restrained dimensions, smooth wheel discs, no grille, NO badges.
Visual concept: "the journey and the fitting table." A restrained cinematic graphite showroom opening alternates with warm chalk workshop chapters. Strong editorial asymmetry with 12-column grid, 80px side margins, 24px gutters. Flat square edges, no rounded cards, no gradients, no shadows, no gaudy gold. Lots of deliberate empty space. Typography is Newsreader regular 400, fine editorial serif for headlines, Manrope regular 400 and medium 500 for body and navigation. 72px hero headline, 48px section headlines, 18px body, 16px captions. Type colours ONLY chalk #F1EEE7 and mineral silver #AFB8B9 on graphite #171B1D; graphite #171B1D and fired clay #80543F on chalk #F1EEE7. Pale brass #D7B98E only tiny focus/detail accents on graphite. ALL text outside photographs on solid backgrounds. High contrast, highly readable. Photographs genuine-looking editorial photography, overcast Jura light, pale limestone, wet roads, physical materials, consistent original car throughout.
EXACT PAGE ORDER AND CONTENT:
HEADER graphite, height 96px: wordmark "VEYRAVEL" at left, quiet navigation "The 01" "Making" "Ownership" "The House", outlined CTA "Request a private appointment" at right. Tiny note under CTA "Demonstration email draft".
1 ARRIVAL graphite, headline left and short description / CTA right above large edge-to-edge cinematic profile photograph. Eyebrow "THE VEYRAVEL 01". Headline "Made for the distance between places." Plain description "An electric grand tourer. Two seats. Up to 180 commissions a year." Outlined CTA "Request a private appointment". Under CTA "Demonstration email draft". Full-width photograph of a graphite original low two-seat fastback coupe side profile parked against long pale limestone wall and wet Jura tarmac, overcast sky; car fills horizontal frame, sophisticated dark tonal photograph, no text on photograph.
2 TOURING PROPOSITION chalk, generous padding: large loaded luggage photograph left spanning 7 columns; heading and body right 4 columns with offset. Eyebrow "01 / THE JOURNEY". Headline "Two seats. A week’s luggage. Your own measure." Body "Two fitted cases and two weekend bags sit behind the seats. The 01 is shaped for the journeys you make together, with room for what you take." Specification ledger three rows "4.78 m / Length", "1.89 m / Width, excluding mirrors", "360 L / Luggage capacity". Photograph explicitly shows open rear hatch with exactly two fitted cases and two weekend bags.
3 FIT graphite, text left 5 columns, tall real portrait right 5 columns, blank column between: eyebrow "02 / PERSONAL FIT". Headline "Your first appointment begins in the seat." Body "We adjust its support, place your luggage behind you and take the 01 onto the roads above the atelier. The fitting record grows from the way you intend to travel." Small detail "Seat support · Steering reach · Pedal position". Photograph of a named-in-caption "At the fitting atelier" maker kneeling beside the open driver door, adjusting wool seat support, intimate candid craft, face and hands visible, physical steering wheel and pedals.
4 MATERIALS AND ASSEMBLY chalk. Eyebrow "03 / MATERIALS & ASSEMBLY". Headline "Wool. Leather. Aluminium." Body "At the worktable, samples sit beside the components they become. Contact surfaces and trim can be replaced individually." Below, two square-edge editorial photographs side by side, asymmetric 5 and 7 columns: left close tactile wool/leather/aluminium sample composition with exposed edges, right hands fastening a satin aluminium physical climate-control assembly with exposed screw heads. Captions "Wool and leather, before fitting." and "Satin aluminium. Accessible fasteners."
5 ENGINEERING EVIDENCE graphite, no background photograph, rigorous typography and ruled ledger. Eyebrow "04 / DEVELOPMENT PROGRAMME". Headline "Figures, with their conditions." Body "The programme follows loaded motorway journeys, broken secondary roads and repeated charging stops. The figures below are development targets, not verified results." Three large stat columns "520 km" / "Target combined WLTP range", "27 min" / "Target DC charge, 10–80%", "450 kW" / "Target combined output". Important visible caption "Charging target requires a conditioned battery and a suitable charger. Homologation and independent route results are not yet available." Two underlined text links "Read the proposed test method" and "View evidence status".
6 CONTINUED OWNERSHIP chalk. Eyebrow "05 / CONTINUED OWNERSHIP". Headline "Made to remain in use." Left large fine-line graphite isometric technical illustration of original electric coupe skateboard chassis, battery access panel visibly separated below, seat trim fasteners, no opaque photo background. Beside it text right: "Replaceable upholstery. Accessible battery modules. Core driving functions without a cloud account." Second paragraph "The proposed ownership agreement provides parts and diagnostic support for 15 years after the final 01 is built. Written terms and the supporting service evidence must be reviewed before commissioning." Small caption under diagram "Service access study — illustrative, not a repair instruction."
7 THE HOUSE graphite. Eyebrow "06 / THE HOUSE". Headline "One atelier. A shared worktable." Body "Iria Veyravel, a vibration engineer, and Lucan Esmeret, a coachbuilder, founded the house in 2017. Near Saint-Claude in the French Jura, fitting, assembly and the appointment salon share one roof." Broad editorial photo left of two fictional middle-aged founders standing beside a large materials worktable inside a pale stone and steel atelier, the original coupe in the background. Text right in 4 columns.
8 PRIVATE APPOINTMENT chalk. Eyebrow "07 / PRIVATE APPOINTMENT". Headline "Begin with the journey you make." Body "Allow three hours for a personal fitting and an extended drive on the roads above the atelier. Bring your companion, your luggage and the route you know by heart." Outline dark CTA "Request a private appointment". Prominent clear helper "Opens a demonstration email draft. No appointment is booked." Direct contact block "Appointment office" / "Saint-Claude, French Jura" / "appointments@veyravel.example" / "Demonstration address — not monitored."
FOOTER graphite, complete at bottom: wordmark "VEYRAVEL", house navigation repeated quietly, "Privacy" "Accessibility", and "Fictional house. Demonstration website."
Ensure all EIGHT distinct sections remain visible in this exact order. This must look like a confident finished luxury website with actual intended photography and exact real copy, not a wireframe. Do not replace body text with gibberish or lorem ipsum.
```

</details>
