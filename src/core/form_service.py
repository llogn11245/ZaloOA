from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.config import FORM_URL
from bot.messages import FORM_PROMPT, BUTTON_FILLED

def get_form_message():
    kb = InlineKeyboardMarkup([
        [ InlineKeyboardButton("Điền form", url=FORM_URL) ],
        [ InlineKeyboardButton(BUTTON_FILLED, callback_data="form_filled") ]
    ])
    return FORM_PROMPT, kb
