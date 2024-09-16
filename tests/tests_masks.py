import pytest


from src.masks import get_masks_card_number
from src.masks import get_mask_account

def test_masks_card_number():
    """Тестирование маскировки номера карты"""
    assert get_masks_card_number("7654123443212345") == "7654 12** **** 2345"
    assert get_masks_card_number("1234123412341234") == "1234 12** **** 1234"


def test_get_mask_account(test_get_mask_account_fix):
    """Тестирование правильности маскирования номера счета"""
    assert get_mask_account(test_get_mask_account_fix) == '**4305'