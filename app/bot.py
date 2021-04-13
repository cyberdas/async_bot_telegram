import asyncio
import os
from aiocache import cached, Cache
from aiocache.serializers import PickleSerializer
from aiogram import __main__ as aiogram_core
from aiogram import Bot, Dispatcher, types, executor, md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, CommandHelp, Text
from collections import deque

from config import BOT_TOKEN
from databases import cache, cache_time
from states import HeadSearch
from handlers import search_hh, app, messages
from keyboards import get_keyboard


bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
search_history = deque(maxlen=3)


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
        "Поиск вакансии в телеграм каналах - /tg_search (вы получите файл с вакансиями) \n"
        "Версия бота /version \n"
    )

@dp.message_handler(commands=["settings"])
async def message_settings(message: types.Message):
    pass
    # параметры для поиска?
    # регион + 

@dp.message_handler(commands=["version"])
async def cmd_version(message: types.Message):
    bot_version = md.quote_html(str(aiogram_core.SysInfo()))
    await message.reply(
        f"My Engine: {bot_version}")


@dp.message_handler(state='*', commands=["cancel"])
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply("Отменено", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Введите мне новую команду! /help")


@dp.message_handler(commands=["hh_search"], state=None)
async def hh_search(message: types.Message):
    keyboard = await get_keyboard(search_history)
    await HeadSearch.waiting_for_vacancy.set()
    await message.answer(
        "Введите название вакансии или выберите из истории поиска",
        reply_markup=keyboard
    )


@dp.message_handler(state=HeadSearch.waiting_for_vacancy)
async def new_hh_search(message: types.Message, state:FSMContext):
    search_for = message.text
    search_results = await search_hh(search_for)
    search_history.append(search_for)
    keyboard = await get_keyboard(search_history)
    await message.answer(search_results)
    await message.answer(
        "Вы можете продолжить поиск по другой вакансии \n"
        "Или отменить его через /cancel",
        reply_markup=keyboard
    )

@dp.message_handler(commands=["tg_search"], state=None)
async def tg_search(message: types.Message):
    loop = asyncio.get_running_loop()
    await loop.create_task(messages.main())
    document = types.InputFile("вакансии.txt")
    await message.answer_document(document)
    await message.answer(
        "Python junior вакансии в телеграм каналах"
    )
