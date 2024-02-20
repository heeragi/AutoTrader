import pytest
from dotenv import load_dotenv, find_dotenv

from src.api import ExchangeAPI, QuotationAPI

load_dotenv(find_dotenv())


@pytest.fixture
def exchange_api():
    return ExchangeAPI()


def test_get_accounts(exchange_api):
    print(exchange_api.get_accounts())


def test_get_coin_code(exchange_api):
    print(api.get_coin_codes())