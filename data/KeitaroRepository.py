import json

import requests

from config import API_KEY_KEITARO, KEITARO_CAMPAIGN_ID_APPS_FLOW, KEITARO_GROUP_ID, KEITARO_CAMPAIGN_ID_USERS


class KeitaroRepository:

    def __init__(self):
        self.campaign_app_id = KEITARO_CAMPAIGN_ID_APPS_FLOW
        self.group_id = KEITARO_GROUP_ID
        self.clone_camoaign_id = KEITARO_CAMPAIGN_ID_USERS
        self.headers = {
            "Accept": "application/json",
            "Api-Key": API_KEY_KEITARO,
            "Content-Type": "application/json"
        }

    def create_offer(self, name, offer_url):
        create_offer_url = "https://hotlab.site/admin_api/v1/offer"
        data = {"name": name, "group_id": self.group_id, "action_payload": offer_url, "action_type": "http",
                "offer_type": "external", "payout_auto": "true", "payout_type": "CPA",
                "payout_upsell": "true", "payout_currency": "USD"}

        response = requests.post(create_offer_url, data=data, headers=self.headers)
        if not response:
            print(f"error create_offer {response.text}")

        return response

    def clone_campaign(self):
        clone_campaign_url = f"https://hotlab.site/admin_api/v1/campaigns/{self.clone_camoaign_id}/clone"

        response = requests.post(clone_campaign_url, headers=self.headers)
        if not response:
            print(f"error clone_campaign {response.text}")

        return response

    def update_campaign_name(self, campaign_id, name):
        update_campaign_url = f"https://hotlab.site/admin_api/v1/campaigns/{campaign_id}"
        data = {"name": name, "group_id": self.group_id}

        response = requests.put(update_campaign_url, data=data, headers=self.headers)
        if not response:
            print(f"update_campaign_name {response.text}")

        return response

    def update_flow_offer(self, flow_id, offer_id):
        update_flow_url = f"https://hotlab.site/admin_api/v1/streams/{flow_id}"
        data = {"offers": [{"offer_id": offer_id, "share": "100"}]}

        response = requests.put(update_flow_url, data=data, headers=self.headers)
        if not response:
            print(f"error update_flow_offer {response.text}")

        return response

    def create_flow_app(self, flow_url, flow_name, sub30):
        create_flow_url = "https://hotlab.site/admin_api/v1/streams"
        data = json.dumps({
            "type": "regular",
            "name": flow_name,
            "campaign_id": self.campaign_app_id,
            "action_type": "http",
            "action_payload": flow_url,
            "schema": "redirect",
            "collect_clicks": "true",
            "filter_or": "false",
            "weight": "100",
            "offer_selection": "after_click",
            "filters": [
                {
                    "name": "sub_id_30",
                    "mode": "accept",
                    "payload": [
                        sub30
                    ]
                }
            ]
        })

        response = requests.post(create_flow_url, data=data, headers=self.headers)
        if not response:
            print(f"create_flow_app {response.text}")

        return response
