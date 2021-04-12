import asyncio
import aiohttp
from aiogram import md
from aiocache import Cache, caches
from databases import cache

#caches.set_config({
    #'default': {
        #'cache': "aiocache.RedisCache",
        ##'endpoint': "127.0.0.1",
        #'port': 6379,
        #'timeout': 1,
        #'serializer': {
        #    'class': "aiocache.serializers.JsonSerializer"
       # },
   ## }
# })


URL = "https://api.hh.ru/vacancies"

async def search_hh(search_for):
    if not await cache.get(search_for):
        async with aiohttp.ClientSession() as session:
            params = {"text": search_for}
            async with session.get(URL, params=params) as resp:
                data = await resp.json()
                vacancies = data["items"]
                search_results = {} # ищет не только в мск, за последний день
                for vacancy in vacancies:
                    search_results[vacancy.get("name")] = vacancy.get("alternate_url")
                search_results_string = "\n".join(f'{k}: {v}' for k,v in search_results.items())
                await cache.set(search_for, search_results_string, ttl=300)
                return search_results_string
    else:
        return await cache.get(search_for)


async def search_tg():
    pass
