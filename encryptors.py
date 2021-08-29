from lower_case_only import LowerCaseOnly
from common import *


def encrypt_rand_substitution(filename, key):
    key = key.lower()
    lower = LowerCaseOnly(filename)
    raw_text = lower.text

    a_position = 97
    alpha_nums = []
    for char in key:
        alpha_nums.append(ord(char) - a_position)
    print(alpha_nums)

    encrypted_text = ""
    for char in raw_text:
        char_num = ord(char) - a_position
        new_num = alpha_nums[char_num]
        encrypted_text += chr(new_num + a_position)

    return lower.reformat_text(encrypted_text)


def hill_encode(key, text, key_size=2, a_position=97, alphabet_size=26):
    """

    :param key: np.array
    :param text: string
    :param key_size: int
    :param a_position: int
    :param alphabet_size: int
    :return: string
    """

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


def transpose_cipher(filename, key):
    ciphertext = get_text(filename)
    text_blocks = [ciphertext[index: index + len(key)] for index in
                   range(0, len(ciphertext), len(key))]

    new_blocks = []
    for block in text_blocks:
        new_block = [''] * len(key)
        for index, shift in enumerate(key):
            new_block[index] = block[shift]
        new_blocks.append(''.join(new_block))

    return ''.join(new_blocks)
