from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

check_weather_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Узнать погоду ☁️',
            callback_data="input_city",
        )
    ]
])