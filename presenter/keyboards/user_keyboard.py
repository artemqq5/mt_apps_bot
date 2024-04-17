from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


kb_menu_user = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.APPS())],
    [KeyboardButton(text=L.USER.PIXEL_FB())],
    [KeyboardButton(text=L.SETTINGS())],
])


class AppKeyboardList(CallbackData, prefix="apps*inline*keyboard"):
    id: int


def apps_keyboard_list(list_application) -> InlineKeyboardMarkup:
    inline_kb = []
    for app in list_application:
        inline_kb.append(
            [InlineKeyboardButton(text=app['name'], callback_data=AppKeyboardList(id=app['id']).pack())]
        )

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


kb_pixel_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.USER.ADD_PIXEL_FB())],
    [KeyboardButton(text=L.USER.SHOW_MY_PIXELS())],
    [KeyboardButton(text=L.CANCEL())],
])


class PixelKeyboardList(CallbackData, prefix="pixel*show*keyboard"):
    id: int


def pixel_keyboard_list(pixels) -> InlineKeyboardMarkup:
    inline_kb = []
    for p in pixels:
        inline_kb.append(
            [InlineKeyboardButton(text=p['pixel_fb'], callback_data=PixelKeyboardList(id=p['id']).pack())]
        )

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


class PixelChoiceKeyboardList(CallbackData, prefix="pixel*choice*keyboard"):
    id: int


def pixel_choice_keyboard_list(pixels) -> InlineKeyboardMarkup:
    inline_kb = []
    for p in pixels:
        inline_kb.append(
            [InlineKeyboardButton(text=p['pixel_fb'], callback_data=PixelChoiceKeyboardList(id=p['id']).pack())]
        )

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


class PixelDeleteKeyboard(CallbackData, prefix="pixel*delete*keyboard"):
    id: int


def kb_delte_pixel(_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.USER.DELETE_PIXEL(), callback_data=PixelDeleteKeyboard(id=_id).pack())]
    ])


class AppCreateLinkKeyboard(CallbackData, prefix="app*createlink*keyboard"):
    id: int


def kb_create_app_link(app_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.USER.CREATE_APP_LINK(), callback_data=AppCreateLinkKeyboard(id=app_id).pack())]
    ])


kb_create_pixelfb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.USER.ADD_PIXEL_FB())],
    [KeyboardButton(text=L.CANCEL())]
])
