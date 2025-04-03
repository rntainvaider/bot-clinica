import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN_URL
from handlers.start_handler import router_start

bot = Bot(token=TOKEN_URL)
dp = Dispatcher()

dp.include_router(router_start)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
