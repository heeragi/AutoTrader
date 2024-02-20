import pytest

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
