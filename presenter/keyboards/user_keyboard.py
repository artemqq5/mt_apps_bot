from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from aiogram_i18n import L
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# no user
kb_menu_no_user = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.SETTINGS())],
])

kb_request_access = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.SEND_REQUEST_ADMIN(), url="https://t.me/sed43f")],
])

# user

kb_menu_user = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.APPS())],
    [KeyboardButton(text=L.SETTINGS())],
])


class AppKeyboardLink(CallbackData, prefix="apps*inline*keyboard"):
    id: int


def kb_apps_keyboard(list_application) -> InlineKeyboardMarkup:
    inline_kb = []
    for app in list_application:
        inline_kb.append(
            [InlineKeyboardButton(text=app['name'], callback_data=AppKeyboardLink(id=app['id']).pack())]
        )

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)
