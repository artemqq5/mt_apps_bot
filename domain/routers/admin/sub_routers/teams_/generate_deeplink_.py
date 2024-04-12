import uuid

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from config import LINK_TO_BOT
from data.repository.AccessRepository import AccessRepository
from data.repository.TeamRepository import TeamRepository
from domain.states.admin.team_.TeamManagment import TeamManagmentState
from presenter.keyboards.admin_keyboard import kb_teams, kb_team_generate

router = Router()


@router.callback_query(F.data.contains("GENERATEJOINKEY"))
async def callback_team_generate(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    team_id = callback.data.split("*CALLBACK*")[0]
    team = TeamRepository().get_team_by_id(team_id)

    if not team:
        return

    await state.set_state(TeamManagmentState.GenerateJoinKey)

    await state.update_data(team_id=team_id)
    await state.update_data(team_name=team['team_name'])
    await state.update_data(team_uuid=team['uuid'])

    await callback.message.answer(i18n.WARNING_GENERATE_KEY_TEAM(team_name=team['team_name']),
                                  reply_markup=kb_team_generate)


@router.message(TeamManagmentState.GenerateJoinKey, F.text == L.APPROVE_GENERATE_TEAM())
async def approve_generate_team(message: types.Message, state: FSMContext, i18n: I18nContext):
    try:
        data = await state.get_data()
        access_uuid = uuid.uuid4()
        if not AccessRepository().generate_accesss(access_uuid, data['team_uuid'], data['team_id'], data['team_name']):
            raise Exception

        await state.clear()
        await message.answer(i18n.SUCCESSFUL_GENERATE_TEAM(team_name=data['team_name'],
                                                           deeplink=f"{LINK_TO_BOT}?start={access_uuid}"),
                             reply_markup=kb_teams)
    except Exception as e:
        print(f"approve_generate_team: {e}")
        await state.clear()
        await message.answer(i18n.ERROR_GENERATE_TEAM(error=str(e)), reply_markup=kb_teams)
