import json
import re
from typing import Dict, List

from src.utils import get_data_from_csv


def filter_by_currency(transactions,currency):
    """Функция, которая выводит транзакции по заданной валюте"""

    for transaction in transactions:
        if transaction["currency"] == currency:
            yield transaction


if __name__ == "__mane__":
    result = filter_by_currency("RUB")
    print(result)



"""def sorting_transactions(search_string: str) -> List[Dict]:
    Функция для поиска операций по заданной строке
    transactions_csv = get_data_from_csv()
    pattern = rf"{search_string}"
    result_transactions = [transactions
                           for transaction in transactions_csv
                           if re.findall(pattern, transaction["description"], flags=re.IGNORECASE)]
    return result_transactions"""

"""if __name__ == "__mane__":
    result = sorting_transactions()
    print(result)"""