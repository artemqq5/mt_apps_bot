from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from data.constants.access import Trial_TEAM, Basic_TEAM, Standard_TEAM, Premium_TEAM, Ultimate_TEAM
from data.constants.buttons_text import TEAMS, BAN_SYSTEM, CANCEL, BAN_USER_CATEGORY, SHOW_BANNED_USERS, \
    UNBAN_USER_CATEGORY, CREATE_TEAM, SHOW_ALL_TEAM, DELETE_TEAM, CHANGE_STATUS, REGENERATE_JOIN_KEY, BACK_TO_TEAM_MENU, \
    APPROVE_REGENERATE_TEAM, APPROVE_DELETE_TEAM, TRIAL, BASIC, STANDART, PREMIUM, ULTIMATE, SETTINGS

kb_menu_admin = ReplyKeyboardBuilder(markup=[
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
        [InlineKeyboardButton(text=DELETE_TEAM, callback_data=f"{team_id}*CALLBACK*DELETE")],
        [InlineKeyboardButton(text=CHANGE_STATUS, callback_data=f"{team_id}*CALLBACK*CHANGESTATUS")],
        [InlineKeyboardButton(text=REGENERATE_JOIN_KEY, callback_data=f"{team_id}*CALLBACK*REGENERATEJOINKEY")],
    ])


kb_team_managment_help = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=BACK_TO_TEAM_MENU)],
    [KeyboardButton(text=CANCEL)]
])

kb_team_delete = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=APPROVE_DELETE_TEAM)],
    [KeyboardButton(text=BACK_TO_TEAM_MENU)],
    [KeyboardButton(text=CANCEL)]
])

kb_team_regenerate = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text=APPROVE_REGENERATE_TEAM)],
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
