from aiogram import types

from bot import dp, bot
from keyboards import choice, settings_menu, region_keyboard, region_menu


# принимаем юзера
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

# передавать юзера
@dp.callback_query_handler(settings_menu.filter(property="region"))
async def change_region(call: types.CallbackQuery):
    print("change region")
    print(call.from_user.id)
    await call.message.answer(
        "Веберите регион поиска",
        reply_markup=region_keyboard
    )


@dp.callback_query_handler(settings_menu.filter(property="region_change"))
async def user_choice_region(call: types.CallbackQuery, callback_data: dict):
    # create on start bot
    # await update user db
    await call.answer("Вы изменили регион поиска")


@dp.callback_query_handler(settings_menu.filter(property="job_type"))
async def message_settings(call: types.CallbackQuery):
    await message.answer("Тест")


@dp.callback_query_handler(settings_menu.filter(property=""))
async def change_job_type(call: types.CallbackQuery, callback_data: dict):
    print("Jpb type change")