#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aktarım Zinciri — kodlayıcılar arası uyum (Cohen kappa'sı).

Kullanım:
    python3 kappa-hesapla.py kodlama-SONUC.csv

Karşılaştırma referansı ayrı bir dosyada tutulmaz: betik, alt örneklemi ve ilk
kodlamayı doğrudan ../data/events.csv ve ../data/objects.csv dosyalarından türetir.
Alt örneklem kuralı yazılıdır ve tekrar üretilebilir — uygarlığa göre orantılı
tabakalama, tohum 20260825.

Ağa hiçbir şey göndermez.
"""
import csv, sys, os, random, collections

SEED  = 20260825
QUOTA = [('modern', 6), ('ottoman', 2), ('roman', 2)]
LINKS = ['paket', 'çözücü', 'bağlam', 'örtük bilgi', 'aparat', 'bakım']
TR    = {'packet':'paket', 'decoder':'çözücü', 'context':'bağlam',
         'tacit':'örtük bilgi', 'apparatus':'aparat', 'maintenance':'bakım'}

def load(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

def subsample(objects):
    """Formu üreten seçim kuralının birebir aynısı."""
    rng, sel = random.Random(SEED), []
    for civ, k in QUOTA:
        pool = sorted(r['object_id'] for r in objects if r['civilisation'] == civ)
        rng.shuffle(pool)
        sel += sorted(pool[:k])
    return sorted(sel)

def reference(here):
    data = os.path.normpath(os.path.join(here, '..', 'data'))
    objects = load(os.path.join(data, 'objects.csv'))
    events  = load(os.path.join(data, 'events.csv'))
    sel = subsample(objects)
    sub = sorted((e for e in events if e['object_id'] in sel),
                 key=lambda e: (e['object_id'], int(e['year'])))
    by_id = {o['object_id']: o for o in objects}
    return ([TR[e['link']] for e in sub],
            [TR[by_id[o]['thinnest_link']] for o in sel],
            [by_id[o]['name_tr'] for o in sel], sel)

def kappa(a, b):
    n = len(a)
    if n == 0: return float('nan'), 0.0, 0.0
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum((ca[k]/n) * (cb[k]/n) for k in set(ca) | set(cb))
    return ((po - pe) / (1 - pe) if pe != 1 else float('nan')), po, pe

def yorum(k):
    if k != k:      return "hesaplanamadı"
    if k < 0.00:    return "tesadüften kötü"
    if k < 0.20:    return "çok zayıf"
    if k < 0.40:    return "zayıf"
    if k < 0.60:    return "orta"
    if k < 0.80:    return "iyi (substantial)"
    return "çok iyi (almost perfect)"

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        gold, gold2, names, sel = reference(here)
    except FileNotFoundError as e:
        raise SystemExit("../data/ bulunamadi (%s). Betigi depo icindeki "
                         "ikinci-kodlayici/ klasorunden calistirin." % e.filename)

    rows = load(sys.argv[1])
    if not {'tip', 'halka'} <= set(rows[0].keys()):
        raise SystemExit('Bu CSV bu forma ait degil. Beklenen sutunlar: '
                         'tip, no, nesne, yil_veya_donem, halka, not')
    got  = [(r['halka'] or '').strip() for r in rows if r['tip'] == 'olay']
    got2 = [(r['halka'] or '').strip() for r in rows if r['tip'] == 'nesne']

    print("Alt örneklem (tohum %d): %s" % (SEED, ' · '.join(sel)))
    if len(got) != len(gold):
        print("UYARI: satır sayıları tutmuyor — form %d, referans %d" % (len(got), len(gold)))

    n = min(len(got), len(gold))
    pairs = [(g, h) for g, h in zip(gold[:n], got[:n]) if h]
    a = [p[0] for p in pairs]; b = [p[1] for p in pairs]
    k, po, pe = kappa(a, b)

    print("=" * 62)
    print("OLAY KODLAMASI  —  %d satırın %d'i dolu" % (n, len(pairs)))
    print("=" * 62)
    print("  yüzde uyum        : %.1f%%" % (po * 100))
    print("  beklenen uyum     : %.1f%%  (tesadüfen)" % (pe * 100))
    print("  Cohen kappa       : %.3f   → %s" % (k, yorum(k)))
    print()
    print("  halka bazında (ilk kodlama → gönüllü):")
    for L in LINKS:
        idx = [i for i, x in enumerate(a) if x == L]
        if not idx: continue
        agree = sum(1 for i in idx if b[i] == L)
        print("    %-12s %2d satır, %2d'inde aynı (%3.0f%%)" % (L, len(idx), agree, 100*agree/len(idx)))
    print()
    dis = [(i + 1, a[i], b[i]) for i in range(len(a)) if a[i] != b[i]]
    print("  anlaşmazlık: %d satır" % len(dis))
    for i, x, y in dis:
        print("    satır %2d:  ilk=%-12s gönüllü=%-12s" % (i, x, y))

    m = min(len(got2), len(gold2))
    pairs2 = [(g, h) for g, h in zip(gold2[:m], got2[:m]) if h]
    if pairs2:
        a2 = [p[0] for p in pairs2]; b2 = [p[1] for p in pairs2]
        k2, po2, _ = kappa(a2, b2)
        print()
        print("=" * 62)
        print("EN İNCE HALKA YARGISI  —  %d nesne" % len(pairs2))
        print("=" * 62)
        print("  yüzde uyum        : %.1f%%" % (po2 * 100))
        print("  Cohen kappa       : %.3f   → %s" % (k2, yorum(k2)))
        print("  (10 nesnede kappa çok gürültülüdür; yüzde uyumu rapor etmek daha dürüst.)")
        for i, (x, y) in enumerate(zip(a2, b2)):
            if x != y:
                print("    %-30s ilk=%-12s gönüllü=%-12s" % (names[i][:30], x, y))

    print()
    print("Raporlanacak cümle örneği:")
    print('  "10 nesnelik bir alt örneklemde (79 olay) ikinci ve bağımsız bir kodlayıcı ile')
    print('   olay-halka kodlaması için Cohen kappa = %.2f (%%%.0f yüzde uyum) elde edilmiştir."' % (k, po*100))

if __name__ == '__main__':
    main()
