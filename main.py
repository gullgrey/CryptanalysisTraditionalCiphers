from hill_breaker import *
import numpy as np
from lower_case_only import LowerCaseOnly
from encryptors import *
from transposition_breaker import *


def find_hill_key():
    for file in ['A', 'B', 'C', 'D']:
        hill = LowerCaseOnly(file, word_number=10)
        print(get_text(file))
        brute_force_hill(hill)


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

    # lower = LowerCaseOnly('C')
    # print(lower.text)

    # print(encrypt_rand_substitution('A', 'uhnzwclbifyqvgaektdrxjomps'))
    # encrypt_rand_substitution('A', 'uhnzwclbifyqvgaektdrxjomps')

    # brute_force_trans('C', max_key_length=9)
    # bigram_check('C', max_key_size=20)
    # zig_zag_check('C')
    # elizabeth_attack('C')
    # force_final('C')
    print(transpose_cipher('C', [6, 3, 2, 0, 1, 7, 4, 5, 8, 15, 12, 11, 9, 10, 16, 13, 14, 17]))
