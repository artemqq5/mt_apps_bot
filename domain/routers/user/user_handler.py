from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext, L

from data.constants.access import USER
from domain.filters.isAdminFilter import IsAdminFilter
from domain.filters.isTeamFilter import IsTeamFilter
from domain.middlewares.IsUserHasTeam import UserHasTeamMiddleware
from domain.middlewares.IsUserRole import UserRoleMiddleware
from domain.routers.common_route_ import localization_
from domain.routers.user.sub_routers import apps_
from domain.states.user.ShowApps import ShowAppsState
from presenter.keyboards._keyboard import kb_settings, kb_apps_platform
from presenter.keyboards.user_keyboard import kb_menu_user

router = Router()
router.include_routers(apps_.router)

router.message.middleware(UserRoleMiddleware(USER))
router.callback_query.middleware(UserRoleMiddleware(USER))

router.message.middleware(UserHasTeamMiddleware(True))
router.callback_query.middleware(UserHasTeamMiddleware(True))


@router.message(Command("start"), IsAdminFilter(False), IsTeamFilter(True))
async def start(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(i18n.MAIN_MENU(), reply_markup=kb_menu_user)


@router.message(F.text == L.SETTINGS(), IsAdminFilter(False), IsTeamFilter(True))
async def settings(message: types.Message, i18n: I18nContext):
    await message.answer(i18n.SETTINGS(), reply_markup=kb_settings)


@router.message(F.text == L.APPS(), IsAdminFilter(False), IsTeamFilter(True))
async def apps(message: types.Message, i18n: I18nContext, state: FSMContext):
    await state.set_state(ShowAppsState.show)
    await message.answer(i18n.USER.CHOICE_PLATFORM_APP(), reply_markup=kb_apps_platform)


@router.message(F.text == L.CANCEL(), IsAdminFilter(False), IsTeamFilter(True))
async def cancel(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(i18n.CANCELED(), reply_markup=kb_menu_user)
