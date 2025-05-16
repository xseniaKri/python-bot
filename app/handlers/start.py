from aiogram import F, Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext



start_router = Router()



@start_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(
        f"{html.bold(message.from_user.full_name)}, привет! Хочешь быстро узнать свой уровень английского?")




@start_router.message(F.text == 'нет')
async def no_handler(message: Message) -> None:
    try:
            await message.answer(f"А чего пришел тогда?")
    except TypeError:
        await message.answer("Наташ, мы все сломали. Вообще все.")





