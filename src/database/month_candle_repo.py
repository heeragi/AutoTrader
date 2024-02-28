from src.database.base import BaseDB
from src.upbit.api.models import MonthCandle


class MonthCandleRepository(BaseDB):

    def __init__(self):
        super().__init__()

    def add_bulk(self, candles: list[MonthCandle]):
        sql = '''
        INSERT INTO month_candle
        (market, date, opening_price, high_price, low_price, trade_price, 
        candle_acc_trade_price, candle_acc_trade_volume, first_day_of_period)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''
        params = list(map(lambda c: (
            c.market, c.candle_date_time_kst, c.opening_price, c.high_price, c.low_price, c.trade_price,
            c.candle_acc_trade_price, c.candle_acc_trade_volume, c.prev_closing_price,
            c.change_price, c.change_rate), candles))
        self.bulk_insert(sql, params)

    def add(self, candle: MonthCandle):
        sql = '''
        INSERT INTO week_candle
        (market, date, opening_price, high_price, low_price, trade_price, 
        candle_acc_trade_price, candle_acc_trade_volume, first_day_of_period)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''
        params = (
            candle.market, candle.candle_date_time_kst, candle.opening_price,
            candle.high_price, candle.low_price, candle.trade_price,
            candle.candle_acc_trade_price, candle.candle_acc_trade_volume,
            candle.first_day_of_period)

        return self.insert(sql, params)
    def get_list_from_date(self, start_date: str, end_date: str):
        sql = '''
        SELECT  *
        FROM    month_candle
        WHERE date BETWEEN ? AND ?
        ORDER BY ID DESC
        '''
        params = (start_date, end_date)

        return self.query(sql, params)