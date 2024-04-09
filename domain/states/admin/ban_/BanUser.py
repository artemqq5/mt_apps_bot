from aiogram.fsm.state import StatesGroup, State


class BanUserState(StatesGroup):
    UserData = State()
    BanMessage = State()
