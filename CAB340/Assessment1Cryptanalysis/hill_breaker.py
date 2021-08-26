import itertools

from common import *
import numpy as np


def get_hill_text(filename, words=0):
    raw_text = get_ciphertext(filename)
    space_positions = [i for i, letter in enumerate(raw_text) if letter == ' ']

    if words == 0:
        first_words = raw_text.split(" ")
        text = ''.join(first_words).lower()
        return text, space_positions
    else:
        first_words = raw_text.split(" ")[:words]
        text = ''.join(first_words).lower()
        if len(text) % 2 == 1:
            text += 'a'
        return text, space_positions[:words-1]


def space_hill_text(hill_text, space_positions):
    space_character = ' '
    text = hill_text
    for index in space_positions:
        text = text[:index] + space_character + text[index:]
    return text


def hill_encode(key, text, key_size=2, a_position=97, alphabet_size=26):

    # splits the text into blocks the length of the key
    text_blocks = [text[i:i+key_size] for i in range(0, len(text), key_size)]
    encoded_text = ""
    for block in text_blocks:

        # The numerical index of the characters in the block
        number_block = [ord(letter) - a_position for letter in block]

        # the numerical indices of the block encoded with the key
        encoded_block = (key.dot(number_block) % alphabet_size).tolist()
        for num in encoded_block:
            encoded_text += chr(num + a_position)

    return encoded_text


def brute_force_hill(hill, word_amount=200, check_limit=30, words_to_compare=5, key_length=2):

    text = hill[0]
    space_positions = hill[1]

    english = get_ciphertext('english.txt').split('\n')
    word_check = english[:word_amount]
    repeat = key_length * key_length
    # current_key = np.array([[0, 0], [0, 0]])

    def _perm_to_array(perm):
        index = 0
        perm_list = []
        while index < len(perm):
            perm_list.append(perm[index:index + key_length])
            index += key_length
        return np.array(perm_list)

    for permutation in itertools.product(range(check_limit), repeat=repeat):

        # print(permutation)
        raw_encode = hill_encode(_perm_to_array(permutation), text)
        # print(_perm_to_array(permutation))
        encoded_text = space_hill_text(raw_encode, space_positions).split(' ')
        english_count = 0
        for word in encoded_text:
            if word in word_check:
                english_count += 1
            if english_count == words_to_compare:
                print(encoded_text)
                print(permutation)
                break




