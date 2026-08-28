# Kod Kitapçığı — Aktarım Zinciri halka-kodlu korpusu

**Veri kümesi sürümü** 1.0.0 · **Türetildiği kaynak** `index.html` v5.2, veri kesim
tarihi 23 Ağustos 2026
**Yazar** Ahmet Çandöken · ORCID https://orcid.org/0009-0001-5197-7888 · **Lisans** CC BY 4.0 (veri ve metin)

Bu kitapçık, bu klasördeki dosyaların işletim tarifidir. Çalışmayı hiç görmemiş bir
kodlayıcının bir kodlama kararını yeniden üretebilmesi ve **belirli bir yerde itiraz
edebilmesi** için yazıldı. Aşağıdaki her madde ya bir tanımdır, ya yayımlanmış kaynak
koddan olduğu gibi alınmış bir kuraldır, ya tam gücüyle beyan edilmiş bir sınırdır, ya da
yazarın kendi sözleriyle bildirdiği bir karardır. Hiçbiri çıkarım değildir: yalnız asıl
kodlayıcının bilebileceği bir şey varsa, tahmin edilmedi — soruldu ve olduğu gibi
aktarıldı.

---

## 1. Korpus nedir

**32 nesnenin** aktarım tarihinden, üç uygarlık katmanına dayanan (19 modern-sınai,
7 Osmanlı, 6 Roma), **tarihli ve tek tek kaynaklı 255 olayın** elle kodlanmış kaydı. Her
olay altı aktarım halkasından **tam birine** atanmıştır. Yanında, çalışmanın 100.000
yıllık grafiğinin kullandığı **38 tarihli kanıt kaydı** ve her nesne–halka çifti için
çalışmanın kendi kuşak modelinin o halkayı temsil edip edemediğini kaydeden bir
**32 × 6 matris** durur.

Korpus, etkileşimli bir çalışmanın ampirik katmanıdır. Çalışmanın argümanı, simülasyonu ve
düzyazısı bu veri kümesine **dâhil değildir** ve kullanmak için gerekmez.

### Dosyalar

| Dosya | Satır | Gözlem birimi |
|---|---|---|
| `events.csv` | 255 | bir nesnenin zincirinde tarihli, kaynaklı bir olay |
| `objects.csv` | 32 | bir nesne |
| `evidence.csv` | 38 | tarihli bir kanıt kaydı (23'ü kanıt şeridinden, 15'i zincir haritalarından) |
| `model-coverage.csv` | 192 | 32 × 6 matrisin bir nesne × halka hücresi |
| `sources.csv` | 291 | benzersiz bir kaynak adresi ve kullanım sayısı |
| `corpus.json` | — | kayıpsız dışa aktarım: özgün iki dilli alanlar, satır içi işaretlemesiyle, artı model parametreleri |

CSV dosyaları **BOM'lu** UTF-8, virgülle ayrılmış, RFC 4180 tırnaklama, başlık satırlı.
BOM bilinçlidir: onsuz Excel ve WPS Office dosyayı sistem kod sayfasıyla açar ve ASCII
dışındaki her karakter bozulur — iki dilli bir Türkçe veri kümesinde bu, metnin çoğu
demektir. Python'da `encoding='utf-8-sig'` ile okuyun; `pandas`, R ve çoğu araç BOM'u
kendisi ayıklar. `corpus.json` BOM taşımaz, RFC 8259 böyle gerektirir. CSV'deki metin
alanlarından satır içi HTML temizlendi ve boşluklar sadeleştirildi; `corpus.json` özgün
dizgileri **değiştirmeden** saklar. Bütün iki dilli alanlar `_tr` ve `_en` ekiyle iki kez
görünür; ikisi birbirinin çevirisidir, **bağımsız gözlem değildir.**

---

## 2. Altı halka — işletim tanımları

