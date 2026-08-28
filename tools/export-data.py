#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aktarım Zinciri — veri dışa aktarımı / The Transmission Chain — data export

index.html tek gerçeklik kaynağıdır. Bu betik oradaki `products` ve `evidence`
dizilerini okur ve data/ altındaki beş CSV ile corpus.json dosyasını üretir.

CSV'ler BOM'lu UTF-8 yazılır (Excel ve WPS'in Türkçe metni bozmaması için);
corpus.json BOM taşımaz (RFC 8259).

Kullanım:  python3 tools/export-data.py [index.html] [data/]

index.html is the single source of truth. This script reads its `products` and
`evidence` arrays and regenerates the five CSVs and corpus.json under data/.
CSVs are written as UTF-8 with BOM; corpus.json carries no BOM (RFC 8259).
"""
import csv, io, json, os, re, sys
from collections import Counter, OrderedDict
from urllib.parse import urlparse

# ---------------------------------------------------------------- kaynak türü
# v5.4: tek bir "web" kovası yerine, kaynağın YAYINCI TÜRÜNÜ ayıran taksonomi.
# Bu bir kalite yargısı değil, bir köken etiketidir: hangi iddianın hangi tür
# kaynağa dayandığı süzülebilsin diye. Kullanım kuralları için kod kitapçığının
# "kaynak politikası" bölümüne bakınız.
SOURCE_TYPES = [
    'official-legal',            # kanun, resmî gazete, bakanlık, denetim raporu,
                                 # standart kuruluşu, ulusal metroloji enstitüsü,
                                 # hükûmetlerarası kuruluş
    'patent',                    # patent ofisi kaydı ya da patent veri tabanı
    'peer-reviewed',             # hakemli dergi, akademik yayınevi, ön baskı sunucusu
    'university-or-institute',   # üniversite/araştırma enstitüsü yayını
    'museum-archive-library',    # koleksiyon kaydı, arşiv, sayısal kütüphane, miras sicili
    'reference-work',            # imzalı maddeleri olan editörlü başvuru eseri
    'tertiary-open-encyclopedia',# Wikipedia
    'professional-or-trade-body',# meslek kuruluşu ya da sektör standardı kuruluşu
    'corporate-or-interested-party',  # konunun kendi şirketi/kurumu — ilgili taraf
    'news-media',                # gazetecilik
    'blog-or-personal-compilation',   # hakemsiz kişisel site/derleme
]

DOMAIN_TYPE = {
    # --- official / legal / standards
    'mevzuat.gov.tr': 'official-legal', 'www5.tbmm.gov.tr': 'official-legal',
    'tbmm.gov.tr': 'official-legal', 'ttkb.meb.gov.tr': 'official-legal',
    'meb.gov.tr': 'official-legal', 'sayistay.gov.tr': 'official-legal',
    'vgm.gov.tr': 'official-legal', 'erdem.gov.tr': 'official-legal',
    'atamdergi.gov.tr': 'official-legal', 'govinfo.gov': 'official-legal',
    'ecfr.gov': 'official-legal', 'federalregister.gov': 'official-legal',
    'gov.uk': 'official-legal', 'energy.gov': 'official-legal',
    'darpa.mil': 'official-legal', 'ntrs.nasa.gov': 'official-legal',
    'primis.phmsa.dot.gov': 'official-legal', 'fcc.gov': 'official-legal',
    'iso.org': 'official-legal', 'bipm.org': 'official-legal',
    'nist.gov': 'official-legal', 'tsapps.nist.gov': 'official-legal',
    'itu.int': 'official-legal', 'iana.org': 'official-legal',
    'rfc-editor.org': 'official-legal', 'w3.org': 'official-legal',
    'unicode.org': 'official-legal', 'ich.unesco.org': 'official-legal',
    'whc.unesco.org': 'official-legal', 'iea.org': 'official-legal',
    'lne.fr': 'official-legal', 'pubs.usgs.gov': 'official-legal',
    'ohp.parks.ca.gov': 'official-legal', 'nps.gov': 'official-legal',
    'home.cern': 'official-legal', 'nobelprize.org': 'official-legal',
    'aaas.confex.com': 'official-legal',
    # --- patents
    'patents.google.com': 'patent', 'dpma.de': 'patent', 'inpi.fr': 'patent',
    'lemelson.mit.edu': 'museum-archive-library', 'invent.org': 'reference-work',
    # --- peer reviewed
    'dergipark.org.tr': 'peer-reviewed', 'doi.org': 'peer-reviewed',
    'nature.com': 'peer-reviewed', 'science.org': 'peer-reviewed',
    'pnas.org': 'peer-reviewed', 'cambridge.org': 'peer-reviewed',
    'assets.cambridge.org': 'peer-reviewed', 'academic.oup.com': 'peer-reviewed',
    'global.oup.com': 'peer-reviewed', 'mdpi.com': 'peer-reviewed',
    'link.springer.com': 'peer-reviewed', 'arxiv.org': 'peer-reviewed',
    'pmc.ncbi.nlm.nih.gov': 'peer-reviewed', 'pubmed.ncbi.nlm.nih.gov': 'peer-reviewed',
    'nlm.nih.gov': 'peer-reviewed', 'journals.linguisticsociety.org': 'peer-reviewed',
    'publications.dainst.org': 'peer-reviewed', 'ojs.utlib.ee': 'peer-reviewed',
    'scholarship.law.wm.edu': 'peer-reviewed', 'isamveri.org': 'peer-reviewed',
    'ajaonline.org': 'peer-reviewed', 'tyndalebulletin.org': 'peer-reviewed',
    'aeaweb.org': 'peer-reviewed', 'ojs.aaai.org': 'peer-reviewed',
    'semanticscholar.org': 'peer-reviewed', 'academia.edu': 'peer-reviewed',
    'eprints.rclis.org': 'peer-reviewed', 'e-docs.geo-leo.de': 'peer-reviewed',
    'al-qantara.revistas.csic.es': 'peer-reviewed', 'hoyuk.gov.tr': 'peer-reviewed',
    'ieeephotonics.org': 'peer-reviewed', 'tms.org': 'peer-reviewed',
    'journals.sagepub.com': 'peer-reviewed',
    # --- university / institute
    'uvm.edu': 'university-or-institute', 'epigraphy.osu.edu': 'university-or-institute',
    'uwyo.edu': 'university-or-institute', 'acikerisim.fsm.edu.tr': 'university-or-institute',
    'ikf.marmara.edu.tr': 'university-or-institute', 'jfa.arch.metu.edu.tr': 'university-or-institute',
    'penelope.uchicago.edu': 'university-or-institute', 'waters.iath.virginia.edu': 'university-or-institute',
    'discovery.ucl.ac.uk': 'university-or-institute', 'cs.virginia.edu': 'university-or-institute',
    'titus.fkidg1.uni-frankfurt.de': 'university-or-institute', 'kit.edu': 'university-or-institute',
    'unibo.it': 'university-or-institute', 'umontpellier.fr': 'university-or-institute',
    'lk.cs.ucla.edu': 'university-or-institute', 'cvml.ista.ac.at': 'university-or-institute',
    'news.mit.edu': 'university-or-institute', 'news.cornell.edu': 'university-or-institute',
    'nit-istanbul.net': 'university-or-institute', 'curation.cs.manchester.ac.uk': 'university-or-institute',
    'max-eup2012.mpipriv.de': 'university-or-institute', 'sites.utexas.edu': 'university-or-institute',
    'hmmlschool.org': 'university-or-institute', 'oxyrhynchus.web.ox.ac.uk': 'university-or-institute',
    'doaks.org': 'university-or-institute', 'makingscience.royalsociety.org': 'university-or-institute',
    'arts.ircica.org': 'university-or-institute', 'chilton-computing.org.uk': 'university-or-institute',
    'linguistics.berkeley.edu': 'university-or-institute',
    # --- museum / archive / library
    'metmuseum.org': 'museum-archive-library', 'britishmuseum.org': 'museum-archive-library',
    'collections.vam.ac.uk': 'museum-archive-library', 'islamicceramics.ashmolean.org': 'museum-archive-library',
    'si.edu': 'museum-archive-library', 'americanhistory.si.edu': 'museum-archive-library',
    'library.si.edu': 'museum-archive-library', 'invention.si.edu': 'museum-archive-library',
    'collection.sciencemuseumgroup.org.uk': 'museum-archive-library',
    'sciencemuseum.org.uk': 'museum-archive-library',
    'blog.scienceandmediamuseum.org.uk': 'museum-archive-library',
    'computerhistory.org': 'museum-archive-library', 'www.computerhistory.org': 'museum-archive-library',
    'slub-dresden.de': 'museum-archive-library', 'moma.org': 'museum-archive-library',
    'spotlight.vatlib.it': 'museum-archive-library', 'kutuphane.ttk.gov.tr': 'museum-archive-library',
    'devletarsivleri.gov.tr': 'museum-archive-library', 'archive.org': 'museum-archive-library',
    'dlib.nyu.edu': 'museum-archive-library', 'archive.nyu.edu': 'museum-archive-library',
    'trismegistos.org': 'museum-archive-library', 'renvenetian.cmog.org': 'museum-archive-library',
    'glassmaking.cmog.org': 'museum-archive-library', 'blog.cmog.org': 'museum-archive-library',
    'hagley.org': 'museum-archive-library', 'english-heritage.org.uk': 'museum-archive-library',
    'historicengland.org.uk': 'museum-archive-library',
    'heritagerecords.nationaltrust.org.uk': 'museum-archive-library',
    'sitelines.newcastle.gov.uk': 'museum-archive-library',
    'beta.nationalarchives.gov.uk': 'museum-archive-library', 'europeana.eu': 'museum-archive-library',
    'ccel.org': 'museum-archive-library', 'auer-von-welsbach-museum.at': 'museum-archive-library',
    'islamicart.museumwnf.org': 'museum-archive-library', 'ebsco.com': 'museum-archive-library',
    'aibl.fr': 'museum-archive-library', 'bl.uk': 'museum-archive-library',
    'porthouston.com': 'corporate-or-interested-party',
    # --- reference works
    'islamansiklopedisi.org.tr': 'reference-work', 'turkmaarifansiklopedisi.org.tr': 'reference-work',
    'britannica.com': 'reference-work', 'ethw.org': 'reference-work',
    'istanbultarihi.ist': 'reference-work',
    # --- tertiary
    'en.wikipedia.org': 'tertiary-open-encyclopedia', 'tr.wikipedia.org': 'tertiary-open-encyclopedia',
    # --- professional / trade bodies
    'spectrum.ieee.org': 'professional-or-trade-body', 'aapg.org': 'professional-or-trade-body',
    'arrl.org': 'professional-or-trade-body', 'nanog.org': 'professional-or-trade-body',
    'internetsociety.org': 'professional-or-trade-body', 'fmi.org': 'professional-or-trade-body',
    'support.gs1.org': 'professional-or-trade-body', 'higherlogicdownload.s3.amazonaws.com': 'professional-or-trade-body',
    'tshaonline.org': 'professional-or-trade-body',
    # --- corporate / interested party
    'ibm.com': 'corporate-or-interested-party', 'ti.com': 'corporate-or-interested-party',
    'bayer.com': 'corporate-or-interested-party', 'asml.com': 'corporate-or-interested-party',
    'investors.seagate.com': 'corporate-or-interested-party',
    'conocophillips.com': 'corporate-or-interested-party',
    'faber-castell.cz': 'corporate-or-interested-party', 'kingkullen.com': 'corporate-or-interested-party',
    'news.gm.com': 'corporate-or-interested-party', 'doctorwho.tv': 'corporate-or-interested-party',
    'mea.bic.com': 'corporate-or-interested-party', 'iznik.com': 'corporate-or-interested-party',
    'counterpointresearch.com': 'corporate-or-interested-party',
    'atlanticcouncil.org': 'corporate-or-interested-party', 'fee.org': 'corporate-or-interested-party',
    'thomasthwaites.com': 'corporate-or-interested-party', 'prnewswire.com': 'corporate-or-interested-party',
    'lexpera.com.tr': 'corporate-or-interested-party', 'turkiyeninustalari.org': 'corporate-or-interested-party',
    'pewresearch.org': 'university-or-institute', 'ourworldindata.org': 'university-or-institute',
    # --- news media
    'hurriyet.com.tr': 'news-media', 'sabah.com.tr': 'news-media', 'dailysabah.com': 'news-media',
    'voanews.com': 'news-media', 'bnrnews.bg': 'news-media', 'malaymail.com': 'news-media',
    'chinadaily.com.cn': 'news-media', 'caixinglobal.com': 'news-media', 'forbes.com': 'news-media',
    'gizmodo.com': 'news-media', 'smithsonianmag.com': 'news-media', 'pbs.org': 'news-media',
    'lngindustry.com': 'news-media', 'chemistryworld.com': 'news-media', 'journo.com.tr': 'news-media',
    'yedikita.com.tr': 'news-media', 'hyperallergic.com': 'news-media', 'thebeliever.net': 'news-media',
    'themarginalian.org': 'news-media', 'courier.unesco.org': 'news-media',
    'lindahall.org': 'museum-archive-library', 'sciencehistory.org': 'museum-archive-library',
    # --- blogs / personal compilations
    'historyofinformation.com': 'blog-or-personal-compilation',
    'kiwihellenist.blogspot.com': 'blog-or-personal-compilation',
    'ageofinvention.xyz': 'blog-or-personal-compilation',
    'ed-thelen.org': 'blog-or-personal-compilation',
    'solar.lowtechmagazine.com': 'blog-or-personal-compilation',
    'construction-physics.com': 'blog-or-personal-compilation',
    'worksinprogress.co': 'blog-or-personal-compilation',
    'thebyzantinelegacy.com': 'blog-or-personal-compilation',
    'romanaqueducts.info': 'blog-or-personal-compilation',
    'daktilo1984.com': 'blog-or-personal-compilation',
    'georgehewitt.net': 'blog-or-personal-compilation',
    'asimov.press': 'blog-or-personal-compilation',
    'monika-schnitzer.com': 'blog-or-personal-compilation',
    'explorepahistory.com': 'blog-or-personal-compilation',
    'savewright.org': 'blog-or-personal-compilation',
    'turkiyeturizmansiklopedisi.com': 'blog-or-personal-compilation',
    'muslimheritage.com': 'blog-or-personal-compilation',
    'the-past.com': 'blog-or-personal-compilation',
    'abkhazworld.com': 'blog-or-personal-compilation',
    'worldhistory.org': 'blog-or-personal-compilation',
    'cepr.org': 'university-or-institute',
    'ismetinonu.org.tr': 'blog-or-personal-compilation',
    'yalantarih.com': 'blog-or-personal-compilation',
    'turkyurdu.com.tr': 'blog-or-personal-compilation',
    'sp.gov.tr': 'official-legal',
}


def host(url):
    h = (urlparse(url).netloc or '').lower()
    return h[4:] if h.startswith('www.') else h


def source_type(url):
    h = host(url)
    if h in DOMAIN_TYPE:
        return DOMAIN_TYPE[h]
    # eşleşmeyenler için ihtiyatlı son çare kuralları
    if h.endswith('.gov') or h.endswith('.gov.tr') or h.endswith('.gov.uk'):
        return 'official-legal'
    if h.endswith('.edu') or h.endswith('.edu.tr') or h.endswith('.ac.uk'):
        return 'university-or-institute'
    return 'UNCLASSIFIED:' + h


# ---------------------------------------------------------------- index.html
def read_var(html, name):
    m = re.search(r'^var %s = ' % re.escape(name), html, re.M)
    if not m:
        raise SystemExit('değişken bulunamadı: ' + name)
    i = m.end()
    depth, instr, esc, start = 0, False, False, i
    while i < len(html):
        c = html[i]
        if instr:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == '"': instr = False
        else:
            if c == '"': instr = True
            elif c in '[{': depth += 1
            elif c in ']}':
                depth -= 1
                if depth == 0:
                    return html[start:i + 1]
        i += 1
    raise SystemExit('değişken kapanmadı: ' + name)


def js_to_json(src):
    """evidence dizisi JS nesne değişmezidir; anahtarları tırnaklayıp JSON'a çevirir."""
    out, i, instr, esc = [], 0, False, False
    while i < len(src):
        c = src[i]
        if instr:
            out.append(c)
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == '"': instr = False
            i += 1
            continue
        if c == '"':
            instr = True; out.append(c); i += 1; continue
        m = re.match(r'([A-Za-z_$][\w$]*)\s*:', src[i:])
        if m and (not out or out[-1] in '{,' or out[-1].isspace()):
            out.append('"%s":' % m.group(1)); i += m.end(); continue
        out.append(c); i += 1
    txt = ''.join(out)
    txt = re.sub(r',(\s*[\]}])', r'\1', txt)
    return json.loads(txt)


# ---------------------------------------------------------------- yazım
def write_csv(path, header, rows):
    with io.open(path, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(header)
        w.writerows(rows)


def main(index_path='index.html', out_dir='data'):
    html = io.open(index_path, encoding='utf-8').read()
    products = json.loads(read_var(html, 'products'))
    evidence = js_to_json(read_var(html, 'evidence'))
    model_map = js_to_json(read_var(html, 'MODEL_MAP'))
    chain_links = json.loads(read_var(html, 'CHAIN_LINKS'))

    os.makedirs(out_dir, exist_ok=True)
    unclassified = Counter()

    def st(u):
        t = source_type(u)
        if t.startswith('UNCLASSIFIED'):
            unclassified[t.split(':', 1)[1]] += 1
        return t

    # -------- events.csv
    ev_rows = []
    for o in products:
        for n, t in enumerate(o['timeline'], 1):
            ev_rows.append([o['id'], o['name'][1], o['name'][0], o['civ'], o['cat'],
                            1 if (o['cat'] == 'loss' or o.get('broke')) else 0, n, t['y'], t['link'],
                            t['t'][0], t['t'][1], t.get('src', ''), st(t.get('src', ''))])
    write_csv(os.path.join(out_dir, 'events.csv'),
              ['object_id', 'object_name_en', 'object_name_tr', 'civilisation', 'category',
               'chain_broke', 'event_index', 'year', 'link', 'claim_tr', 'claim_en',
               'source_url', 'source_type'], ev_rows)

    # -------- objects.csv
    ob_rows = []
    for o in products:
        yrs = [t['y'] for t in o['timeline']]
        weakest = o['weakest']['k']
        mm = model_map.get(weakest, {})
        ob_rows.append([o['id'], o['name'][1], o['name'][0], o['civ'], o['cat'],
                        1 if (o['cat'] == 'loss' or o.get('broke')) else 0, o['era'][1], o['era'][0],
                        len(o['timeline']), min(yrs), max(yrs), weakest,
                        mm.get('state', ''), mm.get('slider', ''),
                        strip(o['weakest']['why'][1]), strip(o['weakest']['why'][0]),
                        strip(o['nearBreak'][1]), strip(o['nearBreak'][0]),
                        strip(o['thesis'][1]), strip(o['thesis'][0]),
                        len(o.get('sources', []))])
    write_csv(os.path.join(out_dir, 'objects.csv'),
              ['object_id', 'name_en', 'name_tr', 'civilisation', 'category', 'chain_broke',
               'era_en', 'era_tr', 'n_events', 'year_first', 'year_last', 'thinnest_link',
               'model_coverage', 'model_slider', 'thinnest_why_en', 'thinnest_why_tr',
               'near_break_en', 'near_break_tr', 'what_it_does_not_show_en',
               'what_it_does_not_show_tr', 'n_sources'], ob_rows)

    # -------- model-coverage.csv
    mc_rows = []
    for o in products:
        weakest = o['weakest']['k']
        cnt = Counter(t['link'] for t in o['timeline'])
        for link in chain_links:
            mm = model_map.get(link, {})
            mc_rows.append([o['id'], link, 1 if link == weakest else 0, cnt.get(link, 0),
                            mm.get('state', ''), mm.get('slider', '')])
    write_csv(os.path.join(out_dir, 'model-coverage.csv'),
              ['object_id', 'link', 'is_thinnest_link', 'n_events_coded_to_link',
               'model_represents_link', 'model_slider'], mc_rows)

    # -------- evidence.csv
    # Kanıt şeridi kayıtları + `ev` alanı taşıyan zincir haritaları (index.html'deki
    # evidence.concat(...) ile aynı kural).
    ev_cat = json.loads(read_var(html, 'EV_CAT'))
    for o in products:
        if o.get('ev'):
            e = o['ev']
            evidence.append({'id': o['id'], 'origin': 'chain-map',
                             'cat': ev_cat.get(o['id'], o['cat']),
                             'year': e.get('year'), 'start': e.get('start'), 'end': e.get('end'),
                             'type': e.get('type'), 'conf': 'medium' if e.get('conf') == 'med' else e.get('conf'),
                             'title': o['name'], 'region': e['region'], 'role': e['role'],
                             'shows': e['shows'], 'limits': e['limits'],
                             'source': e['source'], 'url': e.get('url', '')})
    evidence.sort(key=lambda e: (e.get('year') if e.get('year') is not None else 0))
    ec_rows = []
    for e in evidence:
        ec_rows.append([e['id'], e.get('origin', 'evidence-strip'), e.get('cat', ''), e.get('year', ''),
                        e.get('start', ''), e.get('end', ''), e.get('type', ''), e.get('conf', ''),
                        e['title'][1], e['title'][0], e['region'][1], e['region'][0],
                        e['role'][1], e['role'][0],
                        strip(e['shows'][1]), strip(e['shows'][0]),
                        strip(e['limits'][1]), strip(e['limits'][0]),
                        e['source'][1], e['source'][0], e.get('url', ''), st(e.get('url', ''))])
    write_csv(os.path.join(out_dir, 'evidence.csv'),
              ['record_id', 'origin', 'category', 'year', 'range_start', 'range_end',
               'record_type', 'confidence', 'title_en', 'title_tr', 'region_en', 'region_tr',
               'role_en', 'role_tr', 'shows_en', 'shows_tr', 'does_not_show_en',
               'does_not_show_tr', 'source_en', 'source_tr', 'source_url', 'source_type'], ec_rows)

    # -------- sources.csv
    uses, users = Counter(), {}
    for o in products:
        for t in o['timeline']:
            u = t.get('src', '')
            if u:
                uses[u] += 1; users.setdefault(u, set()).add(o['id'])
        for s in o.get('sources', []):
            uses[s['u']] += 1; users.setdefault(s['u'], set()).add(o['id'])
    for e in evidence:
        u = e.get('url', '')
        if u:
            uses[u] += 1
            users.setdefault(u, set()).add(e.get('origin', 'evidence-strip'))
    sc_rows = [[u, st(u), n, ' '.join(sorted(users[u]))] for u, n in sorted(uses.items())]
    write_csv(os.path.join(out_dir, 'sources.csv'),
              ['source_url', 'source_type', 'n_uses', 'used_by'], sc_rows)

    # -------- corpus.json (BOM'suz)
    corpus = OrderedDict([
        ('title', {'tr': 'Aktarım Zinciri', 'en': 'The Transmission Chain'}),
        ('licence', 'CC BY 4.0 (metin ve veri) · MIT (kod)'),
        ('generated_by', 'tools/export-data.py'),
        ('source_type_vocabulary', SOURCE_TYPES),
        ('objects', products),
        ('evidence', evidence),
    ])
    with io.open(os.path.join(out_dir, 'corpus.json'), 'w', encoding='utf-8') as f:
        json.dump(corpus, f, ensure_ascii=False, indent=1)
        f.write('\n')

    # -------- özet
    print('nesne %d · olay %d · kanıt %d · benzersiz kaynak %d'
          % (len(products), len(ev_rows), len(ec_rows), len(sc_rows)))
    mix = Counter(r[1] for r in sc_rows)
    for t in SOURCE_TYPES:
        if mix.get(t):
            print('  %-32s %d' % (t, mix[t]))
    if unclassified:
        print('\nSINIFLANDIRILAMAYAN ALAN ADLARI (DOMAIN_TYPE tablosuna eklenmeli):')
        for h, n in unclassified.most_common():
            print('  %s (%d)' % (h, n))
        return 1
    return 0


def strip(s):
    return re.sub(r'<[^>]+>', '', s or '').replace(' ', ' ').strip()


if __name__ == '__main__':
    sys.exit(main(*(sys.argv[1:] or ['index.html', 'data'])))
