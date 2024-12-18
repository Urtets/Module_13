from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from api_token import api_token
from aiogram.dispatcher import FSMContext
import asyncio

api = api_token
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    address = State()


@dp.message_handler(text = "Заказать")
async def buy(message):
    await message.answer("Отправь нам свой адрес, пожалуйста")
    await UserState.address.set()


@dp.message_handler(state=UserState.address)
async def fsm_handler(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer(f"Доставка будет отправлена на {data['first']}")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)