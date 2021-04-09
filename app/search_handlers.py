import asyncio
import aiohttp


URL = "https://api.hh.ru/vacancies"

async def search_hh(search_for):
    async with aiohttp.ClientSession() as session:
        params = {"text": search_for}
        async with session.get(URL, params=params) as resp:
            # vacancy = resp.text.get("items")[0]
           #  vacancies = {} # список со всеми вакансиями за последние 3 дня
            return search_for
