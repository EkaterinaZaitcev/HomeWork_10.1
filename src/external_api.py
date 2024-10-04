import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def currency_conversion(transaction: dict, response=None) -> float:
    """Функция конвертации валют"""
    amount = float(transaction["amount"])
    currency = transaction["currency"]
    if currency == "RUB":
        return float(amount)
    elif currency == "USD" or currency == "EUR":
        url = f"https://api.apilayer.com/currency_data/convert?symbols=USD,EUR&to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        print(f"Статус код: {status_code}")
        result = response.json()
        rub_amount = float(result.get("result", 0))
        return rub_amount
    else:
        raise ValueError(f"Неизвестная валюта {currency}.")



if __name__ == "__main__":

    transaction_convert = {"amount": 50, "currency": "USD"}
    print(f"Сумма в рублях (USD): {currency_conversion(transaction_convert)}")


