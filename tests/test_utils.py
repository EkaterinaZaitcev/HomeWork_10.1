import json
from unittest.mock import patch

from src.utils import financial_transactions


@patch("builtins.open")
def test_transactions_amount_json(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value

    # Проверка на удачный результат.
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert financial_transactions("test.json") == [{"test": "test"}]

    # Проверка на ошибку типа файла.
    mock_file.read.return_value = json.dumps({})
    assert financial_transactions("test.json") == []

    # Проверка на некорректный файл.
    mock_file.read.return_value = json.dumps("testtest")
    assert financial_transactions("test.json") == []

    # Проверка на пустой файл.
    mock_file.read.return_value = ""
    assert financial_transactions("test.json") == []