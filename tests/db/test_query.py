from datetime import datetime

import numpy as np
import pandas as pd
import talib

import pandas_ta

from src.database.day_candle_repo import DayCandleRepository


def test_query(day_candle_repository):
    print(day_candle_repository.get_list_from_date('2024-02-27', '2024-02-28'))


def test_query_with_ta(day_candle_repository):
    candles = day_candle_repository.get_all()

    close = np.asarray([candle[6] for candle in candles], dtype='f8')

    df = pd.DataFrame({'close': close})

    print(df.ta.ema(length=5))
    print(df.ta.ema(length=10))
    print(df.ta.ema(length=20))
    print(df.ta.ema(length=50))


def test_is_empty_date(day_candle_repository):
    print(str(datetime.now().date()))
    print(day_candle_repository.is_empty_date('2024-02-27'))

def test_get_date(day_candle_repository):
    print(day_candle_repository.get_last_date())