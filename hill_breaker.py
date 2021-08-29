import itertools
from common import *
import numpy as np
from encryptors import hill_encode


# def hill_encode(key, text, key_size=2, a_position=97, alphabet_size=26):
#     """
#
#     :param key: np.array
#     :param text: string
#     :param key_size: int
#     :param a_position: int
#     :param alphabet_size: int
#     :return: string
#     """
#
#     # splits the text into blocks the length of the key
#     text_blocks = [text[i:i+key_size] for i in range(0, len(text), key_size)]
#     encoded_text = ""
#     for block in text_blocks:
#
#         # The numerical index of the characters in the block
#         number_block = [ord(letter) - a_position for letter in block]
#
#         # the numerical indices of the block encoded with the key
#         encoded_block = (key.dot(number_block) % alphabet_size).tolist()
#         for num in encoded_block:
#             encoded_text += chr(num + a_position)
#
#     return encoded_text


def brute_force_hill(hill, word_amount=200, alphabet_size=26, words_to_compare=5, key_length=2):
    """
    Prints to console encoded text and key of a decrypted hill cipher segment if it contains at least "words_to_compare"
    number of words from the first "word_amount" most common  words in the english language. It
    iterates through all hill cipher keys of size "key_length" for every key element permutation in
    range [0, "alphabet_size"].

    :param hill: Hill object
    :param word_amount: int
    :param alphabet_size: int
    :param words_to_compare: int
    :param key_length: int
    :return: None
    """

    text = hill.text

    english = get_text('english.txt').split('\n')
    word_check = english[:word_amount]
    repeat = key_length * key_length

    def _perm_to_array(perm):
        """

        :param perm: tuple of int
        :return: np.array
        """
        index = 0
        perm_list = []
        while index < len(perm):
            perm_list.append(perm[index:index + key_length])
            index += key_length
        return np.array(perm_list)

    for permutation in itertools.product(range(alphabet_size), repeat=repeat):

        raw_encode = hill_encode(_perm_to_array(permutation), text)

        encoded_text = hill.reformat_text(raw_encode, capitals=False).split(' ')
        english_count = 0
        for word in encoded_text:
            if word in word_check:
                english_count += 1
            if english_count == words_to_compare:
                print(encoded_text)
                print(permutation)
                break
