from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import L, I18nContext
from aiogram_i18n.types import ReplyKeyboardMarkup

from data.constants.access import ADMIN
from data.repository.AccessRepository import AccessRepository
from data.repository.TeamRepository import TeamRepository
from data.repository.UserRepository import UserRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.filters.isTeamFilter import IsTeamFilter
from presenter.keyboards._keyboard import kb_languages, LanguageCD, keyboard_access
from presenter.keyboards.admin_keyboard import kb_menu_admin
from presenter.keyboards.user_keyboard import kb_menu_user, kb_menu_no_user

route = Router()


@route.message(F.text == L.LOCALIZATION())
async def set_localization(message: Message, i18n: I18nContext):
    await message.answer(i18n.CHOICE_LANG(), reply_markup=kb_languages)


@route.callback_query(LanguageCD.filter())
async def callback_set_language_handler_admin(callback: CallbackQuery, i18n: I18nContext):
    kb_menu = keyboard_access(callback.from_user.id)

    if not UserRepository().change_lang(callback.from_user.id, callback.data[5:]):
        await callback.message.answer(i18n.FAIL_CHANGE_LANG())
        return

    await i18n.set_locale(callback.data[5:])
    await callback.message.answer(i18n.SUCCESSFUL_CHANGE_LANG(lang=callback.data[5:]), reply_markup=kb_menu)



