# "Aktarım Zinciri / The Transmission Chain" — FULL CONTENT FOR EXPERT REVIEW

An interactive bilingual (Turkish/English) web essay, self-described as "a conceptual study revised after three expert reviews", version 4.0, data cut-off 20 August 2026. Intended for publication on the author's public GitHub Pages site. Below is EVERY substantive claim it makes, extracted verbatim from the source (English strings; a parallel Turkish translation exists).

## 0. CENTRAL THESIS AND FRAMING

**Hero headline:** "Knowledge travels;context does not always travel with it."

**Hero lead:** We do not inherit the whole of the past, only packets of it compressed into symbols and procedures. When the key is lost, the result can survive while the knowledge becomes impossible to reproduce.

**Stated "most defensible conclusion":** "Progress is not the growth of the archive alone; it is whether the network of records, people, training, tools, institutions and criticism can stay alive together."

**Site description (meta):** An interactive study of how humanity packs knowledge across generations, how context is preserved, and what gets lost.

### The transmission chain (5 links shown as the core diagram)
Section heading: "A sign, on its own, is not knowledge."
1. **Lived experience** — Raw, whole, and too large to transmit.
2. **Selection and packet** — A decision about what is worth recording.
3. **Archive and copy** — Medium, copy fidelity, durability.
4. **Decoder and context** — Language, training, institutions, tacit skill.
5. **Re-execution** — This is the only place where the chain is actually tested.

### "What travels" (the packet) vs "what is easily lost" (the key)
**Travels:** Signs, formulas and drawings · Results and short procedures · Copyable records · Standards and classifications

**Easily lost:** How it was found · Why it was held to be true · The limits of its validity · Tacit manual and judgement skill

### How the study says it came about
1. How short a human life is on a cosmic scale — barely a tick.
2. The bounded budget of individual learning.
3. The way letters and formulas work like a ZIP archive.
4. Method and context going missing while the result travels.
5. The question of whether progress is a straight line.
6. Noticing the strange behaviour in the chart.
7. Rebuilding the model after three expert reviews.
8. Testing the argument against its own examples by adding the loss cases.

## 1. THE FORMAL MODEL

**Stated scope limit:** This study does not measure total human knowledge. The individual generational simulation and the collective historical index are separate instruments, and their numbers cannot be compared directly.

**Core formulas presented to the reader:**
```
H = K × G          (H = effective reach)
C = P × q_c        (C = contextual)
R = C × q_d        (R = reproducible)
```
Explanation given: K is the individual learning budget, G the effective reach gain, P the historical packaging index, qc the quality of context and qd that of the decoder and access. P − R is not context loss alone.

**Glossary:**
- **Packet** — Selected content carried as a sign, formula or procedure.
- **Decoder** — The key: language, training, concepts and standards.
- **Context** — Method, evidence, the history of errors, and conditions of application.
- **Tacit knowledge** — Embodied, intuitive skill that cannot be fully written down.
- **Apparatus** — The machine, software or format support that can physically read the record.
- **Maintenance** — The recurring labour of copying, migrating, updating and teaching.

**ACTUAL SIMULATION CODE (this is what the interactive chart runs — check it against the formulas above):**
```js
function simulate(p) {
  var retention = Math.exp(-Math.log(2) / p.halfLife);
  var archive = p.capacity * 2, contextual = archive, out = [];
  for (var i = 0; i < p.generations; i++) {
    var recorded = p.innovation * .85 * .9;
    archive = archive * retention + recorded;
    contextual = Math.min(archive, contextual * retention * p.qc + recorded * .85);
    var effective = p.capacity * p.gain;
    var selected = Math.min(archive, effective);
    var rebuilt = selected * (archive ? contextual / archive : 0) * p.qd;
    out.push({ g: i + 1, archive: archive, contextual: contextual, rebuilt: rebuilt, effective: effective, selected: selected });
  }
  return out;
}
```
Default parameters: `{"capacity":5,"gain":4,"qc":0.88,"qd":0.82,"innovation":1.5,"halfLife":35,"generations":40}`

**Slider definitions and the long-form explanation shown to users behind a "?" button:**

**Individual learning budget (K)** — An abstract stand-in for how much one person can genuinely learn and master in a lifetime. Not a measure of intelligence, but the sum of time, attention and educational opportunity.The point of the model is this: this budget has barely changed across history. A lifetime was a lifetime 100,000 years ago and it still is. Because the number stays flat while the archive grows, each generation can carry an ever smaller share of it.Raising it means assuming longer schooling and better teaching methods — not a bigger skull.

**Packaging gain (G)** — How much experience a symbol, formula or procedure compresses into a single portable unit. It does not enlarge capacity; it enlarges how much ground the same budget can cover.“F = ma” carries countless observations in three marks — that is the gain. Writing, print, mathematical notation and now language models are what made this term jump.But note: as gain rises, so does the context left outside the packet. Raising G alone is not always good news — to see that, hold Context transfer fixed and push this to the maximum.

**Context transfer (q_c)** — How much of the method, the evidence, the history of errors and the limits of validity travels along with the packet.100% means every result arrives together with “how it was found, why it was believed, where it fails.” Low values are the historical norm: we hold the Antikythera mechanism but not its manual; the Damascus blade survives but not its recipe.When this term falls, the archive keeps growing while reproducibility collapses. That gap is exactly the orange line pulling away from the blue one.

