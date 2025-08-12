from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from random import randint
from os import getenv
from dotenv import load_dotenv

from bot.states.quiz_states import Quiz
from bot.data.questions import questions, good_answers, bad_answers, final_vars
from bot.keyboards.quiz_kb import generate_keyboard
from bot.db.crud import add_result, get_result
from bot.create_bot import bot

load_dotenv()
ADMIN_ID = getenv("ADMIN_ID")
quiz_router = Router()

@quiz_router.callback_query(F.data == 'Да')
async def start_quiz_handler(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print(data.get("completed"))
    if data.get("completed"):

        await callback.message.answer(text="Вы уже прошли тест!")
        return

    await state.set_state(Quiz.question)
    await state.update_data(current_question=0, correct_answers=0)
    await callback.message.answer(text=f"Супер! Тогда начнем.\n"
                                 f"Время прохождения: 3-5 минут.\n"
                                 f"Выбирайте из предложенных кнопок, поскольку текст с обычной клавиатуры не воспринимается тестом.\n")
    await send_question(callback.message, state)

async def send_question(message: types.Message | types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    idx = data.get("current_question", 0)
    question = questions[idx]
    await message.answer(
        text=question['text'],
        reply_markup=generate_keyboard(question['options'])
    )

@quiz_router.callback_query(Quiz.question)
async def handle_answer(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    idx = data.get("current_question", 0)
    correct = data.get("correct_answers", 0)

    user_answer = callback.data
    question = questions[idx]

    if user_answer == question["correct"]:
        correct += 1
        choice = randint(0, 3)
        await callback.message.answer(good_answers[choice])
    else:
        choice = randint(0, 4)
        await callback.message.answer(bad_answers[choice] + f"\n\nПравильный ответ: {question['correct']}")

    idx += 1
    if idx == len(questions):
        await state.update_data(user_id=callback.from_user.id,
                                nickname=callback.from_user.username,
                                result=correct)
        await handle_end(callback=callback, correct=correct)
        await state.set_state(Quiz.hard_question)

    else:
        await state.update_data(current_question=idx, correct_answers=correct)
        await send_question(callback.message, state)

async def handle_end(callback: types.CallbackQuery, correct: int) -> None:
    if correct in [0, 1, 2]:
        first = "Вы в начале пути, но это будет классное путешествие!\n\n"
        level = "Вы на начальном уровне владения английским языком.\n"
    elif correct in [3, 4]:
        first = "Вы на правильном пути! Так держать)\n\n"
        level = "Вы на среднем уровне или приближаетесь к нему.\n"
    else:
        first = "Вы проделали большую работу!\n\n"
        level = "Ваш уровень средний или выше среднего\n"

    if correct in [0, 5, 6, 7, 8, 9, 10]:
        end = "ов"
    elif correct == 1:
        end = ""
    else:
        end = "а"


    name = callback.from_user.full_name or callback.from_user.username

    await callback.message.answer(
        text=(
            first + f"Ваш результат: {correct} балл{end}. " + level + "\nПримечание: тест показывает только знание грамматики. Для определения уровня говорения и понимания на слух нужно устное тестирование с преподавателем."
        )
    )
    await callback.message.answer(
        text=(
            f"{name}, скажите, что сложнее всего дается Вам?"
        ),
        reply_markup=generate_keyboard(final_vars)
    )

@quiz_router.callback_query(Quiz.hard_question)
async def handle_hard_answer(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data.get("user_id")
    nickname = data.get("nickname")
    result = data.get("result")
    hard = callback.data
    name = callback.from_user.full_name
    await add_result(user_id=user_id, nickname=nickname, result=result, hard=hard)

    await callback.message.answer(text=(
        f"{name}, понял Вас.\n\n"
        f"Хотите узнать как преодолеть эти трудности?\n\n"
        f"✍️ Записывайтесь на бесплатный урок.\n"
        f"✔️Определим Ваш текущий уровень английского без всяких тестов.\n"
        f"✔️Построим четкий план действий для достижения Вашей цели.\n"
        f"🎁 Получите подарок — Топ 25 ресурсов для языковой практики.\n"
    ),
    reply_markup=generate_keyboard(["Записаться"]))

    await state.clear()


@quiz_router.callback_query(F.data == "Записаться")
async def send_info(callback: types.CallbackQuery):
    link = "@" + callback.from_user.username
    user_id = callback.from_user.id
    await callback.message.answer(text="Я свяжусь с Вами в ближайшее время!")
    info = await get_result(user_id=user_id)

    await bot.send_message(chat_id=ADMIN_ID, text=f"{link} хочет записаться на пробное занятие.\n"
                           f"Результат: {info['result']}.\nСамое сложное: {info['hard']}")