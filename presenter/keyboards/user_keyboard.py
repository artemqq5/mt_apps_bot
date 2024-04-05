from aiogram_i18n import L
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu_no_user = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.SETTINGS())],
])

kb_menu_user = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.APPS())],
    [KeyboardButton(text=L.SETTINGS())],
])
