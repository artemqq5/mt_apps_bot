import json

import requests

from config import KEITARO_CLIENT_CAMPAIGN_GROUP_ID, KEITARO_ROTATOR_CAMPAIGN_GROUP_ID
from data.DefaultKeitaro import DefaultKeitaro
from data.constants.access import DOT_DOMAINS
from data.repositoryKeitaro.model.KeitaroLinkResponse import KeitaroLinkResponse


class KeitaroLink(DefaultKeitaro):

    # Клонує кампанію по шаблону
    def _clone_campaign(self, campaign):
        clone_campaign_url = f"{self._base_url}/campaigns/{campaign}/clone"

        response = requests.post(clone_campaign_url, headers=self._headers)
        if not response:
            print(f"error clone_campaign {response.text}")

        return response

    # Створюємо оффер під лінку юзера (name, group, offer_link_from_user)
    def _create_offer(self, name, offer_url):
        create_offer_url = f"{self._base_url}/offers"
        data = json.dumps({
            "name": name, "group_id": self._group_id_offer, "action_payload": offer_url, "action_type": "http",
            "offer_type": "external", "payout_auto": "true", "payout_type": "CPA", "payout_upsell": "true",
            "payout_currency": "USD"
        })

        response = requests.post(create_offer_url, data=data, headers=self._headers)
        if not response:
            print(f"error create_offer {response.text}")

        return response

    # Оновлюємо клоновану кампанію для клієнта 36
    def _update_campaign_client(self, campaign_id, name, pixel, token, team):
        update_campaign_url = f"{self._base_url}/campaigns/{campaign_id}"
        data = json.dumps({
            "name": name,
            "group_id": KEITARO_CLIENT_CAMPAIGN_GROUP_ID,
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
    def _update_campaign_distribution(self, campaign_id, name, pixel, system_id, sub3, bundle, domain_id, domain):
        update_campaign_url = f"{self._base_url}/campaigns/{campaign_id}"
        domain = str(domain).replace(".", DOT_DOMAINS)
        data = json.dumps({
            "name": name,
            "group_id": KEITARO_ROTATOR_CAMPAIGN_GROUP_ID,
            "domain_id": domain_id,
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
                "sub_id_5": {"name": "fbclid", "placeholder": "", "alias": ""},
                "sub_id_6": {"name": "system_id", "placeholder": f"{system_id}", "alias": ""},
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

        response = requests.put(update_campaign_url, data=data, headers=self._headers)
        if not response:
            print(f"update_campaign_name {response.text}")

        return response

    # Оновлюємо оффер в потоку клонованої кампанії на той що ми створили (flow_id, offer_id)
    def _update_flow_offer(self, flow_id, offer_id):
        update_flow_url = f"{self._base_url}/streams/{flow_id}"
        data = json.dumps({"offers": [{"offer_id": offer_id, "share": "100"}]})

        response = requests.put(update_flow_url, data=data, headers=self._headers)
        if not response:
            print(f"error update_flow_offer {response.text}")

        return response

    @staticmethod
    def _generate_campaign_client_name(user_id, team_id, team_name, offer_id) -> str:
        return f"{user_id} | {team_name} #{team_id} | offer #{offer_id}"

    @staticmethod
    def _generate_campaign_distribution_name(team_name, team_id, campaign_clent_id) -> str:
        return f"{team_name} #{team_id} | campaign client #{campaign_clent_id}"

    @staticmethod
    def _generate_offer_name(user_id, team_id, team_name, campaign_id) -> str:
        return f"{user_id} | {team_name} #{team_id} | campaign #{campaign_id}"

    # Повна генерація:
    # Клонування кампанії для клієнта | Keitaro Client Company (36)
    # Клонування кампанії для onelink distribution | MT Onelink Distribution (33)
    # Оновлюємо назву, параметри і домен в клонованій кампанії onelink distribution
    # Створюємо оффер під лінку юзера
    # Оновлюємо клоновану під юзера кампанію
    # Оновлюємо оффер в потоку клонованої кампанії під юзера, на той оффер, що ми створили
    # Повертаємо користувачу url клонованої 33 кампанії
    def generate_link_keitaro(self, data, access, team_unq) -> KeitaroLinkResponse | None:
        clone_campaign_client = self._clone_campaign(self._client_company_id)

        if not clone_campaign_client:
            print(f"generate_link_keitaro (clone_campaign_client) | {clone_campaign_client.text}")
            return

        clone_campaign_distribution = self._clone_campaign(self._onelink_distribution_campaign_id)

        if not clone_campaign_distribution:
            print(f"generate_link_keitaro (clone_campaign_distribution) | {clone_campaign_distribution.text}")
            return

        update_campaign_distribution = self._update_campaign_distribution(
            campaign_id=clone_campaign_distribution.json()[0]['id'],
            name=KeitaroLink._generate_campaign_distribution_name(
                team_name=access['team_name'],
                team_id=access['team_id'],
                campaign_clent_id=clone_campaign_client.json()[0]['id']
            ),
            pixel=data['pixel'],
            system_id=self._apps_campaign_alias,
            sub3=clone_campaign_client.json()[0]['alias'],
            bundle=data['bundle'],
            domain_id=data['domain_id'],
            domain=data['domain']
        )

        if not update_campaign_distribution:
            print(f"generate_link_keitaro (update_campaign_distribution) | {update_campaign_distribution.text}")
            return

        create_offer = self._create_offer(
            offer_url=data['offer_link'],
            name=KeitaroLink._generate_offer_name(
                user_id=access['user_id'],
                team_id=access['team_id'],
                team_name=access['team_name'],
                campaign_id=clone_campaign_client.json()[0]['id']
            )
        )

        if not create_offer:
            print(f"generate_link_keitaro (create_offer) | {create_offer.text}")
            return

        update_campaign_client = self._update_campaign_client(
            campaign_id=clone_campaign_client.json()[0]['id'],
            name=KeitaroLink._generate_campaign_client_name(
                user_id=access['user_id'],
                team_id=access['team_id'],
                team_name=access['team_name'],
                offer_id=create_offer.json()['id']
            ),
            team=team_unq,
            pixel=data['pixel'],
            token=data['token']
        )

        if not update_campaign_client:
            print(f"generate_link_keitaro (update_campaign_client) | {update_campaign_client.text}")
            return

        update_flow = self._update_flow_offer(
            flow_id=update_campaign_client.json()['streams'][0]['id'],
            offer_id=create_offer.json()['id']
        )

        if not update_flow:
            print(f"generate_link_keitaro (update_offer) | {update_flow.text}")
            return

        generate_client_link = self._generate_client_link(
            client_campaign_alias=update_campaign_client.json()['alias'],
            pixel=data['pixel'],
            bundle_sub30=data['bundle'],
            domain=data['domain'],
            distribution_campaign_alias=update_campaign_distribution.json()['alias']
        )

        return KeitaroLinkResponse(
            link_user=data['offer_link'],
            link_keitaro=generate_client_link,
            user_id=access['user_id'],
            pixel=data['pixel'],
            token=data['token'],
            client_campain_id=update_campaign_client.json()['id'],
            client_campaign_name=update_campaign_client.json()['name'],
            distribution_campaign_id=update_campaign_distribution.json()['id'],
            distribution_campaign_name=update_campaign_distribution.json()['name'],
            offer_id=create_offer.json()['id'],
            offer_name=create_offer.json()['name'],
            domain=data['domain'],
            bundle=data['bundle'],
            comment=data.get('comment', None),
            alias_client_cmp=update_campaign_client.json()['alias'],
            distribution_campaign_alias=update_campaign_distribution.json()['alias']
        )
