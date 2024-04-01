import uuid

from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.formatting import Text, Bold, Code

from data.constants.buttons_text import CREATE_TEAM, SHOW_ALL_TEAM, BACK_TO_TEAM_MENU
from data.constants.just_message import INPUT_TEAM_NAME, TEAM_NAME_TOO_LONG, ERROR_CREATE_TEAM, SUCCESSFUL_CREATE_TEAM, \
    TEAM_LIST_IS_EMPTY, TEAM_MENU
from data.repository.TeamRepository import TeamRepository
from domain.routers.admin.sub_router.teams_ import delete_team_, generate_team_, change_status_team_
from domain.states.team_.CreateTeam import CreateTeamState
from domain.states.team_.TeamManagment import TeamManagmentState
from presenter.keyboards._keyboard import kb_cancel
from presenter.keyboards.admin_keyboard import kb_teams, kb_team_managment

router = Router()
router.include_routers(
    delete_team_.router,
    generate_team_.router,
    change_status_team_.router
)


@router.message(F.text == CREATE_TEAM)
async def input_team_name(message: types.Message, state: FSMContext):
    await state.set_state(CreateTeamState.TeamName)
    await message.answer(INPUT_TEAM_NAME, reply_markup=kb_cancel.as_markup())


@router.message(CreateTeamState.TeamName)
async def create_team(message: types.Message, state: FSMContext):
    if len(message.text) > 255:
        await message.answer(TEAM_NAME_TOO_LONG, reply_markup=kb_cancel.as_markup())
        return

    team_uuid = uuid.uuid4()

    if not TeamRepository().create_team(message.text, team_uuid):
        await message.answer(ERROR_CREATE_TEAM, reply_markup=kb_cancel.as_markup())
        return

    await state.clear()
    await message.answer(SUCCESSFUL_CREATE_TEAM.format(message.text, team_uuid), reply_markup=kb_teams.as_markup())


@router.message(F.text == SHOW_ALL_TEAM)
async def show_teams(message: types.Message, state: FSMContext):
    team_list = TeamRepository().get_teams()

    if not len(team_list):
        await message.answer(TEAM_LIST_IS_EMPTY, reply_markup=kb_teams.as_markup())
        return

    for team in team_list:
        team_template = Text(
            "ID: ", team['team_id'], "\n",
            "Team: ", Bold(team['team_name']), "\n",
            "Status: ", team['status'], "\n",
            "Created at: ", team['created_at']
        )

        await message.answer(**team_template.as_kwargs(), reply_markup=kb_team_managment(team['team_id']).as_markup())


@router.message(F.text == BACK_TO_TEAM_MENU, StateFilter(TeamManagmentState))
async def back_team_menu(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(TEAM_MENU, reply_markup=kb_teams.as_markup())



