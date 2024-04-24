from aiogram import Bot
from aiogram_i18n import I18nContext
from aiogram_i18n.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

from data.repositoryDB.AccessRepository import AccessRepository
from data.repositoryDB.UserRepository import UserRepository


class NotificationUser:

    # Розсилка за списком (текс, медіа, кнопка)
    async def __notify_list_any(self, bot: Bot, users, data, error_message, i18n):
        counter = 0
        error_list = ""

        for user in users:
            try:
                await self.generate_message_users(data, bot, user)
                counter += 1
            except Exception as e:
                error_list += f"user({user}) - {e}\n"
                print(f"{error_message}: {e}")

        print(f"notification {error_message}: {counter}/{len(users)}")
        return i18n.NOTIFY.RESULT(get=str(counter), users=str(len(users)), error_messaging_list=error_list)

    @staticmethod  # Розсилка за id (текс, медіа, кнопка)
    async def generate_message_users(data, bot: Bot, user_id):
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

    # Стандартна розсилка користувачам
    async def default_messaging_users(self, bot: Bot, i18n: I18nContext, data):
        if data['category'] == i18n.NOTIFY.CATEGORY_NO_USERS():
            users = [user['telegram_id'] for user in UserRepository().get_users_no_team() if user['banned'] == 0]
        elif data['category'] == i18n.NOTIFY.CATEGORY_USERS():
            users = [user['telegram_id'] for user in UserRepository().get_users_in_team() if user['banned'] == 0]
        elif data['category'] == i18n.TEAM_MESSAGING():
            users = [user['user_id'] for user in AccessRepository().get_team_users(data['team_id']) if user['banned'] == 0]
        else:
            users = [user['telegram_id'] for user in UserRepository().get_users() if user['banned'] == 0]

        return await self.__notify_list_any(bot, users, data, "default user message", i18n)
