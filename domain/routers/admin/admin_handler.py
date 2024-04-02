from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from data.constants.access import ADMIN
from data.constants.buttons_text import MAIN_MENU, BAN_SYSTEM, TEAMS, CANCEL, SETTINGS
from data.constants.just_message import CANCELED
from domain.filters.isAdminFilter import IsAdminFilter
from domain.middlewares.IsUserRole import UserRoleMiddleware
from domain.routers.admin.sub_router.bun_ import ban_system
from domain.routers.admin.sub_router.teams_ import teams
from presenter.keyboards.admin_keyboard import kb_menu_admin, kb_ban_system, kb_teams

router = Router()
router.include_routers(ban_system.router, teams.router)

router.message.middleware(UserRoleMiddleware(ADMIN))
router.callback_query.middleware(UserRoleMiddleware(ADMIN))


@router.message(Command("start"), IsAdminFilter(True))
async def start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(MAIN_MENU, reply_markup=kb_menu_admin.as_markup())


@router.message(F.text == CANCEL, IsAdminFilter(True))
async def cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(CANCELED, reply_markup=kb_menu_admin.as_markup())


@router.message(F.text == TEAMS)
async def teams_menu(message: types.Message):
    await message.answer(TEAMS, reply_markup=kb_teams.as_markup())


@router.message(F.text == BAN_SYSTEM)
async def ban_menu(message: types.Message):
    await message.answer(BAN_SYSTEM, reply_markup=kb_ban_system.as_markup())


@router.message(F.text == SETTINGS, IsAdminFilter(True))
async def settings(message: types.Message):
    await message.answer(SETTINGS)









