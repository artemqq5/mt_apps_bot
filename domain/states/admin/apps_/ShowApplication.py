from aiogram.fsm.state import StatesGroup, State


class ShowApplicationState(StatesGroup):
    platform = State()

