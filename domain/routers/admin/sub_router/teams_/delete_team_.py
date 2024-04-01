from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from data.constants.buttons_text import APPROVE_DELETE_TEAM
from data.constants.just_message import WARNING_DELETE_TEAM, SUCCESSFUL_DELETE_TEAM, \
    ERROR_DELETE_TEAM
from data.repository.TeamRepository import TeamRepository
from domain.states.team_.TeamManagment import TeamManagmentState
from presenter.keyboards.admin_keyboard import kb_team_delete, kb_teams

router = Router()


@router.callback_query(F.data.contains("DELETE"))
async def callback_team_delete(callback: CallbackQuery, state: FSMContext):
    team_id = callback.data.split("*CALLBACK*")[0]

    await state.set_state(TeamManagmentState.DeleteTeam)

    team = TeamRepository().get_team_by_id(team_id)

    if not team:
        return

    await state.update_data(team_id=team_id)
    await state.update_data(team_name=team['team_name'])

    await callback.message.answer(WARNING_DELETE_TEAM.format(team['team_name']), reply_markup=kb_team_delete.as_markup())


@router.message(TeamManagmentState.DeleteTeam, F.text == APPROVE_DELETE_TEAM)
async def approve_delete_team(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()

        if not TeamRepository().delete_team(data['team_id']):
            raise Exception

        await state.clear()
        await message.answer(SUCCESSFUL_DELETE_TEAM.format(data['team_name']), reply_markup=kb_teams.as_markup())
    except Exception as e:
        print(f"approve_delete_team: {e}")
        await state.clear()
        await message.answer(ERROR_DELETE_TEAM.format(e), reply_markup=kb_teams.as_markup())

