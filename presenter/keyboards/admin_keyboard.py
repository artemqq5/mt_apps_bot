import math

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import L
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.access import Trial_TEAM, Basic_TEAM, Standard_TEAM, Premium_TEAM, Ultimate_TEAM, Byer_ACCESS, \
    TeamLead_ACCESS, ACTIVE_APP_STATUS, BANNED_APP_STATUS, MASONS_LINK, DRAFT_APP_STATUS

kb_menu_admin = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.APPS())],
    [KeyboardButton(text=L.TEAMS())],
    [KeyboardButton(text=L.NOTIFY.NOTIFICATION())],
    [KeyboardButton(text=L.BAN_SYSTEM())],
    [KeyboardButton(text=L.SETTINGS())],
], resize_keyboard=True)

kb_ban_system = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.BAN_USER_CATEGORY())],
    [KeyboardButton(text=L.UNBAN_USER_CATEGORY())],
    [KeyboardButton(text=L.SHOW_BANNED_USERS())],
    [KeyboardButton(text=L.CANCEL())]
], resize_keyboard=True)

kb_teams = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.CREATE_TEAM())],
    [KeyboardButton(text=L.SHOW_ALL_TEAM())],
    [KeyboardButton(text=L.CANCEL())]
], resize_keyboard=True)


class TeamShowCallback(CallbackData, prefix="teams*show*keyboard"):
    team_id: int
    page: int


class TeamPageCallback(CallbackData, prefix="teams*page*keyboard"):
    page: int


def kb_show_teams(current_page: int, teams):
    total_pages = math.ceil(len(teams) / 10)
    keyboard = InlineKeyboardBuilder()

    start_index = (current_page - 1) * 10
    end_index = min(start_index + 10, len(teams))

    for i in range(start_index, end_index):
        keyboard.row(InlineKeyboardButton(
            text=f"#{teams[i]['team_id']} | {teams[i]['team_name']}",
            callback_data=TeamShowCallback(team_id=teams[i]['team_id'], page=current_page).pack()
        ))

    nav = []
    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<<--',
            callback_data=TeamPageCallback(page=current_page - 1).pack()
        ))
    if current_page < total_pages:
        nav.append(InlineKeyboardButton(
            text='-->>',
            callback_data=TeamPageCallback(page=current_page + 1).pack()
        ))

    keyboard.row(*nav)

    return keyboard.as_markup(resize_keyboard=True)


class TeamDetailBack(CallbackData, prefix="TEAM*DETAIL*BACK"):
    page: int


def kb_team_managment(team_id, page):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.DELETE_TEAM(), callback_data=f"{team_id}*CALLBACK*DELETETEAM")],
        [InlineKeyboardButton(text=L.GENERATE_JOIN_KEY(), callback_data=f"{team_id}*CALLBACK*GENERATEJOINKEY")],
        [InlineKeyboardButton(text=L.ACCESS_TEAM(), callback_data=f"{team_id}*CALLBACK*ACCESSTEAM")],
        [InlineKeyboardButton(text=L.CHANGE_STATUS(), callback_data=f"{team_id}*CALLBACK*CHANGESTATUSTEAM")],
        [InlineKeyboardButton(text=L.DOMAIN_LIMIT(), callback_data=f"{team_id}*CALLBACK*DOMAINLIMIT")],
        [InlineKeyboardButton(text=L.TEAM_MESSAGING(), callback_data=f"{team_id}*CALLBACK*TEAMMESSAGING")],
        [InlineKeyboardButton(text=L.BACK(), callback_data=TeamDetailBack(page=page).pack())]
    ], resize_keyboard=True)


kb_team_managment_help = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.CANCEL())]
], resize_keyboard=True)

kb_delete = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.APPROVE_DELETE())],
    [KeyboardButton(text=L.CANCEL())]
], resize_keyboard=True)

kb_team_generate = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.APPROVE_GENERATE_TEAM())],
    [KeyboardButton(text=L.CANCEL())]
], resize_keyboard=True)

