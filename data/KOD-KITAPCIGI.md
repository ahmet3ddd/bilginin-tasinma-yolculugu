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
| `sources.csv` | 275 | benzersiz bir kaynak adresi ve kullanım sayısı |
| `corpus.json` | — | kayıpsız dışa aktarım: özgün iki dilli alanlar, satır içi işaretlemesiyle, artı model parametreleri |

CSV dosyaları UTF-8, virgülle ayrılmış, RFC 4180 tırnaklama, başlık satırlı. CSV'deki metin
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

### 6.3 Kaynak kalitesi eşit değil, ve karışım yayımlanıyor
275 benzersiz kaynağın dağılımı: dergi ya da ön baskı 17, üniversite 19, resmî ya da
standart kuruluşu 18, müze ya da arşiv 13, ansiklopedi 29, diğer web 179. `source_type`
sütunu dışa aktarım betiği tarafından adresin sunucu adından **otomatik** atanır; kaba bir
kolaylık etiketidir, kalite hakkında editoryal bir yargı değildir. Kaynak kalitesine göre
süzülmüş bir alt küme gerekiyorsa, bu sütunla süzüp elle kontrol edin.

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

CSV ve JSON dosyaları `index.html` v5.2'den bir dışa aktarım betiğiyle **mekanik olarak**
üretildi; dışa aktarım sırasında elle hiçbir değer girilmedi ve yukarıda raporlanan
sayılar çalışmada yayımlanan sayıları yeniden üretir. **Çalışmanın metni, kodu, kaynak
denetimi ve öncül taraması esaslı ölçüde yapay zekâ desteğiyle üretilmiştir; çalışmanın
eskiden "uzman incelemesi" dediği süreç, altı uzmanlık çerçevesinden yapay zekâ modelleri
tarafından yürütülen çekişmeli eleştiridir — insan hakemliği değildir ve öyle
sayılmamalıdır.** Bu kitapçık da aynı destekle taslaklandı. Her iddianın sorumluluğu adı
geçen yazara aittir.
