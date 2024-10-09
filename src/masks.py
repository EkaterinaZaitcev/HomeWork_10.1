import logging

from typing import Union

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s- %(levelname)s - %(message)s',
                    filename='../logs/mask.log',
                    filemode='w')

logger = logging.getLogger("mask")


def get_masks_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принятия номера карты и возврат в виде маски"""
    card_n = str(card_number)
    logger.info(f"Card mask: {card_n[:4]} {card_n[4:6]}** **** {card_n[-4:]}")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


print(get_masks_card_number("7000792289606361"))


def get_mask_account(account: Union[str]) -> Union[str]:
    """Функция принимает номер счета и возвращает его маску"""
    account_n = str(account)
    logger.info(f"Account mask: **{account_n[-4:]}")
    return f"**{account[-4:]}"


print(get_mask_account("73654108430135874305"))
