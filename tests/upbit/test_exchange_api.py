import pytest


def test_get_accounts(exchange_api):
    my_wallets = exchange_api.get_accounts()
    assert len(my_wallets) > 0


def test_get_orders_chance(exchange_api):
    print(exchange_api.get_orders_chance())


def test_get_orders(exchange_api):
    print(exchange_api.get_orders())
