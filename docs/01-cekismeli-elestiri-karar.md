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

# Çekişmeli Eleştiri — Karar Belgesi
## "Aktarım Zinciri / The Transmission Chain" v4.0

Altı ayrı uzmanlık çerçevesinden, birbirinden bağımsız yürütülen çekişmeli eleştiri (arkeoloji · bilim ve teknoloji tarihi · nicel modelleme · dijital koruma ve YZ · bilim felsefesi · yayın hazırlığı ve araştırma bütünlüğü). Her çerçeve diğerlerinin bulgularını görmeden çalıştırıldı; bu bir insan hakemliği değil, yapay zekâ modelleriyle yürütülen bir eleştiridir. Aşağıdaki "yakınsayan bulgular", birbirinden habersiz en az iki incelemecinin bağımsız olarak bulduğu şeylerdir — bu yüzden en yüksek güvenilirliğe sahiptirler.

---

# HÜKÜM

**Altı incelemecinin altısı da aynı sonuca vardı: yayınlanmadan önce esaslı revizyon gerekiyor.**

Bu "ham çalışma" demek değil. Çalışmanın iskeleti sağlam, kaynak disiplini çoğu kişisel denemeden iyi, ve bazı bölümleri gerçekten özgün. Ama şu an yayınlanırsa, on dakikada doğrulanabilir ve savunulamaz üç iddia taşıyor olacak.

Sorunun niteliği önemli: **bulguların çoğu görüş ayrılığı değil, aritmetik.** Beş tanesini kendim çalıştırıp doğruladım. Bir uzmanın "bence abartmışsınız" demesiyle, bir okuyucunun sitenizin kaynak kodunu açıp iddianızın yanlış olduğunu göstermesi farklı şeylerdir. Şu an ikincisi mümkün.

---

# 1. GERÇEKTEN İYİ OLAN NE

Bunu önce söylüyorum, çünkü sonrası ağır ve dengesiz bir izlenim bırakmasını istemiyorum.

- **`Ne gösteriyor?` / `Ne göstermiyor?` disiplini.** Altı incelemeciden dördü bunu kendiliğinden övdü. Bu tür denemelerde nadirdir.
- **Kendi örneklerine karşı yazılmış efsane düzeltmeleri.** Bilim tarihçisi "türün normundan iyi" dedi; editör "çalışmadaki en iyi şey" dedi.
- **Post-1900 malzemesi** (Pew, Domesday, F-1, Cerf) tarihçiye göre "dikkatli, doğru şerhli ve doğrulanıyor."
- **Bağlantı bütünlüğü:** editör 36 bağlantının 36'sını kontrol etti — **ölü bağlantı yok.** Bu, bu ölçekte alışılmadık.
- **Çeviri disiplini:** editör 216 dizgiyi karşılaştırdı; şerhler neredeyse her yerde iki dilde de korunmuş.
- **Altılı kayıp taksonomisi** — editöre göre çalışmanın *tek gerçek özgün katkısı* ve "genuinely useful teaching device".

Bu liste kısa değil. Sorun temelde değil, iddiaların kalibrasyonunda.

---

# 2. YAKINSAYAN ENGELLEYİCİ BULGULAR

Bunlar birden fazla incelemecinin bağımsız bulduğu ve benim doğruladığım şeyler.

## 2.1 Yayımlanan formüller, çalışan kodu tarif etmiyor
**Altı incelemeciden BEŞİ bunu ayrı ayrı buldu.**

Yöntem bölümünde okuyucuya `R = C × q_d` gösteriliyor. Kodun hesapladığı şey bu değil.

```
Varsayılan ayarlarla, 40. nesilde:
  Yazan formül  C × q_d = 5,8336
  Çalışan kod   rebuilt = 3,1925
  Hata          %82,7
```

`C = P × q_c` formülünün ise kodda hiçbir karşılığı yok — üstelik `P`, çalışmanın "doğrudan karşılaştırılamaz" dediği *öteki* aracın değişkeni. Yani üç formülden ikisi yanlış, ve yanlış olan taşıyıcı olanı.

Bu neden bu kadar ağır: sitenin rozeti "Açık varsayımlar" diyor ve kaynak kodu altbilgide bir tık uzakta.

## 2.2 "Paketleme kazancını sonuna kadar açın" talimatı kendini çürütüyor
**Modelleme ve YZ incelemecileri ayrı ayrı buldu.**

`G` kaydırıcısının yardım metni şöyle diyor: *"Raising G alone is not always good news — to see that, hold Context transfer fixed and push this to the maximum."*

Okuyucu bunu yapıyor:

