# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).


def character_freq(data: str) -> dict:
    character_dict = dict()
    for char in enumerate(data.lower()):
        character_dict[char[1]] = data.lower().count(char[1])
    return character_dict


if __name__ == '__main__':
    x = 'Oh, it is python'
    print(character_freq(x))
