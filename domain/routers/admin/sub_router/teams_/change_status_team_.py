
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from data.constants.access import TEAM_STATUS_LIST
from data.constants.just_message import CHOICE_NEW_STATUS_TEAM, PRESS_BACK_TO_TEAM_MENU, SUCCESSFUL_CHANGE_STATUS_TEAM, \
    ERROR_CHANGE_STATUS_TEAM
from data.repository.TeamRepository import TeamRepository
from domain.states.team_.TeamManagment import TeamManagmentState
from presenter.keyboards.admin_keyboard import kb_teams, kb_team_change_status, kb_team_managment_help

router = Router()


@router.callback_query(F.data.contains("CHANGESTATUSTEAM"))
async def callback_team_change_status(callback: CallbackQuery, state: FSMContext):
    team_id = callback.data.split("*CALLBACK*")[0]
    team = TeamRepository().get_team_by_id(team_id)

    if not team:
        return

    await state.set_state(TeamManagmentState.ChangeStatus)

    await state.update_data(team_id=team_id)
    await state.update_data(team_name=team['team_name'])

    await callback.message.answer(CHOICE_NEW_STATUS_TEAM.format(team['team_name']),
                                  reply_markup=kb_team_change_status.as_markup())
    await callback.message.answer(PRESS_BACK_TO_TEAM_MENU, reply_markup=kb_team_managment_help.as_markup())


@router.callback_query(TeamManagmentState.ChangeStatus, F.data.in_(TEAM_STATUS_LIST))
async def callback_team_choice_status(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()

        if not TeamRepository().update_team_status(callback.data, data['team_id']):
            raise Exception

        await state.clear()
        await callback.message.answer(SUCCESSFUL_CHANGE_STATUS_TEAM.format(data['team_name'], callback.data), reply_markup=kb_teams.as_markup())
    except Exception as e:
        print(f"callback_team_choice_status: {e}")
        await state.clear()
        await callback.message.answer(ERROR_CHANGE_STATUS_TEAM.format(e), reply_markup=kb_teams.as_markup())


