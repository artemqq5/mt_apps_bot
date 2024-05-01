from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from config import LINK_TO_SUPPORT

kb_menu_user = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.APPS())],
    [KeyboardButton(text=L.FLOW.MY_FLOWS())],
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


class FlowShowKeyboard(CallbackData, prefix="flow*show*keyboard"):
    id: int


def kb_user_flows(flows) -> InlineKeyboardMarkup:
    inline_kb = []
    for flow in flows:
        inline_kb.append(
            [InlineKeyboardButton(text=f"#{flow['id']} | {flow['domain']}",
                                  callback_data=FlowShowKeyboard(id=flow['id']).pack())]
        )

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


kb_call_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.FLOW.CALL_ADMIN(), url=LINK_TO_SUPPORT)],
])


class EditFlowComment(CallbackData, prefix="flow*edit*comment"):
    id: int


class EditFlowApp(CallbackData, prefix="flow*edit*app"):
    id: int


class EditFlowPixel(CallbackData, prefix="flow*edit*pixel"):
    id: int


class EditFlowOffer(CallbackData, prefix="flow*edit*offer"):
    id: int


def kb_flow_edit(flow_id) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.FLOW.EDIT.APP(), callback_data=EditFlowApp(id=flow_id).pack())],
        [InlineKeyboardButton(text=L.FLOW.EDIT.OFFER(), callback_data=EditFlowOffer(id=flow_id).pack())],
        [InlineKeyboardButton(text=L.FLOW.EDIT.PIXEL(), callback_data=EditFlowPixel(id=flow_id).pack())],
        [InlineKeyboardButton(text=L.FLOW.EDIT.COMMENT(), callback_data=EditFlowComment(id=flow_id).pack())],
        [InlineKeyboardButton(text=L.FLOW.CALL_ADMIN(), url=LINK_TO_SUPPORT)],
    ])


def kb_flow_back_edit(flow_id) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.FLOW.EDIT.BACK(), callback_data=FlowShowKeyboard(id=flow_id).pack())],
        [InlineKeyboardButton(text=L.FLOW.EDIT.APP(), callback_data=EditFlowApp(id=flow_id).pack())],
        [InlineKeyboardButton(text=L.FLOW.EDIT.OFFER(), callback_data=EditFlowOffer(id=flow_id).pack())],
        [InlineKeyboardButton(text=L.FLOW.EDIT.PIXEL(), callback_data=EditFlowPixel(id=flow_id).pack())],
        [InlineKeyboardButton(text=L.FLOW.EDIT.COMMENT(), callback_data=EditFlowComment(id=flow_id).pack())],
        [InlineKeyboardButton(text=L.FLOW.CALL_ADMIN(), url=LINK_TO_SUPPORT)],
    ])


class PixelEditList(CallbackData, prefix="pixel*edit*list"):
    id: int


def pixel_edit_list(pixels) -> InlineKeyboardMarkup:
    inline_kb = []
    for p in pixels:
        inline_kb.append(
            [InlineKeyboardButton(text=p['pixel_fb'], callback_data=PixelEditList(id=p['id']).pack())]
        )

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


class AppEditList(CallbackData, prefix="app*edit*list"):
    id: int


def app_edit_list(apps) -> InlineKeyboardMarkup:
    inline_kb = []
    for app in apps:
        inline_kb.append(
            [InlineKeyboardButton(text=app['name'], callback_data=AppEditList(id=app['id']).pack())]
        )

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)
