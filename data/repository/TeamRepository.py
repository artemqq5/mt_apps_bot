import uuid

from data.DefaultDataBase import DefaultDataBase


class TeamRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()

    def create_team(self, team_name, team_uuid):
        query = "INSERT INTO `teams` (team_name, uuid) VALUES (%s, %s);"
        return self._insert(query, (team_name, team_uuid))

    def get_team_by_id(self, team_id):
        query = "SELECT * FROM `teams` WHERE `team_id` = %s;"
        return self._select_one(query, (team_id,))

    def get_team_by_uuid(self, team_uuid):
        query = "SELECT * FROM `teams` WHERE `uuid` = %s;"
        return self._select_one(query, (team_uuid,))

    def get_teams(self):
        query = "SELECT * FROM `teams`;"
        return self._select(query)

    def delete_team(self, team_id):
        query = "DELETE FROM `teams` WHERE `team_id` = %s;"
        return self._delete(query, (team_id,))

    def update_team_key(self, team_uuid, team_id):
        query = "UPDATE `teams` SET `uuid` = %s WHERE `team_id` = %s;"
        return self._update(query, (team_uuid, team_id))

    def update_team_status(self, team_status, team_id):
        query = "UPDATE `teams` SET `status` = %s WHERE `team_id` = %s;"
        return self._update(query, (team_status, team_id))
