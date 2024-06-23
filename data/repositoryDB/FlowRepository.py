from data.DefaultDataBase import DefaultDataBase


class FlowRepository(DefaultDataBase):

    def __init__(self):
        super().__init__()

    def add_flow(self, link_user, link_keitaro, user_id, pixel, token, client_campain_id, client_campaign_name,
                 offer_id, offer_name, domain, bundle, comment, distribution_campaign_id, distribution_campaign_name,
                 client_alias, distribution_alias, timnameidfilter, platform):
        query = '''INSERT INTO `flows` (`link_user`, `link_keitaro`, `user_id`, `pixel_fb`, `token_fb`, `client_campaign_id`,
        `client_campaign_name`, `offer_id`, `comment`, `offer_name`, `domain`, `bundle`, `distribution_campaign_id`,
         `distribution_campaign_name`, `client_alias`, `distribution_alias`, `timnameidfilter`, `platform`) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
        return self._insert(query,
                            (link_user, link_keitaro, user_id, pixel, token, client_campain_id, client_campaign_name,
                             offer_id, comment, offer_name, domain, bundle, distribution_campaign_id,
                             distribution_campaign_name, client_alias, distribution_alias, timnameidfilter, platform))

    def get_flow(self, flow_id):
        query = "SELECT * FROM `flows` WHERE `id` = %s;"
        return self._select_one(query, (flow_id,))

    def get_flows(self, user_id):
        query = "SELECT * FROM `flows` WHERE `user_id` = %s;"
        return self._select(query, (user_id,))

    def update_comment_flow(self, flow_id, comment):
        query = "UPDATE `flows` SET `comment` = %s WHERE `id` = %s;"
        return self._update(query, (comment, flow_id))

    def update_pixel_flow(self, flow_id, pixel_id, token, link_keitaro):
        query = "UPDATE `flows` SET `pixel_fb` = %s, `token_fb` = %s, `link_keitaro` = %s WHERE `id` = %s;"
        return self._update(query, (pixel_id, token, link_keitaro, flow_id))

    def update_offer_flow(self, flow_id, offer_url):
        query = "UPDATE `flows` SET `link_user` = %s WHERE `id` = %s;"
        return self._update(query, (offer_url, flow_id))

    def update_bundle_flow(self, flow_id, bundle, link_keitaro):
        query = "UPDATE `flows` SET `bundle` = %s, `link_keitaro` = %s WHERE `id` = %s;"
        return self._update(query, (bundle, link_keitaro, flow_id))
