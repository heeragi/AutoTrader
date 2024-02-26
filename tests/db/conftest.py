import pytest

from src.database.day_candle_repo import DayCandleRepository
from src.upbit.api.exchange import ExchangeAPI
from src.upbit.api.quotation import QuotationAPI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

@pytest.fixture
def exchange_api():
    return ExchangeAPI()


@pytest.fixture
def quotation_api():
    return QuotationAPI()

@pytest.fixture
def day_candle_repository():
    return DayCandleRepository()