# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes
# must be ignored.

def split_by_index(data: str, indexes: list[int]) -> list[str]:
    result_list = list()
    back_index = 0

    for index, value in enumerate(indexes):  # need create def clear_indexes
        if type(value) is not int:
            del indexes[index]

    for num in indexes:
        result_list.append(data[back_index:num])
        back_index = num
    return result_list


if __name__ == '__main__':
    print(split_by_index("pythoniscool,isn'tit?", [6, 'dd', 8, 12, 13, 18, 50]))
    print(split_by_index("no luck", [42]))
