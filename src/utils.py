import json

from json import JSONDecodeError


""" Реализуйте функцию, которая принимает на вход путь до JSON-файла и
возвращает список словарей с данными о финансовых транзакциях.
Если файл пустой, содержит не список или не найден, функция
возвращает пустой список. """

def financial_transactions ():
    """ Функция принимает на вход путь
    до JSON-файла и возвращает список словарей с данными о финансовых транзакциях. """
    try:
        with open("../data/operations.json", encoding="UTF8") as file_json:
            try:
                data = json.load(file_json)
            except JSONDecodeError:
                return []
        if not isinstance(data, list):
            return []
        return data
    except FileNotFoundError:
        return []


print(financial_transactions())

