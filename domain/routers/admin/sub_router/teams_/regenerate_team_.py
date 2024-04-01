import uuid

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from data.constants.buttons_text import APPROVE_REGENERATE_TEAM
from data.constants.just_message import SUCCESSFUL_DELETE_TEAM, \
    ERROR_DELETE_TEAM, WARNING_REGENERATE_KEY_TEAM, SUCCESSFUL_REGENERATE_TEAM, ERROR_REGENERATE_TEAM
from data.repository.TeamRepository import TeamRepository
from domain.states.team_.TeamManagment import TeamManagmentState
from presenter.keyboards.admin_keyboard import kb_team_delete, kb_teams, kb_team_regenerate

router = Router()


@router.callback_query(F.data.contains("REGENERATEJOINKEY"))
async def callback_team_regenerate(callback: CallbackQuery, state: FSMContext):
    team_id = callback.data.split("*CALLBACK*")[0]

    await state.set_state(TeamManagmentState.RegenerateJoinKey)

    team = TeamRepository().get_team_by_id(team_id)

    if not team:
        return

    await state.update_data(team_id=team_id)
    await state.update_data(team_name=team['team_name'])

    await callback.message.answer(WARNING_REGENERATE_KEY_TEAM.format(team['team_name']),
                                  reply_markup=kb_team_regenerate.as_markup())


@router.message(TeamManagmentState.RegenerateJoinKey, F.text == APPROVE_REGENERATE_TEAM)
async def approve_regenerate_team(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        team_uuid = uuid.uuid4()
        if not TeamRepository().update_team_key(team_uuid, data['team_id']):
            raise Exception

        await state.clear()
        await message.answer(SUCCESSFUL_REGENERATE_TEAM.format(data['team_name'], team_uuid), reply_markup=kb_teams.as_markup())
    except Exception as e:
        print(f"approve_regenerate_team: {e}")
        await state.clear()
        await message.answer(ERROR_REGENERATE_TEAM.format(e), reply_markup=kb_teams.as_markup())
