# 🚀 Rychlý start - Telegram Email Bot

## ⚡ Spuštění bota na vašem počítači

Bot je **plně nakonfigurovaný a připravený k použití**. Stačí spustit na vašem počítači (ne v Claude Code prostředí).

### Krok 1: Stáhnout kód

```bash
git clone <url-vašeho-repozitáře>
cd m-j-project-claude-code/telegram-email-bot
```

### Krok 2: Vytvořit .env soubor

Vytvořte soubor `.env` v adresáři `telegram-email-bot/`:

```env
# Telegram Bot Configuration
TELEGRAM_TOKEN=8362447766:AAHqINDy3SI33aKbEDpAe_BmbaFJuDIZILU

# Email Configuration
EMAIL_FROM=kedvin70@gmail.com
EMAIL_TO=edvin.kuhner@aaaauto.cz
EMAIL_SUBJECT=nápad do poznámek
EMAIL_PASSWORD=gcdpjreumepkxgxe

# SMTP Configuration (pro Gmail)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

**DŮLEŽITÉ:** Gmail App Password už máte: `gcdp jreu mepk xgxe` (bez mezer)

### Krok 3: Nainstalovat závislosti

```bash
# Vytvořit virtuální prostředí (doporučeno)
python3 -m venv venv

# Aktivovat virtuální prostředí
source venv/bin/activate  # Linux/Mac
# NEBO
venv\Scripts\activate     # Windows

# Nainstalovat závislosti
pip install -r requirements.txt
```

### Krok 4: Spustit bota

```bash
python bot.py
```

Měli byste vidět:
```
Bot je spuštěn a čeká na zprávy...
```

### Krok 5: Otestovat v Telegramu

1. Otevřete Telegram
2. Najděte svého bota (hledejte podle jména, které jste nastavili v BotFather)
3. Pošlete `/start`
4. Napište testovací zprávu: `Test z Telegramu`
5. Zkontrolujte email na edvin.kuhner@aaaauto.cz

---

## 📧 Jak to funguje

Když napíšete v Telegramu:
```
Nápad na zlepšení procesu
```

Email na edvin.kuhner@aaaauto.cz bude vypadat:
```
Od: 📱 [Vaše_Telegram_Jméno]
Předmět: nápad do poznámek

Nápad na zlepšení procesu

---
Odesláno z Telegramu: 26.12.2025 21:35
```

---

## 🔧 Řešení problémů

**Bot nereaguje:**
- Zkontrolujte, že bot běží (vidíte "Bot je spuštěn a čeká na zprávy...")
- Zkontrolujte, že TELEGRAM_TOKEN je správný

**Email se neodešle:**
- Zkontrolujte EMAIL_PASSWORD (Gmail App Password bez mezer)
- Ujistěte se, že máte zapnuté 2-Step Verification v Google účtu
- Zkontrolujte SMTP nastavení

**"Authentication failed":**
- Gmail App Password musí být: `gcdpjreumepkxgxe` (bez mezer)
- Ujistěte se, že používáte App Password, ne běžné heslo

---

## ✅ Co je nastaveno

- ✅ Telegram Bot Token
- ✅ Gmail App Password
- ✅ Email odesílatel: kedvin70@gmail.com
- ✅ Email příjemce: edvin.kuhner@aaaauto.cz
- ✅ Předmět: "nápad do poznámek"

**Vše je připraveno k použití!**
