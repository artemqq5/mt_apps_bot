from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.repositoryDB.AppRepository import AppRepository
from domain.states.admin.apps_.manage.DeleteApplication import DeleteApplicationState
from presenter.keyboards.admin_keyboard import kb_apps, DeleteApp, \
    kb_delete

router = Router()


@router.callback_query(DeleteApp.filter())
async def delete_app_handler(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    app_id = callback.data.split(":")[1]
    application = AppRepository().get_app_by_id(app_id)
    if not application:
        return

    await state.update_data(name=application['name'])
    await state.update_data(id=app_id)
    await state.set_state(DeleteApplicationState.delete)

    await callback.message.answer(i18n.APP.DELETE_WARNING(name=application['name']), reply_markup=kb_delete)


@router.message(DeleteApplicationState.delete, F.text == L.APPROVE_DELETE())
async def approve_delete_app(message: types.Message, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()

    if not AppRepository().delete_app_by_id(data['id']):
        await message.answer(i18n.APP.STATUS_EDIT_FAIL(name=data['name']), reply_markup=kb_apps)
        await state.clear()
        return

    await message.answer(i18n.APP.DELETE_SUCCESS(name=data['name']), reply_markup=kb_apps)
    await state.clear()
