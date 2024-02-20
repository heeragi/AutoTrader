import pytest


def test_get_coin_code(quotation_api):
    '''
    GET /v1/market/all
    마켓 코드 조회
    '''
    coin_list = quotation_api.get_coin_codes()
    assert len(coin_list) > 0



