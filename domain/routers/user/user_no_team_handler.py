from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from data.constants.access import USER
from data.constants.buttons_text import MAIN_MENU, CANCEL, SETTINGS
from data.constants.just_message import CANCELED, INPUT_TEAM_KEY, TEAM_KEY_FAIL_UPDATE, TEAM_UUID_NOT_EXIST, \
    TEAM_KEY_SUCCESS_UPDATE
from data.repository.TeamRepository import TeamRepository
from data.repository.UserRepository import UserRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.filters.isTeamFilter import IsTeamFilter
from domain.middlewares.IsUserHasTeam import UserHasTeamMiddleware
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presenter.keyboards.user_keyboard import kb_menu_user, kb_menu_no_user

router = Router()

router.message.middleware(UserRoleMiddleware(USER))
router.callback_query.middleware(UserRoleMiddleware(USER))

router.message.middleware(UserHasTeamMiddleware(False))
router.callback_query.middleware(UserHasTeamMiddleware(False))


@router.message(Command("start"), IsAdminFilter(False), IsTeamFilter(False))
async def start_(message: types.Message):
    await message.answer(INPUT_TEAM_KEY, reply_markup=kb_menu_no_user.as_markup())


@router.message(F.text == SETTINGS, IsAdminFilter(False), IsTeamFilter(False))
async def settings(message: types.Message):
    await message.answer(SETTINGS)


@router.message(F.text == CANCEL, IsAdminFilter(False), IsTeamFilter(False))
async def cancel_(message: types.Message):
    await message.answer(CANCELED, reply_markup=kb_menu_no_user.as_markup())


@router.message(IsAdminFilter(False))
async def messages(message: types.Message):

    if not TeamRepository().get_team_by_uuid(message.text):
        await message.answer(TEAM_UUID_NOT_EXIST, reply_markup=kb_menu_no_user.as_markup())
        return

    if not UserRepository().update_team_key(message.text, message.from_user.id):
        await message.answer(TEAM_KEY_FAIL_UPDATE, reply_markup=kb_menu_no_user.as_markup())
        return

    await message.answer(TEAM_KEY_SUCCESS_UPDATE, reply_markup=kb_menu_user.as_markup())
