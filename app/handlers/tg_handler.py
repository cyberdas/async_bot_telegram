import asyncio
from aiofile import async_open
from pyrogram import Client
from typing import List

from config import api_id, api_hash


class MessagesSearch:

    def __init__(self):
        self.app = Client("my_account", api_id, api_hash)
        self.chats = ["django_jobs", "django_jobs_board", "ru_pythonjobs"]
        self.search_results = []

    async def get_chat_id(self, chat: str) -> int:
        chat = await self.app.get_chat(chat)
        return chat.id

    async def get_chat_messages(self, chat:str) -> str:
        chat_id = await self.get_chat_id(chat)
        async for message in self.app.search_messages(chat_id, "python junior", limit=3):
            self.search_results.append(message.text)

    async def write_to_file(self, search_results: List[str]):
        async with async_open("вакансии.txt", "w+") as afp:
            for item in self.search_results:
                await afp.write(item)
                await afp.write("\n----------------------------\n")

    async def main(self):
        async with self.app:
            tasks = [self.get_chat_messages(chat) for chat in self.chats]
            await asyncio.gather(*tasks)
            await self.write_to_file(self.search_results)


app = Client("my_account", api_id, api_hash)
messages = MessagesSearch()
