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
        """
        주문 가능 정보 조회
        :param market: 마켓 코드
        :return:
        """
        if market is None:
            market = 'KRW-BTC'
        parameters = {'market': market}
        results = self._call_api('GET', '/v1/orders/chance', params=parameters)
        return results

    def get_orders(self, market: str = None, state: list = None, page: int = 1, limit: int = 100):
        """
        주문 리스트 조회
        :param market:
        :param state:
        :param page:
        :param limit:
        :return:
        """
        parameters = {
            'states[]': ['done', 'cancel']
        }

        results = self._call_api('GET', '/v1/orders', params=parameters)
        return results

    def post_order(self, market: str, side: str, volume: float, price: float, order_type: str):
        parameters = {
            'market': market,
            'side': side,
            'volume': f'{float}',
            'price': f'{price}',
            'ord_type': order_type
        }
        results = self._call_api('POST', '/v1/orders', params=parameters)
        return results

    def delete_order(self, uuid: str):
        """ 주문 취소 """
        parameters = {'uuid': uuid}
        results = self._call_api('DELETE', '/v1/order', params=parameters)
        return results
