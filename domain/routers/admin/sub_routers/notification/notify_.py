from doctest import SKIP

from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.markdown import hlink
from aiogram_i18n import L, I18nContext
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from data.repositoryDB.AppRepository import AppRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.notify.NotificationUser import NotificationUser
from domain.routers.admin.sub_routers.apps.manage import change_geo_, change_status_, delete_app_
from domain.states.admin.apps_.ShowApplication import ShowApplicationState
from domain.states.admin.notify.NotificateUser import NotificateUserState
from presenter.keyboards._keyboard import kb_apps_platform, kb_cancel, kb_skip
from presenter.keyboards.admin_keyboard import kb_apps, kb_managment_app, kb_notify_preview, kb_menu_admin
from presenter.keyboards.user_keyboard import apps_keyboard_list, AppKeyboardList

router = Router()


@router.message(
    NotificateUserState.Category,
    F.text.in_((L.NOTIFY.CATEGORY_ALL_USERS(), L.NOTIFY.CATEGORY_USERS(), L.NOTIFY.CATEGORY_NO_USERS()))
)
async def category_notify_category(message: Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(category=message.text)
    await state.set_state(NotificateUserState.Message)
    await message.answer(i18n.NOTIFY.MESSAGE(), reply_markup=kb_cancel)


@router.message(NotificateUserState.Message)
async def message_notify(message: Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(message=message.text)
    await state.set_state(NotificateUserState.Media)
    await message.answer(i18n.NOTIFY.MEDIA(), reply_markup=kb_skip)


@router.message(NotificateUserState.Media, (F.photo | F.animation | F.video | (F.text == L.SKIP())))
async def media_notify(message: Message, i18n: I18nContext, state: FSMContext):
    if message.content_type == 'photo':
        await state.update_data(photo=message.photo[-1].file_id)
    elif message.content_type == 'animation':
        await state.update_data(animation=message.document.file_id)
    elif message.content_type == 'video':
        await state.update_data(video=message.video.file_id)

    await state.set_state(NotificateUserState.ButtonUrl)
    await message.answer(i18n.NOTIFY.BUTTON_URL(), reply_markup=kb_skip)


@router.message(NotificateUserState.ButtonUrl)
async def button_notify_url(message: Message, i18n: I18nContext, state: FSMContext, bot: Bot):
    if message.text == i18n.SKIP():
        await state.set_state(NotificateUserState.Preview)
        data = await state.get_data()
        await NotificationUser.generate_message_users(data, bot, message.from_user.id)
        await message.answer(i18n.NOTIFY.PREVIEW(), reply_markup=kb_notify_preview)
        return

    if not message.text.startswith("https://"):
        await message.answer(i18n.NOTIFY.BUTTON_URL_VALIDATION(), reply_markup=kb_skip)
        return

    await state.update_data(button_url=message.text)
    await state.set_state(NotificateUserState.ButtonText)
    await message.answer(i18n.NOTIFY.BUTTON_TEXT(), reply_markup=kb_skip)


@router.message(NotificateUserState.ButtonText)
async def button_notify_text(message: Message, i18n: I18nContext, state: FSMContext, bot: Bot):
    await state.update_data(button_text=message.text)

    if len(message.text) > 50:
        await message.answer(i18n.NOTIFY.BUTTON_TEXT_LIMIT(), reply_markup=kb_skip)
        return

    if message.text == i18n.SKIP():
        await state.update_data(button_text=i18n.NOTIFY.DEFAULT_BUTTON_TEXT())

    data = await state.get_data()
    await NotificationUser.generate_message_users(data, bot, message.from_user.id)
    await state.set_state(NotificateUserState.Preview)
    await message.answer(i18n.NOTIFY.PREVIEW(), reply_markup=kb_notify_preview)


@router.message(NotificateUserState.Preview, F.text == L.NOTIFY.SEND())
async def preview_notify(message: Message, i18n: I18nContext, state: FSMContext, bot: Bot):
    data = await state.get_data()
    await state.clear()

    result = await NotificationUser().default_messaging_users(bot, i18n, data)
    await message.answer(result, reply_markup=kb_menu_admin)
