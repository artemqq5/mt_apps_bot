from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositoryDB.AppRepository import AppRepository
from domain.states.admin.apps_.manage.ChangeStatusApplication import ChangeStatusApplicationState
from presenter.keyboards.admin_keyboard import ChangeStatusApp, kb_status_app, kb_apps, ChangeAppStatus

router = Router()


@router.callback_query(ChangeStatusApp.filter())
async def change_status_handler(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    app_id = callback.data.split(":")[1]
    application = AppRepository().get_app_by_id(app_id)
    if not application:
        return

    await state.update_data(name=application['name'])
    await state.update_data(id=app_id)
    await state.set_state(ChangeStatusApplicationState.status)

    await callback.message.answer(i18n.APP.SET_STATUS(name=application['name']), reply_markup=kb_status_app)


@router.callback_query(ChangeStatusApplicationState.status, ChangeAppStatus.filter())
async def choice_app_status_handler(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    data = await state.get_data()
    status_data = callback.data.split(":")[1]
    if not AppRepository().update_status_by_id(data['id'], status_data):
        await callback.message.answer(i18n.APP.STATUS_EDIT_FAIL(), reply_markup=kb_apps)
        await state.clear()
        return

    await callback.message.answer(i18n.APP.STATUS_EDIT_SUCCESS(), reply_markup=kb_apps)
    await state.clear()
