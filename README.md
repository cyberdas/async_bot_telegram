## Асинхронный телеграм бот для поиска вакансии на hh и в telegram каналах
Функционал бота:
- Настройка языка, уведомлений
- Поиск по hh и tg
- Отправка файлов
- Кеширование
- Middlware
## Использованные библиотеки
- asyncio
- aiohttp
- aiogram
- aiocache
- asyncpg
- sqlalchemy
## Развернуть проект с помощью Docker
1) Клонируйте репозиторий 
```
git clone https://github.com/cyberdas/async_bot_telegram
```
2) Создайте файл .env с переменным окружения
BOT_TOKEN, API_ID, API_HASH
3) Используйте docker-compose, он автоматически установит нужные зависимости
```
docker-compose up --build
```