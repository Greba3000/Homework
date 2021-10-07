# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.

from collections import Counter


def most_common_words(file_path: str, number_of_words=3) -> list:
    with open(file_path, 'r') as text:
        text_lines = text.readlines()  # get list

    clear_line_list = [i.strip().replace(',', '').replace('.', '').lower() for i in
                       text_lines]  # strip don't work with ','

    check_list = list()
    for line in clear_line_list:
        check_list += line.split()

    print('' in check_list, ' ' in check_list)  # where are this symbols???

    counts = Counter(check_list)
    return counts.most_common(number_of_words)


# def most_common_words_2():

if __name__ == '__main__':
    print(most_common_words('data/lorem_ipsum.txt'))
