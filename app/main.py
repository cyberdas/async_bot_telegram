from aiogram import executor
from bot import dp
from chat_settings import dp
from middlewares import ThrottlingMiddleware


async def on_startup(dp):
    dp.middleware.setup(ThrottlingMiddleware())
    #db.setUp(dp) create database
    

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
