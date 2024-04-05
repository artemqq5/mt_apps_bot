from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext, L

from data.constants.access import ADMIN
from domain.filters.isAdminFilter import IsAdminFilter
from domain.middlewares.IsUserRole import UserRoleMiddleware
from domain.routers.admin.sub_router.bun_ import ban_system
from domain.routers.common_route_ import localization_
from domain.routers.admin.sub_router.teams_ import teams
from presenter.keyboards._keyboard import kb_settings
from presenter.keyboards.admin_keyboard import kb_menu_admin, kb_ban_system, kb_teams

router = Router()
router.include_routers(
    ban_system.router,
    teams.router
)

router.message.middleware(UserRoleMiddleware(ADMIN))
router.callback_query.middleware(UserRoleMiddleware(ADMIN))


@router.message(Command("start"), IsAdminFilter(True))
async def start(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(i18n.MAIN_MENU(), reply_markup=kb_menu_admin)


@router.message(F.text == L.CANCEL(), IsAdminFilter(True))
async def cancel(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(i18n.CANCELED(), reply_markup=kb_menu_admin)


@router.message(F.text == L.TEAMS())
async def teams_menu(message: types.Message, i18n: I18nContext):
    await message.answer(i18n.TEAMS(), reply_markup=kb_teams)


@router.message(F.text == L.BAN_SYSTEM())
async def ban_menu(message: types.Message, i18n: I18nContext):
    await message.answer(i18n.BAN_SYSTEM(), reply_markup=kb_ban_system)


@router.message(F.text == L.SETTINGS(), IsAdminFilter(True))
async def settings(message: types.Message, i18n: I18nContext):
    await message.answer(i18n.SETTINGS(), reply_markup=kb_settings)
