from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext, L

from data.constants.access import ACCESS_STATUS_LIST
from data.repositoryDB.AccessRepository import AccessRepository
from data.repositoryDB.UserRepository import UserRepository
from domain.states.admin.team_.AccessManagment import AccessManagmentState
from presenter.keyboards.admin_keyboard import kb_teams, kb_team_access_managment, kb_delete, \
    kb_access_change_status

router = Router()


async def get_user_template(user_id):
    if not user_id:
        return ""

    user = UserRepository().get_user(user_id)
    if not user:
        return ""

    return f"\n\nuser id: <code>{user['telegram_id']}</code>\n" \
           f"username: @{user['username']}\n" \
           f"first name: {user['first_name']}\n" \
           f"last name: {user['last_name']}\n" \
           f"is banned: {bool(user['banned'])}"


@router.callback_query(F.data.contains("ACCESSTEAM"))
async def callback_team_access(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    team_id = callback.data.split("*CALLBACK*")[0]
    access_list = AccessRepository().get_access_by_team_id(team_id)

    if not access_list:
        await callback.message.answer(i18n.TEAM_HAVENT_ACCESS(), reply_markup=kb_teams)
        return

    for access in access_list:
        user_template = await get_user_template(access.get('user_id'))

        access_template = (f"deeplink: <code>t.me/mt_rent_apps_bot?start={access['uuid_']}</code>\n\n"
                           f"Created: {access['created_at']}\n"
                           f"Activated: {access['activated']}\n"
                           f"Access status: {access['status']}{user_template}")

        await callback.message.answer(access_template,
                                      reply_markup=kb_team_access_managment(access['uuid_']))


@router.callback_query(F.data.contains("DELETEACCESS"))
async def callback_delete_access(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    access_uuid = callback.data.split("*CALLBACK*")[0]
    access = AccessRepository().get_access_by_uuid(access_uuid)
    if not access:
        return

    await state.set_state(AccessManagmentState.DeleteAccess)
    await state.update_data(access_uuid=access_uuid)
    await callback.message.answer(i18n.WARNING_DELETE_ACCESS(), reply_markup=kb_delete)


@router.message(AccessManagmentState.DeleteAccess, F.text == L.APPROVE_DELETE())
async def approve_delete_access(message: types.Message, state: FSMContext, i18n: I18nContext):
    try:
        data = await state.get_data()

        if not AccessRepository().delete_access_by_uuid(data['access_uuid']):
            raise Exception

        await state.clear()
        await message.answer(i18n.SUCCESSFUL_DELETE_ACCESS(), reply_markup=kb_teams)
    except Exception as e:
        print(f"approve_delete_access: {e}")
        await state.clear()
        await message.answer(i18n.ERROR_DELETE_ACCESS(error=str(e)), reply_markup=kb_teams)


@router.callback_query(F.data.contains("CHANGESTATUSACCESS"))
async def callback_access_change_status(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    access_uuid = callback.data.split("*CALLBACK*")[0]
    access = AccessRepository().get_access_by_uuid(access_uuid)
    if not access:
        return

    await state.set_state(AccessManagmentState.ChangeStateAccess)
    await state.update_data(access_uuid=access_uuid)

    await callback.message.answer(i18n.CHOICE_NEW_STATUS_ACCESS(), reply_markup=kb_access_change_status)


@router.callback_query(AccessManagmentState.ChangeStateAccess, F.data.in_(ACCESS_STATUS_LIST))
async def callback_access_choice_status(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    try:
        data = await state.get_data()

        if not AccessRepository().update_access_status(data['access_uuid'], callback.data):
            raise Exception

        await state.clear()
        await callback.message.answer(i18n.SUCCESSFUL_CHANGE_STATUS_ACCESS(status=callback.data),
                                      reply_markup=kb_teams)
    except Exception as e:
        print(f"callback_access_choice_status: {e}")
        await state.clear()
        await callback.message.answer(i18n.ERROR_CHANGE_STATUS_ACCESS(error=str(e)), reply_markup=kb_teams)
