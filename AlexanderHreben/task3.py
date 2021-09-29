# Implement a function which works the same as `str.split` method (without using `str.split` itself, ofcourse).


def my_split(data: str, sep=' ', quantity_split=-1) -> list[str]:
    assert (quantity_split > 0, f'{quantity_split} - is incorrect value for quantity split')
    result_list = list()
    temp_str = ''
    iter_split = 0
    for index, item in enumerate(data):
        if item == sep:
            result_list.append(temp_str)
            iter_split += 1
            temp_str = ''
            if quantity_split == 0:
                result_list.pop()
                result_list.append(data)
                return result_list
            elif iter_split == quantity_split:
                result_list.append(data[index + 1:])
                return result_list

        else:
            temp_str += item

    result_list.append(temp_str)
    return result_list


if __name__ == '__main__':
    x = '1,  ,2   3***4a sd,dd d,f'
    print(x.split(' ', maxsplit=-1))
    print(my_split(x, ' ', quantity_split=-1))

    print(x.split(' ', maxsplit=1))
    print(my_split(x, ' ', quantity_split=1))

    print(x.split(' ', maxsplit=0))
    print(my_split(x, ' ', quantity_split=0))


