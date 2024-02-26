from src.database.day_candle_repo import DayCandleRepository


def test_query(day_candle_repository):
    print(day_candle_repository.get_list_from_date('2024-01-01', '2024-01-23'))
