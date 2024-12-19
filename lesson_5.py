from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
from api_token import api_token

api = api_token
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Начало')
kb.add(button)
kb.add(button2)


@dp.message_handler(commands='start')
async def start(message):
    await message.answer("Привет!", reply_markup=kb)
    bot = Bot.get_current()
    user = types.User.get_current().username
    print(bot,' - bot\n', user, ' - user')

@dp.message_handler(text = 'Информация')
async def inform(message):
    await message.answer('Информация о боте')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)