```
G=1  bağlamlı = 7,114117   yeniden kurulabilen = 0,7981
G=4  bağlamlı = 7,114117   yeniden kurulabilen = 3,1925
G=8  bağlamlı = 7,114117   yeniden kurulabilen = 5,8336
```

`G` bağlamlı eğriye **tek bir bitlik** etki bile etmiyor — kodda `contextual` satırında `gain` geçmiyor. Ve yeniden kurulabilirlik G ile birlikte **yükseliyor**. Yani metnin okuyucuya yaptırdığı deney, metnin iddiasının tam tersini gösteriyor. Otuz saniyede.

## 2.3 Bağlam açığı kapatılamıyor — gizli bir sabit var
**Modelleme ve felsefe incelemecileri ayrı ayrı buldu.**

`q_c` kaydırıcısının yardımı: *"%100, her sonucun yanında 'nasıl bulundu, neden doğru sayıldı, nerede çalışmaz' bilgisinin de gitmesi demek."*

Her kayıp kanalını kapattım — `q_c = 1`, `q_d = 1`, hiç aşınma yok:

```
C/A = 0,8768
```

1,0 değil. Kodda belgelenmemiş bir `* .85` var; yeni katkının %15'i, `q_c` ne olursa olsun bağlamsız sayılıyor. Kaydırıcının maksimumu, kaydırıcının söylediği şeyi ifade etmiyor. Üstelik v1 düzeltme günlüğü bu sorunun *çözüldüğünü* iddia ediyor.

## 2.4 "Katkı artışı oranları seyreltir" iddiası modelde yanlış
**Modelleme, felsefe ve YZ incelemecileri ayrı ayrı buldu.**

```
Brüt katkı = 0    → C/A = 0,0060
Brüt katkı = 1,5  → C/A = 0,1947
Brüt katkı = 5    → C/A = 0,2126
```

Katkıyı artırmak bağlam oranını **35 kat yükseltiyor**, seyreltmiyor. Bu, çalışmanın "söyleyebilir" listesindeki maddelerden birine denk geliyor.

## 2.5 Dayanıklı arşiv modelde zararlı çıkıyor
**Modelleme incelemecisi buldu; dijital koruma incelemecisi bağımsız olarak teyit etti.**

```
Yarı ömür = 10  nesil → yeniden kurulabilen = 4,4713
Yarı ömür = 35  nesil → yeniden kurulabilen = 3,1925
Yarı ömür = 100 nesil → yeniden kurulabilen = 2,6576
```

Model diyor ki: **bağlantı çürümesi iyidir, dayanıklı arşiv düşmandır.** Bu, Dijital Karanlık Çağ bölümünün, bakım kaybı taksonomisinin ve İskenderiye düzeltmesinin ("koruyan şey bakımdır") işaretini ters çeviriyor.

## 2.6 İki araç birbirinin tersini söylüyor
**Modelleme, YZ, editör ve felsefe incelemecileri ayrı ayrı buldu.**

Tarihsel endekste `R` **4 → 70 (+%1650)** yükseliyor ve 2026'da tüm zamanların zirvesinde. Simülasyonda `R`, **dört ön ayarın dördünde de, 39 adımın 39'unda düşüyor** (%55–%86 kayıp). İkisi de aynı yeşil kesikli çizgi, aynı "Yeniden kurulabilen" etiketi.

"Doğrudan karşılaştırılamaz" şerhi bunu çözmüyor: aynı sayfada, aynı yüzyıl hakkında, zıt işaretli iki hikâye anlatılıyor.

## 2.7 `direct` / `proxy` etiketleri yaklaşık üçte birinde yanlış
**Arkeoloji ve editör incelemecileri ayrı ayrı buldu — ikisi de aynı indirgemeyi gösterdi.**

Efsanevi örnek: **Linear B kil tabletleri `proxy` (dolaylı) etiketli. Yunan ateşi — hiç kimsenin görmediği bir tarif — `direct` (tarihlenmiş maddi kayıt) etiketli.**

