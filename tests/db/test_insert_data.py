from src.upbit.api.models import DayCandle, MinuteCandle, WeekCandle, MonthCandle
from src.upbit.api.request import DayCandleRequest, MinuteCandleRequest, WeekCandleRequest, MonthCandleRequest
from src.utils.date import convert_str_date_to_isoformat


def test_insert_day_candle_data(day_candle_repository, quotation_api):
    """
    KRW-BTC 데이터 삽입
    :param quotation_api:
    :return:
    """
    def get_candle_date(request: DayCandleRequest):
        results = quotation_api.get_candles_days(request)
        if len(results) == 0:
            return None
        candles = [DayCandle.model_validate(result) for result in results]
        if len(candles) == 0:
            return None
        day_candle_repository.add_bulk(candles)
        last_candle_date = convert_str_date_to_isoformat(candles.pop().candle_date_time_kst)
        print(last_candle_date)
        return get_candle_date(DayCandleRequest(to=last_candle_date))
    get_candle_date(DayCandleRequest())
