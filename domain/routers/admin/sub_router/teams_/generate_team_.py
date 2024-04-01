import uuid

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from data.constants.buttons_text import APPROVE_GENERATE_TEAM
from data.constants.just_message import SUCCESSFUL_GENERATE_TEAM, ERROR_GENERATE_TEAM, \
    WARNING_GENERATE_KEY_TEAM
from data.repository.AccessRepository import AccessRepository
from data.repository.TeamRepository import TeamRepository
from domain.states.team_.TeamManagment import TeamManagmentState
from presenter.keyboards.admin_keyboard import kb_teams, kb_team_generate

router = Router()


@router.callback_query(F.data.contains("GENERATEJOINKEY"))
async def callback_team_generate(callback: CallbackQuery, state: FSMContext):
    team_id = callback.data.split("*CALLBACK*")[0]

    await state.set_state(TeamManagmentState.GenerateJoinKey)

    team = TeamRepository().get_team_by_id(team_id)

    if not team:
        return

    await state.update_data(team_id=team_id)
    await state.update_data(team_name=team['team_name'])
    await state.update_data(team_uuid=team['uuid'])

    await callback.message.answer(WARNING_GENERATE_KEY_TEAM.format(team['team_name']),
                                  reply_markup=kb_team_generate.as_markup())


@router.message(TeamManagmentState.GenerateJoinKey, F.text == APPROVE_GENERATE_TEAM)
async def approve_generate_team(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        access_uuid = uuid.uuid4()
        if not AccessRepository().generate_accesss(access_uuid, data['team_uuid'], data['team_id'], data['team_name']):
            raise Exception

        await state.clear()
        await message.answer(SUCCESSFUL_GENERATE_TEAM.format(data['team_name'], access_uuid),
                             reply_markup=kb_teams.as_markup())
    except Exception as e:
        print(f"approve_generate_team: {e}")
        await state.clear()
        await message.answer(ERROR_GENERATE_TEAM.format(e), reply_markup=kb_teams.as_markup())
