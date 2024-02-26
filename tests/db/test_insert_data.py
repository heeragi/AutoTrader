import sqlite3
from contextlib import contextmanager
from datetime import datetime

from src.database.day_candle_repo import DayCandleRepository
from src.upbit.api.models import DayCandle
from src.upbit.api.request import DayCandleRequest
from src.utils.date import convert_str_date_to_isoformat


def test_insert_day_candle_data(day_candle_repository, quotation_api):
    """
    KRW-BTC 데이터 삽입
    :param quotation_api:
    :return:
    """
    last_candle_dates = [
        '2023-01-23 00:00:00',
        '2022-07-07 00:00:00',
        '2021-12-19 00:00:00',
        '2021-06-02 00:00:00',
        '2020-11-14 00:00:00',
        '2020-04-28 00:00:00',
        '2019-10-11 00:00:00',
        '2019-03-25 00:00:00',
        '2018-09-06 00:00:00',
        '2018-02-18 00:00:00',
        '2017-09-25 00:00:00',
    ]

    for last_candle_date in last_candle_dates:
        request = DayCandleRequest(to=last_candle_date)
        results = quotation_api.get_candles_days(request)
        if len(results) == 0:
            break
        candles = [DayCandle.model_validate(result) for result in results]
        if len(candles) == 0:
            break
        day_candle_repository.add_bulk(candles)


    # def get_candle_date(request: DayCandleRequest):
    #     results = quotation_api.get_candles_days(request)
    #     if len(results) == 0:
    #         return None
    #     candles = [DayCandle.model_validate(result) for result in results]
    #     if len(candles) == 0:
    #         return None
    #     day_candle_repository.add_bulk(candles)
    #     last_candle_date = convert_str_date_to_isoformat(candles.pop().candle_date_time_kst)
    #     return get_candle_date(DayCandleRequest(to=last_candle_date))
    # get_candle_date(DayCandleRequest())
