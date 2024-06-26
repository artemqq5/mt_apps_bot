from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.repositoryDB.AccessRepository import AccessRepository
from data.repositoryDB.TeamRepository import TeamRepository
from domain.states.admin.team_.TeamManagment import TeamManagmentState
from presenter.keyboards.admin_keyboard import kb_delete, kb_teams

router = Router()


@router.callback_query(F.data.contains("DELETETEAM"))
async def callback_team_delete(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    team_id = callback.data.split("*CALLBACK*")[0]
    team = TeamRepository().get_team_by_id(team_id)

    if not team:
        return

    await state.set_state(TeamManagmentState.DeleteTeam)

    await state.update_data(team_id=team_id)
    await state.update_data(team_name=team['team_name'])

    await callback.message.answer(i18n.WARNING_DELETE_TEAM(team_name=team['team_name']), reply_markup=kb_delete)


@router.message(TeamManagmentState.DeleteTeam, F.text == L.APPROVE_DELETE())
async def approve_delete_team(message: types.Message, state: FSMContext, i18n: I18nContext):
    try:
        data = await state.get_data()

        if not TeamRepository().delete_team(data['team_id']):
            raise Exception

        AccessRepository().delete_all_access_by_team_id(data['team_id'])

        await state.clear()
        await message.answer(i18n.SUCCESSFUL_DELETE_TEAM(team_name=data['team_name']), reply_markup=kb_teams)
    except Exception as e:
        print(f"approve_delete_team: {e}")
        await state.clear()
        await message.answer(i18n.ERROR_DELETE_TEAM(error=str(e)), reply_markup=kb_teams)

