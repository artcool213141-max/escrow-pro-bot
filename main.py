import asyncio
import os
from aiogram import Bot, Dispatcher
from handlers import router # нужно будет создать папку handlers и файл __init__.py

async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
