from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

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
