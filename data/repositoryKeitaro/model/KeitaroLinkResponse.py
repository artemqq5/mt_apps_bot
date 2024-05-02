class KeitaroLinkResponse:
    def __init__(self, link_user, link_keitaro, user_id, pixel, token, client_campain_id, client_campaign_name,
                 offer_id, offer_name, domain, bundle, comment, distribution_campaign_id, distribution_campaign_name,
                 alias_client_cmp, distribution_campaign_alias):
        self.link_user = link_user
        self.link_keitaro = link_keitaro
        self.user_id = user_id
        self.pixel = pixel
        self.token = token
        self.client_campain_id = client_campain_id
        self.client_campaign_name = client_campaign_name
        self.distribution_campaign_id = distribution_campaign_id
        self.distribution_campaign_name = distribution_campaign_name
        self.offer_id = offer_id
        self.offer_name = offer_name
        self.domain = domain
        self.bundle = bundle
        self.comment = comment
        self.alias_client_cmp = alias_client_cmp
        self.distribution_campaign_alias = distribution_campaign_alias
