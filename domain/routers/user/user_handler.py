from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from data.constants.access import USER
from data.constants.buttons_text import MAIN_MENU, CANCEL, SETTINGS, APPS
from data.constants.just_message import CANCELED
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
async def start_(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(MAIN_MENU, reply_markup=kb_menu_user.as_markup())


@router.message(F.text == SETTINGS, IsAdminFilter(False), IsTeamFilter(True))
async def settings(message: types.Message):
    await message.answer(SETTINGS)


@router.message(F.text == APPS, IsAdminFilter(False))
async def settings(message: types.Message):
    await message.answer(APPS)


@router.message(F.text == CANCEL, IsAdminFilter(False), IsTeamFilter(True))
async def cancel_(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(CANCELED, reply_markup=kb_menu_user.as_markup())
