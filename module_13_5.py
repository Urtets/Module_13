from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import asyncio
from api_token import api_token

api = api_token
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup([[KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')]], resize_keyboard=True)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет, {message["from"]["first_name"]}!'
                         f'Я бот, помогающий твоему здоровью. '
                         f'Выбери одну из кнопок: ', reply_markup=kb)



@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Информация о боте')


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer("Введите свой возраст")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    weight = int(data['weight'])
    growth = int(data['growth'])
    print(age, weight, growth)
    result = (10 * weight) + (6.25 * growth) - (5 * age) + 5
    await message.answer(f"Ваша норма калорий: {result} в день")
    await state.finish()


@dp.message_handler()
async def any_text(message):
    await message.answer(f'Добрый день, {message["from"]["first_name"]}!')
    await message.answer(f'Чтобы начать пользоваться услугами бота, пожалуйста, '
                         f'введите слово "/start"')


if __name__ == '__main__':
    executor.start_polling(dp)