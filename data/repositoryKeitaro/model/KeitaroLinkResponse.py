class KeitaroLinkResponse:
    def __init__(self, link_user, link_keitaro, user_id, pixel, token, campain_id, campaign_name, offer_id, offer_name,
                 domain, bundle, comment):
        self.link_user = link_user
        self.link_keitaro = link_keitaro
        self.user_id = user_id
        self.pixel = pixel
        self.token = token
        self.campain_id = campain_id
        self.campaign_name = campaign_name
        self.offer_id = offer_id
        self.offer_name = offer_name
        self.domain = domain
        self.bundle = bundle
        self.comment = comment
