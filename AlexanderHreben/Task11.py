# Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary.
# Dict values should be summarized in case of identical keys


def combine_dicts(*args) -> dict:
    out = dict()
    # print(args)
    # print(args[1])
    # print(args[1].items())
    for dictionary in args:
        for (key, value) in dictionary.items():
            out[key] = out.get(key, 0) + value  # if key doesnt exist return 0
    return out


if __name__ == '__main__':
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100, 'e': 555}

    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))
