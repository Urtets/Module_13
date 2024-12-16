from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
import logging





api = "7296819356:AAF2e9KDBv_6sfVLWeBdLKmZeVGcpXJKUN8"
bot = Bot(token=api)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


@dp.message()
async def all_mrssage(message):
    print("Мы получили сообщение")
    print(message)

@dp.message()
async def message(message):
    print("Urban message")


if __name__ == '__main__':
    asyncio.run(main())