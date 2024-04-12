from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext, L

from data.constants.access import USER
from domain.filters.isAdminFilter import IsAdminFilter
from domain.filters.isTeamFilter import IsTeamFilter
from domain.middlewares.IsUserHasTeam import UserHasTeamMiddleware
from domain.middlewares.IsUserRole import UserRoleMiddleware
from domain.routers.user.sub_routers.apps_ import show_ as apps_show, create_link_
from domain.states.user.apps_.ShowApps import ShowAppsState
from presenter.keyboards._keyboard import kb_settings, kb_apps_platform
from presenter.keyboards.user_keyboard import kb_menu_user, kb_pixel_menu
from domain.routers.user.sub_routers.pixel import add_ as pixel_add, show_ as pixel_show
from domain.routers.user.sub_routers.pixel.manage import delete_ as pixel_delete

router = Router()
router.include_routers(
    apps_show.router,
    pixel_add.router,
    pixel_delete.router,
    pixel_show.router,
    create_link_.router
)

router.message.middleware(UserRoleMiddleware(USER))
router.callback_query.middleware(UserRoleMiddleware(USER))

router.message.middleware(UserHasTeamMiddleware(True))
router.callback_query.middleware(UserHasTeamMiddleware(True))


@router.message(Command("start"), IsAdminFilter(False), IsTeamFilter(True))
async def start(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(i18n.MAIN_MENU(), reply_markup=kb_menu_user)


@router.message(F.text == L.APPS(), IsAdminFilter(False), IsTeamFilter(True))
async def apps(message: types.Message, i18n: I18nContext, state: FSMContext):
    await state.set_state(ShowAppsState.Show)
    await message.answer(i18n.USER.CHOICE_PLATFORM_APP(), reply_markup=kb_apps_platform)


@router.message(F.text == L.USER.PIXEL_FB())
async def pixel(message: types.Message, i18n: I18nContext, state: FSMContext):
    await message.answer(i18n.USER.PIXEL_FB(), reply_markup=kb_pixel_menu)


@router.message(F.text == L.SETTINGS(), IsAdminFilter(False), IsTeamFilter(True))
async def settings(message: types.Message, i18n: I18nContext):
    await message.answer(i18n.SETTINGS(), reply_markup=kb_settings)


@router.message(F.text == L.CANCEL(), IsAdminFilter(False), IsTeamFilter(True))
async def cancel(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(i18n.CANCELED(), reply_markup=kb_menu_user)
