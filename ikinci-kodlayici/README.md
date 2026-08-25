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

**Yapılacak iş:** `kodlama-formu-BOS.xlsx` dosyasını doldurmak. 79 olay + 10 nesne, hepsi
açılır liste. Yaklaşık **bir saat**. Yazı yazmak gerekmiyor.

**Gönderilecek yer:** depodaki *Issues* sekmesinden ya da yazara doğrudan.

**Katkı, isterseniz adınızla anılır.** İstemezseniz anılmaz.

---

## Klasördeki dosyalar

| Dosya | Kime |
|---|---|
| `kodlama-formu-BOS.xlsx` | **Gönüllüye.** İhtiyaç duyulan tek dosya. |
| `gonulluye-mesaj-TASLAK.md` | Yazara — gönüllüye yazılacak mesajın taslağı |
| `CEVAP-ANAHTARI-*.csv` | Yazara — ilk kodlama, karşılaştırma için |
| `kappa-hesapla.py` | Yazara — dolu formu anahtarla karşılaştırır, Cohen κ hesaplar |

### Cevap anahtarı hakkında dürüst bir not

Bu klasördeki "cevap anahtarı" bir sır değildir ve olamaz: ilk kodlamanın tamamı zaten
`data/events.csv` içinde, `link` sütununda, herkese açık olarak yayımlanmıştır. Yani
körleme **usule dayanır, gizliliğe değil** — gönüllüden istenen, formu doldururken
çalışmaya ve veri dosyalarına *bakmamasıdır*. Bir hakem bunu bilmelidir; bu yüzden burada
yazılıdır ve raporlanacak sonuçta da belirtilecektir.

## Alt örneklem nasıl seçildi

Rastgele değil, **tekrar üretilebilir**: uygarlık katmanına göre orantılı tabakalama
(6 modern, 2 Osmanlı, 2 Roma), her tabaka içinde tohumu **20260825** olan bir karıştırma.

Seçilen nesneler: `aqueducts` · `integrated-circuit` · `iznik` · `kilogram` ·
`latin-alphabet` · `sinan` · `supermarket` · `television` · `transistor` · `ubykh`
— dördü kopmuş, altısı tutmuş zincir. Kodlanacak **79 olay**; ilk kodlamada altı halkanın
hepsi temsil ediliyor (aparat 20, paket 17, bakım 14, çözücü 13, örtük bilgi 8, bağlam 7).

## Dolu form geldiğinde

```bash
pip install openpyxl
python3 kappa-hesapla.py doldurulmus-form.xlsx
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
