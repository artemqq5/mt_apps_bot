from datetime import datetime

from aiogram import Router, types, F
from aiogram.filters import Command, CommandObject
from aiogram_i18n import I18nContext

from data.constants.access import USER
from data.constants.buttons_text import CANCEL, SETTINGS
from data.constants.just_message import CANCELED
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


@router.message(Command('start'), IsAdminFilter(False), IsTeamFilter(False))
async def start(message: types.Message, command: CommandObject, i18n: I18nContext):
    access_join_key = command.args
    access_by_uuid = AccessRepository().get_access_by_uuid(access_join_key)

    # join key is not exist
    if not access_by_uuid:
        await message.answer(i18n.JOIN_KEY_NOT_EXIST(), reply_markup=kb_menu_no_user.as_markup())
        return

    # join key was activated before
    if access_by_uuid['user_id']:
        await message.answer(i18n.JOIN_KEY_ACTIVATED_BEFORE(), reply_markup=kb_menu_no_user.as_markup())
        return

    if not AccessRepository().activate_access(access_join_key, message.from_user.id, datetime.now()):
        await message.answer(i18n.JOIN_KEY_FAIL_UPDATE(), reply_markup=kb_menu_no_user.as_markup())
        return

    await message.answer(i18n.JOIN_KEY_SUCCESS_UPDATE(), reply_markup=kb_menu_user.as_markup())


@router.message(F.text == SETTINGS, IsAdminFilter(False), IsTeamFilter(False))
async def settings(message: types.Message):
    await message.answer(SETTINGS)
