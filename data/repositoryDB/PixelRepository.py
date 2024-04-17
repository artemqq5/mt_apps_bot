from data.DefaultDataBase import DefaultDataBase


class PixelRepository(DefaultDataBase):

    def __init__(self):
        super().__init__()

    def add_pixel(self, pixel_id, token, user_id):
        query = "INSERT INTO `pixels` (`pixel_fb`, `token_fb`, `user_id`) VALUES (%s, %s, %s);"
        return self._insert(query, (pixel_id, token, user_id))

    def get_all_pixels(self, user_id):
        query = "SELECT * FROM `pixels` WHERE `user_id` = %s;"
        return self._select(query, (user_id,))

    def get_pixel(self, _id):
        query = "SELECT * FROM `pixels` WHERE `id` = %s;"
        return self._select_one(query, (_id,))

    def delete_pixel(self, _id):
        query = "DELETE FROM `pixels` WHERE `id` = %s;"
        return self._delete(query, (_id,))
