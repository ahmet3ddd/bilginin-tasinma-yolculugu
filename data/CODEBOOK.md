# Codebook — The Transmission Chain link-coded corpus

**Dataset version** 1.0.0 · **Derived from** `index.html` v5.2, data cut-off 23 August 2026
**Author** Ahmet Çandöken · ORCID https://orcid.org/0009-0001-5197-7888 · **Licence** CC BY 4.0 (data and text)

This codebook is the operational specification for the files in this directory. It is
written so that a coder who has never seen the study can reproduce a coding decision and
disagree with it in a specific place. Everything below is either a definition, a rule
taken verbatim from the published source code, a limitation stated at full strength, or a
decision reported by the author in their own words. Nothing here is inferred: where only
the original coder could know something, it was asked and is quoted, not guessed.

---

## 1. What the corpus is

A hand-coded record of **255 dated, individually sourced events** in the transmission
history of **32 objects**, drawn from three civilisational strata (19 modern-industrial,
7 Ottoman, 6 Roman). Every event is assigned to exactly one of six transmission links.
Alongside it sit **38 dated evidence records** used by the study's 100,000-year chart,
and a **32 × 6 matrix** recording, for every object and link, whether the study's own
generational model can represent that link at all.

The corpus is the empirical layer of an interactive study. The study's argument, its
simulation and its prose are **not** part of this dataset and are not needed to use it.

### Files

| File | Rows | Unit of observation |
|---|---|---|
| `events.csv` | 255 | one dated, sourced event in one object's chain |
| `objects.csv` | 32 | one object |
| `evidence.csv` | 38 | one dated evidence record (23 from the evidence strip, 15 derived from chain maps) |
| `model-coverage.csv` | 192 | one object × link cell of the 32 × 6 matrix |
| `sources.csv` | 291 | one unique cited URL, with usage count |
| `corpus.json` | — | lossless export: original bilingual fields with their inline markup, plus model parameters |

CSV files are UTF-8 **with a byte-order mark**, comma-separated, RFC 4180 quoting, with a
header row. The BOM is deliberate: without it, Excel and WPS Office open the file in the
system code page and every non-ASCII character is mangled, which for a bilingual Turkish
dataset means most of the text. Read them with `encoding='utf-8-sig'` in Python; `pandas`,
R and most other tools strip the BOM themselves. `corpus.json` carries no BOM, as RFC 8259
requires. Text fields in
CSV have had inline HTML stripped and whitespace collapsed; `corpus.json` preserves the
original strings unmodified. All bilingual fields appear twice, suffixed `_tr` and `_en`;
the two are translations of one another, not independent records.

---

## 2. The six links — operational definitions

The links are the coding categories. They are adapted from a vocabulary that already
exists in the digital-preservation and tacit-knowledge literatures; five of the six map
onto terms in OAIS / ISO 14721 (see §7). The definitions below are the ones a coder must
apply, phrased as decision questions rather than as concepts.

| Code | Link | The question the coder asks | Nearest published term |
|---|---|---|---|
| `packet` | Packet | Is this event about the **selected content itself** — a written recipe, drawing, formula, patent, standard, specification, corpus, or the decision about what was worth recording? | OAIS *Data Object* |
| `decoder` | Decoder | Is this event about the **people and shared languages able to read and apply the packet** — literacy in the relevant script, a trained profession, a common notation, a designated community? | OAIS *Representation Information* + *Designated Community* |
| `context` | Context | Is this event about **why the thing worked, within which limits, and with what history of failure** — the knowledge that travels alongside a result and makes it usable rather than merely legible? | OAIS *Context Information* (term identical) |
| `tacit` | Tacit knowledge | Is this event about **hand skill, workshop sequence or judgement that was never written down**, and is transmitted only by working alongside someone who has it? | Polanyi 1966; Collins 2001, 2010 |
| `apparatus` | Apparatus | Is this event about **the machines and instruments that make or read the thing** — the furnace, the press, the reader, the measuring device, the supply of a critical input? | OAIS *Representation Information Network* |
| `maintenance` | Maintenance | Is this event about **the recurring labour, funding or institution that renews copying and teaching each generation** — an endowment, a curriculum, an apprenticeship, a budget, a state? | OAIS *Mandatory Responsibilities*; Star 1999 |

### 2.1 The one-link rule and its cost

**Each event is coded to exactly one link.** Where an event plausibly touches more than
one — and many do — the coder assigns the link the event is *evidence about*, not the
links it has consequences for.

This rule is a simplification and it is the corpus's largest single source of coder
disagreement. Two known systematic pressures:

- **Institutional events** (a ban, a budget, an endowment, an expulsion) are coded
  `maintenance` even when their mechanism runs through apparatus or decoder. A reviewer
  of an earlier version of the study noted correctly that this loads one category with
  political economy that the six-link scheme does not otherwise represent.
