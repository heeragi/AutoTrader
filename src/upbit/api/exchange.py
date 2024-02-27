from src.upbit.api.api import UpbitAPIBase
from src.upbit.api.models import Account
from src.upbit.api.request import OrderListRequest, PostOrderRequest
from src.upbit.api.response import OrderChance, OrderHistory


class ExchangeAPI(UpbitAPIBase):

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
        result = self._call_api('GET', '/v1/orders/chance', params=parameters)
        return OrderChance.model_validate(result)

    def get_orders(self, request: OrderListRequest):
        """
        주문 리스트 조회
        :return:
        """
        results = self._call_api('GET', '/v1/orders', params=request.dict())
        return self._mapping_list(OrderHistory, results)

    def post_order(self, request: PostOrderRequest):
        result = self._call_api('POST', '/v1/orders', params=request.dict())
        return OrderHistory.model_validate(result)

    def delete_order(self, uuid: str):
        """ 주문 취소 """
        parameters = {'uuid': uuid}
        results = self._call_api('DELETE', '/v1/order', params=parameters)
        return results
