import sqlite3
from contextlib import contextmanager
from datetime import datetime, timedelta

import numpy as np
import pytest
import talib
from talib import MA_Type

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
    print(result)




def test_get_candles_days(quotation_api):
    # con = sqlite3.connect('../test.db')
    # cur = con.cursor()

    request = DayCandleRequest()

    results = quotation_api.get_candles_days(request)

    for result in results:
        print(DayCandle.model_validate(result))


    #
    # dataset = []
    #
    # for result in results:
    #     market = result['market']
    #     candle_date = str(datetime.strptime(result['candle_date_time_kst'], "%Y-%m-%dT%H:%M:%S").date())
    #     opening_price = result['opening_price']
    #     high_price = result['high_price']
    #     low_price = result['low_price']
    #     trade_price = result['trade_price']
    #     candle_acc_trade_price = result['candle_acc_trade_price']
    #     candle_acc_trade_volume = result['candle_acc_trade_volume']
    #     prev_closing_price = result['prev_closing_price']
    #     change_price = result['change_price']
    #     change_rate = result['change_rate']
    #
    #     dataset.append(
    #         (
    #             market, candle_date, opening_price, high_price,
    #             low_price, trade_price, candle_acc_trade_price,
    #             candle_acc_trade_volume, prev_closing_price, change_price, change_rate
    #         )
    #     )
    #
    #
    #
    #
    #
    #
    #
    #     # print(
    #     #     f"{result['candle_date_time_kst']} - {result['opening_price']} - {result['high_price']} - {result['low_price']} - {result['trade_price']}"
    #     # )
    # print(dataset)
    # cur.executemany('INSERT INTO day_candle(market, date, opening_price, high_price, low_price, trade_price, candle_acc_trade_price, candle_acc_trade_volume, prev_closing_price, change_price, change_rate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', dataset)
    # con.commit()
    # con.close()
    # def filter_date(candle_date):
    #     standard_date = datetime.now().date() - timedelta(days=14)
    #     candle_date = datetime.strptime(candle_date, "%Y-%m-%dT%H:%M:%S").date()
    #     return standard_date <= candle_date
    #
    #
    #
    # # 현재 날짜 보다 14일 전까지 데이터 추출
    # # print(datetime.now().date() - timedelta(days=14))
    #
    # # results = list(filter(lambda x: filter_date(x['candle_date_time_kst']), results))
    # close = np.array(list(map(lambda x: x['trade_price'], results)))
    #
    # macd = talib.RSI(close)
    #
    # print(macd)

def test_contextmanager_get_candles_days(quotation_api):
    with connection('../test.db') as con:
        cur = con.cursor()
        results = quotation_api.get_candles_days(market='KRW-BTC', count=200)
        print(cur)
