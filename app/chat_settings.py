from aiogram import types

from bot import dp, bot
from keyboards import choice, settings_menu, region_keyboard



@dp.message_handler(commands=["settings"])
async def message_settings(message: types.Message):
    await message.answer(
        "Вы можете выбрать настройки для поиска вакансий \n"
        "Бот будет ежедневно присылать вакансии в соответсвии с настройками",
        reply_markup=choice
    )


@dp.callback_query_handler(settings_menu.filter(property="vacancy"))
async def change_vacancy(call: types.CallbackQuery, callback_data: dict):
    print("test")


@dp.callback_query_handler(settings_menu.filter(property="region"))
async def change_region(call: types.CallbackQuery):
    print("change region")
    await call.message.answer(
        "Веберите регион поиска",
        reply_markup=region_keyboard
    )


@dp.message_handler(commands=["test"])
async def message_settings(message: types.Message):
    await message.answer("Тест")