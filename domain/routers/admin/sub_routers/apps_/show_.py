from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hlink
from aiogram_i18n import L, I18nContext

from data.repository.AppRepository import AppRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.routers.admin.sub_routers.apps_.manage_ import change_geo_, change_status_, delete_app_
from domain.states.admin.apps_.ShowApplication import ShowApplicationState
from presenter.keyboards._keyboard import kb_apps_platform
from presenter.keyboards.admin_keyboard import kb_apps, kb_managment_app
from presenter.keyboards.user_keyboard import kb_apps_keyboard, AppKeyboardLink

router = Router()
router.include_routers(
    change_geo_.router,
    change_status_.router,
    delete_app_.router
)


@router.message(F.text == L.SHOW_APPS())
async def show_platform(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(ShowApplicationState.platform)
    await message.answer(i18n.APP.CHOICE_PLATFORM(), reply_markup=kb_apps_platform)


@router.message(ShowApplicationState.platform, F.text.in_((L.IOS(),)))  # L.ANDROID(), L.PWA()
async def show_applications(message: types.Message, state: FSMContext, i18n: I18nContext):
    applications = AppRepository().show_apps_by_platform(message.text)
    if not applications:
        await message.answer(i18n.APP.APP_LIST_EMPTY(), reply_markup=kb_apps)
        await state.clear()
        return

    await state.update_data(platform=message.text)
    await message.answer(i18n.APP.IOS_APPS(), reply_markup=kb_apps_keyboard(applications))


@router.callback_query(AppKeyboardLink.filter(), IsAdminFilter(True))
async def show_application_detail(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    app = AppRepository().get_app_by_id(callback.data.split(":")[1])
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
        caption=i18n.APP.DESC_TEMPLATE(
            name_url=name_url,
            platform=app['platform'],
            source=app['source'],
            geo=app['geo'],
            status=app['status'],
            desc=app['desc']
        ),
        reply_markup=kb_managment_app(app['id'])
    )