Halkalar kodlama kategorileridir. Sözcük dağarı dijital koruma ve örtük bilgi
literatürlerinde zaten vardır; altısından beşi OAIS / ISO 14721 terimlerine oturur
(bkz. §7). Aşağıdaki tanımlar bir kodlayıcının uygulayacağı hâlleridir: kavram olarak
değil, **karar sorusu** olarak yazıldı.

| Kod | Halka | Kodlayıcının sorduğu soru | En yakın yayımlanmış terim |
|---|---|---|---|
| `packet` | Paket | Bu olay **seçilmiş içeriğin kendisiyle** mi ilgili — yazılı tarif, çizim, formül, patent, standart, şartname, korpus, ya da neyin kaydedilmeye değer olduğu kararı? | OAIS *Data Object* |
| `decoder` | Çözücü | Bu olay **paketi okuyup uygulayabilen insanlar ve ortak dillerle** mi ilgili — ilgili yazıda okuryazarlık, eğitilmiş bir meslek, ortak bir notasyon, hedef topluluk? | OAIS *Representation Information* + *Designated Community* |
| `context` | Bağlam | Bu olay **neden çalıştığı, hangi sınırlarla ve hangi hata tarihiyle** ile mi ilgili — bir sonucun yanında giden ve onu yalnız okunur değil kullanılır kılan bilgi? | OAIS *Context Information* (terim birebir aynı) |
| `tacit` | Örtük bilgi | Bu olay **hiç yazıya geçmemiş el becerisi, atölye sırası ya da yargıyla** mı ilgili — yalnız sahibinin yanında çalışarak aktarılan şey? | Polanyi 1966; Collins 2001, 2010 |
| `apparatus` | Aparat | Bu olay **onu yapan ve okuyan makine ve aletlerle** mi ilgili — fırın, pres, okuyucu, ölçüm cihazı, kritik bir girdinin tedariki? | OAIS *Representation Information Network* |
| `maintenance` | Bakım | Bu olay **kopyalama ve öğretmeyi her kuşakta yenileyen tekrarlı emek, fon ya da kurumla** mı ilgili — vakıf, müfredat, çıraklık, bütçe, devlet? | OAIS *Mandatory Responsibilities*; Star 1999 |

### 2.1 Tek-halka kuralı ve bedeli

**Her olay tam bir halkaya kodlanır.** Bir olay birden fazla halkaya makul biçimde
dokunduğunda — ki çoğu dokunur — kodlayıcı, olayın **kanıt olduğu** halkayı seçer, sonuç
doğurduğu halkaları değil.

Bu kural bir sadeleştirmedir ve korpusun kodlayıcı anlaşmazlığına en açık tek yeridir.
Bilinen iki sistematik basınç:

- **Kurumsal olaylar** (yasak, bütçe, vakıf, sürgün) mekanizmaları aparat ya da çözücü
  üzerinden işlese bile `maintenance` kodlanır. Çalışmanın önceki bir sürümünün
  incelemecisi bunu haklı olarak işaretledi: tek bir kategori, altı halkalı şemanın
  başka türlü temsil etmediği bir **siyasal iktisadı** taşımak zorunda kalıyor.
- **Alet olayları**, aletin azlığı aslında bir bakım aksaması olduğunda bile `apparatus`
  kodlanır.

Tek-halka kuralına katılmayan bir kullanıcı çok etiketli bir kodlamayı `events.csv`'den
yeniden üretebilir: iddia metni her iki dilde de tam olarak oradadır.

### 2.2 Korpustaki halka sıklıkları

`apparatus` 58 · `packet` 53 · `maintenance` 49 · `decoder` 38 · `context` 32 · `tacit` 25

Bunlar **kodlanmış olay** sayılarıdır, önem sayıları değil. `tacit` en düşüktür, çünkü
örtük bilgi tanımı gereği en az belgelenen şeydir — bu, tarihsel kaydın bir özelliğidir,
olgunun değil, ve **bulgu olarak okunmamalıdır.**

---

