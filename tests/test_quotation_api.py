import pytest
from dotenv import load_dotenv, find_dotenv

from src.api import QuotationAPI

load_dotenv(find_dotenv())


@pytest.fixture
def api():
    return QuotationAPI()


def test_get_coin_code(api):
    print(api.get_coin_codes())
