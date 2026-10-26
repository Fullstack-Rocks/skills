# Kaelvorn — Phase 2 style candidate prompts

These three images use the shared scene supplied for Phase 2, with each direction's rendering medium, full palette and lighting setup from `research/art-direction.md` section 5. No real artist, studio or game names occur in the prompts.

Tool: built-in `image_gen.imagegen` (no CLI/API fallback). Model: `gpt-image`, as identified by the PNG provenance; the built-in tool does not expose a more specific model revision or a resolution selector. Every prompt requests the largest native output, targeting 3840 × 2160 and at least 1536 px wide. The tool returned the native sizes recorded below, approximately 16:9; files are saved without resizing or cropping.

## `art/style/candidate-a.png` — Direction A: Gilded Chiaroscuro

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1672 × 941 px, PNG, native output (landscape, approximately 16:9).
- Attempts: 2. Remade once because the first foreground was too tightly rendered; the final repaint strengthens broad bristle strokes, impasto and lost edges. The first image was supplied solely as a composition reference and is not a repository deliverable.

Final prompt, verbatim:

```text
Use case: stylized-concept.
Asset type: pre-launch MMORPG website key art, Direction A — Gilded Chiaroscuro.
Museum-grade digital oil painting on textured linen canvas, bold flat-bristle brushwork and palette-knife impasto, lost-and-found edges. Forms emerge from decisive gestural strokes: thick painted metal highlights, directional bristle-swept cloaks, dry-brushed stone and visible canvas tooth. Sharp contrast at the heroes' upper silhouettes and magical blade; peripheral hems, ruins and clouds dissolve into painterly abstraction.
Scene and composition (keep identical across the three style candidates): landscape 16:9, 24mm wide-angle vista from a fixed camera behind a party of exactly four heroes. On a dark, broken stone cliff ledge occupying the bottom third, the four heroes are seen from behind and in three-quarter view, all looking out across the continent of Kaelvorn. Arrange them left to right: a broad heavily armoured shield-bearer with a large shield; a slimmer cloaked spellblade with one glowing blade; a ranger holding a clearly visible bow, with one wolf-like beast companion beside the ranger; a floating robed arcanist with a staff, boots visibly lifted above the stone. Distinguish all four classes by silhouette alone; keep clear gaps between them and their weapons. Beyond them lies a vast valley with winding rivers, a distant city of pale stone near the centre, and on the right-hand horizon a colossal broken spire with a slow storm of light rising from its break. The spire is the distant threat. Keep the upper-left third as uncluttered, low-contrast sky with generous negative space for a future website title and countdown; do not paint any lettering there. Three depth planes: dark foreground ledge and party, expansive valley and pale city, mist-compressed horizon and sky. Keep the city, river bends, spire, cliff and party placement consistent so this is a style comparison of the same scene.
Strict palette: Abyssal Slate #11151E for the dark foreground and contact shadows; Stormwatch Indigo #232B3A for cool atmospheric shadows and weathered steel; Umber Limestone #6E5A4F for stone and leather; Tarnished Gilding #C29B61 for brass trim and dry grass; Solar Ochre #F2C97D for lit planes; Heraldic Crimson #A62639 for the spellblade's cloak and restrained cloth accents; Aetherial Viridian #38D6C4 for magic and a secondary rim.
Lighting: dramatic 35-degree low golden-hour shafts #F2C97D break through heavy cloud cover, casting long diagonal shadows. Cool slate-indigo #232B3A ambient fill with deep #11151E occlusion and warm/cool shifts across terminators. Sharp palette-knife #F2C97D sunward edges and secondary #38D6C4 arcane rim on shadow contours. Viridian magic has a near-white core, bleeding watercolour-and-oil corona dissolving into #232B3A smoke and teal bounce glints on bronze and steel. Keep the reserved upper-left sky calm despite the dramatic lighting elsewhere.
No photorealism, no 3D plastic sheen, no uniform sharpness, no smooth airbrushed finish.
Output: one full-bleed PNG, landscape 16:9, at the largest native resolution available, target 3840 x 2160 pixels and at least 1536 pixels wide. No text, no lettering, no logos, no watermark, no painted border, no UI, no extra heroes. Do not render a triptych or multiple panels.
Revision instruction: Use the supplied image only as a composition reference, retaining the same party, poses, cliff, pale city, rivers and broken spire placement. Repaint the entire scene more decisively as a visibly handmade oil painting: large flat-bristle stroke shapes across armour, cliffs and clouds; thick, raised palette-knife ochre impasto on light-facing edges; clearly visible linen tooth; fewer tiny descriptive details; deliberate lost-and-found edges around cloak hems and the beast's fur. Keep the four class silhouettes and companion legible. The supplied image's tightly resolved, almost rendered foreground is the specific weakness to correct. Preserve the golden-ochre versus slate-indigo lighting and viridian magic; preserve the clear upper-left sky. This is a complete oil repaint, not a texture overlay.
```

## `art/style/candidate-b.png` — Direction B: Arcane Forge

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1672 × 940 px, PNG, native output (landscape, approximately 16:9).
- Attempts: 1. Retained after visual inspection; no remake.

Final prompt, verbatim:

```text
Use case: stylized-concept.
Asset type: pre-launch MMORPG website key art, Direction B — Arcane Forge.
Stylised hand-painted heroic fantasy illustration, sculptural bevelled forms, bold 3-tone value grouping, zero photo-texture noise. Chunky heroic proportions, oversized bevelled pauldrons, substantial weapons and shield, thick sculptural cloth folds and broad bevelled masonry. Hard, clean silhouettes with deliberate hand-stroked edge highlights and painted-in dents. Every form reads like a master-painted miniature, with warm upper planes and dark baked cavity shading. Broad, rich colour blocks and clean painted gradients rather than loose oil impasto.
Scene and composition (keep identical across the three style candidates): landscape 16:9, 24mm wide-angle vista from a fixed camera behind a party of exactly four heroes. On a dark, broken stone cliff ledge occupying the bottom third, the four heroes are seen from behind and in three-quarter view, all looking out across the continent of Kaelvorn. Arrange them left to right: a broad heavily armoured shield-bearer with a large shield; a slimmer cloaked spellblade with one glowing blade; a ranger holding a clearly visible bow, with one wolf-like beast companion beside the ranger; a floating robed arcanist with a staff, boots visibly lifted above the stone. Distinguish all four classes by silhouette alone; keep clear gaps between them and their weapons. Beyond them lies a vast valley with winding rivers, a distant city of pale stone near the centre, and on the right-hand horizon a colossal broken spire with a slow storm of light rising from its break. The spire is the distant threat. Keep the upper-left third as uncluttered, low-contrast sky with generous negative space for a future website title and countdown; do not paint any lettering there. Three depth planes: dark foreground ledge and party, expansive valley and pale city, mist-compressed horizon and sky. Keep the city, river bends, spire, cliff and party placement consistent so this is a style comparison of the same scene.
Strict palette: Void Bastion #141124 for violet-black shadow floor and cavity occlusion; Twilight Basalt #292643 for structural stone and iron shadows; Runeforged Steel #5C6478 for broad metallic bevels and resting neutrals; Lionheart Gold #D99B38 for chunky armour trim and warm highlights; Cinderforge Ember #FF6B35 for restrained warm accents; Runic Cyan #2EC4B6 for mana and shadow-side rim highlights; Astral Amethyst #B538F5 for arcane ribbons and crystal accents. Translate the pale city into light warm painted stone while retaining the palette's violet-cool shadow structure.
Lighting: overhead 45-degree warm amber-gold #D99B38 directional key illuminates helmets, shoulders and upper planes, grading darker toward boots. Rich chromatic #292643 to #141124 shadows, never neutral grey or pure black, with baked occlusion locked into armour seams and stone cracks. Thick hand-brushed 3 px #2EC4B6 or #FF6B35 highlights trace outer silhouettes of heroes and weapons. Magic uses graphic swirling ribbons and faceted crystals, opaque white-hot centres, saturated cyan #2EC4B6 and amethyst #B538F5 outer glow; use this same graphic treatment for the spire's slow light storm.
No loose impasto, no linen canvas texture, no misty oil-paint dissolution of silhouettes, no photorealism, no glossy plastic CGI, no anime outlines.
Output: one full-bleed PNG, landscape 16:9, at the largest native resolution available, target 3840 x 2160 pixels and at least 1536 pixels wide. No text, no lettering, no logos, no watermark, no painted border, no UI, no extra heroes. Do not render a triptych or multiple panels.
```

## `art/style/candidate-c.png` — Direction C: Vellum and Tempered Steel

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1672 × 941 px, PNG, native output (landscape, approximately 16:9).
- Attempts: 1. Retained after visual inspection; no remake.

Final prompt, verbatim:

```text
Use case: stylized-concept.
Asset type: pre-launch MMORPG website key art, Direction C — Vellum and Tempered Steel.
Prestige illustrated semi-realistic fantasy key art combining tactile weathered materials with fine structural ink accents and gouache washes on a unified warm vellum undertone. Believable functional armour and anatomy, restrained noble proportions, clean idealised illustrative grace. Hammered gunmetal, oiled leather straps, woven linen cloaks, intricate brass astrolabe filigree, weathered stone. Delicate ink contours and dry gouache plane breaks remain visibly drawn across the whole composition; subtle cross-hatching in folds and architectural shadows. Controlled editorial illustration, with finer craftsmanship and quieter edges than broad oil impasto.
Scene and composition (keep identical across the three style candidates): landscape 16:9, 24mm wide-angle vista from a fixed camera behind a party of exactly four heroes. On a dark, broken stone cliff ledge occupying the bottom third, the four heroes are seen from behind and in three-quarter view, all looking out across the continent of Kaelvorn. Arrange them left to right: a broad heavily armoured shield-bearer with a large shield; a slimmer cloaked spellblade with one glowing blade; a ranger holding a clearly visible bow, with one wolf-like beast companion beside the ranger; a floating robed arcanist with a staff, boots visibly lifted above the stone. Distinguish all four classes by silhouette alone; keep clear gaps between them and their weapons. Beyond them lies a vast valley with winding rivers, a distant city of pale stone near the centre, and on the right-hand horizon a colossal broken spire with a slow storm of light rising from its break. The spire is the distant threat. Keep the upper-left third as uncluttered, low-contrast sky with generous negative space for a future website title and countdown; do not paint any lettering there. Three depth planes: dark foreground ledge and party, expansive valley and pale city, mist-compressed horizon and sky. Keep the city, river bends, spire, cliff and party placement consistent so this is a style comparison of the same scene.
Strict palette: Charcoal Obsidian #121417 for deepest structural ink and shadow anchors; Tempered Gunmetal #262B30 for weathered armour and dark stone; Verdurous Slate #4A554E for sage-grey landscapes and cool ambient fill; Weathered Greystone #8C7A6B for earth, ruins and leather; Aged Vellum #DFD3C3 for warm ivory sky haze and the pale stone city; Astrolabe Brass #C59B48 for fine filigree and sun glints; Garnet Damask #8F242E for noble cloth and the spellblade's cloak; Celestial Aether #56B4E9 for rare crystalline magic and thin rim light. Keep most colours muted, with celestial blue and brass reserved for small luminous accents.
Lighting: high-altitude diffused silver-gold daylight #DFD3C3 tinted with #C59B48 cuts through mountain mist. Crisp anisotropic specular glints are translated into fine painted strokes on metal; soft warmth on any visible skin. Desaturated cool slate-green #4A554E to #262B30 ambient sky fill, delicate #121417 ink accents in deep folds and crevices. Fine razor-sharp #56B4E9 or #DFD3C3 rim traces hair, pauldrons and weapon edges. Magic is crystalline and geometric: fine astrolabe rings, refracting aether shards and #56B4E9 embers against the muted world; use this treatment for the slow storm from the broken spire.
No plastic CGI, no glossy 3D render, no photorealistic pores, no bloom-heavy cinematic render, no chunky cartoon proportions, no heavy oil impasto. Preserve the fine ink-and-gouache medium and visible vellum undertone without a paper border.
Output: one full-bleed PNG, landscape 16:9, at the largest native resolution available, target 3840 x 2160 pixels and at least 1536 pixels wide. No text, no lettering, no logos, no watermark, no painted border, no UI, no extra heroes. Do not render a triptych or multiple panels.
```


# Phase 2 — Gilded Chiaroscuro style anchors

Generated 2026-10-25 with built-in `image_gen.imagegen`; exact model revision is not exposed. Seven calls: four first attempts and one remake each for vista, creature and icons. No CLI/API fallback or Gemini image generation. The original candidate entries above are preserved.

Every submitted prompt starts with the 82-word fixed prefix in `docs/STYLE.md`, uses its category suffix and ends with the identical fixed avoid list. Every call used `art/style/candidate-a.png` as the sole visual style reference through `referenced_image_paths`, with `transparent_background: false`. Remakes were new generations referencing the candidate, not edits of the discarded attempt. Output requests are native targets; actual dimensions are recorded below. Selected PNGs were copied unchanged into `art/style/`; discarded attempts are not repository deliverables.

## `art/style/anchor-1-vista.png`

- Reference: `art/style/candidate-a.png` (medium, stroke scale, edge economy, palette and light only).
- Tool: built-in `image_gen.imagegen`.
- Actual native size: 1672 × 941 (approximately 16:9) px; opaque RGB PNG. Both attempts have the same dimensions where a remake exists.
- Attempts: 2; second retained.

### Attempt 1 — discarded

First attempt matched the oil surface but crowded the gorge with towers, copied too much city structure and raised the horizon; discarded after one remake.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

A region of Kaelvorn with no people, animals or figures: a winding river gorge, broken limestone viaduct and ancient terraced ruins, several waterfalls descending into mist. Golden light rakes the ruins on the middle-right; the river leads toward a distant pale ruin below the low horizon. Keep the upper-left third calm and largely empty. Foreground rocks use large indigo and umber stroke masses with sparse dry golden grass; avoid resolving every leaf or stone. Use the supplied candidate-a.png solely as the style reference for oil surface, stroke scale, edge economy, palette and lighting, not as a composition or subject template. Generate one new full-bleed PNG, exact landscape 16:9, target 2048 x 1152 pixels or the largest native equivalent.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: calmer sky, fewer ruins and broad foreground masses. The horizon remains nearer mid-height than the requested bottom third; the style match is strong.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

A region of Kaelvorn with no people, animals or figures: a winding river gorge, broken limestone viaduct and ancient terraced ruins, several waterfalls descending into mist. Golden light rakes the ruins on the middle-right; the river leads toward a distant pale ruin below the low horizon. Keep the upper-left third calm and largely empty. Foreground rocks use large indigo and umber stroke masses with sparse dry golden grass; avoid resolving every leaf or stone. Use the supplied candidate-a.png solely as the style reference for oil surface, stroke scale, edge economy, palette and lighting, not as a composition or subject template. Generate one new full-bleed PNG, exact landscape 16:9, target 2048 x 1152 pixels or the largest native equivalent.

Revision for composition only: put the distant river horizon at two thirds of image height, leaving the upper half predominantly calm, low-contrast indigo-grey and pale ochre sky. Use just a broken viaduct and one ruined terrace in the lower-right gorge; omit the distant city and crowded field of towers. Show a clear river and two principal waterfalls in the lower half. Group foreground stone into much larger dark brush masses with only a few ochre edges. Preserve the candidate's handmade oil medium, warm/cool light and atmosphere; do not copy the candidate's city layout.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/style/anchor-2-hero.png`

- Reference: `art/style/candidate-a.png` (medium, stroke scale, edge economy, palette and light only).
- Tool: built-in `image_gen.imagegen`.
- Actual native size: 1024 × 1536 (2:3) px; opaque RGB PNG. Both attempts have the same dimensions where a remake exists.
- Attempts: 1; retained.

### Attempt 1 — retained

Retained first attempt: good indigo steel, ochre impasto, crimson cloth and teal blade. Weaknesses: busy rivets, a large blade competing with the helmet and tighter framing than the nominal 70% height.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

One anonymous armoured wanderer of Kaelvorn, turned three-quarter toward the viewer, framed from head to just below the knees, with a wind-swept dark crimson cloak. A plain battered closed helmet conceals identity. Weathered indigo steel armour carries sparse tarnished-brass trim and broad ochre impasto glints. One gauntleted hand holds a single teal-enchanted sword diagonally upward beside the body; keep its whole blade, the head and both shoulders inside the image with clear separation. The other hand rests naturally near the belt. Paint a few large cloak folds, not intricate filigree. Empty slate-indigo painterly backdrop, no landscape, fading into #11151E at the edges and lower knees; readable silhouette without a painted border. Use the supplied candidate-a.png solely as the style reference for oil surface, stroke scale, edge economy, palette and lighting, not as a composition or subject template. Generate one PNG, exact portrait 2:3, target 1024 x 1536 pixels or the largest native equivalent.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/style/anchor-3-creature.png`

- Reference: `art/style/candidate-a.png` (medium, stroke scale, edge economy, palette and light only).
- Tool: built-in `image_gen.imagegen`.
- Actual native size: 1672 × 941 (approximately 16:9) px; opaque RGB PNG. Both attempts have the same dimensions where a remake exists.
- Attempts: 2; second retained.

### Attempt 1 — discarded

First attempt matched stone, light and magic but clipped the highest crystal and made the scale traveller too large; discarded after one remake.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

One boss-scale stone-and-crystal colossus of Kaelvorn, a towering asymmetrical ruin made animate, with massive chisel-cut limestone limbs, a compact head, and a few large translucent viridian crystal growths rising from one shoulder. Tight teal fissures and an incandescent chest core illuminate nearby stone with painted bounce; broken bristle-edged wisps dissolve into indigo mist. A single tiny anonymous cloaked traveller stands on a lower-left ledge at roughly one twentieth the creature's height to establish scale. Show the entire colossus, including feet and highest crystals, against a restrained river-gorge basin; do not crop its silhouette. Ochre upper-left shafts pick out its head and shoulder while the lower body stays grouped in indigo and umber shadow. Keep crystal forms painterly and roughly hewn rather than polished glass. Use the supplied candidate-a.png solely as the style reference for oil surface, stroke scale, edge economy, palette and lighting, not as a composition or subject template. Generate one new full-bleed PNG, exact landscape 16:9, target 2048 x 1152 pixels or the largest native equivalent.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: complete silhouette and clearer monumental scale. Weaknesses: top clearance remains below the requested 8%, the traveller remains larger than 1:20, and lower legs merge somewhat into the basin rock.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

One boss-scale stone-and-crystal colossus of Kaelvorn, a towering asymmetrical ruin made animate, with massive chisel-cut limestone limbs, a compact head, and a few large translucent viridian crystal growths rising from one shoulder. Tight teal fissures and an incandescent chest core illuminate nearby stone with painted bounce; broken bristle-edged wisps dissolve into indigo mist. A single tiny anonymous cloaked traveller stands on a lower-left ledge at roughly one twentieth the creature's height to establish scale. Show the entire colossus, including feet and highest crystals, against a restrained river-gorge basin; do not crop its silhouette. Ochre upper-left shafts pick out its head and shoulder while the lower body stays grouped in indigo and umber shadow. Keep crystal forms painterly and roughly hewn rather than polished glass. Use the supplied candidate-a.png solely as the style reference for oil surface, stroke scale, edge economy, palette and lighting, not as a composition or subject template. Generate one new full-bleed PNG, exact landscape 16:9, target 2048 x 1152 pixels or the largest native equivalent.

Revision for full silhouette and scale only: zoom the camera out until every crystal tip and both feet have at least eight percent image-height clearance from the top and bottom edges. The entire colossus including crystals must fit inside the central eighty-four percent of image height. Make the lone traveller extremely small, about one twentieth of the colossus height, on the lower-left ledge. Reduce decorative micro-ruins on the body into broad chisel-cut stone masses, retaining just a few ancient arches. Preserve the candidate's handmade oil medium, golden light, indigo shadows and teal painted magic.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/style/anchor-4-icons.png`

- Reference: `art/style/candidate-a.png` (medium, stroke scale, edge economy, palette and light only).
- Tool: built-in `image_gen.imagegen`.
- Actual native size: 1254 × 1254 (1:1) px; opaque RGB PNG. Both attempts have the same dimensions where a remake exists.
- Attempts: 2; second retained.

### Attempt 1 — discarded

First attempt contained all twelve subjects but some paint approached or crossed nominal row gutters; discarded after one remake.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

A square 4-column by 3-row sheet of exactly twelve independent skill-icon paintings, with equal cell spacing, even empty gutters, and no grid lines. Each cell contains just one centred large readable subject; all twelve cells use identical flat #0B0D12 backgrounds right to the outer edges. Place these subjects in row-major order: row 1, a tarnished-brass shield, a sword with a tight teal flame, a curved bow without arrows, a staff orb represented by one orb on a short staff tip; row 2, a single healing hand with teal light in its palm, one abstract nonlinguistic rune, an arrow volley represented by three parallel arrows as one compact diagonal symbol, one bold spiral storm; row 3, a simple crown, a squat potion bottle, a broad-headed hammer, one sweeping feather. Each subject fills 70–80% of its own cell with comfortable dark clearance, with thick hard-edged palette-knife highlights and reduced internal detail. Use restrained ochre and tarnished brass against indigo, teal for magical accents, occasional crimson cloth or potion detail. Keep glow inside each cell and retain a clear 48 px silhouette; no number labels, no captions, no ornamental frames, no continuous scene. Use the supplied candidate-a.png solely as the style reference for oil surface, impasto, palette and lighting; deliberately tighten its loose edges for tiny icon readability. Generate one PNG, exact square 1:1, target 2048 x 2048 pixels or the largest native equivalent.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: correct subjects and row-major order, more separate silhouettes, simpler crown and bow. Weaknesses: background is near-flat rather than exact #0B0D12, gutters are approximate, and small trim and the bowstring lose detail at 48 px.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

A square 4-column by 3-row sheet of exactly twelve independent skill-icon paintings, with equal cell spacing, even empty gutters, and no grid lines. Each cell contains just one centred large readable subject; all twelve cells use identical flat #0B0D12 backgrounds right to the outer edges. Place these subjects in row-major order: row 1, a tarnished-brass shield, a sword with a tight teal flame, a curved bow without arrows, a staff orb represented by one orb on a short staff tip; row 2, a single healing hand with teal light in its palm, one abstract nonlinguistic rune, an arrow volley represented by three parallel arrows as one compact diagonal symbol, one bold spiral storm; row 3, a simple crown, a squat potion bottle, a broad-headed hammer, one sweeping feather. Each subject fills 70–80% of its own cell with comfortable dark clearance, with thick hard-edged palette-knife highlights and reduced internal detail. Use restrained ochre and tarnished brass against indigo, teal for magical accents, occasional crimson cloth or potion detail. Keep glow inside each cell and retain a clear 48 px silhouette; no number labels, no captions, no ornamental frames, no continuous scene. Use the supplied candidate-a.png solely as the style reference for oil surface, impasto, palette and lighting; deliberately tighten its loose edges for tiny icon readability. Generate one PNG, exact square 1:1, target 2048 x 2048 pixels or the largest native equivalent.

Revision for layout and background only: treat the square as four equal columns and three equal rows. Every subject and all glow must stay strictly within the middle seventy percent of its cell width and height, leaving generous continuous empty gutters; no subject may cross a row boundary. The hammer belongs entirely inside the bottom row. Place each subject inside an imaginary square within its rectangular cell so later square crops retain the complete object. Background, all gutters and outer margin must be one uniform flat #0B0D12 with no grain, no vignette, no gradients and no background brush marks. Simplify embellishments on shield, bow and crown to strengthen the 48 px silhouettes. Preserve candidate-matched oil impasto on the objects only.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

# Phase 5 — The six regions

All prompts below follow `docs/STYLE.md` assembly: verbatim fixed prefix, verbatim Key art and regions suffix, regional subject and reference/output instructions, then the verbatim fixed avoid list. Existing ledger entries are preserved.

- Tool: built-in `image_gen.imagegen`; no CLI/API fallback.
- Model: identifier and revision are not exposed by this tool. No more specific model attribution is asserted.
- References for every attempt, in order: `art/style/candidate-a.png` (primary medium, stroke scale, edge economy, palette and light) and `art/style/anchor-1-vista.png` (atmosphere, stone and foreground mass). Both are style references, not edit targets.
- Requested size for every attempt: largest native landscape 16:9, target 3840 × 2160. Actual size for all nine attempts: 1672 × 941 px, native RGB opaque PNG, approximately 16:9. The tool exposes no explicit resolution parameter and did not return the requested target dimensions. Final assets retain native pixels without resizing, cropping, recolouring or texture overlays.
- Review: each result was viewed at native size and about 300 px wide, comparing medium, subject, silhouette, light, text/marks and framing. No visible text, lettering, logos, watermark or painted border in retained images. No people; the Fen's bronze human forms and the dunes' face are statues. No visible broken turtle or statue anatomy.
- Palette check: visually compared to both references and sampled native RGB pixels. Colours are mixed rather than exact hex replacements. For example, Sun-Steppe foreground at (30,900) is RGB (37,42,49), Frost-Chime at (70,850) is (35,39,47), and dunes twilight at (1100,350) is (109,83,115). Some small warm foreground crevices fall darker than the intended #11151E shadow floor; broad forms retain legibility. Peripheral fading is uneven rather than a uniform vignette. The upper-left sky often remains brighter and more active than the category's ideal text reserve.
- Remakes: Sun-Steppe 0; Fen 0; Brass-Coast 0; Singing Dunes 1; Frost-Chime 0; Shattered Crown 2. Nine generations total; only the six selected final assets are repository deliverables.

## `art/regions/sun-steppe-of-aethel.png`

- File: `art/regions/sun-steppe-of-aethel.png`.
- Tool: `image_gen.imagegen`.
- Model: not exposed by the built-in tool.
- Size: 1672 × 941 px, opaque RGB PNG, native approximately 16:9 (every attempt).
- References: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`.
- Re-makes: 0; first attempt retained.

Final review: Strong match to the candidate's ochre knife edges, linen-like sky, dry-brushed limestone and indigo depth. Golden terraces, bronze-inlaid road, Viaduct of Ten Chords, ivory domes, hanging bells and amber Canopy bands are present; no figures. At 300 px the road and bell-bridge remain clear, while city detail softens. Weakest point: the distant horizon is near mid-height, above the specified bottom third; upper-left sky is brighter and busier than ideal for future text. Retained first attempt.

### Attempt 1 — retained

Strong match to the candidate's ochre knife edges, linen-like sky, dry-brushed limestone and indigo depth. Golden terraces, bronze-inlaid road, Viaduct of Ten Chords, ivory domes, hanging bells and amber Canopy bands are present; no figures. At 300 px the road and bell-bridge remain clear, while city detail softens. Weakest point: the distant horizon is near mid-height, above the specified bottom third; upper-left sky is brighter and busier than ideal for future text. Retained first attempt.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

The Sun-Steppe of Aethel in Kaelvorn: a sweeping Mediterranean vista of terraced golden sun-grain and wheat fields, sparse olive groves and white limestone karst cliffs stepping down toward the western sea. A cobbled resonant highway inlaid with gleaming tarnished-bronze strips enters from the dark lower-left foreground, crosses the fortified pale-stone Viaduct of Ten Chords and leads toward High Solitude, a sunlit ivory city of domes and giant hanging bronze bells on the middle-right terraces of Alabaster Reach. Make the domes and several open belfries with large suspended bells unmistakable, but group minor architecture into simple planes. A pale-stone and bronze aqueduct carries golden water across a lower terrace; the distant Beacon of Dawn-Watch is a small coastal tower. Above, a gently turquoise, indigo-mixed sky is arched by a few distant glowing amber stone bands of the shattered Canopy, not neon beams. Sunward grain and cliff edges take thick ochre impasto; the dark foreground contains broad rocky masses and dry grass. The bronze road, domed city, hanging bells and amber Canopy establish the region rather than the reference's gorge and waterfalls. Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, broad bristle stroke scale, edge economy, palette and warm/cool lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric depth, dry-brushed stone and large foreground masses. Both are style references only, not edit targets or geography templates. Invent this region's composition; do not inherit their party, city or broken spire. Keep roughly sixty percent resting neutrals, thirty percent regional structure, and at most ten percent high-saturation accents, with distance compressed into haze. No people. Preserve a quiet upper-left area, three readable depth planes and a low distant horizon; tall defining landmarks may rise on the right. Generate one new full-bleed opaque PNG, landscape 16:9, at the largest native size available, target 3840 x 2160 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/regions/whispering-fen-root-basin.png`

- File: `art/regions/whispering-fen-root-basin.png`.
- Tool: `image_gen.imagegen`.
- Model: not exposed by the built-in tool.
- Size: 1672 × 941 px, opaque RGB PNG, native approximately 16:9 (every attempt).
- References: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`.
- Re-makes: 0; first attempt retained.

Final review: Candidate-matched bristle bark, warm amber glints, cool mist and painted turquoise water; roots, lantern suspension bridges, drowned bronze statues, two giant snapping turtles and Spire Verdan are present. At 300 px the nearer turtle, bridge and lanterns remain readable; submerged limbs and the distant turtle are less distinct. No visible anatomy errors; statues are intentional archaeological objects. Weakest point: more sunlit and open than the lore's perpetual twilight, and the fine settlement detail is busy. Retained first attempt.

### Attempt 1 — retained

Candidate-matched bristle bark, warm amber glints, cool mist and painted turquoise water; roots, lantern suspension bridges, drowned bronze statues, two giant snapping turtles and Spire Verdan are present. At 300 px the nearer turtle, bridge and lanterns remain readable; submerged limbs and the distant turtle are less distinct. No visible anatomy errors; statues are intentional archaeological objects. Weakest point: more sunlit and open than the lore's perpetual twilight, and the fine settlement detail is busy. Retained first attempt.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

The Whispering Fen and Root-Basin in Kaelvorn: an immense misty subtropical flooded forest with cathedral-scale ironwood and banyan trees. Enormous buttressed roots frame the left and right edges, their bark dry-brushed umber with indigo shadows, not a decorative painted frame. Turquoise water winds into a low distant opening in the forest and reflects sparse hanging lanterns of warm amber glass. Wooden suspension bridges cross about thirty feet above the moss, linking the restrained branch-built township of Root-Cradle on the right. Show two giant turquoise-shelled snapping turtles wading through the water below the bridges, one nearer middle-right and one much smaller in the distance; broad rough shells, beaked heads and anatomically natural low reptilian limbs, no riders. Weathered bronze statues stand half-submerged near the overgrown Drowned Conservatory, their details reduced by moss and mist. Farther back, Spire Verdan is a modest basalt-and-bronze tower choked with crystal vines; a distant cascade suggests the Singing Cataracts. Keep the open upper-left canopy mist quiet and low-contrast. Warm upper-left light breaks sparingly through the canopy onto amber lantern glass and roots. The turquoise wetland is a muted reflected colour with only tiny near-white/viridian spore-lights, not an overall neon wash. Emphasize wetland scale, bridges, warm lanterns, turtles and drowned bronze over busy jungle detail. Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, broad bristle stroke scale, edge economy, palette and warm/cool lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric depth, dry-brushed stone and large foreground masses. Both are style references only, not edit targets or geography templates. Invent this region's composition; do not inherit their party, city or broken spire. Keep roughly sixty percent resting neutrals, thirty percent regional structure, and at most ten percent high-saturation accents, with distance compressed into haze. No people. Preserve a quiet upper-left area, three readable depth planes and a low distant horizon; tall defining landmarks may rise on the right. Generate one new full-bleed opaque PNG, landscape 16:9, at the largest native size available, target 3840 x 2160 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/regions/cinder-reach-brass-coast.png`

- File: `art/regions/cinder-reach-brass-coast.png`.
- Tool: `image_gen.imagegen`.
- Model: not exposed by the built-in tool.
- Size: 1672 × 941 px, opaque RGB PNG, native approximately 16:9 (every attempt).
- References: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`.
- Re-makes: 0; first attempt retained.

Final review: Broad impasto basalt and surf match the references, with weathered copper domes, brass turbines, small furnace cores, pipelines and a fully visible wooden airship tethered at a cliffside crane. At 300 px the coast and airship silhouettes read; turbine blades and crane rigging soften. Weakest point: sunset dominates the requested twilight and the dense terraced city contains more small architectural marks than ideal. Retained first attempt.

### Attempt 1 — retained

Broad impasto basalt and surf match the references, with weathered copper domes, brass turbines, small furnace cores, pipelines and a fully visible wooden airship tethered at a cliffside crane. At 300 px the coast and airship silhouettes read; turbine blades and crane rigging soften. Weakest point: sunset dominates the requested twilight and the dense terraced city contains more small architectural marks than ideal. Retained first attempt.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

The Cinder-Reach and Brass-Coast in Kaelvorn: a dramatic twilight volcanic coastline, hexagonal black basalt columns descending into foamy indigo waves of the Churn. The low open sea horizon lies on the bottom third toward the left; a rocky foreground ledge and broad surf masses establish depth. On the middle-right headland rises Brass-Harbor, a sprawling terraced industrial foundry-city of weathered riveted copper domes, tarnished brass pipelines, sparse glowing orange blast-furnace mouths and large brass wind-turbines with clearly separated blades. A wooden-hulled airship with a plain lifting envelope is tethered by visible mooring ropes to one immense cliffside crane, its full silhouette readable against the sky. A larger furnace complex suggests the Great Smeltery of Caul, with restrained smoke and geothermal steam drifting inland toward Cinder-Crag. A distant inlet can suggest the grounded Wreck of the Sky-Titan without competing with the tethered airship. Low upper-left ochre sunlight breaks below the twilight cloud cover, cutting copper and basalt into broad light planes against indigo fill. Warm furnace cores remain small and painted; no chrome, neon or modern machinery. Prioritize the recognizable columnar basalt, stormy surf, copper foundry terraces, brass turbines and moored timber airship. Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, broad bristle stroke scale, edge economy, palette and warm/cool lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric depth, dry-brushed stone and large foreground masses. Both are style references only, not edit targets or geography templates. Invent this region's composition; do not inherit their party, city or broken spire. Keep roughly sixty percent resting neutrals, thirty percent regional structure, and at most ten percent high-saturation accents, with distance compressed into haze. No people. Preserve a quiet upper-left area, three readable depth planes and a low distant horizon; tall defining landmarks may rise on the right. Generate one new full-bleed opaque PNG, landscape 16:9, at the largest native size available, target 3840 x 2160 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/regions/singing-dunes-of-kal-zir.png`

- File: `art/regions/singing-dunes-of-kal-zir.png`.
- Tool: `image_gen.imagegen`.
- Model: not exposed by the built-in tool.
- Size: 1672 × 941 px, opaque RGB PNG, native approximately 16:9 (every attempt).
- References: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`.
- Re-makes: 1; attempt 2 retained; reasons below.

Final review: The retained remake keeps the candidate's raised ochre crests and indigo rock masses while adding copper/rose sand and a genuinely violet-indigo sky. One timber sand-skiff has three separate masts and saffron sails, an amber wake and a half-buried patina-green statue head with its exposed silhouette inside the image. Distant ziggurat and arches remain subordinate. At 300 px the skiff sails, head and dune masses read, but rigging and individual mast detail soften. Weakest point: the far horizon remains above the bottom third and the warm dune highlights occupy a larger share than the nominal accent budget. Retained attempt 2.

### Attempt 1 — discarded

Discarded attempt 1: oil medium, copper dunes, three-masted skiff and green-patina head were convincing, but the head's exposed right side pressed into the edge and the sky was too sunset-orange. Remade to improve clearance, deepen violet twilight and simplify distant ruins.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

The Singing Dunes of Kal-Zir in Kaelvorn: endless broad rolling dunes of metallic rose-gold and copper sand, the rose tint mixed from muted umber and restrained crimson, beneath a deep violet-indigo twilight sky. Low ochre upper-left sunlight still rakes the dune crests, with broad cool troughs and linen-tooth haze. Exactly one three-masted wooden sand-skiff with three clearly separate mast silhouettes and wind-filled saffron sails glides across the middle-right dune face, carving a narrow glowing amber wake through vibrating bronze-and-amber-quartz sand. The skiff has a sleek complete wooden hull and sand-running keel; no ocean or water around it, no people on deck, no flags or insignia. It passes the half-buried head of one colossal patina-green bronze statue, whose naturally proportioned worn face and crownless broad brow emerge from copper dunes; this archaeological head is the secondary focal landmark, not a living giant. Farther back, the low half-sunken tiers of the Sunken Ziggurat of Kal and wind-carved sandstone arches at Wind-Harp Canyon recede through sand haze; a very small oasis under Leviathan ribs suggests Mirage-Bazaar. Glass-floored canyon glints stay tiny. Keep the left sky calm and the dunes simple; make saffron sails, three masts, copper sand and ancient green-patina head read clearly at 300 pixels. Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, broad bristle stroke scale, edge economy, palette and warm/cool lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric depth, dry-brushed stone and large foreground masses. Both are style references only, not edit targets or geography templates. Invent this region's composition; do not inherit their party, city or broken spire. Keep roughly sixty percent resting neutrals, thirty percent regional structure, and at most ten percent high-saturation accents, with distance compressed into haze. No people. Preserve a quiet upper-left area, three readable depth planes and a low distant horizon; tall defining landmarks may rise on the right. Generate one new full-bleed opaque PNG, landscape 16:9, at the largest native size available, target 3840 x 2160 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

The retained remake keeps the candidate's raised ochre crests and indigo rock masses while adding copper/rose sand and a genuinely violet-indigo sky. One timber sand-skiff has three separate masts and saffron sails, an amber wake and a half-buried patina-green statue head with its exposed silhouette inside the image. Distant ziggurat and arches remain subordinate. At 300 px the skiff sails, head and dune masses read, but rigging and individual mast detail soften. Weakest point: the far horizon remains above the bottom third and the warm dune highlights occupy a larger share than the nominal accent budget. Retained attempt 2.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

The Singing Dunes of Kal-Zir in Kaelvorn: endless broad rolling dunes of metallic rose-gold and copper sand, the rose tint mixed from muted umber and restrained crimson, beneath a deep violet-indigo twilight sky. Low ochre upper-left sunlight still rakes the dune crests, with broad cool troughs and linen-tooth haze. Exactly one three-masted wooden sand-skiff with three clearly separate mast silhouettes and wind-filled saffron sails glides across the middle-right dune face, carving a narrow glowing amber wake through vibrating bronze-and-amber-quartz sand. The skiff has a sleek complete wooden hull and sand-running keel; no ocean or water around it, no people on deck, no flags or insignia. It passes the half-buried head of one colossal patina-green bronze statue, whose naturally proportioned worn face and crownless broad brow emerge from copper dunes; this archaeological head is the secondary focal landmark, not a living giant. Farther back, the low half-sunken tiers of the Sunken Ziggurat of Kal and wind-carved sandstone arches at Wind-Harp Canyon recede through sand haze; a very small oasis under Leviathan ribs suggests Mirage-Bazaar. Glass-floored canyon glints stay tiny. Keep the left sky calm and the dunes simple; make saffron sails, three masts, copper sand and ancient green-patina head read clearly at 300 pixels. Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, broad bristle stroke scale, edge economy, palette and warm/cool lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric depth, dry-brushed stone and large foreground masses. Both are style references only, not edit targets or geography templates. Invent this region's composition; do not inherit their party, city or broken spire. Keep roughly sixty percent resting neutrals, thirty percent regional structure, and at most ten percent high-saturation accents, with distance compressed into haze. No people. Preserve a quiet upper-left area, three readable depth planes and a low distant horizon; tall defining landmarks may rise on the right. Generate one new full-bleed opaque PNG, landscape 16:9, at the largest native size available, target 3840 x 2160 pixels.

Revision after first-attempt review: preserve the clear three-masted saffron-sailed wooden sand-skiff, copper dunes and half-buried patina-green statue head. Zoom out enough that the entire exposed statue head, including both sides of its cranium, has at least eight percent image-width clearance from the right edge. Keep its buried lower part beneath sand. Reduce the distant ruins to a few broad silhouettes and shift the low far horizon to two thirds of image height. Make the upper half predominantly deep muted violet-indigo twilight, with only a narrow low warm horizon and restrained upper-left ochre grazing light on dune edges, rather than a broad orange sunset. Preserve the reference-matched visible oil strokes and the small amber wake, not smooth gradients.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/regions/frost-chime-peaks.png`

- File: `art/regions/frost-chime-peaks.png`.
- Tool: `image_gen.imagegen`.
- Model: not exposed by the built-in tool.
- Size: 1672 × 941 px, opaque RGB PNG, native approximately 16:9 (every attempt).
- References: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`.
- Re-makes: 0; first attempt retained.

Final review: Strong reference match in bristle snow planes, indigo granite and ochre brass edges; blue-shadowed snow and glacier, enormous fortress wind-wall, clear open-mouthed organ pipes, warm fire and silver aurora are present. At 300 px the pipes and cold/warm contrast remain clear; monastery and glacier crevasse details merge. Weakest point: the warm left sky is bright for a twilight aurora scene and the organ pipes are a little more polished than the surrounding stone. Retained first attempt.

### Attempt 1 — retained

Strong reference match in bristle snow planes, indigo granite and ochre brass edges; blue-shadowed snow and glacier, enormous fortress wind-wall, clear open-mouthed organ pipes, warm fire and silver aurora are present. At 300 px the pipes and cold/warm contrast remain clear; monastery and glacier crevasse details merge. Weakest point: the warm left sky is bright for a twilight aurora scene and the organ pipes are a little more polished than the surrounding stone. Retained first attempt.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

The Frost-Chime Peaks in Kaelvorn: jagged granite mountain ridges and blue-shadowed snow above a vast glacial valley with sapphire-indigo crevasses. In the middle-right mountain pass, the massive fortress walls of the Boreal Wind-Wall bridge two ridges and are built around hundred-foot-tall tarnished-brass organ pipes, a monumental architectural wind-organ rather than a church facade. Show several clearly recognizable parallel cylindrical pipes with open round mouths and staggered heights, their sunward edges catching thick ochre strokes. Warm orange brazier fires glow in a few wall recesses and at the pipe bases, suggesting the warming harmonics of the Boreal Pipes and Iron-Hearth Hold. A small secluded Frost-Bell Monastery sits on a secondary ledge; the Glacier of Frozen Echoes descends below in broad cold planes, with a few unnaturally crystalline spires far to the north. Silver-white auroral ribbons swirl gently across the indigo sky, painted with broken brush edges and muted silver rather than fluorescent green. Upper-left low sunlight warms only the highest snow and brass edges; keep a quiet low-contrast left sky and a low distant valley horizon, while the alpine peaks rise on the right. Dark foreground granite and snow ledges establish scale. Prioritize the fortress spanning the glacial pass, towering brass organ pipes, warm brazier accents, blue snow and silver aurora. Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, broad bristle stroke scale, edge economy, palette and warm/cool lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric depth, dry-brushed stone and large foreground masses. Both are style references only, not edit targets or geography templates. Invent this region's composition; do not inherit their party, city or broken spire. Keep roughly sixty percent resting neutrals, thirty percent regional structure, and at most ten percent high-saturation accents, with distance compressed into haze. No people. Preserve a quiet upper-left area, three readable depth planes and a low distant horizon; tall defining landmarks may rise on the right. Generate one new full-bleed opaque PNG, landscape 16:9, at the largest native size available, target 3840 x 2160 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/regions/shattered-crown.png`

- File: `art/regions/shattered-crown.png`.
- Tool: `image_gen.imagegen`.
- Model: not exposed by the built-in tool.
- Size: 1672 × 941 px, opaque RGB PNG, native approximately 16:9 (every attempt).
- References: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`.
- Re-makes: 2; attempt 3 retained; reasons below.

Final review: The retained second remake preserves handmade oil strokes, indigo/ochre polarity and a contained silver-white eruption. Sol-Vara is ruptured, basalt slabs and bronze gears visibly float, branching crystal trees rise from pale vitrified plains, and Last Accord is small. The full tower and storm have sky clearance, though less than the requested fifteen percent. At 300 px the eruption and floating forms read strongly; crystal trees become a pale fine pattern and only two large gears are clearly evident despite the requested three. Weakest point: the porcelain landscape can read as snow, with very restrained local iridescence; the distant horizon remains above the bottom third. Retained attempt 3.

### Attempt 1 — discarded

Discarded attempt 1: style, floating slabs and gears matched, but the crystal forest read as upright spikes, the storm was too saturated teal and its upper spiral met the top edge. Remade for branching crystal trees, porcelain flats, silver-white radiance and complete eruption clearance.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

The Shattered Crown in Kaelvorn: a haunting storm-lashed highland crater, a wasteland of white vitrified porcelain plains and the crystalline trees of the Porcelain Woods, with deep indigo shadows and dry-brushed chipped surfaces. The crystal branches catch tiny restrained prismatic flecks, mostly ochre, pale silver and viridian; iridescence is local to the crystal facets, never a rainbow lighting wash. Huge slabs of black basalt and several broken tarnished-bronze gears float in mid-air with obvious empty air beneath and between them, forming fragments of the Hanging Causeway. At the middle-right stands Sol-Vara, the colossal mile-high ruptured First Spire: a monumental broken bronze-and-basalt tower with a visibly torn upper structure, erupting into a swirling pillar of blinding silver-white radiance, the Pale Wake. Paint the storm as broad impasto spirals with a near-white core, tight restrained viridian corona and indigo falloff, with painted bounce on adjacent stone, not glossy CGI or neon. The entire defining tower and radiant eruption fit with clear air inside the image. A very small fortified encampment of Last Accord lies on the southern crater rim, without visible people. Keep the distant crater floor on a low horizon, quiet storm haze in the upper-left, dark broken foreground basalt, compressed porcelain middle distance, and a sharp focal rupture against the sky. Prioritize the broken tower, floating basalt and bronze gears, porcelain terrain and crystal forest; do not copy the reference candidate's city or party. Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, broad bristle stroke scale, edge economy, palette and warm/cool lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric depth, dry-brushed stone and large foreground masses. Both are style references only, not edit targets or geography templates. Invent this region's composition; do not inherit their party, city or broken spire. Keep roughly sixty percent resting neutrals, thirty percent regional structure, and at most ten percent high-saturation accents, with distance compressed into haze. No people. Preserve a quiet upper-left area, three readable depth planes and a low distant horizon; tall defining landmarks may rise on the right. Generate one new full-bleed opaque PNG, landscape 16:9, at the largest native size available, target 3840 x 2160 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — discarded

Discarded attempt 2: branching crystal trees, flatter porcelain ground and silver-white storm improved, but the storm still ran into the top edge. Remade once more for a compact contained eruption with quiet sky above it.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

The Shattered Crown in Kaelvorn: a haunting storm-lashed highland crater, a wasteland of white vitrified porcelain plains and the crystalline trees of the Porcelain Woods, with deep indigo shadows and dry-brushed chipped surfaces. The crystal branches catch tiny restrained prismatic flecks, mostly ochre, pale silver and viridian; iridescence is local to the crystal facets, never a rainbow lighting wash. Huge slabs of black basalt and several broken tarnished-bronze gears float in mid-air with obvious empty air beneath and between them, forming fragments of the Hanging Causeway. At the middle-right stands Sol-Vara, the colossal mile-high ruptured First Spire: a monumental broken bronze-and-basalt tower with a visibly torn upper structure, erupting into a swirling pillar of blinding silver-white radiance, the Pale Wake. Paint the storm as broad impasto spirals with a near-white core, tight restrained viridian corona and indigo falloff, with painted bounce on adjacent stone, not glossy CGI or neon. The entire defining tower and radiant eruption fit with clear air inside the image. A very small fortified encampment of Last Accord lies on the southern crater rim, without visible people. Keep the distant crater floor on a low horizon, quiet storm haze in the upper-left, dark broken foreground basalt, compressed porcelain middle distance, and a sharp focal rupture against the sky. Prioritize the broken tower, floating basalt and bronze gears, porcelain terrain and crystal forest; do not copy the reference candidate's city or party. Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, broad bristle stroke scale, edge economy, palette and warm/cool lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric depth, dry-brushed stone and large foreground masses. Both are style references only, not edit targets or geography templates. Invent this region's composition; do not inherit their party, city or broken spire. Keep roughly sixty percent resting neutrals, thirty percent regional structure, and at most ten percent high-saturation accents, with distance compressed into haze. No people. Preserve a quiet upper-left area, three readable depth planes and a low distant horizon; tall defining landmarks may rise on the right. Generate one new full-bleed opaque PNG, landscape 16:9, at the largest native size available, target 3840 x 2160 pixels.

Revision after first-attempt review: replace the upright crystal clusters with recognizable branching crystalline trees: trunks split into angular bare boughs and smaller branches, a sparse Porcelain Woods on the white vitrified plains. Use broad porcelain flats with only a few fissures instead of repeating the reference's waterfall gorge. Zoom out and lower the entire broken tower plus swirling eruption until both fit completely within the central eighty percent of image height, with clear sky above the highest luminous spiral. The radiance must be predominantly silver-white with just a tight thin viridian edge, not a large saturated teal cyclone. Keep floating basalt slabs and broken bronze gears clearly separate in empty air. Reduce gear count to three and keep all three complete. Keep Last Accord tiny, no figures; maintain large linen-tooth bristle planes, ochre side light and indigo depth.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 3 — retained

The retained second remake preserves handmade oil strokes, indigo/ochre polarity and a contained silver-white eruption. Sol-Vara is ruptured, basalt slabs and bronze gears visibly float, branching crystal trees rise from pale vitrified plains, and Last Accord is small. The full tower and storm have sky clearance, though less than the requested fifteen percent. At 300 px the eruption and floating forms read strongly; crystal trees become a pale fine pattern and only two large gears are clearly evident despite the requested three. Weakest point: the porcelain landscape can read as snow, with very restrained local iridescence; the distant horizon remains above the bottom third. Retained attempt 3.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

The Shattered Crown in Kaelvorn: a haunting storm-lashed highland crater, a wasteland of white vitrified porcelain plains and the crystalline trees of the Porcelain Woods, with deep indigo shadows and dry-brushed chipped surfaces. The crystal branches catch tiny restrained prismatic flecks, mostly ochre, pale silver and viridian; iridescence is local to the crystal facets, never a rainbow lighting wash. Huge slabs of black basalt and several broken tarnished-bronze gears float in mid-air with obvious empty air beneath and between them, forming fragments of the Hanging Causeway. At the middle-right stands Sol-Vara, the colossal mile-high ruptured First Spire: a monumental broken bronze-and-basalt tower with a visibly torn upper structure, erupting into a swirling pillar of blinding silver-white radiance, the Pale Wake. Paint the storm as broad impasto spirals with a near-white core, tight restrained viridian corona and indigo falloff, with painted bounce on adjacent stone, not glossy CGI or neon. The entire defining tower and radiant eruption fit with clear air inside the image. A very small fortified encampment of Last Accord lies on the southern crater rim, without visible people. Keep the distant crater floor on a low horizon, quiet storm haze in the upper-left, dark broken foreground basalt, compressed porcelain middle distance, and a sharp focal rupture against the sky. Prioritize the broken tower, floating basalt and bronze gears, porcelain terrain and crystal forest; do not copy the reference candidate's city or party. Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, broad bristle stroke scale, edge economy, palette and warm/cool lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric depth, dry-brushed stone and large foreground masses. Both are style references only, not edit targets or geography templates. Invent this region's composition; do not inherit their party, city or broken spire. Keep roughly sixty percent resting neutrals, thirty percent regional structure, and at most ten percent high-saturation accents, with distance compressed into haze. No people. Preserve a quiet upper-left area, three readable depth planes and a low distant horizon; tall defining landmarks may rise on the right. Generate one new full-bleed opaque PNG, landscape 16:9, at the largest native size available, target 3840 x 2160 pixels.

Revision after first-attempt review: replace the upright crystal clusters with recognizable branching crystalline trees: trunks split into angular bare boughs and smaller branches, a sparse Porcelain Woods on the white vitrified plains. Use broad porcelain flats with only a few fissures instead of repeating the reference's waterfall gorge. Zoom out and lower the entire broken tower plus swirling eruption until both fit completely within the central eighty percent of image height, with clear sky above the highest luminous spiral. The radiance must be predominantly silver-white with just a tight thin viridian edge, not a large saturated teal cyclone. Keep floating basalt slabs and broken bronze gears clearly separate in empty air. Reduce gear count to three and keep all three complete. Keep Last Accord tiny, no figures; maintain large linen-tooth bristle planes, ochre side light and indigo depth.

Second revision for silhouette clearance only: compose Sol-Vara and its entire luminous storm as one compact, fully bounded shape on the middle-right. The highest wisp must begin at least fifteen percent of the image height below the top edge; the rightmost wisp must stop at least fifteen percent of image width before the right edge. Show uninterrupted quiet dark sky above and to the right of the entire eruption. The tower plus complete storm together occupy no more than sixty percent of total image height. Keep the storm in a contained vertical twisting column above the rupture, not a huge horizontal cyclone spanning beyond the canvas. Preserve branching crystalline trees, porcelain plains, three bronze gears and floating basalt, the broad oil-painted surface and silver-white light with restrained teal accents.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

# Phase 5 — nine teaser character splashes

All images use `art/style/candidate-a.png` and `art/style/anchor-2-hero.png`, in that order, as style references only. Tool: built-in `image_gen.imagegen`; model: `gpt-image` (PNG provenance; exact model revision is not exposed). Every call requested the largest native 2:3 output, targeting 2304 × 3456 px. Every attempt returned 1024 × 1536 px, opaque RGB PNG. Final files are copied native outputs without resizing, cropping, recolouring or texture overlays. All fourteen attempts were visually reviewed; the nine saved finals were inspected at full native size and at 300 × 450 px card size. No visible text, logos, watermarks, painted frames, obvious extra limbs or broken faces were found. Five images received one remake each; none exceeded the two-remake limit.

## `art/characters/ness-quin/splash.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1024 × 1536 px (2:3), native opaque RGB PNG; all attempts.
- References: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (style only).
- Attempts: 2; re-makes: 1. First attempt clipped the left sunlight wing and overfilled the portrait; remade once for compact wings and complete lance clearance.
- Full-size and 300 px review: Retained remake: candidate-like bristle planes and ochre impasto; espresso skin, platinum crown braids, white-and-gold plate, cobalt feather cape, downward amber spiral lance and two geometric light wings are clear at 300 px. Weakest point: the foreshortened lance dominates the card and its twelve-foot length cannot be judged; the armour is more jagged than sleek fluting.

### Attempt 1 — discarded

First attempt clipped the left sunlight wing and overfilled the portrait; remade once for compact wings and complete lance clearance.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A tall, regal human woman in her early thirties with dark espresso skin, high cheekbones, and a braided crown of platinum-blonde hair, clad in sleek, aerodynamic white-and-gold fluted plate armor with a cape of cobalt-blue feathers; she is captured suspended in mid-air above a cliff edge, both hands gripping a twelve-foot spiral lance of burnished gold and glowing amber glass aimed downward as two blazing wings of geometric sunlight unfurl from her shoulder-guards. Keep both distinct geometric sunlight wings fully inside the portrait margins, with compact swept-back shapes behind the shoulders and the blue feather cape separate beneath. Foreshorten the very long lance diagonally downward into the picture so its complete amber-glass spiral point and both gripping gauntlets are visible. Hint at a cliff edge only in a few low-contrast lower strokes. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: candidate-like bristle planes and ochre impasto; espresso skin, platinum crown braids, white-and-gold plate, cobalt feather cape, downward amber spiral lance and two geometric light wings are clear at 300 px. Weakest point: the foreshortened lance dominates the card and its twelve-foot length cannot be judged; the armour is more jagged than sleek fluting.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A tall, regal human woman in her early thirties with dark espresso skin, high cheekbones, and a braided crown of platinum-blonde hair, clad in sleek, aerodynamic white-and-gold fluted plate armor with a cape of cobalt-blue feathers; she is captured suspended in mid-air above a cliff edge, both hands gripping a twelve-foot spiral lance of burnished gold and glowing amber glass aimed downward as two blazing wings of geometric sunlight unfurl from her shoulder-guards. Keep both distinct geometric sunlight wings fully inside the portrait margins, with compact swept-back shapes behind the shoulders and the blue feather cape separate beneath. Foreshorten the very long lance diagonally downward into the picture so its complete amber-glass spiral point and both gripping gauntlets are visible. Hint at a cliff edge only in a few low-contrast lower strokes. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

Composition correction: pull back markedly. Keep the COMPLETE outline of BOTH geometric light wings inside the central eighty percent of the image width and below an eight-percent empty top margin. Fold the wings upward closely behind the shoulders rather than spreading them off the sides. Make the figure smaller, from head to knees only, centred in about seventy percent of the height; do not show feet. The long lance is strongly foreshortened downward, with its tip comfortably inside the bottom-right margin. No wing ray or lance tip may meet a picture edge.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/bram-hammer-chime/splash.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1024 × 1536 px (2:3), native opaque RGB PNG; all attempts.
- References: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (style only).
- Attempts: 2; re-makes: 1. First attempt was too tall and steel-dominant, with a weak apron; remade once for broad Brannik proportions, copper armour and glowing smith's apron.
- Full-size and 300 px review: Retained remake: broad elderly smith, long silver-white braids, copper plate, glowing apron, raised hammer, floating anvil and healing knight's shield all read in the shared oil medium. Weakest point: warm healing effects compete with the face, and the beard reads more like white hair than literal silver wire.

### Attempt 1 — discarded

First attempt was too tall and steel-dominant, with a weak apron; remade once for broad Brannik proportions, copper armour and glowing smith's apron.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A stocky, barrel-chested elderly Brannik man with a magnificent waist-length beard of braided silver wire and snow-white hair, wearing heavy wolf-fur-trimmed copper plate and a glowing runic blacksmith's apron over slate-blue wool; he stands amidst swirling mountain snow, raising a glowing orange rune-hammer high to strike a floating bronze anvil-chime suspended before him, sending out warm golden ripples that mend the cracked shield of a knight beside him. Bram is the dominant complete head-to-knees silhouette. Raise one arm holding the rune-hammer, keep the other hand anatomically clear near the floating anvil. Represent runes only by abstract nonlinguistic glowing marks. A single subordinate knight is partly visible beside him, holding the cracked shield at lower right, clearly separate from Bram. Keep the mountain snow and healing ripples sparse and painterly. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: broad elderly smith, long silver-white braids, copper plate, glowing apron, raised hammer, floating anvil and healing knight's shield all read in the shared oil medium. Weakest point: warm healing effects compete with the face, and the beard reads more like white hair than literal silver wire.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A stocky, barrel-chested elderly Brannik man with a magnificent waist-length beard of braided silver wire and snow-white hair, wearing heavy wolf-fur-trimmed copper plate and a glowing runic blacksmith's apron over slate-blue wool; he stands amidst swirling mountain snow, raising a glowing orange rune-hammer high to strike a floating bronze anvil-chime suspended before him, sending out warm golden ripples that mend the cracked shield of a knight beside him. Bram is the dominant complete head-to-knees silhouette. Raise one arm holding the rune-hammer, keep the other hand anatomically clear near the floating anvil. Represent runes only by abstract nonlinguistic glowing marks. A single subordinate knight is partly visible beside him, holding the cracked shield at lower right, clearly separate from Bram. Keep the mountain snow and healing ripples sparse and painterly. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

Subject correction: Bram has distinctly SHORT, broad, barrel-chested Brannik proportions, with an enormous belly and wide shoulders; do not make a tall human knight. His armour must be visibly HAMMERED COPPER, warm russet orange-brown in its main midtones, rather than indigo steel with gold trim. Show a broad glowing smith's apron over slate-blue wool, snow-white hair and long silver-wire beard braids. Omit any invented crimson cloak. Keep the raised hammer completely within an eight-percent top margin, the floating bronze anvil in front, and one subordinate knight and cracked healing shield at lower right.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/marrow/splash.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1024 × 1536 px (2:3), native opaque RGB PNG; all attempts.
- References: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (style only).
- Attempts: 1; re-makes: 0. No remake; retained after full-size and 300 px-wide visual review.
- Full-size and 300 px review: Retained first attempt: hulking sealed soot-iron/copper suit, star-cracked round porthole, enlarged right porcelain arm, pressure-ring vents, collar steam and planted anchor match the description with strong impasto and indigo depth. Weakest point: dense rivets and warm trim obscure some soot-black iron at card size.

### Attempt 1 — retained

Retained first attempt: hulking sealed soot-iron/copper suit, star-cracked round porthole, enlarged right porcelain arm, pressure-ring vents, collar steam and planted anchor match the description with strong impasto and indigo depth. Weakest point: dense rivets and warm trim obscure some soot-black iron at card size.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A hulking figure in a sealed, barrel-chested suit of soot-black iron and hammered copper, face hidden behind a round porthole cracked like a star; the right arm is swollen with welded porcelain plates and brass pressure-rings that vent jets of silver-white light, and he plants a ship’s anchor while steam whistles from the collar. Show the swollen porcelain-armoured RIGHT arm on the viewer's left, distinct from the ordinary left arm. Let the right hand plant a single ship's anchor diagonally in front, with both curved flukes inside the frame; left hand rests naturally against the belt. The head is a sealed rounded diving helmet, with one dark circular glass porthole carrying radial star-shaped cracks, no visible human face. Silver-white vent light is sparse and painted, with a tight viridian edge. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/soren-kipp/splash.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1024 × 1536 px (2:3), native opaque RGB PNG; all attempts.
- References: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (style only).
- Attempts: 2; re-makes: 1. First attempt clipped Kipp's highest wing; remade once for a complete companion silhouette and more equipment clearance.
- Full-size and 300 px review: Retained remake: freckled sandy-haired youth, copper aviator coat, canvas glider, one-handed grapple, two-barrel brass rifle with amber scope and complete iron Kipp are legible in candidate-like oil strokes. Weakest point: the rifle lacks an obvious exposed harpoon tip, and Kipp's broad head is less specifically kestrel-like than its wing and beak silhouette.

### Attempt 1 — discarded

First attempt clipped Kipp's highest wing; remade once for a complete companion silhouette and more equipment clearance.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A wiry, energetic nineteen-year-old human youth with freckles, messy sandy-brown hair, and an oversized copper-riveted aviator coat with a deployed canvas glider-wing pack on his back; he hangs one-handed from a brass grappling-hook line high above a smoky dockyard, aiming a long, double-barreled brass harpoon-rifle with a glowing amber scope while a soot-black iron kestrel with a three-foot wingspan and amber-glass eyes dives beside the grapple line. One human and exactly one mechanical kestrel. Show Soren's left hand grasping the grapple line overhead and his right hand securely aiming the harpoon-rifle outward; a shoulder sling supports the rifle's weight. Two distinct parallel brass barrels terminate within the frame. Keep the two canvas glider wings behind his shoulders separate from Kipp's two iron wings. Place Kipp beside the rope, fully visible and large enough to read on a card. Reduce the dockyard to a few distant smoke masses. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: freckled sandy-haired youth, copper aviator coat, canvas glider, one-handed grapple, two-barrel brass rifle with amber scope and complete iron Kipp are legible in candidate-like oil strokes. Weakest point: the rifle lacks an obvious exposed harpoon tip, and Kipp's broad head is less specifically kestrel-like than its wing and beak silhouette.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A wiry, energetic nineteen-year-old human youth with freckles, messy sandy-brown hair, and an oversized copper-riveted aviator coat with a deployed canvas glider-wing pack on his back; he hangs one-handed from a brass grappling-hook line high above a smoky dockyard, aiming a long, double-barreled brass harpoon-rifle with a glowing amber scope while a soot-black iron kestrel with a three-foot wingspan and amber-glass eyes dives beside the grapple line. One human and exactly one mechanical kestrel. Show Soren's left hand grasping the grapple line overhead and his right hand securely aiming the harpoon-rifle outward; a shoulder sling supports the rifle's weight. Two distinct parallel brass barrels terminate within the frame. Keep the two canvas glider wings behind his shoulders separate from Kipp's two iron wings. Place Kipp beside the rope, fully visible and large enough to read on a card. Reduce the dockyard to a few distant smoke masses. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

Composition correction: pull back markedly so Soren, the two canvas glider wings, the entire double-barrel rifle and the COMPLETE iron kestrel silhouette are inside the central eighty percent of the image width, with eight-percent top clearance above the bird's highest wing. Kipp dives with its two wings angled compactly backward beside the rope, not spread across the upper edge. Soren is a knees-up figure, occupying seventy percent of image height; omit his feet. The grapple rope alone may extend out the top. His face is faceted painted skin, not a smooth youthful anime face.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/torga-moss-back/splash.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1024 × 1536 px (2:3), native opaque RGB PNG; all attempts.
- References: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (style only).
- Attempts: 1; re-makes: 0. No remake; retained after full-size and 300 px-wide visual review.
- Full-size and 300 px review: Retained first attempt: mossy stone matriarch, golden eyes, lantern-hung ironwood antlers, bark/shell armour, two hands on the root-totem, swamp and blue thorn-wall match the materials and silhouette in strong oil planes. Weakest point: her face looks gentler and younger than venerable; the wall's twenty-foot scale is only implied.

### Attempt 1 — retained

Retained first attempt: mossy stone matriarch, golden eyes, lantern-hung ironwood antlers, bark/shell armour, two hands on the root-totem, swamp and blue thorn-wall match the materials and silhouette in strong oil planes. Weakest point: her face looks gentler and younger than venerable; the wall's twenty-foot scale is only implied.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A wide, monumental, matriarchal Korvath woman of venerable age with moss-covered emerald-grey stone skin, kind golden eyes, and a crown of real branching ironwood antlers hung with glowing turquoise glass lanterns; she wears layered armor of living tree-bark and river-turtle shell, resting both massive hands atop a gnarled root-totem planted in the swamp as a twenty-foot wall of braided wood and glowing blue thorns erupts from the water around her. Keep the whole branching antler crown and hanging turquoise lanterns inside safe margins. Show exactly two massive stone hands resting naturally side by side on the single central root-totem. Maintain a kind visibly feminine elderly face and golden eyes in faceted emerald-grey stone. The braided thorn-wall rises in two restrained side masses behind her, with indigo-blue magical thorn points; swamp water is just a few dark strokes below. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/lioren-noct/splash.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1024 × 1536 px (2:3), native opaque RGB PNG; all attempts.
- References: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (style only).
- Attempts: 2; re-makes: 1. First attempt clipped the staff's upper finial; remade once to fit the complete instrument and make the hair rise upward.
- Full-size and 300 px review: Retained remake: elegant blindfolded pointed-eared figure, rising silver hair, midnight robes, astrolabe ornaments, floating rocks, bowed vertical string-staff and violet/amber chords are readable in ochre/indigo oil paint. Weakest point: the string-staff reads closer to an elongated lyre than a cello, and fine strings recede at 300 px.

### Attempt 1 — discarded

First attempt clipped the staff's upper finial; remade once to fit the complete instrument and make the hair rise upward.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A tall, androgynous, strikingly elegant Auralin figure with pale moonlit-bronze skin, long pointed ears, and waist-length silver hair floating upward in zero-gravity, dressed in flowing high-collared robes of deep midnight-indigo silk trimmed with burnished gold astrolabe rings; they stand calmly as boulders float around them, drawing a long golden bow across the taut bronze strings of a vertical cello-like staff that projects razor-sharp waves of violet and amber light. They wear a plain dark silk blindfold, leaving the long pointed ears and planar cheekbones visible. One hand holds the upright cello-like staff, the other holds a SINGLE long golden musical bow crossing its taut bronze strings horizontally. Keep the entire bow and staff crown within margins, with readable separation from floating hair and sparse suspended boulders. Use only a few thin muted violet and amber sound-wave planes, not a broad coloured wash. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: elegant blindfolded pointed-eared figure, rising silver hair, midnight robes, astrolabe ornaments, floating rocks, bowed vertical string-staff and violet/amber chords are readable in ochre/indigo oil paint. Weakest point: the string-staff reads closer to an elongated lyre than a cello, and fine strings recede at 300 px.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A tall, androgynous, strikingly elegant Auralin figure with pale moonlit-bronze skin, long pointed ears, and waist-length silver hair floating upward in zero-gravity, dressed in flowing high-collared robes of deep midnight-indigo silk trimmed with burnished gold astrolabe rings; they stand calmly as boulders float around them, drawing a long golden bow across the taut bronze strings of a vertical cello-like staff that projects razor-sharp waves of violet and amber light. They wear a plain dark silk blindfold, leaving the long pointed ears and planar cheekbones visible. One hand holds the upright cello-like staff, the other holds a SINGLE long golden musical bow crossing its taut bronze strings horizontally. Keep the entire bow and staff crown within margins, with readable separation from floating hair and sparse suspended boulders. Use only a few thin muted violet and amber sound-wave planes, not a broad coloured wash. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

Composition correction: shorten the cello-staff to fit its ENTIRE crown, orbital rings, finial and bottom point inside the central eighty-four percent of image height. Leave at least eight-percent blank slate margin above the highest finial. Keep both ends of the horizontal musical bow inside eight-percent side margins. Pull the camera back and reduce the figure slightly to a seventy-percent-height knees-up silhouette. Keep the floating silver hair largely rising upward in loose compact sweeps rather than streaming off the side. Retain the blindfold and a few sparse violet-amber chords.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/brenna-cold-bell/splash.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1024 × 1536 px (2:3), native opaque RGB PNG; all attempts.
- References: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (style only).
- Attempts: 1; re-makes: 0. No remake; retained after full-size and 300 px-wide visual review.
- Full-size and 300 px review: Retained first attempt: muscular warrior, blue eye paint, blonde braids, white furs, green scale mail and two-handed split bronze tuning-fork sword with blue ice and golden sparks match the description and anchor's rough oil surface. Weakest point: the bright ice and oversized blade compete with her face and are brighter cyan than deep sapphire.

### Attempt 1 — retained

Retained first attempt: muscular warrior, blue eye paint, blonde braids, white furs, green scale mail and two-handed split bronze tuning-fork sword with blue ice and golden sparks match the description and anchor's rough oil surface. Weakest point: the bright ice and oversized blade compete with her face and are brighter cyan than deep sapphire.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A tall, muscular, Amazonian human woman in her mid-thirties with wind-burned fair skin, blue war-paint across her eyes, and thick blonde hair braided with frost-crystals and bronze rings; clad in white crag-yeti furs over verdigris-green scale mail, she swings a colossal, six-foot-long greatsword shaped like a split bronze tuning-fork that trails a roaring vortex of sapphire-blue ice and golden sound-sparks. Two powerful hands grip one sword hilt in a credible dynamic mid-swing. Make the enormous bronze weapon a single broad cleaver split into TWO long tuning-fork prongs, with both tips visible inside the portrait and a clear gap between them. Foreshorten its six-foot length diagonally to fit. Preserve the blue eye paint, blonde braids and white fur collar as separate readable features. Keep sapphire ice and golden sound sparks compact and brush-painted behind the weapon. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/lazlo-greaves/splash.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1024 × 1536 px (2:3), native opaque RGB PNG; all attempts.
- References: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (style only).
- Attempts: 1; re-makes: 0. No remake; retained after full-size and 300 px-wide visual review.
- Full-size and 300 px review: Retained first attempt: gaunt goateed physician, monocle, tipped top hat, burgundy/copper coat, emerald/amber distillery, left syringe-gauntlet and exactly three airborne potion bottles are clearly painted and well separated. Weakest point: the small monocle and syringe needle weaken at 300 px, and the heavily detailed coat is busier than ideal.

### Attempt 1 — retained

Retained first attempt: gaunt goateed physician, monocle, tipped top hat, burgundy/copper coat, emerald/amber distillery, left syringe-gauntlet and exactly three airborne potion bottles are clearly painted and well separated. Weakest point: the small monocle and syringe needle weaken at 300 px, and the heavily detailed coat is busier than ideal.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A tall, gaunt, theatrical human man in his late forties with a sharp silver-streaked goatee, a brass monocle over one eye, and a high-collared burgundy-and-copper leather greatcoat; atop his shoulders sits an elaborate glass distillery backpack filled with bubbling emerald-green and golden-amber liquids connected by hoses to a brass syringe-gauntlet on his left hand, while his right hand tips his top-hat and tosses three glowing glass potion-grenades into the air. Choose the instant immediately after his right hand has tossed exactly three separate glass potion-grenades upward and has returned to tipping the top-hat brim; only two arms and two hands. Keep the three bottles suspended separately in the air away from his head. His left hand wears the brass syringe-gauntlet with a clear needle mechanism, linked by hoses to two large emerald and amber glass distillery vessels rising behind his shoulders. Avoid tiny busy lab ornaments. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/asha-renn/splash.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1024 × 1536 px (2:3), native opaque RGB PNG; all attempts.
- References: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (style only).
- Attempts: 2; re-makes: 1. First attempt cropped the constructs' outer hands and made them compete strongly with the central oracle; remade once for more contained, distant constructs.
- Full-size and 300 px review: Retained remake: copper-brown pointed-eared oracle, hooded rose-gold cloth, coin-chimes, golden skin lines, open hands and two flanking sand/amber warrior constructs match the warm oil language. Weakest point: constructs remain quite bright and knight-like, their mirrored pose is approximate, and barefoot status is outside the required knees-up crop.

### Attempt 1 — discarded

First attempt cropped the constructs' outer hands and made them compete strongly with the central oracle; remade once for more contained, distant constructs.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A graceful, barefoot Auralin woman with warm copper-brown skin tattooed with glowing golden harmonic lines, dark eyes, and a hooded mantle of shimmering rose-gold desert silk and tinkling bronze coin-chimes; she stands with arms outstretched in a canyon as two ten-foot-tall humanoid warrior-statues formed of swirling metallic copper sand and glowing amber glass rise out of the ground on either side of her, mimicking her exact stance. One principal living Auralin woman with two specifically requested sand-and-glass constructs, not three identical women. Show the woman's two arms outstretched and hands open with natural fingers, long pointed ears beneath the hood, copper-brown planar face and nonlinguistic golden skin lines. The two taller warrior-statues flank her in softer atmospheric middle distance, both copying her outstretched arm stance; make their heads and arms visible within the frame. Suggest canyon walls only by subdued strokes. Lower body dissolves toward the knees as the category framing requires. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: copper-brown pointed-eared oracle, hooded rose-gold cloth, coin-chimes, golden skin lines, open hands and two flanking sand/amber warrior constructs match the warm oil language. Weakest point: constructs remain quite bright and knight-like, their mirrored pose is approximate, and barefoot status is outside the required knees-up crop.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A graceful, barefoot Auralin woman with warm copper-brown skin tattooed with glowing golden harmonic lines, dark eyes, and a hooded mantle of shimmering rose-gold desert silk and tinkling bronze coin-chimes; she stands with arms outstretched in a canyon as two ten-foot-tall humanoid warrior-statues formed of swirling metallic copper sand and glowing amber glass rise out of the ground on either side of her, mimicking her exact stance. One principal living Auralin woman with two specifically requested sand-and-glass constructs, not three identical women. Show the woman's two arms outstretched and hands open with natural fingers, long pointed ears beneath the hood, copper-brown planar face and nonlinguistic golden skin lines. The two taller warrior-statues flank her in softer atmospheric middle distance, both copying her outstretched arm stance; make their heads and arms visible within the frame. Suggest canyon walls only by subdued strokes. Lower body dissolves toward the knees as the category framing requires. Use art/style/candidate-a.png as the primary style reference and art/style/anchor-2-hero.png as the character-category style reference: borrow oil surface, large stroke scale, edge economy, palette, material separation and lighting only. Invent this subject and composition; do not copy the anonymous helmet, crimson cloak, sword, party, city or spire from the references. Teaser lighting: keep half the face or visor in chromatic indigo shadow, with clear head, shoulder and defining equipment silhouettes. Maintain broad handmade bristle planes and thick ochre knife edges rather than minute ornament. Plain painterly slate-indigo backdrop; any requested setting stays sparse and subordinate. One full-bleed opaque PNG, exact portrait 2:3, at the largest native resolution available for this ratio, target 2304 x 3456 pixels. Keep the focal silhouette and important equipment inside comfortable margins; no panels or UI.

Composition correction: make the two sand-and-amber constructs more distant and slightly smaller in the picture so BOTH complete heads, shoulders, outstretched arms and all FOUR construct hands fit well inside eight-percent left and right margins. Arrange the pair symmetrically flanking the central woman, each turning three-quarter inward so their outstretched arms are foreshortened toward the viewer rather than spanning the image width. Keep Asha's two open hands also within the same safe margins. The constructs should read as rough swirling copper sand and amber glass, not as detailed metal knights. Reduce their brightness and contrast beneath Asha's focal face and upper silhouette. Keep the hooded rose-gold mantle and golden nonlinguistic skin lines, with a little more indigo resting space around the group.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

# Kaelvorn — Phase 5: the four full characters

All eight deliverables are opaque RGB PNGs at native 1024 × 1536 px (exact portrait 2:3). Built-in `image_gen.imagegen`; model `gpt-image` is identified in PNG provenance, with no more specific revision exposed. Every call requested the largest native output, targeting 2560 × 3840; the tool returned 1024 × 1536 instead. Files retain native bytes without resizing, cropping, recolouring or overlays. Inspection thumbnails were temporary and are not deliverables.

Read `docs/STYLE.md` in full and all four full character records in `src/data/characters.ts`. Candidate and hero anchor were inspected at original size before generation. The fixed prefix, category suffix and fixed avoid list below are copied verbatim. Full art descriptions were retained, with subject instructions reconciling notation/runes with the no-lettering rule and adapting full-body effects to the category crop. Each final was visually reviewed at native size and at 300 × 450 px, checking identity against its paired image. No visible text, logo, watermark, painted frame, extra limbs or broken facial anatomy was found. Character identity is consistent across each pair; small jewellery, grip and fitting details retain the limitations noted per asset.

Fourteen calls total: eight first attempts and six remakes. Every submitted prompt, including discarded attempts, follows. Original generated attempts remain with the tool; only the eight selected PNGs were copied into the repository. No private machine paths are recorded.

## `art/characters/valen-korr/splash.png`

- Tool: built-in `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Actual size: 1024 × 1536 px, opaque RGB PNG (all attempts).
- Re-makes: 1. Reasons are recorded with the discarded attempt below.
- Style references, in order: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (surface, stroke scale, edge economy, palette, materials and light only).
- Remake identity reference 3: this image's discarded Attempt 1; subject/equipment continuity only, with targeted corrections below.

### Attempt 1 — discarded

Unbraided beard; porcelain wrist obscured.

References for this attempt: candidate-a.png and anchor-2-hero.png.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A colossal, broad-shouldered rectangle of a man standing nearly eight feet tall, with a wide, grounded stance dominated by an oversized curved tower shield on his left arm and a heavy flanged mace in his right hand; three short brass chime-pipes rise vertically from the back of his pauldrons.

A weathered, noble Korvath face in his late fifties with skin the color and texture of chiseled slate-grey granite; a square jaw with a neat, braided beard of silver-white hair bound in gold clasps; warm, glowing amber eyes; a deep vertical chip across his left brow like carved stone.

Layered plates of burnished gold-bronze and polished ivory-white enamel over a dark cobalt-blue quilted gambeson; his left forearm gauntlet is missing, revealing a hand and wrist transformed into smooth, glowing white porcelain veined with silver cracks.

Burnished Gold, Ivory White, Cobalt Blue, and Slate Grey.

Toll of Aethel, a five-foot tall concave tower shield cast from thick green-patina bell-bronze with a raised golden sun-rose embossing at its center, paired with Gavel of the Tenth Chord, a heavy brass-headed war-mace whose hollow core glows with liquid orange Sun-Pitch.

Planted in a low, wide defensive brace, left foot forward, driving the bottom spike of his giant bell-shield into the ground while drawing back his glowing war-mace to strike the inner rim of his own shield like a gong.

Concentric, rippling rings of translucent golden-amber light and visible musical staff-lines that expand outward along the ground from his shield, leaving warm, glowing geometric ward-runes burned into the earth beneath his boots.

He is Valen Korr, the Bell-Warden, a Korvath tank of the Solaris Bastion. Preserve his uncovered stone face: short swept-back silver-white hair, broad flat nose, heavy square brow and compact silver beard braided into three sections. Keep the porcelain left wrist visible above the shield rim. Exactly three short chime-pipes, exactly one shield and one flanged mace. Golden resonance is sparse translucent arcs and abstract geometry only, with no notation, letters or readable runes. Gold-bronze is weathered tarnished brass; enamel is warm ivory, and cobalt is deep desaturated indigo-blue. The teal rim stays thin. Do not add a helmet or sword. Single character, knees-up three-quarter pose, slight low angle, generous dark clearance around the head, weapon tips and shoulders; figure fills about 70 percent of image height. Keep the defining action from the description, adapting feet and ground effects to the knee-up crop, and keep all focal equipment within the canvas. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: convincing slate-granite elder, silver beard braids, amber eyes, three chime-pipes, ivory/cobalt plate, patinated bell-shield and orange-core mace in candidate-matched bristle impasto. Weakest points: shield still hides most of the porcelain hand; shield and lower resonance remain visually busy and the figure exceeds the nominal 70 percent height.

References for this attempt: candidate-a.png, anchor-2-hero.png and discarded Attempt 1 as identity reference.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

A colossal, broad-shouldered rectangle of a man standing nearly eight feet tall, with a wide, grounded stance dominated by an oversized curved tower shield on his left arm and a heavy flanged mace in his right hand; three short brass chime-pipes rise vertically from the back of his pauldrons.

A weathered, noble Korvath face in his late fifties with skin the color and texture of chiseled slate-grey granite; a square jaw with a neat, braided beard of silver-white hair bound in gold clasps; warm, glowing amber eyes; a deep vertical chip across his left brow like carved stone.

Layered plates of burnished gold-bronze and polished ivory-white enamel over a dark cobalt-blue quilted gambeson; his left forearm gauntlet is missing, revealing a hand and wrist transformed into smooth, glowing white porcelain veined with silver cracks.

Burnished Gold, Ivory White, Cobalt Blue, and Slate Grey.

Toll of Aethel, a five-foot tall concave tower shield cast from thick green-patina bell-bronze with a raised golden sun-rose embossing at its center, paired with Gavel of the Tenth Chord, a heavy brass-headed war-mace whose hollow core glows with liquid orange Sun-Pitch.

Planted in a low, wide defensive brace, left foot forward, driving the bottom spike of his giant bell-shield into the ground while drawing back his glowing war-mace to strike the inner rim of his own shield like a gong.

Concentric, rippling rings of translucent golden-amber light and visible musical staff-lines that expand outward along the ground from his shield, leaving warm, glowing geometric ward-runes burned into the earth beneath his boots.

He is Valen Korr, the Bell-Warden, a Korvath tank of the Solaris Bastion. Preserve his uncovered stone face: short swept-back silver-white hair, broad flat nose, heavy square brow and compact silver beard braided into three sections. Keep the porcelain left wrist visible above the shield rim. Exactly three short chime-pipes, exactly one shield and one flanged mace. Golden resonance is sparse translucent arcs and abstract geometry only, with no notation, letters or readable runes. Gold-bronze is weathered tarnished brass; enamel is warm ivory, and cobalt is deep desaturated indigo-blue. The teal rim stays thin. Do not add a helmet or sword. Single character, knees-up three-quarter pose, slight low angle, generous dark clearance around the head, weapon tips and shoulders; figure fills about 70 percent of image height. Keep the defining action from the description, adapting feet and ground effects to the knee-up crop, and keep all focal equipment within the canvas. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

Revision: reference image 3 is the first Valen splash, used for identity and equipment continuity only. Preserve his face, shield, mace and armour, but replace the short unbraided beard with three clearly interwoven silver-white beard braids bound in simple gold clasps. Make the vertical chipped groove across his anatomical left brow unmistakable. Show his bare white porcelain left hand and silver-cracked wrist gripping the shield's upper inner handle. Reduce fine armour speckles into broad flat-bristle planes. Pull back slightly so the knees-up subject occupies about 75 percent of the image height, with complete weapon and shield inside generous dark margins.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/valen-korr/portrait.png`

- Tool: built-in `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Actual size: 1024 × 1536 px, opaque RGB PNG (all attempts).
- Re-makes: 1. Reasons are recorded with the discarded attempt below.
- Style references, in order: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (surface, stroke scale, edge economy, palette, materials and light only).
- Identity reference 3: `art/characters/valen-korr/splash.png`, retained final splash; same face, hair, colours and costume.

### Attempt 1 — discarded

Identity and style matched, but composition stayed waist-up instead of a close bust; remade for head-and-shoulders framing.

References for this attempt: candidate-a.png, anchor-2-hero.png and this character's retained splash.png as identity reference.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Portrait: bust three-quarter view, 85 mm lens, face and shoulders dominate, faceted brush planes on cheeks and nose, sharp eyes, subdued plain painterly background fading to #11151E, portrait 2:3.

A colossal, broad-shouldered rectangle of a man standing nearly eight feet tall, with a wide, grounded stance dominated by an oversized curved tower shield on his left arm and a heavy flanged mace in his right hand; three short brass chime-pipes rise vertically from the back of his pauldrons.

A weathered, noble Korvath face in his late fifties with skin the color and texture of chiseled slate-grey granite; a square jaw with a neat, braided beard of silver-white hair bound in gold clasps; warm, glowing amber eyes; a deep vertical chip across his left brow like carved stone.

Layered plates of burnished gold-bronze and polished ivory-white enamel over a dark cobalt-blue quilted gambeson; his left forearm gauntlet is missing, revealing a hand and wrist transformed into smooth, glowing white porcelain veined with silver cracks.

Burnished Gold, Ivory White, Cobalt Blue, and Slate Grey.

Toll of Aethel, a five-foot tall concave tower shield cast from thick green-patina bell-bronze with a raised golden sun-rose embossing at its center, paired with Gavel of the Tenth Chord, a heavy brass-headed war-mace whose hollow core glows with liquid orange Sun-Pitch.

Planted in a low, wide defensive brace, left foot forward, driving the bottom spike of his giant bell-shield into the ground while drawing back his glowing war-mace to strike the inner rim of his own shield like a gong.

Concentric, rippling rings of translucent golden-amber light and visible musical staff-lines that expand outward along the ground from his shield, leaving warm, glowing geometric ward-runes burned into the earth beneath his boots.

He is Valen Korr, the Bell-Warden, a Korvath tank of the Solaris Bastion. Preserve his uncovered stone face: short swept-back silver-white hair, broad flat nose, heavy square brow and compact silver beard braided into three sections. Keep the porcelain left wrist visible above the shield rim. Exactly three short chime-pipes, exactly one shield and one flanged mace. Golden resonance is sparse translucent arcs and abstract geometry only, with no notation, letters or readable runes. Gold-bronze is weathered tarnished brass; enamel is warm ivory, and cobalt is deep desaturated indigo-blue. The teal rim stays thin. Do not add a helmet or sword. Identity reference image 3 is this character's approved splash.png: preserve exactly the same facial structure, age, skin, hair arrangement, ears, accessories, costume colours, armour construction and equipment design. Tighten to a bust three-quarter composition with an 85 mm lens and planar painted skin. Face and shoulders dominate; eyes are the sharpest focal point. Adapt the action to a calm confident bust pose, with only partial equipment at the lower edge; do not cram the full-body action or complete weapon into this close portrait. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: close bust preserves the splash's granite face, chipped brow, swept silver hair, gold-bound beard braids, amber eyes, ivory/brass armour and three chime-pipes. Faceted skin and warm/indigo polarity closely match the references. Weakest point: fine armour stippling is busier than the candidate's broad masses, and the far chime-pipe is partly cropped as peripheral equipment.

References for this attempt: candidate-a.png, anchor-2-hero.png and this character's retained splash.png as identity reference.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Portrait: bust three-quarter view, 85 mm lens, face and shoulders dominate, faceted brush planes on cheeks and nose, sharp eyes, subdued plain painterly background fading to #11151E, portrait 2:3.

A colossal, broad-shouldered rectangle of a man standing nearly eight feet tall, with a wide, grounded stance dominated by an oversized curved tower shield on his left arm and a heavy flanged mace in his right hand; three short brass chime-pipes rise vertically from the back of his pauldrons.

A weathered, noble Korvath face in his late fifties with skin the color and texture of chiseled slate-grey granite; a square jaw with a neat, braided beard of silver-white hair bound in gold clasps; warm, glowing amber eyes; a deep vertical chip across his left brow like carved stone.

Layered plates of burnished gold-bronze and polished ivory-white enamel over a dark cobalt-blue quilted gambeson; his left forearm gauntlet is missing, revealing a hand and wrist transformed into smooth, glowing white porcelain veined with silver cracks.

Burnished Gold, Ivory White, Cobalt Blue, and Slate Grey.

Toll of Aethel, a five-foot tall concave tower shield cast from thick green-patina bell-bronze with a raised golden sun-rose embossing at its center, paired with Gavel of the Tenth Chord, a heavy brass-headed war-mace whose hollow core glows with liquid orange Sun-Pitch.

Planted in a low, wide defensive brace, left foot forward, driving the bottom spike of his giant bell-shield into the ground while drawing back his glowing war-mace to strike the inner rim of his own shield like a gong.

Concentric, rippling rings of translucent golden-amber light and visible musical staff-lines that expand outward along the ground from his shield, leaving warm, glowing geometric ward-runes burned into the earth beneath his boots.

He is Valen Korr, the Bell-Warden, a Korvath tank of the Solaris Bastion. Preserve his uncovered stone face: short swept-back silver-white hair, broad flat nose, heavy square brow and compact silver beard braided into three sections. Keep the porcelain left wrist visible above the shield rim. Exactly three short chime-pipes, exactly one shield and one flanged mace. Golden resonance is sparse translucent arcs and abstract geometry only, with no notation, letters or readable runes. Gold-bronze is weathered tarnished brass; enamel is warm ivory, and cobalt is deep desaturated indigo-blue. The teal rim stays thin. Do not add a helmet or sword. Identity reference image 3 is this character's approved splash.png: preserve exactly the same facial structure, age, skin, hair arrangement, ears, accessories, costume colours, armour construction and equipment design. Tighten to a bust three-quarter composition with an 85 mm lens and planar painted skin. Face and shoulders dominate; eyes are the sharpest focal point. Adapt the action to a calm confident bust pose, with only partial equipment at the lower edge; do not cram the full-body action or complete weapon into this close portrait. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

Final framing priority: this is a close head-and-shoulders bust, not a waist-up view. Frame from just above the hair to the upper chest, cropping horizontally through the upper breastplate or collarbone-level costume. The face alone should occupy roughly 40 percent of canvas height, the head including hair about 55 percent. Shoulders extend beyond the lower side edges. Leave 8 percent headroom. Omit hands and full weapons; at most a small staff edge, shoulder pipe or boiler detail may appear beside the shoulder. Keep both eyes, nose, mouth, chin, ear tips and principal hair ornaments visible. The background is subdued broad indigo paint with just a few ochre strokes, so the face is the strongest contrast.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/lyra-vance/splash.png`

- Tool: built-in `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Actual size: 1024 × 1536 px, opaque RGB PNG (all attempts).
- Re-makes: 1. Reasons are recorded with the discarded attempt below.
- Style references, in order: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (surface, stroke scale, edge economy, palette, materials and light only).
- Remake identity reference 3: this image's discarded Attempt 1; subject/equipment continuity only, with targeted corrections below.

### Attempt 1 — discarded

Staff crook and lantern too close to the left edge; ornate detail crowded the card.

References for this attempt: candidate-a.png and anchor-2-hero.png.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

Tall, lithe, and dancer-like (around six feet two inches), with an asymmetrical, flowing silhouette created by long leaf-shaped cloak ribbons, sweeping Auralin ears, and a seven-foot curved ironwood staff from which a large glowing glass lantern swings on a bronze chain.

Warm olive-tan skin dusted with faint, natural bioluminescent turquoise freckles across her cheekbones; expressive, tilted golden-amber eyes; eight-inch tapering sylvan ears adorned with tiny copper bell-studs; thick, wavy auburn-red hair worn in a loose side-braid woven with glowing white marsh-orchids.

Layered robes of verdigris-green marsh-silk, supple bark-brown leather corsetry embossed with leaf veins, and shoulder-guards formed from polished turquoise river-turtle shell inlaid with spun gold.

Verdigris Green, Bioluminescent Turquoise, Warm Amber Yellow, and Bark Brown.

Whisper-Cradle, a curved staff of living dark ironwood whose crook sprouts real glowing blue moss; suspended from its tip on three brass chains is a faceted globe of golden Amber-glass housing a floating, swirling lotus of turquoise fire.

Caught mid-step as if dancing across water, one hand raised to pluck a glowing golden string of light in the air while the other swings her lantern-staff in a wide, graceful figure-eight arc around her hips.

Ribbons of warm golden light braided with sparkling turquoise spore-dust that arch from her lantern to her allies' chests, while translucent glowing water-lilies bloom and ripple beneath her feet with every spell cast.

She is Lyra Vance, the Lantern-Weaver, an Auralin mobile healer of the Verdant Chorus. Preserve an adult face with a long narrow nose, expressive arched brows, amber eyes, sweeping long ears and one loose auburn side-braid over her right shoulder threaded with three white marsh-orchids. Her robes and leaf ribbons are muted verdigris, with bark leather and turquoise turtle-shell shoulder plates. One hand holds the ironwood staff, the other plucks one thin golden light-string; keep both hands anatomically clear. Show exactly one amber-glass lantern suspended on three brass chains, containing one small teal-fire lotus. No additional allies: the healing ribbons dissolve into the backdrop. Keep spores and glow sparse, not a neon wash. Single character, knees-up three-quarter pose, slight low angle, generous dark clearance around the head, weapon tips and shoulders; figure fills about 70 percent of image height. Keep the defining action from the description, adapting feet and ground effects to the knee-up crop, and keep all focal equipment within the canvas. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: complete ironwood crook and amber lantern, teal lotus, olive-tan face, amber eyes, long ears, auburn orchid braid, verdigris robes and turtle-shell shoulders. Broad cloth strokes and warm/cool light match. Weakest point: fine facial freckles and the individual chains lose clarity at card size; skin is smoother than the surrounding impasto.

References for this attempt: candidate-a.png, anchor-2-hero.png and discarded Attempt 1 as identity reference.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

Tall, lithe, and dancer-like (around six feet two inches), with an asymmetrical, flowing silhouette created by long leaf-shaped cloak ribbons, sweeping Auralin ears, and a seven-foot curved ironwood staff from which a large glowing glass lantern swings on a bronze chain.

Warm olive-tan skin dusted with faint, natural bioluminescent turquoise freckles across her cheekbones; expressive, tilted golden-amber eyes; eight-inch tapering sylvan ears adorned with tiny copper bell-studs; thick, wavy auburn-red hair worn in a loose side-braid woven with glowing white marsh-orchids.

Layered robes of verdigris-green marsh-silk, supple bark-brown leather corsetry embossed with leaf veins, and shoulder-guards formed from polished turquoise river-turtle shell inlaid with spun gold.

Verdigris Green, Bioluminescent Turquoise, Warm Amber Yellow, and Bark Brown.

Whisper-Cradle, a curved staff of living dark ironwood whose crook sprouts real glowing blue moss; suspended from its tip on three brass chains is a faceted globe of golden Amber-glass housing a floating, swirling lotus of turquoise fire.

Caught mid-step as if dancing across water, one hand raised to pluck a glowing golden string of light in the air while the other swings her lantern-staff in a wide, graceful figure-eight arc around her hips.

Ribbons of warm golden light braided with sparkling turquoise spore-dust that arch from her lantern to her allies' chests, while translucent glowing water-lilies bloom and ripple beneath her feet with every spell cast.

She is Lyra Vance, the Lantern-Weaver, an Auralin mobile healer of the Verdant Chorus. Preserve an adult face with a long narrow nose, expressive arched brows, amber eyes, sweeping long ears and one loose auburn side-braid over her right shoulder threaded with three white marsh-orchids. Her robes and leaf ribbons are muted verdigris, with bark leather and turquoise turtle-shell shoulder plates. One hand holds the ironwood staff, the other plucks one thin golden light-string; keep both hands anatomically clear. Show exactly one amber-glass lantern suspended on three brass chains, containing one small teal-fire lotus. No additional allies: the healing ribbons dissolve into the backdrop. Keep spores and glow sparse, not a neon wash. Single character, knees-up three-quarter pose, slight low angle, generous dark clearance around the head, weapon tips and shoulders; figure fills about 70 percent of image height. Keep the defining action from the description, adapting feet and ground effects to the knee-up crop, and keep all focal equipment within the canvas. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

Revision: reference image 3 is the first Lyra splash, used for identity and equipment continuity only. Preserve her face, braid, flowers, ears, verdigris robes and lantern design. Pull the camera back: the knees-up figure and complete staff crook and lantern must fit within the central 85 percent of canvas width and height, with clear dark space to the left of the entire ironwood crook and globe. Her head should sit 15 percent below the top. Reduce busy gold filigree and tiny ribbons into larger bristle-swept cloth planes; retain the three white orchids and one thin healing chord. Skin should show larger planar painted shapes, not a smooth rendered face. Keep the dancing mid-step gesture.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/lyra-vance/portrait.png`

- Tool: built-in `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Actual size: 1024 × 1536 px, opaque RGB PNG (all attempts).
- Re-makes: 1. Reasons are recorded with the discarded attempt below.
- Style references, in order: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (surface, stroke scale, edge economy, palette, materials and light only).
- Identity reference 3: `art/characters/lyra-vance/splash.png`, retained final splash; same face, hair, colours and costume.

### Attempt 1 — discarded

Identity and style matched, but composition stayed waist-up instead of a close bust; remade for head-and-shoulders framing.

References for this attempt: candidate-a.png, anchor-2-hero.png and this character's retained splash.png as identity reference.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Portrait: bust three-quarter view, 85 mm lens, face and shoulders dominate, faceted brush planes on cheeks and nose, sharp eyes, subdued plain painterly background fading to #11151E, portrait 2:3.

Tall, lithe, and dancer-like (around six feet two inches), with an asymmetrical, flowing silhouette created by long leaf-shaped cloak ribbons, sweeping Auralin ears, and a seven-foot curved ironwood staff from which a large glowing glass lantern swings on a bronze chain.

Warm olive-tan skin dusted with faint, natural bioluminescent turquoise freckles across her cheekbones; expressive, tilted golden-amber eyes; eight-inch tapering sylvan ears adorned with tiny copper bell-studs; thick, wavy auburn-red hair worn in a loose side-braid woven with glowing white marsh-orchids.

Layered robes of verdigris-green marsh-silk, supple bark-brown leather corsetry embossed with leaf veins, and shoulder-guards formed from polished turquoise river-turtle shell inlaid with spun gold.

Verdigris Green, Bioluminescent Turquoise, Warm Amber Yellow, and Bark Brown.

Whisper-Cradle, a curved staff of living dark ironwood whose crook sprouts real glowing blue moss; suspended from its tip on three brass chains is a faceted globe of golden Amber-glass housing a floating, swirling lotus of turquoise fire.

Caught mid-step as if dancing across water, one hand raised to pluck a glowing golden string of light in the air while the other swings her lantern-staff in a wide, graceful figure-eight arc around her hips.

Ribbons of warm golden light braided with sparkling turquoise spore-dust that arch from her lantern to her allies' chests, while translucent glowing water-lilies bloom and ripple beneath her feet with every spell cast.

She is Lyra Vance, the Lantern-Weaver, an Auralin mobile healer of the Verdant Chorus. Preserve an adult face with a long narrow nose, expressive arched brows, amber eyes, sweeping long ears and one loose auburn side-braid over her right shoulder threaded with three white marsh-orchids. Her robes and leaf ribbons are muted verdigris, with bark leather and turquoise turtle-shell shoulder plates. One hand holds the ironwood staff, the other plucks one thin golden light-string; keep both hands anatomically clear. Show exactly one amber-glass lantern suspended on three brass chains, containing one small teal-fire lotus. No additional allies: the healing ribbons dissolve into the backdrop. Keep spores and glow sparse, not a neon wash. Identity reference image 3 is this character's approved splash.png: preserve exactly the same facial structure, age, skin, hair arrangement, ears, accessories, costume colours, armour construction and equipment design. Tighten to a bust three-quarter composition with an 85 mm lens and planar painted skin. Face and shoulders dominate; eyes are the sharpest focal point. Adapt the action to a calm confident bust pose, with only partial equipment at the lower edge; do not cram the full-body action or complete weapon into this close portrait. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: close bust preserves olive-tan skin, golden eyes, turquoise cheek freckles, long ears, auburn side-braid with three white orchids, verdigris cloth and turquoise turtle-shell shoulder. Painted cheek planes and subdued indigo background remain coherent with the splash. Weakest point: the ear jewellery is more elaborate and the cheek modelling smoother than in the splash.

References for this attempt: candidate-a.png, anchor-2-hero.png and this character's retained splash.png as identity reference.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Portrait: bust three-quarter view, 85 mm lens, face and shoulders dominate, faceted brush planes on cheeks and nose, sharp eyes, subdued plain painterly background fading to #11151E, portrait 2:3.

Tall, lithe, and dancer-like (around six feet two inches), with an asymmetrical, flowing silhouette created by long leaf-shaped cloak ribbons, sweeping Auralin ears, and a seven-foot curved ironwood staff from which a large glowing glass lantern swings on a bronze chain.

Warm olive-tan skin dusted with faint, natural bioluminescent turquoise freckles across her cheekbones; expressive, tilted golden-amber eyes; eight-inch tapering sylvan ears adorned with tiny copper bell-studs; thick, wavy auburn-red hair worn in a loose side-braid woven with glowing white marsh-orchids.

Layered robes of verdigris-green marsh-silk, supple bark-brown leather corsetry embossed with leaf veins, and shoulder-guards formed from polished turquoise river-turtle shell inlaid with spun gold.

Verdigris Green, Bioluminescent Turquoise, Warm Amber Yellow, and Bark Brown.

Whisper-Cradle, a curved staff of living dark ironwood whose crook sprouts real glowing blue moss; suspended from its tip on three brass chains is a faceted globe of golden Amber-glass housing a floating, swirling lotus of turquoise fire.

Caught mid-step as if dancing across water, one hand raised to pluck a glowing golden string of light in the air while the other swings her lantern-staff in a wide, graceful figure-eight arc around her hips.

Ribbons of warm golden light braided with sparkling turquoise spore-dust that arch from her lantern to her allies' chests, while translucent glowing water-lilies bloom and ripple beneath her feet with every spell cast.

She is Lyra Vance, the Lantern-Weaver, an Auralin mobile healer of the Verdant Chorus. Preserve an adult face with a long narrow nose, expressive arched brows, amber eyes, sweeping long ears and one loose auburn side-braid over her right shoulder threaded with three white marsh-orchids. Her robes and leaf ribbons are muted verdigris, with bark leather and turquoise turtle-shell shoulder plates. One hand holds the ironwood staff, the other plucks one thin golden light-string; keep both hands anatomically clear. Show exactly one amber-glass lantern suspended on three brass chains, containing one small teal-fire lotus. No additional allies: the healing ribbons dissolve into the backdrop. Keep spores and glow sparse, not a neon wash. Identity reference image 3 is this character's approved splash.png: preserve exactly the same facial structure, age, skin, hair arrangement, ears, accessories, costume colours, armour construction and equipment design. Tighten to a bust three-quarter composition with an 85 mm lens and planar painted skin. Face and shoulders dominate; eyes are the sharpest focal point. Adapt the action to a calm confident bust pose, with only partial equipment at the lower edge; do not cram the full-body action or complete weapon into this close portrait. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

Final framing priority: this is a close head-and-shoulders bust, not a waist-up view. Frame from just above the hair to the upper chest, cropping horizontally through the upper breastplate or collarbone-level costume. The face alone should occupy roughly 40 percent of canvas height, the head including hair about 55 percent. Shoulders extend beyond the lower side edges. Leave 8 percent headroom. Omit hands and full weapons; at most a small staff edge, shoulder pipe or boiler detail may appear beside the shoulder. Keep both eyes, nose, mouth, chin, ear tips and principal hair ornaments visible. The background is subdued broad indigo paint with just a few ochre strokes, so the face is the strongest contrast.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/kaelen-vos/splash.png`

- Tool: built-in `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Actual size: 1024 × 1536 px, opaque RGB PNG (all attempts).
- Re-makes: 1. Reasons are recorded with the discarded attempt below.
- Style references, in order: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (surface, stroke scale, edge economy, palette, materials and light only).
- Remake identity reference 3: this image's discarded Attempt 1; subject/equipment continuity only, with targeted corrections below.

### Attempt 1 — discarded

Right saber tip clipped; tight framing and busy effects.

References for this attempt: candidate-a.png and anchor-2-hero.png.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

Lean, athletic, and coiled like a panther (around five feet ten inches), with a sharp V-shaped upper torso, billowy desert trousers gathered into bronze shin-greaves, a long flowing saffron scarf trailing two yards behind him, and twin deeply curved scimitars held in reverse and forward grips.

Sun-bronzed human skin in his late twenties; sharp cheekbones with a warm, cocky half-smile; striking copper-gold eyes lined with dark desert kohl against sun-glare; tousled, shoulder-length jet-black hair swept back by a braided leather headband set with an amber prism; a faint white scar across the bridge of his nose.

An open-chested vest of supple cinnamon-brown dune-drake leather reinforced with overlapping scales of hammered rose-gold and copper; asymmetrical pauldrons made from curved bronze wind-harp ribs; silk waist-sashes in vibrant saffron yellow and deep indigo.

Hammered Copper, Saffron Yellow, Deep Indigo, and Cinnamon Brown.

Sol-Edge and Dune-Song, a matched pair of thirty-inch curved scimitars with blades of translucent golden Amber-glass fused into serrated bell-bronze spines; three tuning-slots cut along the flat of each blade whistle and glow like furnace slits when swung.

Crouched low on one knee mid-slide across copper sand, body twisted forward, both curved glowing sabers crossed in an "X" in front of his face as sparks of orange and violet light fly from the point where the two blades touch.

Sweeping crescent arcs of mirage heat-shimmer and fiery saffron-gold light that linger in the air behind his sword swings like glowing ribbons, accompanied by sharp, metallic ringing harmonics.

He is Kaelen Vos, the Sun-Blade, a human melee fighter of the Verdant Chorus Free Clans from Kal-Zir. Preserve a late-twenties face with sharp cheekbones, copper-gold kohl-lined eyes, a cocky half-smile, a faint white scar across the nose bridge and swept-back shoulder-length jet-black hair with a braided leather headband and one small amber prism. The saffron scarf, open cinnamon leather vest, copper scales, wind-harp rib pauldrons and indigo waist sash must be distinct. Exactly two separate deeply curved sabers, each one continuous blade and one hilt, held in anatomically plausible forward and reverse grips. Put their crossing just below eye level so both eyes and the nose scar remain readable. Tiny orange and muted violet contact sparks only; keep the general scene ochre, indigo and umber rather than broadly violet. Single character, knees-up three-quarter pose, slight low angle, generous dark clearance around the head, weapon tips and shoulders; figure fills about 70 percent of image height. Keep the defining action from the description, adapting feet and ground effects to the knee-up crop, and keep all focal equipment within the canvas. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: both complete amber/bronze curved sabers fit, nose scar and amber headband prism read, copper scales, saffron scarf and indigo sash support the crouching slide. Strong bristle oil treatment. Weakest points: blade glow competes with the face and the grips read more similarly than the requested forward/reverse pairing.

References for this attempt: candidate-a.png, anchor-2-hero.png and discarded Attempt 1 as identity reference.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

Lean, athletic, and coiled like a panther (around five feet ten inches), with a sharp V-shaped upper torso, billowy desert trousers gathered into bronze shin-greaves, a long flowing saffron scarf trailing two yards behind him, and twin deeply curved scimitars held in reverse and forward grips.

Sun-bronzed human skin in his late twenties; sharp cheekbones with a warm, cocky half-smile; striking copper-gold eyes lined with dark desert kohl against sun-glare; tousled, shoulder-length jet-black hair swept back by a braided leather headband set with an amber prism; a faint white scar across the bridge of his nose.

An open-chested vest of supple cinnamon-brown dune-drake leather reinforced with overlapping scales of hammered rose-gold and copper; asymmetrical pauldrons made from curved bronze wind-harp ribs; silk waist-sashes in vibrant saffron yellow and deep indigo.

Hammered Copper, Saffron Yellow, Deep Indigo, and Cinnamon Brown.

Sol-Edge and Dune-Song, a matched pair of thirty-inch curved scimitars with blades of translucent golden Amber-glass fused into serrated bell-bronze spines; three tuning-slots cut along the flat of each blade whistle and glow like furnace slits when swung.

Crouched low on one knee mid-slide across copper sand, body twisted forward, both curved glowing sabers crossed in an "X" in front of his face as sparks of orange and violet light fly from the point where the two blades touch.

Sweeping crescent arcs of mirage heat-shimmer and fiery saffron-gold light that linger in the air behind his sword swings like glowing ribbons, accompanied by sharp, metallic ringing harmonics.

He is Kaelen Vos, the Sun-Blade, a human melee fighter of the Verdant Chorus Free Clans from Kal-Zir. Preserve a late-twenties face with sharp cheekbones, copper-gold kohl-lined eyes, a cocky half-smile, a faint white scar across the nose bridge and swept-back shoulder-length jet-black hair with a braided leather headband and one small amber prism. The saffron scarf, open cinnamon leather vest, copper scales, wind-harp rib pauldrons and indigo waist sash must be distinct. Exactly two separate deeply curved sabers, each one continuous blade and one hilt, held in anatomically plausible forward and reverse grips. Put their crossing just below eye level so both eyes and the nose scar remain readable. Tiny orange and muted violet contact sparks only; keep the general scene ochre, indigo and umber rather than broadly violet. Single character, knees-up three-quarter pose, slight low angle, generous dark clearance around the head, weapon tips and shoulders; figure fills about 70 percent of image height. Keep the defining action from the description, adapting feet and ground effects to the knee-up crop, and keep all focal equipment within the canvas. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

Revision: reference image 3 is the first Kaelen splash, used for identity and equipment continuity only. Preserve his face, white nose scar, hair, headband, scarf, costume and crouching slide. Pull the camera back until both complete curved saber tips, both pommels, both hands and saffron scarf fit with at least 7 percent canvas-width dark clearance. Each blade must visibly connect to its own hilt as one continuous metal-and-amber object. Show exactly two sabers crossing below the eyes; one in a forward grip and the other in a reverse grip. Fit the knees-up figure inside the central 75 percent of image height. Reduce decorative scales and glowing arcs to broader three-tone paint masses so the face and twin-weapon silhouette stay readable.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/kaelen-vos/portrait.png`

- Tool: built-in `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Actual size: 1024 × 1536 px, opaque RGB PNG (all attempts).
- Re-makes: 0. First attempt retained.
- Style references, in order: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (surface, stroke scale, edge economy, palette, materials and light only).
- Identity reference 3: `art/characters/kaelen-vos/splash.png`, retained final splash; same face, hair, colours and costume.

### Attempt 1 — retained

Retained first attempt: close bust clearly preserves sun-bronzed skin, copper-gold kohl-lined eyes, white nose scar, tousled black hair, braided headband with amber prism, saffron scarf and copper/indigo clothing. Strong oil strokes and warm/cool light. Weakest point: the saffron scarf occupies a large bright mass and competes slightly with the face; tiny metal scales remain detailed.

References for this attempt: candidate-a.png, anchor-2-hero.png and this character's retained splash.png as identity reference.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Portrait: bust three-quarter view, 85 mm lens, face and shoulders dominate, faceted brush planes on cheeks and nose, sharp eyes, subdued plain painterly background fading to #11151E, portrait 2:3.

Lean, athletic, and coiled like a panther (around five feet ten inches), with a sharp V-shaped upper torso, billowy desert trousers gathered into bronze shin-greaves, a long flowing saffron scarf trailing two yards behind him, and twin deeply curved scimitars held in reverse and forward grips.

Sun-bronzed human skin in his late twenties; sharp cheekbones with a warm, cocky half-smile; striking copper-gold eyes lined with dark desert kohl against sun-glare; tousled, shoulder-length jet-black hair swept back by a braided leather headband set with an amber prism; a faint white scar across the bridge of his nose.

An open-chested vest of supple cinnamon-brown dune-drake leather reinforced with overlapping scales of hammered rose-gold and copper; asymmetrical pauldrons made from curved bronze wind-harp ribs; silk waist-sashes in vibrant saffron yellow and deep indigo.

Hammered Copper, Saffron Yellow, Deep Indigo, and Cinnamon Brown.

Sol-Edge and Dune-Song, a matched pair of thirty-inch curved scimitars with blades of translucent golden Amber-glass fused into serrated bell-bronze spines; three tuning-slots cut along the flat of each blade whistle and glow like furnace slits when swung.

Crouched low on one knee mid-slide across copper sand, body twisted forward, both curved glowing sabers crossed in an "X" in front of his face as sparks of orange and violet light fly from the point where the two blades touch.

Sweeping crescent arcs of mirage heat-shimmer and fiery saffron-gold light that linger in the air behind his sword swings like glowing ribbons, accompanied by sharp, metallic ringing harmonics.

He is Kaelen Vos, the Sun-Blade, a human melee fighter of the Verdant Chorus Free Clans from Kal-Zir. Preserve a late-twenties face with sharp cheekbones, copper-gold kohl-lined eyes, a cocky half-smile, a faint white scar across the nose bridge and swept-back shoulder-length jet-black hair with a braided leather headband and one small amber prism. The saffron scarf, open cinnamon leather vest, copper scales, wind-harp rib pauldrons and indigo waist sash must be distinct. Exactly two separate deeply curved sabers, each one continuous blade and one hilt, held in anatomically plausible forward and reverse grips. Put their crossing just below eye level so both eyes and the nose scar remain readable. Tiny orange and muted violet contact sparks only; keep the general scene ochre, indigo and umber rather than broadly violet. Identity reference image 3 is this character's approved splash.png: preserve exactly the same facial structure, age, skin, hair arrangement, ears, accessories, costume colours, armour construction and equipment design. Tighten to a bust three-quarter composition with an 85 mm lens and planar painted skin. Face and shoulders dominate; eyes are the sharpest focal point. Adapt the action to a calm confident bust pose, with only partial equipment at the lower edge; do not cram the full-body action or complete weapon into this close portrait. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

Final framing priority: this is a close head-and-shoulders bust, not a waist-up view. Frame from just above the hair to the upper chest, cropping horizontally through the upper breastplate or collarbone-level costume. The face alone should occupy roughly 40 percent of canvas height, the head including hair about 55 percent. Shoulders extend beyond the lower side edges. Leave 8 percent headroom. Omit hands and full weapons; at most a small staff edge, shoulder pipe or boiler detail may appear beside the shoulder. Keep both eyes, nose, mouth, chin, ear tips and principal hair ornaments visible. The background is subdued broad indigo paint with just a few ochre strokes, so the face is the strongest contrast.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/tessa-vane-kettler/splash.png`

- Tool: built-in `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Actual size: 1024 × 1536 px, opaque RGB PNG (all attempts).
- Re-makes: 1. Reasons are recorded with the discarded attempt below.
- Style references, in order: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (surface, stroke scale, edge economy, palette, materials and light only).
- Remake identity reference 3: this image's discarded Attempt 1; subject/equipment continuity only, with targeted corrections below.

### Attempt 1 — discarded

Bell muzzle clipped on right; tight framing and busy small fittings.

References for this attempt: candidate-a.png and anchor-2-hero.png.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

Compact, sturdy, and powerfully built Brannik woman (around four feet ten inches tall, broad-shouldered and muscular), whose unmistakable silhouette is doubled in width by a massive brass-and-iron boiler backpack with two smoking chimneys and an oversized, bell-muzzled cannon cradled across her hip like a ship's swivel-gun.

Warm, ruddy-tan skin smudged with honest forge-soot across her nose and cheek; bright, fiercely intelligent furnace-orange eyes; a broad, confident grin showing a gold-capped canine tooth; thick, copper-red hair piled into a messy top-knot held together by brass calipers and multi-lensed magnifying goggles pushed up on her forehead.

A heavy apron-coat of fireproof soot-black salamander leather over riveted plates of hammered copper; thick padded welding gauntlets stained with glowing amber grease; a heavy tool-belt hung with brass monkey-wrenches, pressure gauges, and glowing orange glass mortar shells.

Hammered Copper, Furnace Orange, Soot Black, and Brass Gold.

The Caul-Cracker, a four-foot-long portable siege mortar made of blackened cast iron and bound in thick copper cooling-coils, featuring a flared church-bell muzzle and a transparent central chamber where glowing molten orange Sun-Pitch sloshes under pressure.

Braced wide with one heavy steel-toed boot propped up on a ticking brass turret box, leaning her hip into the kick of her smoking mortar cannon while pulling the brass pressure-whistle chain on her shoulder with a gleeful laugh.

Arcing parabolic trails of black smoke and blinding orange-gold liquid fire that burst on impact into ringing concentric brass gear-runes and pools of bubbling amber slag.

She is Tessa Vane-Kettler, the Foundry-Artillerist, a Brannik ranged engineer of the Iron-Chime Syndicate. Preserve her compact broad muscular adult proportions, rounded strong face, broad nose, furnace-orange eyes, soot across nose and cheek, mischievous broad grin with one gold-capped canine, copper-red messy top-knot secured by brass calipers, and multi-lens goggles pushed onto her forehead. Exactly two smoking backpack chimneys. The Caul-Cracker is one enormous black cast-iron mortar with copper cooling coils, one flared bell muzzle and one transparent orange pressure chamber. Her left forearm cradles its weight against her hip while her right padded glove pulls the shoulder whistle-chain. Keep the two hands separate and legible. Gauges are blank instrument faces without numbers, the pressure effects are abstract nonlinguistic gear-like rings. Restrict fire and smoke to small accents so face and equipment silhouette dominate. Single character, knees-up three-quarter pose, slight low angle, generous dark clearance around the head, weapon tips and shoulders; figure fills about 70 percent of image height. Keep the defining action from the description, adapting feet and ground effects to the knee-up crop, and keep all focal equipment within the canvas. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: full bell muzzle, orange pressure chamber, copper cooling coils, two smoking chimneys, compact broad build, soot, goggles, copper top-knot and gold canine are present. Strong black-leather/copper oil planes. Weakest points: muzzle clearance remains narrow and the requested boot-on-turret action is outside the knees-up crop.

References for this attempt: candidate-a.png, anchor-2-hero.png and discarded Attempt 1 as identity reference.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Character splash: knees-up three-quarter view, 50 mm standard lens, slight low angle, subject fills about 70% of the height, plain painterly background fading to #11151E, distinct cloak and weapon silhouette for a 200 px card, portrait 2:3.

Compact, sturdy, and powerfully built Brannik woman (around four feet ten inches tall, broad-shouldered and muscular), whose unmistakable silhouette is doubled in width by a massive brass-and-iron boiler backpack with two smoking chimneys and an oversized, bell-muzzled cannon cradled across her hip like a ship's swivel-gun.

Warm, ruddy-tan skin smudged with honest forge-soot across her nose and cheek; bright, fiercely intelligent furnace-orange eyes; a broad, confident grin showing a gold-capped canine tooth; thick, copper-red hair piled into a messy top-knot held together by brass calipers and multi-lensed magnifying goggles pushed up on her forehead.

A heavy apron-coat of fireproof soot-black salamander leather over riveted plates of hammered copper; thick padded welding gauntlets stained with glowing amber grease; a heavy tool-belt hung with brass monkey-wrenches, pressure gauges, and glowing orange glass mortar shells.

Hammered Copper, Furnace Orange, Soot Black, and Brass Gold.

The Caul-Cracker, a four-foot-long portable siege mortar made of blackened cast iron and bound in thick copper cooling-coils, featuring a flared church-bell muzzle and a transparent central chamber where glowing molten orange Sun-Pitch sloshes under pressure.

Braced wide with one heavy steel-toed boot propped up on a ticking brass turret box, leaning her hip into the kick of her smoking mortar cannon while pulling the brass pressure-whistle chain on her shoulder with a gleeful laugh.

Arcing parabolic trails of black smoke and blinding orange-gold liquid fire that burst on impact into ringing concentric brass gear-runes and pools of bubbling amber slag.

She is Tessa Vane-Kettler, the Foundry-Artillerist, a Brannik ranged engineer of the Iron-Chime Syndicate. Preserve her compact broad muscular adult proportions, rounded strong face, broad nose, furnace-orange eyes, soot across nose and cheek, mischievous broad grin with one gold-capped canine, copper-red messy top-knot secured by brass calipers, and multi-lens goggles pushed onto her forehead. Exactly two smoking backpack chimneys. The Caul-Cracker is one enormous black cast-iron mortar with copper cooling coils, one flared bell muzzle and one transparent orange pressure chamber. Her left forearm cradles its weight against her hip while her right padded glove pulls the shoulder whistle-chain. Keep the two hands separate and legible. Gauges are blank instrument faces without numbers, the pressure effects are abstract nonlinguistic gear-like rings. Restrict fire and smoke to small accents so face and equipment silhouette dominate. Single character, knees-up three-quarter pose, slight low angle, generous dark clearance around the head, weapon tips and shoulders; figure fills about 70 percent of image height. Keep the defining action from the description, adapting feet and ground effects to the knee-up crop, and keep all focal equipment within the canvas. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

Revision: reference image 3 is the first Tessa splash, used for identity and equipment continuity only. Preserve her face, top-knot, calipers, goggles, gold canine, two-chimney boiler, left cradling glove and right chain-pulling glove. Pull the camera back and shorten the mortar's foreshortening so its entire flared church-bell muzzle fits inside the right edge with at least 8 percent canvas-width empty dark clearance. Show one complete, continuous four-foot mortar across her hip, including the black bell muzzle, copper cooling coils and orange glass chamber. Keep the knees-up figure within the central 75 percent of image height. Simplify tiny rivets, gauges and straps into broad bristle planes. Restrained orange chamber light, not a large firing blast.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/characters/tessa-vane-kettler/portrait.png`

- Tool: built-in `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Actual size: 1024 × 1536 px, opaque RGB PNG (all attempts).
- Re-makes: 0. First attempt retained.
- Style references, in order: `art/style/candidate-a.png`, `art/style/anchor-2-hero.png` (surface, stroke scale, edge economy, palette, materials and light only).
- Identity reference 3: `art/characters/tessa-vane-kettler/splash.png`, retained final splash; same face, hair, colours and costume.

### Attempt 1 — retained

Retained first attempt: close bust clearly preserves broad ruddy-tan face, soot streak, orange eyes, gold canine, copper-red top-knot, calipers, multi-lens goggles, copper shoulders and black foundry leather. Thick impasto and indigo backdrop match. Weakest point: the boiler and second chimney are cropped as peripheral equipment, and the gold canine reads more pointed than in the splash.

References for this attempt: candidate-a.png, anchor-2-hero.png and this character's retained splash.png as identity reference.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Portrait: bust three-quarter view, 85 mm lens, face and shoulders dominate, faceted brush planes on cheeks and nose, sharp eyes, subdued plain painterly background fading to #11151E, portrait 2:3.

Compact, sturdy, and powerfully built Brannik woman (around four feet ten inches tall, broad-shouldered and muscular), whose unmistakable silhouette is doubled in width by a massive brass-and-iron boiler backpack with two smoking chimneys and an oversized, bell-muzzled cannon cradled across her hip like a ship's swivel-gun.

Warm, ruddy-tan skin smudged with honest forge-soot across her nose and cheek; bright, fiercely intelligent furnace-orange eyes; a broad, confident grin showing a gold-capped canine tooth; thick, copper-red hair piled into a messy top-knot held together by brass calipers and multi-lensed magnifying goggles pushed up on her forehead.

A heavy apron-coat of fireproof soot-black salamander leather over riveted plates of hammered copper; thick padded welding gauntlets stained with glowing amber grease; a heavy tool-belt hung with brass monkey-wrenches, pressure gauges, and glowing orange glass mortar shells.

Hammered Copper, Furnace Orange, Soot Black, and Brass Gold.

The Caul-Cracker, a four-foot-long portable siege mortar made of blackened cast iron and bound in thick copper cooling-coils, featuring a flared church-bell muzzle and a transparent central chamber where glowing molten orange Sun-Pitch sloshes under pressure.

Braced wide with one heavy steel-toed boot propped up on a ticking brass turret box, leaning her hip into the kick of her smoking mortar cannon while pulling the brass pressure-whistle chain on her shoulder with a gleeful laugh.

Arcing parabolic trails of black smoke and blinding orange-gold liquid fire that burst on impact into ringing concentric brass gear-runes and pools of bubbling amber slag.

She is Tessa Vane-Kettler, the Foundry-Artillerist, a Brannik ranged engineer of the Iron-Chime Syndicate. Preserve her compact broad muscular adult proportions, rounded strong face, broad nose, furnace-orange eyes, soot across nose and cheek, mischievous broad grin with one gold-capped canine, copper-red messy top-knot secured by brass calipers, and multi-lens goggles pushed onto her forehead. Exactly two smoking backpack chimneys. The Caul-Cracker is one enormous black cast-iron mortar with copper cooling coils, one flared bell muzzle and one transparent orange pressure chamber. Her left forearm cradles its weight against her hip while her right padded glove pulls the shoulder whistle-chain. Keep the two hands separate and legible. Gauges are blank instrument faces without numbers, the pressure effects are abstract nonlinguistic gear-like rings. Restrict fire and smoke to small accents so face and equipment silhouette dominate. Identity reference image 3 is this character's approved splash.png: preserve exactly the same facial structure, age, skin, hair arrangement, ears, accessories, costume colours, armour construction and equipment design. Tighten to a bust three-quarter composition with an 85 mm lens and planar painted skin. Face and shoulders dominate; eyes are the sharpest focal point. Adapt the action to a calm confident bust pose, with only partial equipment at the lower edge; do not cram the full-body action or complete weapon into this close portrait. Use reference image 1 (candidate-a.png) and reference image 2 (anchor-2-hero.png) solely for oil surface, stroke scale, edge economy, palette, material treatment and lighting while inventing this subject and composition. Do not inherit their party, city, spire, helmet, sword or crimson cloak. Generate one opaque full-bleed PNG, exact portrait 2:3, at the largest native size available; target 2560 x 3840 pixels. No decorative surround.

Final framing priority: this is a close head-and-shoulders bust, not a waist-up view. Frame from just above the hair to the upper chest, cropping horizontally through the upper breastplate or collarbone-level costume. The face alone should occupy roughly 40 percent of canvas height, the head including hair about 55 percent. Shoulders extend beyond the lower side edges. Leave 8 percent headroom. Omit hands and full weapons; at most a small staff edge, shoulder pipe or boiler detail may appear beside the shoulder. Keep both eyes, nose, mouth, chin, ear tips and principal hair ornaments visible. The background is subdued broad indigo paint with just a few ochre strokes, so the face is the strongest contrast.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

# Phase 5 — the six world bosses

All six IDs were checked against `worldBosses` in `src/data/bosses.ts`; they match the requested filenames. Every call used `art/style/candidate-a.png` then `art/style/anchor-3-creature.png` as style references. Tool: built-in `image_gen.imagegen`; model: `gpt-image` confirmed in PNG provenance, exact revision not exposed. Each prompt requested the largest available native output, targeting 3840 × 2160, landscape exactly 16:9. The tool returned the native dimensions below, approximately 16:9, with no resolution selector exposed. Final PNGs retain native pixels without cropping, resizing, recolouring or added texture. All finals were inspected at original resolution and approximately 300 px wide; no visible text, logos, watermarks, painted frames, extra limbs or clipped focal silhouettes were found. Broad palette mixtures were also sampled: warm umber/brass neutrals dominate, with indigo and restrained viridian accents; hex anchors are not exact indexed colours. Prior ledger entries are retained.

## `art/bosses/toll-lion-of-dawn-watch.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- References, in order: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png` (style only).
- Actual size: 1672 × 941 px, opaque RGB PNG, native output; approximately 16:9.
- Re-makes: 0; first attempt retained.
- Review at full size and approximately 300 px: Candidate-matched ochre knife strokes, indigo atmosphere and selective teal rim; roaring feline face, brass bell-mane, four-legged stance and Chime-Posts are readable at 300 px. Full silhouette is contained. Weakest point: the foreground travellers are larger than the requested scale ratio, and the detailed bell-mane is busy at card size.

### Attempt 1 — final

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

a brass-maned lion the height of a bell-tower whose roar rings the Beacon and pulls every nearby Chime-Post into the fight. In the open Sun-Steppe of Aethel, a colossal natural lion with a heavy mane of weathered brass bell-like plates strides on four clearly articulated leonine legs, tawny planar hide and one sweeping tail. Show its open roaring feline head in three-quarter view; a restrained painted vibration stirs a few distant Chime-Posts around a Beacon. Dry ochre grass, limestone terraces, sparse distant bell towers under indigo clouds. Tiny travellers, each less than one thirtieth of the lion's height, stand far away beside a Chime-Post to establish bell-tower scale. Show all four paws, mane and tail inside generous safe margins. Keep the animal dominant and the landscape spare. Use the first supplied image, art/style/candidate-a.png, as the primary style reference and the second, art/style/anchor-3-creature.png, as the creature-scale and painted-material anchor. Borrow only their oil surface, broad stroke scale, edge economy, palette and lighting while inventing this subject and composition; do not copy their figures, city, spire, stone giant or crystals. Group into three bold value masses with large bristle planes, restrained focal detail and thin selective teal rim; make the defining silhouette readable at 300 px wide. Generate one opaque PNG in landscape exactly 16:9, requesting the largest available native size, target 3840 x 2160 pixels. No cropping of the focal silhouette.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/bosses/old-brass-back.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- References, in order: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png` (style only).
- Actual size: 1672 × 940 px, opaque RGB PNG, native output; approximately 16:9.
- Re-makes: 0; first attempt retained.
- Review at full size and approximately 300 px: Candidate-matched bristle planes, warm/cool separation and water painted in bold light strokes. Hooked snapping beak, domed shell carrying a flooded Architect temple, marsh and spreading waves communicate the description. Weakest point: water hides much of the feet and rear-leg articulation; temple masonry loses detail at 300 px.

### Attempt 1 — final

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A mountain-sized snapping turtle carrying a half-sunken Architect temple on its shell whose roar triggers tidal waves across the marsh. In the open Whispering Fen root basin, a colossal snapping turtle lumbers through a flooded marsh. Its powerful hooked beak roars and broad rippling tidal waves spread across the water. Its immense low domed shell carries one half-sunken ancient Architect temple, broken limestone colonnades visibly embedded into the shell and submerged in its flooded terraces. Four heavy reptilian legs, one long snapping-turtle tail, rough planar umber skin and tarnished brass scutes; retain recognisable snapping-turtle anatomy. Shallow water leaves the feet and stance readable. Marsh reeds and dark roots foreground, turtle and waves middle plane, distant swamp trees in indigo mist. A few tiny travellers on a ruined causeway, each less than one fiftieth of the turtle's height, establish mountain scale. Fit the complete head, shell temple, legs and tail within safe margins. Use the first supplied image, art/style/candidate-a.png, as the primary style reference and the second, art/style/anchor-3-creature.png, as the creature-scale and painted-material anchor. Borrow only their oil surface, broad stroke scale, edge economy, palette and lighting while inventing this subject and composition; do not copy their figures, city, spire, stone giant or crystals. Group into three bold value masses with large bristle planes, restrained focal detail and thin selective teal rim; make the defining silhouette readable at 300 px wide. Generate one opaque PNG in landscape exactly 16:9, requesting the largest available native size, target 3840 x 2160 pixels. No cropping of the focal silhouette.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/bosses/smelter-heart.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- References, in order: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png` (style only).
- Actual size: 1672 × 941 px, opaque RGB PNG, native output; approximately 16:9.
- Re-makes: 0; first attempt retained.
- Review at full size and approximately 300 px: Oil impasto and weathered slag planes match the references; a colossal quadrupedal slag-drake in the open coastal smeltery spills Amber-glass from split chest plates. Head, feet and tail stay within the image. Weakest point: the bright molten floor and background pours compete with the head, and the amber reads closer to molten metal than cooled glass.

### Attempt 1 — final

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

a slag-drake the size of a drydock nested in the Great Smeltery of Caul, cracking its chest plates to spill a moving floor of Amber-glass. In the Cinder-Reach Brass Coast, depict the open-air Great Smeltery of Caul as a vast ruined industrial drydock beside a smoky coast. A colossal wingless slag-drake, a low heavy quadrupedal reptile with exactly four powerful legs and one long tail, crawls from its nest between enormous smelting walls. Its drydock-sized body is blackened slag and weathered iron plates. Its upper chest plates crack open to spill luminous molten Amber-glass down onto the ground, spreading into a moving amber-glass floor beneath the drake; amber is ochre with pale hot cores, never saturated red lava. The head and split chest are the focal features. Tiny armoured travellers on a distant dock stair, each less than one fortieth of the drake's height, establish the immense scale. Preserve the complete horned head, four planted clawed feet and tail inside safe margins. Keep architecture sparse and subordinate. Use the first supplied image, art/style/candidate-a.png, as the primary style reference and the second, art/style/anchor-3-creature.png, as the creature-scale and painted-material anchor. Borrow only their oil surface, broad stroke scale, edge economy, palette and lighting while inventing this subject and composition; do not copy their figures, city, spire, stone giant or crystals. Group into three bold value masses with large bristle planes, restrained focal detail and thin selective teal rim; make the defining silhouette readable at 300 px wide. Generate one opaque PNG in landscape exactly 16:9, requesting the largest available native size, target 3840 x 2160 pixels. No cropping of the focal silhouette.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/bosses/dune-grinder.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- References, in order: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png` (style only).
- Actual size: 1672 × 941 px, opaque RGB PNG, native output; approximately 16:9.
- Re-makes: 0; first attempt retained.
- Review at full size and approximately 300 px: Broad ochre sand strokes and dark iron/brass planes match the references. A limbless mechanical worm, circular grinding mouth, furnace belly grates and threatened oasis camp clearly convey the description. Weakest point: dense mouth teeth merge at 300 px and airborne camp fragments are less legible than the silhouette.

### Attempt 1 — final

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A three-hundred-foot mechanical sand-worm left over from the Concordance War that swallows entire oasis camps to fuel its furnace belly. In the open Singing Dunes of Kal-Zir, a colossal three-hundred-foot mechanical sand-worm from the Concordance War rises in a single broad curved coil from ochre dunes. A long continuous limbless segmented body of battered black iron and tarnished brass, exposed geared interlocks and a circular toothed grinding mouth; no humanoid face, no arms and no legs. Furnace light glows through a few belly grates. The roaring mouth swallows a small oasis camp: a few tents and palms tilt toward it amid falling sand. Show the full readable above-ground worm arc and tapering tail, comfortably inside the frame, with lower body partially in sand. A few tiny fleeing travellers, each less than one fiftieth of its visible height, demonstrate colossal scale. Dark dune foreground, mechanical silhouette in the middle plane, pale distant dunes and dusty indigo horizon. Use the first supplied image, art/style/candidate-a.png, as the primary style reference and the second, art/style/anchor-3-creature.png, as the creature-scale and painted-material anchor. Borrow only their oil surface, broad stroke scale, edge economy, palette and lighting while inventing this subject and composition; do not copy their figures, city, spire, stone giant or crystals. Group into three bold value masses with large bristle planes, restrained focal detail and thin selective teal rim; make the defining silhouette readable at 300 px wide. Generate one opaque PNG in landscape exactly 16:9, requesting the largest available native size, target 3840 x 2160 pixels. No cropping of the focal silhouette.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/bosses/unstruck-pipe.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- References, in order: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png` (style only).
- Actual size: 1672 × 941 px, opaque RGB PNG, native output; approximately 16:9.
- Re-makes: 1; second attempt retained. Reason: disconnected distant body arcs in attempt 1.
- Review at full size and approximately 300 px: Retained remake has a single continuous brass organ-worm emerging from a frozen Boreal tube, with broad oil-painted snow, indigo ice and restrained teal cracks. Three much smaller travellers establish monumental scale. Weakest point: the implied mile-long extent and out-of-tune Wind-Wall cannot be read literally from this single visible coil.

### Attempt 1 — discarded

- Actual size: 1672 × 941 px, native PNG.
- Review: Discarded after full-size review: separate distant arcs looked like disconnected or duplicated worm bodies, weakening the required continuous anatomy. Remade once to show one visibly connected U-shaped body emerging from one frozen Boreal pipe.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

a mile-long brass organ-worm frozen inside a silent Boreal pipe, shaking loose when the Wind-Wall falls out of tune. In the open Frost-Chime Peaks, a colossal mile-long brass organ-worm is shaking loose from a silent Boreal pipe frozen into a mountainside. The creature has one continuous limbless segmented serpentine body, weathered brass organ-pipe components and a flared resonating mouth without a human face, arms or legs. The silent Boreal pipe is a separate gigantic hollow brass tube fractured open by ice; show clearly the worm emerging from inside its broken circular opening and one long coiling body sweeping across the snowy valley. Freeze-crusted brass, broken blue-indigo ice, distant Wind-Wall peaks and a few restrained atmospheric oscillation strokes imply the wind falling out of tune. Fit the complete visible worm silhouette inside safe margins. Tiny travellers, each less than one fiftieth of the worm's visible height, cross a narrow foreground ice ledge. Convey the mile-long scale with diminishing coils across multiple ridges, keeping one connected readable silhouette. Use the first supplied image, art/style/candidate-a.png, as the primary style reference and the second, art/style/anchor-3-creature.png, as the creature-scale and painted-material anchor. Borrow only their oil surface, broad stroke scale, edge economy, palette and lighting while inventing this subject and composition; do not copy their figures, city, spire, stone giant or crystals. Group into three bold value masses with large bristle planes, restrained focal detail and thin selective teal rim; make the defining silhouette readable at 300 px wide. Generate one opaque PNG in landscape exactly 16:9, requesting the largest available native size, target 3840 x 2160 pixels. No cropping of the focal silhouette.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — final

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

a mile-long brass organ-worm frozen inside a silent Boreal pipe, shaking loose when the Wind-Wall falls out of tune. In the open Frost-Chime Peaks, a colossal mile-long brass organ-worm is shaking loose from a silent Boreal pipe frozen into a mountainside. The creature has one continuous limbless segmented serpentine body, weathered brass organ-pipe components and a flared resonating mouth without a human face, arms or legs. The silent Boreal pipe is a separate gigantic hollow brass tube fractured open by ice; show clearly the worm emerging from inside its broken circular opening and one long coiling body sweeping across the snowy valley. Freeze-crusted brass, broken blue-indigo ice, distant Wind-Wall peaks and a few restrained atmospheric oscillation strokes imply the wind falling out of tune. Fit the complete visible worm silhouette inside safe margins. Tiny travellers, each less than one fiftieth of the worm's visible height, cross a narrow foreground ice ledge. Convey the mile-long scale with diminishing coils across multiple ridges, keeping one connected readable silhouette. Use the first supplied image, art/style/candidate-a.png, as the primary style reference and the second, art/style/anchor-3-creature.png, as the creature-scale and painted-material anchor. Borrow only their oil surface, broad stroke scale, edge economy, palette and lighting while inventing this subject and composition; do not copy their figures, city, spire, stone giant or crystals. Group into three bold value masses with large bristle planes, restrained focal detail and thin selective teal rim; make the defining silhouette readable at 300 px wide. Generate one opaque PNG in landscape exactly 16:9, requesting the largest available native size, target 3840 x 2160 pixels. No cropping of the focal silhouette.

Revision for anatomical continuity and scale: show exactly one worm and one continuous unbroken body. Simplify the composition: its flared brass organ-mouth emerges to the left of the broken Boreal tube at upper right, and its body curves downward into a single broad U-shaped foreground coil before returning continuously into the giant tube. Every connection must be visible and mechanically plausible. Omit all separate distant worm arcs and all disconnected body segments. Use mountain ridges and the tiny foreground figures, each only one fiftieth of the head-to-ground visible height, to convey its mile-long implied length. Keep the full creature silhouette comfortably inside the frame. Do not reproduce the candidate's four-person party; use only three tiny distant faceless silhouettes. Preserve the same broad oil impasto, ochre brass, indigo ice and restrained viridian light.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/bosses/shattered-colossus.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- References, in order: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png` (style only).
- Actual size: 1672 × 941 px, opaque RGB PNG, native output; approximately 16:9.
- Re-makes: 0; first attempt retained.
- Review at full size and approximately 300 px: Candidate-matched impasto, ochre edge light and indigo depth; fused white porcelain, captured bronze bells, coherent two-arm/two-leg anatomy and falling glass meteors distinguish the wandering mountain. Weakest point: dense bells compete with the small head and meteors can resemble suspended crystal shards at 300 px.

### Attempt 1 — final

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A wandering mountain of fused white porcelain and captured bronze bells that rains glass meteors across the endgame zone. In the open Shattered Crown endgame wasteland, a colossal wandering mountain with exactly two massive legs and two heavy arms is formed from fused broken white porcelain plates and captured weathered bronze bells. Its mountainlike shoulders and torso carry embedded bells of different sizes; pale porcelain is fractured into broad chisel planes, warm ochre on sunlit faces and indigo in cracks, never polished marble. A simple mask-like porcelain head above the shoulders; huge simplified hands with coherent fingers. A small sparse shower of jagged glass meteors falls through the sky around it, catching ochre sunlight and tiny restrained viridian cores. Ruined crown-like ridges, fractured ground and far misted monuments establish the Shattered Crown. Tiny travellers, each less than one fiftieth of its height, gather on a distant causeway. Keep the complete head, shoulders, arms and two planted feet in the frame with generous clearance; emphasise the unmistakable white porcelain and bronze-bell silhouette. Use the first supplied image, art/style/candidate-a.png, as the primary style reference and the second, art/style/anchor-3-creature.png, as the creature-scale and painted-material anchor. Borrow only their oil surface, broad stroke scale, edge economy, palette and lighting while inventing this subject and composition; do not copy their figures, city, spire, stone giant or crystals. Group into three bold value masses with large bristle planes, restrained focal detail and thin selective teal rim; make the defining silhouette readable at 300 px wide. Generate one opaque PNG in landscape exactly 16:9, requesting the largest available native size, target 3840 x 2160 pixels. No cropping of the focal silhouette.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

---

# Production Icon Contact Sheets (`art/sheets/`)

All production icon sheets were generated via the Nano Banana CLI (`gemini-api image -m gemini-3-pro-image-preview`) using `art/style/anchor-4-icons.png` and `art/style/candidate-a.png` as visual style references, following the locked four-part prompt contract in `docs/STYLE.md`. Because the CLI API returns `image/jpeg` buffers, each output was losslessly converted to an opaque RGB `.png` sheet before measuring per-subject bounding boxes into `art/sheets/crops.json` and cutting all 55 square icons via `art/sheets/cut.py`.

## `art/sheets/skills-valen-korr.png`

- References: `art/style/anchor-4-icons.png`, `art/style/candidate-a.png`
- Tool: `gemini-api image -m gemini-3-pro-image-preview -i art/style/anchor-4-icons.png -i art/style/candidate-a.png --aspect-ratio 4:3 --image-size 2K -o art/sheets/skills-valen-korr.png "$PROMPT"`
- Actual native size: 2400 × 1792 (4:3) px; opaque RGB PNG.
- Attempts: 1; first retained.
- Cut icons (`art/skills/valen-korr/*.png`): 12 square PNGs (536 × 536 px to 592 × 592 px).

### Attempt 1 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

A 4-column by 3-row contact sheet (aspect ratio 4:3) of exactly twelve independent skill-icon paintings for Valen Korr (Bell-Ward of the Seventh Arch; colour identity weathered bronze, pale limestone, and warm amber resonance), with 4 equal square cells per row across 3 equal rows, generous continuous empty flat #0B0D12 gutters, and no grid lines or frames. Every subject and all glow must stay strictly within the middle 72% of its own square cell, leaving wide uniform flat #0B0D12 dark gutters around all four sides of every icon so square crops never clip or touch neighbours. Place these twelve subjects in strict row-major order (Row 1 = The Unbroken Bastion, Row 2 = Resonant Bulwark, Row 3 = Earth-Shaker; Columns 1 to 4 = Tiers 1 to 4):
Row 1 Col 1 (brace-the-arch): A heavy bronze tower shield planted into cracked white limestone, glowing with a warm amber rim.
Row 1 Col 2 (limestone-marrow): Interlocking plates of pale carved stone and tarnished brass rivets, dusted with golden quarry grit.
Row 1 Col 3 (counter-toll): A cracked bronze bell edge mid-ring, sending out a jagged crescent of amber sparks.
Row 1 Col 4 (keystone-of-the-viaduct): A massive carved limestone keystone suspended in a halo of golden harmonic rings above a shattered floor.
Row 2 Col 1 (chord-of-sanctuary): A bronze tuning fork struck against a shield rim, radiating concentric ripples of warm golden light.
Row 2 Col 2 (echoing-aegis): Three overlapping translucent shields of amber light echoing outward from a tarnished brass core.
Row 2 Col 3 (guard-the-pilgrim): A heavy bronze gauntlet grasping a woven crimson-and-ochre cord that glows with protective warmth.
Row 2 Col 4 (the-first-striking): A colossal cathedral bell wreathed in blinding golden-white fire and a thin teal harmonic corona.
Row 3 Col 1 (gavel-of-judgement): A square-headed bronze warhammer smashing downward, trailing a comet-tail of ochre dust and sparks.
Row 3 Col 2 (fault-line-tremor): A jagged fissure in pale limestone glowing from within with molten amber resonance and rising pebbles.
Row 3 Col 3 (magnetic-pitch): Spiraling filings of dark iron and golden dust being pulled into a glowing bronze bell-mouth.
Row 3 Col 4 (sundering-cadence): Three concentric shockwaves of shattered stone and incandescent amber light erupting from a planted hammer.
Use the supplied reference images solely for oil impasto, stroke economy, palette and lighting. Background, all gutters, and outer margins must be one uniform flat #0B0D12 with no canvas grain, no vignette, no gradients, and no dividing lines.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/sheets/skills-lyra-vance.png`

- References: `art/style/anchor-4-icons.png`, `art/style/candidate-a.png`
- Tool: `gemini-api image -m gemini-3-pro-image-preview -i art/style/anchor-4-icons.png -i art/style/candidate-a.png --aspect-ratio 4:3 --image-size 2K -o art/sheets/skills-lyra-vance.png "$PROMPT"`
- Actual native size: 2400 × 1792 (4:3) px; opaque RGB PNG.
- Attempts: 1; first retained.
- Cut icons (`art/skills/lyra-vance/*.png`): 12 square PNGs (536 × 536 px to 596 × 596 px).

### Attempt 1 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

A 4-column by 3-row contact sheet (aspect ratio 4:3) of exactly twelve independent skill-icon paintings for Lyra Vance (Chime-Weaver of the Verdant Hollows; colour identity bioluminescent teal, warm amber sap, and deep moss green), with 4 equal square cells per row across 3 equal rows, generous continuous empty flat #0B0D12 gutters, and no grid lines or frames. Every subject and all glow must stay strictly within the middle 72% of its own square cell, leaving wide uniform flat #0B0D12 dark gutters around all four sides of every icon so square crops never clip or touch neighbours. Place these twelve subjects in strict row-major order (Row 1 = Living Tether, Row 2 = Canopy Bloom, Row 3 = Thorn-Chime; Columns 1 to 4 = Tiers 1 to 4):
Row 1 Col 1 (thread-of-warmth): A single braided vine glowing with warm amber sap and a soft teal aura, curling in a gentle spiral.
Row 1 Col 2 (symbiotic-pulse): Two luminous seed-pods connected by a figure-eight ribbon of golden and viridian light.
Row 1 Col 3 (mending-arpeggio): Three brass chime-bells hanging from a living branch, each trailing a droplet of glowing teal nectar.
Row 1 Col 4 (lifebond-canopy): A radiant crown of intertwined golden roots and teal-glowing leaves forming a protective dome.
Row 2 Col 1 (lantern-lily-seed): A cupping moss-green flower bud cradling a bright pearl of warm golden-teal light.
Row 2 Col 2 (dew-of-the-cataracts): A falling cascade of luminous teal water droplets catching warm golden sunlight against dark stone.
Row 2 Col 3 (censer-swing-full-bloom): An ornate brass censer mid-swing, spilling a thick swirling trail of golden pollen and teal petals.
Row 2 Col 4 (heart-of-root-cradle): A miniature ancient banyan tree with glowing teal foliage and warm amber lanterns hanging from its boughs.
Row 3 Col 1 (wasp-chord-lash): A segmented whip of thorny dark vine tipped with a stinger of incandescent teal crystal.
Row 3 Col 2 (resonance-harvest): A cluster of glowing amber berries bursting open as a wave of teal acoustic light passes through them.
Row 3 Col 3 (strangling-briars): Coiling black-green brambles with razor-sharp brass thorns and veins of glowing viridian sap.
Row 3 Col 4 (song-of-the-swarm): A swirling vortex of luminous teal-winged cicadas and golden chime-sparks rising from a cracked hollow log.
Use the supplied reference images solely for oil impasto, stroke economy, palette and lighting. Background, all gutters, and outer margins must be one uniform flat #0B0D12 with no canvas grain, no vignette, no gradients, and no dividing lines.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/sheets/skills-kaelen-vos.png`

- References: `art/style/anchor-4-icons.png`, `art/style/candidate-a.png`
- Tool: `gemini-api image -m gemini-3-pro-image-preview -i art/style/anchor-4-icons.png -i art/style/candidate-a.png --aspect-ratio 4:3 --image-size 2K -o art/sheets/skills-kaelen-vos.png "$PROMPT"`
- Actual native size: 2400 × 1792 (4:3) px; opaque RGB PNG.
- Attempts: 2; second retained.
- Cut icons (`art/skills/kaelen-vos/*.png`): 12 square PNGs (536 × 536 px to 596 × 596 px).

### Attempt 1 — discarded

First pass painted rectangular scene backdrops inside six of the twelve cells instead of floating frameless silhouettes on flat `#0B0D12`; remade once with explicit instructions forbidding square tile backdrops.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

A 4-column by 3-row contact sheet (aspect ratio 4:3) of exactly twelve independent skill-icon paintings for Kaelen Vos (Mirage-Dancer of the Sun-Slag Wastes; colour identity sunlit gold, crimson silk, and desert indigo), with 4 equal square cells per row across 3 equal rows, generous continuous empty flat #0B0D12 gutters, and no grid lines or frames. Every subject and all glow must stay strictly within the middle 72% of its own square cell, leaving wide uniform flat #0B0D12 dark gutters around all four sides of every icon so square crops never clip or touch neighbours. Place these twelve subjects in strict row-major order (Row 1 = Blade-Dancer of Kal-Zir, Row 2 = Sun-Edge Assassin, Row 3 = Wind-Harp Skirmisher; Columns 1 to 4 = Tiers 1 to 4):
Row 1 Col 1 (twin-note-slash): Two crossed curved sabres of darkened steel, their edges glowing with twin arcs of golden-white heat.
Row 1 Col 2 (tempo-of-the-mirage): A swirling crimson silk sash leaving three overlapping golden after-images in dark air.
Row 1 Col 3 (cross-blade-shatter): An X-shaped slash of incandescent amber light cutting through a fractured teal crystal.
Row 1 Col 4 (dervish-of-the-seven-winds): A cyclone of golden blade-arcs, crimson cloth ribbons, and glowing desert glass shards.
Row 2 Col 1 (mirage-step): A dissolving silhouette made of golden sand and heat-haze, stepping out of a shadow.
Row 2 Col 2 (molten-vein): A curved dagger blade dripping with liquid golden fire and a thin wisp of dark smoke.
Row 2 Col 3 (zenith-pierce): A single needle-sharp sabre point thrusting forward inside a cone of blinding golden-white light.
Row 2 Col 4 (noon-day-guillotine): A vertical pillar of solar gold and a descending crescent blade splitting a dark stone block in two.
Row 3 Col 1 (ringing-parry): A curved sabre deflecting a jagged bolt, throwing off a bright ring of teal and golden sparks.
Row 3 Col 2 (skiff-riders-footwork): A winged leather boot skimming over a ripple of glowing golden sand and teal wind-lines.
Row 3 Col 3 (deafening-crescendo): Twin sabres struck together like tuning forks, unleashing a jagged sphere of teal and amber soundwaves.
Row 3 Col 4 (gale-of-wind-harp-canyon): Three towering crescent blades of turquoise wind and golden dust tearing across dark stone.
Use the supplied reference images solely for oil impasto, stroke economy, palette and lighting. Background, all gutters, and outer margins must be one uniform flat #0B0D12 with no canvas grain, no vignette, no gradients, and no dividing lines.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: all twelve icons float cleanly as isolated silhouettes on a continuous uniform `#0B0D12` background with wide empty gutters.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

A 4-column by 3-row contact sheet (aspect ratio 4:3) of exactly twelve independent skill-icon paintings for Kaelen Vos (colour identity sunlit gold, crimson silk, and desert indigo). CRITICAL LAYOUT RULE: Do NOT paint square tiles, rectangular cards, sky backdrops, desert horizons, or box backgrounds behind any icon! Every single icon must be an isolated floating object silhouette painted directly on the shared, unbroken, uniform flat #0B0D12 sheet background, exactly like the reference sheet anchor-4-icons.png. Every object and its glow must stay inside the central 70% of its invisible cell with wide empty #0B0D12 space all around it. Place these twelve isolated floating subjects in strict row-major order (4 columns across, 3 rows down):
Row 1 Col 1 (twin-note-slash): Two crossed curved sabres of darkened steel floating on flat #0B0D12, their edges glowing with twin crescent arcs of golden-white heat.
Row 1 Col 2 (tempo-of-the-mirage): A single swirling S-curve of crimson silk sash with three tight golden after-image ribbons floating on flat #0B0D12.
Row 1 Col 3 (cross-blade-shatter): One compact teal crystal being split by an X-shaped slash of bright amber light, floating on flat #0B0D12.
Row 1 Col 4 (dervish-of-the-seven-winds): A compact circular whirl of four curved golden blades and crimson silk ribbons with glass shards floating on flat #0B0D12.
Row 2 Col 1 (mirage-step): A single hooded cloak-and-shoulder bust silhouette made of swirling golden sand grains and indigo shadow, floating on flat #0B0D12 with no ground or backdrop.
Row 2 Col 2 (molten-vein): One curved dagger blade dripping three drops of liquid golden fire and a wisp of dark smoke, floating on flat #0B0D12.
Row 2 Col 3 (zenith-pierce): One needle-sharp sabre tip thrusting diagonally upward with a tight cone of golden-white light around the blade, floating on flat #0B0D12.
Row 2 Col 4 (noon-day-guillotine): One vertical golden crescent blade cleaving a single small dark stone block in two with an amber spark burst, floating on flat #0B0D12.
Row 3 Col 1 (ringing-parry): One curved sabre blade parrying a small bolt, throwing off a tight ring of teal and golden sparks on flat #0B0D12.
Row 3 Col 2 (skiff-riders-footwork): One winged leather boot with a small curl of golden sand and a teal wind-ribbon underneath the sole, floating on flat #0B0D12.
Row 3 Col 3 (deafening-crescendo): Twin sabres struck together like tuning forks with a tight circular ring of teal and amber acoustic waves around the blades, floating on flat #0B0D12.
Row 3 Col 4 (gale-of-wind-harp-canyon): Three compact crescent arcs of turquoise wind and golden dust curving around a small jagged rock fragment, floating on flat #0B0D12.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no square icon tiles, no rectangular scene backgrounds, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/sheets/skills-tessa-vane-kettler.png`

- References: `art/style/anchor-4-icons.png`, `art/style/candidate-a.png`
- Tool: `gemini-api image -m gemini-3-pro-image-preview -i art/style/anchor-4-icons.png -i art/style/candidate-a.png --aspect-ratio 4:3 --image-size 2K -o art/sheets/skills-tessa-vane-kettler.png "$PROMPT"`
- Actual native size: 2400 × 1792 (4:3) px; opaque RGB PNG.
- Attempts: 2; second retained.
- Cut icons (`art/skills/tessa-vane-kettler/*.png`): 12 square PNGs (536 × 536 px to 570 × 570 px).

### Attempt 1 — discarded

First pass had several subjects (`red-line-rifling`, `cinder-crag-buster`, `smeltery-lungs`, `boiler-jump`) whose flames, beams, or upper boots were hard-clipped at an invisible box boundary; remade once with explicit instructions requiring self-contained rounded silhouettes inside the middle 70% of each cell.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

A 4-column by 3-row contact sheet (aspect ratio 4:3) of exactly twelve independent skill-icon paintings for Tessa Vane-Kettler (Siege-Artificer of the Brass Foundry; colour identity tarnished brass, furnace orange-gold, and gunmetal soot), with 4 equal square cells per row across 3 equal rows, generous continuous empty flat #0B0D12 gutters, and no grid lines or frames. Every subject and all glow must stay strictly within the middle 72% of its own square cell, leaving wide uniform flat #0B0D12 dark gutters around all four sides of every icon so square crops never clip or touch neighbours. Place these twelve subjects in strict row-major order (Row 1 = Siege-Bell Ballistics, Row 2 = Clockwork Acoustics, Row 3 = Demolitionist's Grit; Columns 1 to 4 = Tiers 1 to 4):
Row 1 Col 1 (sun-slag-lob): A heavy brass mortar shell mid-flight, cracked open to reveal a core of molten orange-gold slag.
Row 1 Col 2 (red-line-rifling): The fluted bell-mouth of a bronze cannon glowing cherry-red and amber from internal heat, wreathed in dark smoke.
Row 1 Col 3 (vent-valve-blast): A ruptured brass pressure valve spewing a twin jet of white-hot steam and golden cinders.
Row 1 Col 4 (cinder-crag-buster): A massive bell-shaped siege shell impacting stone in a mushroom-cloud of molten gold, crimson fire, and teal sparks.
Row 2 Col 1 (deploy-chime-thumper-mk-iv): A squat three-legged brass automaton with a spinning piston hammer and a glowing teal pressure gauge.
Row 2 Col 2 (synchronized-gearing): Three interlocking brass cogwheels turning together, throwing off a halo of golden and teal sparks.
Row 2 Col 3 (overclock-wrench-toss): A heavy iron spanner wrench spinning through the air, crackling with teal arc-lightning and amber heat.
Row 2 Col 4 (dock-seven-broadside): A row of three miniature brass siege bells firing in unison amidst a bank of illuminated gunsmoke.
Row 3 Col 1 (shatter-pitch-satchel): A stitched leather satchel strapped with brass canisters and a burning fuse spitting teal and golden sparks.
Row 3 Col 2 (smeltery-lungs): A heavy brass-and-leather respirator mask with glowing amber filter lenses and vents of warm steam.
Row 3 Col 3 (boiler-jump): A pair of iron-shod boots with brass exhaust nozzles blasting downward with jets of orange flame and smoke.
Row 3 Col 4 (the-caul-cracker-special): A spinning multi-barrelled brass gatling-mortar wreathed in a ring of muzzle flashes and golden shell casings.
Use the supplied reference images solely for oil impasto, stroke economy, palette and lighting. Background, all gutters, and outer margins must be one uniform flat #0B0D12 with no canvas grain, no vignette, no gradients, and no dividing lines.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained remake: all twelve icons are self-contained floating silhouettes with natural brushstroke edges surrounded by wide `#0B0D12` gutters.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

A 4-column by 3-row contact sheet (aspect ratio 4:3) of exactly twelve independent skill-icon paintings for Tessa Vane-Kettler (Siege-Artificer of the Brass Foundry; colour identity tarnished brass, furnace orange-gold, and gunmetal soot). CRITICAL FRAMING RULE: Every single icon must be a complete, self-contained object with a natural rounded silhouette that terminates cleanly inside the middle 70% of its cell on the shared flat #0B0D12 background. NEVER crop or clip flames, smoke, cannon barrels, boots, or explosions along a straight horizontal or vertical box edge! Place these twelve complete, unclipped floating subjects in strict row-major order (4 columns across, 3 rows down):
Row 1 Col 1 (sun-slag-lob): One compact brass mortar shell tilted diagonally, cracked open with a glowing molten orange-gold slag core and a short tail of embers, floating completely inside its cell on flat #0B0D12.
Row 1 Col 2 (red-line-rifling): One stubby bronze siege-bell cannon barrel seen in three-quarter macro view, its fluted muzzle glowing cherry-red and amber with a small curl of smoke, complete and unclipped on flat #0B0D12.
Row 1 Col 3 (vent-valve-blast): One round brass pressure valve wheel and pipe joint venting two short, self-contained puffs of golden steam and sparks on flat #0B0D12.
Row 1 Col 4 (cinder-crag-buster): One heavy bell-shaped brass siege shell striking a small chunk of stone with a compact, rounded burst of molten gold and teal sparks that stays completely inside the cell on flat #0B0D12.
Row 2 Col 1 (deploy-chime-thumper-mk-iv): One squat three-legged brass automaton with a piston hammer and a glowing teal pressure gauge, complete from top cap to all three feet on flat #0B0D12.
Row 2 Col 2 (synchronized-gearing): Three interlocking brass cogwheels throwing off a tight ring of golden and teal sparks on flat #0B0D12.
Row 2 Col 3 (overclock-wrench-toss): One heavy iron spanner wrench angled diagonally, crackling with tight teal arc-lightning and amber heat on flat #0B0D12.
Row 2 Col 4 (dock-seven-broadside): Three compact miniature brass siege-bell barrels mounted side-by-side on a single timber crossbar with short golden muzzle flashes, complete and unclipped on flat #0B0D12.
Row 3 Col 1 (shatter-pitch-satchel): One stitched leather demolition satchel strapped with three brass canisters and a short curly fuse spitting a teal-and-gold spark on flat #0B0D12.
Row 3 Col 2 (smeltery-lungs): One freestanding brass-and-leather respirator mask with glowing amber lenses and two small curls of warm steam at the side vents, floating on flat #0B0D12.
Row 3 Col 3 (boiler-jump): One pair of freestanding iron-shod boots (complete from boot cuffs to soles, no legs attached) with brass exhaust nozzles under the heels puffing short orange flames, floating on flat #0B0D12.
Row 3 Col 4 (the-caul-cracker-special): One compact multi-barrelled brass gatling-mortar drum surrounded by a tight circular ring of four small muzzle flashes on flat #0B0D12.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no square icon tiles, no straight-edge cropped effects, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/sheets/crafting-items-1.png`

- References: `art/style/anchor-4-icons.png`, `art/style/candidate-a.png`
- Tool: `gemini-api image -m gemini-3-pro-image-preview -i art/style/anchor-4-icons.png -i art/style/candidate-a.png --aspect-ratio 1:1 --image-size 2K -o art/sheets/crafting-items-1.png "$PROMPT"`
- Actual native size: 2048 × 2048 (1:1) px; opaque RGB PNG.
- Attempts: 1; first retained.
- Cut icons (`art/items/*.png`): 4 square PNGs (`harmonic-imprints.png` at 1024 × 1024 px, `chime-sigils.png` at 922 × 922 px, `lantern-oils.png` at 948 × 948 px, `campfire-feasts.png` at 1004 × 1004 px).

### Attempt 1 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Item icon: a single physical object, three-quarter view at 25–35° elevation, grounded by a soft contact shadow on a flat #0B0D12 field, two to three materials, two to three palette colours, no scene background, square 1:1.

A 2-column by 2-row square contact sheet (aspect ratio 1:1) of exactly four independent crafting item icons, with 2 equal square cells per row across 2 equal rows, wide continuous empty flat #0B0D12 gutters, and no grid lines or frames. Every item and its soft contact shadow or glow must stay strictly within the central 72% of its own quadrant cell, surrounded on all four sides by uniform flat #0B0D12 background so square crops never clip or touch neighbours. Place these four subjects in row-major order:
Row 1 Col 1 (harmonic-imprints): A stamped wax-and-bronze seal cradling a vibrating tuning fork, ringed by concentric golden soundwaves.
Row 1 Col 2 (chime-sigils): An engraved brass chime-plate bound with crimson silk cord, glowing with a teal acoustic glyph.
Row 2 Col 1 (lantern-oils): A faceted glass flask of luminous amber-teal oil stoppered with brass and wax, trailing a warm vapour wisp.
Row 2 Col 2 (campfire-feasts): A hammered copper cauldron brimming with golden spiced stew, crusty flatbread loaves, and fragrant steam over glowing coals.
Use the supplied reference images solely for oil impasto, stroke economy, palette and lighting. Background, all gutters, and outer margins must be one uniform flat #0B0D12 with no canvas grain, no vignette, no gradients, and no dividing lines.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/sheets/crafting-items-2.png`

- References: `art/style/anchor-4-icons.png`, `art/style/candidate-a.png`
- Tool: `gemini-api image -m gemini-3-pro-image-preview -i art/style/anchor-4-icons.png -i art/style/candidate-a.png --aspect-ratio 1:1 --image-size 2K -o art/sheets/crafting-items-2.png "$PROMPT"`
- Actual native size: 2048 × 2048 (1:1) px; opaque RGB PNG.
- Attempts: 1; first retained.
- Cut icons (`art/items/*.png`): 3 square PNGs (`architect-clockwork-parts.png` at 930 × 930 px, `sun-baked-supply-caches.png` at 926 × 926 px, `dead-pitch-crystal-nodes.png` at 922 × 922 px). Fourth quadrant is intentionally blank `#0B0D12`.

### Attempt 1 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Item icon: a single physical object, three-quarter view at 25–35° elevation, grounded by a soft contact shadow on a flat #0B0D12 field, two to three materials, two to three palette colours, no scene background, square 1:1.

A 2-column by 2-row square contact sheet (aspect ratio 1:1) containing three independent crafting item icons in the first three quadrants and a completely blank fourth quadrant, with 2 equal square cells per row across 2 equal rows, wide continuous empty flat #0B0D12 gutters, and no grid lines or frames. Every item and its soft contact shadow or glow must stay strictly within the central 72% of its own quadrant cell, surrounded on all four sides by uniform flat #0B0D12 background so square crops never clip or touch neighbours. Place these subjects in row-major order:
Row 1 Col 1 (architect-clockwork-parts): Interlocking ancient brass escapement gears, coiled mainsprings, and a tiny glowing teal crystal lens on oiled leather.
Row 1 Col 2 (sun-baked-supply-caches): A weathered terracotta amphora and rope-lashed timber crate half-buried in golden dust, glinting with brass fittings.
Row 2 Col 1 (dead-pitch-crystal-nodes): A jagged cluster of smoky grey-violet quartz veined with fractures of incandescent amber and teal resonance.
Row 2 Col 2 (empty cell): Leave the bottom-right quadrant completely empty, filled only with the solid flat #0B0D12 background colour and no object or mark of any kind.
Use the supplied reference images solely for oil impasto, stroke economy, palette and lighting. Background, all gutters, the empty fourth cell, and outer margins must be one uniform flat #0B0D12 with no canvas grain, no vignette, no gradients, and no dividing lines.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

# Phase 5 — The six mounts

All images use the built-in image tool with opaque backgrounds. References, in order: `art/style/candidate-a.png` (primary surface, strokes, edges, palette and lighting), `art/style/anchor-3-creature.png` (creature materials, overriding boss scale), `art/style/anchor-2-hero.png` (material separation and isolated backdrop, overriding human anatomy). Every final was visually reviewed at native 1536 × 1024 and 300 × 200 card size. The largest native exact 3:2 output was requested with a 3840 × 2560 target; the tool returned 1536 × 1024 for every attempt. Final assets are the original native RGB PNGs, copied without resizing, cropping, recolouring or texture overlays. Thumbnail resizing was for review only. Palette sampling confirmed dark indigo/umber masses and warm ochre/brass mixtures, rather than exact indexed hex matches. Model identifier and revision are not exposed by the tool.

## `art/mounts/aethel-sun-courser.png`

- Tool: built-in `image_gen.imagegen`.
- Model: not exposed; no model selector is available.
- Size: 1536 × 1024 px, exact landscape 3:2, opaque RGB PNG; all attempts share this size.
- Re-makes: 0; attempt 1 retained.
- References: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png`, `art/style/anchor-2-hero.png`, as style references only.

Retained first attempt. Full-size review: muscular ivory horse, four coherent legs, long golden feather mane and tail, cobalt saddlecloth, empty leather saddle, chest barding with one bell, and heated-brass hooves all match. The candidate's bristle planes, ochre light and indigo backdrop remain visible; no text, watermark, logo, frame or anatomy fault observed. At 300 px, the bright horse and feather silhouette remain clear. Weakest point: feather translucency is suggested by bright edges more than actual see-through structure; fine barding ornament becomes busy at card size. Ear and feather clearance is tighter than the requested eight percent but nothing is clipped.

### Attempt 1 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

Aethel Sun-Courser of Kaelvorn. A tall, muscular equine steed with a coat of creamy ivory fur, hooves that glow like heated brass, and a long mane and tail of streaming, translucent golden feathers; clad in fitted cobalt-blue saddlecloth and burnished gold chest-barding set with a single chiming bell. Quiet proud walking stance, head toward the left, exactly four anatomically coherent horse legs staggered for readability. A functional brown leather riding saddle sits over the fitted cobalt cloth; the single bell hangs visibly at the centre of the breastplate. Make mane and tail visibly individual long feather forms with translucent ochre edges rather than ordinary horse hair. Restrained warm brass glow stays close to all four hooves. Show one saddled mount without a rider, entire silhouette comfortably inside the image with at least eight percent clearance. Use the supplied references in order: candidate-a.png is the primary authority for surface, stroke scale, edge economy, palette and lighting; anchor-3-creature.png supplies painted creature materials, overriding its monumental scale; anchor-2-hero.png supplies material separation and the isolated painterly backdrop, overriding human anatomy. Invent the requested mount and composition; do not inherit the party, city, spire, colossus or knight. Keep roughly sixty percent resting neutrals, thirty percent structural identity and at most ten percent saturated accents; crispest contrast at the head and defining feature, fewer marks toward the feet. The oil medium must remain evident at full size and around 300 px card width. Generate one opaque, full-bleed PNG at the largest native resolution available for exact landscape 3:2 (target 3840 x 2560 pixels, or the largest native exact 3:2 equivalent).

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/mounts/fen-strider-snapper.png`

- Tool: built-in `image_gen.imagegen`.
- Model: not exposed; no model selector is available.
- Size: 1536 × 1024 px, exact landscape 3:2, opaque RGB PNG; all attempts share this size.
- Re-makes: 1; attempt 2 retained. Discarded attempt 1: the far-side rear foot overlapped the near-side hind leg enough that only five foot contacts were clearly countable. Remade once to stagger all six feet while retaining the stone shell, mushrooms and tack.
- References: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png`, `art/style/anchor-2-hero.png`, as style references only.

Retained second attempt after one remake. Full-size review: six distinct foot contacts are visible, with three pairs along the torso; far-side middle and rear feet remain smaller and shadowed. Emerald/turquoise mottling, amber eye, broad flat head, river-stone dome, blue mushrooms and empty woven saddle/baskets match. Oil strokes, warm/cool planes and restrained mushroom light fit the references. At 300 px, reptile, shell and mushrooms read; the two small far-side feet need closer inspection. Weakest point: counting all six feet is still harder at card size. No visible text, watermark, logo, frame or extra limb.

### Attempt 1 — discarded

Discarded attempt 1: the far-side rear foot overlapped the near-side hind leg enough that only five foot contacts were clearly countable. Remade once to stagger all six feet while retaining the stone shell, mushrooms and tack.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

Fen-Strider Snapper of Kaelvorn. A stocky, fast-moving six-legged amphibious reptile with mottled emerald and turquoise scales, a broad flat head with glowing amber eyes, and a domed shell of weathered river-stone overgrown with glowing blue mushrooms and woven reed saddle-baskets. An alert low running-ready pose facing left, with exactly six sturdy reptile legs arranged as three anatomical pairs, each ending in one webbed clawed foot; stagger the far-side feet so all six can be counted separately. The requested six legs are its correct species anatomy, with no additional limbs. A reed riding saddle sits over the stone dome, flanked by the woven baskets; clustered small blue mushrooms grow around the saddle without covering it. Short thick tapered reptilian tail, amber eyes clearly set in the broad flat head. Keep emerald and turquoise mottling earthy and blue mushroom light small and painted. Show one saddled mount without a rider, entire silhouette comfortably inside the image with at least eight percent clearance. Use the supplied references in order: candidate-a.png is the primary authority for surface, stroke scale, edge economy, palette and lighting; anchor-3-creature.png supplies painted creature materials, overriding its monumental scale; anchor-2-hero.png supplies material separation and the isolated painterly backdrop, overriding human anatomy. Invent the requested mount and composition; do not inherit the party, city, spire, colossus or knight. Keep roughly sixty percent resting neutrals, thirty percent structural identity and at most ten percent saturated accents; crispest contrast at the head and defining feature, fewer marks toward the feet. The oil medium must remain evident at full size and around 300 px card width. Generate one opaque, full-bleed PNG at the largest native resolution available for exact landscape 3:2 (target 3840 x 2560 pixels, or the largest native exact 3:2 equivalent).

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Submitted prompt, verbatim (final):

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

Fen-Strider Snapper of Kaelvorn. A stocky, fast-moving six-legged amphibious reptile with mottled emerald and turquoise scales, a broad flat head with glowing amber eyes, and a domed shell of weathered river-stone overgrown with glowing blue mushrooms and woven reed saddle-baskets. An alert low running-ready pose facing left, with exactly six sturdy reptile legs arranged as three anatomical pairs, each ending in one webbed clawed foot; stagger the far-side feet so all six can be counted separately. The requested six legs are its correct species anatomy, with no additional limbs. A reed riding saddle sits over the stone dome, flanked by the woven baskets; clustered small blue mushrooms grow around the saddle without covering it. Short thick tapered reptilian tail, amber eyes clearly set in the broad flat head. Keep emerald and turquoise mottling earthy and blue mushroom light small and painted. Show one saddled mount without a rider, entire silhouette comfortably inside the image with at least eight percent clearance. Use the supplied references in order: candidate-a.png is the primary authority for surface, stroke scale, edge economy, palette and lighting; anchor-3-creature.png supplies painted creature materials, overriding its monumental scale; anchor-2-hero.png supplies material separation and the isolated painterly backdrop, overriding human anatomy. Invent the requested mount and composition; do not inherit the party, city, spire, colossus or knight. Keep roughly sixty percent resting neutrals, thirty percent structural identity and at most ten percent saturated accents; crispest contrast at the head and defining feature, fewer marks toward the feet. The oil medium must remain evident at full size and around 300 px card width. Generate one opaque, full-bleed PNG at the largest native resolution available for exact landscape 3:2 (target 3840 x 2560 pixels, or the largest native exact 3:2 equivalent).

Revision for six-legged anatomy only: place the reptile in a shallow side-three-quarter view, nearly side-on, head to the left. Show exactly six feet all independently visible, three near-side legs and three far-side legs, staggered in a clear walking gait. Lay out the six foot contact positions from left to right at approximately 18%, 30%, 43%, 56%, 69% and 81% of canvas width, with far-side feet slightly higher in the image. Each foot must connect visibly to its own leg, with gaps between all six lower legs and no merged claws. Keep three shoulder/hip attachment pairs along the long torso. Reduce shell overhang and basket clutter just enough to reveal the limb roots. Keep its stocky flat-headed reptile identity, domed river-stone shell, emerald/turquoise mottling, amber eye, blue mushrooms and empty reed saddle with two baskets. Pull back enough for generous tail and nose clearance.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/mounts/frost-chime-crag-ram.png`

- Tool: built-in `image_gen.imagegen`.
- Model: not exposed; no model selector is available.
- Size: 1536 × 1024 px, exact landscape 3:2, opaque RGB PNG; all attempts share this size.
- Re-makes: 0; attempt 1 retained.
- References: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png`, `art/style/anchor-2-hero.png`, as style references only.

Retained first attempt. Full-size review: barrel chest, slate-grey and snow-white wool, two enormous curled horns with embedded blue-cyan quartz veins, empty brown saddle, heavy mountaineering packs, four iron crampon-shoes and hanging warm collar lantern all read. Bristle wool and rough horn planes match the oil references. At 300 px, horn silhouette and lantern stay clear. Weakest point: small crampon and pack hardware becomes dense, and quartz light leans toward the style's teal rather than a pure blue. No visible text, watermark, logo, frame or anatomy fault.

### Attempt 1 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

Frost-Chime Crag-Ram of Kaelvorn. A massive, barrel-chested mountain ram covered in thick slate-grey and snow-white wool, sporting huge curled horns naturally veined with glowing blue quartz, wearing heavy brown leather mountaineering packs, iron crampon-shoes, and a warm brass lantern swinging from its collar. Calm sure-footed standing pose facing left, exactly four strong ungulate legs with individually fitted iron crampon-shoes. Two massive curled horns frame the head, their rough natural horn surfaces crossed by a few embedded blue-quartz veins. Functional brown leather riding saddle between the mountaineering packs, clearly empty. Show the warm brass collar lantern as one readable hanging object. Broad bristle sweeps establish heavy wool without photoreal hair detail; crampons rest on one restrained stone patch. Show one saddled mount without a rider, entire silhouette comfortably inside the image with at least eight percent clearance. Use the supplied references in order: candidate-a.png is the primary authority for surface, stroke scale, edge economy, palette and lighting; anchor-3-creature.png supplies painted creature materials, overriding its monumental scale; anchor-2-hero.png supplies material separation and the isolated painterly backdrop, overriding human anatomy. Invent the requested mount and composition; do not inherit the party, city, spire, colossus or knight. Keep roughly sixty percent resting neutrals, thirty percent structural identity and at most ten percent saturated accents; crispest contrast at the head and defining feature, fewer marks toward the feet. The oil medium must remain evident at full size and around 300 px card width. Generate one opaque, full-bleed PNG at the largest native resolution available for exact landscape 3:2 (target 3840 x 2560 pixels, or the largest native exact 3:2 equivalent).

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/mounts/kal-zir-sand-skimmer.png`

- Tool: built-in `image_gen.imagegen`.
- Model: not exposed; no model selector is available.
- Size: 1536 × 1024 px, exact landscape 3:2, opaque RGB PNG; all attempts share this size.
- Re-makes: 0; attempt 1 retained.
- References: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png`, `art/style/anchor-2-hero.png`, as style references only.

Retained first attempt. Full-size review: continuous manta body without separate bird wings or legs, muted copper/rose-gold stripes, clear hover gap, exactly two long tail-ribbons each with a bronze chime, and an empty mahogany saddle beneath a canvas canopy match. Broad painterly facets and indigo/ochre background follow the references. At 300 px, hover, canopy and both ribbons remain distinct. Weakest point: the acoustic vibration reads as painted ground swirls, and the canopy's small fittings lose definition. Tail clearance is narrower than requested but both chimes remain inside the image. No visible text, watermark, logo or frame.

### Attempt 1 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

Kal-Zir Sand-Skimmer of Kaelvorn. A sleek, wingless desert manta-ray that hovers three feet above the ground on a cushion of acoustic vibration, with leathery hide patterned in copper and rose-gold stripes, twin long tail-ribbons tipped with bronze chimes, and a carved mahogany saddle with a canvas sun-canopy. Face left, broad continuous flattened manta body with organic lateral body lobes, no separate bird wings and no legs. Show exactly two distinct long flexible tail-ribbons extending rightward, each ending in a small bronze chime. A low carved mahogany riding saddle is visibly empty beneath a modest stretched canvas sun-canopy on wooden supports. A clear open gap below the body and its soft ground shadow establish the three-foot hover; represent acoustic vibration through a few subtle broken brush arcs near the ground, without luminous rings. Copper and rose-gold striping remains muted and leathery rather than metallic chrome. Show one saddled mount without a rider, entire silhouette comfortably inside the image with at least eight percent clearance. Use the supplied references in order: candidate-a.png is the primary authority for surface, stroke scale, edge economy, palette and lighting; anchor-3-creature.png supplies painted creature materials, overriding its monumental scale; anchor-2-hero.png supplies material separation and the isolated painterly backdrop, overriding human anatomy. Invent the requested mount and composition; do not inherit the party, city, spire, colossus or knight. Keep roughly sixty percent resting neutrals, thirty percent structural identity and at most ten percent saturated accents; crispest contrast at the head and defining feature, fewer marks toward the feet. The oil medium must remain evident at full size and around 300 px card width. Generate one opaque, full-bleed PNG at the largest native resolution available for exact landscape 3:2 (target 3840 x 2560 pixels, or the largest native exact 3:2 equivalent).

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/mounts/syndicate-gyro-hound.png`

- Tool: built-in `image_gen.imagegen`.
- Model: not exposed; no model selector is available.
- Size: 1536 × 1024 px, exact landscape 3:2, opaque RGB PNG; all attempts share this size.
- Re-makes: 0; attempt 1 retained.
- References: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png`, `art/style/anchor-2-hero.png`, as style references only.

Retained first attempt. Full-size review: coherent four-legged canine machine, hammered copper plating, blackened iron gears, small orange glass chest furnace, exactly two brass exhausts, empty saddle and contact sparks match. The copper is expressed with broken oil strokes rather than CGI gradients. At 300 px, wolf silhouette, saddle, twin pipes and furnace remain readable. Weakest point: small gears and rivets are busier than ideal, and the warm exhaust shimmer resembles faint smoke. No visible text, watermark, logo, frame or extra limb.

### Attempt 1 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

Syndicate Gyro-Hound of Kaelvorn. A rideable, wolf-sized quadrupedal machine built from riveted hammered copper plates and blackened iron gears, featuring a glowing orange glass furnace-heart in its chest, twin brass exhaust pipes trailing warm shimmer-waves, and articulated claw-paws that strike sparks on stone. An alert canine walking stance facing left, exactly four mechanically coherent articulated legs with separated claw-paws, a wolf-like head, two ears and one segmented tail. A fitted empty brown leather riding saddle is strapped to its back. Exactly two brass exhaust pipes rise behind the saddle, emitting faint painted warm heat distortions. The orange furnace-heart is a small clear focal glass aperture in its chest; a few tiny sparks rise where a leading claw-paw touches the simple stone ground. Hammered copper plates have broad dry-brushed facets, worn edges and sparse rivets; blackened iron gears remain readable without mechanical micro-detail. Show one saddled mount without a rider, entire silhouette comfortably inside the image with at least eight percent clearance. Use the supplied references in order: candidate-a.png is the primary authority for surface, stroke scale, edge economy, palette and lighting; anchor-3-creature.png supplies painted creature materials, overriding its monumental scale; anchor-2-hero.png supplies material separation and the isolated painterly backdrop, overriding human anatomy. Invent the requested mount and composition; do not inherit the party, city, spire, colossus or knight. Keep roughly sixty percent resting neutrals, thirty percent structural identity and at most ten percent saturated accents; crispest contrast at the head and defining feature, fewer marks toward the feet. The oil medium must remain evident at full size and around 300 px card width. Generate one opaque, full-bleed PNG at the largest native resolution available for exact landscape 3:2 (target 3840 x 2560 pixels, or the largest native exact 3:2 equivalent).

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/mounts/vitrified-sky-seraph.png`

- Tool: built-in `image_gen.imagegen`.
- Model: not exposed; no model selector is available.
- Size: 1536 × 1024 px, exact landscape 3:2, opaque RGB PNG; all attempts share this size.
- Re-makes: 1; attempt 2 retained. Discarded attempt 1: an upper prism wing tip reached the top edge and the overlapping wings did not clearly establish all four fans. Remade once for four separate wing fans, simpler blades and improved clearance.
- References: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png`, `art/style/anchor-2-hero.png`, as style references only.

Retained second attempt after one remake. Full-size review: four separate wing fans in two pairs, eagle head, two fore talons and two feline hind feet, one distinct tail, porcelain body, articulated gold joints, prism-blade feathers and empty silver leather saddle match. Opalescent and spectral reflections stay within the material; the oil surface, ochre/indigo light and painted edges remain coherent with the anchors. At 300 px, the four wing fans are separate, although their small blades blend together. Weakest point: porcelain is more faceted and gold ornament brighter than the ideal smooth opalescent material; upper wing clearance remains tighter than the requested ten percent, with no clipped tips. No visible text, watermark, logo, frame or extra limb.

### Attempt 1 — discarded

Discarded attempt 1: an upper prism wing tip reached the top edge and the overlapping wings did not clearly establish all four fans. Remade once for four separate wing fans, simpler blades and improved clearance.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

Vitrified Sky-Seraph of Kaelvorn. A majestic, four-winged gryphon-like creature sculpted entirely from smooth, opalescent white porcelain and articulated gold filigree joints, with feathers made of floating, chiming blades of rainbow-refracting prism glass and a saddle of spotless silver leather. Exactly four wings in two distinct anatomical pairs: the larger forward pair opens upward, the smaller rear pair fans lower behind it, with each wing root and outer tip visibly separate. One proud eagle-like head with porcelain beak, exactly four articulated gryphon legs (two fore talons and two feline hind legs), one tail, and the empty silver leather saddle visible between the wing pairs. Keep every wing tip, tail tip and claw within the safe margins. The opalescent porcelain body is smooth as a material but depicted through broad oil-paint planes and a few decisive highlights, with tarnished gold filigree joints. Floating prism-glass feather blades have restrained tiny spectral refractions only within the glass, not rainbow ambient illumination; mainly pale ochre, indigo and muted viridian reflections. Present a poised grounded stance with the wings arranged for a clean countable silhouette. Show one saddled mount without a rider, entire silhouette comfortably inside the image with at least eight percent clearance. Use the supplied references in order: candidate-a.png is the primary authority for surface, stroke scale, edge economy, palette and lighting; anchor-3-creature.png supplies painted creature materials, overriding its monumental scale; anchor-2-hero.png supplies material separation and the isolated painterly backdrop, overriding human anatomy. Invent the requested mount and composition; do not inherit the party, city, spire, colossus or knight. Keep roughly sixty percent resting neutrals, thirty percent structural identity and at most ten percent saturated accents; crispest contrast at the head and defining feature, fewer marks toward the feet. The oil medium must remain evident at full size and around 300 px card width. Generate one opaque, full-bleed PNG at the largest native resolution available for exact landscape 3:2 (target 3840 x 2560 pixels, or the largest native exact 3:2 equivalent).

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Submitted prompt, verbatim (final):

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

Vitrified Sky-Seraph of Kaelvorn. A majestic, four-winged gryphon-like creature sculpted entirely from smooth, opalescent white porcelain and articulated gold filigree joints, with feathers made of floating, chiming blades of rainbow-refracting prism glass and a saddle of spotless silver leather. Exactly four wings in two distinct anatomical pairs: the larger forward pair opens upward, the smaller rear pair fans lower behind it, with each wing root and outer tip visibly separate. One proud eagle-like head with porcelain beak, exactly four articulated gryphon legs (two fore talons and two feline hind legs), one tail, and the empty silver leather saddle visible between the wing pairs. Keep every wing tip, tail tip and claw within the safe margins. The opalescent porcelain body is smooth as a material but depicted through broad oil-paint planes and a few decisive highlights, with tarnished gold filigree joints. Floating prism-glass feather blades have restrained tiny spectral refractions only within the glass, not rainbow ambient illumination; mainly pale ochre, indigo and muted viridian reflections. Present a poised grounded stance with the wings arranged for a clean countable silhouette. Show one saddled mount without a rider, entire silhouette comfortably inside the image with at least eight percent clearance. Use the supplied references in order: candidate-a.png is the primary authority for surface, stroke scale, edge economy, palette and lighting; anchor-3-creature.png supplies painted creature materials, overriding its monumental scale; anchor-2-hero.png supplies material separation and the isolated painterly backdrop, overriding human anatomy. Invent the requested mount and composition; do not inherit the party, city, spire, colossus or knight. Keep roughly sixty percent resting neutrals, thirty percent structural identity and at most ten percent saturated accents; crispest contrast at the head and defining feature, fewer marks toward the feet. The oil medium must remain evident at full size and around 300 px card width. Generate one opaque, full-bleed PNG at the largest native resolution available for exact landscape 3:2 (target 3840 x 2560 pixels, or the largest native exact 3:2 equivalent).

Revision for wing count and safe margins: pull back substantially so the complete mount occupies no more than seventy percent of image height and eighty percent of image width. All prism tips must have at least ten percent image-height clearance at the top. Use a slightly more frontal side-three-quarter view so exactly four wing fans are individually visible: the near large wing sweeps to the upper left, the far large wing sweeps to the upper right, the near small rear wing spreads to the lower left, and the far small rear wing spreads to the lower right behind the saddle. Leave visible dark gaps between all four feather fans. Make each wing a compact fan with only a few large prism blades rather than hundreds of shards. Keep the silver leather saddle unobscured, the four legs countable, and the tail separate from all four wings. Reduce the overall ornament and preserve broad oil strokes, porcelain planes and small prismatic highlights.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

# Phase 5 — Six bestiary bosses

Each image uses `art/style/candidate-a.png` (reference 1) and `art/style/anchor-3-creature.png` (reference 2) solely for oil surface, stroke scale, edge economy, palette and lighting. Sources: the six `bosses` entries in `src/data/bosses.ts` and `content/lore.md` section 8. No world bosses generated.

Tool: built-in `image_gen.imagegen`; model: `gpt-image` from PNG provenance, exact revision not exposed. Every attempt requested the largest available native landscape 16:9 output, targeting 3840 × 2160. The tool exposes no size selector and returned 1672 × 941 px for all 14 attempts (approximately 16:9; ratio 1.77683 versus 1.77778). Final opaque RGB PNGs are unchanged native copies: no resizing, cropping, recolouring or texture overlays. Saved files were inspected at original size and as in-memory previews 300 px wide. No visible lettering, logos, watermarks, painted frames, broken faces, extra unintended limbs, anime, photoreal skin or glossy CGI observed in the retained images. Four arms on Vorgath and six wings on Avren are intentional canonical anatomy. Dominant oil-brush colour relationships were reviewed visually; exact palette hex reproduction is not claimed.

## `art/bosses/crucible-master-vorgath.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1672 × 941 px for every attempt; opaque native RGB PNG, approximately 16:9.
- References, in order: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png`.
- Attempts: 3; re-makes: 2. Discarded after full-size review: the four hammers, furnace and complete silhouette were clear, but the bell head flared downward rather than being inverted; green patina was too subdued and the anvil obscured one foot. Discarded: the inverted bell shape and green-patina bronze improved, but the shoulder cauldron was clipped by the upper edge.

### Attempt 1 — discarded

Discarded after full-size review: the four hammers, furnace and complete silhouette were clear, but the bell head flared downward rather than being inverted; green patina was too subdued and the anvil obscured one foot.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A massive, twenty-foot-tall heavy industrial automaton made of blackened cast iron and weathered green-patina bell-bronze, with a barrel-shaped torso housing a roaring white-hot grate furnace in its belly, a head shaped like an inverted church bell with a single glowing horizontal slit of orange fire, four heavy piston-driven arms wielding square-headed blacksmith hammers, and a huge, tilting cauldron overflowing with glowing liquid gold mounted across its hunched shoulders.

Crucible-Master Vorgath, The Unquenched Warden of Vault Four, in the drained Sunken Bell-Foundry. Pose hunched forward, legs widely braced beside a low anvil; precisely four mechanical arms, two emerging at each shoulder level, each anatomically connected and separately silhouetted, each holding exactly one square-headed blacksmith hammer, four hammers total. This four-arm design is intentional; there are no other arms. Separate the four hammer heads with background gaps. Show the upside-down bell head and its one orange horizontal eye slit above the barrel chest; a large tilting shoulder cauldron is clearly visible behind the head, with a small overflow stream of molten bronze. White-hot belly grate and liquid-gold metal use small near-white cores with ochre-orange paint bounce, never a broad red wash. Black iron and aged green-patina bronze stay rough and stroke-built. Spare setting: dark wet masonry foreground, the boss on a circular foundry floor in the middle, distant hazy hanging cooling bells and a broken roof admitting the required upper-left sun. Two tiny anonymous heroes at the lower left, each less than one seventh his height, establish twenty-foot scale.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — discarded

Discarded: the inverted bell shape and green-patina bronze improved, but the shoulder cauldron was clipped by the upper edge.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A massive, twenty-foot-tall heavy industrial automaton made of blackened cast iron and weathered green-patina bell-bronze, with a barrel-shaped torso housing a roaring white-hot grate furnace in its belly, a head shaped like an inverted church bell with a single glowing horizontal slit of orange fire, four heavy piston-driven arms wielding square-headed blacksmith hammers, and a huge, tilting cauldron overflowing with glowing liquid gold mounted across its hunched shoulders.

Crucible-Master Vorgath, The Unquenched Warden of Vault Four, in the drained Sunken Bell-Foundry. Pose hunched forward, legs widely braced beside a low anvil; precisely four mechanical arms, two emerging at each shoulder level, each anatomically connected and separately silhouetted, each holding exactly one square-headed blacksmith hammer, four hammers total. This four-arm design is intentional; there are no other arms. Separate the four hammer heads with background gaps. Show the upside-down bell head and its one orange horizontal eye slit above the barrel chest; a large tilting shoulder cauldron is clearly visible behind the head, with a small overflow stream of molten bronze. White-hot belly grate and liquid-gold metal use small near-white cores with ochre-orange paint bounce, never a broad red wash. Black iron and aged green-patina bronze stay rough and stroke-built. Spare setting: dark wet masonry foreground, the boss on a circular foundry floor in the middle, distant hazy hanging cooling bells and a broken roof admitting the required upper-left sun. Two tiny anonymous heroes at the lower left, each less than one seventh his height, establish twenty-foot scale.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

Revision for the bell head and aged materials: the head is an INVERTED church bell, physically upside down like a cup, with its broad flared circular bell-mouth lip at the TOP and its narrow closed crown at the BOTTOM where it joins the neck. Make that upside-down bell silhouette unmistakable; the single narrow horizontal orange eye slit crosses the side wall below the upper lip. Do not depict a conventional downward-flaring bell. Keep exactly four connected piston arms, four separate square blacksmith hammers, a white-hot grated belly furnace and a clearly separate overflowing cauldron mounted behind the head. Increase broad weathered green-patina paint planes on bronze shoulders and cauldron while leaving much of the torso blackened cast iron. Move the central anvil slightly to one side so both enormous feet and legs remain readable. Preserve full-body containment, warm upper-left key, indigo fill, rough bristle impasto and two tiny scale heroes.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 3 — retained

Retained: complete cauldron, four connected piston arms and square hammers, upside-down bell head with one orange slit, white-hot belly grate and patinated bronze match the subject. Warm ochre impasto, indigo foundry haze and broad bristle planes match the references. At 300 px the four-arm silhouette, cup-shaped bell head and furnace remain readable. Weakest point: dense mechanical fittings and the cauldron/furnace brightness compete with the head; the far foot remains partly lost in mist.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A massive, twenty-foot-tall heavy industrial automaton made of blackened cast iron and weathered green-patina bell-bronze, with a barrel-shaped torso housing a roaring white-hot grate furnace in its belly, a head shaped like an inverted church bell with a single glowing horizontal slit of orange fire, four heavy piston-driven arms wielding square-headed blacksmith hammers, and a huge, tilting cauldron overflowing with glowing liquid gold mounted across its hunched shoulders.

Crucible-Master Vorgath, The Unquenched Warden of Vault Four, in the drained Sunken Bell-Foundry. Pose hunched forward, legs widely braced beside a low anvil; precisely four mechanical arms, two emerging at each shoulder level, each anatomically connected and separately silhouetted, each holding exactly one square-headed blacksmith hammer, four hammers total. This four-arm design is intentional; there are no other arms. Separate the four hammer heads with background gaps. Show the upside-down bell head and its one orange horizontal eye slit above the barrel chest; a large tilting shoulder cauldron is clearly visible behind the head, with a small overflow stream of molten bronze. White-hot belly grate and liquid-gold metal use small near-white cores with ochre-orange paint bounce, never a broad red wash. Black iron and aged green-patina bronze stay rough and stroke-built. Spare setting: dark wet masonry foreground, the boss on a circular foundry floor in the middle, distant hazy hanging cooling bells and a broken roof admitting the required upper-left sun. Two tiny anonymous heroes at the lower left, each less than one seventh his height, establish twenty-foot scale.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

Revision for the bell head and aged materials: the head is an INVERTED church bell, physically upside down like a cup, with its broad flared circular bell-mouth lip at the TOP and its narrow closed crown at the BOTTOM where it joins the neck. Make that upside-down bell silhouette unmistakable; the single narrow horizontal orange eye slit crosses the side wall below the upper lip. Do not depict a conventional downward-flaring bell. Keep exactly four connected piston arms, four separate square blacksmith hammers, a white-hot grated belly furnace and a clearly separate overflowing cauldron mounted behind the head. Increase broad weathered green-patina paint planes on bronze shoulders and cauldron while leaving much of the torso blackened cast iron. Move the central anvil slightly to one side so both enormous feet and legs remain readable. Preserve full-body containment, warm upper-left key, indigo fill, rough bristle impasto and two tiny scale heroes.

Second revision for full silhouette containment: zoom the camera far enough out that the ENTIRE automaton including the shoulder cauldron, both raised hammer heads and both feet fits within the middle 72 percent of picture height. Leave a continuous band of plain cool foundry haze at least 12 percent image height above the highest edge of the cauldron and above every hammer. Lower the shoulder cauldron behind the head if necessary, but keep its complete oval rim visible and uncut. Move the low anvil to the far right side so both feet are separately visible. Keep the upside-down bell head, stronger green patina, barrel furnace, exactly four mechanical arms each with one hammer, and the same oil medium.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/bosses/vespera-the-glass-bloom.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1672 × 941 px for every attempt; opaque native RGB PNG, approximately 16:9.
- References, in order: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png`.
- Attempts: 2; re-makes: 1. Discarded: convincing ironwood roots, quartz, glass lotus and silver pistil, but the highest rear petals were clipped at the top.

### Attempt 1 — discarded

Discarded: convincing ironwood roots, quartz, glass lotus and silver pistil, but the highest rear petals were clipped at the top.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A towering, thirty-foot-tall predatory plant rising from a pool of glowing turquoise water, anchored by thick, braided roots of dark brown ironwood encrusted with white quartz; its upper body is a magnificent, terrifying lotus blossom made of hundreds of translucent, razor-edged stained-glass petals in hues of emerald, ruby, and amber, surrounding a central humanoid-shaped pistil of glowing silver crystal that weeps liquid light.

Vespera the Glass-Bloom, the Singing Orchid of the Drowned Conservatory. Show the whole thirty-foot rooted plant in a clear flaring lotus silhouette, braided dark ironwood roots gripping a low pool. The monstrous flower is the upper body, no humanoid legs or separate woman; its silver-crystal humanoid-shaped pistil is an integral, smaller central flower organ with a suggested bowed head and arm-like facets, shedding a few liquid-light droplets. Hundreds of glass petals are grouped into several big razor-edged petal masses, emerald dominant with restrained ruby and amber facets; use a few decisive translucent brush planes rather than polished optical rendering. White quartz clusters stud the broad dark roots. Turquoise water glows only close to roots and reflected light; keep the rest indigo and umber. Broken botanical dome ribs recede into cool marsh haze, with upper-left warm sun through a roof breach; dark foreground stone, complete rooted boss in the middle and distant broken dome supply three planes. One tiny anonymous cloaked hero on the far lower-left bank, less than a tenth the plant's height.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained: complete rooted lotus, emerald/ruby/amber glass masses, quartz-studded ironwood and a silver humanoid-shaped pistil shedding light; turquoise pool and broken conservatory support the lore. Oil strokes, impasto and warm/cool lighting closely match the references. At 300 px the lotus and roots remain distinct. Weakest point: the small petals merge into larger masses at card size, and the silver pistil reads rather strongly as a small woman.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A towering, thirty-foot-tall predatory plant rising from a pool of glowing turquoise water, anchored by thick, braided roots of dark brown ironwood encrusted with white quartz; its upper body is a magnificent, terrifying lotus blossom made of hundreds of translucent, razor-edged stained-glass petals in hues of emerald, ruby, and amber, surrounding a central humanoid-shaped pistil of glowing silver crystal that weeps liquid light.

Vespera the Glass-Bloom, the Singing Orchid of the Drowned Conservatory. Show the whole thirty-foot rooted plant in a clear flaring lotus silhouette, braided dark ironwood roots gripping a low pool. The monstrous flower is the upper body, no humanoid legs or separate woman; its silver-crystal humanoid-shaped pistil is an integral, smaller central flower organ with a suggested bowed head and arm-like facets, shedding a few liquid-light droplets. Hundreds of glass petals are grouped into several big razor-edged petal masses, emerald dominant with restrained ruby and amber facets; use a few decisive translucent brush planes rather than polished optical rendering. White quartz clusters stud the broad dark roots. Turquoise water glows only close to roots and reflected light; keep the rest indigo and umber. Broken botanical dome ribs recede into cool marsh haze, with upper-left warm sun through a roof breach; dark foreground stone, complete rooted boss in the middle and distant broken dome supply three planes. One tiny anonymous cloaked hero on the far lower-left bank, less than a tenth the plant's height.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

Revision for complete silhouette only: pull the camera back substantially. Make the entire plant from root base to tallest petal occupy only 70 percent of canvas height, leaving at least 15 percent clear sky above the tallest petal and 10 percent clear water below the lowest root. Every razor-petal tip, including the tallest central and upper-right tips, must be fully inside the frame with visible background around it. Reduce the number of giant outer petals rather than crowding them, while keeping hundreds of smaller translucent facets inside the big lotus masses. Preserve the ironwood roots, white quartz, turquoise pool, silver-crystal pistil weeping light, and the exact oil medium and colour relationships.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/bosses/high-arbiter-sul-kora.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1672 × 941 px for every attempt; opaque native RGB PNG, approximately 16:9.
- References, in order: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png`.
- Attempts: 2; re-makes: 1. Discarded: correct basalt quadruped, gold mask, chime collar and amber claws, but the right sword-wing was clipped along the top.

### Attempt 1 — discarded

Discarded: correct basalt quadruped, gold mask, chime collar and amber claws, but the right sword-wing was clipped along the top.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A majestic, twenty-five-foot-tall lion-bodied guardian sculpted from polished jet-black basalt inlaid with glowing geometric circuit-lines of burnished gold; it has the powerful four-legged body of a lion with claws of solid amber glass, a broad chest framed by a collar of ringing bronze chimes, two huge wings composed of floating golden sword-blades held in formation by light, and a serene, regally crowned face of hammered gold mask-work.

High Arbiter Sul-Kora, Scale-Bearer of the First Charter, standing in the partly buried Ziggurat of Kal. A fully quadrupedal lion guardian, exactly four strong feline legs and one long lion tail; all four amber-glass clawed paws visible and grounded, no human arms. A serene crowned humanoid gold mask replaces the lion face, its expression regal and impersonal. Its stone body remains jet-black basalt described by broad indigo facets with sparse burnished-gold geometric inlay, abstract nonlinguistic circuit patterns without letters. A collar of small bronze hanging chimes frames the chest. Exactly two enormous wings fan outward and upward from the shoulders, each consisting of individually separated floating golden sword-blades held in a coherent feather-like formation by tiny light connections; these are swords, not organic feathers, not additional limbs. Full tips within safe margins. Quiet copper-sand-covered limestone floor, one dim hanging balance pan in the rear, remote stepped walls dissolving into indigo dust and upper-left sun; a tiny hero less than an eighth the guardian's height near the lower-left foreground. Gold must remain tarnished brass and ochre paint, and polished basalt and glass must be interpreted through decisive oil strokes.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained: complete two-wing silhouette, basalt lion body, crowned hammered-gold mask, chime collar, abstract gold inlay and amber claws. Ochre blade strokes and indigo stone facets match the oil references. The guardian and sword-wing fans read at 300 px. Weakest point: wing bases appear more physically joined than purely levitating, and the far hind leg is partially occluded.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A majestic, twenty-five-foot-tall lion-bodied guardian sculpted from polished jet-black basalt inlaid with glowing geometric circuit-lines of burnished gold; it has the powerful four-legged body of a lion with claws of solid amber glass, a broad chest framed by a collar of ringing bronze chimes, two huge wings composed of floating golden sword-blades held in formation by light, and a serene, regally crowned face of hammered gold mask-work.

High Arbiter Sul-Kora, Scale-Bearer of the First Charter, standing in the partly buried Ziggurat of Kal. A fully quadrupedal lion guardian, exactly four strong feline legs and one long lion tail; all four amber-glass clawed paws visible and grounded, no human arms. A serene crowned humanoid gold mask replaces the lion face, its expression regal and impersonal. Its stone body remains jet-black basalt described by broad indigo facets with sparse burnished-gold geometric inlay, abstract nonlinguistic circuit patterns without letters. A collar of small bronze hanging chimes frames the chest. Exactly two enormous wings fan outward and upward from the shoulders, each consisting of individually separated floating golden sword-blades held in a coherent feather-like formation by tiny light connections; these are swords, not organic feathers, not additional limbs. Full tips within safe margins. Quiet copper-sand-covered limestone floor, one dim hanging balance pan in the rear, remote stepped walls dissolving into indigo dust and upper-left sun; a tiny hero less than an eighth the guardian's height near the lower-left foreground. Gold must remain tarnished brass and ochre paint, and polished basalt and glass must be interpreted through decisive oil strokes.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

Revision for framing only: step the camera well back. Keep the entire guardian, including the crown, tail, all four paws and both whole sword-wings, within the central 75 percent of image width and central 72 percent of image height. Leave a broad band of empty indigo haze above every single upper sword tip, at least 12 percent image height. Use lower, wider wings that sweep diagonally outward at shoulder level, not upward beyond the crown. No part of any blade may touch the top or right edge. Preserve the exact four-legged basalt lion anatomy, serene gold mask, bronze chime collar, amber claws, abstract gold inlay, spare ziggurat, and handmade oil paint.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/bosses/prioress-selen-the-unstrikable.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1672 × 941 px for every attempt; opaque native RGB PNG, approximately 16:9.
- References, in order: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png`.
- Attempts: 2; re-makes: 1. Discarded: the upper tuning-fork halo touched/cropped against the top edge; porcelain and ribbons were too smoothly resolved and ornamented compared with the desired broad oil planes.

### Attempt 1 — discarded

Discarded: the upper tuning-fork halo touched/cropped against the top edge; porcelain and ribbons were too smoothly resolved and ornamented compared with the desired broad oil planes.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A tall, slender female figure hovering three feet off the ground, sculpted from immaculate, glossy white porcelain cracked with glowing veins of silver light; she wears flowing monastic robes that have hardened into delicate, layered ribbons of translucent white glass, her eyes are covered by a blindfold of hammered silver, and three concentric halos of floating bronze tuning-forks spin slowly behind her head while she holds a six-foot conductor’s baton of solid diamond.

Prioress Selen, the Unstrikable, First Conductor of the Silent Choir, floating three feet above the courtyard of the Porcelain Cloister. A tall slender adult female porcelain figure, two arms and two feet only, serene and tragic, with an anatomically coherent planar face and hammered-silver blindfold completely covering both eyes. Porcelain is immaculate white in local colour but rendered as warm ochre-lit and indigo-shadowed oil planes, with tiny silver-light cracks; its physical gloss is suggested by a few impasto strokes, not CGI. Monastic robes have hardened into long, layered, translucent white-glass ribbons that sweep below her suspended feet without becoming extra limbs. Exactly three concentric, clearly separated circular halos behind the head, all made of many floating bronze tuning-forks with visible paired prongs, not solid hoops. One right hand naturally grips the midpoint of one six-foot straight diamond conductor's baton, angled outward across clear background, its entire length visible; left hand open in a restrained conducting gesture with clean five-finger anatomy. Keep the whole halo system, baton, ribbons and feet within the picture with generous clearance. Dark flagstones and cast shadow show the hovering gap; a quiet middle courtyard and a few distant pale cloister arches make three planes. No separate giant wings, no battle crowd, no elaborate picture-frame architecture.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained: floating porcelain woman, silver blindfold, three distinct concentric tuning-fork halos, glass-ribbon monastic robes and a long diamond baton. Larger warm/cool facets, bristle sky and scraped courtyard match the references; coherent face, hands and feet, no extra limbs observed. At 300 px the hovering silhouette and three halos read. Weakest point: the small forks and silver fissures lose detail, and some porcelain highlights remain more refined than the anchor's rough stone.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A tall, slender female figure hovering three feet off the ground, sculpted from immaculate, glossy white porcelain cracked with glowing veins of silver light; she wears flowing monastic robes that have hardened into delicate, layered ribbons of translucent white glass, her eyes are covered by a blindfold of hammered silver, and three concentric halos of floating bronze tuning-forks spin slowly behind her head while she holds a six-foot conductor’s baton of solid diamond.

Prioress Selen, the Unstrikable, First Conductor of the Silent Choir, floating three feet above the courtyard of the Porcelain Cloister. A tall slender adult female porcelain figure, two arms and two feet only, serene and tragic, with an anatomically coherent planar face and hammered-silver blindfold completely covering both eyes. Porcelain is immaculate white in local colour but rendered as warm ochre-lit and indigo-shadowed oil planes, with tiny silver-light cracks; its physical gloss is suggested by a few impasto strokes, not CGI. Monastic robes have hardened into long, layered, translucent white-glass ribbons that sweep below her suspended feet without becoming extra limbs. Exactly three concentric, clearly separated circular halos behind the head, all made of many floating bronze tuning-forks with visible paired prongs, not solid hoops. One right hand naturally grips the midpoint of one six-foot straight diamond conductor's baton, angled outward across clear background, its entire length visible; left hand open in a restrained conducting gesture with clean five-finger anatomy. Keep the whole halo system, baton, ribbons and feet within the picture with generous clearance. Dark flagstones and cast shadow show the hovering gap; a quiet middle courtyard and a few distant pale cloister arches make three planes. No separate giant wings, no battle crowd, no elaborate picture-frame architecture.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

Revision for halo clearance and oil surface: pull the view back so the entire floating figure, baton and all three tuning-fork halos occupy at most the middle 75 percent of picture height, leaving 12 percent unbroken indigo sky above the highest tuning-fork tip. Make exactly THREE concentric fork circles distinctly countable behind her head with open indigo gaps; omit solid ring bands. Paint her porcelain face, hands, legs and white glass robes with larger flat-bristle facets and thick broken ochre highlights. Reduce fine golden jewelry, curlicues, tiny cracks and smooth luminous gradients; use only broad monastic glass-ribbon folds and a few clear silver cracks. Keep the silver blindfold, coherent hands and feet, six-foot diamond baton and three-foot floating gap unchanged. Background architecture should be sparse large low-contrast masses rather than a detailed vista.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/bosses/krym-vara-the-rime-glass-wyrm.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1672 × 941 px for every attempt; opaque native RGB PNG, approximately 16:9.
- References, in order: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png`.
- Attempts: 2; re-makes: 1. Discarded: both raised glass wings extended beyond the upper frame, despite correct porcelain/blue-ice materials and bright silver star-heart.

### Attempt 1 — discarded

Discarded: both raised glass wings extended beyond the upper frame, despite correct porcelain/blue-ice materials and bright silver star-heart.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A colossal, winged serpentine dragon with a long, sinuous body covered in overlapping plates of frosted white porcelain and jagged blue glacier-ice; its massive wings are framed by bone-white spars stretched with panes of rainbow-refracting diamond glass, its head features a crown of six backward-swept crystal horns, and its chest is a translucent ribcage revealing a spinning, blindingly bright star of silver light where its heart should be.

Krym-Vara, the Rime-Glass Wyrm, Scourge of the Boreal Pipes. A hundred-foot serpentine alpine dragon, its long body curled in one legible S-curve on a broken brass Wind-Wall battlement, tail curling inward so its whole tip is visible. Exactly four draconic legs with clear joints, two wings, one head and one continuous tail; separate paws and avoid tangled anatomy. Raise the two massive bone-white-spar wings in a broad open V, their membranes made of diamond-glass panes; include the entirety of both wings inside the frame. Porcelain-white overlapping scales, jagged blue glacier-ice ridges and translucent ribcage showing a single spinning silver star-heart. Crown the head with exactly six backward-swept crystal horns, three on each side, separated enough to count at full size. Subtle prismatic warm-cool colour flecks confined to a few diamond-pane edges express rainbow refraction without rainbow scene lighting; mainly indigo, chalky white, ochre sun and tiny teal accents. Face and upper chest get the crispest paint edges; glacial masses and membranes use broad oil strokes and scraped impasto rather than photographic clear glass. Tiny raid silhouettes at lower left, all under one twentieth the wyrm's height. Foreground fractured brass pipe, middle dragon and battlement, distant misty peaks and giant organ pipes; upper-left sunlight cuts the silver blizzard, with no breath beam obscuring anatomy.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained: whole two-wing silhouette, long curling tail, porcelain scales, blue glacier ice, bone-white wing spars, prismatic glass panes and exposed star-heart. Broad sunlit impasto and indigo mountain haze match the references without glossy CGI. At 300 px wings, dragon head and chest-star remain legible. Weakest point: the six intended crown horns blend with adjacent ice spines, and fine wing glass and the far rear leg are less distinct.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A colossal, winged serpentine dragon with a long, sinuous body covered in overlapping plates of frosted white porcelain and jagged blue glacier-ice; its massive wings are framed by bone-white spars stretched with panes of rainbow-refracting diamond glass, its head features a crown of six backward-swept crystal horns, and its chest is a translucent ribcage revealing a spinning, blindingly bright star of silver light where its heart should be.

Krym-Vara, the Rime-Glass Wyrm, Scourge of the Boreal Pipes. A hundred-foot serpentine alpine dragon, its long body curled in one legible S-curve on a broken brass Wind-Wall battlement, tail curling inward so its whole tip is visible. Exactly four draconic legs with clear joints, two wings, one head and one continuous tail; separate paws and avoid tangled anatomy. Raise the two massive bone-white-spar wings in a broad open V, their membranes made of diamond-glass panes; include the entirety of both wings inside the frame. Porcelain-white overlapping scales, jagged blue glacier-ice ridges and translucent ribcage showing a single spinning silver star-heart. Crown the head with exactly six backward-swept crystal horns, three on each side, separated enough to count at full size. Subtle prismatic warm-cool colour flecks confined to a few diamond-pane edges express rainbow refraction without rainbow scene lighting; mainly indigo, chalky white, ochre sun and tiny teal accents. Face and upper chest get the crispest paint edges; glacial masses and membranes use broad oil strokes and scraped impasto rather than photographic clear glass. Tiny raid silhouettes at lower left, all under one twentieth the wyrm's height. Foreground fractured brass pipe, middle dragon and battlement, distant misty peaks and giant organ pipes; upper-left sunlight cuts the silver blizzard, with no breath beam obscuring anatomy.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

Revision for entire wing silhouette: zoom out until the dragon's ENTIRE wingspan fits inside the central 75 percent of canvas width, with at least 12 percent empty sky outside both outer wing tips and 12 percent empty sky above all spars. Lower both wings to an open horizontal arc rather than an upward V. No bone spar, membrane corner, horn or tail tip may touch any image edge. The creature may occupy only 65 percent of image height so its whole shape reads as one contained silhouette. Simplify the wing panes into big painterly diamond-glass planes and the back ridges into a few grouped blue-ice masses; preserve the porcelain body, long S-curve tail, exactly six backward crystal horns, four legs and two wings, and the translucent silver star-heart chest. Keep raid silhouettes extremely tiny. Do not turn the dragon into a shiny render.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/bosses/avren-voice-of-the-cantor.png`

- Tool: `image_gen.imagegen`.
- Model: `gpt-image`; exact revision not exposed.
- Size: 1672 × 941 px for every attempt; opaque native RGB PNG, approximately 16:9.
- References, in order: `art/style/candidate-a.png`, `art/style/anchor-3-creature.png`.
- Attempts: 3; re-makes: 2. Discarded: three masks had facial recesses instead of being featureless; background and foreground party inherited too much of the candidate composition, and upper clearance was tight. Discarded: blank masks, six pipe/crystal wings and green-bronze rings improved, but the upper-right wing/crystal mass reached the top edge.

### Attempt 1 — discarded

Discarded: three masks had facial recesses instead of being featureless; background and foreground party inherited too much of the candidate composition, and upper clearance was tight.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A breathtaking, forty-foot-tall celestial construct suspended in mid-air at the eye of a silver storm; its core is a regal, tall humanoid torso of flawless white marble and porcelain wearing three rotating, featureless masks of gold, silver, and bronze, surrounded by six massive wings made of suspended brass organ pipes and floating crystal spears, while two gigantic, concentric gyroscope-rings of ancient patina-green bell-bronze engraved with glowing runes spin slowly around its entire body.

Avren, Voice of the Cantor, The Final Chord of Kaelvorn, suspended at the center of the ruptured First Spire where the upward Pale Wake waterfall meets broken sky arches. A forty-foot celestial acoustic construct with one elongated regal humanoid torso of white marble and porcelain; its lower marble body tapers into a floating architectural point, coherent two arms resting slightly open. At the head, exactly three separate smooth featureless masks, gold, silver and bronze, rotating close around the same neck-axis; none has eyes, mouth, nostrils or lettering. Exactly six massive wings, arranged as three clearly separated pairs with background gaps, project from the torso in a sculptural radial silhouette. Each wing consists of suspended aged brass organ pipes interspersed with floating crystal spears, not feathered angel wings. Exactly two gigantic concentric gyroscope rings of ancient patina-green bell-bronze encircle the entire construct at different tilts with clear spatial depth; their edges fit comfortably within the frame. Ring engravings are sparse abstract nonlinguistic geometric marks carrying tiny silver-teal glow, absolutely no readable runes or script. Keep six wings distinct from the two rings. Three-quarter perspective and slight asymmetry prevent a flat heraldic diagram. One tiny party on a broken lower-left platform, under one fifteenth the construct's height. Dark foreground ruined platform, dominant suspended boss in the middle and spare receding ruptured arches in a silver-indigo storm; warm light from upper left catches porcelain and brass, fine teal bounce at shadow edges. Preserve sorrowful stillness through broad, weighty oil planes.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — discarded

Discarded: blank masks, six pipe/crystal wings and green-bronze rings improved, but the upper-right wing/crystal mass reached the top edge.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A breathtaking, forty-foot-tall celestial construct suspended in mid-air at the eye of a silver storm; its core is a regal, tall humanoid torso of flawless white marble and porcelain wearing three rotating, featureless masks of gold, silver, and bronze, surrounded by six massive wings made of suspended brass organ pipes and floating crystal spears, while two gigantic, concentric gyroscope-rings of ancient patina-green bell-bronze engraved with glowing runes spin slowly around its entire body.

Avren, Voice of the Cantor, The Final Chord of Kaelvorn, suspended at the center of the ruptured First Spire where the upward Pale Wake waterfall meets broken sky arches. A forty-foot celestial acoustic construct with one elongated regal humanoid torso of white marble and porcelain; its lower marble body tapers into a floating architectural point, coherent two arms resting slightly open. At the head, exactly three separate smooth featureless masks, gold, silver and bronze, rotating close around the same neck-axis; none has eyes, mouth, nostrils or lettering. Exactly six massive wings, arranged as three clearly separated pairs with background gaps, project from the torso in a sculptural radial silhouette. Each wing consists of suspended aged brass organ pipes interspersed with floating crystal spears, not feathered angel wings. Exactly two gigantic concentric gyroscope rings of ancient patina-green bell-bronze encircle the entire construct at different tilts with clear spatial depth; their edges fit comfortably within the frame. Ring engravings are sparse abstract nonlinguistic geometric marks carrying tiny silver-teal glow, absolutely no readable runes or script. Keep six wings distinct from the two rings. Three-quarter perspective and slight asymmetry prevent a flat heraldic diagram. One tiny party on a broken lower-left platform, under one fifteenth the construct's height. Dark foreground ruined platform, dominant suspended boss in the middle and spare receding ruptured arches in a silver-indigo storm; warm light from upper left catches porcelain and brass, fine teal bounce at shadow edges. Preserve sorrowful stillness through broad, weighty oil planes.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

Revision for masks and spare composition: the three head masks must be completely FEATURELESS, smooth convex oval metal plates in gold, silver and bronze. No eye holes, eye dimples, eyebrows, nose ridge, mouth line or human facial modelling whatsoever: each is a single uninterrupted gently convex painted oval. Turn the two side masks enough to show their metal colour while keeping them blank. Keep exactly six pipe-and-crystal wings in three pairs and exactly two patina-green gyroscope rings; pull back until the top ring has 10 percent sky clearance. Reduce the background to a silver-indigo storm, three broad broken arches and a distant upward waterfall; remove the field of tiny towers and waterfalls. Replace the foreground crowd with only two tiny anonymous cloaked figures and no animal, no copied candidate party. Strengthen rough bristle planes on the marble and bronze, limiting decoration to sparse abstract circuit-like scratches without letter shapes. Preserve the whole suspended pointed body and all wing tips within the frame.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 3 — retained

Retained: all six organ-pipe/crystal wings and two green-patina gyroscope rings fit; three blank gold, silver and bronze oval masks, white porcelain torso and suspended pointed lower body match the construct. Silver-indigo storm, upward waterfall, ochre bristle highlights and dark broken arches support lore and style. At 300 px the six-wing pattern, rings and three-mask head remain identifiable. Weakest point: ring overlaps partly hide the lower-left wing and torso; ornament and distant ruins remain busier than the requested spare setting.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Boss and creature: full-body three-quarter view, 50 mm lens with slight low angle, one dominant readable silhouette, brightest contrast at head and upper body, thin shadow-side rim, spare scale-setting environment with three depth planes, landscape 16:9 or 3:2.

A breathtaking, forty-foot-tall celestial construct suspended in mid-air at the eye of a silver storm; its core is a regal, tall humanoid torso of flawless white marble and porcelain wearing three rotating, featureless masks of gold, silver, and bronze, surrounded by six massive wings made of suspended brass organ pipes and floating crystal spears, while two gigantic, concentric gyroscope-rings of ancient patina-green bell-bronze engraved with glowing runes spin slowly around its entire body.

Avren, Voice of the Cantor, The Final Chord of Kaelvorn, suspended at the center of the ruptured First Spire where the upward Pale Wake waterfall meets broken sky arches. A forty-foot celestial acoustic construct with one elongated regal humanoid torso of white marble and porcelain; its lower marble body tapers into a floating architectural point, coherent two arms resting slightly open. At the head, exactly three separate smooth featureless masks, gold, silver and bronze, rotating close around the same neck-axis; none has eyes, mouth, nostrils or lettering. Exactly six massive wings, arranged as three clearly separated pairs with background gaps, project from the torso in a sculptural radial silhouette. Each wing consists of suspended aged brass organ pipes interspersed with floating crystal spears, not feathered angel wings. Exactly two gigantic concentric gyroscope rings of ancient patina-green bell-bronze encircle the entire construct at different tilts with clear spatial depth; their edges fit comfortably within the frame. Ring engravings are sparse abstract nonlinguistic geometric marks carrying tiny silver-teal glow, absolutely no readable runes or script. Keep six wings distinct from the two rings. Three-quarter perspective and slight asymmetry prevent a flat heraldic diagram. One tiny party on a broken lower-left platform, under one fifteenth the construct's height. Dark foreground ruined platform, dominant suspended boss in the middle and spare receding ruptured arches in a silver-indigo storm; warm light from upper left catches porcelain and brass, fine teal bounce at shadow edges. Preserve sorrowful stillness through broad, weighty oil planes.

Use candidate-a.png (reference 1) and anchor-3-creature.png (reference 2) solely as style references: borrow oil surface, bristle stroke scale, edge economy, palette and lighting while inventing this subject and composition. Do not inherit their party, city, spire or stone-colossus anatomy. One dominant full-body silhouette with all extremities and defining objects inside generous safe margins; three-quarter view, slightly low 50 mm perspective. Large painted planes, selective thick ochre glints, indigo shadows, narrow viridian shadow rim; keep most of the image in resting neutrals and concentrate detail at the face and defining upper-body feature. Full-bleed landscape exactly 16:9; generate one opaque PNG at the largest available native size, target 3840 x 2160 pixels. 

Revision for masks and spare composition: the three head masks must be completely FEATURELESS, smooth convex oval metal plates in gold, silver and bronze. No eye holes, eye dimples, eyebrows, nose ridge, mouth line or human facial modelling whatsoever: each is a single uninterrupted gently convex painted oval. Turn the two side masks enough to show their metal colour while keeping them blank. Keep exactly six pipe-and-crystal wings in three pairs and exactly two patina-green gyroscope rings; pull back until the top ring has 10 percent sky clearance. Reduce the background to a silver-indigo storm, three broad broken arches and a distant upward waterfall; remove the field of tiny towers and waterfalls. Replace the foreground crowd with only two tiny anonymous cloaked figures and no animal, no copied candidate party. Strengthen rough bristle planes on the marble and bronze, limiting decoration to sparse abstract circuit-like scratches without letter shapes. Preserve the whole suspended pointed body and all wing tips within the frame.

Second revision for strict safe margins: make Avren much smaller in the composition, occupying only the middle 65 percent of image width and the middle 65 percent of image height INCLUDING every crystal spear, organ pipe and both rings. Show a continuous wide band of empty slate-indigo storm sky above the complete uppermost wing tips and the top ring, with no overlap into the top 15 percent of the image. Both upper wings must point diagonally sideways at a low angle, never nearly vertically. Retain exactly six separated wings, the three completely featureless blank oval masks, two patina-green rings, white porcelain torso and only two tiny scale figures. Full subject containment is more important than scale of the boss within the image.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

# Phase 5 — six pets (2026-10-26)

All six assets were generated with the built-in image tool, copied as unchanged native PNGs, then visually inspected at native 1536 × 1024 and 300 × 200 card size. Largest native landscape 3:2 was requested with a 3072 × 2048 target; the tool returned 1536 × 1024 for all nine attempts. No upscaling, cropping, recolouring or texture overlays were applied to the deliverables. Three assets received one remake each.

## `art/pets/brass-wound-owl.png`

- File: `art/pets/brass-wound-owl.png`.
- Tool: built-in `image_gen.imagegen`.
- Model: not exposed by the built-in tool; no model selector or model identifier was returned.
- Requested size: largest native landscape 3:2; target 3072 × 2048 px.
- Actual size: 1536 × 1024 px, 3:2, opaque RGB PNG.
- References, in order: `art/style/candidate-a.png` (primary paint, palette and light); `art/style/anchor-3-creature.png` (creature material and painted bounce, overriding boss scale); `art/style/anchor-2-hero.png` (isolated backdrop and metal strokes). Style references only, not edit targets.
- Remakes: 0; first attempt retained.
- Review: Retained first attempt. At native size the barn-owl facial disk, amber mechanical lenses, exposed chest gears, bronze verdigris and large shoulder winding key are present. Strong ochre knife edges, broken bristle paint and indigo backdrop match the anchors; feet and tail are complete. At 300 × 200 px the head, key and gear cage remain legible. Weakest point: layered feather plates and gear teeth are busier than ideal; head and feet have tighter vertical margins than requested. No visible text, marks, frame or anatomy defect.

### Attempt 1 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

A mechanical barn owl crafted from polished brass and verdigris-patina bronze, with rotating amber-glass lenses for eyes, visible ticking gears inside its chest cage, and a big brass winding-key turning slowly between its shoulder blades.

Quietly standing with both feet visible, folded wings and the barn owl's heart-shaped facial disk, head turned toward us while the body angles enough away to reveal the large double-loop winding key between the shoulder blades beyond one shoulder. Amber lenses are mechanical glass, not cartoon eyes. Make the chest cage open enough to clearly show three large meshing gears. Polished brass is interpreted through a few decisive painted highlight strokes over weathered bronze and restrained verdigris, never mirror gradients.

A small charming hearth-companion of Kaelvorn, never cute-cartoon. Keep natural proportions and an approachable quiet presence. Subject occupies about 70 percent of image height with at least 10 percent clearance around every extremity and defining feature. Plain subdued indigo and umber painterly backdrop, only a minimal ground plane; no scenery or additional beings. Use the supplied images solely as style references, not edit targets: image 1, art/style/candidate-a.png, fixes oil surface, bristle stroke scale, edge economy, palette and lighting; image 2, art/style/anchor-3-creature.png, fixes rough creature materials and painted light integration, overriding its boss scale and humanoid anatomy; image 3, art/style/anchor-2-hero.png, fixes isolated dark backdrop and decisive material highlights, without borrowing its armour or weapon. Invent the requested pet and composition. Work in broad visible oil strokes, concentrating crisp edges at the head or defining feature and losing some peripheral edges. Generate one opaque full-bleed PNG, exact landscape 3:2, at the largest native size supported, target 3072 x 2048 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/pets/chime-finch.png`

- File: `art/pets/chime-finch.png`.
- Tool: built-in `image_gen.imagegen`.
- Model: not exposed by the built-in tool; no model selector or model identifier was returned.
- Requested size: largest native landscape 3:2; target 3072 × 2048 px.
- Actual size: 1536 × 1024 px, 3:2, opaque RGB PNG.
- References, in order: `art/style/candidate-a.png` (primary paint, palette and light); `art/style/anchor-3-creature.png` (creature material and painted bounce, overriding boss scale); `art/style/anchor-2-hero.png` (isolated backdrop and metal strokes). Style references only, not edit targets.
- Remakes: 0; first attempt retained.
- Review: Retained first attempt. Plump songbird, saffron-yellow breast, cobalt wings and exactly three copper tail feathers are clear at native and 300 × 200 px. Coarse oil strokes and warm/cool material breaks match the references. Weakest point: the copper feathers are broader and their glow stronger than the description's thin, softly glowing feathers; eye is slightly glossy but the overall image reads as oil paint. No visible text, marks, frame or anatomy defect.

### Attempt 1 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

A plump, robin-sized songbird with bright saffron-yellow breast feathers, cobalt-blue wings, and a tail made of three thin, chiming copper feathers that glow softly in the dark.

Standing alert on a low neutral stone with both bird feet visible, folded cobalt-blue wings and plump saffron breast. Angle the body so the tail fans gently sideways into negative space: exactly three narrow copper-metal feather blades, separate, complete and countable, with softly luminous edges. Keep natural songbird anatomy and an ordinary small dark eye. Saffron and cobalt are structural local colours mixed into the fixed ochre and indigo light.

A small charming hearth-companion of Kaelvorn, never cute-cartoon. Keep natural proportions and an approachable quiet presence. Subject occupies about 70 percent of image height with at least 10 percent clearance around every extremity and defining feature. Plain subdued indigo and umber painterly backdrop, only a minimal ground plane; no scenery or additional beings. Use the supplied images solely as style references, not edit targets: image 1, art/style/candidate-a.png, fixes oil surface, bristle stroke scale, edge economy, palette and lighting; image 2, art/style/anchor-3-creature.png, fixes rough creature materials and painted light integration, overriding its boss scale and humanoid anatomy; image 3, art/style/anchor-2-hero.png, fixes isolated dark backdrop and decisive material highlights, without borrowing its armour or weapon. Invent the requested pet and composition. Work in broad visible oil strokes, concentrating crisp edges at the head or defining feature and losing some peripheral edges. Generate one opaque full-bleed PNG, exact landscape 3:2, at the largest native size supported, target 3072 x 2048 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/pets/cinder-pug.png`

- File: `art/pets/cinder-pug.png`.
- Tool: built-in `image_gen.imagegen`.
- Model: not exposed by the built-in tool; no model selector or model identifier was returned.
- Requested size: largest native landscape 3:2; target 3072 × 2048 px.
- Actual size: 1536 × 1024 px, 3:2, opaque RGB PNG for both attempts.
- References, in order: `art/style/candidate-a.png` (primary paint, palette and light); `art/style/anchor-3-creature.png` (creature material and painted bounce, overriding boss scale); `art/style/anchor-2-hero.png` (isolated backdrop and metal strokes). Style references only, not edit targets.
- Remakes: 1; attempt 2 retained.
- Review: Retained attempt 2 after one remake. Squat quadruped, broad short muzzle, floppy dark obsidian ear plates, cracked grey basalt, orange fissures and two grey steam rings from the stubby tail are visible. Larger bristle planes and indigo resting masses match the references at native and 300 × 200 px. Weakest point: the face remains more canine than reptilian, and the tiny steam rings soften at card scale. No visible text, marks, frame or anatomy defect.

### Attempt 1 — discarded

Discarded: the first attempt's high chest and long legs made a tall dog rather than the described stout knee-high lizard-hound. One remake requested a low broad body, short splayed legs and simpler basalt plates.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

A stout, knee-high lizard-hound made of cracked dark-grey volcanic basalt with warm orange magma glowing harmlessly between its stone plates, floppy obsidian ears, and a stubby tail that puffs tiny rings of grey steam when it barks.

Standing at ease with four short sturdy legs, relaxed doglike muzzle and two floppy obsidian ears; a basalt lizard-hound companion, with natural sturdy quadruped proportions. Angle the little stubby tail into clear space beside the rump and show two tiny grey steam rings immediately leaving its tip. Dark-grey angular stone plates, very restrained orange heat only in cracks, welcoming rather than threatening.

A small charming hearth-companion of Kaelvorn, never cute-cartoon. Keep natural proportions and an approachable quiet presence. Subject occupies about 70 percent of image height with at least 10 percent clearance around every extremity and defining feature. Plain subdued indigo and umber painterly backdrop, only a minimal ground plane; no scenery or additional beings. Use the supplied images solely as style references, not edit targets: image 1, art/style/candidate-a.png, fixes oil surface, bristle stroke scale, edge economy, palette and lighting; image 2, art/style/anchor-3-creature.png, fixes rough creature materials and painted light integration, overriding its boss scale and humanoid anatomy; image 3, art/style/anchor-2-hero.png, fixes isolated dark backdrop and decisive material highlights, without borrowing its armour or weapon. Invent the requested pet and composition. Work in broad visible oil strokes, concentrating crisp edges at the head or defining feature and losing some peripheral edges. Generate one opaque full-bleed PNG, exact landscape 3:2, at the largest native size supported, target 3072 x 2048 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

A stout, knee-high lizard-hound made of cracked dark-grey volcanic basalt with warm orange magma glowing harmlessly between its stone plates, floppy obsidian ears, and a stubby tail that puffs tiny rings of grey steam when it barks.

Standing at ease with four short sturdy legs, relaxed doglike muzzle and two floppy obsidian ears; a basalt lizard-hound companion, with natural sturdy quadruped proportions. Angle the little stubby tail into clear space beside the rump and show two tiny grey steam rings immediately leaving its tip. Dark-grey angular stone plates, very restrained orange heat only in cracks, welcoming rather than threatening.

A small charming hearth-companion of Kaelvorn, never cute-cartoon. Keep natural proportions and an approachable quiet presence. Subject occupies about 70 percent of image height with at least 10 percent clearance around every extremity and defining feature. Plain subdued indigo and umber painterly backdrop, only a minimal ground plane; no scenery or additional beings. Use the supplied images solely as style references, not edit targets: image 1, art/style/candidate-a.png, fixes oil surface, bristle stroke scale, edge economy, palette and lighting; image 2, art/style/anchor-3-creature.png, fixes rough creature materials and painted light integration, overriding its boss scale and humanoid anatomy; image 3, art/style/anchor-2-hero.png, fixes isolated dark backdrop and decisive material highlights, without borrowing its armour or weapon. Invent the requested pet and composition. Work in broad visible oil strokes, concentrating crisp edges at the head or defining feature and losing some peripheral edges. Generate one opaque full-bleed PNG, exact landscape 3:2, at the largest native size supported, target 3072 x 2048 pixels.

Revision: make the described stout knee-high lizard-hound genuinely squat and reptilian. The torso is a low broad oval twice as long as the short legs are tall, head carried low above the shoulders, broad short puglike muzzle, a low stone belly and four short splayed lizardlike legs. Keep the floppy black obsidian ear plates and small steam-puffing stubby tail. Use larger simpler basalt plates and fewer orange fissures. Avoid the tall proud chest and long legs of a beagle. Pull back slightly for comfortable dark margins.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/pets/dune-fox-kit.png`

- File: `art/pets/dune-fox-kit.png`.
- Tool: built-in `image_gen.imagegen`.
- Model: not exposed by the built-in tool; no model selector or model identifier was returned.
- Requested size: largest native landscape 3:2; target 3072 × 2048 px.
- Actual size: 1536 × 1024 px, 3:2, opaque RGB PNG.
- References, in order: `art/style/candidate-a.png` (primary paint, palette and light); `art/style/anchor-3-creature.png` (creature material and painted bounce, overriding boss scale); `art/style/anchor-2-hero.png` (isolated backdrop and metal strokes). Style references only, not edit targets.
- Remakes: 0; first attempt retained.
- Review: Retained first attempt. Slender natural fox anatomy, four legs, two exceptionally tall white-lined ears, copper-red coat and natural amber-crystal tail cluster match the description. The ochre impasto and cool indigo background stay coherent with the anchors at native and 300 × 200 px. Weakest point: the tallest ear has very little top clearance and the crystal facets merge somewhat with fur at card scale. No clipped ear, visible text, marks, frame or anatomy defect.

### Attempt 1 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

A small, slender desert fox with oversized, foot-long ears lined with soft white fur, a coat of metallic copper-red, and a bushy tail tipped with a natural cluster of tinkling amber crystals.

Standing quietly with four slender legs, a natural pointed fox muzzle and two exceptionally tall ears lined in warm soft white fur, both complete and separated. Turn the face gently toward us. The rich metallic copper-red coat is rendered in broad fur strokes with a few copper highlights, never polished plastic. Curve the bushy tail sideways into negative space so its natural amber crystal cluster is unmistakable, with a few large irregular facets and no jewellery fastening.

A small charming hearth-companion of Kaelvorn, never cute-cartoon. Keep natural proportions and an approachable quiet presence. Subject occupies about 70 percent of image height with at least 10 percent clearance around every extremity and defining feature. Plain subdued indigo and umber painterly backdrop, only a minimal ground plane; no scenery or additional beings. Use the supplied images solely as style references, not edit targets: image 1, art/style/candidate-a.png, fixes oil surface, bristle stroke scale, edge economy, palette and lighting; image 2, art/style/anchor-3-creature.png, fixes rough creature materials and painted light integration, overriding its boss scale and humanoid anatomy; image 3, art/style/anchor-2-hero.png, fixes isolated dark backdrop and decisive material highlights, without borrowing its armour or weapon. Invent the requested pet and composition. Work in broad visible oil strokes, concentrating crisp edges at the head or defining feature and losing some peripheral edges. Generate one opaque full-bleed PNG, exact landscape 3:2, at the largest native size supported, target 3072 x 2048 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/pets/shard-sprite.png`

- File: `art/pets/shard-sprite.png`.
- Tool: built-in `image_gen.imagegen`.
- Model: not exposed by the built-in tool; no model selector or model identifier was returned.
- Requested size: largest native landscape 3:2; target 3072 × 2048 px.
- Actual size: 1536 × 1024 px, 3:2, opaque RGB PNG for both attempts.
- References, in order: `art/style/candidate-a.png` (primary paint, palette and light); `art/style/anchor-3-creature.png` (creature material and painted bounce, overriding boss scale); `art/style/anchor-2-hero.png` (isolated backdrop and metal strokes). Style references only, not edit targets.
- Remakes: 1; attempt 2 retained.
- Review: Retained attempt 2 after one remake. Exactly six separated triangular white porcelain pieces orbit a golden flame core, with no humanoid features. All six remain countable at 300 × 200 px. Oil impasto, warm bounce and dark indigo backdrop match the anchors. Weakest point: the porcelain triangles still read as thicker faceted wedges than thin plates, and the flame is a stronger focal mass than requested. No visible text, marks or frame.

### Attempt 1 — discarded

Discarded: only four bulky porcelain solids were visible instead of six triangles. One remake requested six separate triangular pieces at six explicit positions, without metal ornament.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

A floating, geometric creature the size of a lantern, consisting of a warm golden flame core orbited by six floating triangles of white porcelain that click and rearrange themselves into different polyhedrons depending on whether the player is in combat.

Hovering calmly above a small soft ground shadow, a friendly non-humanoid elemental with no face, hands or limbs. A warm golden flame core at centre, surrounded by exactly six separate triangular white porcelain plates, all countable, loosely arranged into one open geometric lantern-sized polyhedron. Separate the six triangles with clear dark gaps; each has three unmistakable corners, thin porcelain thickness, warm ivory sunward strokes and cool indigo shadows. Flame is the small warm subject-specific light, with restrained painted bounce and no broad neon halo.

A small charming hearth-companion of Kaelvorn, never cute-cartoon. Keep natural proportions and an approachable quiet presence. Subject occupies about 70 percent of image height with at least 10 percent clearance around every extremity and defining feature. Plain subdued indigo and umber painterly backdrop, only a minimal ground plane; no scenery or additional beings. Use the supplied images solely as style references, not edit targets: image 1, art/style/candidate-a.png, fixes oil surface, bristle stroke scale, edge economy, palette and lighting; image 2, art/style/anchor-3-creature.png, fixes rough creature materials and painted light integration, overriding its boss scale and humanoid anatomy; image 3, art/style/anchor-2-hero.png, fixes isolated dark backdrop and decisive material highlights, without borrowing its armour or weapon. Invent the requested pet and composition. Work in broad visible oil strokes, concentrating crisp edges at the head or defining feature and losing some peripheral edges. Generate one opaque full-bleed PNG, exact landscape 3:2, at the largest native size supported, target 3072 x 2048 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

A floating, geometric creature the size of a lantern, consisting of a warm golden flame core orbited by six floating triangles of white porcelain that click and rearrange themselves into different polyhedrons depending on whether the player is in combat.

Hovering calmly above a small soft ground shadow, a friendly non-humanoid elemental with no face, hands or limbs. A warm golden flame core at centre, surrounded by exactly six separate triangular white porcelain plates, all countable, loosely arranged into one open geometric lantern-sized polyhedron. Separate the six triangles with clear dark gaps; each has three unmistakable corners, thin porcelain thickness, warm ivory sunward strokes and cool indigo shadows. Flame is the small warm subject-specific light, with restrained painted bounce and no broad neon halo.

A small charming hearth-companion of Kaelvorn, never cute-cartoon. Keep natural proportions and an approachable quiet presence. Subject occupies about 70 percent of image height with at least 10 percent clearance around every extremity and defining feature. Plain subdued indigo and umber painterly backdrop, only a minimal ground plane; no scenery or additional beings. Use the supplied images solely as style references, not edit targets: image 1, art/style/candidate-a.png, fixes oil surface, bristle stroke scale, edge economy, palette and lighting; image 2, art/style/anchor-3-creature.png, fixes rough creature materials and painted light integration, overriding its boss scale and humanoid anatomy; image 3, art/style/anchor-2-hero.png, fixes isolated dark backdrop and decisive material highlights, without borrowing its armour or weapon. Invent the requested pet and composition. Work in broad visible oil strokes, concentrating crisp edges at the head or defining feature and losing some peripheral edges. Generate one opaque full-bleed PNG, exact landscape 3:2, at the largest native size supported, target 3072 x 2048 pixels.

Revision: the defining requirement is SIX separate thin triangular porcelain plates, not four tetrahedral solids. Arrange them as a clear six-part open ring around the small flame core, one plate at each clock position 12, 2, 4, 6, 8 and 10. Every plate is a single flat three-cornered white porcelain shard viewed mostly broadside with a slim side edge; all six must be fully visible and individually countable, with dark gaps between them. No assembled tetrahedra, no gold metal frames or ornament. Keep golden flame small and painterly and porcelain warm-white with cool shadows.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/pets/spore-hopper.png`

- File: `art/pets/spore-hopper.png`.
- Tool: built-in `image_gen.imagegen`.
- Model: not exposed by the built-in tool; no model selector or model identifier was returned.
- Requested size: largest native landscape 3:2; target 3072 × 2048 px.
- Actual size: 1536 × 1024 px, 3:2, opaque RGB PNG for both attempts.
- References, in order: `art/style/candidate-a.png` (primary paint, palette and light); `art/style/anchor-3-creature.png` (creature material and painted bounce, overriding boss scale); `art/style/anchor-2-hero.png` (isolated backdrop and metal strokes). Style references only, not edit targets.
- Remakes: 1; attempt 2 retained.
- Review: Retained attempt 2 after one remake. Round sea-green frog with large golden eyes, four plausible limbs in a low hop, exactly three separate violet mushroom caps and a sparse spore trail. Broad paint, ochre planes and indigo depth match the references at native and 300 × 200 px; all three caps remain visible. Weakest point: skin reads more opaque than translucent and the far hind foot is partly concealed beneath the body. No visible text, marks, frame or extra limbs.

### Attempt 1 — discarded

Discarded: only two mushroom caps were clearly visible, and the eyes were too round. One remake requested three separate cap silhouettes and a less cartoonlike face.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

A round, fist-sized tree frog with translucent sea-green skin, large golden eyes, and a cluster of three glowing violet mushroom caps growing cheerfully from its back that release sparkling dust whenever it jumps.

In a gentle low hop just above the ground, three-quarter side view with a round frog body, two front legs and two folded hind legs, plausible tree-frog toes and two large golden eyes. Sea-green translucent skin is represented by luminous planar oil glazes and opaque bristle accents, not wet photographic gloss. Exactly three violet mushroom caps on short stems grow from the back, each cap distinct and countable; a small trail of sparse sparkling spore dust hangs behind them. Violet stays a restrained local accent with tight glow.

A small charming hearth-companion of Kaelvorn, never cute-cartoon. Keep natural proportions and an approachable quiet presence. Subject occupies about 70 percent of image height with at least 10 percent clearance around every extremity and defining feature. Plain subdued indigo and umber painterly backdrop, only a minimal ground plane; no scenery or additional beings. Use the supplied images solely as style references, not edit targets: image 1, art/style/candidate-a.png, fixes oil surface, bristle stroke scale, edge economy, palette and lighting; image 2, art/style/anchor-3-creature.png, fixes rough creature materials and painted light integration, overriding its boss scale and humanoid anatomy; image 3, art/style/anchor-2-hero.png, fixes isolated dark backdrop and decisive material highlights, without borrowing its armour or weapon. Invent the requested pet and composition. Work in broad visible oil strokes, concentrating crisp edges at the head or defining feature and losing some peripheral edges. Generate one opaque full-bleed PNG, exact landscape 3:2, at the largest native size supported, target 3072 x 2048 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Mount and pet: full body in side three-quarter view, 50 mm lens at the subject's chest height, complete ears, tail and feet inside safe margins, one readable silhouette on a plain painterly background fading to #11151E, landscape 3:2.

A round, fist-sized tree frog with translucent sea-green skin, large golden eyes, and a cluster of three glowing violet mushroom caps growing cheerfully from its back that release sparkling dust whenever it jumps.

In a gentle low hop just above the ground, three-quarter side view with a round frog body, two front legs and two folded hind legs, plausible tree-frog toes and two large golden eyes. Sea-green translucent skin is represented by luminous planar oil glazes and opaque bristle accents, not wet photographic gloss. Exactly three violet mushroom caps on short stems grow from the back, each cap distinct and countable; a small trail of sparse sparkling spore dust hangs behind them. Violet stays a restrained local accent with tight glow.

A small charming hearth-companion of Kaelvorn, never cute-cartoon. Keep natural proportions and an approachable quiet presence. Subject occupies about 70 percent of image height with at least 10 percent clearance around every extremity and defining feature. Plain subdued indigo and umber painterly backdrop, only a minimal ground plane; no scenery or additional beings. Use the supplied images solely as style references, not edit targets: image 1, art/style/candidate-a.png, fixes oil surface, bristle stroke scale, edge economy, palette and lighting; image 2, art/style/anchor-3-creature.png, fixes rough creature materials and painted light integration, overriding its boss scale and humanoid anatomy; image 3, art/style/anchor-2-hero.png, fixes isolated dark backdrop and decisive material highlights, without borrowing its armour or weapon. Invent the requested pet and composition. Work in broad visible oil strokes, concentrating crisp edges at the head or defining feature and losing some peripheral edges. Generate one opaque full-bleed PNG, exact landscape 3:2, at the largest native size supported, target 3072 x 2048 pixels.

Revision: show exactly THREE clearly separate violet mushroom caps growing on three short stems from the frog's back. Arrange the three caps in a staggered row on the far upper silhouette: a small cap at rear left, a medium cap at upper middle, a larger cap behind the shoulders to the right. All three cap silhouettes must be visible with dark gaps, without overlapping the eyes. Keep skin sea-green with translucent painted edges and natural-sized golden frog eyes, slightly smaller and less round than before. A gentle frog hop with four correct limbs, no grin or cartoon face.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

# Phase 5 — key art and website concept art

Generated 2026-10-26 with the built-in `image_gen.imagegen` tool; no CLI/API fallback. Model: `gpt-image`, identified by the PNG C2PA software-agent provenance; a more specific revision is not exposed. Every call supplied local style-reference images and `transparent_background: false`. Each prompt requested the largest native 16:9 output, targeting 3840 × 2160. The tool exposes no size selector and returned 1672 × 941 px for all 17 attempts: approximately 16:9 (not mathematically exact 16:9), opaque RGB PNG. Final files are native copies, without resizing, cropping, recolouring or overlays; originals remain at the tool's generated-image location.

Read `docs/STYLE.md` in full and the supporting art-direction sections 4–5; visually inspected the candidate and all four anchors before generation. Every attempt was inspected at original resolution and at approximately 300 px wide. Final review covered oil medium, three-tone masses, anatomy, requested subjects/counts, blank text zones, absence of logos/watermarks, and plain functional interface divisions. The UI concepts necessarily depict functional panel masses, map viewport and tree nodes; they omit decorative picture surrounds and bevelled icon slots. Full-size paint and small-card readability guided the remakes below.

Palette checks: the seven fixed hexes remain unchanged in every prompt. Native colours are mixed and do not reproduce those hexes exactly. The per-file samples below are RGB medians of the darkest fifth and a filtered warm-material sample, measured on a 200 px inspection thumbnail; they are diagnostic samples, not replacements for the fixed palette. Some UI shadow samples fall below the intended #11151E floor, and the brighter vistas have warmer resting masses than the ideal. No corrective colour processing was applied.

## `art/key-art/home.png`

- Tool: built-in `image_gen.imagegen`; model: `gpt-image` (exact revision not exposed).
- Requested: largest native landscape 16:9, target 3840 × 2160. Actual: **1672 × 941 px**, opaque RGB PNG, all attempts.
- References, in supplied order: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`. Style references only; roles are specified in the prompts.
- Attempts: 2; remakes: 1; final attempt retained.
- Palette sample: dark-mass median `#3F3122`; warm-material median `#BCA081`.

### Attempt 1 — discarded

Discarded: the four correct silhouettes and weapons match the references well, but the horizon is high and bright textured upper-left sky competes with headline space. One composition remake requested.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

Home page hero of Kaelvorn: exactly four Calling exemplars, standing apart with clear silhouettes, seen from behind on a dark basalt ridge at golden hour. Left to right: Valen Korr, a huge broad granite-skinned man, bare faceted stone head and stone forearms, carrying a large green-bronze tower shield on his left and a short heavy brass mace in his right hand; Lyra Vance, a slender healer in long weathered robes holding a lantern-staff of soft green light; Kaelen Vos, a lean desert swordsman in wrapped cloth with two curved blades, one warm gold and the other muted dusk-violet, both separately visible; Tessa Vane-Kettler, a short stocky engineer with goggles on her head, leather work gear and a chunky brass hand-mortar with a broad open muzzle. Exactly four people, no pets, no floating characters. Keep heads and weapons separated and show their complete silhouettes inside the bottom third without crowding. Beyond them, continent-wide rivers, plateaus and distant limestone terrain under the Canopy: colossal golden-amber STONE arches crossing the middle-right sky, geological weathered spans rather than light beams. On the right horizon stands broken First Spire Sol-Vara, its upper half visibly suspended well above its broken base by thin white-light tethers. From the break rises the Pale Wake, a reverse waterfall of silver-white radiance spiralling upward into the sky. Keep the horizon at two-thirds of image height and the upper-left third quiet, low contrast and free of arches, bright streaks or objects for a future title and countdown.

Use reference image 1, art/style/candidate-a.png, for oil surface, stroke scale, edge economy, palette and lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric landscape depth and broad stone brushwork. These are style references only: invent the requested subject and composition, and do not inherit their party, city or spire. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained after one remake: broad bristle/knife oil surface, warm ochre against indigo, all four specified exemplars with correct equipment, stone arches and split tethered spire. Upper-left is quieter. Weakness: horizon and hero heads remain higher than the suffix's bottom-third ideal; goggles, green-bronze hue and blade colours lose clarity at 300 px.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

Home page hero of Kaelvorn: exactly four Calling exemplars, standing apart with clear silhouettes, seen from behind on a dark basalt ridge at golden hour. Left to right: Valen Korr, a huge broad granite-skinned man, bare faceted stone head and stone forearms, carrying a large green-bronze tower shield on his left and a short heavy brass mace in his right hand; Lyra Vance, a slender healer in long weathered robes holding a lantern-staff of soft green light; Kaelen Vos, a lean desert swordsman in wrapped cloth with two curved blades, one warm gold and the other muted dusk-violet, both separately visible; Tessa Vane-Kettler, a short stocky engineer with goggles on her head, leather work gear and a chunky brass hand-mortar with a broad open muzzle. Exactly four people, no pets, no floating characters. Keep heads and weapons separated and show their complete silhouettes inside the bottom third without crowding. Beyond them, continent-wide rivers, plateaus and distant limestone terrain under the Canopy: colossal golden-amber STONE arches crossing the middle-right sky, geological weathered spans rather than light beams. On the right horizon stands broken First Spire Sol-Vara, its upper half visibly suspended well above its broken base by thin white-light tethers. From the break rises the Pale Wake, a reverse waterfall of silver-white radiance spiralling upward into the sky. Keep the horizon at two-thirds of image height and the upper-left third quiet, low contrast and free of arches, bright streaks or objects for a future title and countdown.

Use reference image 1, art/style/candidate-a.png, for oil surface, stroke scale, edge economy, palette and lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric landscape depth and broad stone brushwork. These are style references only: invent the requested subject and composition, and do not inherit their party, city or spire. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

Revision for headline layout and scale only: the top-left forty percent must be a broad uninterrupted field of low-contrast muted indigo-ochre cloud haze, with no sun disc, no sunbeams and no sharp speckled impasto there. Put all Canopy arches on the far right half, none crossing the headline area. Lower the distant horizon to y=67% and shrink the correctly described four heroes so their heads lie no higher than y=63%, with boots around y=91%. Keep the upper two-thirds predominantly sky, the four complete figures in the lower third, and retain every specified weapon, green-bronze shield, stone skin, goggles, suspended spire and silver-white upward Wake. Reduce tiny landscape ruins into three broad atmospheric masses. Request an exact 16:9 pixel canvas, preferably 3840 x 2160 or 2048 x 1152, at the largest native output available.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/key-art/coming-soon.png`

- Tool: built-in `image_gen.imagegen`; model: `gpt-image` (exact revision not exposed).
- Requested: largest native landscape 16:9, target 3840 × 2160. Actual: **1672 × 941 px**, opaque RGB PNG, all attempts.
- References, in supplied order: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`. Style references only; roles are specified in the prompts.
- Attempts: 2; remakes: 1; final attempt retained.
- Palette sample: dark-mass median `#25231E`; warm-material median `#937558`.

### Attempt 1 — discarded

Discarded: strong oil medium and three bronze-bell basalt towers, but the left crack is indistinct, the plain is too bright for darkening urgency, and the distant Wake has excess teal. One targeted remake requested.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

Three colossal Chime-Spires of bronze and basalt stand across a darkening empty plain: three distinct tapering bell towers with heavy exposed golden-lit bells, monolithic lower basalt and weathered bronze upper structures. Each spire has one delicate hairline silver crack creeping up its side, with a tiny near-white silver core. Golden light still pulses from all three bells, warm painted bounce on their worn bronze. Far behind on the right horizon, the Pale Wake forms a distant silver-white upward storm. No people, animals, settlements or extra spires. Mood: the clock is running, restrained ominous urgency. Arrange the three spires from lower-middle to right with enough sky clearance to show every bell and tower tip; use broad plain and dark foreground rock masses. Keep the upper-left third low contrast and almost empty, and the horizon on the bottom third.

Use reference image 1, art/style/candidate-a.png, for oil surface, stroke scale, edge economy, palette and lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric landscape depth and broad stone brushwork. These are style references only: invent the requested subject and composition, and do not inherit their party, city or spire. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained after one remake: darkening empty plain, three complete bronze-and-basalt bell towers, three visible silver cracks, warm bell cores and distant silver-white Wake. Strong handmade oil surface and calm upper-left. Weakness: repeated fine ruins are busier than ideal and the smallest crack becomes faint at 300 px.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

Three colossal Chime-Spires of bronze and basalt stand across a darkening empty plain: three distinct tapering bell towers with heavy exposed golden-lit bells, monolithic lower basalt and weathered bronze upper structures. Each spire has one delicate hairline silver crack creeping up its side, with a tiny near-white silver core. Golden light still pulses from all three bells, warm painted bounce on their worn bronze. Far behind on the right horizon, the Pale Wake forms a distant silver-white upward storm. No people, animals, settlements or extra spires. Mood: the clock is running, restrained ominous urgency. Arrange the three spires from lower-middle to right with enough sky clearance to show every bell and tower tip; use broad plain and dark foreground rock masses. Keep the upper-left third low contrast and almost empty, and the horizon on the bottom third.

Use reference image 1, art/style/candidate-a.png, for oil surface, stroke scale, edge economy, palette and lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric landscape depth and broad stone brushwork. These are style references only: invent the requested subject and composition, and do not inherit their party, city or spire. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

Revision for urgency, silver cracks and quiet headline space: paint a genuinely darkening plain with dim ochre residual light, not a bright golden noon. Make each of the three individual silver hairline cracks clearly visible from its lower base toward its bell, separate from any stone seam. The distant Pale Wake is silver-white and indigo only, without a saturated teal storm. Preserve small golden pulses inside the three bronze bells. The upper-left forty percent is an uninterrupted low-contrast field of muted indigo-grey haze; no bright cloud flecks or sunbeams there. Keep all three complete tower silhouettes on the middle-right. Preserve expressive oil strokes and atmospheric depth.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/key-art/world.png`

- Tool: built-in `image_gen.imagegen`; model: `gpt-image` (exact revision not exposed).
- Requested: largest native landscape 16:9, target 3840 × 2160. Actual: **1672 × 941 px**, opaque RGB PNG, all attempts.
- References, in supplied order: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`. Style references only; roles are specified in the prompts.
- Attempts: 2; remakes: 1; final attempt retained.
- Palette sample: dark-mass median `#203442`; warm-material median `#B2926B`.

### Attempt 1 — discarded

Discarded: convincing oil surface, terraces, deltas and central sea, but the crescent's exterior shorelines run out of frame and the upper-left is too bright. Remake requested to show the complete continental silhouette and quiet headline sky.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

An aerial oblique panorama of the entire crescent continent of Kaelvorn at dawn, seen from high above a dark foreground rock outcrop. Its crescent-shaped landmass curves around the central inland sea, the Mirror-Reach, with a narrow southern strait connecting it to the outer ocean. Clearly distinct regions within the same crescent: terraced white limestone plateaus in the west on the left; branching river deltas and deep fjords in the east on the right; a pale glass highland and the broken First Spire Sol-Vara in the north, at the far top of the crescent. Sol-Vara's detached upper section hangs on fine white light tethers, with the silver-white Pale Wake ascending. The Canopy's vast golden-amber stone arches vault across the middle-right overhead, not a ring enclosing the image. Dawn ochre catches limestone terraces while sea and fjords rest in indigo. No labels, map glyphs, compass, people or ships. Reconcile aerial geography with a low distant sea horizon at two-thirds image height: the complete crescent and central sea occupy the lower two-thirds; keep the upper-left sky calm and low contrast.

Use reference image 1, art/style/candidate-a.png, for oil surface, stroke scale, edge economy, palette and lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric landscape depth and broad stone brushwork. These are style references only: invent the requested subject and composition, and do not inherit their party, city or spire. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained after one remake: central inland sea and crescent geography now read at 300 px, west white terraces contrast with east fjords/deltas, suspended northern spire and overhead stone arches are present. Candidate-like ochre impasto and indigo depth. Weakness: the northern glass highland can read as snow, the far eastern outer shoreline is still tight, and the horizon/title sky remains higher and brighter than the nominal suffix layout.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Key art and regions: 24 mm wide-angle, horizon on the bottom third, three atmospheric depth planes, dark foreground repoussoir, quiet low-contrast upper-left sky reserved for future text, landscape 16:9.

An aerial oblique panorama of the entire crescent continent of Kaelvorn at dawn, seen from high above a dark foreground rock outcrop. Its crescent-shaped landmass curves around the central inland sea, the Mirror-Reach, with a narrow southern strait connecting it to the outer ocean. Clearly distinct regions within the same crescent: terraced white limestone plateaus in the west on the left; branching river deltas and deep fjords in the east on the right; a pale glass highland and the broken First Spire Sol-Vara in the north, at the far top of the crescent. Sol-Vara's detached upper section hangs on fine white light tethers, with the silver-white Pale Wake ascending. The Canopy's vast golden-amber stone arches vault across the middle-right overhead, not a ring enclosing the image. Dawn ochre catches limestone terraces while sea and fjords rest in indigo. No labels, map glyphs, compass, people or ships. Reconcile aerial geography with a low distant sea horizon at two-thirds image height: the complete crescent and central sea occupy the lower two-thirds; keep the upper-left sky calm and low contrast.

Use reference image 1, art/style/candidate-a.png, for oil surface, stroke scale, edge economy, palette and lighting; use reference image 2, art/style/anchor-1-vista.png, for atmospheric landscape depth and broad stone brushwork. These are style references only: invent the requested subject and composition, and do not inherit their party, city or spire. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

Revision for geography and headline space: pull the aerial camera much farther back, high above the ocean, until the COMPLETE crescent island-continent silhouette is visible, with a continuous band of open ocean outside both western and eastern coastlines and around its two southern tips. No land may extend off the left or right image edges. Make its central inland sea unmistakably enclosed on three sides, open through one narrow southern channel. Keep all three regional identities readable in large grouped painted shapes rather than dense tiny topography. Reduce the foreground rock to one small dark bottom-left corner wedge so it does not conceal the continent. The upper-left sky must be dim quiet haze without a visible sun or bright speckled cloud, for future title space. Place Canopy arches and suspended spire in the upper-right only. Preserve dawn warm/cool polarity and the references' bold oil surface.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/gallery/concept-home.png`

- Tool: built-in `image_gen.imagegen`; model: `gpt-image` (exact revision not exposed).
- Requested: largest native landscape 16:9, target 3840 × 2160. Actual: **1672 × 941 px**, opaque RGB PNG, all attempts.
- References, in supplied order: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`, `art/style/anchor-2-hero.png`, `art/style/anchor-3-creature.png`, `art/style/anchor-4-icons.png`. Style references only; roles are specified in the prompts.
- Attempts: 2; remakes: 1; final attempt retained.
- Palette sample: dark-mass median `#14181E`; warm-material median `#A38562`.

### Attempt 1 — discarded

Discarded: oil medium, four blank tiles and three pillar panels were clear, but the candidate's wrong party with wolf was copied, the Canopy was absent, and interface diamonds/corner trim read as decorative painted frames. Remake requested for correct hero subject and plain dividers.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

A painted website home screen for Kaelvorn as an in-game interface. The upper sixty percent is one expansive hero artwork showing four rear-view adventurers on a basalt ridge, golden-amber stone Canopy arches over distant terrain, and a broken suspended spire with silver upward radiance on the right. The left side of the hero has broad empty title and subtitle bars. Directly underneath is a countdown assembly of exactly four blank equal rectangular tiles in a simple straight brass bracket, no digits. The lower content area has exactly three adjacent pillar panels, each containing a distinct painted vignette: a stone-skinned shield guardian, a landscape gorge, and a monumental ruin boss, with two short blank caption bars beneath each. Bottom action-bar navigation with simple painted symbols. One small floating tooltip card with a tiny skill symbol and empty bars. Clear spacious hierarchy, no ornamental outer frame.

Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, stroke scale, edge economy, palette and lighting. The other four images are style references only: art/style/anchor-1-vista.png supplies landscape atmosphere; art/style/anchor-2-hero.png supplies character brush planes and materials; art/style/anchor-3-creature.png supplies monumental boss stone and integrated glow; art/style/anchor-4-icons.png supplies simple painted icon silhouettes. Invent the requested screen rather than copying any reference composition. All typography areas are broad empty horizontal bars, completely blank without glyphs, numerals or scribbles. The interface uses flat stone panel masses and thin brass separators, never an ornamental picture surround or bevelled icon slots. A compact action-bar navigation sits along the bottom with frameless painted symbols. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained after one remake: correct four exemplar types, stone Canopy, four blank countdown tiles, three pillar panels, plain panel separations, bottom action bar and blank tooltip. Oil/impasto materials match anchors at full and 300 px. Weakness: the spire upper fragments read more complex than one suspended half; small weapon/face details soften at card scale.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

A painted website home screen for Kaelvorn as an in-game interface. The upper sixty percent is one expansive hero artwork showing four rear-view adventurers on a basalt ridge, golden-amber stone Canopy arches over distant terrain, and a broken suspended spire with silver upward radiance on the right. The left side of the hero has broad empty title and subtitle bars. Directly underneath is a countdown assembly of exactly four blank equal rectangular tiles in a simple straight brass bracket, no digits. The lower content area has exactly three adjacent pillar panels, each containing a distinct painted vignette: a stone-skinned shield guardian, a landscape gorge, and a monumental ruin boss, with two short blank caption bars beneath each. Bottom action-bar navigation with simple painted symbols. One small floating tooltip card with a tiny skill symbol and empty bars. Clear spacious hierarchy, no ornamental outer frame.

Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, stroke scale, edge economy, palette and lighting. The other four images are style references only: art/style/anchor-1-vista.png supplies landscape atmosphere; art/style/anchor-2-hero.png supplies character brush planes and materials; art/style/anchor-3-creature.png supplies monumental boss stone and integrated glow; art/style/anchor-4-icons.png supplies simple painted icon silhouettes. Invent the requested screen rather than copying any reference composition. All typography areas are broad empty horizontal bars, completely blank without glyphs, numerals or scribbles. The interface uses flat stone panel masses and thin brass separators, never an ornamental picture surround or bevelled icon slots. A compact action-bar navigation sits along the bottom with frameless painted symbols. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

Revision for correct hero subject and flat interface: invent NEW hero artwork rather than reproducing the candidate image. Exactly four rear-view Calling exemplars: massive granite-skinned Valen with GREEN-BRONZE TOWER SHIELD and BRASS MACE; slender Lyra with SOFT GREEN LANTERN-STAFF; desert swordsman Kaelen with TWO CURVED BLADES, gold and muted dusk-violet; short stocky Tessa with GOGGLES and BRASS HAND-MORTAR. No wolf, bow, floating mage or ordinary sword knight. Large golden-amber stone Canopy arches must cross the right half of the sky behind them. Sol-Vara must be visibly split into two parts tethered with white light; the Wake is silver-white, no saturated teal sky vortex. Keep exactly four EMPTY countdown tiles and three pillar panels. Remove ALL decorative frame corners, diamonds, ornamental brackets and gold outlines around artwork; use only straight thin brass divider strokes separating flat dark stone panel masses. Empty text bars have no bordering trim. Retain the bottom navigation symbols and one plain tooltip.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/gallery/concept-character.png`

- Tool: built-in `image_gen.imagegen`; model: `gpt-image` (exact revision not exposed).
- Requested: largest native landscape 16:9, target 3840 × 2160. Actual: **1672 × 941 px**, opaque RGB PNG, all attempts.
- References, in supplied order: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`, `art/style/anchor-2-hero.png`, `art/style/anchor-3-creature.png`, `art/style/anchor-4-icons.png`. Style references only; roles are specified in the prompts.
- Attempts: 2; remakes: 1; final attempt retained.
- Palette sample: dark-mass median `#101115`; warm-material median `#9E7A52`.

### Attempt 1 — discarded

Discarded: strong anchor-like oil medium and correct splash/stats/ability-bar layout with blank text, but the hero inherited the anchor helmet and pointed shield instead of bare granite head and tower shield; decorative header diamonds also appeared. Remake requested.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

A painted character-select screen for Kaelvorn. Left half: a tall knees-up hero splash of Valen Korr, a huge broad granite-skinned man with faceted stone head and forearms, weathered indigo armour, green-bronze tower shield and short brass mace, anatomy readable with natural hands. Strong dark silhouette and warm bristle highlights, not a normal flesh-skinned knight. Right half: a dark stone stat panel with a broad empty name bar, six simple stat rows made of tiny symbols plus entirely blank horizontal bars, and a lower horizontal ability bar of six distinct frameless painted ability symbols. A narrow open tooltip card sits beside one selected ability with a symbol and empty description bars. Bottom action-bar navigation. Keep character artwork dominant with a clear divide between splash and stats, no figures elsewhere.

Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, stroke scale, edge economy, palette and lighting. The other four images are style references only: art/style/anchor-1-vista.png supplies landscape atmosphere; art/style/anchor-2-hero.png supplies character brush planes and materials; art/style/anchor-3-creature.png supplies monumental boss stone and integrated glow; art/style/anchor-4-icons.png supplies simple painted icon silhouettes. Invent the requested screen rather than copying any reference composition. All typography areas are broad empty horizontal bars, completely blank without glyphs, numerals or scribbles. The interface uses flat stone panel masses and thin brass separators, never an ornamental picture surround or bevelled icon slots. A compact action-bar navigation sits along the bottom with frameless painted symbols. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained after one remake: bare faceted granite head and forearms, green-bronze rectangular tower shield and brass mace, tall splash at left, six blank stat rows, six ability symbols, open blank tooltip and bottom navigation. Thick ochre/indigo oil surfaces match anchors at full and 300 px; no obvious anatomy defects. Weakness: dense armour rivets and small ability detail compete at card scale, and the tooltip has a heavier functional stone edge than the flat-panel ideal.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

A painted character-select screen for Kaelvorn. Left half: a tall knees-up hero splash of Valen Korr, a huge broad granite-skinned man with faceted stone head and forearms, weathered indigo armour, green-bronze tower shield and short brass mace, anatomy readable with natural hands. Strong dark silhouette and warm bristle highlights, not a normal flesh-skinned knight. Right half: a dark stone stat panel with a broad empty name bar, six simple stat rows made of tiny symbols plus entirely blank horizontal bars, and a lower horizontal ability bar of six distinct frameless painted ability symbols. A narrow open tooltip card sits beside one selected ability with a symbol and empty description bars. Bottom action-bar navigation. Keep character artwork dominant with a clear divide between splash and stats, no figures elsewhere.

Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, stroke scale, edge economy, palette and lighting. The other four images are style references only: art/style/anchor-1-vista.png supplies landscape atmosphere; art/style/anchor-2-hero.png supplies character brush planes and materials; art/style/anchor-3-creature.png supplies monumental boss stone and integrated glow; art/style/anchor-4-icons.png supplies simple painted icon silhouettes. Invent the requested screen rather than copying any reference composition. All typography areas are broad empty horizontal bars, completely blank without glyphs, numerals or scribbles. The interface uses flat stone panel masses and thin brass separators, never an ornamental picture surround or bevelled icon slots. A compact action-bar navigation sits along the bottom with frameless painted symbols. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

Revision for the hero and plain UI: remove the helmet entirely. Valen has a BARE granite head, clear stone face planes and stone forearms with no helmet, no mask, no normal human skin. His green-bronze shield is a tall rectangular TOWER SHIELD, not a pointed oval shield, with only a few plain metal bands. His right hand holds the short heavy BRASS MACE, fully inside the artwork. Show natural stone hands with five fingers and no extra limbs. Borrow only the anchors' paint, not their anonymous helmeted knight. Remove gold rectangular outlines, diamond ornaments and decorative corner marks from every stat panel, heading and tooltip. Use blank unbordered stone bars and a few straight tarnished-brass divider strokes. Ability symbols are frameless, with no square bracket selection outline. Keep the existing correct left-splash/right-stats layout and bottom navigation.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/gallery/concept-skill-tree.png`

- Tool: built-in `image_gen.imagegen`; model: `gpt-image` (exact revision not exposed).
- Requested: largest native landscape 16:9, target 3840 × 2160. Actual: **1672 × 941 px**, opaque RGB PNG, all attempts.
- References, in supplied order: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`, `art/style/anchor-2-hero.png`, `art/style/anchor-3-creature.png`, `art/style/anchor-4-icons.png`. Style references only; roles are specified in the prompts.
- Attempts: 1; remakes: 0; final attempt retained.
- Palette sample: dark-mass median `#0A0D10`; warm-material median `#7C5F40`.

### Attempt 1 — retained

Retained first attempt: three large columns of round and square nodes, thin brass connections, tight painted viridian glow, a single open blank tooltip and bottom action-bar navigation. Thick directional oil texture matches anchors; no lettering. Weakness: some brass junctions and peripheral ochre texture are busy, and the smallest symbols lose identity at 300 px.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

A painted talent-tree interface for Kaelvorn. Three evenly spaced vertical columns of glowing nodes fill the central seventy percent: left column shield and stone motifs, centre lantern and healing motifs, right column curved sword and dusk motifs. Exactly three major columns; each branches within its own column through thin tarnished-brass connecting lines, with a mix of round and square flat nodes. Roughly seven nodes per column, larger important nodes, small near-white cores with tight restrained viridian corona on selected paths and muted indigo inactive nodes. Node symbols are nonlinguistic tiny shield, staff, sword, hand and spiral paintings, with no glyphs. Three empty title bars above the columns. One open tooltip card on the middle-right, occupying spare space without hiding the tree: painted skill symbol, broad blank heading bar and several completely empty description bars. Dark stone background, spare brass dividers, bottom action-bar navigation, no hero portrait or extra landscape.

Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, stroke scale, edge economy, palette and lighting. The other four images are style references only: art/style/anchor-1-vista.png supplies landscape atmosphere; art/style/anchor-2-hero.png supplies character brush planes and materials; art/style/anchor-3-creature.png supplies monumental boss stone and integrated glow; art/style/anchor-4-icons.png supplies simple painted icon silhouettes. Invent the requested screen rather than copying any reference composition. All typography areas are broad empty horizontal bars, completely blank without glyphs, numerals or scribbles. The interface uses flat stone panel masses and thin brass separators, never an ornamental picture surround or bevelled icon slots. A compact action-bar navigation sits along the bottom with frameless painted symbols. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

Interface restraint: only flat functional UI divisions. No diamond ornaments, decorative corner marks, filigree or bevels. Empty heading and description bars have no gold outlines. Tooltips are plain dark cards with a thin straight separator, not picture frames. Do not reproduce the references' subjects or layouts.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/gallery/concept-map.png`

- Tool: built-in `image_gen.imagegen`; model: `gpt-image` (exact revision not exposed).
- Requested: largest native landscape 16:9, target 3840 × 2160. Actual: **1672 × 941 px**, opaque RGB PNG, all attempts.
- References, in supplied order: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`, `art/style/anchor-2-hero.png`, `art/style/anchor-3-creature.png`, `art/style/anchor-4-icons.png`. Style references only; roles are specified in the prompts.
- Attempts: 2; remakes: 1; final attempt retained.
- Palette sample: dark-mass median `#13171B`; warm-material median `#A6824E`.

### Attempt 1 — discarded

Discarded: five markers, crescent/central sea and quest log were clear and the oil medium matched, but the map was a three-dimensional aerial landscape rather than parchment-and-ink cartography. Remake requested with flat top-down ink coastlines, hatching and simple brass viewport.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

A painted world-map and quest-log interface for Kaelvorn. Left seventy percent: a parchment-and-ink cartographic map of one crescent-shaped continent curving around a central inland sea, the Mirror-Reach, in a simple flat tarnished-brass rectangular map frame integrated into the UI, without decorative ornament or picture surround. North is at the top. Western left coast has stepped limestone plateaus; eastern right coast has branching deltas and fjords; northern pale glass highland has a tiny broken-spire silhouette. A narrow southern strait connects central sea to ocean. Subtle ink hatching and broad oil-painted parchment planes, no place names, compass letters, grid numerals or writing. Five small restrained glowing region markers with near-white cores and tight viridian halos. Right thirty percent: a dark stone quest-log panel with three stacked entries represented by small pictorial symbols and completely empty horizontal bars. One compact marker tooltip with blank bars at the edge of the map. Bottom action-bar navigation, no ornamental outer border.

Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, stroke scale, edge economy, palette and lighting. The other four images are style references only: art/style/anchor-1-vista.png supplies landscape atmosphere; art/style/anchor-2-hero.png supplies character brush planes and materials; art/style/anchor-3-creature.png supplies monumental boss stone and integrated glow; art/style/anchor-4-icons.png supplies simple painted icon silhouettes. Invent the requested screen rather than copying any reference composition. All typography areas are broad empty horizontal bars, completely blank without glyphs, numerals or scribbles. The interface uses flat stone panel masses and thin brass separators, never an ornamental picture surround or bevelled icon slots. A compact action-bar navigation sits along the bottom with frameless painted symbols. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

Interface restraint: only flat functional UI divisions. No diamond ornaments, decorative corner marks, filigree or bevels. Empty heading and description bars have no gold outlines. Tooltips are plain dark cards with a thin straight separator, not picture frames. Do not reproduce the references' subjects or layouts.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Retained after one remake: warm parchment field, ink-edged crescent coastline and schematic mountains/rivers, five small glowing region markers, plain functional brass map viewport, blank quest log and tooltip, bottom action bar. Painterly material and palette remain consistent at full and 300 px. Weakness: mountain/terrace forms retain more dimensional modelling than a pure ink map; the southern channel meets the lower viewport edge.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

A painted world-map and quest-log interface for Kaelvorn. Left seventy percent: a parchment-and-ink cartographic map of one crescent-shaped continent curving around a central inland sea, the Mirror-Reach, in a simple flat tarnished-brass rectangular map frame integrated into the UI, without decorative ornament or picture surround. North is at the top. Western left coast has stepped limestone plateaus; eastern right coast has branching deltas and fjords; northern pale glass highland has a tiny broken-spire silhouette. A narrow southern strait connects central sea to ocean. Subtle ink hatching and broad oil-painted parchment planes, no place names, compass letters, grid numerals or writing. Five small restrained glowing region markers with near-white cores and tight viridian halos. Right thirty percent: a dark stone quest-log panel with three stacked entries represented by small pictorial symbols and completely empty horizontal bars. One compact marker tooltip with blank bars at the edge of the map. Bottom action-bar navigation, no ornamental outer border.

Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, stroke scale, edge economy, palette and lighting. The other four images are style references only: art/style/anchor-1-vista.png supplies landscape atmosphere; art/style/anchor-2-hero.png supplies character brush planes and materials; art/style/anchor-3-creature.png supplies monumental boss stone and integrated glow; art/style/anchor-4-icons.png supplies simple painted icon silhouettes. Invent the requested screen rather than copying any reference composition. All typography areas are broad empty horizontal bars, completely blank without glyphs, numerals or scribbles. The interface uses flat stone panel masses and thin brass separators, never an ornamental picture surround or bevelled icon slots. A compact action-bar navigation sits along the bottom with frameless painted symbols. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

Revision for CARTOGRAPHY rather than landscape: the map is a FLAT TOP-DOWN PARCHMENT SHEET, warm aged vellum, with the crescent continent drawn using DARK UMBER INK COASTLINES, sparse hatched contour lines, small schematic mountain chevrons and branching ink rivers. Its central inland sea is a broad quiet pale-blue/indigo ink wash, not a realistic reflective ocean. No three-dimensional aerial landscape, no perspective cliffs, no realistic waterfalls, no horizon or sky inside the map. Use oil bristle and linen texture on parchment and interface, while the geographic marks are unmistakably hand-inked. Keep the entire island-continent coastline surrounded by blank parchment; no place names, lettering or compass symbols. Add a simple thin straight tarnished-brass functional rectangle around the map viewport with no ornament or bevel. Keep five restrained viridian markers, right-hand blank quest log, blank tooltip and bottom action bar. The small quest thumbnails may stay oil-painted.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/gallery/concept-raids.png`

- Tool: built-in `image_gen.imagegen`; model: `gpt-image` (exact revision not exposed).
- Requested: largest native landscape 16:9, target 3840 × 2160. Actual: **1672 × 941 px**, opaque RGB PNG, all attempts.
- References, in supplied order: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`, `art/style/anchor-2-hero.png`, `art/style/anchor-3-creature.png`, `art/style/anchor-4-icons.png`. Style references only; roles are specified in the prompts.
- Attempts: 1; remakes: 0; final attempt retained.
- Palette sample: dark-mass median `#0B1016`; warm-material median `#927552`.

### Attempt 1 — retained

Retained first attempt: colossal bell-boss portrait, three blank difficulty tabs, five distinct party slots, blank action/tooltip cards and bottom navigation. Broad oil planes, warm bell impasto and cool stone agree with the anchors at full and 300 px; no visible lettering or broken faces. Weakness: boss lower silhouette merges with the landscape, and a few teal fissures are stronger than the requested single subtle silver crack.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

A painted raid-finder interface for Kaelvorn. Left half: one large boss portrait panel containing a monumental basalt-and-bronze bell colossus, compact head, immense shoulders, warm glowing bell in its chest, a single silver crack and subdued viridian bounce, painted with broad chisel-cut stone planes. Upper right: exactly three simple difficulty tabs represented by blank horizontal blocks, one softly highlighted in ochre. Below the tabs an empty raid-title bar and short blank description bars. Centre-right a horizontal party composition strip of exactly five equally spaced flat slots, each holding one distinct small painted bust or silhouette: shield guardian, lantern healer, desert swordsman, engineer, cloaked ranger; no duplicated heads, no lettering and no bevelled icon frames. Under the party strip, a broad empty action bar and a compact open tooltip with a boss-mechanic symbol and blank description bars. Bottom action-bar navigation. Clear panel hierarchy with resting dark spaces.

Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, stroke scale, edge economy, palette and lighting. The other four images are style references only: art/style/anchor-1-vista.png supplies landscape atmosphere; art/style/anchor-2-hero.png supplies character brush planes and materials; art/style/anchor-3-creature.png supplies monumental boss stone and integrated glow; art/style/anchor-4-icons.png supplies simple painted icon silhouettes. Invent the requested screen rather than copying any reference composition. All typography areas are broad empty horizontal bars, completely blank without glyphs, numerals or scribbles. The interface uses flat stone panel masses and thin brass separators, never an ornamental picture surround or bevelled icon slots. A compact action-bar navigation sits along the bottom with frameless painted symbols. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

Interface restraint: only flat functional UI divisions. No diamond ornaments, decorative corner marks, filigree or bevels. Empty heading and description bars have no gold outlines. Tooltips are plain dark cards with a thin straight separator, not picture frames. Do not reproduce the references' subjects or layouts.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/gallery/concept-coming-soon.png`

- Tool: built-in `image_gen.imagegen`; model: `gpt-image` (exact revision not exposed).
- Requested: largest native landscape 16:9, target 3840 × 2160. Actual: **1672 × 941 px**, opaque RGB PNG, all attempts.
- References, in supplied order: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`, `art/style/anchor-2-hero.png`, `art/style/anchor-3-creature.png`, `art/style/anchor-4-icons.png`. Style references only; roles are specified in the prompts.
- Attempts: 3; remakes: 2; final attempt retained.
- Palette sample: dark-mass median `#0F1217`; warm-material median `#A7855F`.

### Attempt 1 — discarded

Discarded: correct four blank countdown tiles, five empty checklist rows, three cracked bell towers and silver Wake, but the centre spire tip was clipped by the top image edge and the landscape was too bright. Remake requested for complete silhouettes and dusk.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

A painted launch screen for Kaelvorn. Upper half: three colossal bronze-and-basalt Chime-Spires on a darkening plain, exposed bells still pulsing with golden light, one fine silver crack visibly climbing each tower, far-right distant silver-white Pale Wake storm, no people. Across the middle-left, a very large countdown assembly with exactly four equal blank dark stone tiles separated by thin flat brass dividers, entirely empty with no numerals; above it a broad empty headline bar. Right third: a checklist panel with exactly five small empty square checkboxes and broad blank horizontal bars aligned beside them, no ticks or letters. One small open tooltip card with a bell symbol and empty bars near the countdown. Sparse bottom action-bar navigation. Restrained ominous clock-is-running mood, spare functional divisions, no ornamental outer picture frame.

Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, stroke scale, edge economy, palette and lighting. The other four images are style references only: art/style/anchor-1-vista.png supplies landscape atmosphere; art/style/anchor-2-hero.png supplies character brush planes and materials; art/style/anchor-3-creature.png supplies monumental boss stone and integrated glow; art/style/anchor-4-icons.png supplies simple painted icon silhouettes. Invent the requested screen rather than copying any reference composition. All typography areas are broad empty horizontal bars, completely blank without glyphs, numerals or scribbles. The interface uses flat stone panel masses and thin brass separators, never an ornamental picture surround or bevelled icon slots. A compact action-bar navigation sits along the bottom with frameless painted symbols. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

Interface restraint: only flat functional UI divisions. No diamond ornaments, decorative corner marks, filigree or bevels. Empty heading and description bars have no gold outlines. Tooltips are plain dark cards with a thin straight separator, not picture frames. Do not reproduce the references' subjects or layouts.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — discarded

Discarded remake: all three spire silhouettes fit and the dusk mood improved, but countdown outlines gained decorative diamond junctions and the bottom navigation gained ornamental connecting lines. Second and final remake requested to leave plain stone masses with only straight internal brass dividers.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

A painted launch screen for Kaelvorn. Upper half: three colossal bronze-and-basalt Chime-Spires on a darkening plain, exposed bells still pulsing with golden light, one fine silver crack visibly climbing each tower, far-right distant silver-white Pale Wake storm, no people. Across the middle-left, a very large countdown assembly with exactly four equal blank dark stone tiles separated by thin flat brass dividers, entirely empty with no numerals; above it a broad empty headline bar. Right third: a checklist panel with exactly five small empty square checkboxes and broad blank horizontal bars aligned beside them, no ticks or letters. One small open tooltip card with a bell symbol and empty bars near the countdown. Sparse bottom action-bar navigation. Restrained ominous clock-is-running mood, spare functional divisions, no ornamental outer picture frame.

Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, stroke scale, edge economy, palette and lighting. The other four images are style references only: art/style/anchor-1-vista.png supplies landscape atmosphere; art/style/anchor-2-hero.png supplies character brush planes and materials; art/style/anchor-3-creature.png supplies monumental boss stone and integrated glow; art/style/anchor-4-icons.png supplies simple painted icon silhouettes. Invent the requested screen rather than copying any reference composition. All typography areas are broad empty horizontal bars, completely blank without glyphs, numerals or scribbles. The interface uses flat stone panel masses and thin brass separators, never an ornamental picture surround or bevelled icon slots. A compact action-bar navigation sits along the bottom with frameless painted symbols. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

Revision for complete spires and darkening mood: ZOOM OUT the upper landscape artwork so all THREE complete Chime-Spire tips have at least five percent image-height clearance below the top edge. The tallest centre spire must NOT intersect the canvas edge. Keep all three tower bases visible above the countdown panels. Each has one visible fine silver crack and one warm bell core. Dim the sky and plain toward indigo dusk with sparse ochre highlights, retain the far-right silver-white Wake and no people. Keep exactly four huge blank countdown tiles, five empty checklist boxes and bars, plain tooltip and bottom navigation. Do not add decorative frames, letterforms or digits.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 3 — retained

Retained after two remakes: three complete cracked spires, warm bell cores, silver-white Wake, four large blank countdown tiles with straight internal dividers, five empty checklist rows, plain tooltip and bottom navigation. No decorative frame ornaments or lettering. Strong ochre/indigo impasto at full size and clear card hierarchy. Weakness: the tallest spire has less than the requested five-percent top clearance, and the crack on the smallest spire grows faint at 300 px.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

A painted launch screen for Kaelvorn. Upper half: three colossal bronze-and-basalt Chime-Spires on a darkening plain, exposed bells still pulsing with golden light, one fine silver crack visibly climbing each tower, far-right distant silver-white Pale Wake storm, no people. Across the middle-left, a very large countdown assembly with exactly four equal blank dark stone tiles separated by thin flat brass dividers, entirely empty with no numerals; above it a broad empty headline bar. Right third: a checklist panel with exactly five small empty square checkboxes and broad blank horizontal bars aligned beside them, no ticks or letters. One small open tooltip card with a bell symbol and empty bars near the countdown. Sparse bottom action-bar navigation. Restrained ominous clock-is-running mood, spare functional divisions, no ornamental outer picture frame.

Use reference image 1, art/style/candidate-a.png, as the primary authority for oil surface, stroke scale, edge economy, palette and lighting. The other four images are style references only: art/style/anchor-1-vista.png supplies landscape atmosphere; art/style/anchor-2-hero.png supplies character brush planes and materials; art/style/anchor-3-creature.png supplies monumental boss stone and integrated glow; art/style/anchor-4-icons.png supplies simple painted icon silhouettes. Invent the requested screen rather than copying any reference composition. All typography areas are broad empty horizontal bars, completely blank without glyphs, numerals or scribbles. The interface uses flat stone panel masses and thin brass separators, never an ornamental picture surround or bevelled icon slots. A compact action-bar navigation sits along the bottom with frameless painted symbols. Generate one opaque full-bleed PNG, exact landscape 16:9, largest available native size, target 3840 x 2160 pixels.

Final revision, preserve complete tower silhouettes while simplifying UI: all three spire tips fit inside the upper artwork with five percent top clearance, none cropped. UI must be radically plain: FOUR FLAT DARK STONE COUNTDOWN TILES WITHOUT OUTLINES. Only the three internal straight thin vertical brass separator strokes may appear between countdown tiles; no enclosing rectangle, no outer gold trim, no golden corners, no diamonds, no stars at junctions, no carved border or ornamental brackets anywhere. The heading is one plain unbordered blank horizontal stone bar. Checklist is a plain dark panel with five simple empty square checkboxes and five plain unbordered blank bars. Tooltip is a plain dark rectangle with one bell painting and two unbordered empty bars, no outline. Bottom navigation consists of five isolated painted symbols on one continuous dark stone strip without arrows, connecting lines or ornament. Keep oil brushwork on art and materials. Dim indigo dusk, three silver tower cracks, three warm bells and distant silver-white Wake.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

# Redesign — logo concepts (2026-10-26)

Built-in `image_gen.imagegen`, four generations total; no CLI fallback. Three retained opaque RGB PNGs, each native **1254 × 1254 px**, requested 2048 × 2048, square 1:1. References for every call, in order: `art/style/candidate-a.png` (primary style authority), `art/style/anchor-4-icons.png` (isolated icon brush scale); style references only. Original generated files retained; final assets copied without resizing or recoloring.

The fixed prefix and Skill icon suffix were used verbatim. The requested logo identity requires a narrow exception to the avoid list's text, lettering and logo bans; these three clauses were removed, with the subject paragraph allowing only KAELVORN and concept C's K. All other avoid clauses remain verbatim. No extra words were allowed. The icon suffix's nonlinguistic rule was explicitly overridden only for requested lettering.

Review: inspected native images and temporary 32 × 32 emblem crops, also nearest-neighbor enlarged for scrutiny. All retained wordmarks spell KAELVORN. Native background samples are recorded below; exact background color is not guaranteed. QA thumbnails were temporary and are not deliverables. Finisher should simplify small details and rebuild the chosen emblem at favicon size, using the broad silhouette rather than preserving every paint fleck. These are concept lockups, not production vector masters or exported favicons.

## `art/redesign/logo-concepts/logo-a.png`

Retained first attempt. Full KAELVORN spelling verified. Bell silhouette, flared mouth, spire and flanking arcs remain recognizable in a 32 px emblem-only review crop; tiny architectural details disappear. Weakest point: more architectural ornament than requested and tight top clearance; stone wordmark has brass-like highlights. Background corner sampled #090B0E rather than exact #0B0D12.

### Attempt 1 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

Concept A: a monumental bell-and-spire emblem above a broad carved STONE wordmark. Centered vertical lockup. Emblem occupies the central upper half, wordmark spans about 80 percent of canvas width below with clear separation. A single thick tarnished-brass bell silhouette with a low flared mouth and one broad central clapper; its crown rises into a stout pointed bronze Chime-Spire. One clean diagonal negative-space fracture just below the tip recalls broken Sol-Vara. Two bold short outward sound arcs flank the bell, evoking the golden Canopy arches. Favor one coherent compact bell silhouette, not a detailed building. Wordmark KAELVORN in confident broad wedge-serif capitals chiseled from umber limestone, sunlit ochre cut edges and indigo recesses; individually readable letters, restrained engravings, straight baseline. The stone letters should look materially different from the bronze emblem.

Use case: logo-brand. Create one square 1:1 opaque PNG logo concept, target 2048 x 2048 pixels. The icon suffix governs the emblem's medium and isolation; this request explicitly permits the KAELVORN logo and its engraved lettering, overriding the nonlinguistic constraint only for requested lettering. No text or lettering anywhere except the exact requested wordmark (and K monogram in concept C). Text verbatim: KAELVORN, eight capitals in this order K A E L V O R N. No tagline, no captions, no concept labels, no other branding. Flat uniform #0B0D12 across all unpainted background, including corners; no backdrop texture, vignette, landscape, cast shadow or glow haze. Reference image 1, art/style/candidate-a.png, is the primary style authority; reference image 2, art/style/anchor-4-icons.png, supplies isolated icon brush scale. Borrow tactile oil surfaces, decisive brass strokes, indigo fill and edge economy only; invent the requested logo rather than copying their compositions. Emblem must be a robust simple silhouette independently recognizable when cropped and reduced to 32 x 32 px: broad strokes, wide counters, no filigree, no micro ornament. Leave generous breathing room around emblem and wordmark; all shapes fully inside canvas.

No watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/redesign/logo-concepts/logo-b.png`

Retained first attempt. Full KAELVORN spelling verified. At 32 px the shield, central spire and sound arcs read clearly; the fracture is less reliable. Weakest point: crimson banner overlaps the shield, so an independent favicon needs a clean shield-only redraw/extraction by the finisher rather than a simple rectangular crop. Shield has more raised rim than requested. Background corner sampled #07090D rather than exact #0B0D12.

### Attempt 1 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

Concept B: a heraldic crest, a solid brass SHIELD bearing a CRACKED SPIRE and two SOUND RINGS, with KAELVORN engraved on a wide banner immediately below. Centered vertical lockup. Large plain heater-shaped shield, squared shoulders and a single pointed bottom, broad dark indigo interior and tarnished-brass face, no decorative rim or surrounding frame. One thick high-contrast central basalt spire split by one wide lightning-like negative gap; upper fragment suspended slightly above lower shaft refers to Sol-Vara. Exactly two thick partial circular sound bands flank the shaft and stop before touching its silhouette. Bold spare shield outline and tower charge must read at 32 px. Single broad softly curved dark crimson cloth banner below shield, modest folded ends, sunlit brass engraved uppercase KAELVORN across its uninterrupted central face. Banner letters must stay large and straight enough to read, no swashes, no crest supporters, no crowns or extra heraldic symbols.

Use case: logo-brand. Create one square 1:1 opaque PNG logo concept, target 2048 x 2048 pixels. The icon suffix governs the emblem's medium and isolation; this request explicitly permits the KAELVORN logo and its engraved lettering, overriding the nonlinguistic constraint only for requested lettering. No text or lettering anywhere except the exact requested wordmark (and K monogram in concept C). Text verbatim: KAELVORN, eight capitals in this order K A E L V O R N. No tagline, no captions, no concept labels, no other branding. Flat uniform #0B0D12 across all unpainted background, including corners; no backdrop texture, vignette, landscape, cast shadow or glow haze. Reference image 1, art/style/candidate-a.png, is the primary style authority; reference image 2, art/style/anchor-4-icons.png, supplies isolated icon brush scale. Borrow tactile oil surfaces, decisive brass strokes, indigo fill and edge economy only; invent the requested logo rather than copying their compositions. Emblem must be a robust simple silhouette independently recognizable when cropped and reduced to 32 x 32 px: broad strokes, wide counters, no filigree, no micro ornament. Leave generous breathing room around emblem and wordmark; all shapes fully inside canvas.

No watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/redesign/logo-concepts/logo-c.png`

Attempt 1 discarded: monogram became the first letter of the wordmark, leaving only AELVORN beside it. Attempt 2 retained: separate K emblem plus correctly spelled eight-letter KAELVORN wordmark. At 32 px K silhouette and curved lower arm remain readable; the fine crack and teal rim become incidental. Weakest point: bell reference is subtle and carved surface remains busier than a truly minimal mark. Background corner sampled #0A0C11 rather than exact #0B0D12.

### Attempt 1 — discarded

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

Concept C: a MINIMAL MONOGRAM K built from a spire and a bell's curve, with refined KAELVORN wordmark beside it. Horizontal lockup centered within the square: compact K emblem on left, wordmark on right, entire lockup spans 86 percent canvas width with generous dark space above and below. Emblem occupies roughly one quarter of lockup width, strong upright bronze spire forms K's vertical stem; a single sweeping flared bell curve and one decisive diagonal form the two K arms with broad open negative counters. It MUST unmistakably read as the letter K at 32 px. One small clean notch in stem recalls the First Spire's fracture, no illustrative tower windows. Controlled flat broad brass masses with only a few impasto highlights and a thin selective viridian edge. Refined carved and engraved tarnished-brass Roman wedge-serif uppercase KAELVORN beside emblem, carefully spaced wide capitals, single straight baseline; visually lighter than concept A, restrained proportions, no swashes or flourishes. Keep the K independent and separable from wordmark.

Use case: logo-brand. Create one square 1:1 opaque PNG logo concept, target 2048 x 2048 pixels. The icon suffix governs the emblem's medium and isolation; this request explicitly permits the KAELVORN logo and its engraved lettering, overriding the nonlinguistic constraint only for requested lettering. No text or lettering anywhere except the exact requested wordmark (and K monogram in concept C). Text verbatim: KAELVORN, eight capitals in this order K A E L V O R N. No tagline, no captions, no concept labels, no other branding. Flat uniform #0B0D12 across all unpainted background, including corners; no backdrop texture, vignette, landscape, cast shadow or glow haze. Reference image 1, art/style/candidate-a.png, is the primary style authority; reference image 2, art/style/anchor-4-icons.png, supplies isolated icon brush scale. Borrow tactile oil surfaces, decisive brass strokes, indigo fill and edge economy only; invent the requested logo rather than copying their compositions. Emblem must be a robust simple silhouette independently recognizable when cropped and reduced to 32 x 32 px: broad strokes, wide counters, no filigree, no micro ornament. Leave generous breathing room around emblem and wordmark; all shapes fully inside canvas.

No watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Attempt 2 — retained

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

Concept C: a MINIMAL MONOGRAM K built from a spire and a bell's curve, with refined KAELVORN wordmark beside it. Horizontal lockup centered within the square: compact K emblem on left, wordmark on right, entire lockup spans 86 percent canvas width with generous dark space above and below. Emblem occupies roughly one quarter of lockup width, strong upright bronze spire forms K's vertical stem; a single sweeping flared bell curve and one decisive diagonal form the two K arms with broad open negative counters. It MUST unmistakably read as the letter K at 32 px. One small clean notch in stem recalls the First Spire's fracture, no illustrative tower windows. Controlled flat broad brass masses with only a few impasto highlights and a thin selective viridian edge. Refined carved and engraved tarnished-brass Roman wedge-serif uppercase KAELVORN beside emblem, carefully spaced wide capitals, single straight baseline; visually lighter than concept A, restrained proportions, no swashes or flourishes. Keep the K independent and separable from wordmark.

Use case: logo-brand. Create one square 1:1 opaque PNG logo concept, target 2048 x 2048 pixels. The icon suffix governs the emblem's medium and isolation; this request explicitly permits the KAELVORN logo and its engraved lettering, overriding the nonlinguistic constraint only for requested lettering. No text or lettering anywhere except the exact requested wordmark (and K monogram in concept C). Text verbatim: KAELVORN, eight capitals in this order K A E L V O R N. No tagline, no captions, no concept labels, no other branding. Flat uniform #0B0D12 across all unpainted background, including corners; no backdrop texture, vignette, landscape, cast shadow or glow haze. Reference image 1, art/style/candidate-a.png, is the primary style authority; reference image 2, art/style/anchor-4-icons.png, supplies isolated icon brush scale. Borrow tactile oil surfaces, decisive brass strokes, indigo fill and edge economy only; invent the requested logo rather than copying their compositions. Emblem must be a robust simple silhouette independently recognizable when cropped and reduced to 32 x 32 px: broad strokes, wide counters, no filigree, no micro ornament. Leave generous breathing room around emblem and wordmark; all shapes fully inside canvas.

Targeted remake: the previous attempt incorrectly used the monogram as the first letter of the wordmark. Draw TWO DISTINCT elements, first a small K emblem, then a full wordmark KAELVORN with its own initial K. Leave a very clear empty gap at least the width of the wordmark's letter K between emblem and full wordmark. The complete logo therefore contains a standalone K followed by KAELVORN; nine visible letterforms in total. Emblem must not touch or overlap any wordmark letter. Make emblem simpler and more compact, three thick strokes only, no oversized sweeping tail. Ensure all eight letters K A E L V O R N appear together on the right. All empty background pixels flat #0B0D12, no vignette.

No watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## `art/ui/icons/` — painted interface icons

- Tool: `gemini-api image`; default model `gemini-nano-banana-2.1`.
- References, in supplied order: `art/style/candidate-a.png`, `art/style/anchor-4-icons.png`.
- Requested: two 3 × 2 landscape sheets, 2K, chroma green. Actual generated sheets: **2528 × 1696 px**, JPEG returned by the model despite PNG output names; losslessly decoded and saved as PNG before keying.
- Calls: 4 CLI invocations; 3 generated images and 1 request failed validation before generation because this model only supports JPEG response MIME. Sheet 2 received one generated remake.
- Processing: `art/ui/tools/key.py` converts distance from `#00FF00` to alpha and reverses green compositing on soft edges. `art/ui/tools/cut_icons.py` crops equal cells, exports twelve 512 × 512 RGBA PNGs, and builds the dark/light contact sheet at 32, 48 and 96 px.
- Review: retained sheet 1 and remade sheet 2 have no text, painted substrate, green fringe or clipped retained silhouettes. All twelve are readable at 32 px on both test backgrounds. `skill-trees.png` is weakest because its fine outer branches compress at 32 px.

### Sheet 1 — retained

Command:

```sh
gemini-api image '<prompt below>' -i art/style/candidate-a.png -i art/style/anchor-4-icons.png --aspect-ratio 3:2 --image-size 2K --out art/ui/raw/ui-icons/sheet-1.png
```

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

Paint one clean production sheet of exactly six frameless interface icons arranged in THREE COLUMNS by TWO ROWS, row-major order, one isolated object per equal square cell. Row 1: a hearth lantern for Home; a compass rose over a small torn map fragment for World; one crossed sword and one arcane staff for Callings. Row 2: a simple branching rune tree for Skills; an anvil with one hammer for Crafting; a dark dungeon gate with one torch for Adventures. Every object is centred, complete, and fills 65–72% of its imaginary square cell, with very wide empty gutters and no overlap. Preserve simple silhouettes and oversized defining features so each reads at 32 pixels. Brass and indigo masses with restrained teal accents; no tiny decoration. The entire background and every gutter must be one perfectly flat, uniform, textureless chroma green #00FF00 extending behind and around all objects. The chroma green substrate explicitly replaces the usual #0B0D12 substrate and the usual outer vignette for this production keying sheet. No shadows, paint flecks, glow, haze, canvas tooth, grid lines, dividers, labels, frames, or marks may touch the green outside each object. Borrow only surface, stroke scale, edge economy, palette and lighting from the supplied style references; invent these six requested subjects. Generate one PNG, exact landscape 3:2, 2K.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Sheet 2 attempt 1 — discarded

Discarded because the third More orb crossed the cell boundary into Close, and the News scroll crossed into Launch.

Command:

```sh
gemini-api image '<prompt below>' -i art/style/candidate-a.png -i art/style/anchor-4-icons.png --aspect-ratio 3:2 --image-size 2K --out art/ui/raw/ui-icons/sheet-2.png
```

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

Paint one clean production sheet of exactly six frameless interface icons arranged in THREE COLUMNS by TWO ROWS, row-major order, one isolated object per equal square cell. Row 1: a plain painter frame with one diagonal brush for Gallery; a sealed rolled scroll for News; an hourglass with clearly visible golden sand for Launch. Row 2: exactly three separate round brass orbs in one horizontal row for More; exactly two plain crossed brass rods forming an X for Close; exactly three separate thick stacked horizontal brass bars for Menu. Every object is centred, complete, and fills 65–72% of its imaginary square cell, with very wide empty gutters and no overlap. Preserve extremely simple silhouettes and oversized defining features so each reads at 32 pixels. Brass and indigo masses with restrained teal accents; no tiny decoration. The entire background and every gutter must be one perfectly flat, uniform, textureless chroma green #00FF00 extending behind and around all objects. The chroma green substrate explicitly replaces the usual #0B0D12 substrate and the usual outer vignette for this production keying sheet. No shadows, paint flecks, glow, haze, canvas tooth, grid lines, dividers, labels, frames other than the single Gallery object, or marks may touch the green outside each object. Borrow only surface, stroke scale, edge economy, palette and lighting from the supplied style references; invent these six requested subjects. Generate one PNG, exact landscape 3:2, 2K.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Sheet 2 attempt 2 — retained

The first command below failed request validation before generation because `gemini-nano-banana-2.1` rejected `image/png`; the second submitted the same prompt successfully. Retained: all subjects are complete inside wide gutters and no cell contamination remains.

Commands:

```sh
gemini-api image '<prompt below>' -i art/style/candidate-a.png -i art/style/anchor-4-icons.png --aspect-ratio 3:2 --image-size 2K --output-mime-type image/png --out art/ui/raw/ui-icons/sheet-2.png
gemini-api image '<prompt below>' -i art/style/candidate-a.png -i art/style/anchor-4-icons.png --aspect-ratio 3:2 --image-size 2K --out art/ui/raw/ui-icons/sheet-2-remake.png
```

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Skill icon: a single object or nonlinguistic symbol, frameless, centred, orthographic macro close-up, hard-edged impasto, three bold value masses, 70–80% cell fill, readable at 48 px, flat #0B0D12 background and gutters replace the canvas texture and vignette outside the painted subject, square 1:1.

REMAKE one clean production sheet of exactly six frameless interface icons arranged in THREE COLUMNS by TWO ROWS, row-major order, one isolated object per equal square cell. Row 1: a plain painter frame with one diagonal brush for Gallery; a sealed rolled scroll for News; an hourglass with clearly visible golden sand for Launch. Row 2: exactly three separate round brass orbs in one horizontal row for More; exactly two plain crossed brass rods forming an X for Close; exactly three separate thick stacked horizontal brass bars for Menu. Every complete subject, including all three orbs and every brush tip, scroll end, hourglass flourish, rod end and bar end, must remain inside the CENTRAL 55% of its own imaginary square cell. Leave at least 20% of every cell empty on all four sides. Nothing may cross an imaginary cell boundary or be clipped. Make the three More orbs smaller and tightly grouped around the centre of their own bottom-left cell. Use very wide, perfectly empty chroma-green gutters. Preserve extremely simple silhouettes and oversized defining features so each reads at 32 pixels. Brass and indigo masses with restrained teal accents; no tiny decoration. The entire background and every gutter must be one perfectly flat, uniform, textureless chroma green #00FF00 extending behind and around all objects. The chroma green substrate explicitly replaces the usual #0B0D12 substrate and the usual outer vignette for this production keying sheet. No shadows, paint flecks, glow, haze, canvas tooth, grid lines, dividers, labels, frames other than the single Gallery object, or marks may touch the green outside each object. Borrow only surface, stroke scale, edge economy, palette and lighting from the supplied style references; invent these six requested subjects. Generate one PNG, exact landscape 3:2, 2K.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

## 2026-10-26 — CSS brush masks (`cursor-8`, unit `masks`)

Reference for every invocation: `art/style/candidate-a.png`. Model default: `gemini-nano-banana-2.1`. Requested size: 2K. The CLI returned JPEG data despite `.png` output names; raw files were losslessly decoded and saved as PNG before keying.

### `mask-16x9.png` — retained first generation

Command: `gemini-api image '<prompt below>' -i art/style/candidate-a.png --aspect-ratio 16:9 --image-size 2K --out art/ui/raw/masks/mask-16x9.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Technical CSS mask source, landscape 16:9. On a perfectly flat solid chroma-green #00FF00 background, paint one single solid pure-white #FFFFFF rectangular matte filling almost the whole canvas. Every side must be an irregular bold oil-brush edge, with dry-bristle notches, broken tufts and lost edges extending 3 to 6 percent inward; no side may be geometrically straight. Interior is uninterrupted opaque white. Only white paint and green background, no scene, objects, shadows, texture in the interior, border, lettering, or other colours. Keep the white shape connected and reaching close to all four sides while retaining visible green around its rough perimeter.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

Actual raw dimensions: 2752 × 1536. Review: retained; all four edges are irregular, connected interior, no text or painted background.

### `mask-2x3.png` — retained first generation

Command: `gemini-api image '<prompt below>' -i art/style/candidate-a.png --aspect-ratio 2:3 --image-size 2K --out art/ui/raw/masks/mask-2x3.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Technical CSS mask source, portrait 2:3. On a perfectly flat solid chroma-green #00FF00 background, paint one single solid pure-white #FFFFFF rectangular matte filling almost the whole canvas. Every side must be an irregular bold oil-brush edge, with dry-bristle notches, broken tufts and lost edges extending 3 to 6 percent inward; no side may be geometrically straight. Interior is uninterrupted opaque white. Only white paint and green background, no scene, objects, shadows, texture in the interior, border, lettering, or other colours. Keep the white shape connected and reaching close to all four sides while retaining visible green around its rough perimeter.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

Actual raw dimensions: 1696 × 2528. Review: retained; restrained edge depth suits character cards and the silhouette remains connected.

### `mask-3x2.png` — retained first generation

Command: `gemini-api image '<prompt below>' -i art/style/candidate-a.png --aspect-ratio 3:2 --image-size 2K --out art/ui/raw/masks/mask-3x2.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Technical CSS mask source, landscape 3:2. On a perfectly flat solid chroma-green #00FF00 background, paint one single solid pure-white #FFFFFF rectangular matte filling almost the whole canvas. Every side must be an irregular bold oil-brush edge, with dry-bristle notches, broken tufts and lost edges extending 3 to 6 percent inward; no side may be geometrically straight. Interior is uninterrupted opaque white. Only white paint and green background, no scene, objects, shadows, texture in the interior, border, lettering, or other colours. Keep the white shape connected and reaching close to all four sides while retaining visible green around its rough perimeter.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

Actual raw dimensions: 2528 × 1696. Review: retained; strongest dry-brush underside among the rectangular masks.

### `mask-1x1.png` — retained first generation

Command: `gemini-api image '<prompt below>' -i art/style/candidate-a.png --aspect-ratio 1:1 --image-size 2K --out art/ui/raw/masks/mask-1x1.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Technical CSS mask source, square 1:1. On a perfectly flat solid chroma-green #00FF00 background, paint one single solid pure-white #FFFFFF rectangular matte filling almost the whole canvas. Every side must be an irregular bold oil-brush edge, with dry-bristle notches, broken tufts and lost edges extending 3 to 6 percent inward; no side may be geometrically straight. Interior is uninterrupted opaque white. Only white paint and green background, no scene, objects, shadows, texture in the interior, border, lettering, or other colours. Keep the white shape connected and reaching close to all four sides while retaining visible green around its rough perimeter.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

Actual raw dimensions: 2048 × 2048. Review: retained; most expressive contour, but edge depth is somewhat stronger than the requested range.

### Initial 5:1 banner/divider invocations — rejected before generation

The CLI rejected `--aspect-ratio 5:1` as unsupported before sending an image-generation request. These were CLI invocations but not billable image generations:

- `gemini-api image '<fixed prefix + mask-banner subject below + fixed avoid list>' -i art/style/candidate-a.png --aspect-ratio 5:1 --image-size 2K --out art/ui/raw/masks/mask-banner.png`
- `gemini-api image '<fixed prefix + stroke-divider-1 subject below + fixed avoid list>' -i art/style/candidate-a.png --aspect-ratio 5:1 --image-size 2K --out art/ui/raw/masks/stroke-divider-1.png`
- `gemini-api image '<fixed prefix + stroke-divider-2 subject below + fixed avoid list>' -i art/style/candidate-a.png --aspect-ratio 5:1 --image-size 2K --out art/ui/raw/masks/stroke-divider-2.png`

The exact three submitted prompts were identical to the successful prompts below except that each subject began `Technical CSS mask source, ultra-wide 5:1` (and the banner continued `banner.`). No model output or dimensions resulted.

### `mask-banner.png` — retained first successful generation

Command: `gemini-api image '<prompt below>' -i art/style/candidate-a.png --aspect-ratio 4:1 --image-size 2K --out art/ui/raw/masks/mask-banner.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Technical CSS mask source, ultra-wide banner. On a perfectly flat solid chroma-green #00FF00 background, paint one single solid pure-white #FFFFFF wide banner matte filling almost the whole canvas. Left, top, and right edges are subtly uneven oil-brush edges; the bottom edge is strongly irregular with dry-bristle notches, broken tufts, dragged paint and lost edges extending 3 to 6 percent inward. No edge may be geometrically straight. Interior is uninterrupted opaque white. Only white paint and green background, no scene, objects, shadows, interior texture, border, lettering, or other colours. Keep the white shape connected while retaining visible green around its perimeter.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

Actual raw dimensions: 4128 × 1024. Review: retained; clean mostly-bottom brush treatment and quiet top edge. Native 4:1 is the closest supported ratio to the requested “about 5:1”.

### `stroke-divider-1.png` — retained first successful generation

Command: `gemini-api image '<prompt below>' -i art/style/candidate-a.png --aspect-ratio 4:1 --image-size 2K --out art/ui/raw/masks/stroke-divider-1.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Technical CSS mask source, ultra-wide. On a perfectly flat solid chroma-green #00FF00 background, paint exactly one pure-white #FFFFFF horizontal divider stroke across about 90 percent of the width, centred vertically. One confident flat-bristle pull, medium thickness, slightly rising from left to right, with a loaded blunt start, irregular impasto body, dry-brush gaps and several fine separated bristle trails at the finish. The stroke must remain one readable connected gesture. Only white paint and green background, no scene, second stroke, shadows, lettering, or other colours.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

Actual raw dimensions: 4128 × 1024. Review: retained; strong loaded start and long dry-bristle breakup.

### `stroke-divider-2.png` — retained first successful generation

Command: `gemini-api image '<prompt below>' -i art/style/candidate-a.png --aspect-ratio 4:1 --image-size 2K --out art/ui/raw/masks/stroke-divider-2.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Technical CSS mask source, ultra-wide. On a perfectly flat solid chroma-green #00FF00 background, paint exactly one pure-white #FFFFFF horizontal divider stroke across about 88 percent of the width, centred vertically. One vigorous dry flat-bristle pull, medium-thin and gently bowed downward, with a tapered broken start, dense central knife-mark, uneven feathered underside and sparse separated bristle trails at both ends. Distinct from a straight line and from a calligraphic flourish; one readable connected gesture. Only white paint and green background, no scene, second stroke, shadows, lettering, or other colours.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

Actual raw dimensions: 4128 × 1024. Review: retained; distinct bowed, lighter gesture with clean keyed separation.

Seven billable image generations; ten `gemini-api image` CLI invocations including three pre-generation aspect-ratio validation failures. All retained outputs passed dark/light contact-sheet review with no green fringe, text, painted background or broken silhouette.

---

# Logo final production assets

Date: 2026-10-26. Reference for every generation: `art/redesign/logo-concepts/logo-b.png`. Four paid `gemini-api image` calls total: three initial assets and one targeted horizontal remake. The CLI returned JPEG source files despite requested `.png` output names; these are retained in `art/brand/raw/`. Production files were chroma-keyed to transparent PNG with `art/brand/tools/key.py`.

## Full lockup — attempt 1 retained

Prompt, verbatim:

```text
Using the supplied concept as the strict identity and style reference, recreate a finished production logo lockup. Preserve the indigo heraldic shield, cracked central brass spire, paired brass sound rings, weathered oil-painted impasto, and restrained crimson banner. Shield above the banner, symmetrical, centered, complete silhouette with generous clear space. The banner must read exactly KAELVORN in large uppercase Roman serif letters, checked letter by letter: K-A-E-L-V-O-R-N. No other text. Palette: #11151E, #232B3A, #C29B61 tarnished brass, #F2C97D highlights, #A62639 crimson, tiny #38D6C4 accents. Bold clean outer contour and controlled interior texture; production logo edges, readable when reduced. Put the isolated logo on a perfectly flat, uniform chroma-key green #00FF00 background reaching every edge. Absolutely no background texture, gradient, vignette, cast shadow, green reflected light, green within the logo, watermark, border, clipping, or extra objects. Square composition, logo fills about 86 percent of canvas.
```

Command:

```sh
gemini-api image '<prompt above>' -i art/redesign/logo-concepts/logo-b.png --aspect-ratio 1:1 --image-size 2K --out art/brand/raw/logo-lockup-green.png
```

Review: retained. KAELVORN verified letter by letter. Centered complete lockup, faithful indigo/brass/crimson treatment, flat key background.

## Horizontal lockup — attempt 1 discarded

Prompt, verbatim:

```text
Using the supplied concept as the strict identity and style reference, design a production horizontal logo for a website header, approximately four times wider than tall. Place the same indigo heraldic shield with cracked central brass spire and paired brass sound rings at the left. Place the word KAELVORN to its right on one straight horizontal line, with no banner. The word must read exactly KAELVORN in uppercase Roman serif letters, checked letter by letter: K-A-E-L-V-O-R-N. No other text. Match the concept oil-painted tarnished brass, indigo, and restrained crimson details, with bold clean silhouettes and controlled impasto that remains readable at header size. Vertically center shield and wordmark, balanced spacing, complete forms, generous safe margin. Put the isolated logo on a perfectly flat, uniform chroma-key green #00FF00 background reaching every edge. Absolutely no background texture, gradient, vignette, baseline plaque, cast shadow, green reflected light, green within the logo, watermark, border, clipping, or extra objects.
```

Command:

```sh
gemini-api image '<prompt above>' -i art/redesign/logo-concepts/logo-b.png --aspect-ratio 4:1 --image-size 2K --out art/brand/raw/logo-horizontal-green.png
```

Review: discarded because an unintended painted fragment appeared in the gap between shield and K. Spelling was correct.

## Emblem — attempt 1 retained

Prompt, verbatim:

```text
Using the supplied concept as the strict identity reference, create the emblem alone as a simplified production app icon: the indigo heraldic shield, one cracked central tarnished-brass spire, and two bold paired brass sound-ring arcs. No banner, no letters, no words, no tiny decoration. Preserve the concept silhouette and oil-painted brass/indigo character but simplify into three strong value masses, thicker shapes, fewer cracks, and a clean high-contrast contour so it remains unmistakable at 32 pixels. Centered, symmetrical, front-facing, complete shield, generous safe margin. Palette limited to #232B3A indigo, #C29B61 tarnished brass, #F2C97D sparse highlight, #11151E crevices; no green or teal in the emblem. Put the isolated emblem on a perfectly flat, uniform chroma-key green #00FF00 background reaching every edge. Absolutely no background texture, gradient, vignette, cast shadow, green reflected light, watermark, border, clipping, or extra objects.
```

Command:

```sh
gemini-api image '<prompt above>' -i art/redesign/logo-concepts/logo-b.png --aspect-ratio 1:1 --image-size 2K --out art/brand/raw/emblem-green.png
```

Review: retained. Shield, split spire, and paired rings remain distinct at 32 px. No lettering or banner.

## Horizontal lockup — attempt 2 retained

Prompt, verbatim:

```text
Targeted remake using the supplied concept as strict identity and style reference. Create a clean production horizontal website-header logo, approximately four times wider than tall. At left: the complete indigo heraldic shield with cracked central tarnished-brass spire and paired brass sound rings. At right: KAELVORN on one straight line in uppercase Roman serif letters, checked letter by letter K-A-E-L-V-O-R-N. No banner and no other text. Preserve oil-painted brass and indigo, but use a crisp clean silhouette and controlled detail. IMPORTANT: leave a completely empty, even gap of flat green between shield and the K; no stray paint, no rocks, no pedestal, no fragments, no decorative flourish, no shadow. Vertically center both elements with generous outer safe margins. Put the isolated logo on perfectly flat uniform chroma-key green #00FF00 reaching every edge. No background texture, gradient, vignette, cast shadow, green reflected light, green inside the logo, watermark, border, clipping, or extra objects.
```

Command:

```sh
gemini-api image '<prompt above>' -i art/redesign/logo-concepts/logo-b.png --aspect-ratio 4:1 --image-size 2K --out art/brand/raw/logo-horizontal-green-v2.png
```

Review: retained. KAELVORN verified letter by letter. A tiny disconnected paint fleck remained in the empty gap and was cleared after keying; no generated identity pixels were altered.

## Production commands

```sh
python3 art/brand/tools/key.py art/brand/raw/logo-lockup-green.jpg art/brand/logo-lockup.png
python3 art/brand/tools/key.py art/brand/raw/logo-horizontal-green-v2.jpg art/brand/logo-horizontal.png --clear 1080,560,1280,760
python3 art/brand/tools/key.py art/brand/raw/emblem-green.jpg art/brand/emblem.png
python3 art/brand/tools/build.py
```

Review: transparent edges checked on `#11151E` and `#EFE3C6` in `art/brand/contact-sheet.png`. No visible green fringe. Favicons use Lanczos resampling; the 32 px file receives a light hand-tuned unsharp pass.

## Navigation redesign — 2026-10-26

Built-in image_gen, one call per asset. Style references: `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`, `art/style/anchor-2-hero.png`, `art/style/anchor-3-creature.png`, `art/style/anchor-4-icons.png`, `art/gallery/concept-home.png`. The tool accepts at most five local references: the actual generation calls pass candidate-a and all four anchors. concept-home is the supplied conversation look reference, not a sixth tool path. Six initial calls with six paths were rejected before generation; submitted prompt wording was unchanged on retry. All are style references, not edit targets. The user explicitly requested carved KAELVORN and indicative labels, crown moulding and hanging banners; those specific requests override the generic lettering and architectural ornament restrictions. Mobile portrait overrides the suffix aspect ratio. All six complete submitted prompts follow.

### Navigation concept a-desktop — attempt 1

Output: `art/redesign/nav/concept-a-desktop.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

These are navigation build-reference concepts for the Kaelvorn MMORPG website. User-requested exceptions to the generic no-text/no-logo rule: a painted anonymous emblem placeholder with KAELVORN in carved capitals, plus clear indicative destination labels, which the builder will replace with live HTML text. Avoid other copy. There are exactly nine destinations, each once: Home, World, Callings, Skill Trees, Crafting, Adventures, Gallery, News, Launch. Adventures contains Dungeons, Raids, Bestiary. Match the attached gallery's high-end in-game interface character; this is a website screenshot, no device bezel, no perspective. Hero beneath the header is an oil-painted golden limestone gorge, distant citadel and a small adventuring party, subordinate to the navigation. Borrow surface, stroke scale, edge economy, palette and lighting from references, invent layout. Reference roles: candidate-a is primary paint authority, anchor-1-vista supplies landscape atmosphere, anchor-2-hero character planes/materials, anchor-3-creature stone/glow, anchor-4-icons supplies the frameless impasto icon style, concept-home supplies website visual continuity. Keep generous quiet dark zones behind live labels. Crown moulding and brass rails are functional header architecture, never decorative picture frames or bevelled icon slots.

Concept A, CARVED CROWN BANNER. Desktop home page top, landscape 16:9, target 2048 x 1152. Top 13%: centered anonymous brass sun-shield emblem beside KAELVORN wordmark on broad carved indigo stone lintel. Next 17%: one continuous dark stone banner bar with shallow crown moulding and thin worn brass lip; exactly nine equally spaced frameless painted icons ABOVE generous cream destination labels in the listed order. Icons: sun, compass, helmet, branching tree, hammer, crossed swords, painted landscape, scroll, bell. Active Home has a restrained crimson cloth tab behind its icon and a small brass underline, no separate tile frames. Bottom 70% hero art with quiet left area reserved for future headline. Navigation must dominate and be large enough for a builder to measure spacing.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Navigation concept a-mobile — attempt 1

Output: `art/redesign/nav/concept-a-mobile.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

These are navigation build-reference concepts for the Kaelvorn MMORPG website. User-requested exceptions to the generic no-text/no-logo rule: a painted anonymous emblem placeholder with KAELVORN in carved capitals, plus clear indicative destination labels, which the builder will replace with live HTML text. Avoid other copy. There are exactly nine destinations, each once: Home, World, Callings, Skill Trees, Crafting, Adventures, Gallery, News, Launch. Adventures contains Dungeons, Raids, Bestiary. Match the attached gallery's high-end in-game interface character; this is a website screenshot, no device bezel, no perspective. Hero beneath the header is an oil-painted golden limestone gorge, distant citadel and a small adventuring party, subordinate to the navigation. Borrow surface, stroke scale, edge economy, palette and lighting from references, invent layout. Reference roles: candidate-a is primary paint authority, anchor-1-vista supplies landscape atmosphere, anchor-2-hero character planes/materials, anchor-3-creature stone/glow, anchor-4-icons supplies the frameless impasto icon style, concept-home supplies website visual continuity. Keep generous quiet dark zones behind live labels. Crown moulding and brass rails are functional header architecture, never decorative picture frames or bevelled icon slots.

Concept A, CARVED CROWN BANNER adapted to phone, portrait 2:3, target 1024 x 1536; this portrait specification overrides landscape in the fixed category suffix. Same stone lintel, shallow crown moulding and worn brass lip as desktop. Top 14%: emblem and KAELVORN at left, clear close X at right. Expanded navigation occupies next 54% on a continuous indigo stone panel: exactly THREE COLUMNS by THREE ROWS, icons above labels, in row-major order Home, World, Callings / Skill Trees, Crafting, Adventures / Gallery, News, Launch. Wide touch targets, visible gutters, no tiny nine-across strip, no icon frames. Active Home has crimson cloth backing and brass underline. Bottom 32% shows the top of the same hero, a golden gorge and distant citadel. Keep all nine names readable and distinct.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Navigation concept b-desktop — attempt 1

Output: `art/redesign/nav/concept-b-desktop.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

These are navigation build-reference concepts for the Kaelvorn MMORPG website. User-requested exceptions to the generic no-text/no-logo rule: a painted anonymous emblem placeholder with KAELVORN in carved capitals, plus clear indicative destination labels, which the builder will replace with live HTML text. Avoid other copy. There are exactly nine destinations, each once: Home, World, Callings, Skill Trees, Crafting, Adventures, Gallery, News, Launch. Adventures contains Dungeons, Raids, Bestiary. Match the attached gallery's high-end in-game interface character; this is a website screenshot, no device bezel, no perspective. Hero beneath the header is an oil-painted golden limestone gorge, distant citadel and a small adventuring party, subordinate to the navigation. Borrow surface, stroke scale, edge economy, palette and lighting from references, invent layout. Reference roles: candidate-a is primary paint authority, anchor-1-vista supplies landscape atmosphere, anchor-2-hero character planes/materials, anchor-3-creature stone/glow, anchor-4-icons supplies the frameless impasto icon style, concept-home supplies website visual continuity. Keep generous quiet dark zones behind live labels. Crown moulding and brass rails are functional header architecture, never decorative picture frames or bevelled icon slots.

Concept B, HANGING GUILD BANNERS. Desktop home page top, landscape 16:9, target 2048 x 1152. A narrow dark timber-and-brass crossbeam at top carries anonymous sun-shield emblem and KAELVORN at left. Below hangs a continuous row of nine broad short fabric pennants, alternating indigo resting cloth and subtle umber, secured to the crossbeam by simple brass rings, with painted small symbols and generous cream labels in listed order. Home pennant crimson and pointed; other pennants subtly split-tailed, no stone tile grid. Adventures is open: a wide dark cloth dropdown hangs directly beneath its pennant over the top of hero art, three large horizontal selectable rows named Dungeons, Raids, Bestiary with small painted dungeon gate, swords, creature icons and quiet label zones. A small downward caret marks Adventures. Gallery, News and Launch remain visible to its right. Hero art begins behind the hanging menu and fills lower two-thirds. Strong textile silhouette, spare architecture.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Navigation concept b-mobile — attempt 1

Output: `art/redesign/nav/concept-b-mobile.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

These are navigation build-reference concepts for the Kaelvorn MMORPG website. User-requested exceptions to the generic no-text/no-logo rule: a painted anonymous emblem placeholder with KAELVORN in carved capitals, plus clear indicative destination labels, which the builder will replace with live HTML text. Avoid other copy. There are exactly nine destinations, each once: Home, World, Callings, Skill Trees, Crafting, Adventures, Gallery, News, Launch. Adventures contains Dungeons, Raids, Bestiary. Match the attached gallery's high-end in-game interface character; this is a website screenshot, no device bezel, no perspective. Hero beneath the header is an oil-painted golden limestone gorge, distant citadel and a small adventuring party, subordinate to the navigation. Borrow surface, stroke scale, edge economy, palette and lighting from references, invent layout. Reference roles: candidate-a is primary paint authority, anchor-1-vista supplies landscape atmosphere, anchor-2-hero character planes/materials, anchor-3-creature stone/glow, anchor-4-icons supplies the frameless impasto icon style, concept-home supplies website visual continuity. Keep generous quiet dark zones behind live labels. Crown moulding and brass rails are functional header architecture, never decorative picture frames or bevelled icon slots.

Concept B, HANGING GUILD BANNERS adapted to phone, portrait 2:3, target 1024 x 1536; this portrait specification overrides landscape in fixed category suffix. Compact brass crossbeam with anonymous emblem, KAELVORN and clear close X. Menu OPEN: one broad indigo hanging guild banner beneath crossbeam covers about 80% width, ending in two fabric tails above a small visible golden hero landscape strip. One vertical column of generous touch rows for all nine destinations in listed order, small painted icon LEFT of every label. Home has crimson cloth active highlight. Adventures row expanded inline, showing three slightly indented smaller rows Dungeons, Raids, Bestiary, then Gallery, News, Launch below. Use enough vertical space to fit every row without clipping; do not duplicate a desktop nine-across strip. Shallow fabric folds and subtle stitched divisions, no frames. This is the same cloth-menu concept as desktop, not a stone grid.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Navigation concept c-desktop — attempt 1

Output: `art/redesign/nav/concept-c-desktop.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

These are navigation build-reference concepts for the Kaelvorn MMORPG website. User-requested exceptions to the generic no-text/no-logo rule: a painted anonymous emblem placeholder with KAELVORN in carved capitals, plus clear indicative destination labels, which the builder will replace with live HTML text. Avoid other copy. There are exactly nine destinations, each once: Home, World, Callings, Skill Trees, Crafting, Adventures, Gallery, News, Launch. Adventures contains Dungeons, Raids, Bestiary. Match the attached gallery's high-end in-game interface character; this is a website screenshot, no device bezel, no perspective. Hero beneath the header is an oil-painted golden limestone gorge, distant citadel and a small adventuring party, subordinate to the navigation. Borrow surface, stroke scale, edge economy, palette and lighting from references, invent layout. Reference roles: candidate-a is primary paint authority, anchor-1-vista supplies landscape atmosphere, anchor-2-hero character planes/materials, anchor-3-creature stone/glow, anchor-4-icons supplies the frameless impasto icon style, concept-home supplies website visual continuity. Keep generous quiet dark zones behind live labels. Crown moulding and brass rails are functional header architecture, never decorative picture frames or bevelled icon slots.

Concept C, CENTRAL SEAL HUD. Desktop home page top, landscape 16:9, target 2048 x 1152. Radically slim game HUD taking only upper 17% of image. Small centered KAELVORN wordmark in top strip above a large anonymous brass-and-viridian compass seal that projects slightly below a thin straight indigo-steel HUD rail. FOUR text-led destinations LEFT of seal: Home, World, Callings, Skill Trees. FIVE destinations RIGHT of seal: Crafting, Adventures, Gallery, News, Launch. Tiny restrained painted pictograms adjacent to labels, never large icon tiles. Launch at far right has a compact countdown capsule directly beneath it with indicative 12d 08h 34m, integrated into bar. All nine labels fit with generous gaps, no duplicate links, no second navigation row. Active Home thin ochre notch. Header is a low-profile instrument panel with fine brass ticks, no crown moulding, no hanging cloth. Remaining 83% is expansive golden gorge hero, quiet left sky for future live headline.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Navigation concept c-mobile — attempt 1

Output: `art/redesign/nav/concept-c-mobile.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

These are navigation build-reference concepts for the Kaelvorn MMORPG website. User-requested exceptions to the generic no-text/no-logo rule: a painted anonymous emblem placeholder with KAELVORN in carved capitals, plus clear indicative destination labels, which the builder will replace with live HTML text. Avoid other copy. There are exactly nine destinations, each once: Home, World, Callings, Skill Trees, Crafting, Adventures, Gallery, News, Launch. Adventures contains Dungeons, Raids, Bestiary. Match the attached gallery's high-end in-game interface character; this is a website screenshot, no device bezel, no perspective. Hero beneath the header is an oil-painted golden limestone gorge, distant citadel and a small adventuring party, subordinate to the navigation. Borrow surface, stroke scale, edge economy, palette and lighting from references, invent layout. Reference roles: candidate-a is primary paint authority, anchor-1-vista supplies landscape atmosphere, anchor-2-hero character planes/materials, anchor-3-creature stone/glow, anchor-4-icons supplies the frameless impasto icon style, concept-home supplies website visual continuity. Keep generous quiet dark zones behind live labels. Crown moulding and brass rails are functional header architecture, never decorative picture frames or bevelled icon slots.

Concept C, CENTRAL SEAL HUD adapted to phone, portrait 2:3, target 1024 x 1536; this portrait specification overrides landscape in fixed category suffix. Slim steel HUD rail at top with small KAELVORN wordmark, centered projecting brass/viridian compass seal below it, menu close X at right. A narrow countdown ribbon immediately below rail reads Launch — 12d 08h 34m. Expanded instrument-panel navigation beneath this is a dark translucent indigo overlay with two columns of wide text-led touch targets and tiny painted symbols: left column Home, World, Callings, Skill Trees; right column Crafting, Adventures, Gallery, News. Launch is the ninth destination already in countdown ribbon, do not repeat it. Active Home a tiny ochre notch and quiet teal stroke. No bottom action bar, no crown moulding or hanging cloth. Overlay ends near half screen, leaving lower half golden gorge hero visible. Clear symmetric geometry, restrained thin brass instrument ticks, ample readable label spacing. Every target is wide and practical for a phone.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Navigation first-pass review

A desktop retained: all nine labels, carved wordmark, continuous icon banner and hero read clearly. A mobile omitted lettering. B desktop omitted lettering; B mobile ignored portrait and returned a desktop-like strip. C desktop and mobile omitted labels and wordmark; HUD architecture reads clearly. Five targeted remakes follow. Remake reference 1 is the corresponding first-pass image (B mobile instead uses B desktop as architectural reference); remaining references are candidate-a and anchor-4-icons. Originals retained by the tool; rejected attempts are not project deliverables.

### Navigation concept a-mobile — attempt 2

Output: `art/redesign/nav/concept-a-mobile.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

These are navigation build-reference concepts for the Kaelvorn MMORPG website. User-requested exceptions to the generic no-text/no-logo rule: a painted anonymous emblem placeholder with KAELVORN in carved capitals, plus clear indicative destination labels, which the builder will replace with live HTML text. Avoid other copy. There are exactly nine destinations, each once: Home, World, Callings, Skill Trees, Crafting, Adventures, Gallery, News, Launch. Adventures contains Dungeons, Raids, Bestiary. Match the attached gallery's high-end in-game interface character; this is a website screenshot, no device bezel, no perspective. Hero beneath the header is an oil-painted golden limestone gorge, distant citadel and a small adventuring party, subordinate to the navigation. Borrow surface, stroke scale, edge economy, palette and lighting from references, invent layout. Reference roles: candidate-a is primary paint authority, anchor-1-vista supplies landscape atmosphere, anchor-2-hero character planes/materials, anchor-3-creature stone/glow, anchor-4-icons supplies the frameless impasto icon style, concept-home supplies website visual continuity. Keep generous quiet dark zones behind live labels. Crown moulding and brass rails are functional header architecture, never decorative picture frames or bevelled icon slots.

Concept A, CARVED CROWN BANNER adapted to phone, portrait 2:3, target 1024 x 1536; this portrait specification overrides landscape in the fixed category suffix. Same stone lintel, shallow crown moulding and worn brass lip as desktop. Top 14%: emblem and KAELVORN at left, clear close X at right. Expanded navigation occupies next 54% on a continuous indigo stone panel: exactly THREE COLUMNS by THREE ROWS, icons above labels, in row-major order Home, World, Callings / Skill Trees, Crafting, Adventures / Gallery, News, Launch. Wide touch targets, visible gutters, no tiny nine-across strip, no icon frames. Active Home has crimson cloth backing and brass underline. Bottom 32% shows the top of the same hero, a golden gorge and distant citadel. Keep all nine names readable and distinct.

TARGETED REMAKE: preserve the continuous crown-stone header, nine-icon 3 by 3 menu and hero, but reduce each icon to leave a broad label strip beneath it. MUST visibly paint the word KAELVORN in the header. MUST render these exact cream labels in row-major order: Home | World | Callings / Skill Trees | Crafting | Adventures / Gallery | News | Launch. The previous blank label version is unusable. The task-specific requested words are exceptions to both the generic blank-text suffix and the final generic no-text rule; that final rule applies ONLY to extra lettering. Only these labels and wordmark are allowed. Portrait output exactly 1024 x 1536, do not output landscape.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Navigation concept b-desktop — attempt 2

Output: `art/redesign/nav/concept-b-desktop.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

These are navigation build-reference concepts for the Kaelvorn MMORPG website. User-requested exceptions to the generic no-text/no-logo rule: a painted anonymous emblem placeholder with KAELVORN in carved capitals, plus clear indicative destination labels, which the builder will replace with live HTML text. Avoid other copy. There are exactly nine destinations, each once: Home, World, Callings, Skill Trees, Crafting, Adventures, Gallery, News, Launch. Adventures contains Dungeons, Raids, Bestiary. Match the attached gallery's high-end in-game interface character; this is a website screenshot, no device bezel, no perspective. Hero beneath the header is an oil-painted golden limestone gorge, distant citadel and a small adventuring party, subordinate to the navigation. Borrow surface, stroke scale, edge economy, palette and lighting from references, invent layout. Reference roles: candidate-a is primary paint authority, anchor-1-vista supplies landscape atmosphere, anchor-2-hero character planes/materials, anchor-3-creature stone/glow, anchor-4-icons supplies the frameless impasto icon style, concept-home supplies website visual continuity. Keep generous quiet dark zones behind live labels. Crown moulding and brass rails are functional header architecture, never decorative picture frames or bevelled icon slots.

Concept B, HANGING GUILD BANNERS. Desktop home page top, landscape 16:9, target 2048 x 1152. A narrow dark timber-and-brass crossbeam at top carries anonymous sun-shield emblem and KAELVORN at left. Below hangs a continuous row of nine broad short fabric pennants, alternating indigo resting cloth and subtle umber, secured to the crossbeam by simple brass rings, with painted small symbols and generous cream labels in listed order. Home pennant crimson and pointed; other pennants subtly split-tailed, no stone tile grid. Adventures is open: a wide dark cloth dropdown hangs directly beneath its pennant over the top of hero art, three large horizontal selectable rows named Dungeons, Raids, Bestiary with small painted dungeon gate, swords, creature icons and quiet label zones. A small downward caret marks Adventures. Gallery, News and Launch remain visible to its right. Hero art begins behind the hanging menu and fills lower two-thirds. Strong textile silhouette, spare architecture.

TARGETED REMAKE: preserve this hanging banner architecture and Adventures dropdown, add a narrow top wordmark area clearly reading KAELVORN beside emblem. Reserve cream live-text-style labels beneath the painted icon on EVERY banner: Home, World, Callings, Skill Trees, Crafting, Adventures, Gallery, News, Launch. Render exact dropdown row labels Dungeons, Raids, Bestiary beside the respective three paintings. Reduce icons if necessary so every label has space. This task-specific text is required and takes precedence over generic blank-text suffix and final no-text restriction; that restriction applies ONLY to extra lettering. Keep landscape 16:9.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Navigation concept b-mobile — attempt 2

Output: `art/redesign/nav/concept-b-mobile.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

These are navigation build-reference concepts for the Kaelvorn MMORPG website. User-requested exceptions to the generic no-text/no-logo rule: a painted anonymous emblem placeholder with KAELVORN in carved capitals, plus clear indicative destination labels, which the builder will replace with live HTML text. Avoid other copy. There are exactly nine destinations, each once: Home, World, Callings, Skill Trees, Crafting, Adventures, Gallery, News, Launch. Adventures contains Dungeons, Raids, Bestiary. Match the attached gallery's high-end in-game interface character; this is a website screenshot, no device bezel, no perspective. Hero beneath the header is an oil-painted golden limestone gorge, distant citadel and a small adventuring party, subordinate to the navigation. Borrow surface, stroke scale, edge economy, palette and lighting from references, invent layout. Reference roles: candidate-a is primary paint authority, anchor-1-vista supplies landscape atmosphere, anchor-2-hero character planes/materials, anchor-3-creature stone/glow, anchor-4-icons supplies the frameless impasto icon style, concept-home supplies website visual continuity. Keep generous quiet dark zones behind live labels. Crown moulding and brass rails are functional header architecture, never decorative picture frames or bevelled icon slots.

Concept B, HANGING GUILD BANNERS adapted to phone, portrait 2:3, target 1024 x 1536; this portrait specification overrides landscape in fixed category suffix. Compact brass crossbeam with anonymous emblem, KAELVORN and clear close X. Menu OPEN: one broad indigo hanging guild banner beneath crossbeam covers about 80% width, ending in two fabric tails above a small visible golden hero landscape strip. One vertical column of generous touch rows for all nine destinations in listed order, small painted icon LEFT of every label. Home has crimson cloth active highlight. Adventures row expanded inline, showing three slightly indented smaller rows Dungeons, Raids, Bestiary, then Gallery, News, Launch below. Use enough vertical space to fit every row without clipping; do not duplicate a desktop nine-across strip. Shallow fabric folds and subtle stitched divisions, no frames. This is the same cloth-menu concept as desktop, not a stone grid.

TARGETED REMAKE: RECOMPOSE ENTIRE MENU FOR PORTRAIT PHONE, not a desktop strip. Output exactly 1024 wide x 1536 tall, 2:3. One narrow brass crossbeam with KAELVORN at top and close X. One single broad indigo cloth hanging banner below. Stack one vertical column of nine small painted icons with clearly rendered cream labels: Home, World, Callings, Skill Trees, Crafting, Adventures, Gallery, News, Launch. Adventures expanded inline with three compact indented labels Dungeons, Raids, Bestiary. Total twelve rows, each around 70 pixels tall, header around 160 pixels, banner ends around y=1200, bottom 330 pixels reveal golden gorge hero. No horizontal navigation, no duplicate links, no large desktop hero filling page. The task-specific requested words are mandatory exceptions to generic blank-text suffix and final no-text rule; that rule applies ONLY to extra lettering. Portrait is mandatory even though the category suffix says landscape.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Navigation concept c-desktop — attempt 2

Output: `art/redesign/nav/concept-c-desktop.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

These are navigation build-reference concepts for the Kaelvorn MMORPG website. User-requested exceptions to the generic no-text/no-logo rule: a painted anonymous emblem placeholder with KAELVORN in carved capitals, plus clear indicative destination labels, which the builder will replace with live HTML text. Avoid other copy. There are exactly nine destinations, each once: Home, World, Callings, Skill Trees, Crafting, Adventures, Gallery, News, Launch. Adventures contains Dungeons, Raids, Bestiary. Match the attached gallery's high-end in-game interface character; this is a website screenshot, no device bezel, no perspective. Hero beneath the header is an oil-painted golden limestone gorge, distant citadel and a small adventuring party, subordinate to the navigation. Borrow surface, stroke scale, edge economy, palette and lighting from references, invent layout. Reference roles: candidate-a is primary paint authority, anchor-1-vista supplies landscape atmosphere, anchor-2-hero character planes/materials, anchor-3-creature stone/glow, anchor-4-icons supplies the frameless impasto icon style, concept-home supplies website visual continuity. Keep generous quiet dark zones behind live labels. Crown moulding and brass rails are functional header architecture, never decorative picture frames or bevelled icon slots.

Concept C, CENTRAL SEAL HUD. Desktop home page top, landscape 16:9, target 2048 x 1152. Radically slim game HUD taking only upper 17% of image. Small centered KAELVORN wordmark in top strip above a large anonymous brass-and-viridian compass seal that projects slightly below a thin straight indigo-steel HUD rail. FOUR text-led destinations LEFT of seal: Home, World, Callings, Skill Trees. FIVE destinations RIGHT of seal: Crafting, Adventures, Gallery, News, Launch. Tiny restrained painted pictograms adjacent to labels, never large icon tiles. Launch at far right has a compact countdown capsule directly beneath it with indicative 12d 08h 34m, integrated into bar. All nine labels fit with generous gaps, no duplicate links, no second navigation row. Active Home thin ochre notch. Header is a low-profile instrument panel with fine brass ticks, no crown moulding, no hanging cloth. Remaining 83% is expansive golden gorge hero, quiet left sky for future live headline.

TARGETED REMAKE: preserve the slim HUD with central compass emblem and expansive hero. Add small KAELVORN above central seal. Paint small but legible cream destination labels beside tiny symbols: left side Home, World, Callings, Skill Trees; right side Crafting, Adventures, Gallery, News, Launch. Reduce icons to label height so the bar stays slim. At far-right Launch capsule visibly render 12d 08h 34m in cream; no orange neon numbers. No extra text. All of these task-specific requested words and digits are mandatory exceptions to generic blank-text suffix and the final generic no-text rule; that final rule applies ONLY to extra lettering. Landscape 16:9.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Navigation concept c-mobile — attempt 2

Output: `art/redesign/nav/concept-c-mobile.png`

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

These are navigation build-reference concepts for the Kaelvorn MMORPG website. User-requested exceptions to the generic no-text/no-logo rule: a painted anonymous emblem placeholder with KAELVORN in carved capitals, plus clear indicative destination labels, which the builder will replace with live HTML text. Avoid other copy. There are exactly nine destinations, each once: Home, World, Callings, Skill Trees, Crafting, Adventures, Gallery, News, Launch. Adventures contains Dungeons, Raids, Bestiary. Match the attached gallery's high-end in-game interface character; this is a website screenshot, no device bezel, no perspective. Hero beneath the header is an oil-painted golden limestone gorge, distant citadel and a small adventuring party, subordinate to the navigation. Borrow surface, stroke scale, edge economy, palette and lighting from references, invent layout. Reference roles: candidate-a is primary paint authority, anchor-1-vista supplies landscape atmosphere, anchor-2-hero character planes/materials, anchor-3-creature stone/glow, anchor-4-icons supplies the frameless impasto icon style, concept-home supplies website visual continuity. Keep generous quiet dark zones behind live labels. Crown moulding and brass rails are functional header architecture, never decorative picture frames or bevelled icon slots.

Concept C, CENTRAL SEAL HUD adapted to phone, portrait 2:3, target 1024 x 1536; this portrait specification overrides landscape in fixed category suffix. Slim steel HUD rail at top with small KAELVORN wordmark, centered projecting brass/viridian compass seal below it, menu close X at right. A narrow countdown ribbon immediately below rail reads Launch — 12d 08h 34m. Expanded instrument-panel navigation beneath this is a dark translucent indigo overlay with two columns of wide text-led touch targets and tiny painted symbols: left column Home, World, Callings, Skill Trees; right column Crafting, Adventures, Gallery, News. Launch is the ninth destination already in countdown ribbon, do not repeat it. Active Home a tiny ochre notch and quiet teal stroke. No bottom action bar, no crown moulding or hanging cloth. Overlay ends near half screen, leaving lower half golden gorge hero visible. Clear symmetric geometry, restrained thin brass instrument ticks, ample readable label spacing. Every target is wide and practical for a phone.

TARGETED REMAKE: preserve portrait HUD rail, central compass emblem, two-column menu and hero below. Reduce each icon to a tiny 28-pixel-sized painted silhouette, giving generous text area. MUST paint KAELVORN wordmark in header. MUST paint Launch — 12d 08h 34m in narrow ribbon. Four rows of two text-led targets: left Home, World, Callings, Skill Trees; right Crafting, Adventures, Gallery, News. Left Home icon a tiny sun, World compass, Callings helmet, Skill Trees branch; right Crafting hammer, Adventures crossed swords, Gallery landscape, News scroll. All eight labels plus Launch in ribbon, nine destinations total. These exact required words/digits override generic blank-text suffix and final no-text rule; final rule applies ONLY to extra lettering. Output exactly 1024 x 1536 portrait 2:3. Menu ends around y=740 so hero remains half screen.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Navigation actual dimensions and retained review

All final files are opaque native PNGs copied unchanged from the built-in image tool. No resizing, cropping, colour edits or synthetic lettering overlays. Prefix, complete Website concept art suffix and final avoid paragraph were programmatically checked for verbatim inclusion in all eleven generated-attempt prompts.

| Concept | Attempt | Actual dimensions | Selection |
| --- | --- | --- | --- |
| a-desktop | 1 | 1672 x 941 | Retained |
| a-mobile | 1 | 1024 x 1536 | Discarded |
| a-mobile | 2 | 1024 x 1536 | Retained |
| b-desktop | 1 | 1672 x 941 | Discarded |
| b-desktop | 2 | 1672 x 941 | Retained |
| b-mobile | 1 | 1672 x 940 | Discarded |
| b-mobile | 2 | 1024 x 1536 | Retained |
| c-desktop | 1 | 1672 x 941 | Discarded |
| c-desktop | 2 | 1672 x 941 | Retained |
| c-mobile | 1 | 1024 x 1536 | Discarded |
| c-mobile | 2 | 1024 x 1536 | Retained |

All six retained images visually inspected at full-screen view: all nine destinations visible exactly once, KAELVORN wordmark and emblem present, oil materials and resting dark label masses preserved. All three mobile files are exactly 1024 x 1536 (2:3). All desktop files are 1672 x 941 (approximately 16:9). A uses a continuous icon banner, B hanging cloth with Adventures expanded, C a slim split HUD with integrated countdown. Native size differs from requested desktop target; retained because text and architecture are readable.

Builder handoff — these PNGs are comparison/build references, not finished navigation sprites. Recreate labels, controls, wordmark and countdown in live HTML; countdown values are invented layout examples. Preserve the hierarchy and responsive behaviour rather than exact generated icon identities. Do not use the entire painted screenshot as a clickable image menu.

- **A — Crown banner:** Desktop wordmark lintel above nine icon-over-label targets, active Home crimson tab. At phone width, a compact closed header opens the shown 3 x 3 menu, with a close control at top right. Strongest immediate destination discovery and painted icon presence. Weakness: largest header footprint and menu covers most of phone. Mobile generated icon meanings vary from desktop; live labels and final chosen icon mappings must remain consistent. The labelled menu, not incidental icon subject substitutions, is authoritative.
- **B — Guild banners:** Nine cloth pennants on desktop; Adventures opens the three-row Dungeons/Raids/Bestiary panel anchored beneath its own pennant. Phone opens a single hanging banner with all destinations stacked and Adventures children indented inline. Strongest distinctive material silhouette and explicit submenu relationship. Weakness: tall expanded phone menu and dropdown obscures hero; use internal scrolling for short phone viewports. The cream labels and cloth paint are readable; banner symbols simplify more toward stamped gold than the impasto icon anchor. This is a concept weakness, not a change to the icon style bible.
- **C — Central seal HUD:** Four labels left and five right of central emblem; Launch at far right owns the countdown capsule. Phone moves Launch/countdown to a ribbon above a two-column, four-row menu. Strongest compact desktop shell and hero exposure. Weakness: longest labels make desktop compression sensitive; collapse before targets crowd. Emblem overlaps the rail deliberately. Phone icons are larger than the requested 28 px pictograms and menu is slightly taller than half the screen; builder may reduce icons while retaining the shown hierarchy.

All close symbols and active states are indicative. A and C Adventures should expose Dungeons/Raids/Bestiary through an accessible disclosure using B's explicit child ordering; their open submenu state is not pictured. None of these static art references verifies keyboard interaction, focus treatment, live text contrast or actual responsive breakpoints. Next step: choose A, B or C, then Builder A implements the shell and verifies those behaviours.

## Crown-moulding frame assets — `art/ui/frames/`

- Tool: `gemini-api image`; default model `gemini-nano-banana-2.1`; 2K requested.
- Successful paid image generations: **6**. One additional command was rejected during request validation because this endpoint only supports JPEG response MIME; it returned no image.
- Returned source format: JPEG despite PNG output names. The CLI renamed each response to `.jpg`; lossless PNG copies are retained in `art/ui/raw/ornaments/`, then keyed to transparent production PNGs with `art/ui/tools/key.py`.
- Remakes: 0. All first generated images were retained.
- Review: no text, painted backdrop or broken shape. Green-dominance keying removes the JPEG-noisy chroma field and spill. `contact-sheet.png` checks every asset over `#11151E` and `#EFE3C6`, and assembles frames at two sizes.

### `crest-top.png` — retained

- References: `art/style/anchor-4-icons.png`, `art/gallery/concept-raids.png`, `art/gallery/concept-coming-soon.png`.
- Command: `gemini-api image '<prompt below>' -i art/style/anchor-4-icons.png -i art/gallery/concept-raids.png -i art/gallery/concept-coming-soon.png --aspect-ratio 21:9 --image-size 2K --out art/ui/raw/ornaments/crest-top.png`
- Actual source: 3168 × 1344 RGB JPEG; normalized output: 1600 × 400 RGBA PNG.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Paint one isolated, centred crown-moulding crest component for the top edge of a dark fantasy card, not a complete frame. A small cracked bell hanging inside a three-pronged ruined-spire crown, flanked symmetrically by restrained acanthus scrollwork. Weathered tarnished brass face, indigo-steel recesses, tiny umber-stone chips, upper-left ochre catches; no glow. Strong readable silhouette, broad and low, approximately four-to-one within the canvas, substantial centre and tapered scroll ends. The back and all empty area must be one perfectly flat solid chroma green #00FF00, edge to edge, without texture, vignette, shadow, floor, halo, scenery or other objects. Borrow only the references' impasto, brass rendering, panel scale and edge economy; invent this ornament. Production alpha-key asset, 2K PNG.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### `crest-top-small.png` — retained

- References: `art/style/anchor-4-icons.png`, `art/gallery/concept-home.png`, `art/gallery/concept-character.png`.
- Successful command: `gemini-api image '<prompt below>' -i art/style/anchor-4-icons.png -i art/gallery/concept-home.png -i art/gallery/concept-character.png --aspect-ratio 21:9 --image-size 2K --out art/ui/raw/ornaments/crest-top-small.png`
- Rejected, no-image command: same command plus `--output-mime-type image/png`; API validation reported that only `image/jpeg` is supported.
- Actual source: 3168 × 1344 RGB JPEG; normalized output: 1200 × 300 RGBA PNG.

Submitted prompt, verbatim (same prompt on rejected and successful commands):

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Paint one isolated, centred small crown-moulding crest component for the top edge of a compact dark fantasy card, not a complete frame. A simple cracked bell under one pointed broken-spire finial, with one clean brass curl to each side and an indigo-steel backing. No more than five major shapes, no tiny filigree, no glow. Strong icon-scale silhouette, broad and low, approximately four-to-one within the canvas, with tapered ends and ample green clearance. The back and all empty area must be one perfectly flat solid chroma green #00FF00, edge to edge, without texture, vignette, shadow, floor, halo, scenery or other objects. Borrow only the references' impasto, brass rendering, panel scale and edge economy; invent this ornament. Production alpha-key asset, 2K PNG.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### `corner.png` — retained

- References: `art/style/anchor-4-icons.png`, `art/gallery/concept-map.png`, `art/gallery/concept-skill-tree.png`.
- Command: `gemini-api image '<prompt below>' -i art/style/anchor-4-icons.png -i art/gallery/concept-map.png -i art/gallery/concept-skill-tree.png --aspect-ratio 1:1 --image-size 2K --out art/ui/raw/ornaments/corner.png`
- Actual source: 2048 × 2048 RGB JPEG; normalized output: 512 × 512 RGBA PNG.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Paint one isolated top-left corner ornament for a modular dark fantasy card frame, not a complete frame. Square L-shaped construction: a cracked indigo-steel and umber-stone right angle, faced with one restrained tarnished-brass acanthus leaf curling inward. The outside corner is weighty and the two straight arms taper cleanly toward the right and bottom so mirrored copies make all four corners. No asymmetrical hanging objects, no glow. Strong readable silhouette with both arms meeting at an exact right angle and ample green clearance. The back and every opening and all empty area must be one perfectly flat solid chroma green #00FF00, edge to edge, without texture, vignette, shadow, floor, halo, scenery or other objects. Borrow only the references' impasto, brass rendering, panel scale and edge economy; invent this ornament. Production alpha-key asset, square 2K PNG.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### `edge-horizontal.png` — retained

- References: `art/style/anchor-4-icons.png`, `art/gallery/concept-home.png`, `art/gallery/concept-map.png`.
- Command: `gemini-api image '<prompt below>' -i art/style/anchor-4-icons.png -i art/gallery/concept-home.png -i art/gallery/concept-map.png --aspect-ratio 21:9 --image-size 2K --out art/ui/raw/ornaments/edge-horizontal.png`
- Actual source: 3168 × 1344 RGB JPEG; normalized output: 1024 × 128 RGBA PNG.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Paint one isolated horizontal edge-trim tile for a modular dark fantasy card frame, not a complete frame. A very thin straight indigo-steel rail with chipped stone beneath and sparse tarnished-brass bindings in a simple repeating rhythm. Strictly side-on and level, no perspective, no centre crest, no end caps. The ornament enters at the exact midpoint of the left edge and exits at the exact midpoint of the right edge with identical thickness, colour and pattern phase, designed for seamless left-to-right repetition. Keep all paint inside a low strip approximately eight-to-one, with generous green above and below. The back and all empty area must be one perfectly flat solid chroma green #00FF00, edge to edge, without texture, vignette, shadow, floor, halo, scenery or other objects. Borrow only the references' impasto, brass rendering, panel scale and edge economy; invent this trim. Production alpha-key asset, 2K PNG.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### `edge-vertical.png` — retained

- References: `art/style/anchor-4-icons.png`, `art/gallery/concept-character.png`, `art/gallery/concept-skill-tree.png`.
- Command: `gemini-api image '<prompt below>' -i art/style/anchor-4-icons.png -i art/gallery/concept-character.png -i art/gallery/concept-skill-tree.png --aspect-ratio 9:16 --image-size 2K --out art/ui/raw/ornaments/edge-vertical.png`
- Actual source: 1536 × 2752 RGB JPEG; normalized output: 128 × 1024 RGBA PNG.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Paint one isolated vertical edge-trim tile for a modular dark fantasy card frame, not a complete frame. A very thin straight indigo-steel rail with chipped stone beside it and sparse tarnished-brass bindings in a simple repeating rhythm. Strictly front-on and vertical, no perspective, no centre crest, no end caps. The ornament enters at the exact midpoint of the top edge and exits at the exact midpoint of the bottom edge with identical thickness, colour and pattern phase, designed for seamless top-to-bottom repetition. Keep all paint inside a tall strip approximately one-to-eight, with generous green to both sides. The back and all empty area must be one perfectly flat solid chroma green #00FF00, edge to edge, without texture, vignette, shadow, floor, halo, scenery or other objects. Borrow only the references' impasto, brass rendering, panel scale and edge economy; invent this trim with lighting consistent with a fixed upper-left source. Production alpha-key asset, 2K PNG.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### `divider.png` — retained

- References: `art/style/anchor-4-icons.png`, `art/gallery/concept-raids.png`, `art/gallery/concept-coming-soon.png`.
- Command: `gemini-api image '<prompt below>' -i art/style/anchor-4-icons.png -i art/gallery/concept-raids.png -i art/gallery/concept-coming-soon.png --aspect-ratio 21:9 --image-size 2K --out art/ui/raw/ornaments/divider.png`
- Actual source: 3168 × 1344 RGB JPEG; normalized output: 1600 × 200 RGBA PNG.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Paint one isolated ornamental horizontal section divider, not a complete frame. A long hairline indigo-steel and chipped-stone rule, centred on a small cracked bell medallion under a broken-spire point, with sparse tarnished-brass knots and two subtle acanthus flicks. Symmetrical, elegant and restrained; the line tapers to narrow pointed tips. Broad, very low silhouette approximately eight-to-one, with generous chroma-green clearance, no glow. The back and all empty area must be one perfectly flat solid chroma green #00FF00, edge to edge, without texture, vignette, shadow, floor, halo, scenery or other objects. Borrow only the references' impasto, brass rendering, panel scale and edge economy; invent this divider. Production alpha-key asset, 2K PNG.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```

### Processing commands

```sh
python3 art/ui/tools/key.py art/ui/raw/ornaments/crest-top.png art/ui/frames/crest-top.png --canvas 1600x400
python3 art/ui/tools/key.py art/ui/raw/ornaments/crest-top-small.png art/ui/frames/crest-top-small.png --canvas 1200x300
python3 art/ui/tools/key.py art/ui/raw/ornaments/corner.png art/ui/frames/corner.png --canvas 512x512
python3 art/ui/tools/key.py art/ui/raw/ornaments/edge-horizontal.png art/ui/frames/edge-horizontal.png --canvas 1024x128 --margin-x 0 --margin-y 0.04 --tile-axis x
python3 art/ui/tools/key.py art/ui/raw/ornaments/edge-vertical.png art/ui/frames/edge-vertical.png --canvas 128x1024 --margin-x 0.04 --margin-y 0 --tile-axis y
python3 art/ui/tools/key.py art/ui/raw/ornaments/divider.png art/ui/frames/divider.png --canvas 1600x200
python3 art/ui/tools/contact_sheet.py
```

## Painted atlas — `art/ui/atlas/` — 2026-10-26

- Tool: built-in `image_gen.imagegen`; one generation, retained first attempt.
- References (style only, not edit targets): `art/style/candidate-a.png`, `art/style/anchor-1-vista.png`, `art/gallery/concept-map.png`.
- Requested and actual dimensions: **1536 × 1024**, exact landscape 3:2, opaque PNG. Original native image copied without cropping, resizing or recolouring.
- Output: `art/ui/atlas/kaelvorn-atlas.png`. Companion `regions.json` is a plain array of six `{ id, x, y }` records; x increases left-to-right and y top-to-bottom, both 0–100 percentages of the **whole image**. Preview dot numbers follow array order and the canonical region order in `src/data/world.ts`.
- Builder handoff: render the complete image at aspect-ratio 3 / 2; position live pin centres at `left: x%; top: y%; transform: translate(-50%, -50%)` within the same image rectangle. Avoid cover-cropping; if using contain, the overlay must align to the rendered image, excluding letterbox space. Use the clean atlas in production; `preview.png` is review-only.
- Visual review: crescent opens south into the Churn; white limestone terraces west, warm flooded forest south/southeast, basalt foundries east, copper dunes north of the foundries beneath snowy peaks, glass crater at the northern throat. Ink coastlines, compass rose, faint marginal Canopy arches; no lettering, frame, UI or painted pin markers. The miniature view uses oblique terrain relief as in the map reference. The snow collar partly surrounds the crater but its pass landmark is distinctly south of the broken spire.
- Pins measured by visual inspection of the saved image, on land landmarks: 1 western fortress (high confidence), 2 giant banyan root cluster (high), 3 brass foundry complex on coastal cliff (high), 4 stepped desert ziggurat (high), 5 brass fortress/wind-organ landmark at snowy pass (medium-high: pipes simplify at map scale), 6 broken spire base in glass crater (high). Exact coordinates and numbered preview checked together.
- Preview is a deterministic numbered-dot overlay only; the production painting is untouched.

Submitted prompt, verbatim:

```text
Digital oil painting on fine-tooth linen; bold flat-bristle strokes, raised palette-knife impasto, three-tone masses, sharp focal edges and lost peripheral edges. Low 35-degree upper-left #F2C97D sunlight; #232B3A cool fill; thin #38D6C4 shadow-side rim. Palette: #11151E shadow floor, #232B3A weathered steel, #6E5A4F stone/leather, #C29B61 tarnished brass/dry grass, #F2C97D sunlit planes, #A62639 restrained cloth, #38D6C4 arcane accents. Metal catches decisive strokes; cloth sweeps, stone dry-brushes, skin stays planar. Magic has near-white cores, tight teal corona and painted bounce. Outer ten-percent vignette dissolves into #11151E.

Website concept art: one in-game UI mock-up screen, straight-on orthographic screen view, dark stone panels, tarnished-brass dividers, action-bar navigation, tooltip and restrained rarity accents surrounding painterly art, blank text areas for later live HTML, no decorative picture frames, landscape 16:9.

The output for this request is ONLY the atlas art, without any UI. Override the category's screen composition and aspect ratio: landscape exact 3:2, native target 1536 x 1024. Paint a beautiful aged ochre parchment atlas of Kaelvorn, north at top, an irregular massive horseshoe/crescent continent encircling a large ink-blue inland sea, the Mirror-Reach, open to the ocean at the bottom/south through a broad mouth. The crescent's two long arms curve downward from a joined northern land bridge; no closed ring, no central island city. Use dark hand-inked coastlines and miniature oblique painted terrain on a flat cartographic plane, not a landscape camera. Leave parchment margins on every side, full continent visible.

Exactly six distinct connected biome regions, arranged canonically: WEST/LEFT ARM, high white limestone stepped terraces and golden grasslands of the Sun-Steppe of Aethel, landmark a small pale fortress on a broad tier with aqueducts; SOUTHERN CURVE especially LOWER RIGHT ARM, lush Whispering Fen and Root-Basin with giant banyan trees, branching river delta, turquoise wetlands and a ruined mossy aqueduct, landmark a cluster of three great trees on firm land; EAST/RIGHT ARM at middle-right, Cinder-Reach and Brass-Coast, dark basalt fjords and geothermal copper badlands, landmark a little brass foundry-harbor with smokestacks on a coastal cliff; NORTHEAST/UPPER RIGHT, north of the industrial coast and below the snowy range, Singing Dunes of Kal-Zir, a broad distinct copper dune desert with a half-buried stepped ziggurat and tiny oasis; NORTH, a transverse collar of Frost-Chime Peaks immediately SOUTH of the glass crater, blue-shadowed snow mountains with an identifiable brass wind-organ fortress at a high pass east of centre; FARTHEST NORTH/CENTRE TOP, the Shattered Crown glass highland, a white vitrified crater surrounded by translucent crystalline woods and small floating basalt slabs, landmark Sol-Vara a single broken dark bronze spire with its separated upper section floating just above it and a restrained pale teal-white core. The crater must be LAND attached to the northern bridge, not in the sea. Keep snow peaks visibly distinct from the glass highland above them.

Draw one small elegant unlettered eight-point ink-and-brass compass rose in the lower-left parchment margin. Faint amber fragments of the Canopy's huge arches in the outer parchment margins only, subordinate and incomplete, never a frame. Resting broad parchment and blue sea masses, rich brush-painted landforms, restrained teal at marshes and broken spire. No region boundaries, grid, pin markers, numbered dots, labels, banners, legends, text boxes, interface, decorative border or frame. Live site controls will be overlaid later.

Reference roles: candidate-a.png and anchor-1-vista.png provide ONLY oil surface, stroke scale, palette, edge economy and warm/cool light; do not copy their heroes or landscape composition. concept-map.png provides parchment-and-ink cartographic rendering and blue water ONLY; discard all its UI, frame, beacons and its approximate region placements. Invent the requested canonical geography above.

No text, no lettering, no logos, no watermark, no painted frames, no painted borders, no bevelled icon slots, no photoreal skin, no skin pores, no 3D plastic sheen, no glossy CGI, no neon cyberpunk colours, no lens flare rings, no uniform sharpness, no smooth airbrushed finish, no photographic texture overlays, no anime outlines, no chibi proportions, no rainbow lighting, no pure-black shadow crush, no extra limbs, no duplicated subjects, no clipped focal silhouettes.
```
