# Kaynak denetimi — v5.4

> **Bu belge hakkında.** Bu dosya, **Aktarım Zinciri / The Transmission Chain**
> (yazar: Ahmet Çandöken · ORCID 0009-0001-5197-7888) çalışmasının v5.3 → v5.4
> kaynak denetiminin tam kaydıdır. Denetim, "zincir haritaları" bölümündeki her olayın
> kaynağının **iddianın türüne uygun olup olmadığını** sınadı ve uygun olmayanları
> değiştirdi. Bu belge de çalışmanın geri kalanı gibi **yapay zekâ desteğiyle**
> hazırlanmıştır ve insan hakemliği değildir; önerilen her kaynak getirilip iddiayı
> içerdiği görülerek doğrulanmıştır. Sorumluluk yazara aittir.
>
> Metin ve veri **CC BY 4.0** · kod **MIT**.

## Sorun

v5.3'te her olay kaynaklıydı, ama veri kaynağın **ne tür** bir kaynak olduğunu
gizliyordu: `source_type` alanının tek torba değeri `web`, 255 olayın **163'ünü** içine
alıyordu. `mevzuat.gov.tr`'deki bir kanun metni, imzalı maddeleri olan bir ansiklopedi
maddesi ve bir gazete yazısı, dosyayı süzen biri için birbirinden ayırt edilemiyordu. Bu
örtünün altında tarihsel iddialar haber sitelerine, kişisel bloglara, şirketlerin kendi
tanıtım sayfalarına ve Wikipedia'ya dayanıyordu: **kırk olay** doğrudan Wikipedia'ya
bağlıydı.

Bu, yalnız kaynakların değil **verinin** kusuruydu. Akademik ortamda göze batan da
gazete atfından çok buydu.

## Kaynak politikası

Kaynağın türünü **iddianın türü** belirler:

| İddianın türü | Gereken kaynak |
|---|---|
| Hukukî ya da idarî olgu | kanun, Resmî Gazete ya da kararı veren kurumun yayımladığı metin |
| İstatistik | rakamı üreten kurum; rapor edilmiş yerine denetlenmiş rakam |
| Tarihsel yorum | hakemli çalışma, akademik yayınevi, imzalı maddeleri olan başvuru eseri |
| Nesne, yazıt, yazma, kazı | koleksiyon, arşiv ya da kazı kaydı |
| Teknik standart ya da birim | standardın kendisi (ISO, BIPM, IANA, RFC) |
| Bir buluşun önceliği | patent, Nobel dersi ya da hakemli tarih yazımı |
| Güncel olay | çağdaş gazetecilik meşrudur, tarihiyle ve etiketiyle |

İki sonuç: **haber kaynağı elenmiş değildir** — 2014 tarihli bir bakanlık kararı ya da
2026 tarihli bir ürün duyurusu için uygun kayıt odur — ama hakkında akademik literatür
bulunan bir tarihsel iddiayı taşıyamaz. Ve **resmî kaynak kendiliğinden üstün değildir**:
bir kurumun yürüttüğü işe dair anlatısı olayın tarafıdır; neye karar verildiğinin
birincil kaydıdır, bilgiye ne olduğunun yansız kaydı değil.

## Sonuç

- 255 olay atfının **80'si** değiştirildi.
- **63** olay iddiası, doğrulanabilir kaynağın söylediğine göre yeniden yazıldı.
- **4** olayın yılı düzeltildi.
- Wikipedia atıfları **40'tan 3'e** indi.


## Değişen atıflar

Nesne başına, yıl sırasına göre. "Tür" sütunu eski ve yeni kaynağın yayıncı türünü verir.
İddia metni de değiştiyse satır **✎** ile işaretlidir — bu, kaynağın iddiadaki bir sayıyı
ya da tarihi doğrulamadığı ve iddianın kaynağa göre düzeltildiği anlamına gelir.


