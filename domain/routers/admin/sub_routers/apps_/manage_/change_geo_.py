from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.repository.AppRepository import AppRepository
from domain.states.admin.apps_.manage.ChangeGeoApplication import ChangeGeoApplicationState
from presenter.keyboards.admin_keyboard import ChangeGeoApp, kb_apps

router = Router()


@router.callback_query(ChangeGeoApp.filter())
async def change_geo_handler(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    app_id = callback.data.split(":")[1]
    await state.update_data(id=app_id)
    await state.set_state(ChangeGeoApplicationState.geo)

    await callback.message.answer(i18n.APP.SET_GEO())  # reply_markup=kb_apps_platform


@router.message(ChangeGeoApplicationState.geo)
async def set_new_geo(message: Message, i18n: I18nContext, state: FSMContext):
    data = await state.get_data()
    if not AppRepository().update_geo_by_id(data['id'], message.text):
        await message.answer(i18n.APP.GEO_EDIT_FAIL(), reply_markup=kb_apps)
        await state.clear()
        return

    await message.answer(i18n.APP.GEO_EDIT_SUCCESSFUL(), reply_markup=kb_apps)
    await state.clear()
