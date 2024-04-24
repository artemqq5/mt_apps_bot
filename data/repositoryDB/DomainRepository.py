from data.DefaultDataBase import DefaultDataBase


class DomainRepository(DefaultDataBase):

    def __init__(self):
        super().__init__()

    def add_domain(self, domain, domain_id):
        query = "INSERT IGNORE INTO `domains` (`domain`, `domain_id`) VALUES (%s, %s);"
        return self._insert(query, (domain, domain_id))

    def check_domain_limit(self, team_id):
        query = "SELECT COUNT(*) from `domains` WHERE `team_id` = %s AND `used_at` >= CURDATE() AND `used_at` < CURDATE() + INTERVAL 1 DAY;"
        return self._select_one(query, (team_id,))

    def check_free_domain(self):
        query = "SELECT * FROM `domains` WHERE `team_id` IS NULL;"
        return self._select_one(query)

    def reserve_domain(self, domain, team_id, user_id, team_name, used_at):
        query = "UPDATE `domains` SET `team_id` = %s, `team_name` = %s, `user_id` = %s, `used_at` = %s WHERE `domain` = %s;"
        return self._update(query, (team_id, team_name, user_id, used_at, domain))
