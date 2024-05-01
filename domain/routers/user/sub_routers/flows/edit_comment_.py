from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.repositoryDB.FlowRepository import FlowRepository
from domain.states.user.flow_.EditCommentFlow import EditCommentFlowState
from presenter.keyboards._keyboard import kb_skip, kb_cancel
from presenter.keyboards.user_keyboard import EditFlowApp, EditFlowComment, kb_flow_edit, kb_flow_back_edit

router = Router()


@router.callback_query(EditFlowComment.filter())
async def edit_flow_comment(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    id_ = callback.data.split(":")[1]
    flow = FlowRepository().get_flow(id_)

    if not flow:
        return  # потока не існує

    await state.set_state(EditCommentFlowState.NewComment)
    await state.update_data(flow_id=id_)
    await callback.message.answer(i18n.FLOW.EDIT.NEW_COMMENT(), reply_markup=kb_cancel)


@router.message(EditCommentFlowState.NewComment)
async def set_new_comment(message: Message, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    await state.clear()

    if not FlowRepository().get_flow(data['flow_id']):
        return  # Потока не інує

    if not FlowRepository().update_comment_flow(data['flow_id'], message.text):
        await message.answer(i18n.FLOW.EDIT.NEW_COMMENT_FAIL(), reply_markup=kb_flow_back_edit(data['flow_id']))
        return

    await message.answer(i18n.FLOW.EDIT.NEW_COMMENT_SUCCESS(), reply_markup=kb_flow_back_edit(data['flow_id']))
