from data.DefaultDataBase import DefaultDataBase


class AppRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()

    def get_app_by_id(self, app_id):
        query = "SELECT * FROM `apps` WHERE `id` = %s;"
        return self._select_one(query, (app_id,))

    def add_app(self, name, bundle, image, geo, source, platform, desc):
        query = "INSERT INTO `apps` (`name`, `bundle`, `image`, `geo`, `source`, `platform`, `desc`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        return self._insert(query, (name, bundle, image, geo, source, platform, desc))

    def show_apps_by_platform(self, platform):
        query = "SELECT * FROM `apps` WHERE `platform` = %s AND `visibility` = 1;"
        return self._select(query, (platform,))

    def update_geo_by_id(self, app_id, geo):
        query = "UPDATE `apps` SET `geo` = %s WHERE `id` = %s;"
        return self._update(query, (geo, app_id))

    def update_status_by_id(self, app_id, status):
        query = "UPDATE `apps` SET `status` = %s WHERE `id` = %s;"
        return self._update(query, (status, app_id))

    def delete_app_by_id(self, app_id):
        query = "UPDATE `apps` SET `visibility` = 0 WHERE `id` = %s;"
        return self._update(query, (app_id, ))

