from services.form_service import get_user_stage, mark_follow_up_sent
from services.google_sheets_service import get_sheets_service
from services.bot_service import BotService
from services.bot_service import UserAction
from utils.date_convert import *
from datetime import datetime
import pytz
import asyncio
from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()

FOLLOW_UP_THRESHOLD = 900 #In seconds
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def send_follow_up(user_id, user_name):
    bot_service = BotService()
    user_action = UserAction(
        user_id=user_id,
        user_name=user_name,
        action_type="follow_up"
    )
    response = bot_service.handle_follow_up(user_action)
    
    # TODO: đổi api gửi thực tế theo từng platform
    # Telegram API
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(
        chat_id=user_id,
        text=response.text,
        reply_markup=response.keyboard_markup 
    )
    mark_follow_up_sent(user_id)
            
async def run_follow_up_cron():
    sheets = get_sheets_service()
    all_users = sheets.get_all_users()
    for user in all_users:
        user_id = user.get('id')  
        user_name = user.get('username', 'User') 
        stage = get_user_stage(user_id)
        # print(f"Checking user {user_name} (ID: {user_id}), stage: {stage}")
        
        if stage != 'follow_up':
            continue
            
        last_follow_up_time = user.get('last_follow_up_sent', '')
        last = iso_to_vn_datetime(last_follow_up_time)
        now = datetime.now(timezone(timedelta(hours=7)))
        diff = compare_datetime(now, last)
        seconds = timedelta_to_seconds(diff)
        
        if seconds is None:
            # User has never been followed up so we don't send anything based on requirements
            continue
        elif seconds > FOLLOW_UP_THRESHOLD:
            await send_follow_up(user_id, user_name)
            print(f"Sent follow-up to {user_name} (ID: {user_id})")
        else:
            print(f"Waiting, only {seconds}s passed (need {FOLLOW_UP_THRESHOLD}s)")