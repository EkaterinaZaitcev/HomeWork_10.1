import csv


def get_data_from_csv(file_name: str) -> list[dict]:
    with open(file_name, "r", encoding="utf8") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        result = []
        for row in reader:
            row_dict = dict()
            for id_x, item in enumerate(header):
                row_dict[item] = row[id_x]
            result.append(row_dict)
    return result


"""if __name__ == "__main__":
    #Проверка CSV-файла
    transactions_csv = get_data_from_csv("../data/transactions.csv")
    if transactions_csv:
        print("Список транзакций из CSV-файла:")
        for transaction in transactions_csv:
            print(transaction)
    else:
        print("Ошибка при чтении CSV-файла.")"""
