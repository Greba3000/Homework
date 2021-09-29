# Implement a function which receives a string and replaces all `"` symbols with `'` and vise versa.


def replace_symb(sent: str) -> str:
    num = 0
    new_sent = list(sent)
    for letter in new_sent:
        if letter == '"':

            new_sent[num] = "'"
            num += 1
        elif letter == "'":

            new_sent[num] = '"'
            num += 1
        else:
            num += 1
    return ''.join(new_sent)


def replace_symb_2(sent: str) -> str:  # actual solution
    for letter in sent:
        if letter == '"':
            sent = sent.replace(letter, "'")
        elif letter == "'":
            sent = sent.replace(letter, '"')
    return sent


if __name__ == '__main__':
    sent = '\'sddd"dds\'sa"sdd""sdd'  # плохой пример, т.к. \ - меняет наружные кавычки, там где это невозможно выдает объект с \
    sent1 = 'sss"ss""d'
    sent2 = "sdd'dsd''s"
    sent3 = 'aaaaa\'aaa\''

    print(f'{sent} - {replace_symb(sent)}')
    print(f'{sent1} - {replace_symb_2(sent1)}')
    print(f'{sent2} - {replace_symb_2(sent2)}')
    print(f'{sent3} - {replace_symb_2(sent3)}')