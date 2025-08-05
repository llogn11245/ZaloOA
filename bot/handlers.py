from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
from bot.button_handlers import *
from core.form_service import get_form_message

START_TEXT = "Xin chào! Cảm ơn bạn đã kết nối cùng chúng tôi.\nNếu bạn đã biết đến bot zaloOA này chứng tỏ bạn có tìm hiểu về BCP, mạn phép cho mình hỏi là bạn đã tạo tài khoản BCP chưa?"

async def start_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Tạo rồi", callback_data="yesoption1")],
        [InlineKeyboardButton("Chưa tạo", callback_data="nooption1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(START_TEXT, reply_markup= reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    action = query.data

    if action == 'yesoption1':
        await handle_yes(query)
    elif action == 'nooption1': 
        await handle_no(query)

def register_handlers(dp):
    dp.add_handler(CommandHandler("start", start_message))
    dp.add_handler(CallbackQueryHandler(button_handler))
    # dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start_message))
