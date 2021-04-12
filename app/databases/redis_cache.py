import asyncio

from aiocache import caches, Cache
from aiocache.serializers import PickleSerializer


cache = Cache(Cache.REDIS, endpoint="127.0.0.1", port=6379, namespace="cache_main", serializer=PickleSerializer())
cache_time = 86400
