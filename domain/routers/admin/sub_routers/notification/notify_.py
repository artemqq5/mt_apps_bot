from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.markdown import hlink
from aiogram_i18n import L, I18nContext

from data.repositoryDB.AppRepository import AppRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.routers.admin.sub_routers.apps.manage import change_geo_, change_status_, delete_app_
from domain.states.admin.apps_.ShowApplication import ShowApplicationState
from presenter.keyboards._keyboard import kb_apps_platform
from presenter.keyboards.admin_keyboard import kb_apps, kb_managment_app
from presenter.keyboards.user_keyboard import apps_keyboard_list, AppKeyboardList

router = Router()


@router.message(F.text == L.NOTIFY.CATEGORY_USERS())
async def category_notify_all(message: Message, i18n: I18nContext, state: FSMContext):
    pass
