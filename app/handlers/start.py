from aiogram import F, Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.keyboards.quiz_kb import generate_keyboard



start_router = Router()



@start_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(text=f"{html.bold(message.from_user.full_name)}, приветствую! Хотите быстро узнать свой уровень английского?",
                         reply_markup=generate_keyboard(['Да', 'Нет']))




@start_router.message(F.data == "Нет")
async def no_handler(message: Message) -> None:
    try:
        await message.answer(f"А чего пришел тогда?")
    except TypeError:
        await message.answer("Наташ, мы все сломали. Вообще все.")





