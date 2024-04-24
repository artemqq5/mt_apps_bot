from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.repositoryDB.TeamRepository import TeamRepository
from domain.states.admin.notify.NotificateUser import NotificateUserState
from presenter.keyboards._keyboard import kb_cancel

router = Router()


@router.callback_query(F.data.contains("TEAMMESSAGING"))
async def callback_team_messaging(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    team_id = callback.data.split("*CALLBACK*")[0]
    team = TeamRepository().get_team_by_id(team_id)

    if not team:
        return

    await state.set_state(NotificateUserState.Message)
    await state.update_data(category=i18n.TEAM_MESSAGING())
    await state.update_data(team_id=team_id)
    await callback.message.answer(i18n.NOTIFY.MESSAGE(), reply_markup=kb_cancel)

# тут далі перенаправляється логіка на /sub_routers/notification/notify_
