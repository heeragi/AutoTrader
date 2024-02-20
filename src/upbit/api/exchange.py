from src.upbit.api.api import UpbitAPIBase
from src.upbit.api.models import Account


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

    def get_orders_chance(self, market: str = None):
        if market is None:
            market = 'KRW-BTC'
        parameters = {'market': market}
        results = self._call_api('GET', '/v1/orders/chance', params=parameters)
        return results

    def get_orders(self, market: str = None, state: list = None, page: int = 1, limit: int = 100):

        parameters = {
            'states[]': ['done', 'cancel']
        }

        results = self._call_api('GET', '/v1/orders', params=parameters)

        print(results)

        return results