**Decoder and access (q_d)** — The share and quality of people who can open the packet: language, literacy, shared concepts, standards, training and physical access.If a record exists but nobody can read it, no transmission occurs. That is precisely why the Linear B tablets stayed silent for 3,000 years — and why rongorongo still is.Spreading literacy, a shared scientific language and internet access all raised this term. In the first ages of writing, by contrast, the archive grew while the decoder stayed locked inside a scribal class — which is why the “After writing” preset sets it low.

**Gross new input** — The raw output each generation adds on top of what it inherited. “Gross”, because not all of it enters the archive: the model assumes 85% passes verification and 90% is actually recorded.Raising this grows the archive fast but does not automatically grow the contextualised share — it dilutes the ratios.This slider is the quickest way to see that “more output” and “better transmission” are not the same thing: push it to the maximum and watch the external archive leap while the reproducible portion fails to keep pace.

**Archive half-life** — How many generations it takes for half the records to become inaccessible. A continuous decay rate is used rather than a fixed percentage.A short half-life does not only mean fire and war: papyrus decay, format obsolescence, the reading machine going out of production and link rot all fall under the same term. An unmaintained archive shrinks even when nobody touches it.The “Digital age” preset has a deliberately short half-life: the archive is larger than ever, yet half the live links are gone within a decade.

**Simulation length** — How many generations to look ahead. Not calendar years but an abstract number of steps; a “generation” is one interval in which transmission happens once.Extending it adds no new information — it only shows where the current assumptions converge in the long run. Push it to the maximum to see where the curves settle.Shortening it makes the short-run behaviour easier to read, especially the transient in the first few generations.

**Generation examined** — Selects which generation the vertical guide and the three figures above refer to.It does not change the model — only which moment you are looking at. The shape of the curves stays the same.

**Historical presets (each sets K, G, q_c, q_d, innovation, half-life):**
- **Oral culture** — `{"capacity":5,"gain":1.5,"qc":0.96,"qd":0.5,"innovation":0.5,"halfLife":10,"generations":40}` — rationale shown to user: High context, short range: knowledge travels in bodies and teachers, and no copy is left behind.
- **After writing** — `{"capacity":5,"gain":3,"qc":0.66,"qd":0.3,"innovation":1,"halfLife":40,"generations":40}` — rationale shown to user: Range jumps and the archive becomes durable, but the decoder is locked inside a scribal class and method goes unwritten.
- **Print and the journal** — `{"capacity":5,"gain":4.5,"qc":0.84,"qd":0.62,"innovation":2,"halfLife":55,"generations":40}` — rationale shown to user: Copy fidelity and the institution of criticism arrive together: in this model, the period where context travels best.
- **The digital age** — `{"capacity":5,"gain":7,"qc":0.52,"qd":0.92,"innovation":4.5,"halfLife":18,"generations":40}` — rationale shown to user: Gain and access peak and input explodes, but context thins and link rot shortens the archive's half-life.

Disclaimer shown with the presets: The presets are not historical measurements but debatable readings. The numbers are not derived from history; they encode an interpretation of which mechanism dominated when.

**The "persistent distinction" callout on the model page:** A distinction that holds: knowledge left unselected because of capacity is not the same as knowledge that has lost its context. Rising input can dilute the ratios; that is not an improvement in quality.

## 2. THE HISTORICAL INDEX (a SEPARATE instrument from the simulation)

Labelled in the UI as: "Model inference · Not a measurement · Bands are a scenario range"

Hard-coded index values plotted as three curves plus a shaded "scenario range" band, on a 0–100 scale, from 100,000 years ago to 2026. P = packaging, C = contextual, R = reproducible, low/high = band bounds.

| year | P | C | R | band low | band high |
|---|---|---|---|---|---|
| -97974 | 8 | 6 | 4 | 1 | 12 |
| -71974 | 9 | 7 | 5 | 2 | 15 |
| -47974 | 13 | 10 | 8 | 3 | 20 |
| -28974 | 16 | 13 | 10 | 4 | 24 |
| -9974 | 21 | 17 | 12 | 5 | 28 |
| -8000 | 28 | 15 | 7 | 3 | 23 |
| -3200 | 36 | 18 | 4 | 1 | 18 |
| 1 | 46 | 25 | 8 | 3 | 22 |
| 751 | 56 | 33 | 12 | 6 | 26 |
| 1234 | 62 | 39 | 14 | 8 | 29 |
| 1455 | 71 | 48 | 21 | 14 | 34 |
| 1665 | 77 | 56 | 30 | 22 | 43 |
| 1850 | 86 | 70 | 45 | 37 | 56 |
| 1950 | 92 | 82 | 59 | 52 | 67 |
| 1986 | 94 | 86 | 62 | 56 | 70 |
| 2002 | 98 | 88 | 65 | 58 | 73 |
| 2026 | 100 | 90 | 70 | 62 | 78 |

Values between these anchor points are linearly interpolated. Code:
```js
function interpolateHistory(year) {
  var hp = historyPoints;
  if (year <= hp[0].year) return Object.assign({}, hp[0], { year: year });
  if (year >= 2026) return Object.assign({}, hp[hp.length - 1], { year: year });
  for (var i = 1; i < hp.length; i++) {
    var a = hp[i - 1], b = hp[i];
    if (year <= b.year) {
      var f = (year - a.year) / (b.year - a.year);
      return { year: year, p: a.p + (b.p - a.p) * f, c: a.c + (b.c - a.c) * f, r: a.r + (b.r - a.r) * f,
               low: a.low + (b.low - a.low) * f, high: a.high + (b.high - a.high) * f };
    }
  }
  return hp[hp.length - 1];
}
```

