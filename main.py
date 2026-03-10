import os
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.webhook.urls import SecretTelegramCallbackCheck
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

# Данные из .env
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_HOST = "https://your-domain.com" # Твой домен или IP с SSL
WEBHOOK_PATH = f"/webhook/{TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

async def on_startup(bot: Bot):
    # Устанавливаем вебхук в Telegram
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
    print(f"Вебхук установлен на: {WEBHOOK_URL}")

def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router) # Твои хендлеры
    
    dp.startup.register(on_startup)

    app = web.Application()
    
    # Настраиваем обработчик вебхуков
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    setup_application(app, dp, bot=bot)
    
    web.run_app(app, host="0.0.0.0", port=8080) # Порт, который слушает Docker

if __name__ == "__main__":
    main()
