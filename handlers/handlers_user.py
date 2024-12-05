from aiogram import F, types, Router
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.inline import check_weather_inline

import aiohttp
import asyncio
import os

from dotenv import load_dotenv
load_dotenv()

weather_api = os.getenv("WEATHER_API")

router = Router()

class WeatherCity(StatesGroup):
    city = State()



@router.message(CommandStart())
async def welcome_weather_to_bot(message: types.Message) -> None:
    await message.answer(f"""Приветствую, {message.from_user.first_name}.
                        \nЯ - бот, создан для того, чтобы Вы узнали какая сейчас погода на улице!""", 
                        reply_markup=check_weather_inline)




@router.callback_query(F.data == 'input_city')
async def input_city(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(WeatherCity.city)
    await callback.message.answer("Введите город:")
    
@router.message(WeatherCity.city)
async def check_weather(message: types.Message, state: FSMContext):
    city = message.text
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={weather_api}") as response:
                data = await response.json()
                temp = int(data['main']['temp'])
                humidity = data['main']['humidity']
                description = data['weather'][0]['description']
        
        #print(data)
        await message.reply(
            f"Температура: {temp}°C\n"
            f"Влажность: {humidity}%\n"
            f"Состояние: {description}\n"
        )
    except:
        await message.answer("Город указан неверно.")
        
