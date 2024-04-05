from aiogram_i18n import L
from aiogram_i18n.types import KeyboardButton, ReplyKeyboardMarkup

kb_skip = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.SKIP())],
    [KeyboardButton(text=L.CANCEL())]
])

kb_cancel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.CANCEL())]
])
