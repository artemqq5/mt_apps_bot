from aiogram.filters import BaseFilter
from aiogram.types import Message

from data.repository.AccessRepository import AccessRepository
from data.repository.TeamRepository import TeamRepository


class IsTeamFilter(BaseFilter):

    def __init__(self, is_has_team: bool = True):
        self.is_has_team = is_has_team

    async def __call__(self, message: Message):
        try:
            access = AccessRepository().get_access_by_user_id(message.from_user.id)
            team = TeamRepository().get_team_by_uuid(access['team_uuid'])
        except Exception as _:
            team = False

        return team if self.is_has_team else not team
