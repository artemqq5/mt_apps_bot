from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.constants.access import TEAM_STATUS_LIST
from data.repository.TeamRepository import TeamRepository
from domain.states.team_.TeamManagment import TeamManagmentState
from presenter.keyboards.admin_keyboard import kb_teams, kb_team_change_status

router = Router()


@router.callback_query(F.data.contains("CHANGESTATUSTEAM"))
async def callback_team_change_status(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    team_id = callback.data.split("*CALLBACK*")[0]
    team = TeamRepository().get_team_by_id(team_id)

    if not team:
        return

    await state.set_state(TeamManagmentState.ChangeStatus)

    await state.update_data(team_id=team_id)
    await state.update_data(team_name=team['team_name'])

    await callback.message.answer(i18n.CHOICE_NEW_STATUS_TEAM(team_name=team['team_name']),
                                  reply_markup=kb_team_change_status)


@router.callback_query(TeamManagmentState.ChangeStatus, F.data.in_(TEAM_STATUS_LIST))
async def callback_team_choice_status(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    try:
        data = await state.get_data()

        if not TeamRepository().update_team_status(callback.data, data['team_id']):
            raise Exception

        await state.clear()
        await callback.message.answer(
            i18n.SUCCESSFUL_CHANGE_STATUS_TEAM(team_name=data['team_name'], status=callback.data),
            reply_markup=kb_teams)
    except Exception as e:
        print(f"callback_team_choice_status: {e}")
        await state.clear()
        await callback.message.answer(i18n.ERROR_CHANGE_STATUS_TEAM(error=str(e)), reply_markup=kb_teams)
