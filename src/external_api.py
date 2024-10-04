import os
import requests
from dotenv import load_dotenv

load_dotenv()


def currency_conversion(transaction: dict) -> float:
    """Функция конвертации валют"""
    amount = float(transaction["amount"])
    currency = transaction["currency"]

    if currency == "RUB":
        return float(amount)

    elif currency == "USD" or currency == "EUR":
        api_key = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/currency_data/convert?symbols=USD,EUR&to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        data = response.json()
        return float(data["result"])

    else:
        raise ValueError(f"Неизвестная валюта {currency}.")

if __name__ == "__main__":
    transaction = {"amount": 50, "currency": "USD"}
    print(f"Сумма в рублях (USD): {currency_conversion(transaction)}")


