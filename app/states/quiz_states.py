from aiogram.fsm.state import State, StatesGroup

class Quiz(StatesGroup):
    question = State()
    end = State()
    start = State()