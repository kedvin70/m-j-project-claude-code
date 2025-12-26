# Telegram Email Bot

Python aplikace s Telegram botem, který přijímá textové a hlasové zprávy a odesílá je jako emaily.

## Funkce

- Přijímá textové zprávy z Telegramu
- Přijímá hlasové zprávy z Telegramu
- Automaticky odesílá zprávy jako email
- Konfigurovatelný odesílatel, příjemce a předmět emailu

## Požadavky

- Python 3.8 nebo vyšší
- Telegram Bot Token (získáte od [@BotFather](https://t.me/botfather))
- Gmail účet s App Password pro odesílání emailů

## Instalace

1. Naklonujte nebo stáhněte tento projekt:
```bash
cd telegram-email-bot
```

2. Vytvořte virtuální prostředí (doporučeno):
```bash
python3 -m venv venv
source venv/bin/activate  # Na Windows: venv\Scripts\activate
```

3. Nainstalujte závislosti:
```bash
pip install -r requirements.txt
```

## Konfigurace

### 1. Vytvoření Telegram Bota

1. Otevřete Telegram a vyhledejte [@BotFather](https://t.me/botfather)
2. Pošlete příkaz `/newbot`
3. Zadejte jméno pro vašeho bota
4. Zadejte uživatelské jméno pro bota (musí končit na "bot")
5. BotFather vám pošle token - ten si uložte

### 2. Nastavení Gmail App Password

Pro odesílání emailů z Gmail účtu potřebujete App Password:

1. Přihlaste se do svého Google účtu
2. Jděte na [https://myaccount.google.com/security](https://myaccount.google.com/security)
3. Zapněte "2-Step Verification" pokud ještě není aktivní
4. Vyhledejte "App passwords" a vytvořte nové heslo pro aplikaci
5. Vyberte "Mail" a "Other (Custom name)"
6. Pojmenujte ji např. "Telegram Bot"
7. Google vygeneruje 16-znakové heslo - to si uložte

### 3. Vytvoření .env souboru

Vytvořte soubor `.env` v kořenovém adresáři projektu (zkopírujte z `.env.example`):

```bash
cp .env.example .env
```

Otevřete `.env` a vyplňte vaše údaje:

```env
# Telegram Bot Configuration
TELEGRAM_TOKEN=váš_telegram_bot_token

# Email Configuration
EMAIL_FROM=kedvin70@gmail.com
EMAIL_TO=edvin.kuhner@aaaauto.cz
EMAIL_SUBJECT=nápad do poznámek
EMAIL_PASSWORD=váš_gmail_app_password

# SMTP Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

**DŮLEŽITÉ:**
- `TELEGRAM_TOKEN` - token od BotFather
- `EMAIL_PASSWORD` - App Password z Google (16 znaků bez mezer)
- Nikdy nesdílejte `.env` soubor - obsahuje citlivé údaje!

## Spuštění

Spusťte bota příkazem:

```bash
python bot.py
```

Nebo pokud máte aktivní virtuální prostředí:

```bash
python3 bot.py
```

Bot by měl vypsat:
```
Bot je spuštěn a čeká na zprávy...
```

## Použití

1. Otevřete Telegram a najděte svého bota (podle uživatelského jména)
2. Pošlete příkaz `/start` pro zobrazení uvítací zprávy
3. Pošlete příkaz `/help` pro nápovědu

### Odesílání zpráv

**Textová zpráva:**
- Napište jakýkoliv text do chatu s botem
- Bot automaticky odešle zprávu jako email

**Hlasová zpráva:**
- Nahrajte a pošlete hlasovou zprávu
- Bot stáhne zprávu a odešle informaci o ní emailem

### Příkazy

- `/start` - Zobrazí uvítací zprávu
- `/help` - Zobrazí nápovědu

## Struktura projektu

```
telegram-email-bot/
├── bot.py              # Hlavní soubor aplikace
├── requirements.txt    # Python závislosti
├── .env.example        # Vzorový konfigurační soubor
├── .env               # Váš konfigurační soubor (není v gitu)
├── .gitignore         # Soubory ignorované gitem
└── README.md          # Tento soubor
```

## Řešení problémů

### Bot nereaguje na zprávy
- Zkontrolujte, zda je bot spuštěný
- Ověřte, že TELEGRAM_TOKEN je správný
- Zkuste restartovat bota

### Email se neposílá
- Zkontrolujte EMAIL_PASSWORD (App Password, ne běžné heslo)
- Ověřte, že máte zapnuté 2-Step Verification v Google účtu
- Zkontrolujte SMTP nastavení (server a port)
- Podívejte se do logů na konkrétní chybovou zprávu

### "Authentication failed" při odesílání emailu
- Ujistěte se, že používáte App Password, ne běžné heslo
- App Password musí být 16 znaků bez mezer
- Zkontrolujte, že email v EMAIL_FROM je správný

## Bezpečnost

- **NIKDY** nesdílejte váš `.env` soubor
- **NIKDY** necommitujte `.env` do git repozitáře
- Telegram token a email heslo jsou citlivé údaje
- Používejte App Password, ne vaše hlavní heslo k emailu

## Technologie

- **python-telegram-bot** - Knihovna pro práci s Telegram Bot API
- **smtplib** - Vestavěná Python knihovna pro odesílání emailů
- **python-dotenv** - Načítání konfigurace z .env souboru

## Autor

Vytvořeno pro odesílání nápadů do poznámek přes Telegram

## Licence

Tento projekt je volně k použití pro osobní účely.
