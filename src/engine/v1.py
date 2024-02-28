from dotenv import load_dotenv, find_dotenv

from src.database.day_candle_repo import DayCandleRepository
from src.strategy.v1 import run_strategy
from src.upbit.api.quotation import QuotationAPI
from src.upbit.api.request import DayCandleRequest
from src.utils.date import diff_date, get_now_date


def run():
    candle_repo = DayCandleRepository()
    quotation_api = QuotationAPI()

    # 코인 정보가 없는 경우 불러와서 데이터 처리
    current_date = get_now_date()
    if candle_repo.is_empty_date(current_date):
        last_date_from_db = candle_repo.get_last_date()
        count = diff_date(last_date_from_db, current_date)
        if count > 0:
            candles = quotation_api.get_candles_days(DayCandleRequest(count=count))
            candle_repo.add_bulk(candles)

    candles = candle_repo.get_all()

    # 캔들 정보를 불러와 전략 실행 (매도 또는 매수 신호)
    run_strategy(candles)

    # print(stock_data)


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    run()