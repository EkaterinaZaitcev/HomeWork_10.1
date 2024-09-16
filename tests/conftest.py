import pytest


@pytest.fixture
def test_get_mask_account_fix():
    return '73654108430135874305'

@pytest.fixture
def test_get_date_fix():
    return "2024-03-11T02:26:18.671407"

@pytest.fixture
def test_mask_account_card_fix():
    return "Счет 64686473678894779589"

@pytest.fixture
def state():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]
