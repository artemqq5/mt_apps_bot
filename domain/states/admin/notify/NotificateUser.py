from aiogram.fsm.state import StatesGroup, State


class NotificateUserState(StatesGroup):
    Category = State()
    Message = State()
    Media = State()
    ButtonText = State()
    ButtonUrl = State()
    Preview = State()
