from datetime import datetime

from aiogram import Router, types, F
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext, L

from data.constants.access import USER
from data.repository.AccessRepository import AccessRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.filters.isTeamFilter import IsTeamFilter
from domain.middlewares.IsUserHasTeam import UserHasTeamMiddleware
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presenter.keyboards._keyboard import kb_settings
from presenter.keyboards.no_user_keyboard import kb_menu_no_user, kb_request_access
from presenter.keyboards.user_keyboard import kb_menu_user

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
        await message.answer(i18n.JOIN_KEY_NOT_EXIST(), reply_markup=kb_menu_no_user)
        return

    # join key was activated before
    if access_by_uuid['user_id']:
        await message.answer(i18n.JOIN_KEY_ACTIVATED_BEFORE(), reply_markup=kb_menu_no_user)
        return

    if not AccessRepository().activate_access(access_join_key, message.from_user.id, datetime.now()):
        await message.answer(i18n.JOIN_KEY_FAIL_UPDATE(), reply_markup=kb_menu_no_user)
        return

    await message.answer(i18n.JOIN_KEY_SUCCESS_UPDATE(), reply_markup=kb_menu_user)


@router.message(F.text == L.SETTINGS(), IsAdminFilter(False), IsTeamFilter(False))
async def settings(message: types.Message, i18n: I18nContext):
    await message.answer(i18n.SETTINGS(), reply_markup=kb_settings)


@router.message(F.text == L.CANCEL(), IsAdminFilter(False), IsTeamFilter(False))
async def cancel(message: types.Message, i18n: I18nContext, state: FSMContext):
    await state.clear()
    await message.answer(i18n.CANCELED(), reply_markup=kb_menu_no_user)


@router.message(IsAdminFilter(False), IsTeamFilter(False), F.text != L.LOCALIZATION())
async def other(message: types.Message, i18n: I18nContext):
    await message.answer(i18n.YOU_NEED_BE_REGISTERED(), reply_markup=kb_request_access)

