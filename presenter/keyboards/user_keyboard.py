from aiogram_i18n import L
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu_no_user = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=str(L.SETTINGS()))],
])

kb_menu_user = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=str(L.APPS()))],
    [KeyboardButton(text=str(L.SETTINGS()))],
])
