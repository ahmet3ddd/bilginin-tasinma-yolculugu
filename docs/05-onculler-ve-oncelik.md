# Öncüller ve Öncelik — Prior Art Raporu
## "Aktarım Zinciri / The Transmission Chain" · v5.1 için güncellendi, 23 Ağustos 2026

Yedi ayrı literatür bağımsız olarak tarandı: örtük bilgi ve bilim sosyolojisi · kültürel
evrim ve teknoloji kaybı · dijital koruma ve arşiv bilimi · STS, altyapı ve bakım
çalışmaları · sıkıştırma, dış bellek ve dağıtık biliş · tezler, uzun vadeli mesajlaşma
projeleri ve biçim rakipleri · **yazı sistemlerinin ölümü ve dil tehlikesi (bölüm 2.7).**

Aşağıdaki her kaynak fiilen açılıp doğrulandı. Açılamayanlar bölüm 7'de listelidir ve
**alıntılanmadan önce elle kontrol edilmelidir.**

*(Bu raporun gerektirdiği düzeltmeler çalışmaya işlendi — Yöntem sekmesindeki "Öncüller ve
konum" bölümüne bakın. Rapor, o bölümün gerekçe belgesi olarak burada durur.)*

---

# 1. HÜKÜM

**Sorunun cevabı: evet, hem de fazlasıyla.**

Çalışmanın 1., 3., 4. ve 5. iddiaları — "bilgi taşınır, bağlam taşınmaz", "altı farklı
kayıp mekanizması ayrı çareler ister", "arşiv, onu yeniden çalıştırma kapasitesinden hızlı
büyür", "ilerleme ağın birlikte yaşamasıdır" — **hiçbiri yeni değil.** Her biri en az bir,
çoğu üç-dört ayrı literatürde daha önce, daha dar ve daha kanıtlı biçimde söylenmiş.

Ama bu, çalışmanın değersiz olduğu anlamına gelmiyor. Şunu söylüyor:

> **Bu bir keşif değil, bir sentez ve bir alet.** Böyle çerçevelenirse sağlam durur;
> keşif diye sunulursa ilk uzman okuyucuda düşer.

**Üç şey acil düzeltme istedi** (bölüm 3) ve v5.0'da yapıldı. **Yedinci literatür**
(bölüm 2.7) v5.1'de eklendi. **Dört şey gerçekten özgün kalıyor** (bölüm 4).

---

# 2. HER ALANDA "BUNU ZATEN YAPMIŞLAR"

## 2.1 Örtük bilgi ve bilim sosyolojisi → **Harry Collins**

**"Tacit Knowledge, Trust and the Q of Sapphire", *Social Studies of Science* 31(1), 2001,
71–85.** https://journals.sagepub.com/doi/abs/10.1177/030631201031001004

Rus safir ölçümlerinin yirmi yıl tekrarlanamamasını açıklarken **beş kategorili bir örtük
bilgi sınıflandırması** yayınlıyor: *concealed* · *mismatched salience* · *ostensive* ·
*unrecognised* · *uncognizable* — her biri için ayrı çare öneriyor. **Bu, çalışmanın 3.
iddiasının yapısı ve retoriği.**

Yanına zorunlu ikisi: **Collins, *Tacit and Explicit Knowledge*, Chicago UP, 2010**
(bir "string"in alıcıda etki üretmesi için gereken beş koşul — altı halkanın en yakın
yapısal öncülü) ve **MacKenzie & Spinardi, *AJS* 101(1), 1995, 44–99**
(https://www.journals.uchicago.edu/doi/abs/10.1086/230699) — manşet iddiamızın kanonik
vakası ve alanın terimini icat eden makale: **"uninvention"**.

Ayrıca hazır bir sözcük: Cowan, David & Foray'ın **"displaced codebook"**ü — "çözücü
kaybı"nın ekonomideki adı. https://unu-merit.nl/publications/rmpdf/1999/rm1999-027.pdf

## 2.2 Kültürel evrim → **Alex Mesoudi**

**"Variable Cultural Acquisition Costs Constrain Cumulative Cultural Evolution", *PLoS
ONE* 6(3): e18239, 2011.**
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0018239

| Bizim parametre | Mesoudi'deki karşılığı |
|---|---|
| K — sabit öğrenme bütçesi | **λ** — bireyin ömrü boyunca öğrenmeye ayırabileceği toplam çaba |
| G — paketleme kazancı | **μ_s, μ_i** — biriken karmaşıklık arttıkça edinme maliyeti düşer |
| "arşiv, yeniden çalıştırma kapasitesini aşar" | makalenin **manşet bulgusu** |

**Bu, bizim 4. iddiamız — hakemli bir dergide, on beş yıl önce.**

- **Henrich 2004**, *American Antiquity* 69(2): `Δz̄ = −α + β(ε + ln N)` — kayıp modelinin atası. https://henrich.fas.harvard.edu/publications/demography-and-cultural-evolution-how-adaptive-cultural-processes-can-produce
- **Enquist, Ghirlanda & Eriksson 2011**, *Phil Trans R Soc B* 366: `n(t+1) = (1 − q_dis)·n_t + q_app·(m − n_t)`. https://doi.org/10.1098/rstb.2010.0132
- **Miton & DeDeo 2022**, *J R Soc Interface* 19 — örtük bilginin biçimsel modeli ve geri getirilemezlik iddiası. https://arxiv.org/abs/2201.03582
- **Rivers 1912, "The Disappearance of Useful Arts"** — 114 yıl önceki kayıp taksonomisi. https://en.wikisource.org/wiki/The_Disappearance_of_Useful_Arts

## 2.3 Dijital koruma → **OAIS ve SPOT**

**Altı halkamızın beşi ISO düzeyinde tanımlı terimler.** CCSDS 650.0-M-3 / ISO 14721:
https://ccsds.org/Pubs/650x0m3.pdf

| Bizim halka | OAIS'teki adı |
|---|---|
| Paket | **Data Object** |
| Çözücü | **Representation Information** + **Designated Community** |
| Bağlam | kelimesi kelimesine **Context Information** |
| Aparat | **Representation Information Network** |
| Bakım | altı **Mandatory Responsibility** |

Ve altı-parçalı bir model zaten var: **Vermaaten, Lavoie & Caplan, SPOT modeli, *D-Lib*
2012** — altı özellik, her biri kendi tehdit listesiyle.
http://www.dlib.org/dlib/september12/vermaaten/09vermaaten.html

**Thibodeau 2002:** "Bir dijital belgeyi fiziksel nesne olarak korumak imkânsızdır;
korunabilecek olan, onu yeniden üretebilme yeteneğidir."
https://www.clir.org/pubs/reports/pub107/thibodeau/

## 2.4 STS ve bakım → **Latour, Star, Russell & Vinsel**

Taşınan paketin adı 1986'dan beri var: **Latour'un immutable mobile'ı.**
https://www.bruno-latour.fr/sites/default/files/21-DRAWING-THINGS-TOGETHER-GB.pdf —
ve değişmezliğin matbaanın, optiğin ve standart aletlerin başarısı olduğunu söyleyerek
*aparat* halkasını da teslim ediyor.

**Star, "The Ethnography of Infrastructure", 1999** — "altyapı bozulunca görünür olur":
bütün teşhis yöntemimizin önceden tarifi.
https://ics.uci.edu/~wscacchi/GameLab/Recommended%20Readings/ethnography-infrastructure-Star-1999.pdf

**Russell & Vinsel, "Hail the Maintainers", *Aeon*, 2016** — sonuç cümlemizin popüler hâli.
https://aeon.co/essays/innovation-is-overvalued-maintenance-often-matters-more

**Edgerton, *The Shock of the Old* (2006)** — teknolojiler kaybolmaz, terk edilir.

## 2.5 Sıkıştırma ve dış bellek → **Kirby ekibi ve Merlin Donald**

**Kirby, Tamariz, Cornish & Smith, *Cognition* 141, 2015, 87–102** — yapı,
sıkıştırılabilirlik ile ifade gücü arasındaki ödünleşmeden doğuyor. "Bilginin ziplenmesi"
bir metafor değil, ölçülmüş bir olgu. https://pubmed.ncbi.nlm.nih.gov/25966840/

**Donald, *Origins of the Modern Mind*, 1991** — engram/exogram; sabit biyolojik bellek,
büyüyen kolektif arşiv. http://cogweb.ucla.edu/Abstracts/Donald_91.html

**Jones, "The Burden of Knowledge", *RESt* 76(1), 2009** — aynı iddia, patent verisiyle
sınanmış. https://www.nber.org/papers/w11360

## 2.6 Tezler, mühendislik ve biçim rakipleri

**Olshin, *Lost Knowledge*, Brill, 2019** — argüman omurgamızın en yakın akademik ikizi.
https://searchworks.stanford.edu/view/13159230

**Burja, "Intellectual Dark Matter", 2019** — *lost / proprietary / tacit* üçlemesi.
https://samoburja.com/intellectual-dark-matter/

**Ve en ciddi boşluk: bu problemi bizden önce çözmeye çalışanlar** — Human Interference
Task Force (1981) · Sebeok'un "atom rahipliği" (1984) · Bastide & Fabbri'nin ışın kedileri
(http://www.theraycatsolution.com/) · Sandia'nın WIPP raporu (https://www.osti.gov/biblio/10117359) ·
Long Now Rosetta Diski (https://rosettaproject.org/disk/interactive/) · Memory of Mankind
(https://www.memory-of-mankind.com/) · Voyager ve Arecibo · ve **GitHub Arctic Code
Vault'un "Tech Tree"si** (https://github.com/github/archive-program/blob/master/TheTechTree.md) —
zinciri tarif etmekle kalmadılar, inşa ettiler.

## 2.7 Yazı ve dil → **iki tam alan** *(v5.1'de eklendi)*

Bu, taramada bulunan yedinci literatürdür ve v5.0'da atlanmıştı. Burada, diğer altı
başlıkla **aynı ağırlıkta** duruyor: tezin özel bir kolu değil, sıradaki bir alan.

### Yazı sistemlerinin ölümü — 2003'ten beri adı konmuş

**Stephen Houston, John Baines & Jerrold Cooper, "Last Writing: Script Obsolescence in
Egypt, Mesopotamia, and Mesoamerica", *Comparative Studies in Society and History* 45:3
(Temmuz 2003), 430–479.**
https://www.cambridge.org/core/journals/comparative-studies-in-society-and-history/article/abs/last-writing-script-obsolescence-in-egypt-mesopotamia-and-mesoamerica/D9722CE8975BE16A71729D2DF555F036

Saydıkları beş ölüm nedeni **bakım halkasına birebir oturuyor:** yazıcı eğitimine yapılan
kurumsal yatırımın kesilmesi · işlevin idari ya da dinî bir alana daralması · siyasi güç
tarafından bastırılma · tek bir aristokrat kullanıcı sınıfına bağlılık · daha az yük
taşıyan rakip bir yazının bulunması. 2004'te Oxford'da yalnız bu konu için bir konferans
toplandı; kitabı **Baines, Bennet & Houston (der.), *The Disappearance of Writing
Systems*, Equinox, 2008** olarak çıktı.
https://equinoxonlinelibrary.com/book/684/the-disappearance-of-writing-systems

Yayıncının kendi çerçevesi bir itiraf: icat ve şifre çözme iyi çalışılmıştır, "tutulma ya
da yerini bırakma" ise az çalışılmıştır. Yani bu çalışmanın işaret ettiği asimetriyi alan
kendisi de teşhis etmiş durumda.

### Dil tehlikesi — ve tezin bir BM belgesine yazılmış hâli

Alanı **Krauss ve diğerleri, "Endangered Languages", *Language* 68(1), 1992, 1–42**
kurdu. https://bpb-us-e2.wpmucdn.com/websites.umass.edu/dist/e/4245/files/2013/06/EndangeredLang1992.pdf
Krauss'un ölçütü paketin varlığı değil, **çocukların dili öğrenip öğrenmediğidir** — yani
doğrudan bakım halkası.

**Nikolaus Himmelmann, "Documentary and descriptive linguistics", *Linguistics* 36, 1998,
161–195.** https://bpb-us-w2.wpmucdn.com/voices.uchicago.edu/dist/1/140/files/2013/11/himmelmann-documentary-and-descriptive-linguistics.pdf
*Belgeleme* ile *betimleme*yi ayrı disiplinler ilan ediyor: betimleme sıkıştırılmış
pakettir (soyut bir dizge olarak dil), belgeleme ise paketin sonradan yeniden
bağlamlandırılabilmesi için çevresindeki pratiği saklama çabasıdır. **Bizim paket/bağlam
ayrımımız, bir disiplinin kuruluş gerekçesi olarak 1998'de yazılmış.**

**Ve en sert hâli: UNESCO Uzman Grubu, "Language Vitality and Endangerment", 2003.**
https://ich.unesco.org/doc/src/00120-EN.pdf *(fiilen açılıp doğrulandı)*

Dokuz faktörden ikisi bizim iki halkamız, **ayrı eksenlerde derecelendirilmiş:**

| | Faktör 1 — Kuşaklar arası aktarım | Faktör 9 — Belgelemenin miktarı ve kalitesi |
|---|---|---|
| **Derece 5** | Dil bütün kuşaklarca konuşuluyor | "Kapsamlı gramerler ve sözlükler, geniş metinler; bol miktarda açıklamalı yüksek kaliteli ses ve video kaydı" |
| **Derece 0** | "Konuşabilen ya da hatırlayan kimse yok" | Hiçbir malzeme yok |

Ve talimat, kelimesi kelimesine:

> **"Languages cannot be assessed simply by adding the numbers; we therefore suggest such
> simple addition not be done."**
> *(Diller sayılar toplanarak değerlendirilemez; bu yüzden böyle basit bir toplama
> yapılmamasını öneriyoruz.)*

Bir dil aynı anda **Faktör 9 = 5** ve **Faktör 1 = 0** olabilir. Toplamayı yasaklamaları,
paketin çözücünün yerini tutmadığının kurumsal beyanıdır. Ubıhça tam olarak bu vakadır.

**David Crystal, *Language Death*, Cambridge University Press, 2000, s. 3** madalyonun
öteki yüzünü verir: https://catdir.loc.gov/catdir/samples/cam032/99053220.pdf
*(doğrulandı)*

> "the moment the last speaker of an unwritten or unrecorded language dies, the archive
> disappears for ever."

Yani kaydı olmayan bir dilde **konuşanın kendisi arşivdir.** Bunun tersi — kayıt var,
konuşan yok — bu çalışmanın doldurduğu boşluktur.

### Bu alanın bize itirazı

Ve burası önemli: **bu alan dilin *özel* olduğunu savunur.** Evans, Hale, Nettle & Romaine
hepsi aynı çizgide — her dil benzersiz bir dünya görüşü, sınıflandırma dizgesi ve bilgi
birikimi kodlar; kaybı bir zanaatın ya da bir makinenin kaybına benzemez.

Bu çalışma tersini varsayıyor: **altı halka alandan bağımsızdır; dil, kuralın istisnası
değil en iyi belgelenmiş örneğidir.** Bu, alanın kendi retoriğini ters çeviren bir
konumdur ve çözülmüş değildir. Bu yüzden itiraz, çalışmanın içinde **karşı kaynaklar**
listesine kondu — ve dil, ayrıcalıklı bir vaka olarak değil, otuz bir nesneden biri
olarak, aynı sabit kuralla ölçülerek eklendi.

**Sonuç iddia lehine çıktı:** Ubıhçanın en ince halkası *bakım* — Roma su kemerleriyle ve
kodeksle aynı halka. Nesne değişiyor, kırılma noktası değişmiyor.

### Bu alanda kalan boşluk

Taramada tek bir kanonik makale bulunamadı: **"yazılı kayıt bir dil hakkında yapısal
olarak neyi atlar?"** Alan bunu defalarca gösteriyor ama bir yere yazmamış. Eyak vakası
en temiz kanıt: Fransız bir genç, Guillaume Leduey, Eyakçayı yalnız basılı ve sesli
malzemeden öğrendi — ama Krauss'un **yüz yüze vermek zorunda kaldığı** şey telaffuzdu.
Paket dilbilgisini ve sözlüğü taşıdı, boğumlanmayı taşımadı.

### Ek doğrulanamayanlar

- Tevfik Esenç'in doğum yılı (1904 / 1906) ve ölüm tarihi (7 / 8 Ekim 1992) kaynaklarda
  çelişiyor; çalışmada **1904** ve **7 Ekim** kullanıldı (Haspelmath'ın 1993 tarihli
  çağdaş duyurusunu izleyerek).
- Ubıhça ünsüz sayısı kaynaklara göre 80/81/82/84 arasında değişiyor; çalışmada
  Vikipedi'nin verdiği **84** (dördü yalnız alıntılarda) ve **üç** ünlü kullanıldı.
- Mezar taşındaki ifadenin **Türkçe aslı** doğrulanamadı; yalnız İngilizce çevirileri
  bulunabildi ve bu yüzden çalışmada alıntılanmadı.
- Pangloss arşivindeki kayıt sayısı (55) Vikipedi'den alındı; CNRS'in kendi sayfaları
  erişime kapalıydı.
- Evliya Çelebi'nin Kafkas yolculuğunun **yılı** doğrulanamadı; bu yüzden zaman haritasına
  tarihli bir olay olarak konmadı, yalnız paket halkası açıklamasında yüzyıl düzeyinde
  anıldı.

---

# 3. ÜÇ ACİL DÜZELTME *(v5.0'da yapıldı)*

**3.1 İngilizce başlık başka bir şeyin adı.** "Transmission chain" 1932'den beri Bartlett
paradigmasının adı. https://en.wikipedia.org/wiki/Transmission_chain_method
→ *v5.0: akrabalık sahiplenildi.*

**3.2 Kurucu metafor 1979'da çürütülmüş.** Reddy, "The Conduit Metaphor".
https://en.wikipedia.org/wiki/Conduit_metaphor → *v5.0: imge paketleme halkasına
daraltıldı, şerh basıldı.*

**3.3 İki vaka yazarlarının tezine ters kullanılıyordu.** Read'in "I, Pencil"ı
kendiliğinden düzen savunması; Thwaites'in tost makinesi sanayi bağımlılığı üzerine sanat
işi. → *v5.0: iki karta yazarların kendi okumaları eklendi.*

---

# 4. ÖZGÜN KALAN NE

1. **Altı halkanın tek adlandırılmış sistem olarak paketlenmesi** — birleşim kimsede yok.
2. **Literatürler arası köprü** — yedi alan birbirini okumuyor.
3. **Örtük bilginin eş-değer halka yapılması** — OAIS onu yalnız olumsuzdan tanıyor;
   dil tarafında da bu boşluk açık (bkz. 2.7).
4. **Etkileşimli anlatım kanonunda bu konu hiç yok** — explorabl.es'te tarih kategorisi
   bile yok. Argüman yeni değil; **argümanın çalıştırılabilir hâli yok.**
5. Osmanlı/Roma vaka seti, Ubıhça haritası ve modelin kendi aleyhine 30×6 → 31×6 sınavı.

---

# 5. KARŞI-KAYNAKLAR *(v5.0–v5.1'de çalışmaya işlendi)*

| Kaynak | Neyi vuruyor |
|---|---|
| Sims & Henke 2012 (https://journals.sagepub.com/doi/full/10.1177/0306312712437778) | Halkalar ikame edilebilir |
| Derex ve ark. 2019 (https://www.alexmesoudi.com/publication/derex-causal-2019/) | q_c'nin önemi |
| Rosenthal 2011 (https://blog.dshr.org/2011/02/are-we-facing-digital-dark-age.html) | Format eskimesi gerçekleşmedi |
| Charbonneau & Bourrat 2021 (https://pierrickbourrat.github.io/publication/a-30/a-30.pdf) | Sadakat betimleme tanesine göreli |
| Edgerton 2006 | Kayıp değil terk |
| Vaesen ve ark. 2016 (https://www.pnas.org/doi/10.1073/pnas.1520288113) | Nüfus açıklaması tartışmalı |
| Dartnell 2014 (http://the-knowledge.org/en-gb/the-book/) | Yeniden kurmak mümkün |
| **Evans, Hale, Nettle & Romaine** (https://assets.cambridge.org/97811070/41134/excerpt/9781107041134_excerpt.pdf) | **Dil özeldir — evrensellik iddiamıza itiraz** |

---

# 6. ZORUNLU ATIF LİSTESİ *(kaynakçaya girdi — 75 kayıt, 7 grup)*

Polanyi 1966 · Collins 2001 & 2010 · MacKenzie & Spinardi 1995 · OAIS/ISO 14721 ·
SPOT 2012 · Thibodeau 2002 · Mesoudi 2011 · Henrich 2004 · Enquist ve ark. 2011 ·
Miton & DeDeo 2022 · Rivers 1912 · Donald 1991 · Jones 2009 · Kirby ve ark. 2015 ·
Latour 1986 · Star 1999 · Russell & Vinsel 2016 · Reddy 1979 · Bartlett paradigması ·
Olshin 2019 · Burja 2019 · uygulanmış hat (HITF → Tech Tree) · **Houston, Baines & Cooper
2003 · Krauss ve ark. 1992 · Himmelmann 1998 · UNESCO 2003 · Crystal 2000.**

---

# 7. DOĞRULANAMAYANLAR

- **YÖK Ulusal Tez Merkezi** hiç sorgulanamadı — **Türkçe tez sorusu açık; elle
  aranmalıdır.**
- DART-Europe 3 Şubat 2025'te kalıcı kapandı; EThOS, BASE, OATD, NDLTD, ProQuest
  erişilemedi.
- MacKenzie & Spinardi tam metni; Polanyi sayfa numaraları; Kuny 1997; Rothenberg 1999
  gövdesi; Blow konuşmasının birincil videosu; Burja *Great Founder Theory* kanonik
  adresi; Eghbal "Roads and Bridges".
- Houston, Baines & Cooper'ın **tam metni** (yalnız yayıncı özeti ve kayıtları
  doğrulandı); "bir yazının tek bir okuyucuya ihtiyacı vardır" cümlesi yalnız üçüncü el
  bir alıntıdan geliyor ve **kullanılmadı.**
- Bölüm 2.7'nin sonundaki ek doğrulanamayanlar listesi.

**Hiçbir atıf, DOI ya da alıntı uydurulmamıştır.** Doğrulanamayan her madde açıkça
işaretlidir.
