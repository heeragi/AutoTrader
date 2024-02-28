import sqlite3


def test_create_day_candle_table():
    con = sqlite3.connect('../../test.db')
    cur = con.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS day_candle('
        'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
        'market varchar(7), '
        'date varchar(10), '
        'opening_price float, '
        'high_price float, '
        'low_price float, '
        'trade_price float, '
        'candle_acc_trade_price float, '
        'candle_acc_trade_volume float, '
        'prev_closing_price float, '
        'change_price float, '
        'change_rate float);'
    )


def test_create_minute_candle_table():
    con = sqlite3.connect('../test.db')
    cur = con.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS minute_candle('
        'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
        'market varchar(7), '
        'date varchar(10), '
        'opening_price float, '
        'high_price float, '
        'low_price float, '
        'trade_price float, '
        'candle_acc_trade_price float, '
        'candle_acc_trade_volume float, '
        'unit float); '
    )
def test_create_week_candle_table():
    con = sqlite3.connect('../test.db')
    cur = con.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS week_candle('
        'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
        'market varchar(7), '
        'date varchar(10), '
        'opening_price float, '
        'high_price float, '
        'low_price float, '
        'trade_price float, '
        'candle_acc_trade_price float, '
        'candle_acc_trade_volume float, '
        'first_day_of_period varchar(10)); '
    )

def test_create_month_candle_table():
    con = sqlite3.connect('../test.db')
    cur = con.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS month_candle('
        'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
        'market varchar(7), '
        'date varchar(10), '
        'opening_price float, '
        'high_price float, '
        'low_price float, '
        'trade_price float, '
        'candle_acc_trade_price float, '
        'candle_acc_trade_volume float, '
        'first_day_of_period varchar(10)); '
    )