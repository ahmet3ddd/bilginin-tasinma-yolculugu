# The Transmission Chain — link-coded transmission corpus
# Aktarım Zinciri — halka-kodlu aktarım korpusu

**v1.1.0** · derived from / türetildiği kaynak: `index.html` v5.4 (2026-08-28)
**Regenerate / yeniden üret:** `python3 tools/export-data.py index.html data`
**Licence / Lisans:** CC BY 4.0 (data + text) · code elsewhere in the repo is MIT

255 dated, individually sourced events in the transmission history of 32 objects
(19 modern-industrial, 7 Ottoman, 6 Roman), each coded to exactly one of six
transmission links — packet, decoder, context, tacit, apparatus, maintenance —
under one fixed rule with no per-object tuning.

32 nesnenin aktarım tarihinden tarihli ve tek tek kaynaklı 255 olay; her biri altı
aktarım halkasından tam birine, nesneye özel ayar yapılmadan, tek sabit kuralla
kodlanmış.

## Read this first / Önce bunu okuyun

**`CODEBOOK.md`** (English) / **`KOD-KITAPCIGI.md`** (Türkçe) — the operational
definitions, the coding rules, and the limitations. The corpus should not be used
without them. Two limitations in particular: the coding is by a **single unblinded
coder** with no inter-rater statistic, and the object set carries **two selection
biases in opposite directions**. Neither is a reason not to use the data; both are
reasons not to compute a base rate from it.

## Files / Dosyalar

| File | Rows | Unit |
|---|---|---|
| `events.csv` | 255 | one dated, sourced event |
| `objects.csv` | 32 | one object |
| `evidence.csv` | 38 | one dated evidence record |
| `model-coverage.csv` | 192 | one object × link cell (32 × 6) |
| `sources.csv` | 291 | one unique cited URL |
| `corpus.json` | — | lossless bilingual export + model parameters |

## Headline counts / Manşet sayılar

- objects 32 · chains that held 26 · chains that broke 6
- thinnest link: apparatus 8 · context 8 · maintenance 7 · tacit 6 · decoder 2 · packet 1
- events per link: apparatus 58 · packet 53 · maintenance 49 · decoder 38 · context 32 · tacit 25
- model coverage of each object's own thinnest link: **10 full · 16 partial · 6 none**
- event years: 700 BCE – 2026 CE

## Source provenance / Kaynak kökeni

`source_type` records the **publisher kind** of each citation in eleven categories, not a
quality score. The rule that governs which kind of source a claim may rest on — the
**source policy** — is set out in §6.3 of the codebook, together with the published mix
and the list of figures corrected in v5.4 when higher-order sources contradicted them.

`source_type` her atfın **yayıncı türünü** on bir kategoride kaydeder; bir kalite puanı
değildir. Bir iddianın hangi tür kaynağa dayanabileceğini belirleyen **kaynak politikası**
kod kitapçığının 6.3 bölümündedir; yayımlanan karışım ve üst kaynakların çelişttiği için
v5.4'te düzeltilen sayıların listesi de oradadır.
