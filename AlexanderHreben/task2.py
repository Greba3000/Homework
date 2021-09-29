# Write a function that check whether a string is a palindrome or not. Usage of any reversing functions is prohibited.


def check_pali(word: str) -> str:
    clear_word=word.lower()
    half_lenght = len(clear_word) // 2
    num = 0
    for i in range(half_lenght):
        if clear_word[i] != clear_word[-1 - i]:
            return f"{word} - is not palindrome"
        else:
            num += 1
            if num == half_lenght:
                return f"{word} - is palindrome"


if __name__ == '__main__':
    word1 = 'Summus'
    word2 = 'racecar'
    word3 = 'racer'
    word4 = 'cary'

    print(check_pali(word1))
    print(check_pali(word2))
    print(check_pali(word3))
    print(check_pali(word4))
