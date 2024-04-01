from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from data.constants.buttons_text import APPS, SETTINGS

kb_menu_no_user = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=SETTINGS)],
])

kb_menu_user = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=APPS)],
    [KeyboardButton(text=SETTINGS)],
])
