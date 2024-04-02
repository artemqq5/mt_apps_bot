from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from data.constants.access import Trial_TEAM, Basic_TEAM, Standard_TEAM, Premium_TEAM, Ultimate_TEAM, Byer_ACCESS, \
    TeamLead_ACCESS
from data.constants.buttons_text import TEAMS, BAN_SYSTEM, CANCEL, BAN_USER_CATEGORY, SHOW_BANNED_USERS, \
    UNBAN_USER_CATEGORY, CREATE_TEAM, SHOW_ALL_TEAM, DELETE_TEAM, CHANGE_STATUS, BACK_TO_TEAM_MENU, \
    APPROVE_GENERATE_TEAM, APPROVE_DELETE, TRIAL, BASIC, STANDART, PREMIUM, ULTIMATE, SETTINGS, \
    GENERATE_JOIN_KEY, ACCESS_TEAM, DELETE_ACCESS, CHANGE_ACCESS_STATUS, BYER, TEAM_LEAD, APPS

kb_menu_admin = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=APPS)],
    [KeyboardButton(text=TEAMS)],
    [KeyboardButton(text=BAN_SYSTEM)],
    [KeyboardButton(text=SETTINGS)],
])

kb_ban_system = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=BAN_USER_CATEGORY)],
    [KeyboardButton(text=UNBAN_USER_CATEGORY)],
    [KeyboardButton(text=SHOW_BANNED_USERS)],
    [KeyboardButton(text=CANCEL)]
])

kb_teams = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=CREATE_TEAM)],
    [KeyboardButton(text=SHOW_ALL_TEAM)],
    [KeyboardButton(text=CANCEL)]
])


def kb_team_managment(team_id):
    return InlineKeyboardBuilder(markup=[
        [InlineKeyboardButton(text=DELETE_TEAM, callback_data=f"{team_id}*CALLBACK*DELETETEAM")],
        [InlineKeyboardButton(text=GENERATE_JOIN_KEY, callback_data=f"{team_id}*CALLBACK*GENERATEJOINKEY")],
        [InlineKeyboardButton(text=ACCESS_TEAM, callback_data=f"{team_id}*CALLBACK*ACCESSTEAM")],
        [InlineKeyboardButton(text=CHANGE_STATUS, callback_data=f"{team_id}*CALLBACK*CHANGESTATUSTEAM")],
    ])


kb_team_managment_help = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=BACK_TO_TEAM_MENU)],
    [KeyboardButton(text=CANCEL)]
])

kb_team_delete = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=APPROVE_DELETE)],
    [KeyboardButton(text=BACK_TO_TEAM_MENU)],
    [KeyboardButton(text=CANCEL)]
])

kb_team_generate = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=APPROVE_GENERATE_TEAM)],
    [KeyboardButton(text=BACK_TO_TEAM_MENU)],
    [KeyboardButton(text=CANCEL)]
])

kb_team_change_status = InlineKeyboardBuilder(markup=[
    [InlineKeyboardButton(text=TRIAL, callback_data=Trial_TEAM)],
    [InlineKeyboardButton(text=BASIC, callback_data=Basic_TEAM)],
    [InlineKeyboardButton(text=STANDART, callback_data=Standard_TEAM)],
    [InlineKeyboardButton(text=PREMIUM, callback_data=Premium_TEAM)],
    [InlineKeyboardButton(text=ULTIMATE, callback_data=Ultimate_TEAM)],
])


def kb_team_access_managment(access_uuid):
    return InlineKeyboardBuilder(markup=[
        [InlineKeyboardButton(text=DELETE_ACCESS, callback_data=f"{access_uuid}*CALLBACK*DELETEACCESS")],
        [InlineKeyboardButton(text=CHANGE_ACCESS_STATUS, callback_data=f"{access_uuid}*CALLBACK*CHANGESTATUSACCESS")],
    ])


kb_access_delete = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=APPROVE_DELETE)],
    [KeyboardButton(text=BACK_TO_TEAM_MENU)],
    [KeyboardButton(text=CANCEL)]
])

kb_access_change_status = InlineKeyboardBuilder(markup=[
    [InlineKeyboardButton(text=BYER, callback_data=Byer_ACCESS)],
    [InlineKeyboardButton(text=TEAM_LEAD, callback_data=TeamLead_ACCESS)],
])
