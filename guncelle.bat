@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo ================================================
echo   Bilginin Tasinma Yolculugu - GitHub guncelle
echo ================================================
echo.

git rev-parse --is-inside-work-tree >/dev/null 2>&1
if errorlevel 1 (
  echo HATA: Bu klasor bir git deposu degil.
  echo Bu dosyayi, depoyu klonladiginiz klasorun icine koyun.
  echo.
  pause
  exit /b 1
)

echo Degisiklikler:
git status --short
echo.

set "MSG="
set /p MSG=Commit mesaji (bos birakirsaniz "guncelleme" yazilir): 
if not defined MSG set "MSG=guncelleme"
echo.

git add -A
git commit -m "%MSG%"
echo.
echo GitHub ile esitleniyor...
git pull --rebase
if errorlevel 1 (
  echo.
  echo UYARI: Cakisma var. Once GitHub uzerindeki degisikliklere bakin.
  echo.
  pause
  exit /b 1
)

git push
if errorlevel 1 (
  echo.
  echo HATA: Gonderilemedi. Internet baglantisini ve GitHub girisinizi kontrol edin.
  echo.
  pause
  exit /b 1
)

echo.
echo ================================================
echo   BITTI. Depo guncellendi.
echo ================================================
echo.
pause
