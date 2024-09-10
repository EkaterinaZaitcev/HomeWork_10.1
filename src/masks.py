from typing import Union


def get_masks_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принятия номера карты и возрат ввиде маски"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


print(get_masks_card_number("7000792289606361"))


def get_mask_account(account: Union[str]) -> Union[str]:
    """Функция принимает номер счета и возвращает его маску"""

    return f"**{account[-4:]}"


print(get_mask_account("73654108430135874305"))
