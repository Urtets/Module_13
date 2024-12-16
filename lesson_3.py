from aiogram import Bot, Dispatcher, types, executor
import asyncio
from api_token import api_token
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = api_token
bot = Bot(token=api)
dp = Dispatcher(bot)


@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message):
    print("Urban message")
    await message.answer("Urban message")


@dp.message_handler(commands=['start'])
async def start_message(message):
    print("Start message")
    await message.answer("Welcome")


@dp.message_handler()
async def all_message(message):
    print("Мы получили сообщение")
    await message.answer(message.text.upper())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
