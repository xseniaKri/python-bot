from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import List

def generate_keyboard(options: List[str]) -> InlineKeyboardMarkup:
    keyboard_layout = [
        [InlineKeyboardButton(text=opt, callback_data=opt) for opt in options[i:i+2]]
        for i in range(0, len(options), 2)
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard_layout)
