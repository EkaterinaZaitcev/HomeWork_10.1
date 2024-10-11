import os

import pytest
from unittest.mock import patch
from src.utils import get_data_from_csv, get_data_from_excel


@patch("pandas.read_csv")
def test_get_data_from_csv(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [{'test': 'test'}]
    assert get_data_from_csv("../data/transactions.csv") != [{'test': 'test'}]


@patch("pandas.read_excel")
def test_get_transactions_from_excel(mock_read_excel):
    mock_read_excel.return_value.to_dict.return_value = [{"test": "test"}]
    assert get_data_from_excel("../data/transactions_excel.xlsx") != [{"test": "test"}]


@patch('csv.reader')
def test_get_data_from_csv(mock_reader):
    # Настраиваем mock_reader чтобы он возвращал нужный результат
    mock_reader.return_value = iter([
        ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description'],
        ['650703', 'EXECUTED', '2023-09-05T11:30:32Z', '16210', 'SoL', 'PEN', 'Счет 58803664651298323391', 'Счет 39746506635466619397', 'Перевод организации']
    ])
result = get_data_from_csv(os.path.join('patch_to_data', 'transactions.csv'))
expected_result = [
        {
          "id": "650703",
          "state": "EXECUTED",
          "date": "2023-09-05T11:30:32Z",
          "amount": "16210",
          "currency_name": "SoL",
          "currency_code": "PEN",
          "from": "Счет 58803664651298323391",
          "to": "Счет 39746506635466619397",
          "description": "Перевод организации"
        }
    ]