Callout under the chart: The oldest evidence found is not the date of invention. The archaeological record is not lived culture itself but a small, preserved and interpreted sample of it.

## 3. EVIDENCE RECORDS (23) — plotted as markers on the timeline

Each is tagged `direct` (dated material record) or `proxy` (indirect indicator), with a stated confidence, a "what it shows", a "what it does NOT show", a role in the model, and a primary source link. Categories: `threshold` (transmission threshold), `loss` (loss case), `digital`.

### Blombos multi-stage ochre processing
- **id/category/loss-type:** `blombos` / `threshold`
- **date plotted:** -97974 (range -100974 to -94974) · **region:** South Africa
- **type:** direct · **confidence:** high
- **role in model:** Method and tacit skill
- **SHOWS:** Shows that a multi-component recipe with an ordered procedure existed roughly 100,000 years ago.
- **DOES NOT SHOW:** The purpose of the mixture and how it was taught are not directly known.
- **source:** Science · Henshilwood et al., 2011 — https://www.science.org/doi/10.1126/science.1211535

### The Blombos graphic mark
- **id/category/loss-type:** `mark` / `threshold`
- **date plotted:** -70974 (range -72474 to -69474) · **region:** South Africa
- **type:** direct · **confidence:** medium
- **role in model:** External symbolic packet
- **SHOWS:** An early example of a graphic mark on a portable surface.
- **DOES NOT SHOW:** It cannot be called writing, nor shown to carry a specific message.
- **source:** Nature · Henshilwood et al., 2018 — https://www.nature.com/articles/s41586-018-0514-3

### The Borneo surgical care find
- **id/category/loss-type:** `borneo` / `threshold`
- **date plotted:** -28974 (range -30974 to -26974) · **region:** Indonesia
- **type:** proxy · **confidence:** medium
- **role in model:** Expertise and live instruction
- **SHOWS:** Points to healing, anatomical and care knowledge having been transmitted.
- **DOES NOT SHOW:** How it was taught, and how widespread the technique was, are unknown.
- **source:** Nature · Maloney et al., 2022 — https://www.nature.com/articles/s41586-022-05160-8

### GunaiKurnai ritual continuity
- **id/category/loss-type:** `gunaikurnai` / `threshold`
- **date plotted:** -8974 (range -9974 to -7974) · **region:** Australia
- **type:** proxy · **confidence:** medium
- **role in model:** Oral and embodied continuity
- **SHOWS:** Suggests that transmission without writing can survive for a very long time.
- **DOES NOT SHOW:** The reading of 500 unbroken generations is open to debate.
- **source:** Nature Human Behaviour · 2024 — https://www.nature.com/articles/s41562-024-01912-w

### Early Mesopotamian writing
- **id/category/loss-type:** `writing` / `threshold`
- **date plotted:** -3200 (range -3400 to -3000) · **region:** Southern Mesopotamia
- **type:** direct · **confidence:** high
- **role in model:** Durable external memory
- **SHOWS:** Shows an economic record turning into a durable sign system.
- **DOES NOT SHOW:** Access depended on specialist scribes; it did not carry the whole of experience.
- **source:** Metropolitan Museum · The origins of writing — https://www.metmuseum.org/essays/the-origins-of-writing

### Loss of the Linear B decoder chain
- **id/category/loss-type:** `linear-b` / `loss` / `decoder`
- **date plotted:** -1200 (range -1250 to -1100) · **region:** The Aegean
- **type:** proxy · **confidence:** high
- **role in model:** A regional break in code and institution
- **What survived:** Clay tablets — the written record of a palace economy, made permanent by the fire that destroyed it.
- **What was lost:** The scribal class that read them and the palace institution that made them meaningful. The tablets stayed silent for 3,000 years.
- **SHOWS:** A regional case showing that an archive alone is not openable knowledge.
- **DOES NOT SHOW:** It does not show that human knowledge globally declined at the same date.
- **source:** British Museum · The Mycenaean world — https://www.britishmuseum.org/collection/galleries/greece-minoans-and-mycenaeans

### The Antikythera mechanism
- **id/category/loss-type:** `antikythera` / `loss` / `tacit`
- **date plotted:** -150 (range -205 to -60) · **region:** Aegean · the Hellenistic world
- **type:** direct · **confidence:** high
- **role in model:** Applied astronomy left without a manual
- **What survived:** A single corroded bronze device: a precision gear train that mechanically encodes solar, lunar and eclipse cycles.
- **What was lost:** No manual, no workshop tradition, no comparable second machine. Neither the teaching nor the making was transmitted.
- **SHOWS:** A single artifact proves that mechanical computation existed in the Hellenistic world — yet the rest of the chain is absent.
- **DOES NOT SHOW:** It does not show that geared computation was widespread or continuously transmitted; its date (~205 BCE vs ~150-100 BCE), maker and workshop remain disputed. The popular front-dial reconstructions are models fitted to fragmentary evidence, not observations.
- **source:** Nature · Freeth et al., 2006 — https://www.nature.com/articles/nature05357

