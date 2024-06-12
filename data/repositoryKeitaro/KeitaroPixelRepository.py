import json

import requests

from data.DefaultKeitaro import DefaultKeitaro


class KeitaroPixelRepository(DefaultKeitaro):
    def __init__(self):
        super().__init__()

    def __update_pixel_client(self, cmp_id, pixel, token):
        update_pixel = f"{self._base_url}/campaigns/{cmp_id}"
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
                "sub_id_10": {"name": "fbclid", "placeholder": "{fbclid}", "alias": ""},
                "sub_id_11": {"name": "pixel", "placeholder": pixel, "alias": ""},
                "sub_id_12": {"name": "token", "placeholder": token, "alias": ""},
                "sub_id_13": {"name": "domain", "placeholder": "jombos.com", "alias": ""}
            }
        })

        response = requests.put(update_pixel, data=data, headers=self._headers)
        if not response:
            print(f"update_pixel_client {response.text}")

        return response

    def __update_pixel_distribution(self, cmp_id, pixel, sub3, system_id, bundle):
        update_pixel = f"{self._base_url}/campaigns/{cmp_id}"
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
                "sub_id_7": {"name": "bundle", "placeholder": f"{bundle}", "alias": ""}
            }
        })

        response = requests.put(update_pixel, data=data, headers=self._headers)
        if not response:
            print(f"update_pixel_distribution {response.text}")

        return response

    def update_pixel(self, flow, pixel, token):

        update_client = self.__update_pixel_client(
            cmp_id=flow['client_campaign_id'],
            pixel=pixel,
            token=token
        )

        if not update_client:
            print(f"update pixel (update_pixel_client) | {update_client.text}")
            return

        update_distribution = self.__update_pixel_distribution(
            cmp_id=flow['distribution_campaign_id'],
            pixel=pixel,
            system_id=self._apps_campaign_alias,
            bundle=flow['bundle'],
            sub3=flow['client_alias']
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