- **Instrument events** are coded `apparatus` even where the instrument's scarcity is a
  maintenance failure.

A user who disagrees with the one-link rule can recover a multi-label coding from
`events.csv`: the claim text is present in full in both languages.

### 2.2 Link frequencies in the corpus

`apparatus` 58 · `packet` 53 · `maintenance` 49 · `decoder` 38 · `context` 32 · `tacit` 25

These are counts of *coded events*, not of importance. `tacit` is lowest because tacit
knowledge is by definition the least documented — which is a property of the historical
record, not of the phenomenon, and should not be read as a finding.

---

## 3. The thinnest-link judgement

Each object carries one field, `thinnest_link`, recording which of the six links is
judged **most fragile today** — not which link failed historically.

**Decision rule as applied:** for each object, the coder asks which single link, if it
failed now, would make the object unreproducible soonest, given the sourced timeline.
Where the packet is complete and the chain still fails, the thinnest link is by
definition not `packet`.

**Distribution:** `apparatus` 8 · `context` 8 · `maintenance` 7 · `tacit` 6 ·
`decoder` 2 · `packet` 1.

**This is a single-coder judgement.** See §6.1 — it is the corpus's principal limitation
and the reason the distribution above should be treated as one reading, not a measurement.

---

## 4. Object selection

**Observable properties of the sample** (verifiable from `objects.csv`):

- 32 objects; **26 chains that held, 6 that broke** (`chain_broke`).
- Three civilisational strata: modern-industrial 19, Ottoman 7, Roman 6.
- Six thematic categories: `threshold` 8, `everyday` 7, `info` 6, `loss` 5,
  `electronics` 4, `energy` 2.
- Event years span 700 BCE to 2026 CE.
- Objects were added across successive versions of the study; the set grew from 30 to 32.

**The inclusion rule.** There was no formal criterion set in advance. Objects became
candidates because they interested the author; a candidate was then dropped if dated,
independently checkable sources could not be found for it. Source availability was
therefore an *elimination* criterion, not a selection criterion. Candidates that were
considered and rejected on that basis are listed at the end of this section.

One regularity in the result is worth reporting because a user will notice it: every
object is represented by seven or eight dated events (median 8) and four to six further
reading sources. This was not set as a target; it is a property of the finished corpus and
its cause is not documented.

**Candidates considered and rejected.**

*The Egyptian pyramids.* Initially rejected on the assumption that no sourced timeline
could be built, because how they were constructed is not well enough understood. On
checking, that turned out to be the popular framing rather than the position of the
literature: the Wadi al-Jarf papyri (c. 2560 BCE, the Diary of Merer) document limestone
haulage for Khufu's pyramid in a contemporary record, and there is an active engineering
literature on ramps and workforce logistics. The object was still left out, but **on scope
grounds**: including it would have pulled the study away from what it set out to show.
This entry stands here as the study's own myth-correction criterion applied to the
author's own decision.

*The mobile telephone.* Rejected on component count: decomposing an object with that many
components through six links would not have yielded a meaningful result. This is a
deliberate scope decision — and so that the same limit stays **visible**, some
many-component technological objects (the integrated circuit, the hard disk, the computer,
the internet) were deliberately kept in the corpus.

*Abstract concepts.* Concepts with no material carrier even in their own period were left
out; for such an object the *packet* and *apparatus* links are undefined.

*The general principle.* Adding further objects for similar reasons was judged likely to
pull the work away from what it set out to say; the subject is already complex and not
easy to grasp.

**What follows from this, plainly:** the sample is a convenience sample chosen by one
author from no defined population. It is not random and not representative. No base rate
should be computed from it, and the figure "26 of 32 held" is a property of this shortlist
and of nothing else. See §6.2.

---

## 5. The model-coverage matrix

`model-coverage.csv` records, for each object × link cell, whether the study's own
generational simulation has any term capable of representing that link. It is included
because it is an audit of the study's instrument, not a result about history.

The mapping is fixed for all objects and is taken verbatim from the source:

| Link | Model representation | Slider |
|---|---|---|
| `context` | **full** | `qc` |
| `decoder` | **full** | `qd` |
| `packet` | **partial** | `gain` |
| `apparatus` | **partial** — folded into the archive half-life only | `halfLife` |
| `maintenance` | **partial** — no separate term; dissolves into the half-life | `halfLife` |
| `tacit` | **none** — no term at all | — |

Classifying each object by the representation status of *its own thinnest link* gives
**10 full · 16 partial · 6 none**: for 22 of 32 objects the model cannot cleanly isolate
the link the object actually turns on, and for 6 it has no term for it whatsoever.

