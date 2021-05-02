from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.callback_data import CallbackData


settings_menu = CallbackData("user", "property")
region_menu = CallbackData("region_change", "region")
# job_type_menu = CallbackData(prefix)

choice = InlineKeyboardMarkup(row_width=1)
change_vacancy = InlineKeyboardButton(
    text="Изменить вакансию", callback_data=settings_menu.new(
        property="vacancy"))
choice.insert(change_vacancy)
change_region = InlineKeyboardButton(
    text="Изменить регион", callback_data=settings_menu.new(
        property="region"))
choice.insert(change_region)
change_job_type = InlineKeyboardButton(
    text="Изменить тип занятости", callback_data=settings_menu.new(
        property="job_type"))
choice.insert(change_job_type)


region_keyboard = InlineKeyboardMarkup()
change_moscow = InlineKeyboardButton(
    text="Москва", callback_data=region_menu.new(
        region="Moscowid=113"))
region_keyboard.insert(change_moscow)
change_russia = InlineKeyboardButton(
    text="Россия", callback_data=region_menu.new(
        region="Russiaid=1"))
region_keyboard.insert(change_russia)


job_type_keyboard = InlineKeyboardMarkup()
change_fullday = InlineKeyboardButton(
    text="Полный день",) # callback_data=)
job_type_keyboard.insert(change_fullday)
change_remote = InlineKeyboardButton(
    text="Удаленная работа", 
)