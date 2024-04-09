from aiogram.fsm.state import StatesGroup, State


class DeleteApplicationState(StatesGroup):
    delete = State()
