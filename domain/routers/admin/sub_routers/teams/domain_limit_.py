from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.repositoryDB.TeamRepository import TeamRepository
from domain.states.admin.team_.DomainLimit import DomainLimitState
from presenter.keyboards.admin_keyboard import kb_domain_limit, kb_teams

router = Router()


@router.callback_query(F.data.contains("DOMAINLIMIT"))
async def callback_team_domain_limit(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    team_id = callback.data.split("*CALLBACK*")[0]
    team = TeamRepository().get_team_by_id(team_id)

    if not team:
        return

    await state.set_state(DomainLimitState.CountDomain)
    await state.update_data(team_id=team_id)

    await callback.message.answer(i18n.NEW_DOMAIN_LIMIT(), reply_markup=kb_domain_limit)


@router.message(DomainLimitState.CountDomain)
async def limit_domain(message: Message, state: FSMContext, i18n: I18nContext):
    if message.text == i18n.CANCEL_DOAMIN_LIMIT():
        await state.update_data(limit=999)

    if message.text.isdigit():
        await state.update_data(limit=int(message.text))

    data = await state.get_data()
    await state.clear()

    if not TeamRepository().update_team_doamin_limit(data['team_id'], data['limit']):
        await message.answer(i18n.SET_LIMIT_FAIL(), reply_markup=kb_teams)
        return

    await message.answer(i18n.SET_LIMIT_SUCCESS(limit=data['limit']), reply_markup=kb_teams)
