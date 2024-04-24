from data.DefaultDataBase import DefaultDataBase


class FlowRepository(DefaultDataBase):

    def __init__(self):
        super().__init__()

    def add_flow(self, link_user, link_keitaro, user_id, pixel, token, client_campain_id, client_campaign_name,
                 offer_id,
                 offer_name, domain, bundle, comment, distribution_campaign_id, distribution_campaign_name):
        query = '''INSERT INTO `flows` (`link_user`, `link_keitaro`, `user_id`, `pixel_fb`, `token_fb`, `client_campaign_id`,
        `client_campaign_name`, `offer_id`, `comment`, `offer_name`, `domain`, `bundle`, `distribution_campaign_id`, `distribution_campaign_name`) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
        return self._insert(query,
                            (link_user, link_keitaro, user_id, pixel, token, client_campain_id, client_campaign_name,
                             offer_id, comment, offer_name, domain, bundle, distribution_campaign_id,
                             distribution_campaign_name))

    def get_flow(self, flow_id):
        query = "SELECT * FROM `flows` WHERE `id` = %s;"
        return self._select_one(query, (flow_id,))

    def get_flows(self, user_id):
        query = "SELECT * FROM `flows` WHERE `user_id` = %s;"
        return self._select(query, (user_id,))
