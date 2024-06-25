from aiogram_i18n import L
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from config import LINK_TO_SUPPORT

kb_menu_no_user = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.SETTINGS())],
], resize_keyboard=True)

kb_request_access = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.SEND_REQUEST_ADMIN(), url=LINK_TO_SUPPORT)],
], resize_keyboard=True)
