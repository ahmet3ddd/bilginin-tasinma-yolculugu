> **Bu belge hakkında / About this document**
>
> Bu dosya **Aktarım Zinciri / The Transmission Chain** çalışmasının çalışma
> belgelerinden biridir (yazar: Ahmet Çandöken · `ahmetoff`).
> İçindeki inceleme, **insan hakemliği değildir.** Altı ayrı uzmanlık çerçevesinden
> (arkeoloji · bilim ve teknoloji tarihi · nicel modelleme · dijital koruma ·
> bilim felsefesi · yayın bütünlüğü) **yapay zekâ modelleri tarafından yürütülen
> çekişmeli eleştiridir** ve hakemliğin yerine geçmez. Belgede birinci tekil şahıs
> kullanılması, insan bir incelemeci olduğu anlamına gelmez. Bulguların bir bölümü
> yorum değil aritmetiktir: eleştiri sitenin kendi kodunu çalıştırıp basılan
> formüllerle karşılaştırmıştır. Sorumluluk her hâlde yazara aittir.
>
> This file is one of the working documents of **The Transmission Chain**
> (author: Ahmet Çandöken · `ahmetoff`). The review it contains is **not human peer
> review.** It is **adversarial critique carried out by AI models** from six
> specialist framings (archaeology · history of science and technology ·
> quantitative modelling · digital preservation · philosophy of science ·
> publication integrity), and it is not a substitute for peer review. The use of the
> first person in this document does not indicate a human reviewer. Part of what it
> found is arithmetic rather than interpretation: the critique ran the site's own
> code against its printed formulas. Responsibility rests in every case with the author.
>
> Metin ve veri **CC BY 4.0** · kod **MIT** — bkz. `LICENSE`.

I read the packet in full and verified the historical claims against primary and secondary literature. Findings below, ordered by section, each with the quoted claim, the defect, severity, fix, and verification URL.

---

# Hostile review — historical portion of "The Transmission Chain" v4.0

## 1. The loss cases

### F1 — Antikythera: "no comparable second machine" is false

**(a) Claim:** *"No manual, no workshop tradition, no comparable second machine. Neither the teaching nor the making was transmitted."*

**(b) Wrong:** A second geared calendrical device survives: the Byzantine portable sundial-calendar of c. 500 CE (Field & Wright, *Annals of Science* 42, 1985), routinely described in the Antikythera literature as "the second oldest geared mechanism in existence." Al-Bīrūnī describes a geared calendrical instrument c. 1000 CE; the geared astrolabe of Muḥammad ibn Abī Bakr al-Iṣfahānī (1221/22) survives in Oxford. The specialist consensus is explicitly the *opposite* of your sentence: "the existence of two instruments, using similar technology for comparable purposes, both in an astronomical context, encourages us to believe in a continuing tradition." Textual evidence for a workshop tradition also exists — Cicero (*De Re Publica* I.14; *De Natura Deorum* II.88) describes planetary spheres by Archimedes and Posidonius. Your flagship case's "what was lost" pair is factually incorrect.

**(c) blocking**

**(d) Fix:** Delete "no comparable second machine" and "neither the teaching nor the making was transmitted." Replace with: "No manual and no second *Hellenistic* machine survives; simpler geared calendrical devices are attested in Byzantium c. 500 and in Islamic astronomy c. 1000–1222. The tradition attenuated and simplified; it did not vanish."

**(e)** https://www.tandfonline.com/doi/abs/10.1080/00033798500200131 · https://www.archaeology.wiki/blog/issue/geared-instruments-from-antiquity-to-the-present-day-a-continuous-tradition/

---

### F2 — Antikythera assigned loss-type `tacit` on no evidence

**(a) Claim:** `antikythera` / `loss` / **`tacit`**, "role in model: Applied astronomy left without a manual."

**(b) Wrong:** You concede in the same record that "its date, maker and workshop remain disputed." You therefore have no evidence whatever about what its makers could or could not articulate. Assigning `tacit` is an unevidenced psychological claim about dead artisans, and it is contradicted by your own "role in model" line, which describes a *documentation* absence, not a skill absence. The demonstrable loss here is carrier loss: every other such machine corroded, or was melted for bronze.

**(c) serious**

**(d) Fix:** Reassign to `carrier` (or to the new "never-recorded" category proposed in F26). State that the mechanism of loss is not determinable from a single object.

**(e)** https://www.nature.com/articles/nature05357

---

### F3 — Antikythera plotted date smuggles in a contested epoch date

**(a) Claim:** date plotted **-150** (range **-205** to -60).

**(b) Wrong:** −205 is Carman & Evans' *eclipse epoch* for the Saros dial. An epoch date is not a construction date; Alexander Jones (ISAW Papers 17, 2020) sets out why epoch dates need not coincide with manufacture. You correctly flag the dispute in the "DOES NOT SHOW" field and then quietly encode one side of it in the plotted geometry, where the caveat is invisible.

**(c) minor**

**(d) Fix:** Plot the shipwreck date (c. 70–60 BCE) as the only secure *terminus ante quem*; label the band "epoch date vs construction date, disputed."

**(e)** https://archive.nyu.edu/jspui/bitstream/2451/61000/2/Jones%202020%20Epoch%20dates%20of%20the%20Antikythera%20Mechanism%20ISAW%20Papers%2017.pdf

---

### F4 — Roman concrete: "the written procedure was lost" — you cannot lose a document that never existed

**(a) Claim:** *"What was lost: The written procedure. Vitruvius and Pliny describe Roman mixes but not this step; the recipe survived in the material, not in the text."*

**(b) Wrong:** This is a category error dressed as a finding. There is no evidence a written procedure for hot mixing ever existed. Absence of documentation is not loss of documentation. Vitruvius *does* give explicit mix ratios (1:3 lime:pozzolana for building, 1:2 for underwater work); the 2025 Pompeii study describes hot mixing as departing from Vitruvius and calls this "a knowledge gap in our understanding" — i.e. a modern gap, not an ancient deletion. This is the only "loss case" in your set whose lost object is a hypothesised document.

**(c) serious**

**(d) Fix:** Change to "never entered the surviving textual tradition." Note that this is a different phenomenon from loss and belongs in a category you do not have.

**(e)** https://www.nature.com/articles/s41467-025-66634-7 · https://en.wikipedia.org/wiki/Roman_concrete

---

### F5 — Roman concrete is not a loss case at all, and hot-mixed lime never stopped being used

**(a) Claim:** `roman-concrete` / **`loss`** / `tacit`; *"Roman building knowledge was interrupted, not wholly lost."*

**(b) Wrong:** Hot-mixed lime is not a lost technique. It is standard vernacular practice in British and continental building into the twentieth century and is a live conservation technique with its own practitioner literature and monographs (Copsey, *Hot Mixed Lime and Traditional Mortars*, 2019; "Traditional hot mixed lime mortars for conservation and repair," 2019). What lapsed was *imperial-scale pozzolanic marine concrete*, and it lapsed because the Mediterranean pozzolana supply chain and the fisc that paid for monumental building collapsed — not because anyone forgot how to slake lime hot. Your own hedge ("interrupted, not wholly lost") concedes the point and then leaves the case sitting in the `loss` category with a `tacit` tag, where it does argumentative work it has not earned.

