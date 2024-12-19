from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from api_token import api_token

api = api_token
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start_command(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью')
    await message.answer('Чтобы я помог тебе рассчитать суточную норму калорий,'
                         'введи слово "Calories" и следуй инструкции')



@dp.message_handler(text='Calories')
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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
