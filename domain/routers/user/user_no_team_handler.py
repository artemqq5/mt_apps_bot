from datetime import datetime

from aiogram import Router, types, F
from aiogram.filters import Command

from data.constants.access import USER
from data.constants.buttons_text import CANCEL, SETTINGS
from data.constants.just_message import CANCELED, INPUT_TEAM_KEY, JOIN_KEY_FAIL_UPDATE, JOIN_KEY_NOT_EXIST, \
    JOIN_KEY_SUCCESS_UPDATE, JOIN_KEY_ACTIVATED_BEFORE
from data.repository.AccessRepository import AccessRepository
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


@router.message(IsAdminFilter(False), IsTeamFilter(False))
async def messages(message: types.Message):
    access_join_key = message.text
    access_by_uuid = AccessRepository().get_access_by_uuid(access_join_key)

    # join key is not exist
    if not access_by_uuid:
        await message.answer(JOIN_KEY_NOT_EXIST, reply_markup=kb_menu_no_user.as_markup())
        return

    # join key was activated before
    if access_by_uuid['user_id']:
        await message.answer(JOIN_KEY_ACTIVATED_BEFORE, reply_markup=kb_menu_no_user.as_markup())
        return

    if not AccessRepository().activate_access(access_join_key, message.from_user.id, datetime.now()):
        await message.answer(JOIN_KEY_FAIL_UPDATE, reply_markup=kb_menu_no_user.as_markup())
        return

    await message.answer(JOIN_KEY_SUCCESS_UPDATE, reply_markup=kb_menu_user.as_markup())

