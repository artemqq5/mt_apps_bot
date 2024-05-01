from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositoryDB.FlowRepository import FlowRepository
from data.repositoryDB.PixelRepository import PixelRepository
from data.repositoryKeitaro.KeitaroPixelRepository import KeitaroPixelRepository
from domain.states.user.flow_.EditPixelFlow import EditPixelFlowState
from presenter.keyboards.user_keyboard import EditFlowPixel, pixel_edit_list, kb_pixel_menu, PixelEditList, \
    kb_flow_back_edit

router = Router()


@router.callback_query(EditFlowPixel.filter())
async def edit_flow_pixel(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    id_ = callback.data.split(":")[1]
    flow = FlowRepository().get_flow(id_)

    if not flow:
        return  # потока не існує

    pixels = PixelRepository().get_all_pixels(callback.from_user.id)

    if not pixels:
        await callback.message.answer(i18n.USER.HAVENT_ANY_PIXEL(), reply_markup=kb_pixel_menu)
        return

    await state.set_state(EditPixelFlowState.NewPixel)
    await state.update_data(flow_id=id_)

    await callback.message.answer(i18n.FLOW.EDIT.NEW_PIXEL(), reply_markup=pixel_edit_list(pixels))


@router.callback_query(PixelEditList.filter(), EditPixelFlowState.NewPixel)
async def choice_new_pixel(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    id_ = callback.data.split(":")[1]
    pixel = PixelRepository().get_pixel(id_)
    data = await state.get_data()
    flow = FlowRepository().get_flow(data['flow_id'])

    if not pixel or not flow:
        return  # потока або пікселя не існує

    await state.clear()

    if not KeitaroPixelRepository().update_pixel(flow, pixel['pixel_fb'], pixel['token_fb']):
        await callback.message.answer(i18n.FLOW.EDIT.NEW_PIXEL_FAIL(error="keitaro"), reply_markup=kb_flow_back_edit(data['flow_id']))
        return

    if not FlowRepository().update_pixel_flow(data['flow_id'], pixel['pixel_fb'], pixel['token_fb']):
        await callback.message.answer(i18n.FLOW.EDIT.NEW_PIXEL_FAIL(error="db"), reply_markup=kb_flow_back_edit(data['flow_id']))
        return

    await callback.message.answer(i18n.FLOW.EDIT.NEW_PIXEL_SUCCESS(), reply_markup=kb_flow_back_edit(data['flow_id']))
