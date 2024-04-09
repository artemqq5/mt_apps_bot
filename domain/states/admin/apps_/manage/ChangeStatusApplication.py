from aiogram.fsm.state import StatesGroup, State


class ChangeStatusApplicationState(StatesGroup):
    status = State()
