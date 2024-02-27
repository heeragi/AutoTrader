import numpy as np
import pandas as pd
import talib

from src.database.day_candle_repo import DayCandleRepository


def test_query(day_candle_repository):
    print(day_candle_repository.get_list_from_date('2024-01-01', '2024-01-23'))


def test_query_with_ta(day_candle_repository):
    candles = day_candle_repository.get_list_from_date('2024-01-01', '2024-02-14')
    trade_prices = [int(candle[6]) for candle in candles]
    stock_data = pd.DataFrame({'close': np.array(trade_prices)})
    rsi = talib.RSI(stock_data['close'])
    print(rsi)
