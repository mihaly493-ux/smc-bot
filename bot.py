import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from config import BOT_TOKEN
from analysis import run_smc_analysis

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет! Я бот Smart Money Concepts.\n\n"
        "Команды:\n"
        "/analyze — выполнить анализ BTC\n"
        "/help — помощь"
    )

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer(
        "Команды:\n"
        "/analyze — выполнить анализ BTC"
    )

@dp.message(Command("analyze"))
async def analyze(message: types.Message):
    await message.answer("Выполняю анализ рынка...")

    analysis = run_smc_analysis()

    await message.answer(analysis)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
