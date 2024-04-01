from aiogram.filters import BaseFilter
from aiogram.types import Message

from data.repository.TeamRepository import TeamRepository
from data.repository.UserRepository import UserRepository


class IsTeamFilter(BaseFilter):

    def __init__(self, is_team: bool = True):
        self.is_team = is_team

    async def __call__(self, message: Message):
        user = UserRepository().get_user(message.from_user.id)
        team = TeamRepository().get_team_by_uuid(user['team_uuid'])
        is_team_exist = (True if team else False)

        return is_team_exist if self.is_team else not is_team_exist
