from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext

from data.constants.buttons_text import SHOW_BANNED_USERS, BAN_USER_CATEGORY, SKIP, UNBAN_USER_CATEGORY

from data.repository.UserRepository import UserRepository
from domain.states.ban_.BanUser import BanUserState
from domain.states.ban_.UnbanUser import UnbanUserState
from presenter.keyboards._keyboard import kb_cancel, kb_skip
from presenter.keyboards.admin_keyboard import kb_ban_system

router = Router()


@router.message(F.text == SHOW_BANNED_USERS)
async def all_banned_users(message: types.Message, i18n: I18nContext):
    list_of_banned_users = UserRepository().list_of_banned_users()
    body = ""

    for user in list_of_banned_users:
        # ban message if exist
        ban_m = f"\nmessage: {user['ban_message']}" if user['ban_message'] else ""
        # create info about banned user
        body += (f"id: <code>{user['telegram_id']}</code>\n"
                 f"username: @{user['username']}"
                 f"{ban_m}\n\n")

    if not body:
        body = i18n.BANNED_USERS_EMPTY()

    await message.answer(f"<b>{SHOW_BANNED_USERS}</b>\n\n{body}")


@router.message(F.text == UNBAN_USER_CATEGORY)
async def unban_user(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(UnbanUserState.UserData)
    await message.answer(i18n.INPUT_USER_ID_FOR_UNBAN(), reply_markup=kb_cancel.as_markup())


@router.message(UnbanUserState.UserData)
async def ban_message(message: types.Message, state: FSMContext, i18n: I18nContext):
    if UserRepository().unban_user_by_id(message.text):
        await message.answer(i18n.UNBAN_USER_SUCCESSFUL(), reply_markup=kb_ban_system.as_markup())
        await state.clear()
    else:
        await message.answer(i18n.ERROR_UNBANNED(), reply_markup=kb_cancel.as_markup())


@router.message(F.text == BAN_USER_CATEGORY)
async def ban_user(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(BanUserState.UserData)
    await message.answer(i18n.INPUT_USER_ID_OR_USERNAME_FOR_BAN(), reply_markup=kb_cancel.as_markup())


@router.message(BanUserState.UserData)
async def ban_message(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(user_data=message.text)
    await state.set_state(BanUserState.BanMessage)
    await message.answer(i18n.INPUT_USER_BAN_MESSAGE(), reply_markup=kb_skip.as_markup())


@router.message(BanUserState.BanMessage)
async def ban_(message: types.Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 255:
        await message.answer(i18n.BAN_MESSAGE_TOO_LONG(), reply_markup=kb_cancel.as_markup())
        return

    if message.text != SKIP:
        await state.update_data(ban_message=message.text)

    user_data = await state.get_data()
    user = user_data['user_data']
    ban_m = user_data.get('ban_message', None)

    try:
        if user.startswith("@"):
            if not UserRepository().ban_user_by_username(user.replace("@", ""), ban_m):
                raise Exception
        else:
            if not UserRepository().ban_user_by_id(user, ban_m):
                raise Exception

        await message.answer(i18n.SUCCESSFUL_BANNED(), reply_markup=kb_ban_system.as_markup())
    except Exception as e:
        print(f"ban_: {e}")
        await message.answer(i18n.ERROR_BANNED(), reply_markup=kb_ban_system.as_markup())
    finally:
        await state.clear()
