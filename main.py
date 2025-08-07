from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from bot.handlers import register_handlers
from cronjobs.follow_up_cron import run_follow_up_cron
import asyncio
import threading
import time

async def cron_worker():
    """Run cron jobs periodically"""
    while True:
        try:
            await run_follow_up_cron()
            print("Cron job completed\n")
        except Exception as e:
            print(f"Error in cron job: {e}")

        await asyncio.sleep(60)

def start_cron_thread():
    """Start cron in separate thread"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(cron_worker())

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    register_handlers(app)
    
    cron_thread = threading.Thread(target=start_cron_thread, daemon=True)
    cron_thread.start()
    
    app.run_polling()

if __name__ == "__main__":
    main() 