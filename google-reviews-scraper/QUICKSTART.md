# 🚀 QUICKSTART - Google Reviews Scraper

Rychlý průvodce pro spuštění scraperu Google recenzí AAA Auto.

## ⚡ Rychlé spuštění (5 kroků)

### 1. Nainstalujte Python 3.8+

Zkontrolujte verzi:
```bash
python --version
```

### 2. Vytvořte virtuální prostředí

```bash
cd google-reviews-scraper
python -m venv venv
```

Aktivujte:
- **Linux/Mac**: `source venv/bin/activate`
- **Windows**: `venv\Scripts\activate`

### 3. Nainstalujte závislosti

```bash
pip install -r requirements.txt
```

### 4. Nastavte URL pro AAA Auto

**Způsob A: Přes .env soubor**

```bash
cp .env.example .env
```

Upravte `.env`:
```env
GOOGLE_PLACE_URL=https://www.google.com/maps/place/AAA+AUTO+Praha/@50.xxx,14.xxx/...
```

**Způsob B: Přímo v kódu**

Upravte `scraper.py` na řádku cca 297:
```python
PLACE_URL = "https://www.google.com/maps/place/AAA+AUTO+Praha/@..."
```

### 5. Spusťte scraper

```bash
python scraper.py
```

## 📍 Jak získat správnou URL

1. Otevřete [Google Maps](https://maps.google.com)
2. Vyhledejte: **"AAA Auto Praha"** (nebo jiná pobočka)
3. Klikněte na výsledek
4. Zkopírujte celou URL z adresního řádku

Příklad správné URL:
```
https://www.google.com/maps/place/AAA+AUTO+Praha/@50.0755381,14.4378005,17z/data=!3m1!4b1!4m6!3m5!...
```

## ⏱️ Nastavení období

Upravte v `scraper.py` (funkce `main()`):

```python
# Poslední 3 měsíce (výchozí)
DATE_FROM = datetime.now() - timedelta(days=90)
DATE_TO = datetime.now()

# Nebo konkrétní období
DATE_FROM = datetime(2024, 1, 1)  # Od 1.1.2024
DATE_TO = datetime(2024, 12, 31)  # Do 31.12.2024
```

## 📊 Kde najdu výsledky?

Po dokončení najdete v adresáři soubory:
- `aaa_auto_reviews_YYYYMMDD_HHMMSS.csv` - Excel/CSV formát
- `aaa_auto_reviews_YYYYMMDD_HHMMSS.json` - JSON formát

## 🎯 Tipy pro více recenzí

Pokud chcete získat více recenzí, zvyšte `max_scrolls`:

```python
reviews = scraper.scrape_reviews(
    place_url=PLACE_URL,
    date_from=DATE_FROM,
    date_to=DATE_TO,
    max_scrolls=50  # Změňte z 30 na 50 nebo více
)
```

## ❓ Nejčastější problémy

### Chyba: "ChromeDriver not found"

**Řešení:**
```bash
pip install --upgrade webdriver-manager
```

### Scraper nenajde recenze

**Řešení:**
1. Zkontrolujte URL - musí ukazovat na konkrétní místo
2. Zkuste vypnout headless režim:
   ```python
   scraper = GoogleReviewsScraper(headless=False)
   ```
3. Zvyšte čas čekání v kódu (změňte `time.sleep(5)` na `time.sleep(10)`)

### Python není nainstalovaný

**Windows:**
1. Stáhněte z [python.org](https://python.org)
2. Při instalaci zaškrtněte "Add Python to PATH"

**Linux:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**Mac:**
```bash
brew install python3
```

## 📞 Potřebujete pomoc?

1. Zkontrolujte [README.md](README.md) pro detailní dokumentaci
2. Zkontrolujte logy v konzoli - obsahují užitečné informace
3. Zkuste spustit s `headless=False` pro vizuální debugging

## ✅ Checklist před spuštěním

- [ ] Python 3.8+ nainstalovaný
- [ ] Virtuální prostředí vytvořené a aktivované
- [ ] Závislosti nainstalovány (`pip install -r requirements.txt`)
- [ ] URL pro AAA Auto nastavená v `.env` nebo `scraper.py`
- [ ] Období nastaveno v `scraper.py` (pokud potřebujete jiné než poslední 3 měsíce)

---

**Hotovo! Teď stačí spustit `python scraper.py` a počkat na výsledky.** 🎉
