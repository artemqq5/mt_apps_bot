import json

import requests

from data.DefaultKeitaroRepository import DefaultKeitaroRepository


class KeitaroLinkRepository(DefaultKeitaroRepository):

    # Клонує кампанію по шаблону з Keitaro Client Company (36)
    def _clone_campaign(self):
        clone_campaign_url = f"https://{self._domain_server}/admin_api/v1/campaigns/{self._clone_camoaign_id}/clone"

        response = requests.post(clone_campaign_url, headers=self._headers)
        if not response:
            print(f"error clone_campaign {response.text}")

        return response

    # Створюємо оффер під лінку юзера (name, group, offer_link_from_user)
    def _create_offer(self, name, offer_url):
        create_offer_url = f"https://{self._domain_server}/admin_api/v1/offers"
        data = json.dumps({
            "name": name, "group_id": self._group_id, "action_payload": offer_url, "action_type": "http",
            "offer_type": "external", "payout_auto": "true", "payout_type": "CPA", "payout_upsell": "true",
            "payout_currency": "USD"
        })

        response = requests.post(create_offer_url, data=data, headers=self._headers)
        if not response:
            print(f"error create_offer {response.text}")

        return response

    # Оновлюємо клоновану кампанію (name, grop)
    def _update_campaign(self, campaign_id, name, pixel, token):
        update_campaign_url = f"https://{self._domain_server}/admin_api/v1/campaigns/{campaign_id}"
        data = json.dumps({
            "name": name,
            "group_id": self._group_id,
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

        response = requests.put(update_campaign_url, data=data, headers=self._headers)
        if not response:
            print(f"update_campaign_name {response.text}")

        return response

    # Оновлюємо оффер в потоку клонованої кампанії на той що ми створили (flow_id, offer_id)
    def _update_flow_offer(self, flow_id, offer_id):
        update_flow_url = f"https://{self._domain_server}/admin_api/v1/streams/{flow_id}"
        data = json.dumps({"offers": [{"offer_id": offer_id, "share": "100"}]})

        response = requests.put(update_flow_url, data=data, headers=self._headers)
        if not response:
            print(f"error update_flow_offer {response.text}")

        return response

    # Лінка яка повертається користувачу
    def _generate_client_link(self, user_campaign_alias, pixel, bundle_sub30):
        url = (f"https://{self._domain_server}/1qscFm61"
               "?sub1={sub1}"
               "&sub2={sub2}"
               f"&sub3={user_campaign_alias}"
               f"&pixel={pixel}"
               f"&system_id={self._onelink_campaign_alias}"
               f"&bundle={bundle_sub30}")

        return url

    @staticmethod
    def _generate_campaign_name(user_id, team_id, team_name, offer_id) -> str:
        return f"{user_id} | {team_name} #{team_id} | offer #{offer_id}"

    @staticmethod
    def _generate_offer_name(user_id, team_id, team_name, campaign_id) -> str:
        return f"{user_id} | {team_name} #{team_id} | campaign #{campaign_id}"

    # Повна генерація:
    # Клонування кампанії | Keitaro Client Company (36)
    # Створюємо оффер під лінку юзера
    # Оновлюємо клоновану кампанію
    # Оновлюємо оффер в потоку клонованої кампанії на той що ми створили
    # Повертаємо користувачу лінку з 33 кампанії з підставленими параметрами усіх попередніх генерацій
    def generate_link_keitaro(self, data, access) -> str | None:
        clone_campaign = self._clone_campaign()

        if not clone_campaign:
            print(f"generate_link_keitaro (clone_campaign) | {clone_campaign.text}")
            return

        create_offer = self._create_offer(
            offer_url=data['offer_link'],
            name=KeitaroLinkRepository._generate_offer_name(
                user_id=access['user_id'],
                team_id=access['team_id'],
                team_name=access['team_name'],
                campaign_id=clone_campaign.json()[0]['id']
            )
        )

        if not create_offer:
            print(f"generate_link_keitaro (create_offer) | {create_offer.text}")
            return

        update_campaign = self._update_campaign(
            campaign_id=clone_campaign.json()[0]['id'],
            name=KeitaroLinkRepository._generate_campaign_name(
                user_id=access['user_id'],
                team_id=access['team_id'],
                team_name=access['team_name'],
                offer_id=create_offer.json()['id']
            ),
            pixel=data['pixel'],
            token=data['token']
        )

        if not update_campaign:
            print(f"generate_link_keitaro (update_campaign) | {update_campaign.text}")
            return

        update_flow = self._update_flow_offer(
            flow_id=update_campaign.json()['streams'][0]['id'],
            offer_id=create_offer.json()['id']
        )

        if not update_flow:
            print(f"generate_link_keitaro (update_offer) | {update_flow.text}")
            return

        generate_client_link = self._generate_client_link(
            user_campaign_alias=update_campaign.json()['alias'],
            pixel=data['pixel'],
            bundle_sub30=data['bundle']
        )

        if not create_offer:
            print(f"generate_link_keitaro (generate_client_link) | {generate_client_link.text}")
            return

        return generate_client_link
