import pytest


def test_get_accounts(exchange_api):
    my_wallets = exchange_api.get_accounts()

    print(my_wallets)

    assert len(my_wallets) > 0
