import pandas as pd


def get_data_for_excel(file_name: str) -> list[dict]:
    """Функция чтения файлов excel"""
    try:
        excel_data = pd.read_excel(file_name)
        data_list = excel_data.apply(
            lambda row: {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": row["amount"],
                    "currency": {
                        "name": row["currency_name"],
                        "code": row["currency_code"],
                    },
                },
                "description": row["description"],
                "from": row["from"],
                "to": row["to"],
            },
            axis=1,
        )
        new_dict=[]
        row_index = 0
        for row in data_list:
            new_dict.append(data_list[row_index])
            row_index += 1
        return new_dict
    except Exception:
        return [{}]



if __name__ == "__main__":
    result = get_data_for_excel("../data/transactions_excel.xlsx")
    print(result)