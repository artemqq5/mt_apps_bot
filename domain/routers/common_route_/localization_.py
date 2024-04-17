from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import L, I18nContext

from data.repositoryDB.UserRepository import UserRepository
from presenter.keyboards._keyboard import kb_languages, LanguageCD, keyboard_access

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



