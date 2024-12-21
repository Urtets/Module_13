from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

from api_token import api_token, api_token2

api = api_token
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = types.InlineKeyboardMarkup(row_width=3)
button = types.InlineKeyboardButton(text='Информация', callback_data='Info')
kb.add(button)

start_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Info')], [KeyboardButton(text='shop'), KeyboardButton(text='Donate')]],
    resize_keyboard=True
)


@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer("Рады вас видеть!", reply_markup=kb)


@dp.callback_query_handler(text='Info')
async def infor(call: CallbackQuery):
    print("Попал в callback")
    await call.message.answer("Информация о боте")
    await call.answer()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
