# Codebook — The Transmission Chain link-coded corpus

**Dataset version** 1.0.0 · **Derived from** `index.html` v5.2, data cut-off 23 August 2026
**Author** Ahmet Çandöken · ORCID https://orcid.org/0009-0001-5197-7888 · **Licence** CC BY 4.0 (data and text)

This codebook is the operational specification for the files in this directory. It is
written so that a coder who has never seen the study can reproduce a coding decision and
disagree with it in a specific place. Everything below is either a definition, a rule
taken verbatim from the published source code, or a stated limitation. Where a rule is
known only to the original coder it is marked **[AUTHOR TO COMPLETE]** rather than
guessed at.

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
| `sources.csv` | 275 | one unique cited URL, with usage count |
| `corpus.json` | — | lossless export: original bilingual fields with their inline markup, plus model parameters |

CSV files are UTF-8, comma-separated, RFC 4180 quoting, with a header row. Text fields in
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

**The inclusion rule — [AUTHOR TO COMPLETE].** State here, in the author's own words:
how a candidate object came to be on the list; what the minimum evidence bar was (e.g.
"at least N dated events each with an independently checkable source"); and which
candidates were considered and **rejected**, with the reason. A data paper reviewer will
ask for this and the dataset is materially weaker without it. It cannot be reconstructed
from the files.

**What can be said now, and should be said plainly:** this is a convenience sample chosen
by one author from no defined population. It is not a random or representative sample of
transmission histories and no base rate should be computed from it. The "26 of 32 held"
figure is a property of this shortlist and of nothing else. See §6.2.

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

### 6.3 Source quality is uneven, and the mix is published
Of 275 unique sources: journal or preprint 17, university 19, official or standards body
18, museum or archive 13, encyclopedia 29, other web 179. The `source_type` column is
assigned automatically from the URL host by the export script and is a coarse
convenience label, not an editorial judgement of quality. Users who need a
provenance-graded subset should filter on it and check by hand.

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

The CSV and JSON files were generated mechanically from `index.html` v5.2 by an export
script; no value was entered by hand during export, and the counts reported above
reproduce the counts published in the study. **The study's text, code, source checking
and prior-art survey were produced with substantial AI assistance, and what the study
formerly called "expert review" was adversarial critique by AI models across six
specialist framings — it is not human peer review and must not be counted as such.** This
codebook was drafted with the same assistance. Responsibility for every claim rests with
the named author.
