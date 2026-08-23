# Knowledge travels, context does not — and I was not the first to say so

The complete grammar of Ubykh was published in 2011. Two hundred and twenty-five pages,
LINCOM Europa, by Rohan Fenwick. The dictionary had appeared in 1963, the monograph on the
verb in 1975. The audio recordings sit in an archive in Paris. Eighty-four consonants,
three vowels, the grammar, the lexicon — all of it is in our hands.

The last person able to speak Ubykh, Tevfik Esenç, died on **7 October 1992** in the
village of Hacı Osman, Manyas, in Balıkesir province, Turkey. The grammar came out
**nineteen years after** his death.

The packet is complete. It is still growing. And nobody can speak the language.

---

## The question

Some time ago I got stuck on a question that looked simple: what actually reaches us from
the past?

The result reaches us — the object, the formula, the building, the record. But what about
the thing that produced it? Why it was made that way, where it failed, which mistakes
shaped it, how the hand held it?

Nobody today can make a pencil alone. Rebuilding a toaster from scratch took one man nine
months and three hundred times the price. NASA did not lose the Saturn V blueprints — the
documents were found and used; what was missing was the shop-floor knowledge to execute
them.

Working through these, I noticed that six different things were being collapsed into one.
The sentence "the knowledge was lost" hides six distinct events:

- **Packet** — the written recipe, schema, patent, standard
- **Decoder** — the people and shared languages who can read and apply it
- **Context** — why it works, within what limits, with what history of errors
- **Tacit knowledge** — the hand skill that never reaches paper
- **Apparatus** — the machines that make it and read it
- **Maintenance** — the recurring labour of copying and teaching, redone every generation

All six have to be alive at once. When one breaks, the artefact survives and the recipe
does not.

I did not want to leave this as an essay. I wanted sliders you could move, cases you could
open, sources you could click. Six months later there were thirty-two chain-mapped
objects, a bilingual interface and a runnable model.

## The first correction: my own code contradicted me

Before publishing I put the work through review from six specialist framings —
archaeology, history of science and technology, quantitative modelling, digital
preservation, philosophy of science, publication integrity. (Those reviews were carried
out **by AI models**. That is not human peer review, and the study says so in its credits.)

Five of the six reviewers found the same thing, independently of each other.

The formulas I was showing readers in the Method section did not describe the code the
site runs. The printed version said `R = C × q_d`. That is not what the code computed. On
the default settings, at generation 40, the discrepancy was **82.7%**.

One reviewer went further: extracted the code and ran it. Closed every loss channel —
context transfer at 100%, decoder at 100%, no decay at all — and showed that the model
still reported 12.3% of context lost. Inside the code there was a constant, `0.85`, that
appeared in no formula and no explanation anywhere on the page.

In other words: **the interactive instrument that was supposed to be the argument's
evidence could not represent the argument being false.** Wherever the reader dragged the
sliders, they would find the thesis, because the thesis had been written into the equation.

I earned this sentence: *"A study whose argument is that results travel while the method
behind them is lost has published its results and lost its method."*

I removed the constant, printed the real recurrences, and wrote it into the revision log.

## The second correction: all of it had been said already

When that round was done I asked a more basic question: has any of this been said before?

I surveyed six separate literatures. The answer was clearer than I would have liked.

**Tacit knowledge.** Polanyi wrote "we know more than we can tell" in 1966. Harry Collins
turned it into experiment in the 1970s: not one laboratory built a working TEA laser from
the published papers alone; every success involved working face to face with someone who
had built one. In 2001 he published a five-part taxonomy of how it fails to transmit. The
structure of mine.

**Cultural evolution.** Every parameter in my model has a published owner. My flat
learning budget is λ in Mesoudi's 2011 model. That paper's headline finding is my central
claim: the accumulated stock consumes the acquisition budget. Fifteen years earlier, in a
peer-reviewed journal.

**Digital preservation.** Five of my six links are ISO-grade terms. In the OAIS reference
model the packet is the "Data Object", the decoder is "Representation Information", and
context is — word for word — "Context Information". And a six-property framework, each
property with its own threat list, was published in 2012.

**And the oldest.** W. H. R. Rivers, 1912, "The Disappearance of Useful Arts." Specialists
dying out, dependence on trade networks, technique fused into ritual. A taxonomy of loss
written a hundred and fourteen years ago.

There was also my founding metaphor: knowledge as a "zipped packet". Michael Reddy named
that the "conduit metaphor" in 1979 — and wrote about it **in order to show it was wrong.**

## What I did

I did not delete anything. I changed the frame.

I added a **Precursors** section: seven literatures, each with its owners named, a concept
map (my "packet" is Latour's immutable mobile; my K is Mesoudi's λ), and the lineage of my
simulation, complete with Henrich's and Enquist's equations.

Then I added seven sources that argue **against** me. The experiment finding that
transmitting causal understanding has no measurable effect on the pace of cultural
evolution. The analysis showing the format-obsolescence threat never materialised.
Edgerton, arguing that technologies are not lost but abandoned. And the book-length
counter-argument that rebuilding after collapse is entirely possible.

And at the end of the section I wrote this:

> This section is itself evidence for the thesis. This study rebuilt the same chain from
> scratch, unaware of the literatures above — because that knowledge sat in six separate
> packets, inside six separate decoder communities, with the transmission chain between
> them broken. To be forced to rediscover a thesis independently is precisely the
> condition the thesis describes.

## What is left

Not a discovery. The study now says so itself.

What is left is this: the first runnable version of a seventy-year-old literature that is
split across six fields which do not read one another. Thirty-two objects — from the
pencil to the Iznik tile, from the Roman aqueducts to the Ubykh language — all measured by
the same six links and the same fixed rule. A matrix in which the model testifies against
itself, counting how many of the thirty-two cases it cannot isolate the fragile link in.
The answer is twenty-one.

And one finding I value most: Ubykh's thinnest link came out as **maintenance**. The same
link as the Roman aqueducts' and the codex's. A Caucasian language and a Roman water
system break at the same point.

The object changes. The breaking point does not.

---

**[The study is here →]**

One file, no installation, Turkish and English. Every source is clickable, and the items
that could not be verified are marked as such. The revision log is open — the mistakes
above are in it, version by version. Hiding a revision log is precisely what this study
criticises.

If you find something wrong, write to me. That is exactly what got this text this far.
