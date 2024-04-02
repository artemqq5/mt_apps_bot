from aiogram.fsm.state import StatesGroup, State


class AccessManagmentState(StatesGroup):
    DeleteAccess = State()
    ChangeStateAccess = State()
