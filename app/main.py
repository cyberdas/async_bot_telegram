from aiogram import __main__ as aiogram_core

from dotenv import load_dotenv
from config import BOT_TOKEN

from aiogram import Bot, Dispatcher, types, executor, md
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from states import HeadSearch
from search_handlers import search_hh

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(CommandStart())
async def message_start(message: types.Message):
    user = message.from_user.full_name
    source_url = md.hlink("Github", "https://github.com/cyberdas/async_bot_telegram")
    await message.answer(
        f"Привет, {user}!\n"
        f"Команда /help выведет список доступных команд.\n"
        f"Команда /settings позволит изменить настройки.\n"
        f"Исходники: {source_url}", parse_mode="HTML")


@dp.message_handler(CommandHelp())
async def message_help(message: types.Message):
    await message.reply(
        "Вот список моих комманд: \n"
        "Поиск вакансии на hh - /hh_search \n"
        "Поиск вакансии в телеграм каналах - /tg_search \n"
        "Версия бота /version \n"
    )


@dp.message_handler(commands=["version"])
async def cmd_version(message: types.Message):
    bot_version = md.quote_html(str(aiogram_core.SysInfo()))
    await message.reply(
        f"My Engine: {bot_version}")


@dp.message_handler(commands=["hh_search"], state=None) # входной хендлер
async def message_settings(message: types.Message):
    # кнопка с поиском по предыдущей вакансии
    await message.answer(
        "Введите название вакансии"
    )
    await HeadSearch.waiting_for_vacancy.set()


@dp.message_handler(state=HeadSearch.waiting_for_vacancy)
async def hh_search(message: types.Message, state:FSMContext):
    search_for = message.text
    search_results = await search_hh(search_for)
    # await state.update_data({"search": search_results})
    await message.answer(search_results)
    # можете ввести новое название вакансии или перейти к другой команде
    await state.finish()


@dp.message_handler(commands=["tg_search"])
async def tg_search(message: types.Message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
