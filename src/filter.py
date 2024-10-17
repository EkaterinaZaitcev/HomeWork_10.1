import re

from collections import Counter


def str_sort(filtered_transactions: list[dict], word: str) -> list[dict]:
    """Функция фильтрации по строке вид операции"""
    found_operations = []
    for operation in filtered_transactions:
        if re.search(word, operation.get("description", "")):
            found_operations.append(operation)
            filtered_transactions = found_operations
        return filtered_transactions


def count_operations_by_category(list_filter: list, list_category: list) -> dict:
    """Функция фильтрует список по категориям и возвращает количество операция по категориям"""
    new_list = []
    for i in list_filter:
        if "description" in i:
            if i["description"] in list_category:
                new_list.append(i["description"])
    counted = Counter(new_list)
    return counted

