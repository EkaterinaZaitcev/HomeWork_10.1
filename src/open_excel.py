import pandas as pd


def get_data_from_excel(file_name: str) -> list[dict]:
    """Функция чтения файлов excel"""
    with open(file_name, 'r', encoding='utf-8'):
        reader = pd.read_excel(file_name)
        header = pd.DataFrame(reader, columns=['id', 'state', 'data', 'amount', 'currency_name',
                                               'currency_code', 'from', 'to', 'description'])
        result = header.to_dict('records')
    return result


if __name__ == "__main__":
    transactions_excel = get_data_from_excel("../data/transactions_excel.xlsx")
    if transactions_excel:
        print("\nСписок транзакций из XLSX-файла:")
        for transaction in transactions_excel:
            print(transaction)
    else:
        print("Ошибка при чтении XLSX-файла.")
