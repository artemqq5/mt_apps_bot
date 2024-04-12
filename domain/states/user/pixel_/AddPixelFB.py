from aiogram.fsm.state import StatesGroup, State


class AddPixelFBState(StatesGroup):
    PixelId = State()
    TokenEAAG = State()
    