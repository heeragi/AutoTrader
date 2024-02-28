import numpy as np
import pandas as pd
import talib


def run_strategy(candles: tuple):
    """
    전략 예시)
    - True 인 경우 매수
    - False 인 경우 매도
    - None 인 경우 대기
    :param candles:
    :return:
    """
    closes = [candle[6] for candle in candles]
    stock_data = pd.DataFrame({'close': np.array(closes)})

    stock_data['SMA_20'] = talib.SMA(stock_data['close'], 20)
    stock_data['SMA_20'].fillna(0, inplace=True)
    stock_data['RSI_14'] = talib.RSI(stock_data['close'], 14)
    stock_data['RSI_14'].fillna(0, inplace=True)

    print(stock_data)
    #
    # for stock in stock_data['RSI_14']:
    #     print(stock)