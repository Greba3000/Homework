# Implement The Keyword encoding and decoding for latin alphabet.
# The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
# Add the provided keyword at the begining of the alphabet.
# A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
# Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

import string


class Cipher:
    alphabet = list(string.ascii_uppercase)

    def __init__(self, keyword: str):
        self.keyword = list(keyword.upper())
        self.cipher_alphabet = list(string.ascii_uppercase)
        self.create_cipher_alphabet()

    def create_cipher_alphabet(self):
        for letter in reversed(self.keyword):
            self.cipher_alphabet.remove(letter)
            self.cipher_alphabet.insert(0, letter)
        return print(f'{Cipher.alphabet}\n{self.cipher_alphabet}')

    def encode(self, data: str):
        encode_str = ""
        for letter in data:
            if letter not in string.punctuation and letter != " ":
                if letter == letter.upper():
                    encode_str += self.cipher_alphabet[Cipher.alphabet.index(letter)]
                else:
                    encode_str += self.cipher_alphabet[Cipher.alphabet.index(letter.upper())].lower()
            else:
                encode_str += letter
        return print(encode_str)

    def decode(self, data: str):
        decode_str = ""
        for letter in data:
            if letter not in string.punctuation and letter != " ":
                if letter == letter.upper():
                    decode_str += Cipher.alphabet[self.cipher_alphabet.index(letter)]
                else:
                    decode_str += Cipher.alphabet[self.cipher_alphabet.index(letter.upper())].lower()
            else:
                decode_str += letter
        return print(decode_str)


if __name__ == "__main__":
    cipher1 = Cipher("crypto")
    cipher1.encode("Hello world")
    cipher1.decode("Fjedhc dn atidsn")
