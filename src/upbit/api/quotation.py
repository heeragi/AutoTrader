from src.upbit.api.api import UpbitAPIBase
from src.upbit.api.models import Coin
from src.upbit.api.request import DayCandleRequest


class QuotationAPI(UpbitAPIBase):

    def get_coin_codes(self) -> list[Coin]:
        """
        마켓 코드 조회
        :return: list[Coin]
        """
        results = self._call_api('GET', '/v1/market/all?isDetails=true')

        # 국내장 현물만 가져오기
        results = list(filter(lambda x: x['market'].startswith('KRW-'), results))

        return self._mapping_list(Coin, results)

    def get_candles_minutes(self, market: str, unit: int, to: str = None, count: int = 1):
        """
        분봉 캔들
        :param market:
        :param unit:
        :param to:
        :param count:
        :return:
        """
        path = f'/v1/candles/minutes/{unit}?market={market}&count={count}'
        return self._call_api('GET', path)

    def get_candles_days(self, request: DayCandleRequest):
        """
        일봉 캔들
        :param request: DayCandleRequest
        :return:
        """
        path = f'/v1/candles/days?{self._create_querystring(request)}'
        return self._call_api('GET', path)

    def get_candles_weeks(self, market: str, count: int):
        """
        주봉 캔들
        :param market:
        :param count:
        :return:
        """
        path = f'/v1/candles/weeks?market={market}&count={count}'
        return self._call_api('GET', path)

    def get_candles_months(self, market: str, count: int):
        """
        월봉 캔들
        :param market:
        :param count:
        :return:
        """
        path = f'/v1/candles/months?market={market}&count={count}'
        return self._call_api('GET', path)

    def get_trades_ticks(self, market: str, count: int):
        path = f'/v1/trades/ticks?market={market}&count={count}'
        return self._call_api('GET', path)