### Roman concrete and hot mixing
- **id/category/loss-type:** `roman-concrete` / `loss` / `tacit`
- **date plotted:** 126 (range -200 to 235) · **region:** Roman Italy and the Mediterranean
- **type:** direct · **confidence:** medium
- **role in model:** A step legible in the material but absent from the texts
- **What survived:** Standing structures and the mortar itself: the white “lime clasts” long taken for careless mixing.
- **What was lost:** The written procedure. Vitruvius and Pliny describe Roman mixes but not this step; the recipe survived in the material, not in the text.
- **SHOWS:** The clasts are a reactive quicklime reservoir produced by hot mixing; lab replicas made this way sealed deliberately induced cracks within two weeks, while quicklime-free controls never healed.
- **DOES NOT SHOW:** Intentionality is inferred, not documented; some researchers still read the clasts as relict under-burnt lime. Roman concrete is also not “stronger” than modern concrete — it is more durable in seawater and self-repairing; and Roman building knowledge was interrupted, not wholly lost.
- **source:** Science Advances · Seymour, Maragh, Masic et al., 2023 — https://news.mit.edu/2023/roman-concrete-durability-lime-casts-0106

### The Nalanda teaching network
- **id/category/loss-type:** `nalanda` / `threshold`
- **date plotted:** 600 (range 450 to 1200) · **region:** South Asia
- **type:** proxy · **confidence:** high
- **role in model:** Text plus live teaching
- **SHOWS:** Shows teachers, debate and curriculum completing the text with context.
- **DOES NOT SHOW:** It was not a single, uninterrupted global network.
- **source:** UNESCO World Heritage · Nalanda — https://whc.unesco.org/en/list/1502/

### Greek fire and enforced secrecy
- **id/category/loss-type:** `greek-fire` / `loss` / `secrecy`
- **date plotted:** 950 (range 672 to 1204) · **region:** Byzantine Empire · Constantinople
- **type:** direct · **confidence:** medium
- **role in model:** A decoder deliberately never written down
- **What survived:** Chronicles describing its effects, and the weapon's strategic reputation.
- **What was lost:** The composition. In the handbook he wrote for his son, Constantine VII states that the secret of the “liquid fire discharged through tubes” was revealed to the Byzantines alone and must never be divulged to foreigners.
- **SHOWS:** A documented case of a state deliberately refusing to write the decoder down.
- **DOES NOT SHOW:** No surviving text gives the actual composition; every modern “reconstruction” is inference from described effects. Whether it was one fixed recipe or a family of petroleum-based mixtures, and whether it was truly lost or simply superseded, are both disputed.
- **source:** Dumbarton Oaks Texts · Constantine VII, De Administrando Imperio — https://www.doaks.org/resources/publications/books/de-administrando-imperio

### East Asian and European printing networks
- **id/category/loss-type:** `printing` / `threshold`
- **date plotted:** 1234 (range 751 to 1455) · **region:** China, Korea and Europe
- **type:** direct · **confidence:** high
- **role in model:** Copy fidelity and scale
- **SHOWS:** Enabled packets to be reproduced more often and more consistently.
- **DOES NOT SHOW:** It cannot be reduced to a single inventor or a single civilisational line.
- **source:** UNESCO Courier · The master printers of Koryo — https://courier.unesco.org/en/articles/200-years-gutenberg-master-printers-koryo

### The rongorongo script of Rapa Nui
- **id/category/loss-type:** `rongorongo` / `loss` / `decoder`
- **date plotted:** 1500 (range 1493 to 1887) · **region:** Rapa Nui (Easter Island), Polynesia
- **type:** direct · **confidence:** medium
- **role in model:** A sign system whose readers died out within a generation
- **What survived:** About twenty-five inscribed wooden objects. Direct radiocarbon dating of four Rome-held tablets returned wood ages from 1493-1509 to 1832-1887.
- **What was lost:** Everyone who could read them. Within a generation of contact no readers remained; the objects persist, the key does not.
- **SHOWS:** The clearest example of a decoder vanishing on its own while the carrier remains intact.
- **DOES NOT SHOW:** Radiocarbon dates the wood, not the carving — driftwood and reuse are likely — so a 15th-century date does not prove pre-contact invention. Whether rongorongo is full writing, a mnemonic system, or a post-contact response to Spanish documents is still openly contested.
- **source:** Scientific Reports · Ferrara, Tassoni, Kromer et al., 2024 — https://www.nature.com/articles/s41598-024-53063-7

### The destruction of the Maya codices
- **id/category/loss-type:** `maya-codices` / `loss` / `carrier`
- **date plotted:** 1562 (range 1519 to 1697) · **region:** Yucatán, Mesoamerica
- **type:** direct · **confidence:** high
- **role in model:** A carrier erased within a single generation
- **What survived:** Three securely accepted screenfold codices worldwide — the Dresden among them — plus a disputed fourth. And the inscriptions on stone.
- **What was lost:** Almost the whole of a literate book tradition. The physical carrier was reduced by roughly three orders of magnitude in one colonial generation.
- **SHOWS:** Shows a civilisation's astronomical and ritual corpus being lost by destroying the carrier while the decoder was still alive.
- **DOES NOT SHOW:** The often-cited “27 books burned at Maní in July 1562” rests on Diego de Landa's own account, and the true volume is unknowable. The same Landa also recorded the glyph-and-syllable “alphabet” that Knorozov later used to crack Maya writing: the destroyer also supplied part of the key.
- **source:** SLUB Dresden · The Dresden Maya Codex, Mscr.Dresd.R.310 — https://www.slub-dresden.de/en/explore/manuscripts/the-dresden-maya-codex

