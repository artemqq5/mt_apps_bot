import uuid

from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.formatting import Text, Bold
from aiogram_i18n import I18nContext

from data.constants.buttons_text import CREATE_TEAM, SHOW_ALL_TEAM

from data.repository.TeamRepository import TeamRepository
from domain.routers.admin.sub_router.teams_ import delete_team_, generate_deeplink_, change_status_team_, access_team_
from domain.states.team_.AccessManagment import AccessManagmentState
from domain.states.team_.CreateTeam import CreateTeamState
from domain.states.team_.TeamManagment import TeamManagmentState
from presenter.keyboards._keyboard import kb_cancel
from presenter.keyboards.admin_keyboard import kb_teams, kb_team_managment

router = Router()
router.include_routers(
    delete_team_.router,
    generate_deeplink_.router,
    change_status_team_.router,
    access_team_.router
)


@router.message(F.text == CREATE_TEAM)
async def input_team_name(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(CreateTeamState.TeamName)
    await message.answer(i18n.INPUT_TEAM_NAME(), reply_markup=kb_cancel.as_markup())


@router.message(CreateTeamState.TeamName)
async def create_team(message: types.Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 255:
        await message.answer(i18n.TEAM_NAME_TOO_LONG(), reply_markup=kb_cancel.as_markup())
        return

    team_uuid = uuid.uuid4()

    if not TeamRepository().create_team(message.text, team_uuid):
        await message.answer(i18n.ERROR_CREATE_TEAM(), reply_markup=kb_cancel.as_markup())
        return

    await state.clear()
    await message.answer(i18n.SUCCESSFUL_CREATE_TEAM(team_name=message.text), reply_markup=kb_teams.as_markup())


@router.message(F.text == SHOW_ALL_TEAM)
async def show_teams(message: types.Message, state: FSMContext, i18n: I18nContext):
    team_list = TeamRepository().get_teams()

    if not len(team_list):
        await message.answer(i18n.TEAM_LIST_IS_EMPTY(), reply_markup=kb_teams.as_markup())
        return

    for team in team_list:
        team_template = Text(
            "ID: ", team['team_id'], "\n",
            "Team: ", Bold(team['team_name']), "\n",
            "Status: ", team['status'], "\n",
            "Created at: ", team['created_at']
        )

        await message.answer(**team_template.as_kwargs(), reply_markup=kb_team_managment(team['team_id']).as_markup())

