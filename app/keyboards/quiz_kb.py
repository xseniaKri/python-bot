from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import List

def generate_keyboard(options: List) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=opt, callback_data=opt) for opt in options]])
    return keyboard
