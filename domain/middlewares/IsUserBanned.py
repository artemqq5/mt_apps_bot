from typing import Callable, Any, Dict, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject, Update, ReplyKeyboardRemove

from data.constants.just_message import YOU_ARE_BLOKED
from data.repository.UserRepository import UserRepository


class UserBannedMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, types.Message) or isinstance(event, types.CallbackQuery):
            user_id = event.from_user.id
        else:
            print(type(event))
            return

        if UserRepository().is_banned(user_id)['banned']:
            await event.bot.send_message(chat_id=user_id, text=YOU_ARE_BLOKED, reply_markup=ReplyKeyboardRemove())
            return

        return await handler(event, data)

