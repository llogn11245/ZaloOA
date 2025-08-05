from telegram import Update
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
from bot.messages import START_TEXT, THANK_YOU, BUTTON_FILLED
from core.form_service import get_form_message

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_TEXT)
    text, kb = get_form_message()
    await update.message.reply_text(text, reply_markup=kb)

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.callback_query.data
    if data == "form_filled":
        await update.callback_query.answer()  # remove “loading…”
        await update.callback_query.edit_message_text(THANK_YOU)

def register_handlers(dp):
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(handle_callback))
    # (tuỳ chọn) thêm MessageHandler để bất kỳ tin nhắn nào cũng trigger start()
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start))
