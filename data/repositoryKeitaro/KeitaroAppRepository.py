import json

import requests

from data.DefaultKeitaro import DefaultKeitaro


class KeitaroAppRepository(DefaultKeitaro):

    # При додаванні прілки, створює поток в кампанії Onelink MT AppsLinks (50)
    def create_flow_app(self, flow_url, flow_name, sub30):
        create_flow_url = f"{self._base_url}/streams"
        data = json.dumps({
            "type": "regular",
            "name": flow_name,
            "campaign_id": self._campaign_app_id,
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
            ],
            "triggers": [
                {
                    "condition": "not_respond",
                    "target": "stream",
                    "action": "webhook",
                    "grab_from_page": f"{self._webhook_base_url}/flows?bundle={sub30}",
                    "interval": "1",
                    "reverse": "true",
                    "scan_page": "true"
                }
            ]
        })

        response = requests.post(create_flow_url, data=data, headers=self._headers)
        if not response:
            print(f"create_flow_app {response.text}")

        return response

    def _get_all_apps_flow(self):
        get_all_flows = f"{self._base_url}/campaigns/{self._campaign_app_id}/streams"

        response = requests.get(get_all_flows, headers=self._headers)
        if not response:
            print(f"_get_all_apps_flow {response.text}")
            return None

        return response

    def update_distribution(self, cmp_id, pixel, sub3, bundle):
        update_app = f"{self._base_url}/campaigns/{cmp_id}"
        data = json.dumps({
            "parameters": {
                "keyword": {"name": "keyword", "placeholder": "", "alias": ""},
                "cost": {"placeholder": "", "alias": ""},
                "currency": {"name": "currency", "placeholder": "", "alias": ""},
                "external_id": {"name": "external_id", "placeholder": "", "alias": ""},
                "creative_id": {"name": "creative_id", "placeholder": "", "alias": ""},
                "ad_campaign_id": {"name": "ad_campaign_id", "placeholder": "", "alias": ""},
                "source": {"name": "source", "placeholder": "", "alias": ""},
                "sub_id_1": {"name": "sub1", "placeholder": "{sub1}", "alias": ""},
                "sub_id_2": {"name": "sub2", "placeholder": "{sub2}", "alias": ""},
                "sub_id_3": {"name": "sub3", "placeholder": f"{sub3}", "alias": ""},
                "sub_id_4": {"name": "pixel", "placeholder": f"{pixel}", "alias": ""},
                "sub_id_5": {"name": "fbclid", "placeholder": "", "alias": ""},
                "sub_id_6": {"name": "system_id", "placeholder": f"{self._apps_campaign_alias}", "alias": ""},
                "sub_id_7": {"name": "bundle", "placeholder": f"{bundle}", "alias": ""}
            }
        })

        response = requests.put(update_app, data=data, headers=self._headers)
        if not response:
            print(f"update_distribution_app {response.text}")

        return response
