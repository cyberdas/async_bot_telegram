import asyncio
import aiohttp
from aiogram import md
from aiocache import Cache, caches
from databases import cache, cache_time


request_params = {
    "Москва": "1", "Россия": "113", "Удаленная работа": "remote", "Полный день": "fullDay"
    }


URL = "https://api.hh.ru/vacancies"


async def search_hh_extended(user_data):
    vacancy = user_data.get("chosen_vacancy")
    region = user_data.get("chosen_region")
    job_type = user_data.get("chosen_type")
    key_string = vacancy + region + job_type
    if not await cache.get(key_string):
        async with aiohttp.ClientSession() as session:
            params = {"text": vacancy, "schedule": request_params.get(job_type), "area": request_params.get(region)}
            async with session.get(URL, params=params) as resp:
                data = await resp.json()
                vacancies = data["items"]
                search_results = {}
                for vacancy in vacancies:
                    search_results[vacancy.get("name")] = vacancy.get("alternate_url")
                search_results_string = "\n".join(f'{k}: {v}' for k,v in search_results.items())
                await cache.set(key_string, search_results_string, ttl=cache_time)
                return search_results_string
    else:
        return await cache.get(key_string)
