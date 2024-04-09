from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hlink
from aiogram_i18n import L, I18nContext

from data.repository.AppRepository import AppRepository
from domain.states.user.ShowApps import ShowAppsState
from presenter.keyboards.user_keyboard import kb_apps_keyboard, AppKeyboardLink, kb_menu_user

router = Router()


@router.message(ShowAppsState.show, F.text.in_((L.IOS(),)))  # L.ANDROID(), L.PWA()
async def show_applications(message: types.Message, state: FSMContext, i18n: I18nContext):
    applications = AppRepository().show_apps_by_platform_for_users(message.text)
    if not applications:
        await message.answer(i18n.APP.APP_LIST_EMPTY(), reply_markup=kb_menu_user)
        await state.clear()
        return

    await message.answer(i18n.USER.IOS_APPS(), reply_markup=kb_apps_keyboard(applications))


@router.callback_query(AppKeyboardLink.filter())
async def detail_app_handler(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    app = AppRepository().get_app_by_id_for_users(callback.data.split(":")[1])
    if not app:
        return

    if app['platform'] == i18n.IOS():
        name_url = hlink(app['name'], f"https://apps.apple.com/app/id{app['bundle']}")
    elif app['platform'] == i18n.ANDROID():
        name_url = hlink(app['name'], f"https://play.google.com/store/apps/details?id={app['bundle']}")
    else:
        name_url = app['name']

    await callback.message.answer_photo(
        photo=app['image'],
        caption=i18n.USER.DESC_TEMPLATE(
            name_url=name_url,
            platform=app['platform'],
            source=app['source'],
            geo=app['geo'],
            desc=app['desc']
        )
    )