### The scientific journal and peer review
- **id/category/loss-type:** `journal` / `threshold`
- **date plotted:** 1665 (range 1665 to 1832) · **region:** Initially Europe, later international
- **type:** proxy · **confidence:** high
- **role in model:** Method, evidence and criticism
- **SHOWS:** Strengthened the regular circulation of method and debate alongside results.
- **DOES NOT SHOW:** It does not mean science began in 1665.
- **source:** Royal Society · Philosophical Transactions — https://royalsociety.org/journals/publishing-activities/publishing350/history-philosophical-transactions/

### Damascus (wootz) crucible steel
- **id/category/loss-type:** `wootz` / `loss` / `tacit`
- **date plotted:** 1750 (range 1600 to 1850) · **region:** South India and Sri Lanka; the Near East
- **type:** direct · **confidence:** medium
- **role in model:** A variable the craftsmen themselves could not see
- **What survived:** The blades themselves — patterned, keen, physically present in museums.
- **What was lost:** The process. Production stops around 1750 even though smiths, forges and demand persisted. The critical variable — trace elements in specific ores plus a heat-treatment sequence — was invisible to the very craftsmen who depended on it.
- **SHOWS:** Shows a technique halting silently when it depends on an input its practitioners were never aware of.
- **DOES NOT SHOW:** The ore-exhaustion / trace-element (V, Cr, Mo, Mn, Nb) account is a leading hypothesis, not settled fact. Modern metallurgists have reproduced wootz-like patterned steel, so the technique is not irrecoverable. And the “Damascus steel” sold today is pattern-welded steel — a different material entirely.
- **source:** JOM (TMS) · Verhoeven, Pendray & Dauksch, 1998 — https://www.tms.org/pubs/journals/JOM/9809/Verhoeven-9809.html

### The spread of global literacy
- **id/category/loss-type:** `literacy` / `threshold`
- **date plotted:** 1820 (range 1820 to 2024) · **region:** Global; unevenly
- **type:** proxy · **confidence:** medium
- **role in model:** Decoder access
- **SHOWS:** Shows the share of the population able to decode written text rising.
- **DOES NOT SHOW:** Literacy is not expertise, nor knowledge of method.
- **source:** Our World in Data · Literacy — https://ourworldindata.org/literacy

### The BBC Domesday Project laserdiscs
- **id/category/loss-type:** `domesday` / `digital` / `apparatus`
- **date plotted:** 1986 (range 1986 to 2011) · **region:** United Kingdom
- **type:** direct · **confidence:** high
- **role in model:** The reading apparatus dying before the medium
- **What survived:** The discs. They stayed physically sound.
- **What was lost:** The machine that read them. A 1986 national survey — some one million contributors, 200,000 photographs, video and maps — was bound to a BBC Micro plus a Philips LV-ROM player, and the player became commercially extinct.
- **SHOWS:** Shows an archive can close when the reading apparatus dies rather than the medium. Recovery required the CAMiLEON project's emulation work and deposit of the material at The National Archives (PRO 30/100).
- **DOES NOT SHOW:** The “digital Domesday lasted 15 years, not 1,000” headline overstates it: the data never actually became unreadable, working players and emulators recovered it, and it was republished as Domesday Reloaded in 2011. But recovery was expensive, the interactivity was only partly preserved, and the rescued material has had access gaps of its own since.
- **source:** The National Archives (UK) · catalogue record PRO 30/100 — https://beta.nationalarchives.gov.uk/catalogue/id/C16160

### The Web released for open use
- **id/category/loss-type:** `web` / `threshold`
- **date plotted:** 1993 (range 1989 to 1993) · **region:** The global network
- **type:** direct · **confidence:** high
- **role in model:** Search, linking and copying
- **SHOWS:** Reduced the cost of distribution and of making connections enormously.
- **DOES NOT SHOW:** Volume is not the same as accuracy or quality of context.
- **source:** CERN · A short history of the Web — https://home.cern/science/computing/birth-web/short-history-web

### Waking the Saturn V F-1 engine
- **id/category/loss-type:** `f1-engine` / `digital` / `tacit`
- **date plotted:** 2013 (range 2011 to 2013) · **region:** United States · Marshall Space Flight Center
- **type:** direct · **confidence:** high
- **role in model:** The documents survive, the ability to run them does not
- **What survived:** The original F-1 documentation. It was retrieved from the archive and used.
- **What was lost:** Tacit shop-floor knowledge: hand-brazed tube-wall welding, undocumented production deviations, the 1960s supplier and alloy base, and the analogue, obsolete formats the drawings sit in.
- **SHOWS:** Engineers had to physically tear the engine down, structured-light scan it, and hot-fire a restored gas generator for 30 seconds on 24 January 2013 — because the archived drawings alone were not a runnable decoder.
- **DOES NOT SHOW:** This is not a case of “NASA lost the blueprints”: the original documentation was found and used. What was missing was not the record but the capacity to re-execute it.
- **source:** NASA NTRS · Erin M. Betts, “Waking a Giant”, 2013 — https://ntrs.nasa.gov/citations/20140011656

