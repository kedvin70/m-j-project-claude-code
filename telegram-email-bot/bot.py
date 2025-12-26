#!/usr/bin/env python3
"""
Telegram bot pro odesílání zpráv emailem
Přijímá textové i hlasové zprávy a odesílá je jako email
"""

import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from datetime import datetime
from dotenv import load_dotenv

# Načtení proměnných prostředí
load_dotenv()

# Konfigurace loggingu
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Email konfigurace
EMAIL_FROM = os.getenv('EMAIL_FROM', 'kedvin70@gmail.com')
EMAIL_TO = os.getenv('EMAIL_TO', 'edvin.kuhner@aaaauto.cz')
EMAIL_SUBJECT = os.getenv('EMAIL_SUBJECT', 'nápad do poznámek')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Telegram konfigurace
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')


def send_email(message_text: str, from_user: str = "Telegram") -> bool:
    """
    Odešle zprávu jako email přímo z Telegramu

    Args:
        message_text: Text zprávy k odeslání
        from_user: Jméno uživatele nebo zdroje zprávy

    Returns:
        True pokud bylo odeslání úspěšné, jinak False
    """
    try:
        # Vytvoření email zprávy
        msg = MIMEMultipart()
        # Nastavení odesílatele jako "Telegram Bot" nebo jméno uživatele
        msg['From'] = formataddr((f"📱 {from_user}", EMAIL_FROM))
        msg['To'] = EMAIL_TO
        msg['Subject'] = EMAIL_SUBJECT
        msg['Reply-To'] = EMAIL_TO  # Odpovědi půjdou na cílový email

        # Přidání těla emailu
        msg.attach(MIMEText(message_text, 'plain', 'utf-8'))

        # Připojení k SMTP serveru a odeslání
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            server.send_message(msg)

        logger.info(f"Email úspěšně odeslán z Telegramu na {EMAIL_TO}")
        return True

    except Exception as e:
        logger.error(f"Chyba při odesílání emailu: {e}")
        return False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler pro /start příkaz"""
    welcome_message = (
        "Vítejte v botu pro přímé odesílání poznámek emailem! 📧\n\n"
        "Jednoduše mi napište textovou zprávu nebo pošlete hlasovou zprávu "
        f"a já ji okamžitě odešlu jako email přímo z Telegramu na: {EMAIL_TO}\n\n"
        "Příkazy:\n"
        "/start - Zobrazit tuto zprávu\n"
        "/help - Nápověda"
    )
    await update.message.reply_text(welcome_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler pro /help příkaz"""
    help_text = (
        "📱 Jak používat tento bot:\n\n"
        "1. Napište mi jakoukoliv textovou zprávu\n"
        "2. Nebo pošlete hlasovou zprávu 🎤\n"
        "3. Bot okamžitě odešle zprávu jako email přímo z Telegramu\n\n"
        f"📧 Email bude odeslán na: {EMAIL_TO}\n"
        f"📝 S předmětem: {EMAIL_SUBJECT}\n\n"
        "Vaše zprávy budou odeslány přesně tak, jak je napíšete, "
        "s časovým razítkem z Telegramu."
    )
    await update.message.reply_text(help_text)


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handler pro textové zprávy
    Odešle textovou zprávu přímo jako email z Telegramu
    """
    user = update.effective_user
    message_text = update.message.text
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")

    logger.info(f"Přijata textová zpráva od {user.username}: {message_text}")

    # Zpráva bude odeslána přímo, s timestampem
    email_body = f"{message_text}\n\n---\nOdesláno z Telegramu: {timestamp}"

    # Jméno odesílatele pro email
    from_name = user.username or user.first_name or "Telegram"

    # Odeslání emailu
    await update.message.reply_text("Odesílám email... ⏳")

    if send_email(email_body, from_user=from_name):
        await update.message.reply_text("✅ Email byl úspěšně odeslán!")
    else:
        await update.message.reply_text("❌ Chyba při odesílání emailu. Zkuste to prosím znovu.")


async def handle_voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handler pro hlasové zprávy
    Stáhne hlasovou zprávu a odešle informaci o ní emailem přímo z Telegramu
    """
    user = update.effective_user
    voice = update.message.voice
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")

    logger.info(f"Přijata hlasová zpráva od {user.username}")

    try:
        # Stažení hlasového souboru
        voice_file = await context.bot.get_file(voice.file_id)
        file_path = f"voice_{voice.file_id}.ogg"
        await voice_file.download_to_drive(file_path)

        # Formátování zprávy pro email - jednoduché a přímé
        duration = voice.duration
        email_body = (
            f"🎤 HLASOVÁ ZPRÁVA ({duration} sekund)\n\n"
            f"Soubor uložen: {file_path}\n"
            f"File ID: {voice.file_id}\n\n"
            f"---\nOdesláno z Telegramu: {timestamp}"
        )

        # Jméno odesílatele pro email
        from_name = user.username or user.first_name or "Telegram"

        # Odeslání emailu
        await update.message.reply_text("Zpracovávám hlasovou zprávu a odesílám email... ⏳")

        if send_email(email_body, from_user=from_name):
            await update.message.reply_text("✅ Email s hlasovou zprávou byl odeslán!")
        else:
            await update.message.reply_text("❌ Chyba při odesílání emailu. Zkuste to prosím znovu.")

        # Volitelně: smazání lokálního souboru
        # os.remove(file_path)

    except Exception as e:
        logger.error(f"Chyba při zpracování hlasové zprávy: {e}")
        await update.message.reply_text("❌ Chyba při zpracování hlasové zprávy.")


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler pro chyby"""
    logger.error(f"Update {update} způsobil chybu: {context.error}")


def main() -> None:
    """Hlavní funkce pro spuštění bota"""

    # Kontrola konfigurace
    if not TELEGRAM_TOKEN:
        logger.error("TELEGRAM_TOKEN není nastavený! Nastavte ho v .env souboru.")
        return

    if not EMAIL_PASSWORD:
        logger.error("EMAIL_PASSWORD není nastavené! Nastavte ho v .env souboru.")
        return

    # Vytvoření aplikace
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Přidání handlerů
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice_message))
    application.add_error_handler(error_handler)

    # Spuštění bota
    logger.info("Bot je spuštěn a čeká na zprávy...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
