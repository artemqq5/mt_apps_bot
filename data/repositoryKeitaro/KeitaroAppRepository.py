import json

import requests

from data.DefaultKeitaro import DefaultKeitaro


class KeitaroApp(DefaultKeitaro):

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
            ]
        })

        response = requests.post(create_flow_url, data=data, headers=self._headers)
        if not response:
            print(f"create_flow_app {response.text}")

        return response
