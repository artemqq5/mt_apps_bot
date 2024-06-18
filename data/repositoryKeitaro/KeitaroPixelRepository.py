import json

import requests

from config import KEITARO_ROTATOR_CAMPAIGN_GROUP_ID, KEITARO_CLIENT_CAMPAIGN_GROUP_ID
from data.DefaultKeitaro import DefaultKeitaro
from data.constants.access import DOT_DOMAINS


class KeitaroPixelRepository(DefaultKeitaro):
    def __init__(self):
        super().__init__()

    def _update_campaign_client(self, campaign_id, pixel, token, team):
        update_campaign_url = f"{self._base_url}/campaigns/{campaign_id}"
        data = json.dumps({
            "parameters": {
                "keyword": {"name": "keyword", "placeholder": "", "alias": ""},
                "cost": {"name": "cost", "placeholder": "", "alias": ""},
                "currency": {"name": "currency", "placeholder": "", "alias": ""},
                "external_id": {"name": "external_id", "placeholder": "", "alias": ""},
                "creative_id": {"name": "creative_id", "placeholder": "", "alias": ""},
                "ad_campaign_id": {"name": "ad_campaign_id", "placeholder": "", "alias": ""},
                "source": {"name": "source", "placeholder": "", "alias": ""},
                "sub_id_1": {"name": "sub1", "placeholder": "{sub1}", "alias": ""},
                "sub_id_2": {"name": "sub2", "placeholder": "{sub2}", "alias": ""},
                "sub_id_3": {"name": "sub4", "placeholder": "{sub4}", "alias": ""},
                "sub_id_4": {"name": "sub5", "placeholder": "{sub5}", "alias": ""},
                "sub_id_5": {"name": "sub6", "placeholder": "{sub6}", "alias": ""},
                "sub_id_6": {"name": "sub7", "placeholder": "{sub7}", "alias": ""},
                "sub_id_7": {"name": "sub8", "placeholder": "{sub8}", "alias": ""},
                "sub_id_8": {"name": "sub9", "placeholder": "{sub9}", "alias": ""},
                "sub_id_9": {"name": "sub10", "placeholder": "{sub10}", "alias": ""},
                "sub_id_10": {"name": "fbclid", "placeholder": "{fbclid}", "alias": ""},
                "sub_id_11": {"name": "pixel", "placeholder": pixel, "alias": ""},
                "sub_id_12": {"name": "token", "placeholder": token, "alias": ""},
                "sub_id_13": {"name": "domain", "placeholder": "jombos.com", "alias": ""},
                "sub_id_14": {"name": "timnameidfilter", "placeholder": f"{team}", "alias": ""}
            }
        })

        response = requests.put(update_campaign_url, data=data, headers=self._headers)
        if not response:
            print(f"update_campaign_name {response.text}")

        return response

    # Оновлюємо клоновану кампанію onelink distribution 33
    def _update_campaign_distribution_pixel(self, campaign_id, pixel, system_id, sub3, bundle, domain):
        update_campaign_url = f"{self._base_url}/campaigns/{campaign_id}"
        domain = str(domain).replace(".", DOT_DOMAINS)
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
                "sub_id_6": {"name": "system_id", "placeholder": f"{system_id}", "alias": ""},
                "sub_id_7": {"name": "bundle", "placeholder": f"{bundle}", "alias": ""},
                "sub_id_8": {"name": "sub4", "placeholder": "{sub4}", "alias": ""},
                "sub_id_9": {"name": "sub5", "placeholder": "{sub5}", "alias": ""},
                "sub_id_10": {"name": "sub6", "placeholder": "{sub6}", "alias": ""},
                "sub_id_11": {"name": "sub7", "placeholder": "{sub7}", "alias": ""},
                "sub_id_12": {"name": "sub8", "placeholder": "{sub8}", "alias": ""},
                "sub_id_13": {"name": "sub9", "placeholder": "{sub9}", "alias": ""},
                "sub_id_14": {"name": "sub10", "placeholder": "{sub10}", "alias": ""},
                "sub_id_15": {"name": "domain", "placeholder": f"{domain}", "alias": ""}
            }
        })

        response = requests.put(update_campaign_url, data=data, headers=self._headers)
        if not response:
            print(f"update_campaign_name {response.text}")

        return response

    def update_pixel(self, flow, pixel, token):

        update_client = self._update_campaign_client(
            campaign_id=flow['client_campaign_id'],
            team=flow['timnameidfilter'],
            pixel=pixel,
            token=token
        )

        if not update_client:
            print(f"update pixel (update_pixel_client) | {update_client.text}")
            return

        update_distribution = self._update_campaign_distribution_pixel(
            campaign_id=flow['distribution_campaign_id'],
            pixel=pixel,
            system_id=self._apps_campaign_alias,
            sub3=flow['client_alias'],
            bundle=flow['bundle'],
            domain=flow['domain']
        )

        if not update_distribution:
            print(f"update pixel (update_distribution) | {update_distribution.text}")
            return

        return self._generate_client_link(
            client_campaign_alias=flow['client_alias'],
            pixel=pixel,
            bundle_sub30=flow['bundle'],
            domain=flow['domain'],
            distribution_campaign_alias=flow['distribution_alias']
        )
