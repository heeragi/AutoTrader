from pathlib import Path

import pytest

from src.database.day_candle_repo import DayCandleRepository
from src.database.month_candle_repo import MonthCandleRepository
from src.database.minute_candle_repo import MinuteCandleRepository
from src.database.week_candle_repo import WeekCandleRepository
from src.upbit.api.exchange import ExchangeAPI
from src.upbit.api.quotation import QuotationAPI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


@pytest.fixture
def root_path():
    return Path(__file__).parent.parent

@pytest.fixture
def exchange_api():
    return ExchangeAPI()


@pytest.fixture
def quotation_api():
    return QuotationAPI()

@pytest.fixture
def day_candle_repository():
    return DayCandleRepository()

@pytest.fixture
def month_candle_repository():
    return MonthCandleRepository()


@pytest.fixture
def minute_candle_repository():
    return MinuteCandleRepository()


@pytest.fixture
def week_candle_repository():
    return WeekCandleRepository()
