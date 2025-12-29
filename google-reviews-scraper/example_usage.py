#!/usr/bin/env python3
"""
Příklady použití Google Reviews Scraperu
"""

from scraper import GoogleReviewsScraper
from datetime import datetime, timedelta

# ============================================
# PŘÍKLAD 1: Základní použití
# ============================================

def example_basic():
    """Základní scraping recenzí"""
    print("=== PŘÍKLAD 1: Základní použití ===\n")

    scraper = GoogleReviewsScraper(headless=True)

    # AAA Auto Praha - upravte URL na skutečnou
    url = "https://www.google.com/maps/place/AAA+AUTO+Praha/"

    reviews = scraper.scrape_reviews(
        place_url=url,
        max_scrolls=10
    )

    print(f"Získáno {len(reviews)} recenzí")

    # Uložení
    scraper.save_to_csv('example_basic.csv')
    scraper.save_to_json('example_basic.json')


# ============================================
# PŘÍKLAD 2: Filtrování podle období
# ============================================

def example_date_filter():
    """Scraping recenzí za konkrétní období"""
    print("=== PŘÍKLAD 2: Filtrování podle období ===\n")

    scraper = GoogleReviewsScraper(headless=True)

    # Recenze za poslední měsíc
    date_from = datetime.now() - timedelta(days=30)
    date_to = datetime.now()

    url = "https://www.google.com/maps/place/AAA+AUTO+Praha/"

    reviews = scraper.scrape_reviews(
        place_url=url,
        date_from=date_from,
        date_to=date_to,
        max_scrolls=20
    )

    print(f"Získáno {len(reviews)} recenzí za poslední měsíc")
    print(f"Období: {date_from.strftime('%Y-%m-%d')} až {date_to.strftime('%Y-%m-%d')}")


# ============================================
# PŘÍKLAD 3: Konkrétní období
# ============================================

def example_specific_period():
    """Scraping recenzí za konkrétní kalendářní období"""
    print("=== PŘÍKLAD 3: Konkrétní období ===\n")

    scraper = GoogleReviewsScraper(headless=True)

    # Recenze za celý rok 2024
    date_from = datetime(2024, 1, 1)
    date_to = datetime(2024, 12, 31)

    url = "https://www.google.com/maps/place/AAA+AUTO+Praha/"

    reviews = scraper.scrape_reviews(
        place_url=url,
        date_from=date_from,
        date_to=date_to,
        max_scrolls=50
    )

    print(f"Získáno {len(reviews)} recenzí za rok 2024")

    # Uložení s časovým razítkem v názvu
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    scraper.save_to_csv(f'reviews_2024_{timestamp}.csv')


# ============================================
# PŘÍKLAD 4: Analýza recenzí
# ============================================

def example_analysis():
    """Scraping a základní analýza recenzí"""
    print("=== PŘÍKLAD 4: Analýza recenzí ===\n")

    scraper = GoogleReviewsScraper(headless=True)

    url = "https://www.google.com/maps/place/AAA+AUTO+Praha/"

    reviews = scraper.scrape_reviews(
        place_url=url,
        max_scrolls=30
    )

    # Statistiky
    total = len(reviews)
    if total > 0:
        # Průměrné hodnocení
        ratings = [r['rating'] for r in reviews if r['rating']]
        avg_rating = sum(ratings) / len(ratings) if ratings else 0

        # Počet podle hvězdiček
        rating_counts = {i: 0 for i in range(1, 6)}
        for r in reviews:
            if r['rating']:
                rating_counts[r['rating']] += 1

        print(f"Celkem recenzí: {total}")
        print(f"Průměrné hodnocení: {avg_rating:.2f} ⭐")
        print("\nRozdělení hodnocení:")
        for stars in range(5, 0, -1):
            count = rating_counts[stars]
            percentage = (count / total * 100) if total > 0 else 0
            bar = '█' * int(percentage / 2)
            print(f"{stars}⭐: {bar} {count} ({percentage:.1f}%)")

        # Nejnovější recenze
        print("\n--- Nejnovější recenze ---")
        for review in reviews[:3]:
            print(f"\n{review['author']} - {review['rating']}⭐ - {review['date_text']}")
            print(f"{review['text'][:100]}...")


# ============================================
# PŘÍKLAD 5: Více poboček najednou
# ============================================

def example_multiple_locations():
    """Scraping recenzí z více poboček AAA Auto"""
    print("=== PŘÍKLAD 5: Více poboček ===\n")

    locations = {
        'Praha': 'https://www.google.com/maps/place/AAA+AUTO+Praha/',
        'Brno': 'https://www.google.com/maps/place/AAA+AUTO+Brno/',
        'Ostrava': 'https://www.google.com/maps/place/AAA+AUTO+Ostrava/'
    }

    all_reviews = {}

    for city, url in locations.items():
        print(f"\nZískávám recenze pro {city}...")

        scraper = GoogleReviewsScraper(headless=True)

        reviews = scraper.scrape_reviews(
            place_url=url,
            max_scrolls=20
        )

        all_reviews[city] = reviews

        # Uložení pro každé město zvlášť
        timestamp = datetime.now().strftime('%Y%m%d')
        scraper.save_to_csv(f'reviews_{city}_{timestamp}.csv')

        print(f"✅ {city}: {len(reviews)} recenzí")

    # Celkový přehled
    print("\n=== CELKOVÝ PŘEHLED ===")
    for city, reviews in all_reviews.items():
        ratings = [r['rating'] for r in reviews if r['rating']]
        avg = sum(ratings) / len(ratings) if ratings else 0
        print(f"{city}: {len(reviews)} recenzí, průměr {avg:.2f}⭐")


# ============================================
# SPUŠTĚNÍ PŘÍKLADŮ
# ============================================

if __name__ == '__main__':
    print("Google Reviews Scraper - Příklady použití\n")
    print("POZOR: Před spuštěním upravte URL na skutečné odkazy z Google Maps!\n")

    # Odkomentujte příklad, který chcete spustit:

    # example_basic()
    # example_date_filter()
    # example_specific_period()
    # example_analysis()
    # example_multiple_locations()

    print("\n✅ Hotovo!")
