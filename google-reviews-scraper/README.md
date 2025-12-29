# Google Reviews Scraper pro AAA Auto

Aplikace pro získávání recenzí z Google Maps pro firmu AAA Auto s možností filtrování podle období.

## 🚀 Funkce

- ✅ Scraping Google recenzí z Google Maps
- ✅ Filtrování podle období (od-do)
- ✅ Export do CSV a JSON formátu
- ✅ Automatické parsování dat a hodnocení
- ✅ Podpora pro scrollování a načítání více recenzí
- ✅ Logging a reportování průběhu

## 📋 Požadavky

- Python 3.8+
- Chrome/Chromium prohlížeč
- ChromeDriver (instaluje se automaticky)

## 🔧 Instalace

1. **Klonování nebo stažení projektu**

```bash
cd google-reviews-scraper
```

2. **Vytvoření virtuálního prostředí (doporučeno)**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# nebo
venv\Scripts\activate  # Windows
```

3. **Instalace závislostí**

```bash
pip install -r requirements.txt
```

4. **Konfigurace**

Zkopírujte `.env.example` na `.env` a upravte:

```bash
cp .env.example .env
```

Upravte `.env` soubor:
```env
GOOGLE_PLACE_URL=https://www.google.com/maps/place/AAA+AUTO+Praha/@50.0755381,14.4378005,17z/...
```

## 🎯 Jak získat URL pro AAA Auto

1. Otevřete [Google Maps](https://www.google.com/maps)
2. Vyhledejte konkrétní pobočku AAA Auto (např. "AAA Auto Praha")
3. Klikněte na místo
4. Zkopírujte URL z adresního řádku prohlížeče
5. Vložte URL do `.env` souboru jako `GOOGLE_PLACE_URL`

## 💻 Použití

### Základní použití

```bash
python scraper.py
```

### Přizpůsobení v kódu

Upravte `scraper.py` pro změnu období:

```python
# Recenze za poslední 3 měsíce
DATE_FROM = datetime.now() - timedelta(days=90)
DATE_TO = datetime.now()

# Nebo konkrétní období
DATE_FROM = datetime(2024, 1, 1)
DATE_TO = datetime(2024, 12, 31)
```

### Použití jako knihovna

```python
from scraper import GoogleReviewsScraper
from datetime import datetime, timedelta

# Vytvoření scraperu
scraper = GoogleReviewsScraper(headless=True)

# Získání recenzí
reviews = scraper.scrape_reviews(
    place_url="https://www.google.com/maps/place/AAA+AUTO+...",
    date_from=datetime(2024, 1, 1),
    date_to=datetime(2024, 12, 31),
    max_scrolls=30
)

# Uložení
scraper.save_to_csv('reviews.csv')
scraper.save_to_json('reviews.json')

# Přístup k datům
for review in scraper.reviews:
    print(f"{review['author']}: {review['rating']} stars - {review['text']}")
```

## 📊 Výstupní formáty

### CSV

Soubor obsahuje sloupce:
- `author` - Jméno autora recenze
- `rating` - Hodnocení (1-5 hvězdiček)
- `date_text` - Původní text data (např. "před 2 měsíci")
- `date` - Parsované datum (YYYY-MM-DD HH:MM:SS)
- `text` - Text recenze
- `scraped_at` - Čas získání recenze

### JSON

Pole objektů s stejnými vlastnostmi jako CSV:

```json
[
  {
    "author": "Jan Novák",
    "rating": 5,
    "date_text": "před 2 měsíci",
    "date": "2024-10-29 10:30:00",
    "text": "Výborné služby...",
    "scraped_at": "2024-12-29 12:00:00"
  }
]
```

## ⚙️ Parametry

| Parametr | Popis | Výchozí hodnota |
|----------|-------|-----------------|
| `place_url` | URL místa na Google Maps | Z `.env` |
| `date_from` | Datum od (včetně) | Poslední 90 dní |
| `date_to` | Datum do (včetně) | Dnes |
| `max_scrolls` | Počet scrollů pro načtení recenzí | 30 |
| `headless` | Spustit bez GUI | `True` |

## 🐛 Řešení problémů

### Chrome driver se nenainstaluje

```bash
pip install --upgrade webdriver-manager
```

### Recenze se nenačítají

1. Zkontrolujte, zda je URL správná
2. Zvyšte `max_scrolls` pro více recenzí
3. Zkuste vypnout headless režim: `GoogleReviewsScraper(headless=False)`

### Parsování data selhává

Aplikace podporuje český formát dat ("před X dny/měsíci/lety"). Pokud jsou recenze v jiném jazyce, může být potřeba upravit metodu `parse_review_date()`.

## 📝 Poznámky

- Google může blokovat příliš časté požadavky - doporučujeme přidávat pauzy mezi požadavky
- Scraping je závislý na struktuře Google Maps - změny v HTML mohou vyžadovat aktualizaci XPath selektorů
- Pro velké objemy dat může být nutné zvýšit `max_scrolls`
- Doporučujeme používat headless režim pro rychlejší běh

## 📄 Licence

MIT License

## 👤 Autor

Vytvořeno pro AAA Auto
