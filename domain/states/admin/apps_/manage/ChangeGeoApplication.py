from aiogram.fsm.state import StatesGroup, State


class ChangeGeoApplicationState(StatesGroup):
    geo = State()
