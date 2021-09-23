# Write a Python program to print all unique values of all dictionaries in a list.


def uni_val(data: list) -> set:
    uni_value = set()  # short case - uni_value=set(val for i in d for val in i.values())
    for pair in data:
        for val in pair.values():
            uni_value.add(val)
    return uni_value


if __name__ == '__main__':
    d = [{"V": "S001", 'VI': 'S010'}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
         {"VIII": "S007"}]
    print(uni_val(d))
