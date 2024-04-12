from aiogram.fsm.state import StatesGroup, State


class AddAplicationState(StatesGroup):
    Platform = State()
    Name = State()
    Url = State()
    Bundle = State()
    Image = State()
    Geo = State()
    Source = State()
    Desc = State()
    PreView = State()
