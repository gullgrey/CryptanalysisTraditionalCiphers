from hill_breaker import *
import numpy as np
from lower_case_only import LowerCaseOnly


def find_hill_key():
    for file in ['A', 'B', 'C', 'D']:
        hill = LowerCaseOnly(file, word_number=10)
        print(get_text(file))
        brute_force_hill(hill, max_key_value=10)


def print_plaintext(filename, key):
    print(get_text(filename))
    hill = LowerCaseOnly(filename)
    raw_plaintext = hill_encode(key, hill.text)
    plaintext = hill.reformat_text(raw_plaintext)
    save_text("DPlaintext", plaintext)
    print(plaintext)


def print_ciphertext(filename, key):
    print(get_text(filename))
    hill = LowerCaseOnly(filename)
    raw_plaintext = hill_encode(key, hill.text)
    ciphertext = hill.reformat_text(raw_plaintext)
    print(ciphertext)


if __name__ == '__main__':
    # find_hill_key()
    # print_plaintext('D', np.array([[22, 19], [19, 19]]))
    # print_ciphertext('DPlaintext', np.array([[9, 17], [17, 20]]))

    vig = LowerCaseOnly('B')
    print(vig.text)
