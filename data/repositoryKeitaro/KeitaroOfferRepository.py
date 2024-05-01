import json

import requests

from data.DefaultKeitaro import DefaultKeitaro


class KeitaroOfferRepository(DefaultKeitaro):

    def __init__(self):
        super().__init__()

    def update_offer_url(self, offer_id: str, url: str):
        update_url = f"{self._base_url}/offers/{offer_id}"
        data = json.dumps({"action_payload": url})

        response = requests.put(update_url, data=data, headers=self._headers)
        if not response:
            print(f"update_offer_url {response.text}")

        return response
