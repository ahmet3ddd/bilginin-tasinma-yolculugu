# Depoyu güncelleme / Updating the site

Depo **yayındadır**: <https://ahmet3ddd.github.io/bilginin-tasinma-yolculugu/>

## Bir değişikliği yayına almak

1. Değişen dosyaları depoya yükleyin (GitHub arayüzünden sürükle-bırak da olur).
2. **Actions → Deploy to Pages → Run workflow.**
   `.github/workflows/pages.yml` kendiliğinden çalışmaz; elle tetiklenir.
3. Bir iki dakika sonra canlı adresi **sert yenileme** ile açıp kontrol edin
   (Ctrl+F5 / Cmd+Shift+R) — tarayıcı eski dosyayı önbellekte tutuyor olabilir.

Otomatikleştirmek isterseniz `pages.yml` içindeki `push:` bloğunun yorumunu kaldırın;
o zaman her yükleme kendiliğinden yayınlanır.

## Sürüm çıkarırken

`index.html` içinde sürüm numarası **üç yerde** geçer ve üçü birden güncellenmelidir:

| Yer | Ne yazar |
|---|---|
| JSON-LD | `"version":"5.4"` ve `"dateModified"` |
| Künye (`mCreditBody`) | `Sürüm: v5.4` / `Version: v5.4` |
| Yöntem rozeti (`mBadgeNote`) ve alt bilgi (`footerLeft`) | `Sürüm 5.4` / `Model v5.4` |

Ayrıca `CITATION.cff` içindeki `version` ve `date-released`, ve düzeltme günlüğüne
(`var changes`) yeni bir kayıt. Bu çalışmanın kendi tezi gereği: **ne değiştiğini
yazmadan sürüm çıkarılmaz.**

## Zenodo bağlıysa

Zenodo'ya bağlandıktan sonra her **GitHub Release**, yeni bir sürüm DOI'si üretir.
Sürüm çıkarma sırası: dosyaları yükle → Actions ile yayınla → **Releases → Draft a new
release** → etiket `v5.4` → Publish. DOI birkaç dakika içinde Zenodo'da görünür ve
`CITATION.cff` ile `README` içindeki DOI satırına yazılır.

## Depodaki dosyalar

```
index.html                     tek dosya, ~880 KB, dış istek yok
README.md                      künye, tez, veri, lisans
LICENSE                        iki lisans: metin/veri CC BY 4.0, kod MIT
LICENSE-CC-BY-4.0.txt          CC BY 4.0 tam metni
third-party/                   Inter yazı tipi, SIL OFL 1.1 (üçüncü taraf lisansı)
CITATION.cff                   makine okunur atıf künyesi
.nojekyll                      Pages'in dosyaları olduğu gibi sunması için
.github/workflows/pages.yml    elle tetiklenir
assets/og.png                  sosyal medya kartı (1200×630)
data/                          halka-kodlu korpus (CSV + JSON) ve kod kitapçığı
docs/01…05                     çekişmeli eleştiri ve revizyon belgeleri
```

`index.html` içindeki `canonical`, `og:url`, `og:image` ve kaynak kodu bağlantısı bu
depoya göre ayarlanmıştır: `https://ahmet3ddd.github.io/bilginin-tasinma-yolculugu/`
Depoyu başka bir adla açarsanız bu dört yeri güncellemek gerekir.
