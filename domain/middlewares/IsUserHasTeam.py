from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject

from data.repository.TeamRepository import TeamRepository
from data.repository.UserRepository import UserRepository


class UserHasTeamMiddleware(BaseMiddleware):

    def __init__(self, has_team: bool = True):
        self.has_team = has_team

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, types.Message) or isinstance(event, types.CallbackQuery):
            user_id = event.from_user.id
        else:
            return

        user = UserRepository().get_user(user_id)

        if self.has_team:
            if not user['team_uuid']:
                return

            if not TeamRepository().get_team_by_uuid(user['team_uuid']):
                return

            return await handler(event, data)
        else:
            if not user['team_uuid']:
                return await handler(event, data)

            if not TeamRepository().get_team_by_uuid(user['team_uuid']):
                return await handler(event, data)

            return
