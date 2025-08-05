from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from bot.handlers import *

def get_form_message(form_url: str):
    keyboard = [
        [InlineKeyboardButton("Điền form", url=form_url)]
    ]
    return "Vui lòng nhấn nút bên dưới để điền form:", InlineKeyboardMarkup(keyboard)
