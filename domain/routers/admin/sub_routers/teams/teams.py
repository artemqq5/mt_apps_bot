import uuid

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.formatting import Text, Bold
from aiogram_i18n import I18nContext, L

from data.repositoryDB.AccessRepository import AccessRepository
from data.repositoryDB.TeamRepository import TeamRepository
from domain.routers.admin.sub_routers.teams import delete_team_, generate_deeplink_, change_status_team_, access_team_, \
    domain_limit_, team_messaging_
from domain.states.admin.team_.CreateTeam import CreateTeamState
from presenter.keyboards._keyboard import kb_cancel
from presenter.keyboards.admin_keyboard import kb_teams, kb_team_managment, kb_show_teams, TeamShowCallback

router = Router()
router.include_routers(
    delete_team_.router,
    generate_deeplink_.router,
    change_status_team_.router,
    access_team_.router,
    domain_limit_.router,
    team_messaging_.router
)


@router.message(F.text == L.CREATE_TEAM())
async def input_team_name(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(CreateTeamState.TeamName)
    await message.answer(i18n.INPUT_TEAM_NAME(), reply_markup=kb_cancel)


@router.message(CreateTeamState.TeamName)
async def create_team(message: types.Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 255:
        await message.answer(i18n.TEAM_NAME_TOO_LONG(), reply_markup=kb_cancel)
        return

    team_uuid = uuid.uuid4()

    if not TeamRepository().create_team(message.text, team_uuid):
        await message.answer(i18n.ERROR_CREATE_TEAM(), reply_markup=kb_cancel)
        return

    await state.clear()
    await message.answer(i18n.SUCCESSFUL_CREATE_TEAM(team_name=message.text), reply_markup=kb_teams)


@router.message(F.text == L.SHOW_ALL_TEAM())
async def show_teams(message: types.Message, state: FSMContext, i18n: I18nContext):
    team_list = TeamRepository().get_teams()

    if not len(team_list):
        await message.answer(i18n.TEAM_LIST_IS_EMPTY(), reply_markup=kb_teams)
        return

    await message.answer(i18n.TEAMS(), reply_markup=kb_show_teams(team_list))


@router.callback_query(TeamShowCallback.filter())
async def team_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    id_ = callback.data.split(":")[1]
    team = TeamRepository().get_team_by_id(id_)

    team_users = AccessRepository().get_team_users(team['team_id'])

    team_template = Text(
        "ID: ", team['team_id'], "\n",
        "Team: ", Bold(team['team_name']), "\n",
        "Users: ", Bold(len(team_users)), "\n",
        "Domains Limit: ", Bold(team['limit']), "\n",
        "Status: ", Bold(team['status']), "\n",
        "Created at: ", Bold(team['created_at'])
    )
    await callback.message.answer(**team_template.as_kwargs(), reply_markup=kb_team_managment(team['team_id']))

