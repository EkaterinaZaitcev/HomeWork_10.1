import pytest

from src.widget import get_date, mask_account_card

def test_get_date(test_get_date_fix):
    assert get_date(test_get_date_fix) == "11.03.2024"

def test_mask_account_card(test_mask_account_card_fix):
    assert mask_account_card(test_mask_account_card_fix) == "Счет **9589"

@pytest.mark.parametrize('nums, mask', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
    ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353')
])
def test_mask_account_card(nums, mask):
    assert mask_account_card(nums) == mask

