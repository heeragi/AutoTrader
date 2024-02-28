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

    def add(self, candle: DayCandle):
        sql = '''
        INSERT INTO day_candle
        (market, date, opening_price, high_price, low_price, trade_price, 
        candle_acc_trade_price, candle_acc_trade_volume, prev_closing_price, 
        change_price, change_rate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''
        params = (
            candle.market, candle.candle_date_time_kst, candle.opening_price,
            candle.high_price, candle.low_price, candle.trade_price,
            candle.candle_acc_trade_price, candle.candle_acc_trade_volume,
            candle.prev_closing_price, candle.change_price, candle.change_rate)

        return self.insert(sql, params)
    def get_list_from_date(self, start_date: str, end_date: str):
        sql = '''
        SELECT  *
        FROM    day_candle
        WHERE   date BETWEEN ? AND ?
        ORDER BY date DESC
        '''

        params = (start_date, end_date)

        return self.query(sql, params, size=200)

    def is_empty_date(self, date: str):
        sql = '''
        SELECT  COUNT(*)
        FROM    day_candle
        WHERE   date = ?
        '''
        result = self.scalar(sql, (date, ))[0]
        return result == 0

    def get_last_date(self):
        sql = '''
        SELECT  date
        FROM    day_candle
        ORDER BY date DESC
        LIMIT 1
        '''
        result = self.scalar(sql, None)
        return result[0]

    def get_all(self):
        sql = '''
        SELECT  *
        FROM    day_candle
        ORDER BY date DESC
        '''
        result = self.query(sql, None, size=200)
        return result