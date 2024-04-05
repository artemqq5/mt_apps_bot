from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext, L

from data.constants.access import USER
from domain.filters.isAdminFilter import IsAdminFilter
from domain.filters.isTeamFilter import IsTeamFilter
from domain.middlewares.IsUserHasTeam import UserHasTeamMiddleware
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presenter.keyboards.user_keyboard import kb_menu_user

router = Router()

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
    await message.answer(i18n.SETTINGS())


@router.message(F.text == L.APPS(), IsAdminFilter(False))
async def apps(message: types.Message, i18n: I18nContext):
    await message.answer(i18n.APPS())


@router.message(F.text == L.CANCEL(), IsAdminFilter(False), IsTeamFilter(True))
async def cancel(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(i18n.CANCELED(), reply_markup=kb_menu_user)
