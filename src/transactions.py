import json

from tests.test_generators import transactions


def filter_by_currency(currency):
    """Функция, которая выводит транзакции по заданной валюте"""
    with open(transactions.json) as f:
        data = json.load(f)
    for transaction in data:
        if transaction["currency"] == currency:
            yield transaction
