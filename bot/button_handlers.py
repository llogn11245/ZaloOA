from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
)
import textwrap

async def handle_yes(query):
    keyboard = [
        [InlineKeyboardButton("📝 Hỗ trợ tạo demand", callback_data="demandoption")],
        [InlineKeyboardButton("🤖 Chat với AI BCP", callback_data="ai_chatoption")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = textwrap.dedent("""
        Bạn đã tạo tài khoản BCP rồi, vậy thì bạn có cần mình giúp gì không?
        Đây là một số chức năng hiện tại của mình:
        1. Hỗ trợ tạo demand
        2. Chat với AI BCP
    """)

    await query.edit_message_text(text=text, reply_markup=reply_markup)

async def handle_no(query):
    await query.edit_message_text("Bạn chọn chưa tạo tài khoản BCP \nmình mong bạn sẽ tạo tài khoản, BCP rất tuyệt")