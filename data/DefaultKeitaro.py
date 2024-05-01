from config import API_KEY_KEITARO, KEITARO_CAMPAIGN_ID_APPS_FLOW, KEITARO_CAMPAIGN_GROUP_ID, KEITARO_CAMPAIGN_ID_USERS, \
    KEITARO_DOMAIN_SERVER, KEITARO_CAMPAIGN_ONELINK_ALIAS, KEITARO_OFFER_GROUP_ID, KEITARO_BASE_URL, \
    KEITARO_CAMPAIGN_ID_MAIN_URL, WEBHOOK_URL, KEITARO_WHITE_OFFER, KEITARO_HOST_LINK


class DefaultKeitaro:

    def __init__(self):
        self._webhook_base_url = WEBHOOK_URL
        self._offer_white = KEITARO_WHITE_OFFER
        self._apps_campaign_alias = KEITARO_CAMPAIGN_ONELINK_ALIAS
        self._domain_server = KEITARO_DOMAIN_SERVER
        self._campaign_app_id = KEITARO_CAMPAIGN_ID_APPS_FLOW
        self._group_id_campaign = KEITARO_CAMPAIGN_GROUP_ID
        self._group_id_offer = KEITARO_OFFER_GROUP_ID
        self._base_url = KEITARO_BASE_URL
        self._host_link = KEITARO_HOST_LINK
        self._client_company_id = KEITARO_CAMPAIGN_ID_USERS
        self._onelink_distribution_campaign_id = KEITARO_CAMPAIGN_ID_MAIN_URL
        self._headers = {
            "Accept": "application/json",
            "Api-Key": API_KEY_KEITARO,
            "Content-Type": "application/json"
        }

