from typing import List, Dict, Any

from data.constants.access import BANNED_APP_STATUS
from data.repositoryDB.AppRepository import AppRepository
from data.repositoryKeitaro.KeitaroAppRepository import KeitaroAppRepository


class KeitaroAppUseCase(KeitaroAppRepository):

    def __init__(self):
        super().__init__()

    def __get_list_flows(self) -> List[Dict[str, Any]]:
        response = self._get_all_apps_flow()
        if not response:
            return list(dict())
        return response.json()

    def check_available_apps(self):
        counter = 0
        flows = self.__get_list_flows()
        flows_id = [flow['id'] for flow in flows]

        for app in AppRepository().get_all_apps():
            if app['id'] not in flows_id:
                if AppRepository().delete_app_by_id(app['id']):
                    counter += 1

        print(f"check_available_apps | {counter}/{len(flows)} was banned")
