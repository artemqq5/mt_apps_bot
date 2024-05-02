from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.constants.access import validate_user_link, MACROS
from data.repositoryDB.FlowRepository import FlowRepository
from data.repositoryKeitaro.KeitaroOfferRepository import KeitaroOfferRepository
from domain.states.user.flow_.EditOfferFlow import EditOfferFlowState
from presenter.keyboards._keyboard import kb_cancel
from presenter.keyboards.user_keyboard import EditFlowOffer, kb_flow_back_edit

router = Router()


@router.callback_query(EditFlowOffer.filter())
async def edit_flow_offer(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    id_ = callback.data.split(":")[1]
    flow = FlowRepository().get_flow(id_)

    if not flow:
        return  # потока не існує

    await state.set_state(EditOfferFlowState.NewOffer)
    await state.update_data(flow_id=id_)

    await callback.message.answer(i18n.FLOW.EDIT.NEW_OFFER(), reply_markup=kb_cancel)


@router.message(EditOfferFlowState.NewOffer)
async def change_offer(message: Message, state: FSMContext, i18n: I18nContext):
    # Валідуємо лінку від юзера
    if not validate_user_link(message.text):
        await message.answer(i18n.FLOW.OFFER_LINK_ERROR(subid=MACROS), reply_markup=kb_cancel)
        return

    data = await state.get_data()
    flow = FlowRepository().get_flow(data['flow_id'])

    if not flow:
        return  # потока не існує

    await state.clear()

    if not KeitaroOfferRepository().update_offer_url(flow['offer_id'], message.text):
        await message.answer(
            i18n.FLOW.EDIT.NEW_OFFER_FAIL(error="keitaro"),
            reply_markup=kb_flow_back_edit(flow['id'])
        )
        return

    if not FlowRepository().update_offer_flow(flow['id'], message.text):
        await message.answer(
            i18n.FLOW.EDIT.NEW_OFFER_FAIL(error="db"),
            reply_markup=kb_flow_back_edit(flow['id'])
        )
        return

    await message.answer(i18n.FLOW.EDIT.NEW_OFFER_SUCCESS(), reply_markup=kb_flow_back_edit(flow['id']))
