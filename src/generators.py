from typing import Generator


def filter_by_currency(transactions, currency) -> Generator:
    """Функция, которая выводит транзакции по заданной валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Генератор, который выводит описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start, end):
    """Функция генерирует номера карт"""
    for number in range(start, end + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number