### Yapay zekâ (`ai`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1973 | `en.wikipedia.org` | [`chilton-computing.org.uk`](http://www.chilton-computing.org.uk/inf/literature/reports/lighthill_report/p001.htm) | Wikipedia → **üniversite/enstitü** | ✎ |

### Su kemerleri (`aqueducts`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| -19 | `en.wikipedia.org` | [`penelope.uchicago.edu`](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Frontinus/De_Aquis/Bennett/1*.html) | Wikipedia → **üniversite/enstitü** | ✎ |
| 97 | `britannica.com` | [`penelope.uchicago.edu`](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Frontinus/De_Aquis/Bennett/1*.html) | başvuru eseri → **üniversite/enstitü** | ✎ |
| 373 | `thebyzantinelegacy.com` | [`e-docs.geo-leo.de`](https://e-docs.geo-leo.de/server/api/core/bitstreams/706965e5-4d59-45c7-a1d6-1f1db9aec336/content) | blog/kişisel derleme → **hakemli** | ✎ |
| 537 | `romanaqueducts.info` | [`waters.iath.virginia.edu`](https://waters.iath.virginia.edu/karmon.html) | blog/kişisel derleme → **üniversite/enstitü** | ✎ |
| 1453 | `thebyzantinelegacy.com` | [`nit-istanbul.net`](https://nit-istanbul.net/index.php/2024/02/01/introducing-water-heritage-for-sustainable-cities-the-revalorization-of-the-valens-aqueduct-in-istanbul/) | blog/kişisel derleme → **üniversite/enstitü** |  |
| 1563 | `islamicart.museumwnf.org` | [`dergipark.org.tr`](https://dergipark.org.tr/tr/download/article-file/481733) | müze/arşiv → **hakemli** | ✎ |

### Aspirin (`aspirin`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1897 | `bayer.com` | [`pmc.ncbi.nlm.nih.gov`](https://pmc.ncbi.nlm.nih.gov/articles/PMC1119266/) | ilgili taraf → **hakemli** | ✎ |

### Tükenmez kalem (`ballpoint`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1950 | `en.wikipedia.org` | [`moma.org`](https://www.moma.org/collection/works/82141) | Wikipedia → **müze/arşiv** | ✎ |
| 2017 | `chinadaily.com.cn` | [`caixinglobal.com`](https://www.caixinglobal.com/2017-01-10/china-steelmaker-finally-puts-the-ball-in-ballpoint-pen-101042333.html) | haber → **haber** | ✎ |

### Kodeks (`codex`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 85 | `historyofinformation.com` | [`publications.dainst.org`](https://publications.dainst.org/journals/chiron/article/download/369/4977) | blog/kişisel derleme → **hakemli** | ✎ |
| 331 | `en.wikipedia.org` | [`ccel.org`](https://www.ccel.org/ccel/schaff/npnf201.iv.vi.iv.xxxvi.html) | Wikipedia → **müze/arşiv** | ✎ |
| 400 | `kiwihellenist.blogspot.com` | [`publications.dainst.org`](https://publications.dainst.org/journals/chiron/article/download/369/4977) | blog/kişisel derleme → **hakemli** | ✎ |
| 850 → **835** | `en.wikipedia.org` | [`spotlight.vatlib.it`](https://spotlight.vatlib.it/greek-paleography/feature/3-old-round-minuscule) | Wikipedia → **müze/arşiv** | ✎ |

### Bilgisayar (`computer`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1945 | `historyofinformation.com` | [`library.si.edu`](https://library.si.edu/digital-library/book/firstdraftofrepo00vonn) | blog/kişisel derleme → **müze/arşiv** | ✎ |

### Diyot (`diode`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1906 | `en.wikipedia.org` | [`patents.google.com`](https://patents.google.com/patent/US836531A/en) | Wikipedia → **patent** | ✎ |
| 1907 | `en.wikipedia.org` | [`assets.cambridge.org`](https://assets.cambridge.org/97805218/65388/excerpt/9780521865388_excerpt.pdf) | Wikipedia → **hakemli** | ✎ |

### Elektrikli otomobil (`electric-car`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1996 | `news.gm.com` | [`americanhistory.si.edu`](https://americanhistory.si.edu/collections/object/nmah_1293145) | ilgili taraf → **müze/arşiv** |  |

### Cam üfleme (`glassblowing`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 673 | `the-past.com` | [`sitelines.newcastle.gov.uk`](https://sitelines.newcastle.gov.uk/SMR/417) | blog/kişisel derleme → **müze/arşiv** | ✎ |

### Hat (`hat`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1975 → **1971** | `turkiyeninustalari.org` | [`dergipark.org.tr`](https://dergipark.org.tr/tr/download/article-file/2197259) | ilgili taraf → **hakemli** | ✎ |

### Sabit disk (`hdd`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1961 | `en.wikipedia.org` | [`computerhistory.org`](https://www.computerhistory.org/storageengine/flying-heads-improve-hdd-capacity-speed/) | Wikipedia → **müze/arşiv** | ✎ |
| 2002 | `ed-thelen.org` | [`computerhistory.org`](https://computerhistory.org/restorations/) | blog/kişisel derleme → **müze/arşiv** | ✎ |

### Hipokaust (`hypocaust`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| -25 | `en.wikipedia.org` | [`penelope.uchicago.edu`](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Vitruvius/5*.html) | Wikipedia → **üniversite/enstitü** |  |
| 1350 | `solar.lowtechmagazine.com` | [`ojs.utlib.ee`](https://ojs.utlib.ee/index.php/bjah/article/view/13502/8558) | blog/kişisel derleme → **hakemli** | ✎ |
| 1936 | `savewright.org` | [`nps.gov`](https://www.nps.gov/subjects/nationalhistoriclandmarks/upload/Allaback-NHL-Final-Report-508-Compliant.pdf) | blog/kişisel derleme → **resmî/hukukî** |  |

### Entegre devre (`integrated-circuit`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1958 | `ti.com` | [`computerhistory.org`](https://www.computerhistory.org/siliconengine/all-semiconductor-solid-circuit-is-demonstrated/) | ilgili taraf → **müze/arşiv** |  |

### İznik çinisi (`iznik`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1480 | `en.wikipedia.org` | [`islamicceramics.ashmolean.org`](https://islamicceramics.ashmolean.org/Iznik/develop.htm) | Wikipedia → **müze/arşiv** |  |
| 1963 | `turkiyeturizmansiklopedisi.com` | [`dergipark.org.tr`](https://dergipark.org.tr/en/pub/akdenizsanat/issue/49183/620055) | blog/kişisel derleme → **hakemli** | ✎ |
| 1993 | `malaymail.com` | [`iznik.com`](https://www.iznik.com/tr/sayfa/iznik-vakfi) | haber → **ilgili taraf** | ✎ |

### Kilogram (`kilogram`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1799 | `en.wikipedia.org` | [`nist.gov`](https://www.nist.gov/si-redefinition/kilogram/kilogram-past) | Wikipedia → **resmî/hukukî** | ✎ |
| 1889 | `en.wikipedia.org` | [`bipm.org`](https://www.bipm.org/en/committees/cg/cgpm/1-1889/resolution-1) | Wikipedia → **resmî/hukukî** | ✎ |
| 1948 | `en.wikipedia.org` | [`nist.gov`](https://www.nist.gov/si-redefinition/kilogram/kilogram-present) | Wikipedia → **resmî/hukukî** | ✎ |
| 1989 | `en.wikipedia.org` | [`nist.gov`](https://www.nist.gov/si-redefinition/kilogram/kilogram-present) | Wikipedia → **resmî/hukukî** | ✎ |
| 2016 | `en.wikipedia.org` | [`bipm.org`](https://www.bipm.org/documents/20126/27314082/cc-publication-ID-501.pdf/addd563b-71e6-8e1c-a960-fb37b8fd5e55) | Wikipedia → **resmî/hukukî** | ✎ |
| 2018 | `en.wikipedia.org` | [`bipm.org`](https://www.bipm.org/en/committees/cg/cgpm/26-2018/resolution-1) | Wikipedia → **resmî/hukukî** | ✎ |
| 2026 | `en.wikipedia.org` | [`nist.gov`](https://www.nist.gov/noac/technology/mass-force-and-acceleration/tabletop-kibble-balance-gram-level-mass-realization) | Wikipedia → **resmî/hukukî** | ✎ |

### Latin alfabesi (`latin-alphabet`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| -700 | `britannica.com` | [`uvm.edu`](https://www.uvm.edu/~jbailly/courses/LundquistLatinHistoryPrehistory/Wallace%20Latin%20alphabet%20from%20Clackson%202013%20Companion%20to%20the%20Latin%20Language-2.pdf) | başvuru eseri → **üniversite/enstitü** | ✎ |
| -560 → **-520** | `en.wikipedia.org` | [`epigraphy.osu.edu`](https://epigraphy.osu.edu/collections/latin-photo/cil-i2-21-24) | Wikipedia → **üniversite/enstitü** | ✎ |
| -250 | `britannica.com` | [`uvm.edu`](https://www.uvm.edu/~jbailly/courses/LundquistLatinHistoryPrehistory/Wallace%20Latin%20alphabet%20from%20Clackson%202013%20Companion%20to%20the%20Latin%20Language-2.pdf) | başvuru eseri → **üniversite/enstitü** |  |
| -50 | `britannica.com` | [`uvm.edu`](https://www.uvm.edu/~jbailly/courses/LundquistLatinHistoryPrehistory/Wallace%20Latin%20alphabet%20from%20Clackson%202013%20Companion%20to%20the%20Latin%20Language-2.pdf) | başvuru eseri → **üniversite/enstitü** | ✎ |
| 800 | `britannica.com` | [`hmmlschool.org`](https://hmmlschool.org/latin-caroline/) | başvuru eseri → **üniversite/enstitü** | ✎ |
| 1450 | `en.wikipedia.org` | [`europeana.eu`](https://www.europeana.eu/en/stories/how-corbie-abbeys-medieval-manuscripts-connect-to-todays-fonts) | Wikipedia → **müze/arşiv** |  |
| 1928 | `en.wikipedia.org` | [`mevzuat.gov.tr`](https://www.mevzuat.gov.tr/MevzuatMetin/1.3.1353.pdf) | Wikipedia → **resmî/hukukî** | ✎ |
| 1989 | `en.wikipedia.org` | [`iso.org`](https://www.iso.org/standard/16346.html) | Wikipedia → **resmî/hukukî** | ✎ |

### Çakmak (`lighter`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1973 | `en.wikipedia.org` | [`mea.bic.com`](https://mea.bic.com/en-za/lighters/50-years-of-BIC) | Wikipedia → **ilgili taraf** | ✎ |

### Doğal gaz (`natural-gas`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1959 | `conocophillips.com` | [`higherlogicdownload.s3.amazonaws.com`](https://higherlogicdownload.s3.amazonaws.com/SNAME/1dcdb863-8881-4263-af8d-530101f64412/UploadedFiles/c3352777fcaa4c4daa8f125c0a7c03e9.pdf) | ilgili taraf → **meslek kuruluşu** | ✎ |
| 1964 | `conocophillips.com` | [`lngindustry.com`](https://www.lngindustry.com/lng-shipping/19062014/first_lng_carrier_entered_service_50_years_ago_802/) | ilgili taraf → **haber** |  |

### Osmanlı matbaası (`ottoman-print`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1493 | `historyofinformation.com` | [`islamansiklopedisi.org.tr`](https://islamansiklopedisi.org.tr/matbaa) | blog/kişisel derleme → **başvuru eseri** |  |
| 1553 | `ageofinvention.xyz` | [`dergipark.org.tr`](https://dergipark.org.tr/en/download/article-file/5498251) | blog/kişisel derleme → **hakemli** |  |
| 1567 | `dailysabah.com` | [`islamansiklopedisi.org.tr`](https://islamansiklopedisi.org.tr/matbaa) | haber → **başvuru eseri** | ✎ |

### Osmanlı Türkçesi (`ottoman-script`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1917 → **1913** | `en.wikipedia.org` | [`islamansiklopedisi.org.tr`](https://islamansiklopedisi.org.tr/elifba) | Wikipedia → **başvuru eseri** | ✎ |
| 1931 | `bnrnews.bg` | [`eprints.rclis.org`](http://eprints.rclis.org/11734/1/bulgaristana_satilan_evrakveozel.pdf) | haber → **hakemli** | ✎ |
| 2014 | `voanews.com` | [`ttkb.meb.gov.tr`](https://ttkb.meb.gov.tr/meb_iys_dosyalar/2019_12/10095332_19_sura.pdf) | haber → **resmî/hukukî** | ✎ |
| 2026 | (değişmedi) | (değişmedi) | — | ✎ |

### Kurşun kalem (`pencil`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1795 | `britannica.com` | [`inpi.fr`](https://www.inpi.fr/conte-ou-l-art-du-crayon-1795) | başvuru eseri → **patent** | ✎ |
| 1958 | `fee.org` | [`fee.org`](https://fee.org/ebooks/i-pencil/) | ilgili taraf → **ilgili taraf** |  |

### Roma hukuku (`roman-law`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 529 | `britannica.com` | [`uwyo.edu`](https://www.uwyo.edu/lawlib/blume-justinian/ajc-edition-2/books/book1/Book%201-ConcerningCode.pdf) | başvuru eseri → **üniversite/enstitü** | ✎ |
| 533 | `worldhistory.org` | [`scholarship.law.wm.edu`](https://scholarship.law.wm.edu/cgi/viewcontent.cgi?article=1122&context=libpubs) | blog/kişisel derleme → **hakemli** | ✎ |
| 534 | `en.wikipedia.org` | [`scholarship.law.wm.edu`](https://scholarship.law.wm.edu/cgi/viewcontent.cgi?article=1122&context=libpubs) | Wikipedia → **hakemli** |  |
| 1250 | `en.wikipedia.org` | [`scholarship.law.wm.edu`](https://scholarship.law.wm.edu/cgi/viewcontent.cgi?article=1122&context=libpubs) | Wikipedia → **hakemli** | ✎ |
| 1406 | `historyofinformation.com` | [`scholarship.law.wm.edu`](https://scholarship.law.wm.edu/cgi/viewcontent.cgi?article=1122&context=libpubs) | blog/kişisel derleme → **hakemli** | ✎ |
| 1804 | `en.wikipedia.org` | [`scholarship.law.wm.edu`](https://scholarship.law.wm.edu/cgi/viewcontent.cgi?article=1122&context=libpubs) | Wikipedia → **hakemli** | ✎ |
| 1926 | `en.wikipedia.org` | [`cambridge.org`](https://www.cambridge.org/core/journals/international-journal-of-law-in-context/article/abs/receiving-the-swiss-civil-code-translating-authority-in-early-republican-turkey/870523755C8D09C5F157C0FB8E0DA03C) | Wikipedia → **hakemli** | ✎ |

### Sinan / Süleymaniye (`sinan`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1550 | `yedikita.com.tr` | [`kutuphane.ttk.gov.tr`](https://kutuphane.ttk.gov.tr/details?id=518458&materialType=KT&query=Barkan,+%C3%96mer+L%C3%BBtfi.) | haber → **müze/arşiv** |  |
| 1557 | `en.wikipedia.org` | [`islamansiklopedisi.org.tr`](https://islamansiklopedisi.org.tr/suleymaniye-camii-ve-kulliyesi) | Wikipedia → **başvuru eseri** | ✎ |
| 1660 | `en.wikipedia.org` | [`isamveri.org`](https://isamveri.org/pdfdrg/D175781/2007/2007_EYUPGILLER_OZALTIN.pdf) | Wikipedia → **hakemli** | ✎ |
| 1766 | `en.wikipedia.org` | [`acikerisim.fsm.edu.tr`](https://acikerisim.fsm.edu.tr/bitstreams/cbef0a7b-a2be-4935-9546-8ae5a5488885/download) | Wikipedia → **üniversite/enstitü** | ✎ |
| 2010 | `en.wikipedia.org` | [`acikerisim.fsm.edu.tr`](https://acikerisim.fsm.edu.tr/xmlui/bitstream/handle/11352/247/Ersen%26Olgun%26Akbulut%26Y%C4%B1ld%C4%B1r%C4%B1m.pdf) | Wikipedia → **üniversite/enstitü** | ✎ |

### Süpermarket (`supermarket`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1937 | `britannica.com` | [`smithsonianmag.com`](https://www.smithsonianmag.com/history/industrious-grocer-1930s-wanted-make-easier-customers-buy-more-just-needed-push-180987633/) | başvuru eseri → **haber** |  |
| 1973 | `ibm.com` | [`support.gs1.org`](https://support.gs1.org/support/solutions/articles/43000734073-gs1-historical-timeline) | ilgili taraf → **meslek kuruluşu** | ✎ |

### Televizyon (`television`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1935 | `explorepahistory.com` | [`lindahall.org`](https://www.lindahall.org/about/news/scientist-of-the-day/philo-farnsworth/) | blog/kişisel derleme → **müze/arşiv** | ✎ |
| 1972 | `doctorwho.tv` | [`blog.scienceandmediamuseum.org.uk`](https://blog.scienceandmediamuseum.org.uk/unravelling-the-mystery-of-lost-television/) | ilgili taraf → **müze/arşiv** |  |
| 2012 | `en.wikipedia.org` | [`gov.uk`](https://www.gov.uk/government/news/on-time-and-under-budget-an-all-digital-uk--2) | Wikipedia → **resmî/hukukî** | ✎ |

### Ekmek kızartma makinesi (`toaster`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1906 | `chemistryworld.com` | [`patents.google.com`](https://patents.google.com/patent/US811859A/en) | haber → **patent** | ✎ |

### Transistör (`transistor`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1951 | `pbs.org` | [`patents.google.com`](https://patents.google.com/patent/US2569347A/en) | haber → **patent** | ✎ |
| 1956 | `monika-schnitzer.com` | [`cepr.org`](https://cepr.org/voxeu/columns/how-antitrust-enforcement-can-spur-innovation-bell-labs-and-1956-consent-decree) | blog/kişisel derleme → **üniversite/enstitü** |  |

### Ubıhça (`ubykh`)

| Yıl | Eski kaynak | Yeni kaynak | Tür | ✎ |
|---|---|---|---|---|
| 1864 | `en.wikipedia.org` | [`journals.linguisticsociety.org`](https://journals.linguisticsociety.org/booknotices/?p=2376) | Wikipedia → **hakemli** | ✎ |
| 1956 | (değişmedi) | (değişmedi) | — | ✎ |
| 1963 | `en.wikipedia.org` | [`archive.org`](https://archive.org/details/rosettaproject_uby_contents-1) | Wikipedia → **müze/arşiv** | ✎ |
| 1974 | `en.wikipedia.org` | [`georgehewitt.net`](https://georgehewitt.net/multimedia/recordings/281-george-hewitt-s-recordings-from-turkey-1974) | Wikipedia → **blog/kişisel derleme** | ✎ |
| 1975 | `en.wikipedia.org` | [`aibl.fr`](https://aibl.fr/collections/tome-1-le-verbe-oubykh-etudes-descriptives-et-comparatives/) | Wikipedia → **müze/arşiv** |  |
| 1992 | `en.wikipedia.org` | [`dergipark.org.tr`](https://dergipark.org.tr/tr/download/article-file/305216) | Wikipedia → **hakemli** |  |


## Doğrulanamadığı için çıkarılan ya da düzeltilen sayılar

| Nesne | Eski | Yeni | Doğrulayan kaynak |
|---|---|---|---|
| Kilogram | dönemsel doğrulamalar 1889 / 1948 / 1989 | 1899-1911 / 1939-1953 / 1988-1992 | NIST |
| Kilogram | "üç bağımsız anahtarlı kasa" | erişim CIPM'in sıkı denetiminde | BIPM |
| Kilogram | watt terazisinin adı Haziran 2016'da değişti | 9 Temmuz 2016 | CCEM 30. toplantı raporu |
| Osmanlı Türkçesi | 27 ton, beş vagon, 2 Haziran 1931 | Mayıs 1931, 30-50 ton, ~1,5 milyon belge | Anameriç & Rukancı 2008 |
| Osmanlı Türkçesi | hurûf-ı munfasıla 1917 | 1 Mayıs 1913 | TDV İslâm Ansiklopedisi |
| Süleymaniye | kubbe 26,5 m / 53 m | 27,40 m / 50 metreyi biraz aşan | TDV İslâm Ansiklopedisi |
| Süleymaniye | 1766'da kubbenin bir bölümü çöktü | doğrulanamadı, çıkarıldı; Mihrimah'ın minaresi yıkıldı | Köse 2014 (arşiv belgeleri) |
| Süleymaniye | 1660 yangını iç bezemeyi yok etti | bezeme kaybı 19. yy Fossati onarımı ve 1959-1969 | Eyüpgiller & Özaltın 2007 |
| Roma hukuku | Glossa Ordinaria 96.940 gloss, 62.577'si Digesta | yaklaşık 96.000 | Dingledy 2016 |
| Roma hukuku | Digesta: iki bini aşkın kitap, üç milyon satır | otuz dokuz hukukçunun 1.528 kitabı | Dingledy 2016 |
| Roma hukuku | 529: bütün imparatorluk emirnameleri kaldırıldı | üç eski codex'in mahkemede anılması yasaklandı | Blume, Annotated Justinian Code |
| Su kemerleri | Valens hattı 250 km'yi aşkın | 4. yy'da ~246 km; uzantıyla en az 426 km | Sürmelihindi vd. 2021 |
| Su kemerleri | Kırkçeşme 300'ü aşkın çeşme | doğrulanamadı, çıkarıldı | Karakuş vd. 2018 |
| Hipokaust | 1500'e doğru 800-1000 örnek | Bingenheimer 1998: Avrupa'da 154 | Tvauri (Tartu Üniversitesi) |
| Hat | Hasan Çelebi icâzeti 1975 | 1391/1971 | Atik 2019 (icâzetnâme fotoğrafları) |
| İznik | Vakıf: iki yıllık deneme, %85 kuvars | süre çıkarıldı; hamur için Paynter vd. 2004 (%65-75) | İznik Vakfı + hakemli ölçüm |
| İznik | Aslanapa kazısı 1963 | ilk dönem 1963-1969 | Demirsar Arlı vd. 2019 |
| Kodeks | y. 400'de kitapların ~%80'i kodeks | 3. yy %18,5 · 4. yy %62,3 · 5. yy %89 | Meyer, Chiron 37 (2007) |
| Kodeks | Yunan minüskülü y. 850 | tarihli en eski minüskül yazma 835 | Vatikan Kütüphanesi |
| Latin alfabesi | 1928: yirmi dokuz harfli alfabe | kanun metninde harf sayısı yok; "merbut cetvel" | 1353 sayılı kanun |
| Latin alfabesi | Lapis Niger MÖ 570-550 | MÖ 6. yüzyılın sonu | CIL I² 2.1, 1 kaydı |
| Ekmek kızartma makinesi | patent US 852.338 | US 811.859 (alaşım patenti) | USPTO |
| Süpermarket | UPC 1 Nisan 1973 | 3 Nisan 1973 | GS1 |
| Televizyon | Temmuz 1935, Patent Ofisi kararı, öğretmenin hatırlaması | 1935, mahkeme kararı, öğretmenin çizimi saklamış olması | Linda Hall Library |
| Tükenmez kalem | uç çeliğinin tamamı Japonya'dan | başta Japonya ve İsviçre | Caixin |
| Diyot | Pickard patenti 30 Ağustos 1906'da alındı | başvuru 30 Ağustos, tescil 20 Kasım 1906 | USPTO |
| Ubıhça | 84 ünsüz | seksenin üzerinde (Fenwick 2011: 85 fonem / 80 yerli) | LSA · Language |
| Ubıhça | dört köy adı | doğrulanamadı, çıkarıldı | — |
| Yapay zekâ | Lighthill raporu üniversiteleri kapattırdı | raporun kendi ifadeleri; fon kesintileri sonrasında | Lighthill raporu (SRC) |

## Değiştirilemeyenler

Aşağıdaki atıflar için doğrulanmış bir üst kaynak bulunamadı. Hepsi veride kendi yayıncı
türüyle etiketlidir ve kaynak notlarında bu durum yazılıdır.

- **Tükenmez kalem 1961** (tungsten karbür bilye) — Wikipedia. MoMA kaydı ile DPMA kaydı
  malzeme konusunda birbiriyle çelişiyor; bağımsız doğrulama yapılmadan yeniden
  yazılmamalı.
- **Transistör 1955** (Sony TR-55) — Wikipedia. Sony'nin kurumsal tarih sayfası
  erişilemedi, IEEE/ETHW'de karşılığı yok.
- **Yapay zekâ 1987** (Lisp makinesi pazarının çöküşü) — Wikipedia. Rakamın bilinen
  kaynakları Crevier 1993 ve Roland & Shiman 2002; ikisi de çevrimiçi doğrulanamadı.
- **Sabit disk 1957** (34.500 dolar, 785 kg) — kişisel derleme sitesi. IBM arşivi dahil
  hiçbir kurumsal karşılık bulunamadı.
- **Osmanlı vakfı 1935** (2762 sayılı Vakıflar Kanunu) — ticari hukuk veritabanı.
  Vakıflar Genel Müdürlüğü'nün kendi PDF nüshası bu ortamdan doğrulanamadı; yayına
  almadan önce elle teyit edilmeli.
- **Yazma eser envanteri 2026** (784 bin) — haber kaynağı. Güncel olay olduğu için
  korundu, ama denetlenmiş rakam farklıdır: Sayıştay raporu 2021 faaliyet raporunda
  705.802, muhasebe kayıtlarında 356.559 verir. Bu kayıt nesnenin kaynak listesine ikinci
  kaynak olarak eklendi ve iddia "kurumun kamuoyuna açıkladığı" biçiminde yeniden yazıldı.

## Yeniden üretilebilirlik

`tools/export-data.py` beş CSV ile `corpus.json` dosyasını `index.html`'den üretir.
`source_type` değerini betik, adresin alan adına bakarak bir yayıncı türü tablosundan
atar; tabloda olmayan bir alan adı dışa aktarımı **hata verdirir** — eski tek `web`
kovasının yaptığı sessiz düşürme artık mümkün değil.

```bash
python3 tools/export-data.py index.html data
```

