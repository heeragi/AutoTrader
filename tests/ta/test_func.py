import numpy as np
import talib

def test_ta_rsi():
    c = np.random.randn(100)
    rsi = talib.RSI(c)
    print(rsi)