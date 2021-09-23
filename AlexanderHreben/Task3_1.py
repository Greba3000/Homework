# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.


def uni_sort_1(data: list) -> list:
    uni_sorted_data = sorted(set(data))  # sorted return list, set used for unic
    return uni_sorted_data


def uni_sort_2(data: list) -> list:
    unic_data = list()
    for elem in data:
        if elem not in unic_data:
            unic_data.append(elem)
    return sorted(unic_data)


if __name__ == '__main__':
    x = ['red', 'white', 'black', 'red', 'green', 'black']
    print(uni_sort_1(x))
    print(uni_sort_2(x))
