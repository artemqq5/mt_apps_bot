from aiogram.fsm.state import StatesGroup, State


class CreateTeamState(StatesGroup):
    TeamName = State()