### Vint Cerf's “digital vellum” warning
- **id/category/loss-type:** `cerf` / `digital`
- **date plotted:** 2015 (range 2015 to 2015) · **region:** United States · AAAS Annual Meeting, San Jose
- **type:** proxy · **confidence:** high
- **role in model:** A proposal to carry meaning along with the bits
- **SHOWS:** One of the architects of TCP/IP argued in a 13 February 2015 plenary that bit-level storage is insufficient, that preserving digital material for centuries requires carrying the semantics with the bits — an explicitly Rosetta-Stone-shaped proposal he called “Digital Vellum”.
- **DOES NOT SHOW:** This is an expert forecast and a design proposal, not evidence that a digital dark age has occurred. Institutional archiving and emulation have improved markedly since 2015; “digital dark age” is a rhetorical frame, not a measured quantity.
- **source:** AAAS 2015 Annual Meeting · V. G. Cerf, “Digital Vellum” — https://aaas.confex.com/aaas/2015/webprogram/Paper14064.html

### Link rot measured at web scale
- **id/category/loss-type:** `link-rot` / `digital` / `maintenance`
- **date plotted:** 2024 (range 2013 to 2024) · **region:** Global · the World Wide Web
- **type:** direct · **confidence:** high
- **role in model:** The archive closing when maintenance stops
- **SHOWS:** Pew's crawl-based study found 38% of webpages that existed in 2013 were inaccessible by October 2023 (8% for pages from 2023, 25% across the whole 2013-2023 span). 23% of news pages and 21% of government pages carry at least one broken link, and 54% of Wikipedia articles have a dead reference link.
- **DOES NOT SHOW:** These are availability measurements, not content-loss measurements — many “gone” pages survive in the Wayback Machine or at moved URLs. The sample is drawn from Common Crawl and is not a census of the web, and the study cannot say whether the vanished material had scholarly value.
- **source:** Pew Research Center · Chapekis, Bestvater, Remy & Rivero, 2024 — https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/

### Model collapse from recursively generated data
- **id/category/loss-type:** `model-collapse` / `digital`
- **date plotted:** 2024 (range 2023 to 2024) · **region:** United Kingdom and Canada
- **type:** direct · **confidence:** high
- **role in model:** The context term collapsing at machine scale
- **SHOWS:** Across large language models, variational autoencoders and Gaussian mixture models, training successive generations on the previous generation's output produced “model collapse”: the tails of the original distribution disappeared first, then the model converged on a low-variance caricature. The authors conclude that indiscriminate use of model-generated content causes “irreversible defects”.
- **DOES NOT SHOW:** The headline result comes from a regime where each generation's training data is largely replaced by synthetic output. Follow-up work shows that accumulating real alongside synthetic data, or filtering it, substantially slows or avoids collapse — so “the internet will inevitably poison AI” is not what this paper establishes.
- **source:** Nature · Shumailov, Shumaylov, Zhao, Papernot, Anderson & Gal, 2024 — https://www.nature.com/articles/s41586-024-07566-y

### Internet access and present inequality
- **id/category/loss-type:** `internet` / `threshold`
- **date plotted:** 2025 (range 2025 to 2025) · **region:** Global
- **type:** proxy · **confidence:** high
- **role in model:** Access and the spread of decoders
- **SHOWS:** Shows the broad access base of roughly 6 billion people online.
- **DOES NOT SHOW:** Quality of access, and the capacity to evaluate sources, are not evenly distributed.
- **source:** ITU · Facts and Figures 2025 — https://www.itu.int/itu-d/reports/statistics/2025/10/15/ff25-internet-use/


## 4. TAXONOMY OF LOSS (presented in the Method section)

Framing: The most common error here is to collapse six very different events into a single sentence: “the knowledge was lost.” These are distinct mechanisms and they call for distinct remedies.
- **Carrier loss** — The physical medium is destroyed or decays. The decoder may still be alive; there is simply nothing left to read. (example case: `maya-codices`)
- **Decoder loss** — The object survives intact, but the language, script or training chain that could read it runs out. (example case: `rongorongo`)
- **Tacit knowledge loss** — Both the document and the object survive; the manual skill, the shop-floor sequence and the supply chain that produced them do not. (example case: `f1-engine`)
- **Apparatus loss** — The medium is sound and the encoding known, but the machine or software that reads it goes commercially extinct. (example case: `domesday`)
- **Maintenance loss** — Nobody destroys anything. Nobody keeps copying, migrating and updating the links either. (example case: `link-rot`)
- **Deliberate non-recording** — Knowledge is deliberately not recorded in order to protect it; when the institution protecting it falls, the knowledge falls with it. (example case: `greek-fire`)

## 5. MYTH CORRECTIONS (the study explicitly corrects six popular claims, including its own examples)

### Claim labelled "common but wrong": "The Library of Alexandria burned in a fire and ancient knowledge was destroyed."
There is no direct evidence that a single catastrophic fire destroyed ancient knowledge. Bagnall's analysis shows the famous 500,000-roll figures are ancient rhetoric (plausibly an order of magnitude too high), and that Caesar's 48 BCE fire, the 391 CE Serapeum episode and the 642 CE Arab story are contested or fictional. The collection most likely dissolved through the ordinary decay of papyrus plus the end of the will to keep recopying it. A papyrus roll in Mediterranean humidity survives perhaps one to three centuries: what preserves a collection is maintenance, not fireproofing. This is why the case appears nowhere as a data point on this study's timeline.
Source: Roger S. Bagnall, “Alexandria: Library of Dreams”, Proc. Am. Phil. Soc. 146(4), 2002 — https://archive.nyu.edu/bitstream/2451/28263/2/D172-Alexandria%20Library%20of%20Dreams.pdf

