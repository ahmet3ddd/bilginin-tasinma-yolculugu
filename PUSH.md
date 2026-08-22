# Depoyu kurma / Setting the repository up

Bu klasör **eksiksizdir** — `index.html` dahil. Tek yapmanız gereken depoyu açıp itmek.

## 1. GitHub'da boş bir depo açın

- Ad: `bilginin-tasinma-yolculugu`
- Görünürlük: **Private** (şimdilik yayınlamıyoruz)
- README, .gitignore, lisans **eklemeyin** — hepsi bu klasörde zaten var

## 2. İtin / Push

Bu klasörün içinde:

```bash
git init -b main
git add .
git commit -m "Aktarım Zinciri v4.6 — ilk yükleme"
git remote add origin https://github.com/ahmet3ddd/bilginin-tasinma-yolculugu.git
git push -u origin main
```

## 3. Kontrol

Push'tan sonra depoda şunlar olmalı:

```
index.html                     ~692 KB, tek dosya, Model v4.6
README.md                      kapak görseli + tez + sürüm notu
LICENSE                        MIT
.nojekyll                      Pages'in dosyaları olduğu gibi sunması için
.gitignore
.github/workflows/pages.yml    KAPALI — kendiliğinden çalışmaz
assets/og.png                  sosyal medya kartı (1200×630)
docs/01…04                     uzman incelemesi ve revizyon belgeleri
```

## 4. Bundan sonra

Depo hazır ama **yayında değil**. Yayına almak istediğinizde README'deki
"Yayına alma" bölümünü izleyin — üç adım.

`index.html` içindeki `canonical`, `og:url`, `og:image` ve kaynak kodu bağlantısı
bu depoya göre ayarlandı: `https://ahmet3ddd.github.io/bilginin-tasinma-yolculugu/`
Depoyu başka bir adla açarsanız bu dört yeri güncellemek gerekir.