## 3. En ince halka yargısı

Her nesne, altı halkadan hangisinin **bugün en kırılgan** olduğunu kaydeden tek bir alan
taşır: `thinnest_link`. Bu, tarihsel olarak hangi halkanın koptuğu değildir.

**Uygulanan karar kuralı:** her nesne için kodlayıcı şunu sorar — kaynaklı zaman
çizelgesine bakıldığında, şimdi hangi tek halka çökerse nesne en kısa sürede yeniden
üretilemez hâle gelir? Paket eksiksizken zincir yine de kopuyorsa, en ince halka tanım
gereği `packet` değildir.

**Dağılım:** `apparatus` 8 · `context` 8 · `maintenance` 7 · `tacit` 6 · `decoder` 2 ·
`packet` 1.

**Bu tek kodlayıcılı bir yargıdır.** Bkz. §6.1 — korpusun başlıca sınırı budur ve
yukarıdaki dağılım bir ölçüm değil **bir okuma** olarak ele alınmalıdır.

---

## 4. Nesne seçimi

**Örneklemin gözlenebilir özellikleri** (`objects.csv`'den doğrulanabilir):

- 32 nesne; **26 tutmuş, 6 kopmuş zincir** (`chain_broke`).
- Üç uygarlık katmanı: modern-sınai 19, Osmanlı 7, Roma 6.
- Altı tematik kategori: `threshold` 8, `everyday` 7, `info` 6, `loss` 5,
  `electronics` 4, `energy` 2.
- Olay yılları MÖ 700 ile MS 2026 arasında.
- Nesneler çalışmanın ardışık sürümlerinde eklendi; set 30'dan 32'ye büyüdü.

**Katılım kuralı.** Önceden konmuş biçimsel bir ölçüt yoktu. Nesneler yazarın ilgisini
çektiği için aday oldu; aday olduktan sonra, açılıp bağımsız denetlenebilen tarihli kaynak
bulunamayanlar çalışmadan çıkarıldı. Yani kaynak bulunabilirliği bir **seçim** değil, bir
**eleme** ölçütüydü. Bu gerekçeyle değerlendirilip alınmayan adaylar aşağıda listelidir.

Sonuçtaki bir düzenlilik, kullanıcı fark edeceği için yazılmalıdır: her nesne yedi ya da
sekiz tarihli olayla (ortanca 8) ve dört-altı ek okuma kaynağıyla temsil edilmiştir. Bu bir
hedef olarak konmadı; bitmiş korpusun bir özelliğidir ve sebebi belgelenmemiştir.

**Değerlendirilip alınmayan adaylar.**

*Mısır piramitleri.* Başlangıçta, nasıl yapıldıkları yeterince bilinmediği için kaynaklı
bir zaman çizelgesi çıkarılamayacağı düşünülerek elendi. Denetimde bunun literatürün değil
popüler anlatının konumu olduğu görüldü: Wadi el-Jarf papirüsleri (~MÖ 2560, Merer'in
Günlüğü) Keops piramidi için kireçtaşı taşınmasını çağdaş bir kayıtla belgeler ve rampa
ile iş gücü lojistiği üzerine yaşayan bir mühendislik literatürü vardır. Nesne yine de
alınmadı, ancak **kapsam gerekçesiyle**: eklenmesi çalışmanın anlatmak istediği şeyden
uzaklaştıracaktı. Bu kayıt, çalışmanın efsane düzeltmesi ölçütünün yazarın kendi kararına
uygulanmış hâli olarak burada durur.

*Cep telefonu.* Bileşen sayısı nedeniyle elendi: bu kadar çok bileşenli bir nesneyi altı
halkayla çözümlemek anlamlı bir sonuç vermeyecekti. Bu bilinçli bir kapsam kararıdır —
aynı sınırın **görünmesi** için bazı çok bileşenli teknolojik nesneler (entegre devre,
sabit disk, bilgisayar, internet) korpusta bilerek bırakılmıştır.

*Soyut kavramlar.* Kendi dönemlerinde de maddi bir taşıyıcısı olmayan kavramlar dışarıda
bırakıldı; böyle bir nesnede altı halkanın *paket* ve *aparat* halkaları tanımsız kalır.

*Genel ilke.* Benzer gerekçelerle daha fazla nesne eklemenin, anlatılmak istenen şeyden
uzaklaştıracağı değerlendirilmiştir; konu zaten karmaşık ve kavranması kolay değildir.

**Bundan açıkça çıkan sonuç:** bu, tanımlı bir evrenden değil, tek bir yazarın elinden çıkma
bir kolaylık örneklemidir. Rastgele değildir, temsilî değildir. Ondan hiçbir taban oran
hesaplanamaz ve "32'nin 26'sı tuttu" rakamı yalnız bu kısa listenin özelliğidir. Bkz. §6.2.

---

## 5. Model kapsama matrisi

`model-coverage.csv`, her nesne × halka hücresi için, çalışmanın kendi kuşak
simülasyonunun o halkayı temsil edebilecek herhangi bir terimi olup olmadığını kaydeder.
Buraya konmasının sebebi, tarih hakkında bir sonuç değil, **çalışmanın kendi aygıtının
denetimi** olmasıdır.

Eşleme bütün nesneler için sabittir ve kaynaktan olduğu gibi alınmıştır:

| Halka | Modelin temsili | Kaydırıcı |
|---|---|---|
| `context` | **tam** | `qc` |
| `decoder` | **tam** | `qd` |
| `packet` | **kısmî** | `gain` |
| `apparatus` | **kısmî** — yalnız arşiv yarı ömrünün içine gömülü | `halfLife` |
| `maintenance` | **kısmî** — ayrı terim yok; yarı ömrün içinde eriyor | `halfLife` |
| `tacit` | **yok** — hiçbir terim yok | — |

Her nesneyi **kendi en ince halkasının** temsil durumuna göre sınıflarsak:
**10 tam · 16 kısmî · 6 yok.** Yani 32 nesnenin 22'sinde model, nesnenin fiilen üzerinde
döndüğü halkayı temiz biçimde yalıtamıyor; 6'sında ise o halka için hiçbir terimi yok.

Nesne başına eğrileri süren senaryo kuralı da sabittir, nesneye özel ayar yoktur, ve
kaynaktan olduğu gibi buraya alınmıştır:

```js
/* en zayıf halkanın kaydırıcısı -> DÜŞÜK sabiti
   eşlenmiş diğer bütün kaydırıcılar -> SAĞLIKLI sabiti
   tacit'in kaydırıcısı yok: senaryo bilerek sağlıklı kalır, böylece modelin
   bu vakaya körlüğü örtülmek yerine eğrilerde GÖRÜNÜR olur. */
SCENARIO_RULE = {
  qc:       { low: .40, healthy: .90 },
  qd:       { low: .40, healthy: .90 },
  gain:     { low: 1.5, healthy: 4   },
  halfLife: { healthy: 45 }          // v5.3'ten beri DÜŞÜK değeri yok — aşağıya bakın
};
```

**v5.3'te bulunup düzeltilen bir kusur — daha önceki bütün sürümlerin eğrilerini
etkilediği için burada kayda geçiyor.** `apparatus` ve `maintenance` halkalarının ikisi de
`halfLife`'a eşlendiği ve bu motorda **daha kısa** bir arşiv yarı ömrü yeniden
kurulabilirliği **yükselttiği** için (40. nesilde süpürme: h=5 → R=3,54; h=10 → R=4,63;
zirve h≈12 → R=4,89; h=45 → R=3,11; h=100 → R=2,75), eski kural en ince halkası aparat ya
da bakım olan nesnelere h=10 veriyordu — optimumun kılpayı yanında. Bu yüzden onların
eğrileri çalışmanın **en sağlıklı** eğrileri olarak, sağlıklı bir zincirden %41,7 yukarıda
çiziliyordu — kodlanmış okumanın tam tersi. On beş nesne bu daldan geçiyordu; altı örtük
bilgi nesnesiyle birlikte 32 nesnenin 21'i, kırılganlık göstermesi gereken bir özellik
tarafından taban çizgisinde ya da üstünde gösteriliyordu.

v5.3'ten beri yarı ömür hiçbir vakada düşürülmüyor: aparat ve bakım tam olarak örtük bilgi
gibi ele alınıyor, senaryo bilerek sağlıklı bırakılıyor, ve o 21 nesne artık sağlıklı
zincir taban çizgisinde duruyor — bu, modelin onların döndüğü halka için terimi olmadığının
dürüst ifadesidir. **Model eğrileri hâlâ bir kırılganlık ölçüsü değildir ve öyle
kullanılmamalıdır.** Bu dosyadaki matris eğrilerden bağımsızdır; ne kusurdan ne de
onarımdan etkilenir.

---

## 6. Sınırlar

Bunlar, düşman bir hakemin yazacağı sertlikte yazılmıştır.

### 6.1 Tek kodlayıcı, körleme yok, güvenilirlik istatistiği yok
Her halka ataması ve her en-ince-halka yargısı **tek bir kodlayıcı tarafından yapıldı ve o
kodlayıcı, kodlamanın desteklediği argümanın da yazarıdır** — körleme yok, ikinci kodlayıcı
yok, kodlayıcılar arası uyum istatistiği yok. κ yoktur. 10/16/6 kapsama sonucu ve en ince
halka dağılımı korpustaki en kullanışlı iki sayıdır ve ikisi de **n = 1 kodlayıcıya**
dayanır. **10 nesnelik bir alt örneklemde ikinci bir kodlayıcı ve rapor edilmiş bir Cohen
κ, bunu bir okumadan bir ölçüme çeviren tek değişikliktir.** O yapılana kadar kodlama,
dünya hakkında veri olarak değil, **yorumlayıcı bir kaynak** olarak alıntılanmalıdır.

### 6.2 İki ayrı seçim yanlılığı, iki ayrı yönde
Beş `loss` nesnesi **kayıp yaşandığı için** seçildi — bağımlı değişkende seçim. Kalan 26
büyük ölçüde ünlü, iyi belgelenmiş, **hayatta kalmış** nesnelerden seçildi — hayatta kalma
yanlılığı. Bu iki yanlılık birbirini götürmez; **yön değiştirir.** Bu korpustan aktarım
başarısızlığının genel sıklığı, dağılımı ya da nedenleri hakkında hiçbir çıkarım yapılamaz.

### 6.3 Kaynak kökeni eşit değil, ve karışım yayımlanıyor

Bu korpustaki her iddia kaynağını adıyla verir; ama kaynaklar tek cinsten değildir ve
v5.4'e kadar veri bunu gizliyordu: `source_type` alanının `web` diye tek bir torba değeri
255 olayın 163'ünü içine alıyordu. Bu yüzden `mevzuat.gov.tr`'deki bir kanun metni,
imzalı maddeleri olan bir ansiklopedi maddesi ve bir gazete yazısı, dosyayı süzen biri
için birbirinden ayırt edilemiyordu. Bu, yalnız kaynakların değil, **verinin** kusuruydu.

`source_type` artık **yayıncı türünü** kaydediyor. Bu bir kalite puanı değil, bir köken
etiketidir: bir atfı yeterli kılan şey, kaynağın türü ile iddianın türü arasındaki
uygunluktur — ve o yargı aşağıda bir politika olarak yazılıdır.

**Kaynak politikası — kaynak türünü iddia türü belirler.**

| İddianın türü | Gereken kaynak |
|---|---|
| Hukukî ya da idarî olgu | kanunun kendisi, Resmî Gazete ya da kararı veren kurumun yayımladığı metin |
| İstatistik | rakamı üreten kurum; rapor edilmiş rakam yerine denetlenmiş rakam |
| Tarihsel yorum | hakemli çalışma, akademik yayınevi ya da imzalı maddeleri olan editörlü başvuru eseri |
| Nesne, yazıt, yazma, kazı | koleksiyon, arşiv ya da kazı kaydı |
| Teknik standart ya da birim | standardın kendisi (ISO, BIPM, IANA, RFC) |
| Bir buluşun önceliği | patent, Nobel dersi ya da hakemli tarih yazımı — asla tek başına firmanın kendi anlatısı değil |
| Güncel olay | çağdaş gazetecilik meşrudur; tarihiyle verilir ve öyle etiketlenir |

Bundan iki sonuç çıkar ve ikisi de bu korpusta uygulanmıştır. Haber kaynağı **elenmiş
değildir** — 2014 tarihli bir bakanlık kararı ya da 2026 tarihli bir ürün duyurusu için
uygun kayıt o olabilir — ama hakkında akademik literatür bulunan bir tarihsel iddiayı
taşıyamaz. Resmî kaynak da **kendiliğinden üstün değildir**: bir bakanlığın yürüttüğü
reforma dair anlatısı olayın tarafıdır; neye karar verildiğinin birincil kaydıdır,
bilgiye ne olduğunun yansız kaydı değil.

**Karışım, yayımlandığı hâliyle:**

| `source_type` | Benzersiz kaynak | Olay |
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
| **Toplam** | **291** | **255** |

Daha iyisi doğrulanamadığı için zayıf bir kaynağın korunduğu yerlerde, çalışmadaki kaynak
notu bunu açıkça söyler — `corporate-or-interested-party` ve
`blog-or-personal-compilation` girdileri bu kaydı taşır. Üç iddia hâlâ Wikipedia'ya
dayanıyor; kökene göre derecelendirilmiş bir alt küme isteyen kullanıcı `source_type`
üzerinden süzmeli ve bu üçünü çözülmemiş saymalıdır.

**v5.4'te ne değişti ve bu neden atıf hijyeninden ibaret değil.** Yeniden kaynaklandırma
biçimsel bir iş olmadı: iddiaları üst kaynaklara karşı denetlemek iddiaları değiştirdi.
**255 olay atfının 80'i değiştirildi, 63 olay iddiası doğrulanabilir kaynağın söylediğine
göre yeniden yazıldı ve dört olayın yılı düzeltildi.** Hiçbir üst kaynağın doğrulamadığı
sayılar yeniden atıflandırılmak yerine çıkarıldı — bunların arasında kilogram
prototipinin dönemsel doğrulama yılları (1889/1948/1989 → 1899-1911, 1939-1953,
1988-1992), 1931 Osmanlı evrak satışının tonajı (27 ton → 30-50 ton), Süleymaniye'nin
kubbe ölçüleri (26,5 m / 53 m → 27,40 m / 50 metreyi biraz aşan), Glossa Ordinaria'daki
gloss sayısı (96.940 → yaklaşık 96.000), Valens kanal ağının uzunluğu (250 kilometreyi
aşkın → yaklaşık 246 km, 5. yüzyıl uzantısıyla en az 426 km) ve Hasan Çelebi'nin icâzet
yılı (1975 → 1391/1971) var. v5.3 verisini bu noktalarda olduğu gibi alan bir kullanıcı,
tek dayanağı üçüncül bir kaynak olan bir rakamı almış oluyordu.

### 6.4 Kapsama coğrafi ve zamansal olarak dengesiz
Üç katman da Avrupa, Anadolu ve Akdeniz merkezlidir. Ayrı kanıt şeridinde görünenler
dışında sette Sahra-altı Afrika, Doğu Asya, Güney Asya ya da Yerli Amerika kökenli hiçbir
nesne yoktur. Kültürler arası hiçbir iddia bu korpusun erimi içinde değildir.

### 6.5 İki dilli alanlar çeviridir
`_tr` ve `_en` alanları aynı iddianın iki dildeki hâlidir. Bağımsız gözlem değildir ve iki
kez sayılmamalıdır.

### 6.6 Tarihler çalışmanın tarihleridir, bir kayıt kronolojisi değil
Olay yılları, alıntılanan kaynağın kaydettiği gibidir. Kaynaklar çeliştiğinde çalışma
birini seçmiş ve birkaç vakada çelişkiyi düzyazıda dipnotlamıştır — o düzyazı **bu
dosyalara taşınmadı.** Yılları nicel olarak kullanacak olan herkes `source_url` üzerinden
yeniden denetlemelidir.

---

## 7. Mevcut çerçevelerle ilişkisi

Bu korpus yeni bir kuram olarak sunulmuyor. Altı halkanın beşinin önceden adı var:
`packet` ≈ OAIS *Data Object*; `decoder` ≈ *Representation Information* + *Designated
Community*; `context` ≈ *Context Information*; `apparatus` ≈ *Representation Information
Network*; `maintenance` ≈ OAIS *Mandatory Responsibilities* ve bakım literatürü
(Star 1999; Russell & Vinsel 2016). Altı özellikli bir koruma modeli zaten var (SPOT:
Vermaaten, Lavoie & Caplan, *D-Lib* 2012); her kategoriye ayrı çare öneren beş kategorili
bir örtük bilgi taksonomisi de var (Collins 2001).

Korpusun katkısı şema değil, şunlardır: **tek sabit bir şemanın, nesneye özel ayar
yapılmadan, heterojen ve kültürler arası bir nesne setine uygulanması; her olayın tarihli
ve kaynaklı olması; ve ortaya çıkan matrisin, şemanın aleyhine çıktığı yerde bile
yayımlanması.**

---

## 8. Atıf ve yeniden kullanım

Bu veri kümesi ve bu kitapçık için lisans **CC BY 4.0**; çalışmanın kodu MIT'tir. CC BY
4.0, geçerli olduğu yerlerde *sui generis* veritabanı haklarını da kapsar.

Atıf:

> Ahmet Çandöken (2026). *The Transmission Chain: a link-coded corpus of 255 dated
> transmission events across 32 objects* (Sürüm 1.0.0) [Veri kümesi]. Zenodo.
> https://doi.org/10.5281/zenodo.22093227

Alıntılanan birincil kaynaklar kendi haklarına tabidir; hepsine `source_url` üzerinden
doğrudan erişilir.

---

## 9. Bu dosyanın künyesi

CSV ve JSON dosyaları `index.html` v5.4'ten, depoyla birlikte gelen
`tools/export-data.py` betiğiyle **mekanik olarak** üretilir; dışa aktarım sırasında elle
hiçbir değer girilmez ve yukarıda raporlanan sayılar çalışmada yayımlanan sayıları yeniden
üretir. Yeniden üretmek için: `python3 tools/export-data.py index.html data`.
`source_type` değerini bu betik, adresin alan adına bakarak bir yayıncı türü tablosundan
atar; tabloda olmayan bir alan adı, dışa aktarımı sessizce bir torba değere düşürmek
yerine **hata verdirir** — eski tek `web` kovasının yaptığı tam da o düşürmeydi. **Çalışmanın metni, kodu, kaynak
denetimi ve öncül taraması esaslı ölçüde yapay zekâ desteğiyle üretilmiştir; çalışmanın
eskiden "uzman incelemesi" dediği süreç, altı uzmanlık çerçevesinden yapay zekâ modelleri
tarafından yürütülen çekişmeli eleştiridir — insan hakemliği değildir ve öyle
sayılmamalıdır.** Bu kitapçık da aynı destekle taslaklandı. Her iddianın sorumluluğu adı
geçen yazara aittir.
