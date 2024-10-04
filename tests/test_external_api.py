import unittest
from unittest.mock import patch

from src.external_api import currency_conversion


@patch("requests.get")
def test_currency_conversion_rub(mock_get):
    transaction = {"amount": 100, "currency": "RUB"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 100}
    assert currency_conversion(transaction) == 100


@patch("requests.get")
def test_currency_conversion_usd(mock_get):
    transaction = {"amount": 50, "currency": "USD"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 4340.0814}
    assert currency_conversion(transaction) == 4340.0814


@patch("requests.get")
def test_currency_conversion_eur(mock_get):
    transaction = {"amount": 150, "currency": "EUR"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 13974.2193}
    assert currency_conversion(transaction) == 13974.2193


@patch("requests.get")
def test_currency_conversion_unknown_currency(mock_get):
    transaction = {"amount": 100, "currency": "JPY"}
    with unittest.TestCase().assertRaises(ValueError) as context:
        currency_conversion(transaction)
        assert "Неизвестная валюта JPY." in str(context.exception)