import json

import requests

from config import API_KEY_KEITARO, KEITARO_CAMPAIGN_ID_APPS_FLOW, KEITARO_GROUP_ID, KEITARO_CAMPAIGN_ID_USERS, \
    KEITARO_DOMAIN_SERVER, KEITARO_CAMPAIGN_ONELINK_ALIAS


class DefaultKeitaroRepository:

    def __init__(self):
        self._onelink_campaign_alias = KEITARO_CAMPAIGN_ONELINK_ALIAS
        self._domain_server = KEITARO_DOMAIN_SERVER
        self._campaign_app_id = KEITARO_CAMPAIGN_ID_APPS_FLOW
        self._group_id = KEITARO_GROUP_ID
        self._clone_camoaign_id = KEITARO_CAMPAIGN_ID_USERS
        self._headers = {
            "Accept": "application/json",
            "Api-Key": API_KEY_KEITARO,
            "Content-Type": "application/json"
        }

