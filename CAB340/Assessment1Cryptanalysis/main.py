from hill_breaker import *
import numpy as np
from lower_case_only import LowerCaseOnly


def find_hill_key():
    for file in ['A', 'B', 'C', 'D']:
        hill = LowerCaseOnly(file, word_number=10)
        print(get_ciphertext(file))
        brute_force_hill(hill, max_key_value=10)


def print_plaintext(filename, key):
    print(get_ciphertext(filename))
    hill = LowerCaseOnly(filename)
    raw_plaintext = hill_encode(key, hill.text)
    plaintext = hill.reformat_text(raw_plaintext)
    print(plaintext)


if __name__ == '__main__':
    find_hill_key()
    print_plaintext('D', np.array([[22, 19], [19, 19]]))
