from src.upbit.api.api import UpbitAPIBase
from src.upbit.models import Account


class ExchangeAPI(UpbitAPIBase):
    def __init__(self):
        super().__init__()

    def get_accounts(self):
        """
        계좌 정보 조회
        :return:
        """
        results = self._call_api('GET', '/v1/accounts')
        return self._mapping_list(Account, results)
