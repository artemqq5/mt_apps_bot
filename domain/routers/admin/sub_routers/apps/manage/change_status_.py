from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext, L

from data.constants.access import ACTIVE_APP_STATUS, BANNED_APP_STATUS
from data.repositoryDB.AppRepository import AppRepository
from domain.notify.NotificationUser import NotificationUser
from domain.states.admin.apps_.manage.ChangeStatusApplication import ChangeStatusApplicationState
from presenter.keyboards.admin_keyboard import ChangeStatusApp, kb_status_app, kb_apps, ChangeAppStatus, \
    kb_notify_status_app, kb_menu_admin

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
    await state.update_data(status_app=status_data)
    if not AppRepository().update_status_by_id(data['id'], status_data):
        await callback.message.answer(i18n.APP.STATUS_EDIT_FAIL(), reply_markup=kb_apps)
        await state.clear()
        return

    await callback.message.answer(i18n.APP.STATUS_EDIT_SUCCESS())

    await callback.message.answer(
        i18n.APP.STATUS_NOTIFY_NEW_STATUS(status=status_data),
        reply_markup=kb_notify_status_app()
    )
    await state.set_state(ChangeStatusApplicationState.notify)


@router.message(ChangeStatusApplicationState.notify, F.text == L.YES())
async def notify_user_about_status(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()
    app = AppRepository().get_app_by_id(data['id'])

    if not app:
        await state.clear()
        return

    if data['status_app'] == ACTIVE_APP_STATUS:
        result = await NotificationUser().active_app_message(app, bot, i18n)
    elif data['status_app'] == BANNED_APP_STATUS:
        result = await NotificationUser().ban_app_message(app, bot, i18n)
    else:
        result = await NotificationUser().draft_app_message(app, bot, i18n)

    await message.answer(result, reply_markup=kb_menu_admin)
    await state.clear()
