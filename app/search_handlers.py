import asyncio
import aiohttp
from aiogram import md


URL = "https://api.hh.ru/vacancies"
# search_for = "python junior"

async def search_hh(search_for):
    async with aiohttp.ClientSession() as session:
        params = {"text": search_for}
        async with session.get(URL, params=params) as resp:
            # vacancy = resp.text.get("items")[0]
           #  vacancies = {} # список со всеми вакансиями за последние 3 дня
            data = await resp.json()
            vacancies = data["items"]
            search_results = {}
            for vacancy in vacancies:
                search_results[vacancy.get("name")] = vacancy.get("alternate_url")
            return "\n".join(f'{k}: {v}' for k,v in search_results.items())


#loop = asyncio.get_event_loop()
# loop.run_until_complete(search_hh())

