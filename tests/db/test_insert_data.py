from src.upbit.api.models import DayCandle, MinuteCandle, WeekCandle, MonthCandle
from src.upbit.api.request import DayCandleRequest, MinuteCandleRequest, WeekCandleRequest, MonthCandleRequest
from src.utils.date import convert_str_date_to_isoformat, get_now_date, diff_date


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


def test_update_current_date(day_candle_repository, quotation_api):

    # 코인 정보가 없는 경우 불러와서 데이터 처리
    current_date = get_now_date()
    if day_candle_repository.is_empty_date(current_date):
        last_date_from_db = day_candle_repository.get_last_date()
        count = diff_date(last_date_from_db, current_date)
        if count > 0:
            candles = quotation_api.get_candles_days(DayCandleRequest(count=count))
            day_candle_repository.add_bulk(candles)