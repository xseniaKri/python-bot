import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.methods import send_video

from bot_logic import cat

load_dotenv()
TOKEN = getenv('BOT_TOKEN')

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"{html.bold(message.from_user.full_name)}, спасибо за подписку! Как у тебя сейчас дела с английским?")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.answer(f"Слышу!")
        await bot.send_video(chat_id=message.chat.id, video=cat)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls


    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())