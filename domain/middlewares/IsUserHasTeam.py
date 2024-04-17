from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject

from data.repositoryDB.AccessRepository import AccessRepository
from data.repositoryDB.TeamRepository import TeamRepository


class UserHasTeamMiddleware(BaseMiddleware):

    def __init__(self, has_team: bool = True):
        self.has_team = has_team

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if not isinstance(event, (types.Message, types.CallbackQuery)):
            return

        if self.has_team:
            access = AccessRepository().get_access_by_user_id(event.from_user.id)
            if not access or not TeamRepository().get_team_by_uuid(access['team_uuid']):
                return
        else:
            access = AccessRepository().get_access_by_user_id(event.from_user.id)
            if access and TeamRepository().get_team_by_uuid(access['team_uuid']):
                return

        return await handler(event, data)
