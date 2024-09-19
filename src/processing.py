from typing import Any

states_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(states: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрации операций по ключу"""
    states_list = []
    for key in states:
        if key.get("state") == state_id:
            states_list.append(key)
    return states_list


print(filter_by_state(states_dict))


def sort_by_date(states_list: list[dict[str, Any]], revers: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки по дате"""
    sorted_list = sorted(states_list, key=lambda x: x["date"], reverse=revers)
    return sorted_list


print(sort_by_date(states_dict))
