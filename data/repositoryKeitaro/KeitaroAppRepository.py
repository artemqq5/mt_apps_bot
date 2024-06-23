import json
import uuid

import requests

from config import WEBHOOK_PASSWORD
from data.DefaultKeitaro import DefaultKeitaro
from data.constants.access import DOT_DOMAINS
from data.repositoryKeitaro.model.KeitaroAppResponse import KeitaroAppResponse


class KeitaroAppRepository(DefaultKeitaro):

    # При додаванні прілки, створює поток в кампанії Onelink MT AppsLinks (50)
    def __create_flow_app(self, flow_url, flow_name, sub30):
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
                    "grab_from_page": f"{self._webhook_base_url}/flows?bundle={sub30}&key={WEBHOOK_PASSWORD}",
                    "interval": "5",
                    "reverse": "true",
                    "scan_page": "true"
                }
            ]
        })

        response = requests.post(create_flow_url, data=data, headers=self._headers)
        if not response:
            print(f"create_flow_app {response.text}")

        return response

    def __create_organic_campaign_app(self, campaign_name, alias_organic):
        create_organic_cmp = f"{self._base_url}/campaigns"
        data = json.dumps({
            "alias": alias_organic,
            "name": campaign_name,
            "group_id": self._group_id_campaign,
            "uniqueness_method": "ip_ua",
            "cost_auto": True
        })

        response = requests.post(create_organic_cmp, data=data, headers=self._headers)
        if not response:
            print(f"create_flow_app {response.text}")

        return response

    def __create_white_flow(self, cmp_id):
        create_white = f"{self._base_url}/streams"
        data = json.dumps({
            "campaign_id": cmp_id,
            "type": "regular",
            "name": "White",
            "action_type": "http",
            "schema": "landings",
            "offers": [{"offer_id": self._offer_white, "share": "100"}]
        })

        response = requests.post(create_white, data=data, headers=self._headers)
        if not response:
            print(f"create_white {response.text}")

        return response

    def upload_app_keitaro(self, flow_url, flow_name, bundle, app_name) -> KeitaroAppResponse | None:
        create_flow_app = self.__create_flow_app(flow_url, flow_name, sub30=bundle)

        if not create_flow_app:
            print(f"create app keitaro (create_flow_app) | {create_flow_app.text}")
            return

        create_organic_campaign = self.__create_organic_campaign_app(f"Organic | {app_name}", bundle)

        if not create_organic_campaign:
            print(f"create app keitaro (create_organic_app) | {create_organic_campaign.text}")
            return

        add_white = self.__create_white_flow(create_organic_campaign.json()['id'])

        if not add_white:
            print(f"create app keitaro (add_white) | {add_white.text}")
            return

        return KeitaroAppResponse(
            flow_app_id=create_flow_app.json()['id'],
            organic_campaign_id=create_organic_campaign.json()['id'],
            organic_campaign_name=create_organic_campaign.json()['name'],
            link_keitaro=f"{self._host_link}/admin/#!/campaigns/{create_organic_campaign.json()['id']}"
        )

    def _get_all_apps_flow(self):
        get_all_flows = f"{self._base_url}/campaigns/{self._campaign_app_id}/streams"

        response = requests.get(get_all_flows, headers=self._headers)
        if not response:
            print(f"_get_all_apps_flow {response.text}")
            return None

        return response

    def update_distribution_app(self, flow, app):
        cmp_id = flow['distribution_campaign_id']
        pixel = flow['pixel_fb']
        sub3 = flow['client_alias']
        bundle = app['bundle']

        domain = str(flow['domain']).replace(".", DOT_DOMAINS)

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
                "sub_id_1": {"name": "sub1", "placeholder": "sub1", "alias": ""},
                "sub_id_2": {"name": "sub2", "placeholder": "sub2", "alias": ""},
                "sub_id_3": {"name": "sub3", "placeholder": f"{sub3}", "alias": ""},
                "sub_id_4": {"name": "pixel", "placeholder": f"{pixel}", "alias": ""},
                "sub_id_5": {"name": "fbclid", "placeholder": "none", "alias": ""},
                "sub_id_6": {"name": "system_id", "placeholder": f"{self._apps_campaign_alias}", "alias": ""},
                "sub_id_7": {"name": "bundle", "placeholder": f"{bundle}", "alias": ""},
                "sub_id_8": {"name": "sub4", "placeholder": "sub4", "alias": ""},
                "sub_id_9": {"name": "sub5", "placeholder": "sub5", "alias": ""},
                "sub_id_10": {"name": "sub6", "placeholder": "sub6", "alias": ""},
                "sub_id_11": {"name": "sub7", "placeholder": "sub7", "alias": ""},
                "sub_id_12": {"name": "sub8", "placeholder": "sub8", "alias": ""},
                "sub_id_13": {"name": "sub9", "placeholder": "sub9", "alias": ""},
                "sub_id_14": {"name": "sub10", "placeholder": "sub10", "alias": ""},
                "sub_id_15": {"name": "domain", "placeholder": f"{domain}", "alias": ""}
            }
        })

        response = requests.put(update_app, data=data, headers=self._headers)
        if not response:
            print(f"update_distribution_app {response.text}")
            return

        print(flow['client_campaign_id'])
        return self._generate_client_link(
            client_campaign_alias=flow['client_alias'],
            pixel=pixel,
            bundle_sub30=bundle,
            domain=flow['domain'],
            distribution_campaign_alias=flow['distribution_alias']
        )
