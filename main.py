import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from handlers.handlers_user import router


load_dotenv()

bot_token = os.getenv("BOT_TOKEN")


bot = Bot(token=bot_token)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())