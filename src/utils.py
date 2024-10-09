import json
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
