from config import API_KEY_KEITARO, KEITARO_CAMPAIGN_ID_APPS_FLOW, KEITARO_CAMPAIGN_GROUP_ID, KEITARO_CAMPAIGN_ID_USERS, \
    KEITARO_DOMAIN_SERVER, KEITARO_CAMPAIGN_ONELINK_ALIAS, KEITARO_OFFER_GROUP_ID, KEITARO_BASE_URL, \
    KEITARO_CAMPAIGN_ID_MAIN_URL, WEBHOOK_URL, KEITARO_WHITE_OFFER, KEITARO_HOST_LINK
from data.constants.access import DOT_DOMAINS


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

    # Лінка 33 кампанії яка повертається користувачу
    def _generate_client_link(self, client_campaign_alias, pixel, bundle_sub30, domain,
                              distribution_campaign_alias) -> str:
        url = (f"https://{domain}/{distribution_campaign_alias}"
               "?sub1=sub1"
               "&sub2=sub2"
               f"&sub3={client_campaign_alias}"
               "&sub4=sub4"
               "&sub5=sub5"
               "&sub6=sub6"
               "&sub7=sub7"
               "&sub8=sub8"
               "&sub9=sub9"
               "&sub10=sub10"
               f"&pixel={pixel}"
               f"&fbclid=none"
               f"&system_id={self._apps_campaign_alias}"
               f"&bundle={bundle_sub30}"
               f"&domain={str(domain).replace('.', DOT_DOMAINS)}")

        return url
