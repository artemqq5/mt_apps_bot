from typing import List, Dict, Any

from data.repositoryDB.DomainRepository import DomainRepository
from data.repositoryKeitaro.KeitaroDomainRepository import KeitaroDomainRepository


class KeitaroDomainUseCase(KeitaroDomainRepository):

    def __init__(self):
        super().__init__()

    def __get_list_domains(self) -> List[Dict[str, Any]]:
        response = self._get_all_domains()
        if not response:
            return list(dict())
        return response.json()

    def domains_update_db(self):
        counter = 0
        domains = self.__get_list_domains()

        for domain in domains:
            if DomainRepository().add_domain(domain['name'], domain['id']):
                counter += 1

        print(f"domains_update_db | {counter}/{len(domains)} was add")
