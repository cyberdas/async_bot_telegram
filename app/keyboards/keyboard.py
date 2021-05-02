from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.callback_data import CallbackData


async def get_keyboard(search_history):
    search_history_keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    if search_history:
        buttons = [i for i in search_history]
        search_history_keyboard.add(*buttons)
    return search_history_keyboard.add("/cancel")
