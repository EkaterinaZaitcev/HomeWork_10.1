import json
import csv
import pandas as pd
import logging

from json import JSONDecodeError


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="../logs/utils.log",
    filemode="w")

logger = logging.getLogger("utils")


def financial_transactions(file_json: str) -> list[dict]:
    """ Функция принимает на вход путь
    до JSON-файла и возвращает список словарей с данными о финансовых транзакциях. """
    try:
        logger.info("Получение списка транзакций")
        with open("../data/operations.json", encoding="UTF8") as file_json:
            try:
                data = json.load(file_json)
                logger.info("Список транзакций готов")
            except JSONDecodeError:
                logger.error("Ошибка декодирования")
                return []
        if not isinstance(data, list):
            logger.info("Проверка, является ли data списком")
            return []
        return data
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []


print(financial_transactions("../data/operations.json"))


def get_data_from_csv(file_name: str) -> list[dict]:
    """ Функция чтения csv файла"""
    with open(file_name, "r", encoding="utf8") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        result = []
        for row in reader:
            row_dict = dict()
            for id_x, item in enumerate(header):
                row_dict[item] = row[id_x]
            result.append(row_dict)
    return result


"""if __name__ == "__main__":
    #Проверка CSV-файла
    transactions_csv = get_data_from_csv("../data/transactions.csv")
    if transactions_csv:
        print("Список транзакций из CSV-файла:")
        for transaction in transactions_csv:
            print(transaction)
    else:
        print("Ошибка при чтении CSV-файла.")"""


def get_data_from_excel(file_name: str) -> list[dict]:
    """Функция чтения файлов excel"""
    with open(file_name, 'r', encoding='utf-8'):
        reader = pd.read_excel(file_name)
        header = pd.DataFrame(reader, columns=['id', 'state', 'data', 'amount', 'currency_name',
                                               'currency_code', 'from', 'to', 'description'])
        result = header.to_dict('records')
    return result


"""if __name__ == "__main__":
    transactions_excel = get_data_from_excel("../data/transactions_excel.xlsx")
    if transactions_excel:
        print("\nСписок транзакций из XLSX-файла:")
        for transaction in transactions_excel:
            print(transaction)
    else:
        print("Ошибка при чтении XLSX-файла.")"""
