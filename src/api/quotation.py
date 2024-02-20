from src.api.base_api import UpbitAPI
from src.api.models import Coin


class QuotationAPI(UpbitAPI):

    def get_coin_codes(self):
        """
        마켓 코드 조회
        :return:
        """
        results = self._call_api('GET', '/v1/market/all?isDetails=true')
        return self._mapping_list(Coin, results)