import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BOT_TOKEN = "ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН"       # получить у @BotFather
SITE_URL = "ВСТАВЬ_СЮДА_ССЫЛКУ_НА_САЙТ"    # см. README, как захостить бесплатно

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


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
