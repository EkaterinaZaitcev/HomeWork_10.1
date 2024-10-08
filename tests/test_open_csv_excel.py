import csv
from unittest.mock import patch

import pandas
from src.open_csv import get_data_for_csv
from src.open_excel import get_data_for_excel


@patch("pandas.read.csv")
def test_get_data_for_csv(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [{"test": "test"}]
    assert get_data_for_csv("test.csv") == [{"test": "test"}]
    mock_read_csv.assert_called_once_with("data/transactions.csv", encoding="utf8")


@patch("pandas.read_excel")
def test_get_transactions_from_excel(mock_read_excel, transactions):
    mock_read_excel.return_value.to_dict.return_value = transactions
    assert get_data_for_excel("data/transactions.xlsx") == transactions
    mock_read_excel.assert_called_once_with("data/transactions.xlsx")