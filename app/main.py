import asyncio
import logging
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.handlers.start import start_router
from app.handlers.quiz import quiz_router
from app.create_bot import bot, dp



async def start_bot():
    dp.include_router(start_router)
    dp.include_router(quiz_router)
    await bot.delete_webhook()
    await dp.start_polling(bot)


async def main() -> None:
    await asyncio.gather(
        start_bot()
    )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())