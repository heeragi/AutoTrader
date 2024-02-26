from src.database.base import BaseDB
from src.upbit.api.models import DayCandle


class DayCandleRepository(BaseDB):

    def __init__(self):
        super().__init__()

    def add_bulk(self, candles: list[DayCandle]):
        sql = '''
        INSERT INTO day_candle
        (market, date, opening_price, high_price, low_price, trade_price, 
        candle_acc_trade_price, candle_acc_trade_volume, prev_closing_price, 
        change_price, change_rate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''
        params = list(map(lambda c: (
            c.market, c.candle_date_time_kst, c.opening_price, c.high_price, c.low_price, c.trade_price,
            c.candle_acc_trade_price, c.candle_acc_trade_volume, c.prev_closing_price,
            c.change_price, c.change_rate), candles))
        self.bulk_insert(sql, params)