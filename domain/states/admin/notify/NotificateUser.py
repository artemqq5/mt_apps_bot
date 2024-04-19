from aiogram.fsm.state import StatesGroup, State


class NotificateUserState(StatesGroup):
    Category = State()
    Message = State()
    Media = State()
    Button = State()
    Preview = State()
