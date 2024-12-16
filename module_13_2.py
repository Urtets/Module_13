from aiogram import Bot, Dispatcher, types, executor
import asyncio
from api_token import api_token

api = api_token
bot = Bot(token=api)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')
    print(message["from"]['first_name'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)