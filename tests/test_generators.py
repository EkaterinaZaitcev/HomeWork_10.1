from typing import AnyStr

import pytest

from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)

def test_filter_by_currency(transaction_list, usd_transaction):
    """Функция тестирует выдачу списка операций по названию валюты"""
    assert list(filter_by_currency(transaction_list, "USD")) == usd_transaction

def test_transaction_descriptions(transaction_list):
    """Функция тестирует выдачу списка описания операций"""
    des = transaction_descriptions(transaction_list)
    assert next(des) == "Перевод организации"
    assert next(des) == "Перевод со счета на счет"
    assert next(des) == "Перевод со счета на счет"
    assert next(des) == "Перевод с карты на карту"


@pytest.mark.parametrize("start, end", [(1, 3)])
def test_card_number_generator(start, end):
    """Функция тестирует генератор номеров карт"""
    generator_number = card_number_generator(start, end)
    assert next(generator_number) == "0000 0000 0000 0001"
    assert next(generator_number) == "0000 0000 0000 0002"
    assert next(generator_number) == "0000 0000 0000 0003"