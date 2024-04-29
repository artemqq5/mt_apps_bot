from data.DefaultDataBase import DefaultDataBase
from data.constants.access import BANNED_APP_STATUS


class AppRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()

    def get_all_apps(self):
        query = "SELECT * FROM `apps` WHERE `visibility` = 1 AND `status` != %s;"
        return self._select(query, (BANNED_APP_STATUS,))

    def get_app_by_id(self, app_id):
        query = "SELECT * FROM `apps` WHERE `id` = %s AND `visibility` = 1;"
        return self._select_one(query, (app_id,))

    def add_app(self, keitaro_id, name, url, bundle, image, geo, source, platform, desc):
        query = "INSERT INTO `apps` (`id`, `name`, `url`, `bundle`, `image`, `geo`, `source`, `platform`, `desc`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        return self._insert(query, (keitaro_id, name, url, bundle, image, geo, source, platform, desc))

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
        query = "UPDATE `apps` SET `visibility` = 0, `status` = %s WHERE `id` = %s;"
        return self._update(query, (BANNED_APP_STATUS, app_id))

    #  USERS =======================================================================================================

    def show_apps_by_platform_for_users(self, platform):
        query = "SELECT * FROM `apps` WHERE `platform` = %s AND `visibility` = 1 AND `status` = 'Active';"
        return self._select(query, (platform,))

    def get_app_by_id_for_users(self, app_id):
        query = "SELECT * FROM `apps` WHERE `id` = %s AND `visibility` = 1 AND `status` = 'Active';"
        return self._select_one(query, (app_id,))

    def get_app_by_bundle_keitaro_for_users(self, bundle):
        query = "SELECT * FROM `apps` WHERE `bundle` = %s;"
        return self._select_one(query, (bundle,))
