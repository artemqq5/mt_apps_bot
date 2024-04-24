import requests

from data.DefaultKeitaro import DefaultKeitaro


class KeitaroDomainRepository(DefaultKeitaro):

    def __init__(self):
        super().__init__()

    def _get_all_domains(self):
        clone_campaign_url = f"{self._base_url}/domains"

        response = requests.get(clone_campaign_url, headers=self._headers)
        if not response:
            print(f"get_all_domains {response.text}")
            return None

        return response

