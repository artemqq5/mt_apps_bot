from aiogram.fsm.state import StatesGroup, State


class TeamManagmentState(StatesGroup):
    DeleteTeam = State()
    ChangeStatus = State()
    RegenerateJoinKey = State()