The scenario rule that drives the per-object curves is likewise fixed, with no per-object
tuning, and is reproduced here verbatim from the source:

```js
/* the weakest link's slider  -> its LOW constant
   every other mapped slider  -> its HEALTHY constant
   tacit has no slider: the scenario stays healthy on purpose, so the model's
   blindness to this case is VISIBLE in the curves rather than papered over. */
SCENARIO_RULE = {
  qc:       { low: .40, healthy: .90 },
  qd:       { low: .40, healthy: .90 },
  gain:     { low: 1.5, healthy: 4   },
  halfLife: { healthy: 45 }          // no LOW value since v5.3 — see below
};
```

**A defect that was found and fixed in v5.3, recorded here because it affected every
earlier version of these curves.** Because `apparatus` and `maintenance` both map to
`halfLife`, and because a *shorter* archive half-life raises reconstructability in this
engine (sweeping at generation 40: h=5 → R=3.54, h=10 → R=4.63, peak h≈12 → R=4.89,
h=45 → R=3.11, h=100 → R=2.75), the old rule handed apparatus- and maintenance-thinnest
objects h=10 — within a hair of the optimum. Their curves therefore rendered as the
*healthiest* in the study, 41.7% above an all-healthy chain, which is the exact opposite
of the coded reading. Fifteen objects routed through that branch; with the six tacit
objects, 21 of 32 were drawn at or above baseline by a feature whose purpose is to show
fragility.

Since v5.3 the half-life is never lowered: apparatus and maintenance are treated exactly
like tacit knowledge, the scenario is left healthy on purpose, and those 21 objects now
sit at the all-healthy baseline — which is the honest statement that the model has no
term for what they turn on. **The model curves are still not a measure of fragility and
must not be used as one.** The matrix in this file is independent of the curves and is
unaffected by the defect or by its repair.

---

## 6. Limitations

These are stated at the strength a hostile reviewer would state them.

### 6.1 Single coder, unblinded, no reliability statistic
Every link assignment and every thinnest-link judgement was made by **one coder, who is
also the author of the argument the coding supports**, without blinding, without a second
coder, and with no inter-rater agreement statistic. There is no κ. The 10/16/6 coverage
result and the thinnest-link distribution are the most useful numbers in the corpus and
both rest on n = 1 coder. **A second coder on a 10-object subsample, reporting Cohen's κ,
is the single change that would convert this from one reading into a measurement.** Until
that exists, the coding should be cited as an interpretive resource, not as data about
the world.

### 6.2 Two different selection biases, in two different directions
The five `loss` objects were selected **because loss occurred** — selection on the
dependent variable. The remaining 26 were selected substantially from famous,
well-documented, *surviving* objects — survivorship selection. These biases do not cancel;
they rotate. No inference about the frequency, distribution or causes of transmission
failure in general can be drawn from this corpus.

### 6.3 Source provenance is uneven, and the mix is published

Every claim in this corpus names its source, but the sources are not of one kind, and
until v5.4 the data hid that: `source_type` had a single catch-all `web` value holding
163 of 255 events, so a statute on `mevzuat.gov.tr`, a signed article in a scholarly
encyclopaedia and a newspaper feature were indistinguishable to anyone filtering the
file. That was a defect in the data, not only in the sources.

`source_type` now records the **publisher kind**. It is a provenance label, not a
quality score: what makes a citation adequate is the fit between the kind of source and
the kind of claim, and that judgement is set out as a policy below.

**The source policy — claim type governs source type.**

| Kind of claim | Source required |
|---|---|
| Legal or administrative fact | the statute, gazette or the deciding body's own published decision |
| Statistic | the institution that produced the figure; an audited figure in preference to a reported one |
| Historical interpretation | refereed scholarship, an academic press, or an edited reference work with signed articles |
| Object, inscription, manuscript, excavation | the collection, archive or excavation record |
| Technical standard or unit | the standard itself (ISO, BIPM, IANA, RFC) |
| Priority of an invention | the patent, the Nobel lecture, or refereed history — never the firm's own account alone |
| Contemporary event | contemporaneous journalism is legitimate; it is dated and labelled as such |

Two consequences follow, and both are applied in this corpus. A news source is **not**
disqualified — for a 2014 ministerial decision or a 2026 product announcement it may be
the appropriate record — but it may not carry a historical claim for which scholarship
exists. And an official source is **not** automatically superior: a ministry's account of
a reform it carried out is a party to the events, a primary record of what was decided
rather than a neutral record of what happened to the knowledge.

**The mix, as published:**

