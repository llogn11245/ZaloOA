from telegram.ext import ApplicationBuilder
from bot.handlers import register_handlers
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    FORM_URL  = os.getenv("FORM_URL")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    register_handlers(app)
    app.run_polling()

if __name__ == "__main__":
    main()