### Claim labelled "common but wrong": "NASA lost the blueprints for the Saturn V."
False. The original F-1 documentation was retrieved and used in the 2011-2013 Marshall teardown. What had decayed was not the record but the capacity to re-execute it: tacit shop-floor knowledge such as hand-brazed tube-wall welding, the 1960s supplier and materials base, and the analogue or obsolete formats the drawings sit in. That is why engineers had to disassemble and 3D-scan a real engine. This does not weaken the argument — it strengthens it: even complete documentation is not, on its own, a runnable decoder.
Source: NASA NTRS · Erin M. Betts, “Waking a Giant: Bringing the Saturn F-1 Engine Back to Life”, 2013 — https://ntrs.nasa.gov/citations/20140011656

### Claim labelled "common but wrong": "The secret of Damascus steel was lost forever."
Overstated. The ore-exhaustion account resting on trace elements such as vanadium is a hypothesis, not proof. Modern metallurgists have reproduced wootz-like patterned steel in the laboratory. And the material sold as “Damascus steel” today is pattern-welded steel — visually similar, metallurgically different. The accurate statement is not “lost forever” but “the transmission chain broke, and rebuilding it took two centuries and modern analytical instruments.”
Source: JOM · Verhoeven, Pendray & Dauksch, 1998; Nature · Reibold et al., 2006 — https://www.tms.org/pubs/journals/JOM/9809/Verhoeven-9809.html

### Claim labelled "common but wrong": "The digital Domesday lasted only 15 years, not 1,000."
Striking but overstated. The data never actually became unreadable: surviving LV-ROM players and the CAMiLEON emulation effort recovered it, and it was republished in 2011. The real lesson is finer: it was the reading apparatus, not the medium, that went extinct — and recovery was expensive, delayed and only partial in its interactivity. The shape of the loss is not annihilation but unbudgeted recovery cost.
Source: The National Archives (UK) · PRO 30/100; DCC Digital Curation Manual — https://www.dcc.ac.uk/sites/default/files/documents/resource/curation-manual/chapters/preservation-strategies/preservation-strategies.pdf

### Claim labelled "common but wrong": "The internet is disappearing: 38% of pages are gone."
Half right. Pew's 38% measures live URL availability, not permanent loss of content; a large share of those pages still sit in the Wayback Machine or at moved addresses. The sample is drawn from Common Crawl and is not a census of the web. The accurate sentence is not “the internet is disappearing” but “live links decay, and an archive exists only as long as it is maintained.”
Source: Pew Research Center · “When Online Content Disappears”, 17 May 2024 — https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/

### Claim labelled "common but wrong": "As AI spreads across the internet it will inevitably poison itself."
This is not what the 2024 Nature paper establishes. Collapse was demonstrated in a regime where each generation's training data is largely replaced by synthetic output. Follow-up work finds that accumulating real data alongside synthetic data, rather than replacing it, or curating the synthetic portion, substantially mitigates the effect. The critical variable is not the technology itself but whether provenanced human-authored data continues to be maintained.
Source: Nature · Shumailov et al., 2024, 631:755-759 — https://www.nature.com/articles/s41586-024-07566-y


## 6. DIGITAL DARK AGE SECTION

Framing: The model's most contested claim is this: while the archive has grown as never before, the lifetime of the apparatus that opens it has shortened. The figures below are the measurable part of that claim.

Headline statistics presented:
- **38%** — Share of webpages that existed in 2013 and were no longer accessible by October 2023.
- **54%** — Share of Wikipedia articles carrying at least one dead reference link.
- **23%** — Share of news pages containing at least one broken link; for government pages it is 21%.
- **~70%** — Share of URLs suffering link and reference rot in the law journals sampled by Zittrain et al.; roughly 50% in U.S. Supreme Court opinions.

Caveat printed directly beneath them: Caveat: what Pew measured is availability, not permanent loss. A large share of those pages still sit in web archives. The accurate statement is not “the internet is disappearing” but “live links decay” and “an archive exists only as long as it is maintained.”

## 7. AI SECTION

Framing: Large language models sit simultaneously in the packaging link and the decoder link of the chain described here. This makes transmission cheaper, and at the same time produces a new form of loss.

As packager: the model reduces an enormous corpus to a compressed surface that can answer questions. This is the largest jump the G term — packaging gain — has ever seen.

As decoder: the model opens specialist text to someone without access to its language. This raises the qd term — decoder and access — and is the largest expansion of access since the two-century literacy curve in this study.

The name of the risk: a 2024 Nature paper shows that when each generation's training data is largely replaced by the previous generation's output, model collapse occurs. The tails of the distribution go first — the rare, the atypical, the minority — and then the model converges on a caricature of itself. This is precisely a collapse in this study's qc term: the packet keeps travelling, its diversity and its boundary knowledge do not.

What we are not claiming: this does not mean “AI will inevitably poison the internet.” Follow-up work in the same literature shows that accumulating real data alongside synthetic data, rather than replacing it, or curating the synthetic portion, substantially slows collapse. The critical variable is not the technology but whether provenanced human-authored data continues to be maintained — which is what this study has said from the start.

