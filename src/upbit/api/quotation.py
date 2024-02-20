from src.upbit.api.api import UpbitAPIBase
from src.upbit.models import Coin


class QuotationAPI(UpbitAPIBase):

    def get_coin_codes(self) -> list[Coin]:
        """
        마켓 코드 조회
        :return: list[Coin]
        """
        results = self._call_api('GET', '/v1/market/all?isDetails=true')
        return self._mapping_list(Coin, results)