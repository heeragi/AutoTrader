from datetime import datetime

import numpy as np
import pandas as pd
import talib

from src.database.day_candle_repo import DayCandleRepository


def test_query(day_candle_repository):
    print(day_candle_repository.get_list_from_date('2024-01-01', '2024-01-23'))


def test_query_with_ta(day_candle_repository):
    candles = day_candle_repository.get_list_from_date('2023-08-01', '2024-02-26')
    trade_prices = [int(candle[6]) for candle in candles]
    stock_data = pd.DataFrame({'close': np.array(trade_prices)})
    stock_data['RSI'] = talib.RSI(stock_data['close'], 14)
    stock_data['RSI'].fillna(0, inplace=True)
    print(stock_data['RSI'])

def test_is_empty_date(day_candle_repository):
    print(str(datetime.now().date()))
    print(day_candle_repository.is_empty_date('2024-02-27'))

def test_get_date(day_candle_repository):
    print(day_candle_repository.get_last_date())