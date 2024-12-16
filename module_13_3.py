from aiogram import Bot, Dispatcher, types, executor
import asyncio
from api_token import api_token

api = api_token
bot = Bot(token=api)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message):
    user_name = message["from"]['first_name']
    print("Попал в СТАРТ")
    await message.answer(f'Привет, {user_name}! Я бот, помогающий твоему здоровью.')

@dp.message_handler()
async def all_messages(message):
    user_name = message["from"]['first_name']
    print("Попал в общие сообщения")
    await message.answer(f'{user_name}, введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)