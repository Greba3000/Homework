# Implement a function which works the same as `str.split` method (without using `str.split` itself, ofcourse).


def my_split(data: str, sep=' ', quantity_split=0) -> list[str]:
    result_list = list()
    intermed_str = ''
    clear_str = " ".join(data.split())  # dell extra white space
    print(clear_str)

    for i in clear_str:
        if i == sep:
            result_list.append(intermed_str)
            intermed_str = ''
        else:
            intermed_str += i
    result_list.append(intermed_str)
    return result_list


if __name__ == '__main__':
    x = '1,,2   3***4a sd,dd d,f'
    print(x.split(','))
    print(my_split(x,','))
