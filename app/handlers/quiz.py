from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from app.states.quiz_states import Quiz
from app.data.questions import questions
from app.keyboards.quiz_kb import generate_keyboard

quiz_router = Router()

@quiz_router.message()
async def start_quiz_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    print(data.get("completed"))
    if data.get("completed"):

        await message.answer(text="Вы уже прошли тест!")
        return

    await state.set_state(Quiz.question)
    await state.update_data(current_question=0, correct_answers=0)
    await message.answer(text=f"Супер! Тогда начнем.\n"
                                 f"Время прохождения: 3-5 минут.\n"
                                 f"Выбирайте из предложенных кнопок, поскольку текст с обычной клавиатуры не воспринимается тестом.\n")
    await send_question(message, state)

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
        await callback.message.answer("Правильно!")
    else:
        await callback.message.answer("Неправильно!")

    idx += 1
    if idx == len(questions):
        await handle_end(callback=callback, correct=correct)
        await state.clear()
        await state.update_data(completed=True)

    else:
        await state.update_data(current_question=idx, correct_answers=correct)
        await send_question(callback.message, state)

async def handle_end(callback: types.CallbackQuery, correct: int) -> None:
    if correct in [0, 1, 2]:
        level = "A0"
    elif correct in [3, 4]:
        level = "A1"
    elif correct in [5, 6]:
        level = "A2"
    elif correct in [7, 8]:
        level = "B1"
    else:
        level = "B2"

    if correct in [0, 5, 6, 7, 8, 9, 10]:
        end = "ов"
    elif correct == 1:
        end = ""
    else:
        end = "а"
    await callback.message.answer(text=f"Поздравляю с прохождением теста! Вы набрали {correct} балл{end}\nВаш уровень: {level}.")

