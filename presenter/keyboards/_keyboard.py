from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from data.constants.buttons_text import MAIN_MENU, SETTINGS, CANCEL, SKIP

kb_skip = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=SKIP)],
    [KeyboardButton(text=CANCEL)]
])


kb_cancel = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=CANCEL)]
])
