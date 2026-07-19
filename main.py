import asyncio
import logging
import os
from aiohttp import web

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Берем токен из переменных окружения Railway. Если его там нет, берем запасной (твой)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8617942287:AAG4J2qYhw6DvDiHMs7bKaz6sjKvpM5brko")
SITE_URL = "https://rho-dearie.vercel.app/"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Внимание. Установлено защищённое соединение с Министерством Дружбы...")
    await asyncio.sleep(1.5)

    await message.answer("Загружаю досье получателя... 📂")
    await asyncio.sleep(1.5)

    await message.answer("Комиссия завершила рассмотрение. Документ готов к вручению.")
    await asyncio.sleep(1)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📜 Открыть указ", web_app=WebAppInfo(url=SITE_URL))]
    ])
    await message.answer("Нажми, чтобы ознакомиться с официальным документом:", reply_markup=keyboard)

# Костыль для Railway: пустой веб-сервер, который просто «слушает» порт, чтобы Railway не выключал бота
async def handle(request):
    return web.Response(text="Bot is running!")

async def start_webserver():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # Railway автоматически передает порт в переменную окружения PORT
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

async def main():
    # Запускаем веб-сервер для Railway в фоновом режиме
    asyncio.create_task(start_webserver())
    # Запускаем самого бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