| `source_type` | Unique sources | Events |
|---|---:|---:|
| `official-legal` | 48 | 40 |
| `patent` | 12 | 11 |
| `peer-reviewed` | 47 | 46 |
| `university-or-institute` | 36 | 31 |
| `museum-archive-library` | 60 | 54 |
| `reference-work` | 25 | 32 |
| `professional-or-trade-body` | 13 | 14 |
| `corporate-or-interested-party` | 17 | 12 |
| `news-media` | 18 | 9 |
| `blog-or-personal-compilation` | 10 | 3 |
| `tertiary-open-encyclopedia` | 5 | 3 |
| **Total** | **291** | **255** |

Where a weaker source is retained because no better one could be verified, the note on
that source in the study says so in plain words — `corporate-or-interested-party` and
`blog-or-personal-compilation` entries carry that qualifier. Three claims still rest on
Wikipedia; a user who needs a provenance-graded subset should filter on `source_type`
and treat those three as unresolved.

**What changed in v5.4, and why it matters beyond citation hygiene.** Re-sourcing was not
cosmetic: checking claims against higher-order sources changed the claims. **80 of the 255
event citations were replaced, 63 event claims were rewritten to what the verifiable
source actually says, and four event years were corrected.** Figures that no higher-order
source would corroborate were removed rather than re-cited — among them the
periodic-verification years of the kilogram prototype (1889/1948/1989 → 1899-1911,
1939-1953, 1988-1992), the tonnage in the 1931 Ottoman archive sale (27 tons → 30-50
tons), the dome measurements of the Süleymaniye (26.5 m / 53 m → 27.40 m / just over
50 m), the gloss count of the Glossa Ordinaria (96,940 → c. 96,000), the length of the
Valens channel network (over 250 km → c. 246 km, or at least 426 km including the
fifth-century extension), and the year of Hasan Çelebi's icâzet (1975 → 1391/1971). Any
user who took the v5.3 data at face value on those points was taking a figure whose only
warrant was a tertiary source.

### 6.4 Coverage is geographically and temporally lopsided
The three strata are Europe-, Anatolia- and Mediterranean-centred. There is no
sub-Saharan African, East Asian, South Asian or Indigenous-American object in the set
apart from what appears in the separate evidence strip. Any cross-cultural claim is out
of this corpus's reach.

### 6.5 Bilingual fields are translations
`_tr` and `_en` fields are the same claim in two languages. They are not independent
observations and must not be counted twice.

### 6.6 The dates are the study's, not a chronology of record
Event years are as recorded by the cited source. Where sources disagree the study picked
one and, in several cases, footnoted the conflict in prose that is **not** carried into
these files. Anyone using the years quantitatively should re-check against `source_url`.

---

## 7. Relation to existing frameworks

This corpus is not proposed as a new theory. Five of its six links have prior names:
`packet` ≈ OAIS *Data Object*; `decoder` ≈ *Representation Information* + *Designated
Community*; `context` ≈ *Context Information*; `apparatus` ≈ *Representation Information
Network*; `maintenance` ≈ the OAIS *Mandatory Responsibilities* and the maintenance
literature (Star 1999; Russell & Vinsel 2016). A six-property preservation model already
exists (SPOT: Vermaaten, Lavoie & Caplan, *D-Lib* 2012), as does a five-category tacit
knowledge taxonomy with per-category remedies (Collins 2001).

What the corpus contributes is not the scheme but the **application of one fixed scheme,
without per-object tuning, to a heterogeneous cross-civilisational object set, with every
event dated and sourced** — and the publication of the resulting matrix even where it
counts against the scheme.

---

## 8. Citation and reuse

Licence **CC BY 4.0** for this dataset and this codebook; the study's code is MIT. Under
CC BY 4.0 the licence also covers sui generis database rights where they subsist.

Cite as:

> Ahmet Çandöken (2026). *The Transmission Chain: a link-coded corpus of 255 dated
> transmission events across 32 objects* (Version 1.0.0) [Data set]. Zenodo.
> https://doi.org/10.5281/zenodo.22093227

Cited primary sources remain subject to their own rights; every one is reachable from
`source_url`.

---

## 9. Provenance of this file

The CSV and JSON files are generated mechanically from `index.html` v5.4 by
`tools/export-data.py`, which ships with the repository; no value is entered by hand
during export, and the counts reported above reproduce the counts published in the study.
Re-run it with `python3 tools/export-data.py index.html data`. The `source_type` value is
assigned by that script from the URL host against a table of publisher kinds; a host the
table does not know makes the export fail loudly rather than fall back to a catch-all,
which is what the old single `web` bucket did. **The study's text, code, source checking
and prior-art survey were produced with substantial AI assistance, and what the study
formerly called "expert review" was adversarial critique by AI models across six
specialist framings — it is not human peer review and must not be counted as such.** This
codebook was drafted with the same assistance. Responsibility for every claim rests with
the named author.