Editörün listesi: `greek-fire`, `printing`, `web`, `link-rot`, `model-collapse` yanlışlıkla `direct`; `linear-b`, `borneo` yanlışlıkla `proxy`. Ayrıca `f1-engine` (1960'lar roket motoru) `digital` kategorisinde.

Bu şema 100.000 yıllık grafiğin iki şeridini sürüyor — yani yapısal.

## 2.8 Kanıt bağımlı değişkene göre seçilmiş
**Tarih ve felsefe incelemecileri ayrı ayrı buldu.**

Vakalar kayıp yaşandığı için seçildi. Aktarımın *başarılı olduğu* çok daha kalabalık örneklem çalışmada yok. Felsefeci bunu tarihsel endeks ve dijital argüman için `blocking` saydı.

---

# 3. ALANLARA GÖRE EN AĞIR BULGULAR

## Tarih — vakaların çoğu "bilgi kaybı" vakası değil
Bilim tarihçisinin en yıkıcı eleştirisi ve bence en önemli tek bulgu:

> *Wootz, aktarım zinciri yıprandığı için durmadı. Ateşli silahlar kılıç ticaretini öldürdüğü, Sheffield fiyat kırdığı ve 1866'da İngilizler orman koruma kılıfıyla Hindistan'da çelik üretimini yasakladığı için durdu — Hint pota fırınları 1807'de hâlâ çalışırken görülmüş, süreç 1893'te Tamil Nadu'da hâlâ kayda geçiriliyorken. Roma sıcak karışımı hiç durmadı; sürekli kullanımda ve modern bir literatürü var. Yunan ateşi için önde gelen açıklama, toprakla birlikte kaybedilen petrol tedariki.*

Yani: modelin elinde yalnızca "bağlam aktarımı" ve "çözücü erişimi" açıklamaları var; yedi vaka sonuca göre seçilmiş; ve en az üçünde tarihsel kayıt sebebin **cevher kimyası, pazar talebi ve sömürge yasağı** olduğunu söylüyor — modelin temsil edemediği şeyler.

Ayrıca: **Antikythera'nın "benzer ikinci bir makine yok" iddiası yanlış.** ~500 tarihli Bizans dişli takvim-güneş saati var ve literatür bunu "süregelen bir gelenek" kanıtı sayıyor.

## Arkeoloji — eğri, kaybı temsil edemiyor
> *Tezi "bilgi kaybolur" olan bir çalışma, 100.000 yılının ilk 88.000'inde kaybı gösteremeyecek bir eğri çizmiş — sadece merkezde değil, kendi "senaryo aralığı"nın alt sınırında da.*

Ve: eğri **Blombos Mağarası'na** çapalanmış; kendi kaynağının ~70.000 ile ~2.000 yıl öncesi arasında **terk edilmiş** olarak kaydettiği mağara. Yükselen çizgi terk edişin içinden geçiyor.

Ayrıca ciddi bir örneklem sorunu: 23 kaydın Sahra-altı Afrika'dan olan **ikisi de 70.000 yıldan eski**, sonrası yok. Batı-dışı kayıtların çoğu *kayıp* vakası, eşik geçişleri ise Avrupa/Amerika. Arkeolog bunu şöyle özetledi: *"Bu cümleyi siz yazmadınız. Veri tablonuz yazdı."*

## Dijital ve YZ — modern yarı basın bültenlerinden yazılmış
- **"Across large language models"** yanlış: deney, **125 milyon parametreli OPT-125m**'in WikiText-2 üzerinde ince ayarı. Kayıt `direct / high` etiketli.
- **Pew şerhi ters:** "taşınmış adreslerde duruyor" diyorsunuz; Pew yönlendirmeleri **yaşıyor** sayıyor, yani %38 zaten onları içermiyor. Şerh yanlış yönde.
- **"Canlı bağlantıların yarısı on yılda gidiyor"** — Pew %38/10 yıl diyor, ve ön ayarın yarı ömrü **18 nesil**, yıl değil. Kendi verinizle çelişiyor. *(Doğruladım.)*
- **Gerstgrasser vd. (arXiv:2404.01413)** — YZ argümanınızın en dürüst hamlesi olan "biriktirmek çöküşü yavaşlatır" şerhi, **kaynakçada olmayan** bir literatüre dayanıyor.
- **2025 literatürü yok:** Schaeffer vd. "Model Collapse Does Not Mean What You Think" (arXiv:2503.03150) model çöküşünün sekiz farklı tanımını sayıyor ve popüler okumanın gerçekçi olmadığını söylüyor. Veri kesim tarihiniz Ağustos 2026.

## Felsefe — dokuz çelişki, dördü engelleyici
Felsefecinin doğrudan yanıtı: **"Evet. En az dokuz çelişki, dördü engelleyici. Üçü iki cümle arasında değil — metin ile kendi çalışan kodu arasında."**

En keskin olanı: `C = P × q_c` denklemi, `q_c` ölçülmediği sürece bir *iddia* değil, `q_c`'nin *tanımı*. Yani her sonuç sonradan uydurulabilir. Model açıklama yapmıyor, sonucu yeniden betimliyor.

Ayrıca: Polanyi, Collins ve Henrich hiç geçmiyor; MacKenzie & Spinardi kaynakçada var ama **hiçbir iddiada kullanılmamış**.

## Yayın bütünlüğü — en hızlı düzeltilebilir, en riskli
- **"Üç uzman incelemesinden geçirilmiş"** — üç yerde geçiyor, hiçbirinde isim, tarih, kurum yok. "Bilimsel dergi ve hakemlik" başlıklı bir bölümün yanında bu, dış hakemlik iddiası gibi okunuyor.
- **JSON-LD `ScholarlyArticle` ilan ediyor** — yazar yok, tarih yok, yayıncı yok, lisans yok.
- **"Her madde birincil kaynağa bağlıdır"** rozeti **yanlış**: 23 bağlantının 9'u birincil kaynak değil (müze vitrin yazısı, 1972 tarihli popüler dergi, MIT basın bülteni, konferans özeti, yayınevi satış sayfası).
- **Yazar adı yok. Lisans yok.** Kendi README'niz lisans eksikliğini not etmiş, hâlâ eklenmemiş.

## İki dil — bir tanesi tezi tersine çeviriyor
*(Doğruladım.)*

```
TR: "Yapay zekânın farkı DERECE değil, hız ve döngü kapanma süresidir."
EN: "What is different about AI is not KIND but speed and loop-closure time."
```

"Derece / tür" felsefede sabit bir ikilidir. İngilizce *türü* reddediyor (⇒ fark derecede — tutarlı). Türkçe *dereceyi* reddediyor (⇒ fark türde) — hem tezi ters çeviriyor hem de kendi içinde çelişiyor, çünkü cümle iki nicel değişken sayıyor. Bu, YZ bölümünün en alıntılanabilir kapanış cümlesi.

## Kendi kendiyle çelişen slider metni
*(Doğruladım.)*

`q_c` yardım metni: *"Şam çeliğinin kılıcı duruyor ama tarifi durmuyor"* — düz bir olgu olarak.
Efsane düzeltmesi paneli: *"Şam çeliğinin sırrı sonsuza dek kayboldu"* → **"Yaygın ama yanlış."**

Yani çalışma bir bölümde çürüttüğü şeyi başka bir bölümde iddia ediyor — ve daha çok okunan yerde.

---

# 4. NE YAPMALI

Üç kademe. Toplam yaklaşık bir haftalık odaklanmış iş.

## Kademe 1 — Adınızla yayınlamadan önce (2–3 saat)
1. **"Üç uzman incelemesi" ifadesini kaldırın** ya da isim verin. İncelemeler YZ destekliyse bunu açıkça yazın; bu dürüsttür ve hiçbir şey kaybettirmez.
2. **JSON-LD'yi `ScholarlyArticle` → `Article`** yapın; `author`, `datePublished`, `license` ekleyin.
3. **Adınızı koyun** + iki cümlelik konum beyanı: neyin uzmanı olduğunuz ve olmadığınız. Bu, çalışmanın en büyük zaafını en büyük güvenilirlik kazancına çevirir.
4. **LISANS ekleyin** — metin/veri için CC BY 4.0, kod için MIT.
5. **"Her madde birincil kaynağa bağlıdır" → "Her madde kaynağına bağlıdır"**.
6. **Türkçe YZ cümlesi:** `derece` → `tür`.

## Kademe 2 — Teknik biri okumadan önce (2 gün)
7. **Formül bloğunu ya koda uydurun ya kaldırın.** Felsefecinin tavsiyesi: kaldırın ve simülasyonu açıkça "argümanın çalıştırılabilir hâli, tarihin modeli değil" diye etiketleyin. Bu tek hamle dört engelleyici bulguyu birden düşürüyor.
8. **`G` kaydırıcısının yardım metnini düzeltin** — ya `G`'ye bir bağlam maliyeti ekleyin, ya iddiayı silin.
9. **Gizli `.85` sabitini** ya kaldırın ya görünür bir parametre yapın.
10. **"Katkı seyreltir" ve "matbaa bağlamın en iyi taşındığı dönem"** iddialarını ölçülen çıktıya göre yeniden yazın.
11. **Yarı ömrün işaretini düzeltin** — şu an dayanıklı arşiv zararlı çıkıyor.
12. **23 kaydı `direct`/`proxy` tanımına göre yeniden etiketleyin**, sonra `confidence` değerlerini gözden geçirin.
13. **"Canlı bağlantıların yarısı on yılda"** ifadesini düzeltin.
14. **Gerstgrasser vd. 2024'ü kaynakçaya ekleyin** ve üç yerde atıf verin.
15. **"Üç büyüklük mertebesi" (Maya) sayısını silin** — kendi şerhinizle çelişiyor.
16. **Antikythera'nın "benzer ikinci makine yok" cümlesini düzeltin.**

## Kademe 3 — Bir uzman okumadan önce (2–3 gün)
17. **Öncüller bölümü ekleyin:** Polanyi 1966, Collins 1985/2010, Henrich 2016, Hutchins 1995, Hayek 1945, Rothenberg 1995, OAIS/ISO 14721. *Bu çalışmanın itibarını yükseltir, düşürmez.*
18. **Tarih öncesi eğriyi ya düşebilir yapın ya kesikli çizgiye çevirin** ve Pleistosen'in kaç kayda dayandığını grafiğin üstüne yazın (dört kayıt, üç yerleşim).
19. **Batı-dışı örneklemi dengeleyin:** khipu, Timbuktu 2013 (kurtarılmış taşıyıcı — İskenderiye düzeltmenizin gerçek hayattaki karşılığı), Ge'ez yazıcı geleneği.
20. **Wootz / Roma betonu / Yunan ateşi** vakalarını ya siyasal iktisat açıklamasıyla yeniden yazın ya vaka setinden çıkarın.
21. **Seçim yanlılığını açıkça kabul edin** — bir paragraf yeter ve çalışmayı güçlendirir.
22. **"Hiçbir gözlem bu modeldeki hiçbir sayıyı değiştiremez"** cümlesini "Söyleyemez" listesine ekleyin. Modelleme incelemecisi bunun en yıkıcı eleştiriyi en güvenilir iddiaya çevireceğini söylüyor.

---

# 5. SİZE KARŞI ALINTILANACAK ÜÇ CÜMLE

Her incelemeci "en yıkıcı eleştiri" belirtti. En tehlikeli üçü:

**Editör:**
> *"Kendine hakemli bir bilimsel makale diyor ve üç uzmanın incelediğini söylüyor; kimin yazdığını, kimin incelediğini, ne zaman olduğunu söylemiyor — ve Yöntem bölümünde bastığı üç denklem, altbilgide bir tık uzaktaki kendi kaynak kodundaki denklemler değil. Tezi 'sonuçlar taşınır ama arkasındaki yöntem kaybolur' olan bir çalışma, sonuçlarını yayımlamış ve yöntemini kaybetmiş."*

**Modelleme:**
> *Aynı yeşil kesikli çizgi ve aynı "Yeniden kurulabilen" etiketiyle iki araç yayınlıyorsunuz. Tarihsel endekste R %1650 yükseliyor; simülasyonda dört ön ayarın dördünde de her adımda düşüyor.*

**Tarih:**
> *Aktarımın kırılganlığı üzerine bir çalışmayı, aktarımın gayet iyi olduğu ama siyasal iktisadın olmadığı üç vaka üzerine kurmuşsunuz.*

---

# 6. SON SÖZ

Sorunuz üçlüydü: mantıksal çelişki var mı, yayın sorunu var mı, yoksa daha mı işlenmesi gerekiyor.

**Mantıksal çelişki:** Var. Felsefeci dokuz saydı, dördü engelleyici. Beşini bağımsız olarak doğruladım.

**Yayın sorunu:** Var, ve en hızlı düzeltilebilir olanı bu. Yazar adı, lisans, "üç uzman incelemesi" ve `ScholarlyArticle` ilanı — bunlar birlikte, iddia edilen otorite maksimum, hesap verebilirlik sıfır bir birleşim oluşturuyor.

**Ham mı?** Hayır. Ham bir çalışma bu kadar iyi kaynaklanmaz, 36 bağlantının 36'sı yaşamaz, kendi örneklerine karşı efsane düzeltmesi yazmaz. Bu, **fazla iddialı hâle getirilmiş sağlam bir çalışma.** Tedavi de bu yüzden büyük ölçüde *geri çekme* yönünde: formül bloğunu kaldırın, simülasyonu illüstrasyon ilan edin, "uzman incelemesi" iddiasını bırakın, iki vakayı çıkarın. Sildikçe savunulabilir hâle geliyor.

En umut verici bulgu şu: incelemecilerin çoğu, çalışmanın **öğretici bir araç** olarak — iki dilli, kaynaklı, kendini düzelten, etkileşimli, ve "bilgi kayboldu" cümlesini altı ayrı mekanizmaya ayrıştıran bir taksonomiyle — var olmak için gerçek bir gerekçesi olduğunu söyledi. Sorun, bunun yerine bir *keşif* gibi çerçevelenmiş olması.
