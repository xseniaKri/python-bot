import asyncio
import logging
import sys


from app.handlers.start import start_router
from app.handlers.quiz import quiz_router
from create_bot import bot, dp




async def main() -> None:
    dp.include_router(start_router)
    dp.include_router(quiz_router)
    await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())