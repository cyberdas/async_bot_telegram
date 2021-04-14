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


settings_menu = CallbackData("user", "property", "value")
region_menu = CallbackData("user", "region")

def get_markup():
    return(
        InlineKeyboardMarkup(row_width=1,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Изменить вакансию", callback_data=settings_menu.new(
                        property="vacancy", value="change"
                    )),
                    InlineKeyboardButton(text="Изменить регион", callback_data=settings_menu.new(
                        property="region", value="change"
                    )),
                    InlineKeyboardButton(text="Изменить тип занятости", callback_data=settings_menu.new(
                        property="job_type", value="change"
                    ))
                ]
            ]
        )
    )


choice = InlineKeyboardMarkup(row_width=1)
change_vacancy = InlineKeyboardButton(text="Изменить вакансию", callback_data=settings_menu.new(
                        property="vacancy", value="change"))
choice.insert(change_vacancy)
change_region = InlineKeyboardButton(
    text="Изменить регион", callback_data=settings_menu.new(
        property="region", value="change"))
choice.insert(change_region)
change_job_type = InlineKeyboardButton(
    text="Изменить тип занятости", callback_data=settings_menu.new(
        property="job_type", value="change"))
choice.insert(change_job_type)


region_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        InlineKeyboardButton(text="Москва", callback_data=region_menu.new(
            region="Moscow"
        )),
        InlineKeyboardButton(text="Россия", callback_data=region_menu.new(
            region="Russia"
        ))
        ]
    )
