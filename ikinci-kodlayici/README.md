# İkinci kodlayıcı — açık çağrı

**Bu klasör neden var, tek cümleyle:** Bu çalışmadaki 255 olayın halka kodlamasını ve 32
nesnenin "bugün en ince halkası" yargısını **tek bir kişi** yaptı, ve o kişi aynı zamanda
bu yargıların desteklediği tezi savunan kişi. Bu, korpusun bilinen en büyük sınırıdır ve
kod kitapçığının §6.1'inde açıkça yazılıdır.

Bir kişinin bir saatlik emeği bu sınırı kaldırır.

---

## Aranıyor

Kod kitapçığını okuyup altı halkanın karar sorularını uygulayabilen, **çalışmanın
yazarından bağımsız** bir kişi. Uzmanlık gerekmiyor.

**Yapılacak iş:** `kodlama-formu.html` dosyasını tarayıcıda açıp doldurmak. 79 olay +
10 nesne; her biri için altı düğmeden birine basılıyor. Yaklaşık **bir saat**. Kurulum ve
yazı yazmak gerekmiyor. Elektronik tabloyu tercih edenler için `kodlama-formu-BOS.xlsx`
de var.

**Gönderilecek yer:** depodaki *Issues* sekmesinden ya da yazara doğrudan.

**Katkı, isterseniz adınızla anılır.** İstemezseniz anılmaz.

---

## Klasördeki dosyalar

| Dosya | Kime |
|---|---|
| **`kodlama-formu.html`** | **Gönüllüye — önerilen yol.** Tarayıcıda açılır, kurulum yok, altı düğmeden birine basılır. Hiçbir dış sunucuya istek yapmaz; cevaplar yalnız tarayıcıda kalır ve sonunda bir dosya olarak inip elle gönderilir. |
| `kodlama-formu-BOS.xlsx` | Gönüllüye — yedek yol, elektronik tablo tercih ederse. **Önizleme penceresinde değil, indirip Excel/WPS/LibreOffice ile açılmalı**; açılır listeler önizlemede çalışmaz. |
| `gonulluye-mesaj-TASLAK.md` | Yazara — gönüllüye yazılacak mesajın taslağı |
| `kappa-hesapla.py` | Yazara — dolu formu `data/` içindeki ilk kodlamayla karşılaştırır, Cohen κ hesaplar |

### Körleme hakkında

Gönüllüden istenen, formu doldururken çalışmaya ve `data/` içindeki dosyalara
*bakmamasıdır*. İlk kodlama zaten herkese açık yayımlıdır (`data/events.csv` →
`link`, `data/objects.csv` → `thinnest_link`), yani körleme **usule dayanır,
gizliliğe değil.** Bir hakem bunu bilmelidir; raporlanacak sonuçta da belirtilecek.

## Alt örneklem nasıl seçildi

Rastgele değil, **tekrar üretilebilir**: uygarlık katmanına göre orantılı tabakalama
(6 modern, 2 Osmanlı, 2 Roma), her tabaka içinde tohumu **20260825** olan bir karıştırma.

Seçilen nesneler: `aqueducts` · `integrated-circuit` · `iznik` · `kilogram` ·
`latin-alphabet` · `sinan` · `supermarket` · `television` · `transistor` · `ubykh`
— dördü kopmuş, altısı tutmuş zincir. Kodlanacak **79 olay**; ilk kodlamada altı halkanın
hepsi temsil ediliyor (aparat 20, paket 17, bakım 14, çözücü 13, örtük bilgi 8, bağlam 7).

## Dolu form geldiğinde

```bash
python3 kappa-hesapla.py kodlama-SONUC.csv        # HTML formundan geldiyse
python3 kappa-hesapla.py doldurulmus-form.xlsx    # elektronik tablodan geldiyse (pip install openpyxl)
```

Betik ağa hiçbir şey göndermez. Çıktı: yüzde uyum, Cohen κ, halka bazında döküm ve
anlaşmazlığa düşülen satırların listesi.

## Sonuç ne çıkarsa çıksın yayımlanacaktır

Bu, şimdiden ve yazılı olarak taahhüt edilmiştir — sonradan karar vermek zor olur.

- **κ yüksek çıkarsa:** kodlama şemasının tek bir okuyucunun dışında da uygulanabildiğinin
  kanıtı olur.
- **κ düşük çıkarsa:** bulgu şudur — *"altı halkalı şema, tek bir kodlayıcının dışında
  güvenilir biçimde uygulanamıyor."* Bu da bir sonuçtur ve çalışmanın 8. kuralına göre
  saklanamaz.

Anlaşmazlığın nerede çıkacağı şimdiden tahmin edilebilir: kurumsal olaylar — yasak, bütçe,
sürgün, vakıf. Kod kitapçığı §2.1 zaten orayı setin en tartışmalı yeri olarak işaretliyor.
Oradaki anlaşmazlık bir hata değil, şemanın sınırının ölçüsüdür.

## Sonuç geldiğinde güncellenecek yerler

1. `data/CODEBOOK.md` ve `data/KOD-KITAPCIGI.md` §6.1 — şu an "κ yoktur" diyor
2. Varsa gönderilmiş veri makalesinin sınırlar bölümü
3. `index.html` içindeki "söyleyemez" listesi
4. Yeni bir sürüm ve düzeltme günlüğü kaydı
