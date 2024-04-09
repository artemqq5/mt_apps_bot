from aiogram.fsm.state import StatesGroup, State


class UnbanUserState(StatesGroup):
    UserData = State()
