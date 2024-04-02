from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from data.constants.access import ACCESS_STATUS_LIST
from data.constants.buttons_text import APPROVE_DELETE
from data.constants.just_message import TEAM_HAVENT_ACCESS, WARNING_DELETE_ACCESS, SUCCESSFUL_DELETE_ACCESS, \
    ERROR_DELETE_ACCESS, \
    CHOICE_NEW_STATUS_ACCESS, PRESS_BACK_TO_TEAM_MENU, SUCCESSFUL_CHANGE_STATUS_ACCESS, ERROR_CHANGE_STATUS_ACCESS
from data.repository.AccessRepository import AccessRepository
from data.repository.UserRepository import UserRepository
from domain.states.team_.AccessManagment import AccessManagmentState
from presenter.keyboards.admin_keyboard import kb_teams, kb_team_access_managment, kb_team_delete, \
    kb_access_change_status, kb_team_managment_help

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
async def callback_team_access(callback: CallbackQuery, state: FSMContext):
    team_id = callback.data.split("*CALLBACK*")[0]
    access_list = AccessRepository().get_access_by_team_id(team_id)

    if not access_list:
        await callback.message.answer(TEAM_HAVENT_ACCESS, reply_markup=kb_teams.as_markup())
        return

    for access in access_list:
        user_template = await get_user_template(access.get('user_id'))

        access_template = (f"deeplink: <code>t.me/mt_rent_apps_test_bot?start={access['uuid_']}</code>\n\n"
                           f"Created: {access['created_at']}\n"
                           f"Activated: {access['activated']}\n"
                           f"Access status: {access['status']}{user_template}")

        await callback.message.answer(access_template,
                                      reply_markup=kb_team_access_managment(access['uuid_']).as_markup())


@router.callback_query(F.data.contains("DELETEACCESS"))
async def callback_delete_access(callback: CallbackQuery, state: FSMContext):
    access_uuid = callback.data.split("*CALLBACK*")[0]
    access = AccessRepository().get_access_by_uuid(access_uuid)
    if not access:
        return

    await state.set_state(AccessManagmentState.DeleteAccess)
    await state.update_data(access_uuid=access_uuid)
    await callback.message.answer(WARNING_DELETE_ACCESS, reply_markup=kb_team_delete.as_markup())


@router.message(AccessManagmentState.DeleteAccess, F.text == APPROVE_DELETE)
async def approve_delete_access(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()

        if not AccessRepository().delete_access_by_uuid(data['access_uuid']):
            raise Exception

        await state.clear()
        await message.answer(SUCCESSFUL_DELETE_ACCESS, reply_markup=kb_teams.as_markup())
    except Exception as e:
        print(f"approve_delete_access: {e}")
        await state.clear()
        await message.answer(ERROR_DELETE_ACCESS.format(e), reply_markup=kb_teams.as_markup())


@router.callback_query(F.data.contains("CHANGESTATUSACCESS"))
async def callback_access_change_status(callback: CallbackQuery, state: FSMContext):
    access_uuid = callback.data.split("*CALLBACK*")[0]
    access = AccessRepository().get_access_by_uuid(access_uuid)
    if not access:
        return

    await state.set_state(AccessManagmentState.ChangeStateAccess)
    await state.update_data(access_uuid=access_uuid)

    await callback.message.answer(CHOICE_NEW_STATUS_ACCESS, reply_markup=kb_access_change_status.as_markup())
    await callback.message.answer(PRESS_BACK_TO_TEAM_MENU, reply_markup=kb_team_managment_help.as_markup())


@router.callback_query(AccessManagmentState.ChangeStateAccess, F.data.in_(ACCESS_STATUS_LIST))
async def callback_access_choice_status(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()

        if not AccessRepository().update_access_status(data['access_uuid'], callback.data):
            raise Exception

        await state.clear()
        await callback.message.answer(SUCCESSFUL_CHANGE_STATUS_ACCESS.format(callback.data), reply_markup=kb_teams.as_markup())
    except Exception as e:
        print(f"callback_access_choice_status: {e}")
        await state.clear()
        await callback.message.answer(ERROR_CHANGE_STATUS_ACCESS.format(e), reply_markup=kb_teams.as_markup())