Closing callout: The symmetry: writing, print and the web also extended reach while thinning context. What is different about AI is not kind but speed and loop-closure time: a generation can now take months rather than a century.

## 8. SELF-DECLARED LIMITS

**"It can say":**
- That context need not grow at the same rate as the archive.
- That writing can extend range while initially keeping access narrow.
- That local institutional collapse can sever the decoder chain.
- That the types of loss are distinct mechanisms requiring distinct remedies.

**"It cannot say":**
- The real percentage of knowledge at any given date.
- Anything about human intelligence or civilisational superiority.
- A single global rate of progress.
- Whether any given loss was inevitable.

**Revision log shown to readers:**
- **v1** — was: The archive gap was being counted as context loss. → now: The types of loss were separated.
- **v2** — was: Input appeared to change quality. → now: Ratio and stock were separated.
- **v3** — was: Evidence and assumption were being conflated. → now: Evidence lanes were separated out.
- **v3.1** — was: The date lane was misaligned. → now: It was bound to a single x scale.
- **v4.0** — was: The argument had not been tested against its own counter-examples. → now: Loss cases, a taxonomy of loss and myth corrections were added.

## 9. FULL BIBLIOGRAPHY (29 entries)

**Archaeology and oral transmission**
- Blombos multi-stage processing — Science, 2011 — https://www.science.org/doi/10.1126/science.1211535
- Early symbolic marks — PNAS, 2020 — https://www.pnas.org/doi/10.1073/pnas.1910880117
- GunaiKurnai continuity — Nature Human Behaviour, 2024 — https://www.nature.com/articles/s41562-024-01912-w
- Preservation bias in archaeology — HSS Communications, 2020 — https://www.nature.com/articles/s41599-020-00635-3

**Writing, print and institutions**
- The origins of writing — Metropolitan Museum — https://www.metmuseum.org/essays/the-origins-of-writing
- The evolution of writing — University of Texas — https://sites.utexas.edu/dsb/tokens/the-evolution-of-writing/
- The history of East Asian printing — UNESCO Courier — https://courier.unesco.org/en/articles/200-years-gutenberg-master-printers-koryo
- The history of scientific publishing — Royal Society — https://royalsociety.org/journals/publishing-activities/publishing350/history-philosophical-transactions/

**Lost technologies and undeciphered scripts**
- Decoding the Antikythera mechanism — Nature · Freeth et al., 2006 — https://www.nature.com/articles/nature05357
- The Rosetta Stone — the decoder that survived — The British Museum · EA24, 196 BCE — https://www.britishmuseum.org/collection/object/Y_EA24
- Tacit knowledge and the uninvention of nuclear weapons — Am. J. Sociology · MacKenzie & Spinardi, 1995 — https://www.journals.uchicago.edu/doi/10.1086/230699
- Carbon nanotubes in a Damascus sabre — Nature · Reibold et al., 2006 — https://www.nature.com/articles/444286a
- Self-healing in Roman concrete — Science Advances / MIT News, 2023 — https://news.mit.edu/2023/roman-concrete-durability-lime-casts-0106
- Radiocarbon dating of the rongorongo tablets — Scientific Reports · Ferrara et al., 2024 — https://www.nature.com/articles/s41598-024-53063-7
- The Dresden Maya Codex — SLUB Dresden · Mscr.Dresd.R.310 — https://www.slub-dresden.de/en/explore/manuscripts/the-dresden-maya-codex
- Alexandria: Library of Dreams — Proc. Am. Phil. Soc. · Bagnall, 2002 — https://archive.nyu.edu/bitstream/2451/28263/2/D172-Alexandria%20Library%20of%20Dreams.pdf

**Networks and cumulative culture**
- Partially connected networks — PNAS, 2016 — https://www.pnas.org/doi/10.1073/pnas.1518798113
- Group size and accumulation — PNAS, 2019 — https://www.pnas.org/doi/10.1073/pnas.1811413116
- Fidelity in cultural transmission — Royal Society — https://pmc.ncbi.nlm.nih.gov/articles/PMC3385684/

**Digital preservation and AI**
- A short history of the Web — CERN — https://home.cern/science/computing/birth-web/short-history-web
- Internet access 2025 — ITU — https://www.itu.int/itu-d/reports/statistics/2025/10/15/ff25-internet-use/
- When online content disappears — Pew Research Center, 2024 — https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/
- Perma: link and reference rot in legal citations — Harvard Law Review Forum · Zittrain, Albert & Lessig, 2014 — https://harvardlawreview.org/wp-content/uploads/2014/03/forvol127_zittrain.pdf
- Digital Curation Manual: preservation strategies — Digital Curation Centre, 2007 — https://www.dcc.ac.uk/sites/default/files/documents/resource/curation-manual/chapters/preservation-strategies/preservation-strategies.pdf
- Digital preservation at the Library of Congress — Library of Congress — https://www.digitalpreservation.gov/
- Bringing the Saturn F-1 engine back to life — NASA NTRS · Betts, 2013 — https://ntrs.nasa.gov/citations/20140011656
- AI models collapse when trained on recursively generated data — Nature · Shumailov et al., 2024 — https://www.nature.com/articles/s41586-024-07566-y
- The world's capacity to store information — Science / PubMed — https://pubmed.ncbi.nlm.nih.gov/21310967/
- Generative AI risk profile — NIST — https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958388
