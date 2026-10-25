I inspected [`examples/maison-lumen/BRIEF.md`](../BRIEF.md), researched public brand/design case studies from leading luxury digital agencies (Pentagram, AREA 17, Build in Amsterdam, KMS Team, Wednesday, BIRCH, Construct), and extracted live production CSS tokens (`@font-face`, custom properties, hex palettes, type scales, letter-spacing, and grid layouts) from 10 luxury houses across automotive, horology, hospitality, and fashion. No files were created or modified (`read-only` task).

---

# Digital Flagship Design Guidelines of the Great Luxury Houses

## 1. Houses & Agencies Studied (10 Houses Across 4 Verticals)

| Vertical | House | Primary URL & Agency / Typography Reference | Core Digital Posture |
| :--- | :--- | :--- | :--- |
| **Automotive** | **Rolls-Royce Motor Cars** | [rolls-roycemotorcars.com](https://www.rolls-roycemotorcars.com/en_GB/home.html) · Pentagram ([Case Study 1](https://www.pentagram.com/work/rolls-royce-2), [Case Study 2](https://www.pentagram.com/work/rolls-royce-3)) | Nocturnal "House of Luxury" showroom; bespoke sans-serif + beveled Art Deco display |
| **Automotive** | **Bentley Motors** | [bentleymotors.com](https://www.bentleymotors.com/en.html) · KMS Team ([Bentley Case Study](https://www.kms-team.com/en/cases/bentley/)) | Technical British grand touring; dark-mode configurator precision |
| **Horology** | **Audemars Piguet** | [audemarspiguet.com](https://www.audemarspiguet.com/com/en/home.html) | Architectural museum/gallery; ultra-thin grotesque + sharp italic serif |
| **Horology** | **Patek Philippe** | [patek.com](https://www.patek.com/en/home) · [Fonts in Use](https://fontsinuse.com/in/2/formats/55/magazines-journals) | Archival Geneva salon; warm parchment, bronze/gold accents, print-editorial serif |
| **Horology** | **A. Lange & Söhne** | [alange-soehne.com](https://www.alange-soehne.com/eu-en) ([Live CSS](https://www.alange-soehne.com/als/dist/assets/main-0zN_Xf6M.css)) | Saxon engineering austerity; obsidian `#1b1b1b` canvas and German-silver tokens |
| **Hospitality** | **Aman** | [aman.com](https://www.aman.com) · [Blaze Type](https://blazetype.eu/typefaces/aman/) · [BP&O / Construct](https://bpando.org/2016/02/15/logo-aman/) | Architectural sanctuary; warm linen `#f3eee7`, soft charcoal `#1d1d1b`, zero visual noise |
| **Hospitality** | **Belmond** | [belmond.com](https://www.belmond.com/) ([Live CSS](https://www.belmond.com/_nuxt/entry.Mn3Glzco.css)) | Cinematic slow travel; 24-column editorial subgrid and warm stone `#efefec` |
| **Hospitality** | **Rosewood Hotels** | [rosewoodhotels.com](https://www.rosewoodhotels.com/en/default) · [The Brand Identity / BIRCH](https://the-brandidentity.com/project/birch-treats-hotel-marketing-like-a-fashion-editorial-for-rosewood) | "Sense of Place" manor editorial; high-contrast italic serif + estate greens/parchment |
| **Fashion** | **Hermès** | [hermes.com](https://www.hermes.com/us/en/) · [Bonhomme Paris Glossary](https://bonhommeparis.com/en/fontsfontsfonts/glossary/hermes) | Tactile craft & whimsy; ecru/parchment canvas with controlled orange punctuation |
| **Fashion** | **Chanel** (with **Loro Piana** & **Balenciaga**) | [chanel.com](https://www.chanel.com/us/) ([Bonhomme](https://bonhommeparis.com/en/fontsfontsfonts/glossary/chanel)) · [loropiana.com](https://www.loropiana.com/en/) · [AREA 17 Balenciaga](https://area17.com/clients/balenciaga) | Monochromatic couture authority (Chanel), cashmere warmth (Loro Piana), gallery restraint (AREA 17) |

---

## 2. Typography: Pairings, Scales, Weights, and Tracking

Luxury houses reject bold weights (`700+`) and tight UI cramming. Hierarchy is achieved through **scale contrast, light weights (`100`–`400`), italic editorial serifs, and wide-tracked uppercase micro-labels**.

- **High-Contrast Editorial Serif + Neutral Grotesque/Humanist Sans (The Dominant Paradigm):**
  - **Aman** ([aman.com](https://www.aman.com)) loads `LyonDisplay-Light-Web.woff2` (`300`) and `LyonText-Regular-Web.woff2` (`400`) for headings and narrative copy, paired with `WhitneySSm` (`300` Light / `400` Book) for navigation and metadata, alongside its custom stone-carved *Aman* serif by [Blaze Type](https://blazetype.eu/typefaces/aman/).
  - **Belmond** ([belmond.com](https://www.belmond.com/)) pairs `Sebenta` (`300`, `400`, `500` serif) with `Gotham ScreenSmart` (`GothamSSm-Light`, `Book`, `Medium`).
  - **Rosewood** ([rosewoodhotels.com](https://www.rosewoodhotels.com/en/default)) pairs `Austin Light Web Italic` (a high-contrast editorial serif) for atmospheric titles with a clean system/grotesque sans-serif stack for booking UI.
  - **Patek Philippe** ([patek.com](https://www.patek.com/en/home)) defines `--font-primary: 'lora'` (editorial serif), `--font-secondary: 'openSans'` (body/UI), and `--font-alt: 'erbaum'` (technical labels).
  - **A. Lange & Söhne** ([alange-soehne.com](https://www.alange-soehne.com/eu-en)) pairs `ALangeUndSoehne-Headline` (engraved Saxon serif) with `UniversforALS` (custom Univers neo-grotesque).
  - **Audemars Piguet** ([audemarspiguet.com](https://www.audemarspiguet.com/com/en/home.html)) inverts the ratio: primary display headings use ultra-light `Neue-Helvetica-25-Ultra-Light` (`font-weight: 100`) and `Neue-Helvetica-35-Thin` (`200`), counterbalanced by a `250 italic` serif (`--font-secondary-display-xl: 250 italic 9.3rem/.83 var(--font-family-secondary)`).
- **Proprietary All-Sans Couture & Automotive Systems:**
  - **Rolls-Royce** ([Pentagram](https://www.pentagram.com/work/rolls-royce-2)) commissioned **Rolls-Royce Pioneer** (Colophon Foundry, 5 weights) and **Riviera Nights** (beveled display caps).
  - **Chanel** ([chanel.com](https://www.chanel.com/us/), [Bonhomme](https://bonhommeparis.com/en/fontsfontsfonts/glossary/chanel)) uses proprietary **AB Chanel Corpo** in uppercase across all headings.
- **Concrete Type Scale & Line-Height Tokens (Audemars Piguet & Belmond Live CSS):**
  - **Display / Hero (`H1`):** `40px` (`2.5rem`) on mobile scaling to `56px`–`93px` (`3.5rem`–`5.8rem`) on desktop (`--font-primary-display-xl: 100 8.6rem/1` on AP's 10px root; `93px` for secondary italic display). Line-height is tight: `0.83` to `1.15`.
  - **Section Headlines (`H2`):** `28px`–`32px` mobile scaling to `40px`–`56px` desktop (`--font-primary-headline-lg: 100 5.6rem/6.4rem`, line-height `1.14`–`1.25`).
  - **Subheads / Titles (`H3`):** `20px`–`32px` (`line-height: 1.25`–`1.33`).
  - **Body Copy:** `16px` (`1rem`) with `14px` (`0.875rem`) secondary body (`--font-primary-body-lg: 300 1.6rem/2.4rem`, `line-height: 1.5`–`1.65`, constrained to `55ch`–`68ch` measure).
  - **Eyebrows, Micro-Labels & Navigation:** `10px`–`12px` (`0.625rem`–`0.75rem`, `font-weight: 500`, `text-transform: uppercase`).
- **Concrete Tracking (`letter-spacing`) Values:**
  - **Uppercase Eyebrows, Buttons & Navigation:** `+0.14em` to `+0.20em` (`2.4px` / `0.1428rem` in [Aman's CSS](https://www.aman.com); `.16em` and `2.52px` in [Rosewood's CSS](https://www.rosewoodhotels.com/en/default); `1.5px` in [Belmond's CSS](https://www.belmond.com/)).
  - **Large Lowercase/Title-Case Display Serifs:** `-0.02em` to `-0.04em` (`-0.7px` in [Aman's CSS](https://www.aman.com); `-.0375rem` in [Belmond's CSS](https://www.belmond.com/)).
  - **Body Copy:** `0em` (`0` in Aman, Lange, and Belmond CSS).

---

## 3. Colour Palettes: The Ratio of Black, Ivory, and Metallic

Luxury websites avoid raw browser defaults (`#000000` text on `#FFFFFF` backgrounds) except in high-fashion couture (Chanel, Bottega Veneta). Instead, hospitality and heritage houses use **warm mineral/paper neutrals** (~80–85% of viewport), **softened obsidian/anthracite** (~10–15%), and **restrained metallic or heritage accents** (<5%, limited to 1px hairlines, active states, and monograms).

| House | Canvas / Ivory / Surface Hexes | Dark / Text / Obsidian Hexes | Metallic & Heritage Accent Hexes |
| :--- | :--- | :--- | :--- |
| **Aman** ([aman.com](https://www.aman.com)) | `#F3EEE7` / `#F3EEE3` (warm linen), `#EBE8E5` (stone), `#D4CDC3` (sand border) | `#1D1D1B` / `#313131` (anthracite), `#404040`, `#7C7C7C` (warm grey) | `#B08D57` (muted bronze), `#325E1C` (botanical accent) |
| **Audemars Piguet** ([audemarspiguet.com](https://www.audemarspiguet.com/com/en/home.html)) | `#F6F5F3` (`beige96`), `#E7E4DF` (`beige89`), `#FBFAF9` | `#1B1B1B` (`grey11`), `#000000`, `#757575` (`boulder`) | `#02291F` (Vallée de Joux deep green), `#456148` (brand green), `#2B4F4F` |
| **A. Lange & Söhne** ([alange-soehne.com](https://www.alange-soehne.com/eu-en)) | `#FAFAFA`, `#E8E7E6`, `#D9D9D9` (argentine silver) | `#1B1B1B` (primary dark showcase), `#393939` | `#B9AF8C` (`--minute-repeater-zeitwerk-color-gold`, German silver/champagne), `#B8B8B8` |
| **Patek Philippe** ([patek.com](https://www.patek.com/en/home)) | `#FCFBF9` (parchment), `#FFFFFF` | `#1A1A1A` (charcoal), `#8C7A66` (warm taupe) | `#C6BA82` (Calatrava pale gold) |
| **Belmond** ([belmond.com](https://www.belmond.com/)) | `#FBFBFA`, `#F7F7F5`, `#F1F1EF`, `#EFEFEC` (`stone-400`) | `#0F1D2F` (heritage midnight), `#4D4D4D` (`midnight-350`) | `#E84221` (terracotta accent, used <2% for CTAs) |
| **Rosewood** ([rosewoodhotels.com](https://www.rosewoodhotels.com/en/default)) | `#E8E5CF` (parchment), `#F7F4F0` (cream) | `#191919` (near-black), `#031633` (manor navy), `#4C4C4C` | `#435643` / `#01503B` (estate green), `#664D03` / `#FFE69C` (antique brass) |
| **Rolls-Royce & Bentley** ([pentagram.com](https://www.pentagram.com/work/rolls-royce-2), [kms-team.com](https://www.kms-team.com/en/cases/bentley/)) | `#F5F5F3` (technical light mode) | `#121212` / `#0A0A0A` (dark showroom primary) | `#2A1B2E` (Purple Spirit), `#004225` (British Racing Green), `#C0C0C0` (chrome) |
| **Hermès & Chanel** ([hermes.com](https://www.hermes.com/us/en/), [chanel.com](https://www.chanel.com/us/)) | `#EAE0D5` / `#FAF7F2` (Hermès ecru), `#FFFFFF` (Chanel) | `#0A0908` / `#444444` (Hermès), `#000000` / `#3E3E3E` (Chanel) | `#F37021` (Hermès Orange, interactive punctuation only) |

**Key Rule on Metallics:** None of the 10 houses use CSS linear-gradient "faux gold" on buttons. Metallic tones (`#C6BA82`, `#B9AF8C`, `#B08D57`) are flat, desaturated champagne/brass hexes that pass or pair with high-contrast text, leaving real specular reflection to macro photography.

---

## 4. Whitespace, Grid Architecture, and Concrete Spacing Scales

Luxury interfaces treat whitespace as architectural gallery floor ([AREA 17 Balenciaga](https://area17.com/clients/balenciaga); [Build in Amsterdam](https://www.buildinamsterdam.com/cases)). At least **40%–55% of any viewport** outside full-bleed hero media remains open background canvas.

- **Grid Systems:**
  - **12-Column or 24-Column CSS Subgrid:** **Belmond** ([belmond.com CSS](https://www.belmond.com/_nuxt/entry.Mn3Glzco.css)) uses a **24-column CSS Grid** with `grid-cols-subgrid` on desktop (`lg:col-start-19 lg:col-span-6`) and 16 columns on tablet (`md:col-span-16`), enabling asymmetrical editorial offsets (e.g., an image spanning columns 2–13 and a text block spanning columns 15–22, leaving outer columns empty).
  - **Max Container Widths & Gutters:** `1440px`–`1680px` max container width, outer page padding of `24px` (mobile) to `64px`–`96px` (desktop), and grid gutters of `24px`–`48px`.
  - **Product & Story Card Density:** Never more than **2 or 3 items per row** on desktop (compared to 4–5 in mass e-commerce).
- **Concrete Spacing Scale (Extracted from [Audemars Piguet Live CSS](https://www.audemarspiguet.com/com/en/home.html)):**
  - Micro/UI tokens: `--spacing-5xs: 4px`, `--spacing-4xs: 8px`, `--spacing-3xs: 16px`, `--spacing-2xs: 20px` (mobile) → `24px` (desktop), `--spacing-xs: 24px` → `32px`.
  - Component tokens: `--spacing-sm: 32px → 48px → 64px`, `--spacing-md: 48px → 64px → 80px`, `--spacing-lg: 64px → 80px → 104px`.
  - Section vertical rhythm tokens: `--spacing-xl: 80px → 96px → 120px`, `--spacing-2xl: 96px → 120px → 176px`, `--spacing-3xl: 120px → 136px → 208px`, `--spacing-4xl: 136px → 160px → 256px`.

---

## 5. Imagery, Art Direction, and Photography vs. Illustration

- **Art Direction:**
  - **Automotive (Rolls-Royce, Bentley):** Low-key studio chiaroscuro and twilight architectural locations ([Pentagram](https://www.pentagram.com/work/rolls-royce-3)). Reflections highlight single coachlines and material grain (open-pore wood, stitched leather).
  - **Horology (Patek Philippe, A. Lange & Söhne, Audemars Piguet):** Extreme macro photography showing hand-beveled *anglage*, *Côtes de Genève*, and perlage at 5x–10x magnification against `#1b1b1b` void backgrounds ([alange-soehne.com](https://www.alange-soehne.com/eu-en)).
  - **Hospitality (Aman, Belmond, Rosewood):** Natural golden-hour or overcast architectural daylight ([aman.com](https://www.aman.com)); zero wide-angle real-estate distortion; human subjects are shown either at a contemplative distance within the landscape or in tactile close-up (hands pouring tea, linen drape) ([BIRCH for Rosewood](https://the-brandidentity.com/project/birch-treats-hotel-marketing-like-a-fashion-editorial-for-rosewood)).
- **Aspect Ratios & Framing:** Sharp `0px` border-radius on all photography (`border-radius: 0px` is universal across Aman, Chanel, AP, Lange, and Loro Piana; rounded card corners signal SaaS/consumer tech, not luxury). Favored aspect ratios are tall editorial portraits (`3:4` or `4:5`) paired with cinematic wides (`16:9` or `21:9`).
- **Photography vs. Illustration:**
  - **95% Photography, 5% Technical/Heritage Line Art:** Corporate Memphis or flat vector spot illustrations are strictly taboo.
  - **Where Illustration Appears:**
    1. **Horology & Automotive:** 1px hairline technical blueprints, exploded movement calibre diagrams, and patent drawings (e.g., [A. Lange & Söhne](https://www.alange-soehne.com/eu-en) and [Audemars Piguet Chronicles](https://www.audemarspiguet.com/com/en/home.html)).
    2. **Hospitality & Fashion:** Hand-drawn architectural estate maps, botanical/equestrian engravings, or bespoke artist commissions ([Hermès](https://www.hermes.com/us/en/), [Belmond](https://www.belmond.com/)).

---

## 6. Motion, Interaction, and Accessibility

Luxury motion simulates physical inertia and unhurried weight ([Build in Amsterdam](https://www.buildinamsterdam.com/cases), [AREA 17](https://area17.com/clients/balenciaga)).

- **Timing & Easing Curves:** Fast durations (`150ms`) feel nervous. Luxury houses use **`500ms`–`900ms`** for reveals and image transitions, and **`300ms`–`450ms`** for hover states, using custom deceleration curves (`cubic-bezier(0.22, 1, 0.36, 1)` or `cubic-bezier(0.16, 1, 0.3, 1)`).
- **Micro-Interactions:**
  - **Links & CTAs:** No bouncy buttons or drop shadows. Links use a 1px underline that animates `transform: scaleX(0)` to `scaleX(1)` (`transform-origin: left`), or an understated pill/rectangle border (`1px solid`) that fills smoothly on hover ([aman.com](https://www.aman.com), [belmond.com](https://www.belmond.com/)).
  - **Image Hover:** Subtle slow scale (`transform: scale(1.02)` over `800ms ease-out`) inside an `overflow: hidden` `0px`-radius frame.
  - **Header Chrome:** Transparent over hero media, transitioning to solid canvas (`#f3eee7` or `#1b1b1b`) on scroll ([Aman CSS](https://www.aman.com)).
- **Accessibility & Reduced Motion:**
  - **Patek Philippe** ([patek.com](https://www.patek.com/en/home)) and **Belmond** ([belmond.com](https://www.belmond.com/en/digital-accessibility-statement)) ship explicit accessible video controls (`aria-label="Play"`, `aria-label="sound on"`, keyboard `tabindex="0"`) and native `<dialog>` modals with Escape-key semantics.

---

## 7. How Product and Price Are (and Are Not) Shown

Luxury digital flagships invert standard e-commerce UX ([Baymard Institute](https://baymard.com/blog/current-state-of-ecommerce-product-page-ux), [NN/g](https://www.nngroup.com/articles/luxury-principles-usability/)): **story and provenance precede specification, and specification precedes price**.

- **Absence of Mass-Market Conversion Chrome:** Zero pop-up discount wheels, countdown timers, star ratings, "X people viewing this", sticky "Buy Now" bars, or crossed-out sale prices.
- **Vocabulary Shift:** Navigation and CTAs never say *"Shop Now"* or *"Buy"*. They use **"Discover"**, **"Explore the Collection"**, **"Configure"**, **"Inquire"**, or **"Request a Private Appointment"** ([Rolls-Royce](https://www.rolls-roycemotorcars.com/en_GB/home.html), [Aman](https://www.aman.com), [Audemars Piguet](https://www.audemarspiguet.com/com/en/home.html)).
- **Vertical-Specific Pricing Rules:**
  1. **Bespoke Automotive (Rolls-Royce, Bentley):** **No price is ever shown on model pages.** The product is presented through narrative chapters (Design, Craft, Performance) leading to a visual configurator and a *"Commission Yours"* / dealer concierge handoff ([rolls-roycemotorcars.com](https://www.rolls-roycemotorcars.com/en_GB/home.html)).
  2. **Haute Horology (Patek Philippe, A. Lange & Söhne, Audemars Piguet):** The homepage and collection pages show zero prices. On deep reference sheets, standard production pieces show a quiet, small-type MSRP (`14px` muted grey) or **"Price on Request"** for grand complications, paired with calibre specifications (number of parts, jewels, power reserve in hours, case diameter in `mm`) and a *"Locate a Salon"* / *"Book an Appointment"* CTA ([patek.com](https://www.patek.com/en/home), [alange-soehne.com](https://www.alange-soehne.com/eu-en)).
  3. **Ultra-Luxury Hospitality (Aman, Rosewood, Belmond):** **No nightly rates appear on the homepage, destination, or villa showcase pages** ([aman.com](https://www.aman.com)). Properties are presented through architecture, geography, and seasonal experiences; rates appear only inside a dedicated reservation/inquiry flow or are replaced entirely by *"Inquire with Private Office"* for private estates and buyouts.

---

## 8. What Maison Lumen Should Do (8 Concrete, Testable Recommendations)

These rules apply directly to Maison Lumen's own flagship and our three showcase clients (the electric grand tourer automaker, the independent haute horology house, and the invitation-only private estate hospitality house) while meeting every constraint in [`BRIEF.md`](../BRIEF.md):

1. **Ban `#000000` on `#FFFFFF`; enforce warm mineral light themes and obsidian dark themes with >= 4.5:1 WCAG 2.2 AA contrast.**
   - *Testable rule:* For Maison Lumen and the hospitality/horology light sections, set canvas backgrounds to warm linen/parchment (`#F5F2EB` to `#F3EEE7`) and primary text to soft anthracite (`#1D1D1B` or `#1B1B1B`, contrast ratio `~15.4:1`). For the electric grand tourer and horology movement showcases, use obsidian (`#121212` to `#1B1B1B`) with warm alabaster text (`#F6F5F3`) and flat champagne/silver accents (`#C6BA82` or `#B9AF8C`), keeping secondary muted text at `#585858` (on light) or `#B0B0B0` (on dark) so every text node passes WCAG 2.2 AA (`>= 4.5:1`).
2. **Pair one light/regular high-contrast Google Font serif (`300`–`400`) with one geometric/humanist Google Font sans-serif (`300`–`500`), and never use `font-weight: 700+`.**
   - *Testable rule:* Load at most 2 font families from Google Fonts (e.g., *Cormorant Garamond*, *Newsreader*, *Instrument Serif*, or *Playfair Display* at weights `300`/`400` + `400 italic` for display/editorial; *Plus Jakarta Sans*, *Inter*, or *DM Sans* at `300`/`400`/`500` for UI/specs). Inspect computed styles: zero elements on any page may compute to `font-weight >= 600`.
3. **Lock a 6-step `rem` typographic scale with tight display leading (`1.0`–`1.15`), relaxed body leading (`1.6`), and wide uppercase tracking (`0.15em`–`0.20em`).**
   - *Testable rule:* Define CSS custom properties: `--text-xs: 0.75rem` (`12px`, uppercase eyebrows/labels with `letter-spacing: 0.16em`), `--text-sm: 0.875rem` (`14px`, captions/specs), `--text-base: 1rem` (`16px`, body copy with `line-height: 1.6` and `max-width: 62ch`), `--text-lg: 1.25rem` (`20px`, lead paragraphs), `--text-xl: clamp(1.75rem, 3vw, 2.5rem)` (`H2`/`H3`), and `--text-display: clamp(2.5rem, 5.5vw, 5.25rem)` (`H1` with `line-height: 1.05` and `letter-spacing: -0.02em`).
4. **Enforce an 8px-base architectural spacing scale with `96px`–`176px` desktop vertical section padding and a 12-column asymmetrical CSS Grid.**
   - *Testable rule:* Use a strict spacing token scale (`8px`, `16px`, `24px`, `32px`, `48px`, `64px`, `96px`, `128px`, `176px`). Every top-level `<section>` must have at least `clamp(5rem, 10vw, 11rem)` (`80px`–`176px`) of vertical padding, and multi-card rows must never exceed **3 columns on desktop** (`1 column` on mobile).
5. **Enforce `border-radius: 0px` and `box-shadow: none` across all imagery, cards, and buttons.**
   - *Testable rule:* Audit `styles.css` across all four sites: zero `border-radius` values above `0px` (except circular `50%` play/control buttons if used) and zero drop shadows on cards. Separate sections and specification rows using `1px solid` hairlines at `12%–18%` opacity of the foreground color.
6. **Use photography for atmosphere and material grain, and restrict SVG graphics to 1px technical blueprints, monograms, and estate maps.**
   - *Testable rule:* Frame photography in tall editorial (`4:5`) and cinematic (`16:9` / `21:9`) ratios with descriptive `alt` attributes detailing material and light. Include at least one 1px-stroke technical SVG per client (an exploded calibre diagram for the horology house, an aerodynamic/chassis line blueprint for the electric grand tourer, and a topographic island/estate plan for the hospitality house).
7. **Replace all transactional e-commerce chrome with progressive disclosure, technical provenance tables, and concierge inquiry flows.**
   - *Testable rule:* Never display a currency symbol (`€`, `$`, `£`), price tag, star rating, or "Buy/Add to Cart" button on the homepage or hero sections. Use a specification ledger (`dl`/`dt`/`dd` or `table`) to prove craft with numbers (e.g., *312 hand-finished components*, *72-hour power reserve*, *12 bespoke commissions per year*, *8 guest residences*), followed by a single primary CTA (*"Request a Private Salon Appointment"*, *"Commission a Specification"*, or *"Inquire with the Private Office"*).
8. **Use slow, inertial CSS transitions (`500ms`–`800ms cubic-bezier(0.22, 1, 0.36, 1)`) and hard-disable them under `@media (prefers-reduced-motion: reduce)`.**
   - *Testable rule:* Limit motion to link-underline reveals (`400ms`), subtle image hover zooms (`scale(1.02)` over `800ms`), and scroll-triggered opacity/translate reveals (`600ms`). Include an explicit `@media (prefers-reduced-motion: reduce)` block in every `styles.css` that sets `animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important;`, and style `:focus-visible` with a high-contrast `2px solid` outline (`outline-offset: 4px`).
