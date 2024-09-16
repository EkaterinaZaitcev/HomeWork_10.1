import pytest


@pytest.fixture
def test_get_mask_account_fix():
    return '**4305'

@pytest.fixture
def mask_account_card_fix():
    return 'Счет 64686473678894779589','Visa Platinum 7000792289606361', 'Счет 35383033474447895560'



@pytest.fixture
def get_date_fix():
    return '2024-03-11T02:26:18.671407','2025-12-11T02:26:18.671407', '2024-03-11T02:2', '2024-03-11T0255555555:26:18.671407', '6651665', '', 'hgyjd462'