from data.DefaultDataBase import DefaultDataBase


class UserRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()

    def add_user(self, telegrram_id, username, first_name, last_name, lang):
        query = "INSERT INTO `users` (telegram_id, username, first_name, last_name, lang) VALUES (%s, %s, %s, %s, %s);"
        return self._insert(query, (telegrram_id, username, first_name, last_name, lang))

    def get_user(self, telegram_id):
        query = "SELECT * FROM `users` WHERE `telegram_id` = %s;"
        return self._select_one(query, (telegram_id,))

    def is_banned(self, telegram_id):
        query = "SELECT `banned` FROM `users` WHERE `telegram_id` = %s;"
        return self._select_one(query, (telegram_id,))

    def is_admin(self, telegram_id):
        query = "SELECT `role` FROM `users` WHERE `telegram_id` = %s;"
        return self._select_one(query, (telegram_id,))

    def ban_user_by_id(self, telegram_id, ban_message=None):
        query = "UPDATE `users` SET `banned` = 1, `ban_message` = %s WHERE `telegram_id` = %s;"
        return self._update(query, (ban_message, telegram_id))

    def ban_user_by_username(self, username, ban_message=None):
        query = "UPDATE `users` SET `banned` = 1, `ban_message` = %s WHERE `username` = %s;"
        return self._update(query, (ban_message, username))

    def list_of_banned_users(self):
        query = "SELECT * FROM `users` WHERE `banned` = 1;"
        return self._select(query)

    def unban_user_by_id(self, telegram_id):
        query = "UPDATE `users` SET `banned` = 0, `ban_message` = null WHERE `telegram_id` = %s;"
        return self._update(query, (telegram_id,))
