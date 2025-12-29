#!/usr/bin/env python3
"""
Google Reviews Scraper pro AAA Auto
Získává recenze z Google Maps pro zadané období
"""

import os
import time
import json
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

# Načtení proměnných prostředí
load_dotenv()

# Konfigurace loggingu
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class GoogleReviewsScraper:
    """Scraper pro získávání Google recenzí"""

    def __init__(self, headless: bool = True):
        """
        Inicializace scraperu

        Args:
            headless: Spustit prohlížeč bez GUI
        """
        self.headless = headless
        self.driver = None
        self.reviews = []

    def setup_driver(self):
        """Nastavení Chrome webdriveru"""
        chrome_options = Options()

        if self.headless:
            chrome_options.add_argument('--headless')

        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()

        logger.info("Chrome driver inicializován")

    def parse_review_date(self, date_text: str) -> Optional[datetime]:
        """
        Parsování data z recenze

        Args:
            date_text: Text s datem (např. "před 2 měsíci", "před týdnem")

        Returns:
            Datum jako datetime objekt
        """
        try:
            now = datetime.now()
            date_text = date_text.lower().strip()

            # Parsování relativních dat
            if 'před' in date_text:
                if 'den' in date_text or 'dny' in date_text or 'dnem' in date_text:
                    # Před X dny
                    days = int(''.join(filter(str.isdigit, date_text)) or 1)
                    return now - timedelta(days=days)
                elif 'týden' in date_text or 'týdny' in date_text or 'týdnem' in date_text:
                    # Před X týdny
                    weeks = int(''.join(filter(str.isdigit, date_text)) or 1)
                    return now - timedelta(weeks=weeks)
                elif 'měsíc' in date_text or 'měsíci' in date_text or 'měsícem' in date_text:
                    # Před X měsíci
                    months = int(''.join(filter(str.isdigit, date_text)) or 1)
                    return now - timedelta(days=months * 30)
                elif 'rok' in date_text or 'roky' in date_text or 'rokem' in date_text or 'lety' in date_text:
                    # Před X lety
                    years = int(''.join(filter(str.isdigit, date_text)) or 1)
                    return now - timedelta(days=years * 365)

            # Pokud není relativní datum, vrátíme aktuální datum
            return now

        except Exception as e:
            logger.warning(f"Chyba při parsování data '{date_text}': {e}")
            return None

    def scroll_reviews(self, scrolls: int = 20):
        """
        Scrollování v panelu recenzí pro načtení více recenzí

        Args:
            scrolls: Počet scrollů
        """
        try:
            # Najít scrollovací panel s recenzemi
            scrollable_div = self.driver.find_element(
                By.XPATH,
                "//div[contains(@class, 'review') or contains(@aria-label, 'Reviews')]//ancestor::div[contains(@class, 'scrollable') or @role='feed']"
            )

            for i in range(scrolls):
                # Scrollovat dolů
                self.driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollHeight',
                    scrollable_div
                )
                time.sleep(2)  # Počkat na načtení
                logger.info(f"Scroll {i+1}/{scrolls}")

        except NoSuchElementException:
            logger.warning("Nebyl nalezen scrollovací panel recenzí")

    def scrape_reviews(
        self,
        place_url: str,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        max_scrolls: int = 20
    ) -> List[Dict]:
        """
        Získání recenzí z Google Maps

        Args:
            place_url: URL místa na Google Maps
            date_from: Datum od (včetně)
            date_to: Datum do (včetně)
            max_scrolls: Maximální počet scrollů

        Returns:
            Seznam recenzí jako slovníky
        """
        try:
            self.setup_driver()

            logger.info(f"Načítám URL: {place_url}")
            self.driver.get(place_url)

            # Čekat na načtení stránky
            time.sleep(5)

            # Kliknout na záložku "Recenze" pokud existuje
            try:
                reviews_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Reviews') or contains(text(), 'Recenze')]"))
                )
                reviews_button.click()
                time.sleep(3)
            except TimeoutException:
                logger.info("Tlačítko Recenze nenalezeno, pokračuji...")

            # Scrollovat pro načtení více recenzí
            logger.info(f"Scrolluji recenze (max {max_scrolls} scrollů)...")
            self.scroll_reviews(scrolls=max_scrolls)

            # Najít všechny recenze
            review_elements = self.driver.find_elements(
                By.XPATH,
                "//div[contains(@class, 'review') or @data-review-id]"
            )

            logger.info(f"Nalezeno {len(review_elements)} elementů recenzí")

            reviews = []

            for idx, review_elem in enumerate(review_elements):
                try:
                    # Získat jméno autora
                    try:
                        author = review_elem.find_element(By.XPATH, ".//div[contains(@class, 'author')]//span | .//button[contains(@class, 'author')]").text
                    except NoSuchElementException:
                        author = "Neznámý"

                    # Získat hodnocení (počet hvězdiček)
                    try:
                        rating_elem = review_elem.find_element(By.XPATH, ".//span[contains(@aria-label, 'stars') or contains(@role, 'img')]")
                        rating_text = rating_elem.get_attribute('aria-label')
                        rating = int(''.join(filter(str.isdigit, rating_text))[:1])
                    except (NoSuchElementException, ValueError):
                        rating = None

                    # Získat datum
                    try:
                        date_elem = review_elem.find_element(By.XPATH, ".//span[contains(@class, 'date') or contains(text(), 'před')]")
                        date_text = date_elem.text
                        review_date = self.parse_review_date(date_text)
                    except NoSuchElementException:
                        date_text = ""
                        review_date = None

                    # Získat text recenze
                    try:
                        # Pokusit se rozbalit celý text
                        try:
                            more_button = review_elem.find_element(By.XPATH, ".//button[contains(text(), 'Více') or contains(@aria-label, 'More')]")
                            more_button.click()
                            time.sleep(0.5)
                        except NoSuchElementException:
                            pass

                        review_text = review_elem.find_element(By.XPATH, ".//span[contains(@class, 'text') or contains(@class, 'review-text')]").text
                    except NoSuchElementException:
                        review_text = ""

                    # Filtrování podle data
                    if date_from and review_date and review_date < date_from:
                        continue
                    if date_to and review_date and review_date > date_to:
                        continue

                    review_data = {
                        'author': author,
                        'rating': rating,
                        'date_text': date_text,
                        'date': review_date.strftime('%Y-%m-%d %H:%M:%S') if review_date else None,
                        'text': review_text,
                        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }

                    reviews.append(review_data)
                    logger.info(f"Recenze {idx+1}: {author} - {rating} hvězd - {date_text}")

                except Exception as e:
                    logger.warning(f"Chyba při parsování recenze {idx+1}: {e}")
                    continue

            self.reviews = reviews
            logger.info(f"Celkem získáno {len(reviews)} recenzí")

            return reviews

        except Exception as e:
            logger.error(f"Chyba při scrapingu: {e}")
            raise

        finally:
            if self.driver:
                self.driver.quit()

    def save_to_csv(self, filename: str = 'reviews.csv'):
        """
        Uložení recenzí do CSV souboru

        Args:
            filename: Název výstupního souboru
        """
        if not self.reviews:
            logger.warning("Žádné recenze k uložení")
            return

        df = pd.DataFrame(self.reviews)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        logger.info(f"Recenze uloženy do {filename}")

    def save_to_json(self, filename: str = 'reviews.json'):
        """
        Uložení recenzí do JSON souboru

        Args:
            filename: Název výstupního souboru
        """
        if not self.reviews:
            logger.warning("Žádné recenze k uložení")
            return

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.reviews, f, ensure_ascii=False, indent=2)

        logger.info(f"Recenze uloženy do {filename}")


