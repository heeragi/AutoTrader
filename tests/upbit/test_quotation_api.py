from src.upbit.api.models import DayCandle
from src.upbit.api.request import DayCandleRequest


def test_get_coin_code(quotation_api):
    '''
    GET /v1/market/all
    마켓 코드 조회
    '''
    coin_list = quotation_api.get_coin_codes()
    assert len(coin_list) > 0
    for coin in coin_list:
        print(coin)


def test_get_candles_minutes(quotation_api):
    result = quotation_api.get_candles_minutes(market='KRW-BTC', unit=5)


def test_get_candles_days(quotation_api):
    request = DayCandleRequest(convertingPriceUnit='KRW')
    results = quotation_api.get_candles_days(request)
    for result in results:
        print(DayCandle.model_validate(result))


def test_contextmanager_get_candles_days(quotation_api):
    results = quotation_api.get_candles_days(market='KRW-BTC', count=200)
