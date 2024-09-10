from src.masks import get_masks_card_number, get_mask_account


def mask_account_card (number:str) ->str:
    """Функция принимает и обрабатывать информацию о картах и о счетах"""
    if "Счет" in number:
        return f'{number[:4]} {get_mask_account(number)}'

    else:
        result = "".join('' if num.isdigit() else num for num in number)
        return f'{result}{get_masks_card_number(number[-16:])}'


print(mask_account_card('Maestro 1596837868705199'))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card('Visa Platinum 8990922113665229'))
print(mask_account_card('Visa Gold 5999414228426353'))
print(mask_account_card('Счет 73654108430135874305'))


def get_date(date:str) ->str|None:
    """"Меняет формат даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(get_date("2024-03-11T02:26:18.671407"))
