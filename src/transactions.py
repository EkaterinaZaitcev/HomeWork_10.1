

def filter_by_currency(transactions,currency):
    """Функция, которая выводит транзакции по заданной валюте"""

    for transaction in transactions:
        if transaction['code'] == currency:
            yield transaction


"""if __name__ == "__mane__":
    result = filter_by_currency(financial_transactions("../data/operations.json"),'RUB')
    print([result])"""
