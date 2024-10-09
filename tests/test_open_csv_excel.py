from unittest.mock import patch
from src.open_csv import get_data_from_csv
from src.open_excel import get_data_from_excel


@patch("pandas.read_csv")
def test_get_data_from_csv(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [{"test": "test"}]
    assert get_data_from_csv("../data/transactions.csv") != [{"test": "test"}]


@patch("pandas.read_excel")
def test_get_transactions_from_excel(mock_read_excel):
    mock_read_excel.return_value.to_dict.return_value = [{"test": "test"}]
    assert get_data_from_excel("../data/transactions_excel.xlsx") != [{"test": "test"}]
