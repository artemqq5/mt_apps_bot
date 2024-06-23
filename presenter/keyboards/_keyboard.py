from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.access import ADMIN
from data.repositoryDB.AccessRepository import AccessRepository
from data.repositoryDB.TeamRepository import TeamRepository
from data.repositoryDB.UserRepository import UserRepository
from presenter.keyboards.admin_keyboard import kb_menu_admin
from presenter.keyboards.no_user_keyboard import kb_menu_no_user
from presenter.keyboards.user_keyboard import kb_menu_user

kb_skip = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.SKIP())],
    [KeyboardButton(text=L.CANCEL())]
])

kb_cancel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.CANCEL())]
])

kb_settings = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.LOCALIZATION())],
    [KeyboardButton(text=L.CANCEL())]
])


class LanguageCD(CallbackData, prefix="lang"):
    lang: str


kb_languages = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.Language.uk(), callback_data=LanguageCD(lang="uk").pack())],
    [InlineKeyboardButton(text=L.Language.en(), callback_data=LanguageCD(lang="en").pack())],
    [InlineKeyboardButton(text=L.Language.ru(), callback_data=LanguageCD(lang="ru").pack())],
])


def keyboard_access(from_user_id) -> ReplyKeyboardMarkup:
    if UserRepository().user_role_by_id(from_user_id)['role'] == ADMIN:
        return kb_menu_admin
    else:
        try:
            access = AccessRepository().get_access_by_user_id(from_user_id)
            TeamRepository().get_team_by_uuid(access['team_uuid'])
            return kb_menu_user
        except Exception as _:
            return kb_menu_no_user


kb_apps_platform = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.IOS())],
    [KeyboardButton(text=L.TELEGRAM())],
    # [KeyboardButton(text=L.ANDROID())],
    # [KeyboardButton(text=L.PWA())],
    [KeyboardButton(text=L.CANCEL())]
])
