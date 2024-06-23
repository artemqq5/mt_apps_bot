from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError
from aiogram_i18n import I18nContext
from aiogram_i18n.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.access import ACTIVE_APP_STATUS, BANNED_APP_STATUS, DRAFT_APP_STATUS
from data.repositoryDB.UserRepository import UserRepository


class NotificationUser:

    # Розсилка за списком (текс, медіа, кнопка)
    async def __notify_list_any(self, bot: Bot, users, data, error_message, i18n):
        counter = 0
        block = 0
        other = 0

        for user in users:
            try:
                await self.generate_message_users(data, bot, user, i18n)
                counter += 1
            except TelegramForbiddenError as e:
                block += 1
                print(f"user({user}) | {error_message}: {e} ")
            except Exception as e:
                other += 1
                print(f"user({user}) | {error_message}: {e} ")

        print(f"notification {error_message}: {counter}/{len(users)}")
        return i18n.NOTIFY.RESULT(get=str(counter), users=str(len(users)), block=str(block), other=str(other))

    # Розсилка за id (текс, медіа, кнопка)
    async def generate_message_users(self, data, bot: Bot, user_id, i18n=None):
        if i18n:
            await self.generate_message_state(data, bot, user_id, i18n)
            return

        keyboard = ReplyKeyboardRemove()
        if data.get('button_url', None):
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=data['button_text'], url=data['button_url'])]
            ])

        if data.get('photo', None):
            await bot.send_photo(chat_id=user_id, photo=data['photo'], caption=data['message'], reply_markup=keyboard)
        elif data.get('video', None):
            await bot.send_video(chat_id=user_id, video=data['video'], caption=data['message'], reply_markup=keyboard)
        elif data.get('animation', None):
            await bot.send_animation(chat_id=user_id, animation=data['animation'], caption=data['message'],
                                     reply_markup=keyboard)
        else:
            await bot.send_message(chat_id=user_id, text=data['message'], reply_markup=keyboard)

    @staticmethod  # Розсилка за id (текс, медіа, кнопка)
    async def generate_message_state(data, bot: Bot, user, i18n):
        with i18n.use_locale(user['lang']):
            if data['type'] == ACTIVE_APP_STATUS:
                message = i18n.NOYIFY.APP_STATUS_ACTIVE(app_name=data['app_name'])
            elif data['type'] == BANNED_APP_STATUS:
                message = i18n.NOYIFY.APP_STATUS_BAN(app_name=data['app_name'])
            elif data['type'] == DRAFT_APP_STATUS:
                message = i18n.NOYIFY.APP_STATUS_DRAFT(app_name=data['app_name'])
            else:
                raise Exception

            await bot.send_photo(chat_id=user['telegram_id'], photo=data['photo'], caption=message)

    # Стандартна розсилка користувачам
    async def default_messaging_users(self, bot: Bot, i18n: I18nContext, data):
        if data['category'] == i18n.NOTIFY.CATEGORY_NO_USERS():
            users = [user['telegram_id'] for user in UserRepository().get_users_no_team() if user['banned'] == 0]
        elif data['category'] == i18n.NOTIFY.CATEGORY_USERS():
            users = [user['telegram_id'] for user in UserRepository().get_users_in_team() if user['banned'] == 0]
        elif data['category'] == i18n.TEAM_MESSAGING():
            users = [user['telegram_id'] for user in UserRepository().get_users_by_team_id(data['team_id']) if
                     user['banned'] == 0]
        else:
            users = [user['telegram_id'] for user in UserRepository().get_all_users() if user['banned'] == 0]

        return await self.__notify_list_any(bot, users, data, "default user message", i18n)

    async def ban_app_message(self, application, bot: Bot, i18n):
        users = [user for user in UserRepository().get_all_users() if user['banned'] == 0]
        data = {
            "photo": application['image'],
            "app_name": application['name'],
            "type": BANNED_APP_STATUS
        }

        return await self.__notify_list_any(bot, users, data, "ban_app_message", i18n)

    async def active_app_message(self, application, bot: Bot, i18n):
        users = [user for user in UserRepository().get_all_users() if user['banned'] == 0]
        data = {
            "photo": application['image'],
            "app_name": application['name'],
            "type": ACTIVE_APP_STATUS
        }

        return await self.__notify_list_any(bot, users, data, "active_app_message", i18n)

    async def draft_app_message(self, application, bot: Bot, i18n):
        users = [user for user in UserRepository().get_all_users() if user['banned'] == 0]
        data = {
            "photo": application['image'],
            "app_name": application['name'],
            "type": DRAFT_APP_STATUS
        }

        return await self.__notify_list_any(bot, users, data, "draft_app_message", i18n)
