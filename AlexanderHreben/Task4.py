# Write a Python program to sort a dictionary by key.

from operator import itemgetter


def sort_dict_1(data: dict) -> dict:
    sorted_dict = {}
    list_keys = sorted(d.keys())
    for key in list_keys:
        sorted_dict[key] = data[key]
    return sorted_dict


def sort_dict_2(data: dict) -> dict:
    sorted_dict = sorted(data.items(), key=lambda i: i[0])  # 0 - key, 1 - value
    return dict(sorted_dict)


def sort_dict_3(data: dict) -> dict:
    sorted_dict = sorted([i for i in data.items()], key=itemgetter(0))  # 0 - key, 1 - value
    return dict(sorted_dict)


if __name__ == '__main__':
    d = {2: 'two', 1: 'one', 5: 'five', 4: 'four'}
    print(sort_dict_1(d))
    print(sort_dict_2(d))
    print(sort_dict_3(d))