def main():
    """Hlavní funkce"""

    # Konfigurace
    # URL místa AAA Auto na Google Maps
    # POZOR: Tuto URL je nutné získat z Google Maps pro konkrétní pobočku AAA Auto
    PLACE_URL = os.getenv('GOOGLE_PLACE_URL', 'https://www.google.com/maps/place/AAA+AUTO/')

    # Období pro filtrování
    # Příklad: recenze za poslední 3 měsíce
    DATE_FROM = datetime.now() - timedelta(days=90)
    DATE_TO = datetime.now()

    # Alternativně lze nastavit konkrétní data
    # DATE_FROM = datetime(2024, 1, 1)
    # DATE_TO = datetime(2024, 12, 31)

    logger.info(f"Spouštím scraper pro období {DATE_FROM.strftime('%Y-%m-%d')} až {DATE_TO.strftime('%Y-%m-%d')}")

    # Vytvoření scraperu
    scraper = GoogleReviewsScraper(headless=True)

    # Získání recenzí
    reviews = scraper.scrape_reviews(
        place_url=PLACE_URL,
        date_from=DATE_FROM,
        date_to=DATE_TO,
        max_scrolls=30
    )

    # Uložení výsledků
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    scraper.save_to_csv(f'aaa_auto_reviews_{timestamp}.csv')
    scraper.save_to_json(f'aaa_auto_reviews_{timestamp}.json')

    logger.info(f"Hotovo! Získáno {len(reviews)} recenzí.")


if __name__ == '__main__':
    main()