kb_team_change_status = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.TRIAL(), callback_data=Trial_TEAM)],
    [InlineKeyboardButton(text=L.BASIC(), callback_data=Basic_TEAM)],
    [InlineKeyboardButton(text=L.STANDART(), callback_data=Standard_TEAM)],
    [InlineKeyboardButton(text=L.PREMIUM(), callback_data=Premium_TEAM)],
    [InlineKeyboardButton(text=L.ULTIMATE(), callback_data=Ultimate_TEAM)],
], resize_keyboard=True)


def kb_team_access_managment(access_uuid):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.DELETE_ACCESS(), callback_data=f"{access_uuid}*CALLBACK*DELETEACCESS")],
        [InlineKeyboardButton(text=L.CHANGE_ACCESS_STATUS(),
                              callback_data=f"{access_uuid}*CALLBACK*CHANGESTATUSACCESS")],
    ], resize_keyboard=True)


kb_access_delete = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.APPROVE_DELETE())],
    [KeyboardButton(text=L.CANCEL())]
], resize_keyboard=True)

kb_access_change_status = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BYER(), callback_data=Byer_ACCESS)],
    [InlineKeyboardButton(text=L.TEAM_LEAD(), callback_data=TeamLead_ACCESS)],
], resize_keyboard=True)

kb_apps = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.ADD_APP())],
    [KeyboardButton(text=L.SHOW_APPS())],
    [KeyboardButton(text=L.CANCEL())]
], resize_keyboard=True)

kb_source = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=MASONS_LINK)],
    [KeyboardButton(text=L.CANCEL())]
], resize_keyboard=True)

kb_preview = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.PUBLUSH_APP())],
    [KeyboardButton(text=L.START_ADD_OVER())],
    [KeyboardButton(text=L.CANCEL())]
], resize_keyboard=True)


class ChangeGeoApp(CallbackData, prefix="change*geo*application"):
    id: int


class ChangeStatusApp(CallbackData, prefix="change*status*application"):
    id: int


class DeleteApp(CallbackData, prefix="delete*application"):
    id: int


def kb_managment_app(id_app) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.CHANGE_GEO_APP(), callback_data=ChangeGeoApp(id=id_app).pack())],
        [InlineKeyboardButton(text=L.CHANGE_STATUS_APP(), callback_data=ChangeStatusApp(id=id_app).pack())],
        [InlineKeyboardButton(text=L.DELETE_APP(), callback_data=DeleteApp(id=id_app).pack())],
    ], resize_keyboard=True)


class ChangeAppStatus(CallbackData, prefix="change*status*app"):
    status: str


kb_status_app = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ACTIVE_STATUS_APP(), callback_data=ChangeAppStatus(status=ACTIVE_APP_STATUS).pack())],
    [InlineKeyboardButton(text=L.BANNED_STATUS_APP(), callback_data=ChangeAppStatus(status=BANNED_APP_STATUS).pack())],
    [InlineKeyboardButton(text=L.DRAFT_STATUS_APP(), callback_data=ChangeAppStatus(status=DRAFT_APP_STATUS).pack())],
], resize_keyboard=True)

kb_notification = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.NOTIFY.CATEGORY_USERS())],
    [KeyboardButton(text=L.NOTIFY.CATEGORY_NO_USERS())],
    [KeyboardButton(text=L.NOTIFY.CATEGORY_ALL_USERS())],
    [KeyboardButton(text=L.CANCEL())]
], resize_keyboard=True)

kb_domain_limit = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.CANCEL_DOAMIN_LIMIT())],
    [KeyboardButton(text=L.CANCEL())]
], resize_keyboard=True)

kb_notify_preview = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.NOTIFY.SEND())],
    [KeyboardButton(text=L.CANCEL())]
], resize_keyboard=True)


class AccessShowCallback(CallbackData, prefix="access*show*keyboard"):
    uuid_: str


def kb_show_access(accesses) -> InlineKeyboardMarkup:
    inline_kb = []
    for access in accesses:
        inline_kb.append(
            [InlineKeyboardButton(text=f"#{access['user_id']} | {access['uuid_']}",
                                  callback_data=AccessShowCallback(uuid_=access['uuid_']).pack())]
        )

    return InlineKeyboardMarkup(inline_keyboard=inline_kb, resize_keyboard=True)


def kb_notify_status_app() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=L.YES())],
        [KeyboardButton(text=L.CANCEL())]
    ], resize_keyboard=True)