**(c) blocking** (for the case set's integrity)

**(d) Fix:** Remove from the `loss` category. If retained, retag as demand/supply cessation (see F26) and state plainly that the technique has a continuous vernacular history.

**(e)** https://www.academia.edu/40884630/Traditional_hot_mixed_lime_mortars_for_conservation_and_repair

---

### F6 — Roman concrete: presented as contested where the literature has moved

**(a) Claim:** *"some researchers still read the clasts as relict under-burnt lime."*

**(b) Wrong:** With a stated data cut-off of 20 August 2026 you should have the 2025 *Nature Communications* study of an unfinished Pompeian construction site, which analyses lime clasts by FTIR, isotopic analysis, EDS mapping and Raman and explicitly rules out the relict-lime reading on morphological grounds ("distinct from the morphology of relict lime inclusions within poorly mixed slaked lime"), concluding "the common use of hot-mixing techniques." You are hedging in the direction of caution, which is the less damaging error — but you asked to be judged on whether contested/settled status is stated correctly, and here it is not.

**(c) minor**

**(d) Fix:** Cite the 2025 Pompeii paper; downgrade "still read" to "was read before 2025."

**(e)** https://www.nature.com/articles/s41467-025-66634-7

---

### F7 — Greek fire: *De Administrando Imperio* ch. 13 is imperial ideology, read here as administrative evidence

**(a) Claim:** *"In the handbook he wrote for his son, Constantine VII states that the secret of the 'liquid fire discharged through tubes' was revealed to the Byzantines alone and must never be divulged to foreigners"* → *"SHOWS: A documented case of a state deliberately refusing to write the decoder down."*

**(b) Wrong:** You have stripped the passage's genre. DAI ch. 13 says the fire was *revealed by an angel to Constantine the Great*, that it may be prepared only for Christians and only in the imperial city, and that an official who sold it to foreigners was struck down by "a flame from heaven" as he entered a church. It sits in a chapter of comparably fabricated prohibitions (on regalia, on imperial marriage to foreigners) whose function is deterrent legend, not records policy. Treating a hagiographic topos as documentary evidence of an information-security decision is exactly the source-criticism failure a study about "context travelling with the packet" should be immune to. Note also what your reading implies: if the secret was truly never written, DAI could not know it was a secret worth guarding.

**(c) serious**

**(d) Fix:** Quote the angel passage in full, label it as ideological, and change the SHOWS field to "a documented case of a state *claiming* exclusive divine possession of a secret." Drop "documented case of… refusing to write down."

**(e)** https://en.wikipedia.org/wiki/Greek_fire

---

### F8 — Greek fire: "No surviving text gives the actual composition" is overstated

**(a) Claim:** *"No surviving text gives the actual composition; every modern 'reconstruction' is inference from described effects."*

**(b) Wrong:** Several texts give partial composition and apparatus. Anna Komnene (*Alexiad* XIII.3) specifies resin from pine and evergreens mixed with sulphur, blown through reed tubes and ignited at the tip. The ninth-century Wolfenbüttel Latin manuscript names naphtha as the principal component and describes the furnace, copper vessel and bronze siphon. The *Praecepta Militaria* calls it "sticky fire," implying resin thickeners. What is missing is a *complete quantified recipe*, which is a much weaker and much more ordinary claim.

**(c) serious** — because the strong version is what makes the case rhetorically useful to you

**(d) Fix:** "No surviving text gives a complete recipe; several give partial compositional and apparatus descriptions (Anna Komnene, the Wolfenbüttel manuscript, *Praecepta Militaria*)."

**(e)** https://en.wikipedia.org/wiki/Greek_fire

---

### F9 — Greek fire: date range endpoint 1204 unsupported

**(a) Claim:** date plotted 950, **range 672 to 1204**.

**(b) Wrong:** Last securely attested combat use is twelfth century (1099 against the Pisans). 1203 is unconfirmed and 1204 appears to be the sack of Constantinople standing in for a use-date. You are encoding "it lasted until the Empire fell" as data.

**(c) minor**

**(d) Fix:** 672 – c. 1110, with a note that disuse predates 1204 by roughly a century — which, incidentally, weakens the "secrecy killed it" reading.

**(e)** https://en.wikipedia.org/wiki/Greek_fire

---

### F10 — Linear B: the Cypriot counter-case is omitted, and it is decisive

**(a) Claim:** *"What was lost: The scribal class that read them and the palace institution that made them meaningful. The tablets stayed silent for 3,000 years."*

**(b) Wrong by omission:** Aegean syllabic writing did not die in the Bronze Age collapse. The Cypriot syllabary — descended via Cypro-Minoan from the same Linear A root — was in continuous use on Cyprus from roughly the eleventh century BCE to the fourth (with traces to the first century BCE), straight through the collapse that killed Linear B. That means the Mycenaean case does not show that scripts are fragile; it shows that a script tied to a *single institutional function* (palace redistributive accounting) dies with that institution while a cousin script tied to broader use survives. This is the most interesting fact available about your case and you have left it out. It is simultaneously your best evidence (institutions, not media, carry decoders) and your worst (transmission worked next door).

Separately: "stayed silent for 3,000 years" silently merges two different silences — the tablets were *undiscovered* until Evans at Knossos in 1900, so for most of that span nobody was failing to read them; they were not available to read.

**(c) serious**

**(d) Fix:** Add the Cypriot syllabary explicitly to the "what was lost" analysis. Distinguish buried-and-unknown from extant-and-unreadable.

**(e)** https://en.wikipedia.org/wiki/Cypriot_syllabary

---

### F11 — Linear B: dates and source

**(a) Claim:** date plotted **-1200** (range -1250 to -1100); source: British Museum *Mycenaean world* gallery page; **confidence: high**.

**(b) Wrong:** The Knossos corpus is conventionally dated c. 1400–1375 BCE, the mainland (Pylos, Thebes) c. 1200. Your band excludes Knossos entirely. And a museum gallery landing page is not a source capable of supporting `confidence: high` on a dating claim.

**(c) minor**

**(d) Fix:** Split Knossos and Pylos, or widen to −1400/−1180. Cite Chadwick or the Cambridge decipherment paper.

**(e)** https://www.britannica.com/topic/Linear-B · https://www.classics.cam.ac.uk/system/files/documents/process.pdf

---

### F12 — rongorongo: "within a generation of contact" is off by 140 years

**(a) Claim:** *"Within a generation of contact no readers remained."*

**(b) Wrong:** First European contact was Roggeveen in 1722. Readers survived for roughly five to six generations after that. The literate class was destroyed by the Peruvian slave raids of 1862–63 and the smallpox epidemics that followed, which reduced the population to under 200 by the 1870s — precisely because "literacy was a privilege of the ruling families and priests who were all kidnapped in the Peruvian slaving raids or died soon afterward in the resulting epidemics." This is not a pedantic date fix: it changes the mechanism from "contact dissolves indigenous knowledge" (a diffusionist cliché) to "a targeted demographic catastrophe removed a small specialist class" (your actual thesis, and a better one).

**(c) serious**

**(d) Fix:** "Within a generation of the 1862–63 slave raids and the subsequent epidemics, no readers remained."

**(e)** https://en.wikipedia.org/wiki/Rongorongo

---

### F13 — rongorongo: the radiocarbon result is compressed into a misleading range

**(a) Claim:** *"Direct radiocarbon dating of four Rome-held tablets returned wood ages from 1493-1509 to 1832-1887."*

**(b) Wrong:** Only **one** of the four gave a fifteenth-century date. Ferrara et al. 2024 report: Tablet D (Échancrée) 1493–1509 (68.3%); Tablet C (Mamari) 1694–1727; Tablet B (Aruku Kurenga) 1832–1857; Tablet A (Tahua) 1862–1887. Presented as a "range from…to…", your sentence implies a distribution spanning four centuries. It is three modern samples and a single outlier — which is exactly why the pre-contact-invention claim is fragile, and why the authors hedge with driftwood and reuse. Your own caveat field says the right thing; the summary sentence above it does not.

**(c) serious**

**(d) Fix:** List the four dates individually. State that the pre-contact claim rests on n = 1.

**(e)** https://www.nature.com/articles/s41598-024-53063-7

---

### F14 — rongorongo: object count

**(a) Claim:** *"About twenty-five inscribed wooden objects."*

**(b) Wrong:** Your own cited paper says "approximately twenty-seven wooden objects"; the standard count is 26 texts, of which only about half are of unquestioned authenticity — a caveat that matters more than the exact number.

**(c) minor**

**(d) Fix:** "About 26, of which roughly half are beyond doubt as to authenticity."

**(e)** https://www.nature.com/articles/s41598-024-53063-7

---

### F15 — Maya codices: the "disputed fourth" has been accepted for a decade

**(a) Claim:** *"Three securely accepted screenfold codices worldwide — the Dresden among them — plus a disputed fourth."*

**(b) Wrong:** The Grolier Codex was argued authentic in the 2016 study by Coe, Gallenkamp, Houston, Milbrath and Taube, and formally declared authentic by Mexico's INAH in 2018, when it was renamed the *Códice Maya de México*. It is now generally described as the oldest surviving book of the Americas. With a 2026 cut-off, "disputed fourth" is a decade out of date, and the error runs in the direction that inflates your loss figure.

**(c) serious**

**(d) Fix:** "Four accepted codices — Dresden, Madrid, Paris and the *Códice Maya de México* (formerly Grolier), authenticated 2016–2018."

**(e)** https://www.mesoweb.com/articles/Coe_etal/Fourth_Codex.pdf · https://www.brown.edu/news/2016-09-07/mayacodex

---

### F16 — Maya codices: "three orders of magnitude" contradicts your own caveat in the same record

**(a) Claim:** *"The physical carrier was reduced by roughly three orders of magnitude in one colonial generation"* — three sentences before *"the true volume is unknowable."*

**(b) Wrong:** These cannot both stand. A 1,000× reduction requires knowing the denominator, which you have just declared unknowable. There is no derivation offered. This is precision theatre.

**(c) serious**

**(d) Fix:** Delete the quantification. "Almost the whole of a literate book tradition, of unknown but certainly large extent."

**(e)** https://sacred-texts.com/nam/maya/ybac/index.htm

---

### F17 — Maya codices: `carrier` assignment hides a compound loss

**(a) Claim:** `maya-codices` / `loss` / **`carrier`**; *"lost by destroying the carrier while the decoder was still alive."*

**(b) Wrong:** Half-true and it conceals the more interesting fact. Glyphic literacy also died — the last independent Maya polity fell at Nojpetén in 1697, and the twentieth-century decipherment problem existed precisely *because* both the carrier and the decoder had gone. This is a compound carrier + decoder case, which contradicts your claim that the six categories are "distinct mechanisms."

**(c) serious**

**(d) Fix:** Assign both. See F27 on exclusivity.

**(e)** https://www.slub-dresden.de/en/explore/manuscripts/the-dresden-maya-codex

---

### F18 — Wootz: three factual errors in one sentence, and it is the sentence the case rests on

**(a) Claim:** *"Production stops around 1750 even though smiths, forges and demand persisted."*

**(b) Wrong, three times:**

1. **"Production stops around 1750"** misreads your own cited source. Verhoeven, Pendray & Dauksch write: *"The date of the last blades produced with the highest-quality damascene patterns is uncertain, but is probably around 1750; it is unlikely that blades displaying low-quality damascene patterns were produced later than the early 19th century."* That is a statement about *pattern quality in collectable blades*, not about production. You have silently converted a connoisseurship boundary into an industrial one.
2. **Wootz ingot production in South India continued through the nineteenth century.** Buchanan-Hamilton observed working crucible furnaces in Mysore and Salem in 1807; Wood recorded the crucible process in Tamil Nadu in 1893; production is attested as late as c. 1900.
3. **"Demand persisted" is the reverse of the truth.** Sword demand collapsed with firearms; cheap Sheffield crucible steel undercut the Indian product; and the colonial state actively suppressed the industry, prohibiting Indian steel production in 1866 nominally for forest conservation, with a licensing regime that left only "a few of the best makers" able to work.

**(c) blocking**

**(d) Fix:** Rewrite the record entirely. The accurate statement is: the highest-quality patterned blades cease c. 1750; patterned production tails off into the early nineteenth century; the crucible steel industry itself is undercut and then legally suppressed under colonial rule and dies in the later nineteenth century. Then ask whether that belongs in a study about transmission chains at all.

**(e)** https://www.tms.org/pubs/journals/JOM/9809/Verhoeven-9809.html · https://student-journals.ucl.ac.uk/pia/article/164/galley/241/view/ · https://www.tf.uni-kiel.de/matwis/amat/iss/kap_b/articles/2017_alter_stephan_truth_damascus_steel.pdf

---

### F19 — Wootz: a hypothesis is stated as the finding and disclaimed only in the footnote

**(a) Claim:** SHOWS field: *"Shows a technique halting silently when it depends on an input its practitioners were never aware of."* DOES NOT SHOW field: *"The ore-exhaustion / trace-element account is a leading hypothesis, not settled fact."*

**(b) Wrong:** You cannot make a hypothesis the headline of the case and then retract it in the caveat. The SHOWS field is what the reader takes away and what the model's `tacit` tag encodes. As written, the study asserts the thing it denies asserting. This is the single clearest instance in the packet of the caveat-as-inoculation pattern.

**(c) serious**

**(d) Fix:** Move the conditional into the SHOWS field: "*If* the trace-element account holds, this would show…"

**(e)** https://www.tms.org/pubs/journals/JOM/9809/Verhoeven-9809.html

---

### F20 — Wootz: `tacit` contradicts your own glossary

**(a) Claim:** `wootz` / `loss` / **`tacit`**. Glossary: *"Tacit knowledge — Embodied, intuitive skill that cannot be fully written down."*

**(b) Wrong:** Your preferred causal story is that vanadium at 40 ppmw in particular ore bodies did the work. That is a *materials-supply* constraint. It is the explicit negation of a tacit-skill constraint: the trace-element hypothesis says the smiths' embodied skill was intact and the *feedstock* changed. Your own model has no term for feedstock, so the case has been forced into the nearest available box.

**(c) serious**

**(d) Fix:** New category (F26a). Do not use `tacit` for a case whose stated cause is chemistry in the ground.

**(e)** https://www.tms.org/pubs/journals/JOM/9809/Verhoeven-9809.html

---

## 2. The transmission-threshold cases

### F21 — Printing: a `direct` / `high` record for a book that does not exist

**(a) Claim:** `printing`, date plotted **1234**, **type: direct**, **confidence: high**.

**(b) Wrong:** 1234 refers to the *Sangjeong Gogeum Yemun*, of which no copy survives; the date is known from Yi Gyubo's later colophon. The oldest *extant* metal-type-printed book is the *Jikji* (1377). A dating claim that rests on a lost book, attested only in a later text, is by definition not "direct material record, high confidence" — it is the textbook definition of your own `proxy` tag. This matters because your evidence-lane distinction (direct vs proxy) is one of the study's stated methodological achievements (revision log v3).

**(c) serious**

**(d) Fix:** Plot 1377 (*Jikji*) as `direct`; plot 1234 separately as `proxy`, attested-but-lost.

**(e)** https://www.guinnessworldrecords.com/world-records/689333-oldest-book-printed-using-movable-metal-type

---

### F22 — Printing: the record that refuses a single civilisational line has no Chinese anchor in it

**(a) Claim:** region *"China, Korea and Europe"*; range **751 to 1455**; *"DOES NOT SHOW: It cannot be reduced to a single inventor or a single civilisational line."* Source: a UNESCO *Courier* popular article about Koryŏ printers.

**(b) Wrong:** Not one of your three anchor dates is Chinese. 751 is the Korean *Mugujeonggwang* dhāraṇī (and is *woodblock*, a different technology from the movable type at 1234 and 1455 — the range silently merges two technologies). Bi Sheng's ceramic movable type (c. 1040s, described by Shen Kuo in the *Dream Pool Essays*) and Wang Zhen's wooden type (1298) are absent, as is the entire Chinese woodblock canon, which is by orders of magnitude the largest pre-modern printing tradition on earth. The net effect is a record that announces its resistance to a single civilisational line and then supplies one, with Korea substituted for Europe. That is not de-centring; it is relocating the centre.

**(c) serious**

**(d) Fix:** Split woodblock from movable type into separate records. Add Bi Sheng (c. 1040s) and the Chinese woodblock corpus. Replace the *Courier* piece with a scholarly source.

**(e)** https://tricycle.org/magazine/buddhist-history-moveable-type/

---

### F23 — The journal: the peer-review myth is left standing, in a study whose job is myth-correction

**(a) Claim:** Record title *"The scientific journal **and peer review**"*, date 1665; DOES NOT SHOW field says only *"It does not mean science began in 1665."*

**(b) Wrong:** Peer review is not a 1665 institution and the claim that it is may be the single most-repeated false date in the history of science. *Philosophical Transactions* was Oldenburg's private commercial venture; the Royal Society took editorial control and created a Committee of Papers only in **1752**; independently written referee reports informing that committee begin in the **1820s–1832**; the *term* "peer review" is not attested until **1967** and becomes common only in the 1970s; *Nature* had no systematic external refereeing until 1973. You correct six myths, including several that are less widely believed than this one, and this one you print in a record title.

Compounding it: your sole source is the Royal Society's own 350th-anniversary house history — an interested party on precisely the question of its own priority.

**(c) serious**

**(d) Fix:** Retitle the record "The scientific journal." Add a seventh myth-correction: "Peer review did not begin in 1665." Cite Fyfe/Moxham/Baldwin, not the Royal Society's marketing.

**(e)** https://www.timeshighereducation.com/peer-review-not-as-old-as-you-might-think · https://www.cambridge.org/core/journals/historical-journal/article/royal-society-and-the-prehistory-of-peer-review-16651965/93B903FD4D6561AA7224C62EE57B0C18

---

### F24 — The journal: 1665 anchored on the wrong journal

**(a) Claim:** date plotted **1665**, sourced to *Philosophical Transactions*.

**(b) Wrong:** The *Journal des sçavans* first appeared 5 January 1665, two months before *Philosophical Transactions* (6 March 1665). If you are going to pick a single European founding date, pick the earlier one, or state that the priority question is itself contested and depends on what counts as a scientific journal.

**(c) minor**

**(d) Fix:** Cite both; note the definitional dispute.

**(e)** https://blog.scielo.org/en/2015/03/05/350-years-of-scientific-publication-from-the-journal-des-scavans-and-philosophical-transactions-to-scielo/

---

### F25 — Mesopotamian writing: a contested origin thesis presented as settled, and three independent origins omitted

**(a) Claim:** *"SHOWS: Shows an economic record turning into a durable sign system."* Bibliography cites Schmandt-Besserat's token-origin site alongside the Met essay.

**(b) Wrong, two ways:**

1. The token → bulla → tablet account is a specific and heavily contested thesis, not a background fact. It has drawn sustained criticism (Zimansky's review; Englund's work on proto-cuneiform accounting; and the *Cambridge Archaeological Journal* reassessment arguing the "tokens" are multifunctional utilitarian objects rather than an accounting system). You present the conclusion without the controversy.
2. Writing has at minimum three, probably four, independent origins: Mesopotamia (c. 3400–3200), Egypt (Abydos, c. 3250 — effectively simultaneous, and the priority question is open), China (oracle bone, c. 1250, independent), and Mesoamerica (independent). Your timeline has exactly one writing threshold and it is Mesopotamian. Your printing record explicitly insists a technology "cannot be reduced to a single… civilisational line"; you do not apply that standard to writing. An inconsistent standard applied in the direction of Near-Eastern-then-European priority is a diffusionist structure whatever the author's intention.

**(c) serious**

**(d) Fix:** Hedge the token thesis and cite the critique. Either add the independent origins as separate records, or relabel −3200 "the earliest securely attested durable sign system," not "writing."

**(e)** https://www.cambridge.org/core/journals/cambridge-archaeological-journal/article/abs/reconsidering-tokens-the-neolithic-origins-of-accounting-or-multifunctional-utilitarian-tools/7E6C04CB040AD8AA0EA84B94D4D275C4

---

### F26 — Nalanda: founding date wrong, and the destruction myth is implied but not corrected — while the European equivalent gets a full debunking

**(a) Claim:** `nalanda`, date plotted 600, **range 450 to 1200**, category `threshold`, no loss framing; DOES NOT SHOW: *"It was not a single, uninterrupted global network."*

**(b) Wrong, three ways:**

1. Nalanda was founded c. **427 CE** under Kumāragupta I, evidenced by seals and numismatics. Your range opens at 450.
2. The range closes silently at **1200**, which encodes the Bakhtiyār Khaljī destruction narrative without stating it and therefore without correcting it. Modern scholarship rejects the popular version: the archaeology shows gradual decline with new buildings raised over old and fire damage on at least one occasion rather than a single catastrophe; teaching and students continued into the thirteenth century; Tibetan sources record survivors and a visitor c. 1235 finding the site damaged and deserted but with scholars still present. The "burned for months, nine million books" story is folklore with the same evidentiary status as the Alexandria story you spend a full myth-correction demolishing.
3. Structurally, this is the most consequential Eurocentrism in the packet. You debunk the *European* library-destruction myth at length and leave the *South Asian* one not merely uncorrected but silently encoded in your date range. A reader finishes the study believing Alexandria is a myth and Nalanda is a fact. That asymmetry is not neutral.

**(c) serious**

**(d) Fix:** Correct the founding to 427. Extend the range past 1200. Add a Nalanda myth-correction with the same rigour as the Alexandria one.

**(e)** https://en.wikipedia.org/wiki/Nalanda_mahavihara

---

### F27 — Domesday: figures and the "physically sound" claim

**(a) Claim:** *"some one million contributors, 200,000 photographs"*; *"What survived: The discs. They stayed physically sound."*

**(b) Partly wrong:** The contributor figure checks out (>1 million people, >9,000 schools). The image figure is inflated relative to the documented Community Disc content (~25,000 images) unless you are counting all media across both discs — say which, and cite it. More importantly, "they stayed physically sound" is stated as fact when laserdisc oxidation ("laser rot") is a documented failure mode of the format; you have no basis for a blanket soundness claim about a 1986 LV-ROM pressing, and the claim is load-bearing for the apparatus-vs-medium distinction the case exists to make.

**(c) minor**

**(d) Fix:** Source the 200,000. Change to "the surviving discs read successfully when players were located."

**(e)** https://en.wikipedia.org/wiki/BBC_Domesday_Project

---

### F28 — Domesday: the second loss is undated and it is the better story

**(a) Claim:** *"republished as Domesday Reloaded in 2011… the rescued material has had access gaps of its own since."*

**(b) Weak:** Domesday Reloaded went online in May 2011 and was **taken offline in June 2018**, with copies subsequently at the National Archives. Naming that date turns a vague hedge into a clean second data point: the rescue itself rotted in seven years. You have the strongest version of your own argument here and you have blurred it.

**(c) minor**

**(d) Fix:** Give the June 2018 date.

**(e)** https://en.wikipedia.org/wiki/BBC_Domesday_Project

---

### Claims that check out (recorded so the negative findings are legible as targeted, not blanket)

F-1 gas generator: 30-second hot fire, 24 January 2013, Marshall Test Stand 116 — **correct** (https://www.nasa.gov/centers/marshall/about/star/star130130.html). Cerf "Digital Vellum," AAAS Annual Meeting, San Jose, 13 February 2015 — **correct** (https://aaas.confex.com/aaas/2015/webprogram/Paper14064.html). Pew figures 38% / 8% / 25% / 23% / 21% / 54%, Common Crawl sample, October 2023 — **all correct** (https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/). PRO 30/100 = "Data from BBC Domesday Project," 1984–1986 — **correct** (https://beta.nationalarchives.gov.uk/catalogue/id/C16160). ITU ~6 billion online, 2025 — **correct** (https://www.itu.int/en/mediacentre/Pages/PR-2025-11-17-Facts-and-Figures.aspx). Bagnall's argument as summarised — **correct** (https://archive.nyu.edu/bitstream/2451/28263/2/D172-Alexandria%20Library%20of%20Dreams.pdf), except that the "one to three centuries" papyrus survival figure is your gloss, not his; he argues from Tiberius-era usability. Roman concrete two-week crack healing and "previously disregarded as sloppy mixing" — **correct** (https://news.mit.edu/2023/roman-concrete-durability-lime-casts-0106).

The pattern is unmistakable: **your post-1900 material is accurate and your pre-modern material is not.** The study's authority is being borrowed from the digital section and spent in the ancient one.

---

## 3. The framing

### F29 — You are reproducing the "lost technology" genre while auditing it

**(a) Claim:** *"When the key is lost, the result can survive while the knowledge becomes impossible to reproduce."* And: *"we hold the Antikythera mechanism but not its manual; the Damascus blade survives but not its recipe."*

**(b) Wrong:** That artifact/recipe couplet *is* the load-bearing structure of the popular lost-technology genre — the one that runs from *Chariots of the Gods* through every "10 lost technologies science can't explain" listicle. The scholarly critique you have to answer has three parts and you engage none of them:

1. **Technologies are abandoned, not lost.** Edgerton's use-centred history of technology (*The Shock of the Old*) shows that apparent disappearance is nearly always substitution under changed prices, demand, materials or politics. Your own cases confirm this: firearms displaced swords, the imperial fisc stopped funding concrete domes, the British prohibited Indian steel-making. "Loss" is what abandonment looks like from the artifact's point of view.
2. **"Recipe" is a modern category retrojected onto craft.** Pre-industrial craft did not organise itself around written procedures. Saying "the recipe was lost" usually means "no document of the kind we would now want ever existed." Your Roman concrete case is exactly this (F4) and you do not notice.
3. **The artifact/recipe asymmetry is manufactured by preservation, not by history.** Bronze, stone and fired clay survive; papyrus, wood, workshops, apprentices, ore bodies and market conditions do not. You will *always* find that the object outlasted the knowledge, in every period, for every technology, because that is what taphonomy does. You cite the preservation-bias literature in your bibliography (*HSS Communications* 2020) and then construct seven cases out of precisely the bias that paper describes — and your on-chart callout ("the archaeological record is not lived culture itself but a small, preserved and interpreted sample") states the objection and then does nothing with it.

**(c) blocking**

**(d) Fix:** Promote the abandonment/loss distinction from footnote to thesis. Re-sort every case against it. Then ask honestly what survives of the argument.

**(e)** https://en.wikipedia.org/wiki/The_Shock_of_the_Old

---

### F30 — The myth-corrections inoculate; they do not revise

**(a) Claim:** Six myth-corrections, of which the NASA one closes: *"This does not weaken the argument — it strengthens it."*

**(b) Wrong:** Examine what the corrections are permitted to cost you. Alexandria — corrected, but it was already excluded from the dataset, so the correction costs nothing. NASA blueprints — corrected, then the corrected version is explicitly recruited to *strengthen* the thesis. Damascus — corrected to "the transmission chain broke and rebuilding took two centuries," which preserves the frame intact while conceding every fact that should dissolve it. Domesday, Pew, model collapse — all corrected in ways that leave the model's parameters, case set and conclusion untouched.

**Not one correction removes a case, changes a preset, or alters the conclusion.** A revision process in which every correction terminates in re-affirmation is not a revision process. It is a credibility-purchasing mechanism: the reader sees six debunkings, credits the author with rigour, and extends that credit to the twenty-three claims that were *not* audited. The corrections function as an inoculation against exactly the critique they appear to invite.

The tell is the Damascus correction. If, as you concede, the chain broke for reasons your own model cannot represent (ore chemistry, colonial prohibition, firearms), then the honest response is not "rebuilding took two centuries" — it is to remove the case or to redefine the study's subject. You reached for the first and did not consider the second.

**(c) blocking**

**(d) Fix:** For each myth-correction, state explicitly what it costs the argument. If the answer is "nothing," the correction is decorative and should be labelled as background rather than as self-criticism.

---

### F31 — The presets are where the history actually lives, and they are indefensible in both directions

**(a) Claim:** *Oral culture* `qc: 0.96, qd: 0.5`; *After writing* `qc: 0.66, qd: 0.3`; *Digital age* `qc: 0.52`. Disclaimer: *"The presets are not historical measurements but debatable readings."*

**(b) Wrong:**

- **qc = 0.96 for oral culture** asserts that oral transmission carries method, evidence, error history and limits of validity *better than print* (0.84) and nearly twice as well as the digital present. This is romantic primitivism with a decimal point. It is also in tension with the cultural-transmission literature you cite in your own bibliography on copying fidelity and content drift.
- **qd = 0.5 for oral culture** is incoherent with your own glossary, which defines qd as "the share and quality of people who can open the packet." In a wholly oral culture that share is close to 1 within the speech community and 0 outside it — which is equally true of a written text in an unread language. You need to pick a reference population (community or species) and apply it consistently; as written, oral culture is penalised on a criterion that print is not.
- **qd = 0.3 for "After writing", *below* oral culture's 0.5,** asserts that the invention of writing *reduced* decoder access. Under any consistent reading of your own definition this is false: writing added a channel; it did not close the spoken one.
- **The disclaimer does not discharge the problem.** The presets are not decoration around the argument; they are the mechanism by which the argument is generated. Saying "these are debatable readings" while making them the sole input to the historical claim is having it both ways.

**(c) blocking**

**(d) Fix:** Either derive the presets from something, or delete them and make the historical argument in prose where it can be challenged.

---

### F32 — The historical index makes a spectacular claim in total silence

**(a) Claim:** Index R (reproducible): **−9974: R = 12** → **−8000: R = 7** → **−3200: R = 4**.

**(b) Wrong, or at minimum unargued:** Your index asserts that literate Uruk was **one third** as able to reproduce its knowledge as Upper Palaeolithic foragers, and that the invention of writing roughly *halved* reproducibility, which then took until c. 1455 CE to recover to the pre-agricultural level (R = 21 at 1455 vs R = 12 at −9974 — so recovery arrives only with print, 12,000 years later).

That is a large, striking, genuinely contestable thesis about the history of knowledge. It is nowhere stated in prose, nowhere argued, and nowhere defended. It is a numerical by-product of setting the "After writing" preset's qd to 0.3 (see F31). A reader who reads only the text will never encounter it; a reader who reads only the chart will absorb it as a finding.

**(c) blocking**

**(d) Fix:** Either state and defend the claim explicitly — it is the most interesting thing in the study — or fix the index so it does not assert something you have not argued.

---

### F33 — The published formulas do not describe the code the chart runs

**(a) Claim:** *"C = P × q_c ; R = C × q_d"*.

**(b) Wrong:** The simulation computes `contextual = Math.min(archive, contextual * retention * p.qc + recorded * .85)` — a decaying stock with an unexplained 0.85 coefficient, not a product of P and qc. And `rebuilt = selected * (contextual/archive) * p.qd` — i.e. R = *selected* × (C/P) × qd, not C × qd. There are three unexplained magic constants (0.85 "passes verification", 0.9 "actually recorded", and a second 0.85 in the contextual line that is never mentioned in the prose at all). The reader is given a model they cannot reconstruct from the description, and the historical presets are fed into it.

**(c) serious** (transparency; bears directly on whether the historical claims are checkable)

**(d) Fix:** Publish the equations the code implements, or change the code to implement the published equations. Justify or remove the three constants.

---

## 4. Is "loss" the right word?

### F34 — The study conflates "nobody makes this any more" with "the knowledge was lost", and its model has no term for the difference

**(a) Claim:** The framing sentence for the taxonomy: *"The most common error here is to collapse six very different events into a single sentence: 'the knowledge was lost.'"*

**(b) Wrong — and this is the most serious conceptual problem in the packet:** You correctly identify the collapsing error and then commit a version of it. For wootz (F18, F20), Roman concrete (F5), and arguably Greek fire (F8, F9), the historically attested proximate causes are **inputs, demand, and coercive political economy**: ore chemistry, the collapse of the pozzolana supply and the fisc, the substitution of firearms for swords, Sheffield steel undercutting Indian steel, and the 1866 colonial prohibition.

Your model contains K, G, qc, qd, innovation and half-life. **Not one of these represents raw-material supply, market demand, price, or state coercion.** So the model is structurally incapable of representing the actual cause of three of your seven loss cases — and because it is the only lens you offer, those three cases have been read as transmission failures purely because transmission failure is the only explanation the instrument can express. That is not evidence supporting the model; it is the model determining what the evidence is allowed to say.

**(c) blocking**

**(d) Fix:** Three honest options. (i) Add a supply/demand/coercion term and re-derive. (ii) Remove the three cases and narrow the claim. (iii) Redefine the study's subject as *reproducibility conditional on the will and the means to reproduce* — which is a real and defensible subject, and would make wootz an explicit out-of-scope example rather than a headline one.

**(e)** https://www.tf.uni-kiel.de/matwis/amat/iss/kap_b/articles/2017_alter_stephan_truth_damascus_steel.pdf

---

### F35 — No criterion for "lost" is ever stated, and under any strict criterion five of the seven cases are not losses

**(a) Claim:** The set is labelled `loss` throughout; the Damascus correction settles on *"the transmission chain broke, and rebuilding it took two centuries and modern analytical instruments."*

**(b) Wrong:** You never define lost. Candidate criteria: (a) no living person can perform it; (b) no living person could perform it even if they tried; (c) it cannot be recovered from the surviving record; (d) it cannot be recovered at all. Apply them:

| Case | Status now |
|---|---|
| Antikythera | Working reconstructions exist |
| Roman concrete / hot mixing | Reproduced in lab 2023; continuous vernacular practice anyway |
| Linear B | Read since 1952 |
| Maya codices | Read since Knorozov |
| Wootz | Reproduced by Verhoeven & Pendray, museum-quality, matching microstructure |
| rongorongo | Genuinely undeciphered |
| Greek fire | Genuinely unrecovered as a specific formulation |

Under criterion (d), **five of your seven "losses" are delays, not losses** — and one of the two survivors (Greek fire) may never have been a single formulation at all, as you concede. What you are actually measuring across the set is **recovery cost and recovery latency**, and you get within one sentence of saying so in the Domesday correction: *"The shape of the loss is not annihilation but unbudgeted recovery cost."* That is the study's best sentence. You wrote it, applied it to one case, and did not generalise it.

**(c) blocking**

**(d) Fix:** Define the criterion in the Method section. Then reframe the whole loss set around recovery cost/latency — which is falsifiable, quantifiable, and does not require the romantic vocabulary of loss. This single change would fix F29, F30, F34 and F35 together.

---

## 5. Selection bias

### F36 — The evidence is selected on the dependent variable and the study never admits it

**(a) Claim:** Self-declared limits, *"It cannot say"*: the real percentage of knowledge at any date; anything about intelligence or civilisational superiority; a single global rate of progress; whether any given loss was inevitable.

**(b) Wrong by omission:** Four limits are declared and the governing one is missing: **the cases were chosen because of their outcomes.** Seven loss cases were selected *because* something was lost; the threshold cases *because* transmission worked. There is no sampling frame, no denominator, no counterfactual, and no criterion for inclusion stated anywhere in the packet.

The consequence is specific and fatal to a specific sentence. Your q_c slider text asserts to the reader: *"Low values are the historical norm."* You cannot know that from this dataset. Nothing about frequency, base rates, or what is "normal" is derivable from a set assembled by looking for instances of the outcome. The same applies to the hero lead ("When the key is lost, the result can survive…") and to the digital-age preset's qc = 0.52, which encodes a frequency claim about the present.

**(c) blocking**

**(d) Fix:** Add to "It cannot say": *"How often transmission succeeds or fails, or which mechanisms are common — the cases are selected on the outcome and the study has no denominator."* Then delete "low values are the historical norm."

---

### F37 — The counter-evidence is enormous, and the single best case against you is also the best case *for* you

**(a) Claim:** *"Oral culture — halfLife: 10"* (half the records inaccessible within 10 generations) and the case set's absence of any transmission-success case with the same analytic apparatus.

**(b) Wrong:** The successes vastly outnumber the failures and several bear directly on your parameters. Euclid's *Elements* copied continuously for ~2,300 years. The Hippocratic and Galenic corpora. The Chinese woodblock canon. The Islamic manuscript tradition, which is the reason you have Greek science at all. And most damagingly: **the Vedic oral tradition**, transmitted for roughly 3,000 years without writing using explicit error-correcting recitation schemes (*padapāṭha*, *kramapāṭha*, *jaṭāpāṭha*, *ghanapāṭha*) that preserve phonetic detail to a fidelity that written transmission of comparable texts did not achieve.

That case simultaneously (i) flatly falsifies a 10-generation oral half-life, and (ii) is the single strongest historical demonstration of your own central concept — a culture that recognised the context-transfer problem and engineered institutional redundancy against it. Its absence from a study about how knowledge is packed across generations is not a gap; it is the missing chapter.

**(c) serious**

**(d) Fix:** Add at least three transmission-success cases with the full "what survived / what was lost" apparatus, including at least one non-Western and non-script case. Revisit the oral half-life.

---

### F38 — The apparatus itself is asymmetric

**(a) Claim:** Structure of the 23 evidence records.

**(b) Wrong:** Loss cases get a "what survived / what was lost" pair, a loss-type tag, a mechanism, and in several cases a myth-correction. Threshold cases get a one-line SHOWS, a one-line DOES NOT SHOW, and no counterfactual, no mechanism, and no "what was at risk and did not fail." The instrument is built to make losses legible and successes invisible, independently of the underlying history. A reader cannot see the successes even where you have included them.

**(c) serious**

**(d) Fix:** Give threshold cases the same fields, including "what could have been lost here and was not, and why."

---

## 6. The taxonomy

### F39 — Not exhaustive: five categories missing, and they cover most of your own cases

**(a) Claim:** *"The most common error here is to collapse six very different events into a single sentence… These are distinct mechanisms and they call for distinct remedies."*

**(b) Wrong. Missing, at minimum:**

- **(a) Input / supply loss** — the feedstock becomes unavailable. Covers wootz on your *own preferred hypothesis* (trace elements in specific ores), Greek fire on Haldon & Byrne's (Caucasian/Crimean naphtha lost with the territories), and Roman marine concrete (pozzolana logistics). You currently force all three into `tacit`, which your glossary contradicts.
- **(b) Demand obsolescence** — nobody wants it any more. Firearms vs swords; monumental concrete without an imperial budget. This is the most common reason technologies stop being practised in all of history and you have no box for it.
- **(c) Suppression / coerced cessation** — a third party stops production. The 1866 British prohibition on Indian steel-making. Categorically distinct from "deliberate non-recording," which concerns the holder's own choice.
- **(d) Referential / interpretive loss** — the record survives, the language survives, and the meaning still does not. We can read every word of the ancient pharmacological corpora and cannot identify the referents: what plant was *silphium*, what mineral was *ḫaššu*. Your `decoder` category as defined ("the language, script or training chain that could read it runs out") does not cover this, because nothing ran out.
- **(e) Never-recorded (non-deliberate)** — as distinct from deliberately not recorded. Roman hot mixing was presumably not a secret; it simply fell below the threshold of what anyone bothered to write. This is the largest category in the history of craft and it is the correct home for your Roman concrete case (F4).

**(c) blocking**

**(d) Fix:** Add all five, or stop claiming the six are the distinct mechanisms.

---

### F40 — Not mutually exclusive, and your own cases prove it

**(a) Claim:** *"These are distinct mechanisms and they call for distinct remedies."*

**(b) Wrong, from within your own dataset:**

- **Maya codices** = carrier + decoder (glyphic literacy also died; see F17).
- **Domesday** = apparatus + maintenance (the emulation gap is a maintenance failure; Domesday Reloaded then rotted in 2018 — pure maintenance loss, in the same case).
- **F-1 engine** = tacit + apparatus. You say so yourself: *"the analogue, obsolete formats the drawings sit in"* is verbatim your apparatus category, sitting inside a record tagged `tacit`.
- **Link rot** = maintenance + apparatus + carrier, varying per page.
- **Greek fire** = deliberate restriction + input supply (F9).

**(c) serious**

**(d) Fix:** Present these as non-exclusive *dimensions* with a per-case profile, not a partition. That is both more honest and more useful, since your "distinct remedies" argument works better on dimensions than on bins.

---

### F41 — The taxonomy mixes two axes, which is why the assignments keep going wrong

**(a) Claim:** The six category names.

**(b) Wrong:** "Carrier loss," "decoder loss" and "apparatus loss" name **what went missing**. "Maintenance loss" and "deliberate non-recording" name **why it went missing**. "Tacit knowledge loss" does both at once. A single-axis taxonomy built from two axes will always generate ambiguous assignments — which is exactly what has happened in F2, F5, F17, F20 and F40. `tacit` has become the residual bin for every case whose actual cause your model cannot represent.

**(c) serious**

**(d) Fix:** Two axes: *what was lost* (carrier / decoder / skill / apparatus / referent) × *why* (destroyed / never recorded / restricted / unmaintained / input unavailable / demand gone / suppressed). Every case then gets a coordinate, and F40's compound cases stop being anomalies.

---

### F42 — Data-integrity slip in the taxonomy keys

**(a) Claim:** Greek fire record carries `loss-type: secrecy`; the taxonomy's sixth category is labelled **"Deliberate non-recording"**.

**(b) Wrong:** The key and the label do not match, and they do not mean the same thing — secrecy is restricted circulation of *recorded* knowledge, non-recording is its absence. Given that the Byzantine fire was demonstrably a state-held craft secret with known practitioners (the Lampros family), "restricted circulation" is the correct description and "non-recording" is not.

**(c) minor** (data integrity) / **serious** (as evidence for F41)

**(d) Fix:** Align the key and label; then decide which mechanism you actually mean.

---

# Verdict on the historical portion

**Not publishable as history in its present form.** Not because of tone or ambition — the taxonomy instinct is sound and the myth-correction section is better than the genre norm — but because the case set does not survive verification and the conceptual frame does not survive the case set.

Specifically: one flagship case rests on a claim that is simply false (Antikythera, "no comparable second machine"). Three of seven loss cases are misclassified at the level of mechanism, in each instance because your model has no term for the mechanism the historical record actually reports (wootz, Roman concrete, Greek fire). One case is a decade out of date in the direction that inflates the loss (Maya, Grolier). One is wrong by 140 years in a way that changes the causal story (rongorongo). One threshold record is tagged `direct`/`high` for an artefact that does not exist (printing, 1234). One prints a well-known false date in its title in a study whose stated purpose is correcting well-known false dates (peer review, 1665). And the deepest historiographical failure is structural, not factual: you debunk the European library myth in full and leave the South Asian one encoded in a date range.

The post-1900 material — Pew, Domesday, F-1, Cerf, model collapse — is careful, correctly caveated, and checks out. That accuracy is currently underwriting a pre-modern section that has not earned it.

---

# The single most damaging criticism a hostile expert would make

**You built a model whose only available explanations are context transfer and decoder access, then selected seven cases on the outcome and explained all seven with context transfer and decoder access — but in at least three of them the historical record says the cause was ore chemistry, market demand, and colonial prohibition, none of which your model can represent.**

Wootz did not stop because a chain of tacit knowledge frayed. It stopped because firearms killed the sword trade, Sheffield undercut the price, and in 1866 the British made Indian steel-making illegal under cover of forest conservation — while Indian crucible furnaces were still being observed working in 1807 and the process was still being recorded in Tamil Nadu in 1893. Roman hot-mixed lime did not stop at all; it is in continuous vernacular use and has a modern trade literature. Greek fire's leading explanation is loss of a petroleum supply that went with the territory.

You have written a study about the fragility of transmission using three cases where transmission was fine and the political economy was not. And because the myth-corrections never cost you a case, a parameter or a conclusion, the reader who notices this has no way to tell whether you were unable to see it or unwilling to let it matter.

**Sources**

[Field & Wright, *Annals of Science*, Byzantine geared sundial](https://www.tandfonline.com/doi/abs/10.1080/00033798500200131) · [Geared instruments: a continuous tradition](https://www.archaeology.wiki/blog/issue/geared-instruments-from-antiquity-to-the-present-day-a-continuous-tradition/) · [Jones, *Epoch Dates of the Antikythera Mechanism*, ISAW Papers 17](https://archive.nyu.edu/jspui/bitstream/2451/61000/2/Jones%202020%20Epoch%20dates%20of%20the%20Antikythera%20Mechanism%20ISAW%20Papers%2017.pdf) · [Pompeii construction site, *Nature Communications* 2025](https://www.nature.com/articles/s41467-025-66634-7) · [Roman concrete overview](https://en.wikipedia.org/wiki/Roman_concrete) · [MIT News, hot mixing 2023](https://news.mit.edu/2023/roman-concrete-durability-lime-casts-0106) · [Traditional hot mixed lime mortars for conservation and repair](https://www.academia.edu/40884630/Traditional_hot_mixed_lime_mortars_for_conservation_and_repair) · [Greek fire: DAI, Anna Komnene, Wolfenbüttel MS](https://en.wikipedia.org/wiki/Greek_fire) · [Cypriot syllabary](https://en.wikipedia.org/wiki/Cypriot_syllabary) · [Linear B dating](https://www.britannica.com/topic/Linear-B) · [Cambridge, *The Decipherment of Linear B*](https://www.classics.cam.ac.uk/system/files/documents/process.pdf) · [Ferrara et al., rongorongo radiocarbon, *Sci Rep* 2024](https://www.nature.com/articles/s41598-024-53063-7) · [Rongorongo: contact, slave raids, literacy loss](https://en.wikipedia.org/wiki/Rongorongo) · [Coe et al., *The Fourth Maya Codex*](https://www.mesoweb.com/articles/Coe_etal/Fourth_Codex.pdf) · [Brown University, Grolier Codex authenticated](https://www.brown.edu/news/2016-09-07/mayacodex) · [Landa, *Yucatan Before and After the Conquest*](https://sacred-texts.com/nam/maya/ybac/index.htm) · [Verhoeven, Pendray & Dauksch, *JOM* 1998](https://www.tms.org/pubs/journals/JOM/9809/Verhoeven-9809.html) · [UCL PIA, wootz production site](https://student-journals.ucl.ac.uk/pia/article/164/galley/241/view/) · [Alter, *Seeking Truth in Damascus Steel*](https://www.tf.uni-kiel.de/matwis/amat/iss/kap_b/articles/2017_alter_stephan_truth_damascus_steel.pdf) · [Guinness, oldest metal-type book](https://www.guinnessworldrecords.com/world-records/689333-oldest-book-printed-using-movable-metal-type) · [Tricycle, movable type: the Buddhists were first](https://tricycle.org/magazine/buddhist-history-moveable-type/) · [Fyfe, peer review: not as old as you think](https://www.timeshighereducation.com/peer-review-not-as-old-as-you-might-think) · [Moxham & Fyfe, *The Royal Society and the Prehistory of Peer Review*](https://www.cambridge.org/core/journals/historical-journal/article/royal-society-and-the-prehistory-of-peer-review-16651965/93B903FD4D6561AA7224C62EE57B0C18) · [SciELO, *Journal des sçavans* and *Phil Trans*](https://blog.scielo.org/en/2015/03/05/350-years-of-scientific-publication-from-the-journal-des-scavans-and-philosophical-transactions-to-scielo/) · [Reconsidering 'Tokens', *Cambridge Archaeological Journal*](https://www.cambridge.org/core/journals/cambridge-archaeological-journal/article/abs/reconsidering-tokens-the-neolithic-origins-of-accounting-or-multifunctional-utilitarian-tools/7E6C04CB040AD8AA0EA84B94D4D275C4) · [Nalanda mahavihara](https://en.wikipedia.org/wiki/Nalanda_mahavihara) · [BBC Domesday Project](https://en.wikipedia.org/wiki/BBC_Domesday_Project) · [TNA PRO 30/100](https://beta.nationalarchives.gov.uk/catalogue/id/C16160) · [NASA Marshall Star, 30 Jan 2013](https://www.nasa.gov/centers/marshall/about/star/star130130.html) · [AAAS 2015, Cerf, "Digital Vellum"](https://aaas.confex.com/aaas/2015/webprogram/Paper14064.html) · [Pew, When Online Content Disappears](https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/) · [ITU Facts and Figures 2025](https://www.itu.int/en/mediacentre/Pages/PR-2025-11-17-Facts-and-Figures.aspx) · [Bagnall, *Alexandria: Library of Dreams*](https://archive.nyu.edu/bitstream/2451/28263/2/D172-Alexandria%20Library%20of%20Dreams.pdf) · [Edgerton, *The Shock of the Old*](https://en.wikipedia.org/wiki/The_Shock_of_the_Old)
