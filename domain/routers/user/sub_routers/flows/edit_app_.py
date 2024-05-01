from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositoryDB.AppRepository import AppRepository
from data.repositoryDB.FlowRepository import FlowRepository
from data.repositoryKeitaro.KeitaroAppRepository import KeitaroAppRepository
from domain.states.user.flow_.EditAppFlow import EditAppFlowState
from presenter.keyboards.user_keyboard import EditFlowApp, kb_flow_back_edit, app_edit_list, AppEditList

router = Router()


@router.callback_query(EditFlowApp.filter())
async def edit_flow_app(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    id_ = callback.data.split(":")[1]
    flow = FlowRepository().get_flow(id_)
    apps = AppRepository().show_apps_by_platform_for_users(i18n.IOS())

    if not flow:
        return  # потока не існує

    if not apps:
        await callback.message.answer(i18n.APP.APP_LIST_EMPTY(), reply_markup=kb_flow_back_edit(id_))
        return  # пріл немає

    await state.set_state(EditAppFlowState.NewApp)
    await state.update_data(flow_id=id_)

    await callback.message.answer(i18n.FLOW.EDIT.NEW_APP(), reply_markup=app_edit_list(apps))


@router.callback_query(EditAppFlowState.NewApp, AppEditList.filter())
async def choice_new_app(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    id_ = callback.data.split(":")[1]
    app = AppRepository().get_app_by_id_active(id_)
    data = await state.get_data()
    flow = FlowRepository().get_flow(data['flow_id'])

    if not app or not flow:
        return  # додаток або поток не існує

    await state.clear()

    if not KeitaroAppRepository().update_distribution(
            cmp_id=flow['distribution_campaign_id'], pixel=flow['pixel_fb'],
            sub3=flow['client_alias'], bundle=app['bundle']
    ):
        await callback.message.answer(
            i18n.FLOW.EDIT.NEW_APP_FAIL(error="keitaro"),
            reply_markup=kb_flow_back_edit(flow['id'])
        )
        return

    if not FlowRepository().update_bundle_flow(flow['id'], app['bundle']):
        await callback.message.answer(
            i18n.FLOW.EDIT.NEW_APP_FAIL(error="db"),
            reply_markup=kb_flow_back_edit(flow['id'])
        )
        return

    await callback.message.answer(
        i18n.FLOW.EDIT.NEW_APP_SUCCESS(),
        reply_markup=kb_flow_back_edit(flow['id'])
    )
